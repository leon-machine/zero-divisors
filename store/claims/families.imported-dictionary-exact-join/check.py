"""families.imported-dictionary-exact-join: exact checks of the imported Fact's computable content over
the Gaussian rationals (GA.QI), ported from legacy verify_T13.py (fact:dictionary) and from the T11
computations the Fact imports (rebuilt here, not imported).

lam = Lambda/6, Q(I_Lambda) = 2 lam = Lambda/3 = H^2.
  (1) The dictionary: pairing the frozen point (1, 0, J/4), J = 2 Lambda/3, with the Thomas tractor of a
      weight-w density gives m^2 = -w(w+3) Lambda/3; on the principal series -w(w+3) = nu^2 + 9/4 > 0
      (the sign with positive mass).
  (2) The exact join: B_Lambda = <pi1 pi2> + lam [omega1 omega2] = <I_Lambda, Z1 ^ Z2>, and the grip norm
      m^2 = 2|B|^2 + (Lambda/3) C on 10 pairs; C >= 0 and C = 0 exactly when the Gram matrix h is scalar.
  (3) Massless composites for Lambda > 0 are exactly B = 0 with scalar h (checked on samples and the
      examples), and composites with B = 0 and m^2 = Lambda C/3 != 0 exist (doubled composites).
  (4) The principal-series expansion: for a = x - 9/(8x), x = m/H, a^2 - (x^2 - 9/4) = 81/(64 x^2) exactly,
      so nu = m/H - (9/8) H/m + O((H/m)^3).
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
PAIRS = [(TW[i], TW[j]) for i in range(5) for j in range(i + 1, 5)]
WS = [F(1), F(-1), F(-3, 2), F(2), F(-3), F(0), F(5, 3)]
LAM_SAMPLE = F(1, 2)                                     # sample lam = Lambda/6 > 0
MASSLESS_PAIR = ([q(1), QZ, QZ, q(1)], [q(3), QZ, QZ, q(-1)])   # sample Z1 = e1 + e4, Z2 = 3 e1 - e4
DOUBLED = TW[1:4]                                          # sample twistors Z for the doubled composites (Z, Z)


def check_dictionary_sign():
    premise("mass.mass-weight-dictionary")
    ok = True
    for lam6 in (F(1, 2), F(3), F(-1, 7)):
        Lam = 6 * lam6
        J = 2 * Lam / 3
        for w in WS:
            # (sigma, Box sigma) coefficients of I . D sigma with I = (1, 0, J/4)
            a = F(-1)
            b = w * J + (J / 4) * w * (4 + 2 * w - 2)
            ok = ok and b / a == -w * (w + 3) * Lam / 3
    for nu in (F(1), F(7, 2), F(10 ** 6)):
        w = q(F(-3, 2), nu)
        prod = w * (w + q(3))
        ok = ok and -prod == q(nu * nu + F(9, 4)) and prod.re < 0
    GA.check("m^2 = -w(w+3) Lambda/3, positive on the principal series", ok)
    assert ok


def check_exact_join_and_casimir():
    premise("mass.exact-join")
    ok = True
    lam = F(1, 2)
    I = i_lam(lam)
    for (o1, p1), (o2, p2) in PAIRS:
        Z1, Z2 = twistor(o1, p1), twistor(o2, p2)
        B = amb_pair(I, wedge2(Z1, Z2))
        ok = ok and B == eps2(p1, p2) + q(lam) * eps2(o1, o2)
        PL = grip([Z1, Z2], I)
        C = internal_casimir(Z1, Z2)
        ok = ok and amb_pair(PL, PL) == q(2) * B * B.conj() + q(2 * lam) * C
        h = gram_h([Z1, Z2])
        scalar_h = h[0][1] == QZ and h[0][0] == h[1][1]
        ok = ok and C.im == 0 and C.re >= 0 and ((C == QZ) == scalar_h)
    # scalar and non-scalar Gram controls: Z1 = (1,0;1,0) has h11 = 2, Z2 = (0,1;0,1) has h22 = 2, h12 = 0
    Z1, Z2 = [q(1), QZ, q(1), QZ], [QZ, q(1), QZ, q(1)]
    ok = ok and gram_h([Z1, Z2]) == [[q(2), QZ], [QZ, q(2)]] and internal_casimir(Z1, Z2) == QZ
    GA.check("exact join m^2 = 2|B|^2 + Lambda C/3; C >= 0, zero iff h scalar", ok)
    assert ok


def check_massless_locus_and_pure_residue():
    premise("mass.exact-join")
    lam = LAM_SAMPLE
    I = i_lam(lam)
    ok = True
    # massless, not doubled: Z1 = e1 + e4, Z2 = 3 e1 - e4
    Z1, Z2 = MASSLESS_PAIR
    PL = grip([Z1, Z2], I)
    ok = ok and amb_pair(PL, PL) == QZ and amb_pair(I, wedge2(Z1, Z2)) == QZ
    ok = ok and internal_casimir(Z1, Z2) == QZ                   # h scalar (C = 0), as (3) requires
    ok = ok and any(c != QZ for c in wedge2(Z1, Z2))              # not doubled: Z1, Z2 independent
    # B = 0 with m^2 = Lambda C/3 != 0: doubled composites
    for o, p in DOUBLED:
        Z = twistor(o, p)
        PL = grip([Z, Z], I)
        C = internal_casimir(Z, Z)
        ok = ok and amb_pair(I, wedge2(Z, Z)) == QZ and C != QZ
        ok = ok and amb_pair(PL, PL) == q(2 * lam) * C
    # every sampled massive pair has B != 0 or non-scalar h
    for (o1, p1), (o2, p2) in PAIRS:
        Z1, Z2 = twistor(o1, p1), twistor(o2, p2)
        m2 = amb_pair(grip([Z1, Z2], I), grip([Z1, Z2], I))
        B = amb_pair(I, wedge2(Z1, Z2))
        ok = ok and ((m2 == QZ) == (B == QZ and internal_casimir(Z1, Z2) == QZ))
    GA.check("massless iff B = 0 and h scalar; B = 0 with m^2 = Lambda C/3 != 0 exists", ok)
    assert ok


def check_principal_series_expansion():
    premise("mass.weight-composite")
    ok = True
    for x in (F(2), F(5, 3), F(10), F(1000)):
        a = x - F(9, 8) / x
        ok = ok and (a * a - (x * x - F(9, 4))) * x * x == F(81, 64)
    root = GA.ps_pow_rat(GA.ps_trunc([F(1), F(0), F(-9, 4)], 4), F(1, 2), 4)
    ok = ok and root[2] == F(-9, 8) and root[1] == 0
    GA.check("nu = m/H - (9/8) H/m + O((H/m)^3)", ok)
    assert ok
