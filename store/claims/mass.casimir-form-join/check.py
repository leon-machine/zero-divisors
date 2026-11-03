"""mass.casimir-form-join: exact checks over the Gaussian rationals (GA.QI), ported from legacy
verify_T11.py (prop:casimir) and widened: clause (1) at three non-null vectors I (two frozen points of
opposite sign and one generic vector off the n_inf, n_0 plane) and for composites of one, two and
three conformal spinors; clause (2) for one, two and three constituents.

C2(W) = (1/2) g^{ac} g^{bd} M_ab M_cd is formed from the exact moment components M_ab = M_{A(e_a ^ e_b)}
in a basis of W (the spin isomorphism is solved exactly for each basis rotation); I-perp gets the
basis of the kernel of U -> <U, I>. The grip P = M(I) is built independently (Riesz vector of
U -> M_{A(U ^ I)}).
  (1) Q(P) = Q(I) (C2(Lambda^2 CS) - C2(I-perp));
  (2) C2(Lambda^2 CS) = tr(h^2) - (tr h)^2/4, h the Hermitian Gram matrix;
  (3) two spinors, I = I_Lambda (lam = Lambda/6): C2(I-perp) = (tr h)^2/4 + C - 6|B|^2/Lambda;
      and the normalisation: the grading element E = A(n_inf ^ n_0) has tr E^2 = 1.
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

T5 = [
    twistor([q(1), q(0)], [q(0), q(1)]),
    twistor([q(2, 1), q(0)], [q(1), q(1, -1)]),
    twistor([q(0), q(1, 1)], [q(3), q(2)]),
    twistor([q(1), q(2)], [q(1, 2), q(-1)]),
    twistor([q(1, -1), q(2, 1)], [q(0, 1), q(1, 1)]),
]
COMPOSITES = [[T5[1]], [T5[0], T5[1]], [T5[2], T5[3]], [T5[1], T5[3], T5[4]]]
GENERIC_I = vadd(N_0, vscal(q(3), N_INF), X_SLOT[0], vscal(q(2), X_SLOT[3]))


def perp_basis(I):
    row = [[amb_pair(I, EAMB[b]) for b in range(6)]]
    return [vadd(*[vscal(c, EAMB[b]) for b, c in enumerate(v)]) for v in GA.field_kernel(row)]


def _premises():
    premise("mass.imported-flat-model-twistor-chart-infinity")
    premise("mass.chart-form-spin-isomorphism")


def check_grip_norm_is_difference_of_casimirs():
    _premises()
    premise("mass.invariant-forms-simple-lie-algebra")
    ok = True
    for I in (i_lam(F(1, 2)), GENERIC_I):
        perp = perp_basis(I)
        ok = ok and len(perp) == 5 and all(amb_pair(u, I) == QZ for u in perp)
        for Zs in COMPOSITES[1:]:
            P = grip(Zs, I)
            ok = ok and amb_pair(P, P) == amb_pair(I, I) * (casimir(Zs, EAMB) - casimir(Zs, perp))
    ok = ok and amb_pair(GENERIC_I, GENERIC_I) == q(6 - 4)    # 2*3 from n_0.n_inf, -2 det x = -2*2
    GA.check("Q(P) = Q(I)(C2(Lambda^2 CS) - C2(I-perp))", ok)
    assert ok


def check_grip_norm_casimirs_negative_lambda_and_one_spinor():
    _premises()
    premise("mass.invariant-forms-simple-lie-algebra")
    ok = True
    I = i_lam(F(-1, 3))
    perp = perp_basis(I)
    for Zs in (COMPOSITES[0], COMPOSITES[1]):
        P = grip(Zs, I)
        ok = ok and amb_pair(P, P) == amb_pair(I, I) * (casimir(Zs, EAMB) - casimir(Zs, perp))
    ok = ok and amb_pair(I, I) == q(F(-2, 3))
    GA.check("Q(P) = Q(I)(C2 - C2(I-perp)) at Lambda < 0 and for one spinor", ok)
    assert ok


def check_conformal_casimir_is_trace_form():
    _premises()
    premise("mass.invariant-forms-simple-lie-algebra")
    ok = True
    for Zs in COMPOSITES:
        h = gram_h(Zs)
        n = len(Zs)
        tr = sum((h[i][i] for i in range(n)), QZ)
        tr2 = sum((h[i][k] * h[k][i] for i in range(n) for k in range(n)), QZ)
        ok = ok and casimir(Zs, EAMB) == tr2 - tr * tr / q(4)
    # hand value, one spinor Z = (2+i, 0; 1, 1-i): h = 2 Re((2-i)*1) = 4, C2 = 16 - 4 = 12
    ok = ok and casimir([T5[1]], EAMB) == q(12)
    GA.check("C2(Lambda^2 CS) = tr h^2 - (tr h)^2/4 for 1, 2, 3 constituents", ok)
    assert ok


def check_de_sitter_casimir_closed_form():
    _premises()
    premise("mass.exact-join")
    lam = F(1, 2)
    I = i_lam(lam)
    perp = perp_basis(I)
    ok = True
    for Zs in COMPOSITES[1:3]:
        Z1, Z2 = Zs
        h = gram_h(Zs)
        tr = h[0][0] + h[1][1]
        B = amb_pair(I, wedge2(Z1, Z2))
        C = internal_casimir(Z1, Z2)
        ok = ok and casimir(Zs, perp) == tr * tr / q(4) + C - B * B.conj() / q(lam)
    E = spin_preimage(N_INF, N_0)
    ok = ok and E == [[q(F(-1, 2)) if i == j and i < 2 else q(F(1, 2)) if i == j else QZ for j in range(4)]
                      for i in range(4)]
    ok = ok and sum((E[i][k] * E[k][i] for i in range(4) for k in range(4)), QZ) == q(1)
    GA.check("two spinors: C2(I_Lambda-perp) = (tr h)^2/4 + C - 6|B|^2/Lambda; tr E^2 = 1", ok)
    assert ok
