"""one-relation.imported-pure-spinors-incidence-chart: exact checks.

Model: the Fock model of Cl(2,4)_C on Lambda W (three modes, Gaussian-rational coefficients); conformal
model n0 = (e_+ + e_-)/2, n_inf = e_+ - e_-, X(x) = n0 + x - (1/2) Q(x) n_inf.
(1) Irreducibility (64 independent blade products); for twelve sample conformal spinors u the annihilator
    W_u has dimension exactly three, is totally isotropic, and its joint kernel is C u (W_u determines u up
    to scale); non-proportional samples have distinct annihilators.
(2) Spin(6,C) = SL(4,C) on CS: the fifteen bivectors act on CS by traceless maps spanning a 15-dimensional
    space (sl(4,C)), and for each sample u the tangent space {X u} + C u is all of CS, so the vacuum orbit is
    open in P(CS) = P^3.
(3) At 2 nu = 8 purity is one quadratic condition: on the four-mode Fock space an even spinor
    a + sum b_ij w_i w_j + c w_0w_1w_2w_3 has a four-dimensional annihilator exactly when a c = Pf(b), and
    otherwise none (eight samples, both outcomes, e.g. 1 + w_0w_1w_2w_3 is not pure).
(4) X(x) is null at real and complex sample points, and with slot coefficient s in place of -1/2 the square
    is Q(x)(1 + 2s), nonzero for Q(x) != 0 unless s = -1/2. A null vector is a decomposable bivector of
    Lambda^2 CS (rank of M_v is 2, Pf(M_v) = -Q(v)) and a line of P(CS) (ker c(v) on CS has dimension 2);
    <X(x), X(y)> = -(1/2) Q(x - y), and two point lines meet exactly when the points are null-separated.
    The line of a null vector depends only on its ray (v and -v give one line, the double cover), and
    non-proportional null samples give distinct lines.
The open orbit is checked infinitesimally; the remark that this is a low-dimensional coincidence is the
contrast with (3).
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

U_SAMPLES = [(1, 0, 0, 0), (0, 0, 0, 1), (1, 1, 0, 0), (1, 2, -3, 5), (QI(1, 1), 2, QI(0, -1), 3),
             (0, 1, 1, 1), (2, 0, QI(0, 1), QI(4, -3)), (0, 1, 0, 0), (1, 0, 0, 1), (3, -1, 2, 7),
             (QI(0, 1), 0, 1, 0), (1, QI(2, 1), QI(1, -2), -1)]
POINTS = [(0, 0, 0, 0), (1, 0, 0, 0), (2, 1, 0, 0), (1, 1, 0, 0), (F(3, 2), -1, 2, F(1, 3)), (-5, 2, F(7, 4), -1),
          (QI(0, 1), 1, 0, 2)]


def blade_product(idx):
    M = ID8
    for a in idx:
        M = mmul(M, CB[a])
    return M


# four-mode Fock space for the 2 nu = 8 comparison
SUB4 = [frozenset(s) for k in range(5) for s in combinations(range(4), k)]
IX4 = {S: i for i, S in enumerate(SUB4)}


def wedge4(i, u):
    out = [ZERO] * 16
    for S in SUB4:
        if u[IX4[S]] and i not in S:
            out[IX4[S | {i}]] += u[IX4[S]] * (-1) ** len([j for j in S if j < i])
    return out


def contract4(i, u):
    out = [ZERO] * 16
    for S in SUB4:
        if u[IX4[S]] and i in S:
            out[IX4[S - {i}]] += u[IX4[S]] * (-1) ** sorted(S).index(i)
    return out


def annihilator4(u):
    cols = [wedge4(i, u) for i in range(4)] + [contract4(i, u) for i in range(4)]
    return GA.field_kernel([[cols[a][r] for a in range(8)] for r in range(16)])


def spinor4(a, b, c):
    u = [ZERO] * 16
    u[IX4[frozenset()]] = QI(a)
    u[IX4[frozenset(range(4))]] = QI(c)
    for (i, j), v in b.items():
        u[IX4[frozenset((i, j))]] = QI(v)
    return u


def pf4(b):
    g = lambda i, j: QI(b.get((i, j), 0))  # noqa: E731
    return g(0, 1) * g(2, 3) - g(0, 2) * g(1, 3) + g(0, 3) * g(1, 2)


NU4_SAMPLES = [(1, {}, 1), (1, {(0, 1): 1}, 0), (1, {(0, 1): 1, (2, 3): 1}, 1), (1, {(0, 1): 1, (2, 3): 1}, -1),
               (2, {(0, 1): 3, (2, 3): 1, (0, 2): 5}, 1), (0, {(0, 1): 1, (2, 3): 1}, 0), (0, {(0, 1): 1}, 0),
               (3, {(0, 1): 2, (1, 3): 1, (0, 2): 1, (2, 3): 5}, 3)]


def check_every_conformal_spinor_is_a_pure_vacuum():
    premise("correspondence.fock-model-complexified-ascended-algebra")
    premise("correspondence.twistors-are-states-three-ladder-pairs")
    ok = True
    rows = [[x for row in blade_product(idx) for x in row] for k in range(7) for idx in combinations(range(6), k)]
    ok = ok and GA.field_rank(rows) == 64
    anns = []
    for c4 in U_SAMPLES:
        u = from_even(c4)
        Wu = annihilator(u)
        ok = ok and len(Wu) == 3 and all(ip(x, y) == ZERO for x in Wu for y in Wu)
        jk = joint_kernel(Wu)
        ok = ok and len(jk) == 1 and GA.field_rank(jk + [u]) == 1
        anns.append(Wu)
    for i in range(len(anns)):
        for j in range(i + 1, len(anns)):
            ok = ok and GA.field_rank(anns[i] + anns[j]) > 3
    _tp_rv = (ok); assert _tp_rv is not False, "check_every_conformal_spinor_is_a_pure_vacuum"; return _tp_rv


def check_spin6_acts_as_sl4_with_open_vacuum_orbit():
    premise("correspondence.fock-model-complexified-ascended-algebra")
    ok = True
    reps = []
    for a in range(6):
        for b in range(a + 1, 6):
            X = mmul(CB[a], CB[b])
            Xc = [[X[r][c] for c in EVEN] for r in EVEN]
            ok = ok and sum((Xc[i][i] for i in range(4)), ZERO) == ZERO
            ok = ok and all(not X[r][c] for r in ODD for c in EVEN)
            reps.append((X, Xc))
    ok = ok and GA.field_rank([[x for r in Xc for x in r] for _, Xc in reps]) == 15
    for c4 in U_SAMPLES:
        u = from_even(c4)
        tangent = [apply(X, u) for X, _ in reps] + [u]
        ok = ok and GA.field_rank(tangent) == 4
    _tp_rv = (ok); assert _tp_rv is not False, "check_spin6_acts_as_sl4_with_open_vacuum_orbit"; return _tp_rv


def check_purity_is_one_quadric_at_dimension_eight():
    ok = True
    pure_count = 0
    for a, b, c in NU4_SAMPLES:
        d = len(annihilator4(spinor4(a, b, c)))
        on_quadric = QI(a) * QI(c) == pf4(b)
        ok = ok and d == (4 if on_quadric else 0)
        pure_count += 1 if d == 4 else 0
    ok = ok and pure_count == 4
    _tp_rv = (ok); assert _tp_rv is not False, "check_purity_is_one_quadric_at_dimension_eight"; return _tp_rv


def check_point_embedding_null_and_incidence_lines():
    premise("correspondence.incidence-relation-chart")
    premise("correspondence.spinor-identification")
    premise("mass.imported-flat-model-twistor-chart-infinity")
    ok = True
    lines = []
    for x in POINTS:
        X, Q = point(x)
        ok = ok and ip(X, X) == ZERO and ip(X, NINF) == ONE
        M = skew_form(X)
        ok = ok and GA.field_rank(M) == 2 and pfaff4(M) == ZERO
        L = cs_kernel(X)
        ok = ok and len(L) == 2 and mzero(mmul(c_of(X), c_of(X)))
        lines.append(L)
        # another slot coefficient s: the square is Q(x)(1 + 2s)
        xv = [X[a] + QI(F(1, 2)) * Q * NINF[a] for a in range(6)]
        for s in (F(0), F(1), F(-1), F(1, 2)):
            Xs = [xv[a] + QI(s) * Q * NINF[a] for a in range(6)]
            ok = ok and ip(Xs, Xs) == Q * QI(1 + 2 * s)
    met = 0
    for i in range(len(POINTS)):
        for j in range(i + 1, len(POINTS)):
            Xi, _ = point(POINTS[i])
            Xj, _ = point(POINTS[j])
            dx = [QI(POINTS[i][k]) - QI(POINTS[j][k]) for k in range(4)]
            d = [ZERO, dx[0], ZERO, dx[1], dx[2], dx[3]]
            Qd = ip(d, d)
            ok = ok and ip(Xi, Xj) == QI(F(-1, 2)) * Qd
            rk = GA.field_rank(lines[i] + lines[j])
            ok = ok and rk >= 3 and (rk == 3) == (Qd == ZERO)
            met += 1 if rk == 3 else 0
    ok = ok and met == 2
    # the line depends on the ray only; non-proportional null vectors give distinct lines
    nulls = [point(x)[0] for x in POINTS] + [NINF, qv(0, 1, 0, 1, 0, 0), qv(0, 0, 0, 0, 1, QI(0, 1))]
    for v in nulls:
        ok = ok and GA.field_rank(cs_kernel(v) + cs_kernel([-a for a in v])) == 2
    for i in range(len(nulls)):
        for j in range(i + 1, len(nulls)):
            ok = ok and GA.field_rank(cs_kernel(nulls[i]) + cs_kernel(nulls[j])) > 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_point_embedding_null_and_incidence_lines"; return _tp_rv
