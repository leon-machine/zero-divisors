"""families.imported-face-valued-bracket-quantum-numbers: exact checks.

(1) Flat mass: for Gaussian-rational spinors, a single momentum P = pi pi^dagger has det P = 0 and
    tr P > 0 (null, future-directed); for two, m^2 = 2 det(pi1 pi1^dagger + pi2 pi2^dagger) =
    2 |<pi1 pi2>|^2 on six pairs, and 0 for aligned (proportional) spinors. The Minkowski reading
    P = p^a sigma_a / sqrt 2 (p.p = det(p^a sigma_a) = 2 det P) is checked on rational p.
(2) Internal U(2): for five unitary Gaussian-rational U (U U^dagger = 1, determinants 1, i, i, -1, -i) the
    mixing preserves the total momentum, and <pi1' pi2'> = det(U) <pi1 pi2>: an SU(2) singlet (det 1 leaves it
    fixed), charge one under the determinant (the scalar phase i gives the factor i^2 = -1), modulus (the
    mass) invariant, phase moved.
(3) Quantum numbers on the five-mode module (pairs 0, 1, 2; rungs 3, 4; Y = N_R/2 - N_W/3,
    T3 = (N_4 - N_5)/2 in the text's labels): the bracket b = v_4 v_5 has ad-weight Y = +1, T3 = 0, commutes
    with the six su(3) generators and the three su(2) generators, and creates the (2,0) state, the e^c
    sector, from the vacuum; a weak doublet constituent (v_4: Y = 1/2, T3 = 1/2) is moved by su(2).
The three-spinor bound and the order-parameter reading are observation-level statements with no finite core.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from pyutil import get_or_set
from tp_premise import premise

# ---------------------------------------------------------------------------
# Two-component spinors over Q(i): momentum P = sum pi pi^dagger (P_AA' = pi_A conj(pi_A')), the
# bracket <pi1 pi2> = eps^AB pi1_A pi2_B = pi1_0 pi2_1 - pi1_1 pi2_0, and the Minkowski reading
# P = p^a sigma_a / sqrt 2, under which p.p = det(p^a sigma_a) = 2 det P.
# ---------------------------------------------------------------------------
QI = GA.QI
ZQ = QI(0)


def sp2(a, b):
    return (a if isinstance(a, QI) else QI(a), b if isinstance(b, QI) else QI(b))


def outer(p):
    return [[p[A] * p[B].conj() for B in range(2)] for A in range(2)]


def m2add(*Ms):
    return [[sum((M[i][j] for M in Ms), ZQ) for j in range(2)] for i in range(2)]


def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def tr2(M):
    return M[0][0] + M[1][1]


def momentum(*spinors):
    return m2add(*[outer(p) for p in spinors])


def bracket(p, q):
    return p[0] * q[1] - p[1] * q[0]


def absq(z):
    return z.re * z.re + z.im * z.im


def pauli_matrix(p):
    """p^a sigma_a for a rational 4-vector p."""
    p0, p1, p2, p3 = [QI(x) for x in p]
    return [[p0 + p3, p1 - QI(0, 1) * p2], [p1 + QI(0, 1) * p2, p0 - p3]]


def mink(p):
    return p[0] * p[0] - p[1] * p[1] - p[2] * p[2] - p[3] * p[3]


def mix(U, spinors):
    """pi'^i = sum_j U^i_j pi^j."""
    n = len(spinors)
    return [tuple(sum((U[i][j] * spinors[j][A] for j in range(n)), ZQ) for A in range(2)) for i in range(n)]
# ---------------------------------------------------------------------------
# The five-mode module Lambda(W + R_2) = Lambda(C^5), exact (sparse matrices {(row, col): Fraction}).
# Modes 0, 1, 2 are the pair modes (W), modes 3, 4 the two rung (slot) modes, the text's modes 4 and 5.
# v_i = creation (wedge), w_i = annihilation (contraction), v_i w_i + w_i v_i = 1.
# ---------------------------------------------------------------------------
NM = 5
PAIRS5, RUNGS5 = (0, 1, 2), (3, 4)
STATES = [frozenset(S) for k in range(NM + 1) for S in combinations(range(NM), k)]
SIDX = {S: i for i, S in enumerate(STATES)}
DIM5 = len(STATES)


def sp_from_action(act):
    M = {}
    for S in STATES:
        for T, c in act(S).items():
            if c != 0:
                M[(SIDX[T], SIDX[S])] = M.get((SIDX[T], SIDX[S]), F(0)) + c
    return {k: v for k, v in M.items() if v != 0}


def sp_mul(A, B):
    Bc = {}
    for (i, j), b in B.items():
        get_or_set(Bc, i, []).append((j, b))
    C = {}
    for (i, k), a in A.items():
        for j, b in Bc.get(k, ()):
            C[(i, j)] = C.get((i, j), F(0)) + a * b
    return {k: v for k, v in C.items() if v != 0}


def sp_add(*Ms):
    C = {}
    for M in Ms:
        for k, v in M.items():
            C[k] = C.get(k, F(0)) + v
    return {k: v for k, v in C.items() if v != 0}


def sp_scal(c, M):
    return {k: c * v for k, v in M.items() if c * v != 0}


def sp_eq(A, B):
    return sp_add(A, sp_scal(F(-1), B)) == {}


def sp_apply(M, vec):
    out = {}
    for (i, j), a in M.items():
        if j in vec:
            out[i] = out.get(i, F(0)) + a * vec[j]
    return {k: v for k, v in out.items() if v != 0}


ID5 = {(i, i): F(1) for i in range(DIM5)}
V5 = [sp_from_action(lambda S, i=i: GA.ext_wedge(i, {S: F(1)})) for i in range(NM)]
W5 = [sp_from_action(lambda S, i=i: GA.ext_contract([F(1) if j == i else F(0) for j in range(NM)], {S: F(1)}))
      for i in range(NM)]


def num(i):
    return sp_mul(V5[i], W5[i])


N_W = sp_add(*[num(i) for i in PAIRS5])
N_R = sp_add(*[num(i) for i in RUNGS5])
HYP = sp_add(sp_scal(F(1, 2), N_R), sp_scal(F(-1, 3), N_W))
T3 = sp_scal(F(1, 2), sp_add(num(3), sp_scal(F(-1), num(4))))
SU3 = [sp_mul(V5[i], W5[j]) for i in PAIRS5 for j in PAIRS5 if i != j]
SU2 = [sp_mul(V5[3], W5[4]), sp_mul(V5[4], W5[3]), T3]


def comm(A, B):
    return sp_add(sp_mul(A, B), sp_scal(F(-1), sp_mul(B, A)))


def weight(M, Q):
    """The eigenvalue of ad Q on M, or None if M is not an eigenvector."""
    c = comm(Q, M)
    if c == {}:
        return F(0)
    (i, j), a = next(iter(M.items()))
    q = c.get((i, j), F(0)) / a
    return q if sp_eq(c, sp_scal(q, M)) else None


def basis5(S):
    return {SIDX[frozenset(S)]: F(1)}

SPINORS = [sp2(1, 0), sp2(0, 1), sp2(1, QI(0, 1)), sp2(QI(2, -1), 3), sp2(F(1, 2), QI(-1, 4)), sp2(QI(0, 3), QI(5, 2))]
UNITARIES = [
    [[QI(F(3, 5)), QI(F(4, 5))], [QI(F(-4, 5)), QI(F(3, 5))]],
    [[QI(0, 1), ZQ], [ZQ, QI(1)]],
    [[QI(F(1, 2), F(1, 2)), QI(F(1, 2), F(-1, 2))], [QI(F(1, 2), F(-1, 2)), QI(F(1, 2), F(1, 2))]],
    [[QI(0, 1), ZQ], [ZQ, QI(0, 1)]],
    [[QI(0, F(3, 5)), QI(0, F(4, 5))], [QI(F(4, 5)), QI(F(-3, 5))]],
]
RVECS = [(1, 0, 0, 0), (2, 1, -1, 3), (F(1, 2), F(3, 4), 0, -2), (5, 3, 4, 0)]


def check_two_spinor_mass_is_twice_squared_bracket():
    premise("mass.mass-symplectic-area-two-twistor-formula")
    ok = True
    for p in RVECS:
        ok = ok and det2(pauli_matrix(p)) == QI(mink(p))
    for p in SPINORS:
        P = momentum(p)
        ok = ok and det2(P) == ZQ and tr2(P).re > 0 and tr2(P).im == 0
    pairs = 0
    for p, q in combinations(SPINORS, 2):
        P = momentum(p, q)
        ok = ok and 2 * det2(P) == QI(2 * absq(bracket(p, q)))
        pairs += 1
    ok = ok and pairs == 15
    for p in SPINORS:
        for c in (QI(2), QI(1, -3)):
            q = (c * p[0], c * p[1])
            ok = ok and det2(momentum(p, q)) == ZQ and bracket(p, q) == ZQ
    _tp_rv = (ok); assert _tp_rv is not False, "check_two_spinor_mass_is_twice_squared_bracket"; return _tp_rv


def check_bracket_transforms_by_the_determinant():
    premise("standard-model.mass-bracket-charged-singlet")
    premise("standard-model.internal-symmetry-ladder")
    ok = True
    dets = []
    for U in UNITARIES:
        Ud = [[U[j][i].conj() for j in range(2)] for i in range(2)]
        UUd = [[sum((U[i][k] * Ud[k][j] for k in range(2)), ZQ) for j in range(2)] for i in range(2)]
        ok = ok and UUd == [[QI(1), ZQ], [ZQ, QI(1)]]
        d = det2(U)
        dets.append(d)
        for p, q in combinations(SPINORS[:4], 2):
            p2, q2 = mix(U, [p, q])
            ok = ok and momentum(p2, q2) == momentum(p, q)
            ok = ok and bracket(p2, q2) == d * bracket(p, q)
            ok = ok and absq(bracket(p2, q2)) == absq(bracket(p, q))
    ok = ok and dets == [QI(1), QI(0, 1), QI(0, 1), QI(-1), QI(0, -1)]
    _tp_rv = (ok); assert _tp_rv is not False, "check_bracket_transforms_by_the_determinant"; return _tp_rv


def check_bracket_carries_the_quantum_numbers_of_ec():
    premise("standard-model.mass-bracket-charged-singlet")
    ok = True
    b = sp_mul(V5[3], V5[4])
    ok = ok and weight(b, HYP) == F(1) and weight(b, T3) == F(0)
    ok = ok and weight(b, sp_scal(F(6), HYP)) == F(6)
    ok = ok and all(comm(X, b) == {} for X in SU3 + SU2)
    state = sp_apply(b, basis5(()))
    ok = ok and len(state) == 1 and set(state) == {SIDX[frozenset((3, 4))]}
    # the state of b is in the sector (j, k) = (2, 0): two rungs, no pairs
    (S,) = [STATES[i] for i in state]
    ok = ok and len(S & set(RUNGS5)) == 2 and len(S & set(PAIRS5)) == 0
    # a doublet constituent: Y = 1/2, T3 = 1/2, moved by su(2)
    ok = ok and weight(V5[3], HYP) == F(1, 2) and weight(V5[3], T3) == F(1, 2)
    ok = ok and comm(SU2[1], V5[3]) != {}
    _tp_rv = (ok); assert _tp_rv is not False, "check_bracket_carries_the_quantum_numbers_of_ec"; return _tp_rv
