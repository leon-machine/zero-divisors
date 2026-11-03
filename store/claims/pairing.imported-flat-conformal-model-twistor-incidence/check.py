"""pairing.imported-flat-conformal-model-twistor-incidence: exact checks.

Conventions: Cl(2,4) with orthonormal e_+ (+1), g0 (+1), e_- (-1), g1, g2, g3 (-1); n0 = (e_+ + e_-)/2,
n_inf = e_+ - e_-, <n0, n_inf> = 1, X(x) = n0 + x - (1/2) Q(x) n_inf, Q(x) = t^2 - x1^2 - x2^2 - x3^2.
(1) X(x) is null at seven sample points (real and complex). In the Fock model of Cl(2,4)_C, the
    conformal spinors whose annihilator contains X(x) are exactly ker c(X(x)) on CS, a 2-plane (a projective
    line): each spinor on it, and generic combinations, is a vacuum (3-dimensional W_u) with X(x) in W_u,
    and a spinor off the line does not have X(x) in its annihilator. Two lines meet exactly when the points
    are null-separated.
(2) Flat model (computed in the real Clifford algebra with GA): (1/2)[e_a n_inf, X(x)] = dX/dx^a =
    e_a - x_a n_inf for a = 0..3 at four points, and the translations e_a n_inf fix n_inf. The stabiliser
    of n_inf among the fifteen bivectors is 10-dimensional; it is spanned by the six spacetime bivectors
    (so(1,3)) and the four translations; the translations commute pairwise, form an ideal of the
    stabiliser, and act on vectors nilpotently in two steps (T^2 != 0, T^3 = 0): the nilradical of the
    Poincare algebra so(1,3) + R^4.
That the flat tractor connection is the ambient derivative (trivial parallel transport) is the BEG
literature input and is not checked; the computable part is (2). The -external entity is the
literature restatement and is not called.
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

POINTS = [(0, 0, 0, 0), (1, 0, 0, 0), (2, 1, 0, 0), (1, 1, 0, 0), (F(3, 2), -1, 2, F(1, 3)), (-5, 2, F(7, 4), -1),
          (QI(0, 1), 1, 0, 2)]
RPOINTS = [(0, 0, 0, 0), (2, 1, 0, 0), (F(3, 2), -1, 2, F(1, 3)), (-5, 2, F(7, 4), -1)]
SQR = (1, 1, -1, -1, -1, -1)
ST = (1, 3, 4, 5)          # spacetime indices g0, g1, g2, g3


def rvec(c):
    return {(a,): F(v) for a, v in enumerate(c) if v != 0}


RN0 = rvec((F(1, 2), 0, F(1, 2), 0, 0, 0))
RNINF = rvec((1, 0, -1, 0, 0, 0))


def rpoint(x):
    xv = rvec((0, x[0], 0, x[1], x[2], x[3]))
    Q = GA.dot(xv, xv, SQR)
    return GA.add(RN0, xv, GA.scal(-Q / 2, RNINF)), xv


def half_comm(A, B):
    return GA.scal(F(1, 2), GA.sub(GA.mul(A, B, SQR), GA.mul(B, A, SQR)))


def bivec(i, j):
    return GA.mul(GA.gen(i), GA.gen(j), SQR)


BIVS = [bivec(i, j) for i, j in combinations(range(6), 2)]
VBASIS = [GA.gen(a) for a in range(6)]


def coords(x, blades):
    return [x.get(b, F(0)) for b in blades]


def check_point_vacua_form_a_line_and_lines_meet_on_null_separation():
    premise("one-relation.imported-pure-spinors-incidence-chart")
    premise("one-relation.spacetime-manifold-vacuum-lines")
    premise("correspondence.incidence-relation-chart")
    ok = True
    lines = []
    for x in POINTS:
        X, _ = point(x)
        ok = ok and ip(X, X) == ZERO
        L = cs_kernel(X)
        ok = ok and len(L) == 2
        for u in L + [[a + 2 * b for a, b in zip(L[0], L[1])], [a - b * QI(0, 3) for a, b in zip(L[0], L[1])]]:
            Wu = annihilator(u)
            ok = ok and len(Wu) == 3 and GA.field_rank(Wu + [X]) == 3
        lines.append(L)
        # a spinor off the line (completing it to a basis of CS) does not contain X(x) in its annihilator
        off = [e for e in ECS if GA.field_rank(L + [e]) == 3][0]
        ok = ok and GA.field_rank(annihilator(off) + [X]) == 4
    met = 0
    for i in range(len(POINTS)):
        for j in range(i + 1, len(POINTS)):
            dx = [QI(POINTS[i][k]) - QI(POINTS[j][k]) for k in range(4)]
            Qd = dx[0] * dx[0] - dx[1] * dx[1] - dx[2] * dx[2] - dx[3] * dx[3]
            rk = GA.field_rank(lines[i] + lines[j])
            ok = ok and (rk == 3) == (Qd == ZERO) and rk >= 3
            met += 1 if rk == 3 else 0
    ok = ok and met == 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_point_vacua_form_a_line_and_lines_meet_on_null_separation"; return _tp_rv


def check_translations_generate_point_motion_poincare_stabiliser():
    premise("correspondence.imported-stabilisers-flat-model")
    ok = True
    for x in RPOINTS:
        X, xv = rpoint(x)
        ok = ok and GA.dot(X, X, SQR) == 0 and GA.dot(X, RNINF, SQR) == 1
        for k, a in enumerate(ST):
            ea = GA.gen(a)
            T = GA.mul(ea, RNINF, SQR)
            xa = GA.dot(ea, xv, SQR)
            ok = ok and GA.eq(half_comm(T, X), GA.sub(ea, GA.scal(xa, RNINF)))
            ok = ok and GA.is_zero(half_comm(T, RNINF))
            # derivative of X(x) along x^a by exact difference quotient of a quadratic (central difference)
            h = F(1, 3)
            xp = list(x)
            xm = list(x)
            xp[k] = F(x[k]) + h
            xm[k] = F(x[k]) - h
            dX = GA.scal(F(1) / (2 * h), GA.sub(rpoint(xp)[0], rpoint(xm)[0]))
            ok = ok and GA.eq(dX, GA.sub(ea, GA.scal(xa, RNINF)))
    # stabiliser of n_inf in so(2,4)
    vb = [(a,) for a in range(6)]
    M = [[coords(half_comm(B, RNINF), vb)[r] for B in BIVS] for r in range(6)]
    ker = GA.field_kernel(M)
    ok = ok and len(ker) == 10
    trans = [GA.mul(GA.gen(a), RNINF, SQR) for a in ST]
    lorentz = [bivec(i, j) for i, j in combinations(ST, 2)]
    bl = [b for b in GA.all_blades(6) if len(b) == 2]
    stab = [GA.add(*[GA.scal(c, B) for c, B in zip(k, BIVS) if c != 0]) for k in ker]
    stab_rows = [coords(S, bl) for S in stab]
    ok = ok and GA.rank_of_vectors(stab_rows + [coords(T, bl) for T in trans + lorentz]) == 10
    ok = ok and GA.rank_of_vectors([coords(T, bl) for T in trans + lorentz]) == 10
    # translations: abelian ideal, two-step nilpotent on vectors
    for T1 in trans:
        for T2 in trans:
            ok = ok and GA.is_zero(half_comm(T1, T2))
        for S in stab:
            c = half_comm(S, T1)
            ok = ok and GA.rank_of_vectors([coords(T, bl) for T in trans] + [coords(c, bl)]) == 4
        sq = [half_comm(T1, half_comm(T1, v)) for v in VBASIS]
        cube = [half_comm(T1, s) for s in sq]
        ok = ok and any(not GA.is_zero(s) for s in sq) and all(GA.is_zero(c) for c in cube)
    _tp_rv = (ok); assert _tp_rv is not False, "check_translations_generate_point_motion_poincare_stabiliser"; return _tp_rv
