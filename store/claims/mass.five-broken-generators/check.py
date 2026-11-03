"""mass.five-broken-generators: exact checks over the Gaussian rationals (GA.QI), ported from legacy
verify_T11.py (lem:five) and widened to five ambient vectors I (two frozen points of opposite sign,
one generic non-null vector, and two null controls).

Omega_I(u, v) = <I, u ^ v> is the 4x4 antisymmetric matrix on CS; elements of gl(CS) are the 16 matrix
units, and the conditions "Omega_I A symmetric" / "antisymmetric" are solved as exact linear systems.
  (1) det Omega_I = (Q(I)/2)^2 on every sample, so Omega_I is nondegenerate iff Q(I) != 0; the simple
      vectors I = z1 ^ z2 have Q(I) = 0 (and degenerate Omega_I).
  (2) For non-null I: {A : Omega_I A symmetric} has dimension 10, every element traceless and annihilating
      I (the stabiliser), cut out by 6 conditions; {A : Omega_I A antisymmetric} has dimension 6, contains
      the identity, and its traceless part has dimension 5; the five A(e_a ^ I), e_a a basis of I-perp,
      are traceless, lie in it, and are independent.
  (3) Real form: on the real span of n_inf, n_0 and the real slice, I_Lambda-perp has signature (1,4)
      for Lambda > 0 and (2,3) for Lambda < 0 (the stabiliser so(1,4), resp. so(2,3)).
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

GENERIC_I = vadd(N_0, vscal(q(3), N_INF), X_SLOT[0], vscal(q(2), X_SLOT[3]))
NULL_I = [N_INF, xpoint(xslot((1, 2, -1, 3)))]
REAL_BASIS = [N_INF, N_0] + [xreal(*p) for p in ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))]
UNITS = [[[QO if (r, c) == (i, j) else QZ for c in range(4)] for r in range(4)] for i in range(4) for j in range(4)]


def omega(I):
    e = [[QO if r == i else QZ for r in range(4)] for i in range(4)]
    return [[amb_pair(I, wedge2(e[i], e[j])) for j in range(4)] for i in range(4)]


def mmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(4)), QZ) for j in range(4)] for i in range(4)]


def det4(M):
    if len(M) == 1:
        return M[0][0]
    return sum((q((-1) ** c) * M[0][c] * det4([row[:c] + row[c + 1:] for row in M[1:]])
                for c in range(len(M)) if M[0][c]), QZ)


def cond_rows(Om, sym):
    rows = []
    for i in range(4):
        for j in range(4):
            if (sym and i < j) or ((not sym) and i <= j):
                row = []
                for X in UNITS:
                    OX = mmul(Om, X)
                    row.append(OX[i][j] - OX[j][i] if sym else OX[i][j] + OX[j][i])
                rows.append(row)
    return rows


def perp_basis(I):
    row = [[amb_pair(I, EAMB[b]) for b in range(6)]]
    return [vadd(*[vscal(c, EAMB[b]) for b, c in enumerate(v)]) for v in GA.field_kernel(row)]


def as_matrix(v):
    return [[v[4 * r + c] for c in range(4)] for r in range(4)]


# Ambient vectors for det Omega_I = (Q(I)/2)^2: two frozen points (Lambda > 0, < 0), a generic one, two null.
OMEGA_SAMPLES = [i_lam(F(1, 2)), i_lam(F(-1, 3)), GENERIC_I] + NULL_I
# Twistor pairs whose wedge is a simple ambient vector.
SIMPLE_PAIRS = (([q(1), q(2), q(0), q(1, 1)], [q(0), q(1), q(3), q(-1)]),
                ([q(2, 1), q(0), q(1), q(1)], [q(1), q(1), q(0, 1), q(2)]))


def check_omega_nondegenerate_iff_non_null():
    premise("mass.imported-flat-model-twistor-chart-infinity")
    premise("mass.de-sitter-scale-frozen-point")
    ok = True
    for I in OMEGA_SAMPLES:
        d = det4(omega(I))
        QI_ = amb_pair(I, I)
        ok = ok and d == QI_ * QI_ / q(4) and ((d == QZ) == (QI_ == QZ))
    for z1, z2 in SIMPLE_PAIRS:
        I = wedge2(z1, z2)
        ok = ok and amb_pair(I, I) == QZ and det4(omega(I)) == QZ
    # hand value: I = n_inf + n_0/2 has Q = 1, det Omega = 1/4
    ok = ok and det4(omega(i_lam(F(1, 2)))) == q(F(1, 4))
    GA.check("Omega_I nondegenerate iff Q(I) != 0 iff I non-simple", ok)
    assert ok


def check_stabiliser_ten_complement_five():
    premise("mass.imported-flat-model-twistor-chart-infinity")
    premise("mass.de-sitter-scale-frozen-point")
    ok = True
    for I in (i_lam(F(1, 2)), i_lam(F(-1, 3)), GENERIC_I):
        Om = omega(I)
        rs, ra = cond_rows(Om, True), cond_rows(Om, False)
        ok = ok and len(rs) == 6 and GA.field_rank(rs) == 6 and GA.field_rank(ra) == 10
        stab = GA.field_kernel(rs)
        comp = GA.field_kernel(ra)
        ok = ok and len(stab) == 10 and len(comp) == 6
        for v in stab:
            A = as_matrix(v)
            ok = ok and sum((A[i][i] for i in range(4)), QZ) == QZ and all(c == QZ for c in act(A, I))
        # the identity lies in the antisymmetric space; its traceless part has dimension 5
        ident = [QO if r == c else QZ for r in range(4) for c in range(4)]
        ok = ok and GA.field_rank(comp + [ident]) == 6
        trace_row = [[sum((v[5 * k] for k in range(4)), QZ) for v in comp]]
        ok = ok and len(GA.field_kernel(trace_row)) == 5
        five = [spin_preimage(u, I) for u in perp_basis(I)]
        for A in five:
            OA = mmul(Om, A)
            ok = ok and all(OA[i][j] + OA[j][i] == QZ for i in range(4) for j in range(4))
            ok = ok and sum((A[i][i] for i in range(4)), QZ) == QZ
        ok = ok and GA.field_rank([[A[r][c] for r in range(4) for c in range(4)] for A in five]) == 5
    GA.check("stabiliser of dimension 10; the five A(e_a ^ I) span the 5-dimensional complement", ok)
    assert ok


def check_real_form_de_sitter_and_anti_de_sitter():
    premise("mass.imported-frozen-point-tractor-connection")
    premise("mass.de-sitter-scale-frozen-point")
    ok = True
    G = [[amb_pair(u, v) for v in REAL_BASIS] for u in REAL_BASIS]
    ok = ok and all(c.im == 0 for row in G for c in row)
    ok = ok and GA.congruence_signature([[c.re for c in row] for row in G])[:2] == (2, 4)
    for lam, expected in ((F(1, 2), (1, 4)), (F(3), (1, 4)), (F(-1, 3), (2, 3))):
        I = i_lam(lam)
        # real coordinates of I-perp inside the real span: kernel of c -> <sum c_k R_k, I>
        row = [[amb_pair(R, I).re for R in REAL_BASIS]]
        ker = GA.field_kernel([[F(c) for c in row[0]]])
        ok = ok and len(ker) == 5
        vecs = [vadd(*[vscal(q(c), R) for c, R in zip(v, REAL_BASIS)]) for v in ker]
        Gp = [[amb_pair(u, v).re for v in vecs] for u in vecs]
        ok = ok and GA.congruence_signature(Gp)[:2] == expected
    GA.check("real form: I_Lambda-perp has signature (1,4) for Lambda > 0, (2,3) for Lambda < 0", ok)
    assert ok
