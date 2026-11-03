"""standard-model.imported-fock-model-twistor-space: exact checks.

Model: the Fock model of Cl(2,4)_C on Lambda W, W = span(w_0, w_1, w_2) maximal isotropic (wedge and
contraction realise the six ambient generators), Gaussian-rational coefficients throughout.
(1) Cl(V_C) = M_8(C): the six generators satisfy the Clifford relations and the 64 ordered blade
    products are independent (irreducible module); vectors are odd and the halves have dimension 4.
(2) Klein identification: v -> M_v(Z1, Z2) = B(Z1, c(v) Z2) on CS is a skew form (an element of
    Lambda^2 CS*, dual to Lambda^2 CS by the volume functional), injective on V_C, with
    Pf(M_v) = -Q(v) on ten sample vectors (real and complex), so the quadratic form is the wedge square
    up to the normalisation of epsilon; M_v has rank 2 (decomposable) exactly when v is null, rank 4
    otherwise. In the chart, ker c(n_inf) on CS is the plane S_omega (its bivector is n_inf) and
    ker c(n_0) on CS the plane S_pi, with CS = S_omega + S_pi.
(3) Reality: kappa = Gamma c(g3) J (J conjugates coefficients) is antilinear with kappa c(v) =
    c(conj v) kappa for real and complex v, swaps the halves, kappa^2 = -1; Sigma(Z1, Z2) = B(kappa Z1, Z2)
    is Hermitian on CS of signature (2,2) (its realification has signature (4,4)), and the fifteen real
    bivectors act Sigma-anti-Hermitianly, so Spin(2,4) preserves it (su(2,2)).
(4) The top-degree pairing B (degrees summing to three, reversal sign on the first argument) vanishes on
    CS x CS and CS- x CS-, is nondegenerate on CS x CS-, and is invariant under all bivectors; the
    bivector-invariant bilinear forms on the module form a 2-dimensional space (one per block), and
    asking instead that the vectors act symmetrically (which implies bivector invariance) leaves exactly
    the line of B.
The five-mode case is a separate Lemma with its own check and is not re-checked here.
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


def blade_product(idx):
    M = ID8
    for a in idx:
        M = mmul(M, CB[a])
    return M


def kappa(u):
    return apply(mmul(GAMMA, CB[5]), conj(u))


def sigma_matrix():
    return [[bpair(kappa(ECS[i]), ECS[j]) for j in range(4)] for i in range(4)]


def realify(H):
    A = [[x.re for x in r] for r in H]
    B = [[x.im for x in r] for r in H]
    return [A[i] + [-b for b in B[i]] for i in range(4)] + [B[i] + A[i] for i in range(4)]


def check_complexified_algebra_is_m8_on_fock_space():
    premise("correspondence.fock-model-complexified-ascended-algebra")
    ok = True
    for a in range(6):
        for b in range(6):
            ac = madd(mmul(CB[a], CB[b]), mmul(CB[b], CB[a]))
            ok = ok and ac == (mscal(2 * SQ[a], ID8) if a == b else zmat())
    rows = [[x for row in blade_product(idx) for x in row] for k in range(7) for idx in combinations(range(6), k)]
    ok = ok and GA.field_rank(rows) == 64
    ok = ok and len(EVEN) == 4 and len(ODD) == 4
    ok = ok and all((len(SUBSETS[r]) + len(SUBSETS[c])) % 2 == 1
                    for a in range(6) for r in range(8) for c in range(8) if CB[a][r][c])
    _tp_rv = (ok); assert _tp_rv is not False, "check_complexified_algebra_is_m8_on_fock_space"; return _tp_rv


def check_klein_identification_and_chart():
    premise("correspondence.spinor-identification")
    ok = True
    for v in VSAMPLES:
        M = skew_form(v)
        ok = ok and all(M[i][j] == -M[j][i] for i in range(4) for j in range(4))
        ok = ok and pfaff4(M) == -ip(v, v)
        r = GA.field_rank(M)
        ok = ok and r == (2 if ip(v, v) == ZERO else 4)
        # the plane of a null vector is the kernel of its operator on CS
        ok = ok and len(cs_kernel(v)) == (2 if ip(v, v) == ZERO else 0)
    # injectivity of v -> M_v on V_C
    rows = [[x for row in skew_form(qv(*[1 if b == a else 0 for b in range(6)])) for x in row] for a in range(6)]
    ok = ok and GA.field_rank(rows) == 6
    # the chart: S_omega = ker c(n_inf), S_pi = ker c(n_0), complementary
    S_om, S_pi = cs_kernel(NINF), cs_kernel(N0)
    ok = ok and len(S_om) == 2 and len(S_pi) == 2 and GA.field_rank(S_om + S_pi) == 4
    _tp_rv = (ok); assert _tp_rv is not False, "check_klein_identification_and_chart"; return _tp_rv


U_SAMPLE = qv(1, QI(0, 1), 2, 0, QI(1, 1), 0, 3, QI(0, -2))   # a generic sample spinor besides the basis E8


def check_reality_structure_and_twistor_form():
    premise("correspondence.reality-conjugation-twistor-form-factor")
    ok = True
    for v in VSAMPLES:
        vb = conj(v)
        for u in E8 + [U_SAMPLE]:
            ok = ok and kappa(apply(c_of(v), u)) == apply(c_of(vb), kappa(u))
    ok = ok and all(kappa(kappa(u)) == [-x for x in u] for u in E8)
    ok = ok and all(not kappa(z)[i] for z in ECS for i in EVEN)
    H = sigma_matrix()
    ok = ok and all(H[i][j] == H[j][i].conj() for i in range(4) for j in range(4))
    ok = ok and GA.congruence_signature(realify(H)) == (4, 4, 0)
    for a in range(len(CB)):                 # the fifteen real bivectors e_b e_a, b < a
        for b in range(a):
            X = mmul(CB[a], CB[b])
            ok = ok and all(bpair(kappa(apply(X, ECS[i])), ECS[j]) + bpair(kappa(ECS[i]), apply(X, ECS[j])) == ZERO
                            for i in range(4) for j in range(4))
    _tp_rv = (ok); assert _tp_rv is not False, "check_reality_structure_and_twistor_form"; return _tp_rv


def check_invariant_pairing_is_the_top_degree_pairing():
    premise("correspondence.fock-model-complexified-ascended-algebra")
    ok = True
    ok = ok and all(bpair(E8[i], E8[j]) == ZERO for i in EVEN for j in EVEN)
    ok = ok and all(bpair(E8[i], E8[j]) == ZERO for i in ODD for j in ODD)
    ok = ok and GA.field_rank([[bpair(E8[i], E8[j]) for j in ODD] for i in EVEN]) == 4
    # all bilinear forms beta (64 unknowns beta_ij) invariant under the bivectors
    def inv_rows(ops, sign):
        rows = []
        for X in ops:
            for i in range(8):
                for j in range(8):
                    row = [ZERO] * 64
                    for k in range(8):
                        if X[k][i]:
                            row[8 * k + j] += X[k][i]
                        if X[k][j]:
                            row[8 * i + k] += sign * X[k][j]
                    if any(row):
                        rows.append(row)
        return rows
    # the adjacent bivectors e_a e_(a+1) generate so(6), so invariance under them is invariance under all
    gens = [mmul(CB[a], CB[a + 1]) for a in range(5)]
    ker_biv = GA.field_kernel(inv_rows(gens, 1))
    ok = ok and len(ker_biv) == 2
    ker_all = GA.field_kernel(inv_rows(CB, -1))
    ok = ok and len(ker_all) == 1
    bvec = [bpair(E8[i], E8[j]) for i in range(8) for j in range(8)]
    ok = ok and GA.field_rank(ker_all + [bvec]) == 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_invariant_pairing_is_the_top_degree_pairing"; return _tp_rv
