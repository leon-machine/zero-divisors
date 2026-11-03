"""rungs.imported-spinor-identification-witt-data-line: exact checks.

Model: the Fock model of Cl(2,4)_C on Lambda W (three modes, Gaussian-rational coefficients); conformal
model n0 = (e_+ + e_-)/2, n_inf = e_+ - e_-, X(x) = n0 + x - (1/2) Q(x) n_inf.
(1) Irreducible action: the 64 ordered blade products are independent (Cl(V_C) = M_8(C)).
(2) V_C = Lambda^2 CS: v -> M_v(Z1, Z2) = B(Z1, c(v) Z2) is an injective map to skew forms on CS with
    Pf(M_v) = -Q(v) on ten sample vectors (so Q is the wedge square for the volume functional, up to its
    normalisation), and M_v is decomposable (rank 2) exactly when v is null.
(3) Chart and Witt pair: S_omega = ker c(n_inf) and S_pi = ker c(n_0) on CS are complementary planes
    (the bivectors of the two summands are n_inf and n_0); the vectors v whose M_v has no S_omega-S_omega
    and no S_pi-S_pi block (M_v in S_omega ^ S_pi) form exactly the 4-dimensional {n0, n_inf}^perp.
    For null samples, the line of v is skew to L_inf = P(S_omega) exactly when <v, n_inf> != 0, and then
    v / <v, n_inf> = X(x) for x its spacetime part: the skew lines are the chart points.
(4) Real form: Sigma(Z1, Z2) = B(kappa Z1, Z2), kappa = Gamma c(g3) J, is Hermitian of signature (2,2) and
    the fifteen real bivectors act Sigma-anti-Hermitianly, spanning a 15-dimensional real algebra (su(2,2));
    the lines of real null vectors (X(x) at rational x, n_0, n_inf) are Sigma-null, and the lines of
    complex null vectors that are not real up to scale (X(x) at complex x, e2 + i e3) are not.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

from itertools import combinations
# ---------------------------------------------------------------------------
# Fock model of Cl(2,4)_C on Lambda W, W = span(w_0, w_1, w_2), exact over Q(i).
# Ambient orthonormal basis of R^{2,4}: index 0 e_plus (+1), 1 g0 (+1), 2 e_minus (-1),
# 3 g1, 4 g2, 5 g3 (-1).  Witt pairs: (e_plus, e_minus) -> mode 0, (g0, g1) -> mode 1,
# (g2, g3) complexified -> mode 2; c(w_i) = wedge, c(w'_i) = contraction, <w_i, w'_j> = delta_ij / 2.
# ---------------------------------------------------------------------------
QI = GA.QI
ZERO, ONE, IU = QI(0), QI(1), QI(0, 1)
SQ = (1, 1, -1, -1, -1, -1)
SUBSETS = [frozenset(s) for k in range(4) for s in combinations(range(3), k)]
IDX = {S: i for i, S in enumerate(SUBSETS)}
EVEN = [IDX[S] for S in SUBSETS if len(S) % 2 == 0]
ODD = [IDX[S] for S in SUBSETS if len(S) % 2 == 1]
FULL = frozenset(range(3))


def zmat(n=8):
    return [[ZERO] * n for _ in range(n)]


def wedge_mat(i):
    M = zmat()
    for S in SUBSETS:
        if i not in S:
            M[IDX[S | {i}]][IDX[S]] = QI((-1) ** len([j for j in S if j < i]))
    return M


def contract_mat(i):
    M = zmat()
    for S in SUBSETS:
        if i in S:
            M[IDX[S - {i}]][IDX[S]] = QI((-1) ** sorted(S).index(i))
    return M


def madd(*Ms):
    n = len(Ms[0])
    return [[sum((M[r][c] for M in Ms), ZERO) for c in range(len(Ms[0][0]))] for r in range(n)]


def mscal(c, M):
    c = QI(c) if not isinstance(c, QI) else c
    return [[c * v for v in row] for row in M]


def mmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B)) if A[i][k] and B[k][j]), ZERO)
             for j in range(len(B[0]))] for i in range(len(A))]


def mzero(M):
    return all(not v for row in M for v in row)


def apply(M, u):
    return [sum((M[r][c] * u[c] for c in range(len(u)) if M[r][c] and u[c]), ZERO) for r in range(len(M))]


CW = [wedge_mat(i) for i in range(3)]
CWP = [contract_mat(i) for i in range(3)]
CB = [madd(CW[0], CWP[0]), madd(CW[1], CWP[1]), madd(CW[0], mscal(-1, CWP[0])),
      madd(CW[1], mscal(-1, CWP[1])), madd(CW[2], mscal(-1, CWP[2])), mscal(QI(0, -1), madd(CW[2], CWP[2]))]
ID8 = [[ONE if r == c else ZERO for c in range(8)] for r in range(8)]


def c_of(v):
    """Operator of the ambient vector with coordinates v (six QI) in the orthonormal basis."""
    M = zmat()
    for a in range(6):
        if v[a]:
            M = madd(M, mscal(v[a], CB[a]))
    return M


def ip(u, v):
    return sum((SQ[a] * u[a] * v[a] for a in range(6)), ZERO)


def qv(*xs):
    return [x if isinstance(x, QI) else QI(x) for x in xs]


def annihilator(u):
    """Basis of W_u = {v in C^6 : c(v) u = 0}."""
    cols = [apply(CB[a], u) for a in range(6)]
    return GA.field_kernel([[cols[a][r] for a in range(6)] for r in range(8)])


def joint_kernel(vecs):
    rows = []
    for v in vecs:
        rows += c_of(v)
    return GA.field_kernel(rows)


def from_even(c4):
    out = [ZERO] * 8
    for k, col in enumerate(EVEN):
        out[col] = c4[k] if isinstance(c4[k], QI) else QI(c4[k])
    return out


def from_odd(c4):
    out = [ZERO] * 8
    for k, col in enumerate(ODD):
        out[col] = c4[k] if isinstance(c4[k], QI) else QI(c4[k])
    return out


def eps_sign(S):
    seq = sorted(S) + sorted(FULL - S)
    return (-1) ** sum(1 for a in range(len(seq)) for b in range(a + 1, len(seq)) if seq[a] > seq[b])


# the top-degree pairing on Lambda W, twisted by the reversal sign on the first argument
BCOEF = {S: (-1) ** (len(S) * (len(S) - 1) // 2) * eps_sign(S) for S in SUBSETS}


def bpair(p, q):
    return sum((BCOEF[S] * p[IDX[S]] * q[IDX[FULL - S]] for S in SUBSETS), ZERO)


GAMMA = [[(ONE if len(SUBSETS[r]) % 2 == 0 else -ONE) if r == c else ZERO for c in range(8)] for r in range(8)]
E8 = [[ONE if i == j else ZERO for i in range(8)] for j in range(8)]
ECS = [from_even([1 if k == i else 0 for k in range(4)]) for i in range(4)]


def conj(u):
    return [x.conj() for x in u]


def restrict_cs(M):
    """Columns of M on the even half (an 8 x 4 matrix)."""
    return [[row[c] for c in EVEN] for row in M]


def cs_kernel(v):
    """Kernel of c(v) on the conformal spinor half, as 8-vectors."""
    return [from_even(k) for k in GA.field_kernel(restrict_cs(c_of(v)))]


def skew_form(v):
    """M_v(Z1, Z2) = B(Z1, c(v) Z2) on the conformal spinor half: the bivector of v in Lambda^2 CS*."""
    C = c_of(v)
    return [[bpair(ECS[i], apply(C, ECS[j])) for j in range(4)] for i in range(4)]


def pfaff4(M):
    return M[0][1] * M[2][3] - M[0][2] * M[1][3] + M[0][3] * M[1][2]


# Witt data of the conformal model: n0 = (e_plus + e_minus)/2, ninf = e_plus - e_minus, <n0, ninf> = 1
N0 = qv(F(1, 2), 0, F(1, 2), 0, 0, 0)
NINF = qv(1, 0, -1, 0, 0, 0)


def point(x):
    """X(x) = n0 + x - (1/2) Q(x) ninf for x = (t, x1, x2, x3) (rational or Gaussian rational)."""
    xv = qv(0, x[0], 0, x[1], x[2], x[3])
    Q = ip(xv, xv)
    return [N0[a] + xv[a] - QI(F(1, 2)) * Q * NINF[a] for a in range(6)], Q

VSAMPLES = [qv(1, 0, 0, 0, 0, 0), qv(0, 0, 1, 0, 0, 0), qv(1, 2, 3, 0, 1, 5), qv(QI(1, 1), 2, 0, QI(0, 3), 1, 1),
            qv(1, 0, 1, 0, 0, 0), qv(0, 1, 0, 1, 0, 0), qv(0, 0, 0, 0, 1, QI(0, 1)), qv(2, 3, 1, 1, 2, 1),
            qv(F(1, 2), 1, F(1, 2), 1, 0, 0), qv(1, QI(2, -1), 0, 1, QI(0, 1), 3)]
REAL_POINTS = [(0, 0, 0, 0), (1, 0, 0, 0), (2, 1, 0, 0), (F(3, 2), -1, 2, F(1, 3)), (-5, 2, F(7, 4), -1)]
COMPLEX_POINTS = [(QI(0, 1), 0, 0, 0), (1, QI(0, 2), 0, 0), (QI(1, 1), 0, 1, QI(0, -1))]


def blade_product(idx):
    M = ID8
    for a in idx:
        M = mmul(M, CB[a])
    return M


def kappa(u):
    return apply(mmul(GAMMA, CB[5]), conj(u))


def sigma(z1, z2):
    return bpair(kappa(z1), z2)


def realify(H):
    A = [[x.re for x in r] for r in H]
    B = [[x.im for x in r] for r in H]
    return [A[i] + [-b for b in B[i]] for i in range(4)] + [B[i] + A[i] for i in range(4)]


def basis_vec(a):
    return qv(*[1 if b == a else 0 for b in range(6)])


def check_irreducible_and_klein_identification():
    premise("correspondence.fock-model-complexified-ascended-algebra")
    premise("correspondence.spinor-identification")
    ok = True
    rows = [[x for row in blade_product(idx) for x in row] for k in range(7) for idx in combinations(range(6), k)]
    ok = ok and GA.field_rank(rows) == 64
    for v in VSAMPLES:
        M = skew_form(v)
        ok = ok and all(M[i][j] == -M[j][i] for i in range(4) for j in range(4))
        ok = ok and pfaff4(M) == -ip(v, v)
        ok = ok and GA.field_rank(M) == (2 if ip(v, v) == ZERO else 4)
    ok = ok and GA.field_rank([[x for r in skew_form(basis_vec(a)) for x in r] for a in range(6)]) == 6
    _tp_rv = (ok); assert _tp_rv is not False, "check_irreducible_and_klein_identification"; return _tp_rv


def check_witt_pair_is_the_two_summands():
    premise("correspondence.skew-lines-splittings-hyperbolic-planes-one")
    premise("correspondence.incidence-relation-chart")
    ok = True
    S_om, S_pi = cs_kernel(NINF), cs_kernel(N0)
    ok = ok and len(S_om) == 2 and len(S_pi) == 2 and GA.field_rank(S_om + S_pi) == 4
    ok = ok and ip(N0, NINF) == ONE and ip(N0, N0) == ZERO and ip(NINF, NINF) == ZERO

    def block_functionals(v):
        C = c_of(v)
        oo = bpair(S_om[0], apply(C, S_om[1]))
        pp = bpair(S_pi[0], apply(C, S_pi[1]))
        return [oo, pp]
    # v -> (omega-omega block, pi-pi block) is linear; its kernel is {n0, n_inf}^perp
    L = [[block_functionals(basis_vec(a))[k] for a in range(6)] for k in range(2)]
    ker = GA.field_kernel(L)
    ok = ok and len(ker) == 4
    ok = ok and all(ip(k, N0) == ZERO and ip(k, NINF) == ZERO for k in ker)
    bi, b0 = block_functionals(NINF), block_functionals(N0)
    ok = ok and bi[0] == ZERO and bi[1] != ZERO and b0[0] != ZERO and b0[1] == ZERO
    # skew lines to L_inf are the chart points
    nulls = [point(x)[0] for x in REAL_POINTS + COMPLEX_POINTS] + [NINF, qv(0, 1, 0, 1, 0, 0), qv(0, 0, 0, 0, 1, QI(0, 1))]
    skew_count = 0
    for v in nulls:
        line = cs_kernel(v)
        ok = ok and len(line) == 2
        skew = GA.field_rank(line + S_om) == 4
        ok = ok and skew == (ip(v, NINF) != ZERO)
        if skew:
            skew_count += 1
            s = ip(v, NINF)
            vn = [a / s for a in v]
            x = (vn[1], vn[3], vn[4], vn[5])
            ok = ok and point(x)[0] == vn
    ok = ok and skew_count == 8
    _tp_rv = (ok); assert _tp_rv is not False, "check_witt_pair_is_the_two_summands"; return _tp_rv


def check_real_form_and_sigma_null_lines():
    premise("correspondence.reality-conjugation-twistor-form-factor")
    ok = True
    H = [[sigma(ECS[i], ECS[j]) for j in range(4)] for i in range(4)]
    ok = ok and all(H[i][j] == H[j][i].conj() for i in range(4) for j in range(4))
    ok = ok and GA.congruence_signature(realify(H)) == (4, 4, 0)
    real_algebra = []
    for a in range(6):
        for b in range(a + 1, 6):
            X = mmul(CB[a], CB[b])
            ok = ok and all(sigma(apply(X, ECS[i]), ECS[j]) + sigma(ECS[i], apply(X, ECS[j])) == ZERO
                            for i in range(4) for j in range(4))
            Xr = restrict_cs([row for k, row in enumerate(X) if k in EVEN])
            real_algebra.append([y for r in Xr for x in r for y in (x.re, x.im)])
    ok = ok and GA.rank_of_vectors(real_algebra) == 15

    def sigma_null(v):
        line = cs_kernel(v)
        return all(sigma(p, q) == ZERO for p in line for q in line)
    for x in REAL_POINTS:
        ok = ok and sigma_null(point(x)[0])
    ok = ok and sigma_null(N0) and sigma_null(NINF)
    for x in COMPLEX_POINTS:
        ok = ok and not sigma_null(point(x)[0])
    ok = ok and not sigma_null(qv(0, 0, 0, 0, 1, QI(0, 1)))
    _tp_rv = (ok); assert _tp_rv is not False, "check_real_form_and_sigma_null_lines"; return _tp_rv
