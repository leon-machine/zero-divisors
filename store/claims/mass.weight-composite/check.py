"""mass.weight-composite: exact checks over the Gaussian rationals (GA.QI), ported from legacy
verify_T11.py Part E (prop:weight) and widened (real-weight cases, the leading-order regime).

lam = Lambda/6 > 0, H^2 = Lambda/3 = 2 lam. The composite's m^2 is the norm of the grip P = M(I_Lambda),
computed from the spin isomorphism and the moment map (never from the closed formula).
  (1) nu^2 := m^2/H^2 - 9/4 equals 6|B_Lambda|^2/Lambda + C - 9/4 = |B|^2/lam + C - 9/4 on 7 pairs at
      two Lambda; w = -3/2 +- i nu solves -w(w+3) = m^2/H^2 (Gaussian-rational nu), real part -3/2.
  (2) The weight is real exactly when |B|^2/lam + C <= 9/4: the discriminant 9/4 - m^2/H^2 of
      w^2 + 3w + m^2/H^2 = 0 is >= 0 exactly then (a massless and two doubled composites, one with a
      real irrational pair of weights, and the principal-series pairs as controls).
  (3) Leading order: scaling the spinor parts pi -> t pi gives B ~ t^2 and C ~ t^2, and
      Im w / (sqrt 2 |B|/H) -> 1: nu^2 H^2/(2|B|^2) - 1 = lam (C - 9/4)/|B|^2 decreases to 0 like t^-2.
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

TW = [
    ([q(1), q(0)], [q(0), q(1)]),
    ([q(2, 1), q(0)], [q(1), q(1, -1)]),
    ([q(0), q(1, 1)], [q(3), q(2)]),
    ([q(1), q(2)], [q(1, 2), q(-1)]),
    ([q(1, -1), q(2, 1)], [q(0, 1), q(1, 1)]),
]
PAIRS = [(TW[0], TW[1]), (TW[0], TW[2]), (TW[1], TW[3]), (TW[2], TW[4]), (TW[3], TW[4]), (TW[1], TW[4]),
         (TW[0], TW[3])]
NUS = [F(1, 2), F(3), F(7, 5)]


def m2_over_h2(Zs, lam):
    PL = grip(Zs, i_lam(lam))
    return amb_pair(PL, PL) / q(2 * lam)


def check_induced_weight_principal_series():
    premise("mass.exact-join")
    premise("mass.weight-polynomial-two-series")
    ok = True
    for (o1, p1), (o2, p2) in PAIRS:
        Z1, Z2 = twistor(o1, p1), twistor(o2, p2)
        for lam in (F(1, 2), F(2)):
            r = m2_over_h2([Z1, Z2], lam)
            B = amb_pair(i_lam(lam), wedge2(Z1, Z2))
            nu2 = r - q(F(9, 4))
            ok = ok and nu2 == B * B.conj() / q(lam) + internal_casimir(Z1, Z2) - q(F(9, 4))
            ok = ok and nu2.im == 0
    for nu in NUS:
        for sgn in (1, -1):
            w = q(F(-3, 2), sgn * nu)
            ok = ok and -(w * (w + q(3))) == q(F(9, 4) + nu * nu) and w.re == F(-3, 2)
    # hand value: Z1 = (1,0;0,1), Z2 = (2+i,0;1,1-i), lam = 1/2: B = -1, h11 = 0, h22 = 4, h12 = 1, C = 16/4 + 1 = 5,
    # m^2/H^2 = |B|^2/lam + C = 2 + 5
    Z1, Z2 = twistor(*TW[0]), twistor(*TW[1])
    ok = ok and internal_casimir(Z1, Z2) == q(5) and m2_over_h2([Z1, Z2], F(1, 2)) == q(7)
    GA.check("nu^2 = 6|B|^2/Lambda + C - 9/4 and w = -3/2 +- i nu", ok)
    assert ok


def check_real_weight_exactly_below_threshold():
    premise("mass.exact-join")
    premise("mass.weight-polynomial-two-series")
    lam = F(1, 2)
    cases = [
        ([q(1), QZ, QZ, q(1)], [q(2), QZ, QZ, q(5)]),                          # massless, not doubled
        (twistor([q(F(1, 2)), QZ], [q(1), QZ]), twistor([q(F(1, 2)), QZ], [q(1), QZ])),  # doubled, h = 1
        (twistor([q(F(3, 4)), QZ], [q(1), QZ]), twistor([q(F(3, 4)), QZ], [q(1), QZ])),  # doubled, h = 3/2
    ] + [(twistor(*a), twistor(*b)) for a, b in PAIRS[:3]]
    ok = True
    reals = 0
    for Z1, Z2 in cases:
        r = m2_over_h2([Z1, Z2], lam)
        B = amb_pair(i_lam(lam), wedge2(Z1, Z2))
        s = B * B.conj() / q(lam) + internal_casimir(Z1, Z2)
        ok = ok and r == s and r.im == 0
        disc = F(9, 4) - r.re
        real_weight = disc >= 0
        ok = ok and real_weight == (s.re <= F(9, 4))
        reals += real_weight
    # the three below-threshold cases: m^2/H^2 = 0, 1, 9/4 (the last at the nu = 0 endpoint)
    ok = ok and reals == 3
    ok = ok and m2_over_h2(list(cases[1]), lam) == q(1) and m2_over_h2(list(cases[2]), lam) == q(F(9, 4))
    GA.check("the induced weight is real exactly when 6|B|^2/Lambda + C <= 9/4", ok)
    assert ok


# The leading-order regime: one sample pair at lam = Lambda/6 = 1/2, spinor parts scaled pi -> t pi.
LAM_LEAD = F(1, 2)
LEAD_PAIR = (TW[2], TW[4])
T_SCALE = (1, 10, 100)


def strictly_decreasing(xs):
    return all(a > b for a, b in zip(xs, xs[1:]))


def check_leading_order_im_w():
    premise("mass.exact-join")
    lam = LAM_LEAD
    (o1, p1), (o2, p2) = LEAD_PAIR
    # by hand: B_Lambda = <pi1 pi2> + lam [omega1 omega2], so pi -> t pi gives B = t^2 <pi1 pi2> + lam [omega1 omega2];
    # h is linear in pi, so C(t) = t^2 C(1). Hence rel(t) = lam (t^2 C(1) - 9/4)/|B(t)|^2 and
    # t^2 rel(t) -> L = lam C(1)/|<pi1 pi2>|^2, nonzero: the relative error decays exactly like t^-2.
    P, W = eps2(p1, p2), eps2(o1, o2)
    C1 = internal_casimir(twistor(o1, p1), twistor(o2, p2))
    ok = P != QZ and C1 != QZ and C1.im == 0
    L = lam * C1.re / (P * P.conj()).re
    rels = []
    for t in T_SCALE:
        Z1 = twistor(o1, [q(t) * c for c in p1])
        Z2 = twistor(o2, [q(t) * c for c in p2])
        B = amb_pair(i_lam(lam), wedge2(Z1, Z2))
        C = internal_casimir(Z1, Z2)
        ok = ok and B == q(t ** 2) * P + q(lam) * W and C == q(t ** 2) * C1
        nu2 = m2_over_h2([Z1, Z2], lam) - q(F(9, 4))                 # m^2 from the grip
        rel = nu2 * q(2 * lam) / (q(2) * B * B.conj()) - q(1)       # nu^2 H^2 / (2|B|^2) - 1
        ok = ok and rel == q(lam) * (C - q(F(9, 4))) / (B * B.conj())
        rels.append((t, rel.re))
    rs = [abs(r) for _, r in rels]
    errs = [abs(t * t * r - L) for t, r in rels]
    ok = ok and strictly_decreasing(rs) and strictly_decreasing(errs)
    GA.check("Im w = sqrt 2 |B|/H at leading order", ok)
    assert ok
