"""mass.exact-join: exact checks over the Gaussian rationals (GA.QI), ported from legacy
verify_T11.py Parts C-D (thm:grip) and widened (7 twistors, 21 pairs, 4 deformation values).

lam stands for Lambda/6, so I_Lambda = n_inf + lam n_0 and Q(I_Lambda) = 2 lam = Lambda/3.
  (1) B_Lambda = <I_Lambda, Z1 ^ Z2> = <pi1 pi2> + lam [omega1 omega2] on all pairs; at lam = 0 it is
      the contraction with n_inf.
  (2) The grip P = M(I_Lambda) is built from the spin isomorphism (the traceless preimage of each
      ambient rotation, solved exactly) and the moment map; Q(P) = 2|B|^2 + Q(I) C with C the internal
      su(2) Casimir, as an identity in lam (the three lam-coefficients of Q(P_inf + lam P_0) agree, and
      P_Lambda = P_inf + lam P_0 is recomputed from scratch); P is orthogonal to I.
  (3) At lam = 0, Q(P) = 2 |<pi1 pi2>|^2 = p^2 of the spinor momentum (the symplectic-area formula).
  (4) Twistors on the incidence line of x: Z1 ^ Z2 = <pi1 pi2> X(x) and B = (1 - lam Q(x)/2) <pi1 pi2>,
      which is sigma(x) = 1 - Lambda Q(x)/12.
  (5) For lam > 0: m^2 >= 0, and m^2 = 0 exactly when B = 0 and C = 0 (h scalar); the doubled
      composite has B = 0 and m^2 = 2 lam (conj(Z).Z)^2; Z1 = e1 + e4, Z2 = alpha e1 + beta e4
      (alpha != beta) is massless and not doubled. The sentence "that multiple is zero" is checked on
      its computable core: on a line with sigma(x) = 0 (det x = -1/lam) the Hermitian part of the
      incidence matrix is never definite (det <= 0 on 71 points, 0 attained), so h cannot be a nonzero scalar there.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

# ---------------------------------------------------------------------------
# Twistor core (shared text, ported from legacy/verify_T11.py Parts B-D; self-contained).
# CS = C^4 with basis e1, e2 (omega-plane) and e3, e4 (pi-plane); the ambient space is
# Lambda^2 CS in the basis e_i ^ e_j (i < j), with n_inf = e1^e2, n_0 = e3^e4 and the pairing
# <P, P'> = coefficient of e1^e2^e3^e4 in P ^ P'. Everything is over the Gaussian rationals GA.QI.
# ---------------------------------------------------------------------------
from itertools import combinations as _comb

QZ = GA.qi(0)
QO = GA.qi(1)
PAIRS4 = list(_comb(range(4), 2))


def q(re, im=0):
    return GA.qi(re, im)


def eps2(a, b):
    """<ab> = a_0 b_1 - a_1 b_0."""
    return a[0] * b[1] - a[1] * b[0]


def wedge2(z1, z2):
    return [z1[i] * z2[j] - z1[j] * z2[i] for (i, j) in PAIRS4]


def perm_sign(perm):
    s, p = 1, list(perm)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def amb_pair(P, R):
    tot = QZ
    for a, (i, j) in enumerate(PAIRS4):
        if not P[a]:
            continue
        for b, (k, l) in enumerate(PAIRS4):
            if R[b] and len({i, j, k, l}) == 4:
                tot = tot + q(perm_sign((i, j, k, l))) * P[a] * R[b]
    return tot


def biv(i, j):
    out = [QZ] * 6
    out[PAIRS4.index((min(i, j), max(i, j)))] = QO if i < j else -QO
    return out


def vadd(*us):
    return [sum((u[k] for u in us), QZ) for k in range(len(us[0]))]


def vscal(c, u):
    return [c * a for a in u]


N_INF, N_0 = biv(0, 1), biv(2, 3)
EAMB = [biv(i, j) for (i, j) in PAIRS4]
X_SLOT = [biv(0, 2), biv(0, 3), biv(1, 2), biv(1, 3)]


def twistor(om, pi):
    return [om[0], om[1], pi[0], pi[1]]


def i_lam(lam):
    """I = n_inf + lam n_0 (lam = Lambda/6)."""
    return vadd(N_INF, vscal(q(lam), N_0))


def xslot(co):
    return vadd(*[vscal(q(c), v) for c, v in zip(co, X_SLOT)])


def xpoint(x):
    """X(x) = n_0 + x - (1/2) <x,x> n_inf."""
    return vadd(N_0, x, vscal(-amb_pair(x, x) / q(2), N_INF))


def on_line(co, pi):
    """The twistor (mu_x pi, pi) on the incidence line of x = (x13, x14, x23, x24)."""
    x13, x14, x23, x24 = co
    om = [-q(x13) * pi[1] + q(x14) * pi[0], -q(x23) * pi[1] + q(x24) * pi[0]]
    return twistor(om, pi)


def act(A, P):
    """A.(u^v) = Au^v + u^Av, extended linearly to bivectors."""
    out = [QZ] * 6
    for a, (i, j) in enumerate(PAIRS4):
        if not P[a]:
            continue
        Aei = [A[r][i] for r in range(4)]
        Aej = [A[r][j] for r in range(4)]
        ei = [QO if r == i else QZ for r in range(4)]
        ej = [QO if r == j else QZ for r in range(4)]
        out = vadd(out, vscal(P[a], vadd(wedge2(Aei, ej), wedge2(ei, Aej))))
    return out


def rot(U, V, W):
    """R_{U^V}(W) = <U,W> V - <V,W> U."""
    return vadd(vscal(amb_pair(U, W), V), vscal(-amb_pair(V, W), U))


def gsolve(rows, rhs):
    """Exact solution of a consistent (possibly overdetermined) system over Q(i)."""
    m, n = len(rows), len(rows[0])
    A = [rows[i][:] + [rhs[i]] for i in range(m)]
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c]), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        inv = QO / A[r][c]
        A[r] = [x * inv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    if any(A[i][n] for i in range(r, m)):
        raise ValueError("inconsistent linear system")
    if len(piv) != n:
        raise ValueError("underdetermined linear system")
    sol = [QZ] * n
    for i, c in enumerate(piv):
        sol[c] = A[i][n]
    return sol


_UNIT_ACT = []


def _unit_act():
    if not _UNIT_ACT:
        for r in range(4):
            for c in range(4):
                A = [[QZ] * 4 for _ in range(4)]
                A[r][c] = QO
                _UNIT_ACT.append([act(A, EAMB[b]) for b in range(6)])
    return _UNIT_ACT


_SP = {}


def spin_preimage(U, V):
    """The traceless A in gl(4) whose action on Lambda^2 CS is the rotation R_{U^V} (memoised)."""
    key = tuple((c.re, c.im) for c in U + V)
    if key not in _SP:
        _SP[key] = _spin_preimage(U, V)
    return [row[:] for row in _SP[key]]


def _spin_preimage(U, V):
    ua = _unit_act()
    rows, rhs = [], []
    for b in range(6):
        target = rot(U, V, EAMB[b])
        for comp in range(6):
            rows.append([ua[k][b][comp] for k in range(16)])
            rhs.append(target[comp])
    rows.append([QO if r == c else QZ for r in range(4) for c in range(4)])
    rhs.append(QZ)
    sol = gsolve(rows, rhs)
    return [[sol[4 * r + c] for c in range(4)] for r in range(4)]


SIG = [[QO if abs(a - b) == 2 else QZ for b in range(4)] for a in range(4)]


def herm(zi, zj):
    """conj(zi)^T Sigma zj: the (2,2) Hermitian form pairing omega with conj(pi)."""
    return sum((zi[a].conj() * zj[b] for a in range(4) for b in range(4) if SIG[a][b]), QZ)


def moment(A, Zs):
    """M_A = i sum_i conj(Z_i)^T Sigma A Z_i."""
    tot = QZ
    for z in Zs:
        Az = [sum((A[r][c] * z[c] for c in range(4)), QZ) for r in range(4)]
        tot = tot + herm(z, Az)
    return GA.QI_I * tot


def gram_inverse(basis):
    n = len(basis)
    Gs = [[amb_pair(u, v) for v in basis] for u in basis]
    cols = [gsolve([row[:] for row in Gs], [QO if r == c else QZ for r in range(n)]) for c in range(n)]
    return [[cols[c][r] for c in range(n)] for r in range(n)]


_GI = []


def grip(Zs, I):
    """P = M(I): the ambient vector with <P, U> = M_{A(U ^ I)} for every U."""
    if not _GI:
        _GI.append(gram_inverse(EAMB))
    vals = [moment(spin_preimage(EAMB[a], I), Zs) for a in range(6)]
    P = [sum((vals[a] * _GI[0][a][J] for a in range(6)), QZ) for J in range(6)]
    assert all(amb_pair(P, EAMB[a]) == vals[a] for a in range(6))
    return P


def gram_h(Zs):
    return [[herm(a, b) for b in Zs] for a in Zs]


def internal_casimir(Z1, Z2):
    """C = (h11 - h22)^2/4 + |h12|^2 = tr(h_0^2)/2."""
    h11, h22, h12 = herm(Z1, Z1), herm(Z2, Z2), herm(Z1, Z2)
    return (h11 - h22) * (h11 - h22) / q(4) + h12 * h12.conj()


def casimir(Zs, basis):
    """C2(W) = (1/2) g^{ac} g^{bd} M_ab M_cd over the span of `basis`."""
    n = len(basis)
    Gi = gram_inverse(basis)
    Mm = [[moment(spin_preimage(u, v), Zs) if a != b else QZ for b, v in enumerate(basis)]
          for a, u in enumerate(basis)]
    tot = QZ
    for a in range(n):
        for b in range(n):
            if not Mm[a][b]:
                continue
            for c in range(n):
                if not Gi[a][c]:
                    continue
                for d in range(n):
                    if Gi[b][d] and Mm[c][d]:
                        tot = tot + Gi[a][c] * Gi[b][d] * Mm[a][b] * Mm[c][d]
    return tot / q(2)


def xreal(t, x_, y, z):
    """The real slice x = i K eps, K the Hermitian matrix of (t, x, y, z)."""
    K = [[q(t + z), q(x_, -y)], [q(x_, y), q(t - z)]]
    eps = [[QZ, QO], [-QO, QZ]]
    X = [[sum((K[a][b] * eps[b][c] for b in range(2)), QZ) * GA.QI_I for c in range(2)] for a in range(2)]
    return vadd(*[vscal(c_, v) for c_, v in zip((X[0][0], X[0][1], X[1][0], X[1][1]), X_SLOT)])


def in_su22(A):
    SA = [[sum((SIG[i][k] * A[k][j] for k in range(4)), QZ) for j in range(4)] for i in range(4)]
    return all(SA[i][j] + SA[j][i].conj() == QZ for i in range(4) for j in range(4))

TWISTORS = [
    ([q(1), q(0)], [q(0), q(1)]),
    ([q(2, 1), q(0)], [q(1), q(1, -1)]),
    ([q(0), q(1, 1)], [q(3), q(2)]),
    ([q(1), q(2)], [q(1, 2), q(-1)]),
    ([q(1, -1), q(2, 1)], [q(0, 1), q(1, 1)]),
    ([q(F(1, 2), 3), q(-1)], [q(2, F(-1, 3)), q(0, 4)]),
    ([q(-2), q(F(3, 4), 1)], [q(1, 1), q(F(-5, 2))]),
]
PAIRS = [(twistor(*TWISTORS[i]), twistor(*TWISTORS[j]), TWISTORS[i], TWISTORS[j])
         for i in range(len(TWISTORS)) for j in range(i + 1, len(TWISTORS))]
LAMS = [F(1, 2), F(2), F(-1, 3), F(1, 7)]
X_SAMPLES = [(1, 0, 0, 0), (1, 2, -1, 3), (0, F(1, 2), F(1, 3), -2), (2, -1, F(1, 3), 1)]


def _chart_premises():
    premise("mass.imported-flat-model-twistor-chart-infinity")
    premise("mass.de-sitter-scale-frozen-point")


def spinor_p2(p1, p2):
    """p^2 of p = pi1 conj(pi1) + pi2 conj(pi2) by the epsilon contraction."""
    p = [[p1[A] * p1[B].conj() + p2[A] * p2[B].conj() for B in range(2)] for A in range(2)]
    tot = QZ
    for A, B, s1 in ((0, 1, 1), (1, 0, -1)):
        for Ap, Bp, s2 in ((0, 1, 1), (1, 0, -1)):
            tot = tot + q(s1 * s2) * p[A][Ap] * p[B][Bp]
    return tot


def check_deformed_bracket_is_pairing_with_frozen_point():
    _chart_premises()
    ok = amb_pair(N_INF, N_0) == QO and amb_pair(N_INF, N_INF) == QZ and amb_pair(N_0, N_0) == QZ
    for lam in LAMS:
        ok = ok and amb_pair(i_lam(lam), i_lam(lam)) == q(2 * lam)
    for Z1, Z2, (o1, p1), (o2, p2) in PAIRS:
        W = wedge2(Z1, Z2)
        ok = ok and amb_pair(N_INF, W) == eps2(p1, p2) and amb_pair(N_0, W) == eps2(o1, o2)
        for lam in LAMS:
            ok = ok and amb_pair(i_lam(lam), W) == eps2(p1, p2) + q(lam) * eps2(o1, o2)
    # hand value: Z1 = (1,0;0,1), Z2 = (2+i,0;1,1-i): <pi1 pi2> = 0*(1-i) - 1*1 = -1, [w1 w2] = 0
    Z1, Z2 = twistor(*TWISTORS[0]), twistor(*TWISTORS[1])
    ok = ok and amb_pair(i_lam(F(1, 2)), wedge2(Z1, Z2)) == q(-1)
    ok = ok and amb_pair(i_lam(F(1, 2)), i_lam(F(1, 2))) == q(1)
    GA.check("B_Lambda = <pi1 pi2> + (Lambda/6)[omega1 omega2] is the pairing with I_Lambda", ok)
    assert ok


def check_mass_is_grip_norm_identity_in_lambda():
    _chart_premises()
    premise("mass.chart-form-spin-isomorphism")
    ok = True
    for Z1, Z2, (o1, p1), (o2, p2) in PAIRS[::2]:
        Pi, P0 = grip([Z1, Z2], N_INF), grip([Z1, Z2], N_0)
        C = internal_casimir(Z1, Z2)
        bp, bo = eps2(p1, p2), eps2(o1, o2)
        ok = ok and amb_pair(Pi, Pi) == q(2) * bp * bp.conj()
        ok = ok and q(2) * amb_pair(Pi, P0) == q(2) * (bp * bo.conj() + bo * bp.conj()) + q(2) * C
        ok = ok and amb_pair(P0, P0) == q(2) * bo * bo.conj()
        ok = ok and C.im == 0 and C.re >= 0
        for lam in LAMS[:2]:
            I = i_lam(lam)
            PL = grip([Z1, Z2], I)
            B = amb_pair(I, wedge2(Z1, Z2))
            m2 = amb_pair(PL, PL)
            ok = ok and PL == vadd(Pi, vscal(q(lam), P0))
            ok = ok and m2 == q(2) * B * B.conj() + amb_pair(I, I) * C and m2.im == 0
            ok = ok and amb_pair(PL, I) == QZ
    # hand value on the first pair: B = -1, C = |h12|^2 + (h11-h22)^2/4 with h11 = 0, h22 = 2 Re(conj(2+i)) = 4
    Z1, Z2 = twistor(*TWISTORS[0]), twistor(*TWISTORS[1])
    ok = ok and herm(Z2, Z2) == q(4) and herm(Z1, Z1) == q(0)
    PL = grip([Z1, Z2], i_lam(F(1, 2)))
    ok = ok and amb_pair(PL, PL) == q(2) + q(1) * internal_casimir(Z1, Z2)
    GA.check("m^2 = Q(P) = 2|B_Lambda|^2 + (Lambda/3) C, identically in Lambda", ok)
    assert ok


# Every third pair, from the second: the flat-shadow sample.
SHADOW_PAIRS = PAIRS[1::3]


def check_flat_shadow_is_symplectic_area():
    premise("mass.imported-flat-model-twistor-chart-infinity")
    premise("mass.chart-form-spin-isomorphism")
    premise("mass.mass-symplectic-area-two-twistor-formula")
    ok = True
    for Z1, Z2, (o1, p1), (o2, p2) in SHADOW_PAIRS:
        P = grip([Z1, Z2], N_INF)
        pair = amb_pair(N_INF, wedge2(Z1, Z2))
        ok = ok and amb_pair(P, P) == q(2) * pair * pair.conj()
        ok = ok and amb_pair(P, P) == spinor_p2(p1, p2)
        ok = ok and amb_pair(P, N_INF) == QZ
    GA.check("at Lambda = 0 the grip norm is 2|<pi1 pi2>|^2 = p^2", ok)
    assert ok


def check_point_supported_composite():
    premise("correspondence.incidence-relation-chart")
    premise("mass.de-sitter-scale-frozen-point")
    ok = True
    for co in X_SAMPLES:
        x = xslot(co)
        Qx = amb_pair(x, x)
        ok = ok and Qx == q(-2 * (F(co[0]) * co[3] - F(co[1]) * co[2]))
        ok = ok and amb_pair(xpoint(x), xpoint(x)) == QZ
        for (o1, p1), (o2, p2) in ((TWISTORS[0], TWISTORS[1]), (TWISTORS[2], TWISTORS[4]), (TWISTORS[5], TWISTORS[6])):
            Z1, Z2 = on_line(co, p1), on_line(co, p2)
            W = wedge2(Z1, Z2)
            ok = ok and W == vscal(eps2(p1, p2), xpoint(x))
            for lam in LAMS:
                ok = ok and amb_pair(i_lam(lam), W) == (q(1) - q(lam) * Qx / q(2)) * eps2(p1, p2)
    # hand value: x = (1,0,0,0) (x13 = 1): det x = 0, Q = 0, so sigma = 1 at every Lambda
    ok = ok and amb_pair(xslot(X_SAMPLES[0]), xslot(X_SAMPLES[0])) == QZ
    # x = (1,2,-1,3): det = 1*3 - 2*(-1) = 5, Q = -10, sigma at lam = 1/2 is 1 + 5/2 = 7/2
    x = xslot(X_SAMPLES[1])
    ok = ok and amb_pair(i_lam(F(1, 2)), xpoint(x)) == q(F(7, 2))
    GA.check("point-supported composite: Z1^Z2 = <pi1 pi2> X(x), B = sigma(x) <pi1 pi2>", ok)
    assert ok


# Positive sample value of lam = Lambda/6 for the massless-locus checks.
LAM_LOCUS = F(1, 2)
# Doubled composites Z ^ Z: four sample twistors and one with pi = 0.
DOUBLED = TWISTORS[:4] + [([q(1), q(2, 1)], [q(0), q(0)])]
# Non-doubled massless composites Z1 = e1 + e4, Z2 = alpha e1 + beta e4 (alpha != beta).
ND_Z1 = [q(1), QZ, QZ, q(1)]
ND_AB = ((q(1), q(2)), (q(3, 1), q(-2, 5)), (q(0), q(1)))
# Lines with sigma(x) = 0: the free incidence entries (x13, x14, x23), x24 solved from det x = -1/lam.
# A grid of 4 * 5 * 2 * 2 = 80 seeds (the 10 with x13 = 0 are skipped), then one anti-Hermitian
# M = i [[1, 1], [1, 3]] (det M = -2), for which K = M + M^dagger = 0 attains det K = 0.
SIGMA_ZERO_SEEDS = [(q(a, s), q(b, 1 - s), q(c, a))
                    for a in range(-2, 2) for b in range(-2, 3) for c in (1, 2) for s in (0, 1)]
SIGMA_ZERO_SEEDS.append((q(0, -1), q(0, 1), q(0, -3)))


def check_massless_locus():
    _chart_premises()
    premise("mass.chart-form-spin-isomorphism")
    lam = LAM_LOCUS
    I = i_lam(lam)
    ok = amb_pair(I, I) == q(2 * lam)
    nd_pairs = [(ND_Z1, [al, QZ, QZ, be]) for al, be in ND_AB]
    # the closed form of (2), m^2 = 2|B|^2 + Q(I) C, matched to the grip norm; m^2 >= 0 with equality
    # exactly when B = 0 and C = 0, the bound attained by the non-doubled massless pairs
    m2s = []
    for Z1, Z2 in [(Z1, Z2) for Z1, Z2, _, _ in PAIRS] + nd_pairs:
        B = amb_pair(I, wedge2(Z1, Z2))
        C = internal_casimir(Z1, Z2)
        m2 = q(2) * B * B.conj() + q(2 * lam) * C
        P = grip([Z1, Z2], I)
        ok = ok and m2 == amb_pair(P, P)
        ok = ok and m2.im == 0 and ((m2 == QZ) == (B == QZ and C == QZ))
        m2s.append(m2.re)
    ok = ok and min(m2s) == 0
    # doubled composites: B = 0, m^2 = 2 lam h^2, massless iff the constituent is null
    for o, p in DOUBLED:
        Z = twistor(o, p)
        PL = grip([Z, Z], I)
        h = herm(Z, Z)
        ok = ok and all(c == QZ for c in wedge2(Z, Z))
        ok = ok and amb_pair(PL, PL) == q(2 * lam) * h * h
        ok = ok and (amb_pair(PL, PL) == QZ) == (h == QZ)
    # non-doubled massless composites: Z1 = e1 + e4, Z2 = alpha e1 + beta e4
    for Z1, Z2 in nd_pairs:
        W = wedge2(Z1, Z2)
        PL = grip([Z1, Z2], I)
        ok = ok and any(c != QZ for c in W) and amb_pair(I, W) == QZ
        ok = ok and gram_h([Z1, Z2]) == [[QZ, QZ], [QZ, QZ]] and amb_pair(PL, PL) == QZ
    # "that multiple is zero": on lines with sigma(x) = 0, det x = -1/lam, the Hermitian part
    # K = M + M^dagger of the incidence matrix M (omega = M pi) is never definite: det K <= 0,
    # with equality attained, on 80 - 10 + 1 = 71 lines
    detx = q(-1 / lam)
    dKs = []
    for x13, x14, x23 in SIGMA_ZERO_SEEDS:
        if x13 == QZ:
            continue
        x24 = (detx + x14 * x23) / x13
        M = [[x14, -x13], [x24, -x23]]
        ok = ok and M[0][0] * M[1][1] - M[0][1] * M[1][0] == detx
        K = [[M[i][j] + M[j][i].conj() for j in range(2)] for i in range(2)]
        dK = K[0][0] * K[1][1] - K[0][1] * K[1][0]
        ok = ok and dK.im == 0
        dKs.append(dK.re)
    ok = ok and len(dKs) == 71 and max(dKs) == 0
    GA.check("massless locus: B = 0 and h = 0; doubled and non-doubled examples", ok)
    assert ok
