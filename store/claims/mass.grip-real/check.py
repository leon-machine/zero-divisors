"""mass.grip-real: exact checks over the Gaussian rationals (GA.QI), ported from legacy verify_T11.py
(lem:real) and widened (more real pairs, three frozen points, the real coordinates of P computed).

V_R is the real span of n_inf, n_0 and the real slice x = i K eps (K Hermitian; the slice's 1/sqrt 2 is
dropped, which rescales and does not affect reality). Sigma is the (2,2) Hermitian form of CS pairing
omega with conj(pi) (the reversion form, the twistor form); su(2,2) = {A : Sigma A anti-Hermitian}.
  (1) A(U ^ V) is in su(2,2) for all 15 pairs of the six real basis vectors and for real combinations;
      the commutator identity [A(x ^ n_inf), A(y ^ n_0)] = <x,y> A(n_inf ^ n_0) + A(x ^ y) holds.
  (2) Hence M_{U ^ V} is real on composites of one, two and three spinors.
  (3) For I in V_R the grip P = M(I) has real coordinates in the real basis (Gram matrix real, pairings
      real), so P is in V_R; for I_Lambda it is orthogonal to I_Lambda, and Q(P) is the value of the
      real form on I_Lambda-perp, of signature (1,4), at P's real coordinates.
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

REAL_PTS = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
REAL_BASIS = [N_INF, N_0] + [xreal(*p) for p in REAL_PTS]
MIXED = [vadd(xreal(3, 1, -2, 5), vscal(q(2), N_INF)), vadd(xreal(2, -1, 1, 1), vscal(q(-1), N_0))]
T5 = [
    twistor([q(1), q(0)], [q(0), q(1)]),
    twistor([q(2, 1), q(0)], [q(1), q(1, -1)]),
    twistor([q(0), q(1, 1)], [q(3), q(2)]),
    twistor([q(1), q(2)], [q(1, 2), q(-1)]),
    twistor([q(1, -1), q(2, 1)], [q(0, 1), q(1, 1)]),
]
COMPOSITES = [[T5[2]], [T5[0], T5[1]], [T5[3], T5[4]], [T5[1], T5[2], T5[4]]]


def comm(A, B):
    AB = [[sum((A[i][k] * B[k][j] for k in range(4)), QZ) for j in range(4)] for i in range(4)]
    BA = [[sum((B[i][k] * A[k][j] for k in range(4)), QZ) for j in range(4)] for i in range(4)]
    return [[AB[i][j] - BA[i][j] for j in range(4)] for i in range(4)]


def real_coords(P):
    G = [[amb_pair(u, v) for v in REAL_BASIS] for u in REAL_BASIS]
    rhs = [amb_pair(P, u) for u in REAL_BASIS]
    return gsolve(G, rhs)


def check_real_pairs_generate_su22():
    premise("correspondence.reality-conjugation-twistor-form-factor")
    premise("mass.chart-form-spin-isomorphism")
    premise("mass.imported-flat-model-twistor-chart-infinity")
    ok = True
    vecs = REAL_BASIS + MIXED
    for a in range(len(vecs)):
        for b in range(a + 1, len(vecs)):
            ok = ok and in_su22(spin_preimage(vecs[a], vecs[b]))
    # a complex multiple of a real pair is not in su(2,2): the condition is not vacuous
    ok = ok and not in_su22(spin_preimage(vscal(GA.QI_I, REAL_BASIS[2]), REAL_BASIS[3]))
    Agr = spin_preimage(N_INF, N_0)
    for v in REAL_BASIS[2:]:
        for w in REAL_BASIS[2:]:
            lhs = comm(spin_preimage(v, N_INF), spin_preimage(w, N_0))
            Axy = spin_preimage(v, w)
            xy = amb_pair(v, w)
            ok = ok and lhs == [[xy * Agr[i][j] + Axy[i][j] for j in range(4)] for i in range(4)]
    # hand value: the real slice point (1,0,0,0) has Q = 2 (t^2 with the dropped 1/sqrt 2)
    ok = ok and amb_pair(REAL_BASIS[2], REAL_BASIS[2]) == q(2)
    GA.check("real pairs generate su(2,2)", ok)
    assert ok


# Real pair (U, V) whose rotation, multiplied by i, is the non-real control generator.
CONTROL_PAIR = (REAL_BASIS[2], REAL_BASIS[3])


def check_moments_of_real_pairs_are_real():
    premise("correspondence.reality-conjugation-twistor-form-factor")
    premise("mass.chart-form-spin-isomorphism")
    ok = True
    vecs = REAL_BASIS + MIXED
    for Zs in COMPOSITES:
        for u, v in _comb(vecs, 2):
            ok = ok and moment(spin_preimage(u, v), Zs).im == 0
    # control: A(iU ^ V) = i A(U ^ V) is not real; its moments are exactly i times the real moments
    # of A(U ^ V), and these are nonzero on some composite
    U, V = CONTROL_PAIR
    A = spin_preimage(vscal(GA.QI_I, U), V)
    A_real = spin_preimage(U, V)
    real_moments = [moment(A_real, Zs) for Zs in COMPOSITES]
    ok = ok and (len(COMPOSITES) == len(real_moments) and all(moment(A, Zs) == GA.QI_I * m for Zs, m in zip(COMPOSITES, real_moments)))
    ok = ok and any(m != QZ for m in real_moments)
    GA.check("moments of real pairs are real", ok)
    assert ok


def check_grip_on_frozen_point_is_real_vector_of_one_four_form():
    premise("mass.chart-form-spin-isomorphism")
    premise("mass.imported-flat-model-twistor-chart-infinity")
    premise("mass.imported-frozen-point-tractor-connection")
    ok = True
    for lam in (F(1, 2), F(3), F(1, 7)):
        I = i_lam(lam)
        row = [amb_pair(R, I).re for R in REAL_BASIS]
        ker = GA.field_kernel([[F(c) for c in row]])
        perp = [vadd(*[vscal(q(c), R) for c, R in zip(v, REAL_BASIS)]) for v in ker]
        Gp = [[amb_pair(u, v) for v in perp] for u in perp]
        ok = ok and len(perp) == 5 and GA.congruence_signature([[c.re for c in r] for r in Gp])[:2] == (1, 4)
        for Zs in COMPOSITES[1:]:
            P = grip(Zs, I)
            c = real_coords(P)
            ok = ok and all(x.im == 0 for x in c)
            ok = ok and P == vadd(*[vscal(x, R) for x, R in zip(c, REAL_BASIS)])
            ok = ok and amb_pair(P, I) == QZ
            # coordinates of P in the real basis of I-perp, and Q(P) as the (1,4) form's value
            d = gsolve([r[:] for r in Gp], [amb_pair(P, u) for u in perp])
            ok = ok and all(x.im == 0 for x in d)
            val = sum((d[i] * Gp[i][j] * d[j] for i in range(5) for j in range(5)), QZ)
            ok = ok and val == amb_pair(P, P) and val.im == 0
    # control: a complex frozen point gives a grip off the real span
    P = grip(COMPOSITES[1], vadd(N_INF, vscal(q(0, 1), N_0)))
    ok = ok and any(x.im != 0 for x in real_coords(P))
    GA.check("the grip on I_Lambda is a real vector of the (1,4) space", ok)
    assert ok
