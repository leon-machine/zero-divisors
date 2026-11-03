"""pairing.displacement-pairs-point-mode-vacuum-parallel: exact checks.

Conventions: C^6 = V_C with orthonormal e_+ (+1), g0 (+1), e_- (-1), g1, g2, g3 (-1); n0 = (e_+ + e_-)/2,
n_inf = e_+ - e_-, X(x) = n0 + x - (1/2) Q(x) n_inf; l = g0 + g1, n = g0 - g1, m = g2 + i g3, mb = g2 - i g3;
lifts l(x) = l - <x, l> n_inf, m(x) = m - <x, m> n_inf; W(x) = span(X(x), l(x), m(x)). Bivectors act on
vectors by (u ^ v).w = <v, w> u - <u, w> v, which is checked against (1/2)[u v, w] in GA on all basis
bivectors and vectors.
(1) W(x) is totally isotropic of dimension three at four rational points; (1/2)[e_a n_inf, X(x)] =
    e_a - x_a n_inf, (1/2)[e_a n_inf, n_inf] = 0, and X(x + dx) - X(x) - dx^a d_a X = -(1/2) Q(dx) n_inf.
(2) The pairing classes (<Om(dx).X, l(x)>, <Om(dx).X, m(x)>, <Om(dx).l(x), m(x)>) equal
    (<dx, l>, <dx, m>, 0) for twelve displacements at each point (real, the named ones, complex m and mb);
    the classes of mb are (0, -2, 0) and those of m vanish; on real displacements the three classes vanish
    exactly on the line R l (the real kernel of (<dx,l>, Re<dx,m>, Im<dx,m>) is one-dimensional, spanned by l).
(3) Incidence: X(x + s l) = X(x) + s l(x) in W(x) for three values of s.
(4) The stabiliser {B in so(6,C) : B.W(x) in W(x)} has dimension 12, cut out by the three class
    functionals (rank 3); in the Fock model the bivectors fixing the ray of the vacuum of W(x) form the same
    12-dimensional space.
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

SQR = (1, 1, -1, -1, -1, -1)
ST = (1, 3, 4, 5)
RPOINTS = [(0, 0, 0, 0), (2, 1, 0, 0), (F(3, 2), -1, 2, F(1, 3)), (-5, 2, F(7, 4), -1)]
DISPLACEMENTS = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (1, 1, 0, 0), (1, -1, 0, 0),
                 (F(2, 3), -1, 5, F(1, 2)), (-3, F(7, 5), 2, -1), (4, 1, F(-1, 3), 2), (1, 2, 3, 4),
                 (0, 0, 1, QI(0, 1)), (0, 0, 1, QI(0, -1))]
ELL = qv(0, 1, 0, 1, 0, 0)
ENN = qv(0, 1, 0, -1, 0, 0)
EM = qv(0, 0, 0, 0, 1, QI(0, 1))
EMB = qv(0, 0, 0, 0, 1, QI(0, -1))


def st(dx):
    return qv(0, dx[0], 0, dx[1], dx[2], dx[3])


def vsum(*terms):
    return [sum((c * v[a] for c, v in terms), ZERO) for a in range(6)]


def wedge_act(u, v, w):
    return vsum((ip(v, w), u), (-ip(u, w), v))


def omega_act(dx, w):
    """Om(dx) = dx^a e_a n_inf acting on w."""
    d = st(dx)
    return wedge_act(d, NINF, w)


def frame(x):
    X, _ = point(x)
    xv = st(x)
    lx = vsum((ONE, ELL), (-ip(xv, ELL), NINF))
    mx = vsum((ONE, EM), (-ip(xv, EM), NINF))
    return X, lx, mx


def basis_bivectors():
    return [(qv(*[1 if c == a else 0 for c in range(6)]), qv(*[1 if c == b else 0 for c in range(6)]))
            for a, b in combinations(range(6), 2)]


def check_formula_and_translation_identities():
    premise("pairing.imported-flat-conformal-model-twistor-incidence")
    ok = True
    # the action formula agrees with (1/2)[u v, w] in the Clifford algebra on basis elements
    for a, b in combinations(range(6), 2):
        B = GA.mul(GA.gen(a), GA.gen(b), SQR)
        for c in range(6):
            w = GA.gen(c)
            hc = GA.scal(F(1, 2), GA.sub(GA.mul(B, w, SQR), GA.mul(w, B, SQR)))
            fv = wedge_act(qv(*[1 if k == a else 0 for k in range(6)]), qv(*[1 if k == b else 0 for k in range(6)]),
                           qv(*[1 if k == c else 0 for k in range(6)]))
            ok = ok and all(fv[k] == QI(hc.get((k,), F(0))) for k in range(6))
    for x in RPOINTS:
        X, lx, mx = frame(x)
        Wx = [X, lx, mx]
        ok = ok and all(ip(p, q) == ZERO for p in Wx for q in Wx) and GA.field_rank(Wx) == 3
        for k, a in enumerate(ST):
            ea = qv(*[1 if c == a else 0 for c in range(6)])
            xa = ip(ea, st(x))
            ok = ok and wedge_act(ea, NINF, X) == vsum((ONE, ea), (-xa, NINF))
            ok = ok and wedge_act(ea, NINF, NINF) == [ZERO] * 6
        for dx in DISPLACEMENTS:
            xd = tuple(QI(x[i]) + QI(dx[i]) for i in range(4))
            Xd, _ = point(xd)
            lin = vsum(*[(QI(dx[k]), vsum((ONE, qv(*[1 if c == a else 0 for c in range(6)])),
                                          (-ip(qv(*[1 if c == a else 0 for c in range(6)]), st(x)), NINF)))
                         for k, a in enumerate(ST)])
            Qd = ip(st(dx), st(dx))
            ok = ok and vsum((ONE, Xd), (-ONE, X), (-ONE, lin)) == vsum((QI(F(-1, 2)) * Qd, NINF))
    _tp_rv = (ok); assert _tp_rv is not False, "check_formula_and_translation_identities"; return _tp_rv


def classes(x, dx):
    X, lx, mx = frame(x)
    OX = omega_act(dx, X)
    return (ip(OX, lx), ip(OX, mx), ip(omega_act(dx, lx), mx))


def check_pairing_classes_and_parallel_direction():
    premise("pairing.imported-flat-conformal-model-twistor-incidence")
    ok = True
    for x in RPOINTS:
        for dx in DISPLACEMENTS:
            d = st(dx)
            ok = ok and classes(x, dx) == (ip(d, ELL), ip(d, EM), ZERO)
        ok = ok and classes(x, (0, 0, 1, QI(0, -1))) == (ZERO, QI(-2), ZERO)
        ok = ok and classes(x, (0, 0, 1, QI(0, 1))) == (ZERO, ZERO, ZERO)
    # real displacements: (<dx,l>, Re<dx,m>, Im<dx,m>) is a real 3 x 4 matrix; its kernel is R l
    rows = [[ip(st(e), ELL).re for e in ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))],
            [ip(st(e), EM).re for e in ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))],
            [ip(st(e), EM).im for e in ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))]]
    ker = GA.field_kernel(rows)
    ok = ok and len(ker) == 1 and ker[0][0] == ker[0][1] and ker[0][2] == 0 and ker[0][3] == 0
    # incidence: X(x + s l) = X(x) + s l(x), inside W(x)
    for x in RPOINTS:
        X, lx, mx = frame(x)
        for s in (F(1), F(-2), F(5, 3)):
            Xs, _ = point((F(x[0]) + s, F(x[1]) + s, x[2], x[3]))
            ok = ok and Xs == vsum((ONE, X), (QI(s), lx))
            ok = ok and GA.field_rank([X, lx, mx, Xs]) == 3
    _tp_rv = (ok); assert _tp_rv is not False, "check_pairing_classes_and_parallel_direction"; return _tp_rv


def check_vacuum_stabiliser_has_dimension_twelve():
    premise("pairing.imported-flat-conformal-model-twistor-incidence")
    ok = True
    bivs = basis_bivectors()
    for x in RPOINTS:
        Wx = list(frame(x))
        rows = []
        for i in range(3):
            for j in range(3):
                rows.append([ip(wedge_act(u, v, Wx[i]), Wx[j]) for u, v in bivs])
        ok = ok and GA.field_rank(rows) == 3
        stab = GA.field_kernel(rows)
        ok = ok and len(stab) == 12
        # the three class functionals alone have rank three and cut out the same space
        cls = [[ip(wedge_act(u, v, Wx[0]), Wx[1]) for u, v in bivs],
               [ip(wedge_act(u, v, Wx[0]), Wx[2]) for u, v in bivs],
               [ip(wedge_act(u, v, Wx[1]), Wx[2]) for u, v in bivs]]
        ok = ok and GA.field_rank(cls) == 3 and GA.field_rank(cls + rows) == 3
        # spin action on the vacuum of W(x): B fixes the ray of u iff B stabilises W(x)
        u = joint_kernel(Wx)
        ok = ok and len(u) == 1
        u = u[0]
        imgs = [apply(mmul(CB[a], CB[b]), u) for a, b in combinations(range(6), 2)]
        # B u in C u: kernel of B -> (B u mod u), computed with u appended as a free direction
        M = [[imgs[k][r] for k in range(15)] + [-u[r]] for r in range(8)]
        ker = GA.field_kernel(M)
        ok = ok and len(ker) == 12
        ok = ok and GA.field_rank([k[:15] for k in ker] + stab) == 12
    _tp_rv = (ok); assert _tp_rv is not False, "check_vacuum_stabiliser_has_dimension_twelve"; return _tp_rv
