"""standard-model.grip-mass-two-rung-module: exact checks.

(1) Components and chirality: in the five-mode module Lambda(W + R_2) (pairs 0, 1, 2; rungs 3, 4) a state of
    rung sector j has binom(2, j) slot components (1, 2, 1); the n-rung module has binom(n, j) (counted for
    n = 2..4 against Pascal's rows); within the even chirality half every rung sector has a single pair
    parity, so all its components lie in one of CS, CS-.
(2) Masses, with P = sum_a pi_a pi_a^dagger for Gaussian-rational spinor parts and m^2 = 2 det P (the
    Minkowski reading p.p = det(p^a sigma_a) is checked on rational p): a single component is null and
    future-directed (m^2 = 0); two components give 2 |<pi1 pi2>|^2 on all fifteen pairs of six spinors,
    vanishing exactly for the proportional pairs; for k = 3, 4, 6 components (the n-rung sectors)
    m^2 = 2 sum_{a<b} |<pi_a pi_b>|^2.
(3) Sector labels: on the sixteen even states the sectors present are (j, k) = (0,0), (0,2), (1,1), (1,3),
    (2,0), (2,2); the slot-singlet ones (j = 0, 2) carry Y = 0, -2/3, 1, 1/3 (nu^c, u^c, e^c, d^c) and the
    slot-doublet ones Y = 1/6, -1/2 (Q, L), read off the hypercharge operator Y = N_R/2 - N_W/3.
That (i) is the moment-map theorem's sum over components is used, not re-derived.
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
PROPORTIONAL = [(sp2(1, 2), sp2(3, 6)), (sp2(QI(1, 1), 2), sp2(QI(0, 2), QI(2, 2)))]
RVECS = [(1, 0, 0, 0), (2, 1, -1, 3), (F(1, 2), F(3, 4), 0, -2), (5, 3, 4, 0)]


def check_components_per_rung_sector_and_chirality():
    premise("standard-model.module-factorises-even-ground-elements-act")
    premise("standard-model.moment-map-grip-mass-are-insensitive")
    ok = True
    counts = [0, 0, 0]
    for S in STATES:
        if not S & set(PAIRS5):
            counts[len(S)] += 1
    ok = ok and counts == [1, 2, 1]
    rows = {3: [1, 3, 3, 1], 4: [1, 4, 6, 4, 1]}
    for n, row in rows.items():
        ok = ok and [len(list(combinations(range(n), j))) for j in range(n + 1)] == row
    for j in range(3):
        parities = {len(S & set(PAIRS5)) % 2 for S in STATES if len(S) % 2 == 0 and len(S & set(RUNGS5)) == j}
        ok = ok and len(parities) == 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_components_per_rung_sector_and_chirality"; return _tp_rv


def mass2(spinors):
    return 2 * det2(momentum(*spinors))


def check_grip_mass_of_each_sector():
    premise("standard-model.imported-grip-area-casimir-form")
    ok = True
    for p in RVECS:
        ok = ok and det2(pauli_matrix(p)) == QI(mink(p))
    for p in SPINORS:
        ok = ok and mass2([p]) == ZQ and tr2(momentum(p)).re > 0
    n = 0
    for p, q in combinations(SPINORS, 2):
        m2 = mass2([p, q])
        ok = ok and m2 == QI(2 * absq(bracket(p, q))) and m2 != ZQ
        n += 1
    ok = ok and n == 15
    for p, q in PROPORTIONAL:
        ok = ok and mass2([p, q]) == ZQ and bracket(p, q) == ZQ
    for k in (3, 4, 6):
        comps = SPINORS[:k]
        total = sum((absq(bracket(p, q)) for p, q in combinations(comps, 2)), F(0))
        ok = ok and mass2(comps) == QI(2 * total)
    _tp_rv = (ok); assert _tp_rv is not False, "check_grip_mass_of_each_sector"; return _tp_rv


def check_sector_labels_under_s():
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.under-s-composites-state-space-spinor")
    ok = True
    sectors = {}
    for S in STATES:
        if len(S) % 2:
            continue
        j, k = len(S & set(RUNGS5)), len(S & set(PAIRS5))
        img = sp_apply(HYP, basis5(S))
        y = img.get(SIDX[S], F(0))
        ok = ok and set(img) <= {SIDX[S]}
        get_or_set(sectors, (j, k), set()).add(y)
    ok = ok and sorted(sectors) == [(0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2)]
    ok = ok and all(len(v) == 1 for v in sectors.values())
    singlet = sorted(next(iter(sectors[s])) for s in sectors if s[0] in (0, 2))
    doublet = sorted(next(iter(sectors[s])) for s in sectors if s[0] == 1)
    ok = ok and singlet == [F(-2, 3), F(0), F(1, 3), F(1)] and doublet == [F(-1, 2), F(1, 6)]
    _tp_rv = (ok); assert _tp_rv is not False, "check_sector_labels_under_s"; return _tp_rv
