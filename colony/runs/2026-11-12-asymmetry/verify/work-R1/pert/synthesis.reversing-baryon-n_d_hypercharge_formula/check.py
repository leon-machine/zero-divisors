"""Reversing baryon number is a conjugation, and a conjugation reverses the Jarlskog invariant: exact checks.

Part 1, on the five-mode module (pair modes 1, 2, 3, slot modes 4, 5; occupation states): the 32 partial
exchanges of set and clear, S -> S symmetric-difference A. n_B = 0, 1/3, -1/3, 0 and B - L = 1 - (2/3)k at pair
number k, Y = (j - 1)/2 + (B - L)/2 at slot number j, on all 32 states. Exactly four exchanges reverse n_B (A
contains the three pair modes); exactly two carry Y to plus or minus Y and keep the pair and slot blocks
(identity and the total exchange); the total exchange reverses Y, B - L, n_B and maps the even states to the odd
ones. The six species of the sixteen have pairwise distinct (dimension, Y), with Q the only one of dimension 6.
Part 2, on 3 x 3 Hermitian matrices over the Gaussian rationals (GA.QI): D = det[H_u, H_d] has no real part,
is unchanged by a common unitary change of family basis, changes sign under entrywise conjugation, and vanishes
for real symmetric pairs.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from GA import QI
from tp_premise import premise

MODES = (1, 2, 3, 4, 5)
PAIR, SLOT = frozenset((1, 2, 3)), frozenset((4, 5))
STATES = [frozenset(c) for r in range(6) for c in combinations(MODES, r)]
EVEN = [S for S in STATES if len(S) % 2 == 0]


def k_of(S):
    return len(S & PAIR)


def j_of(S):
    return len(S & SLOT)


def n_b(S):
    return [F(0), F(1, 3), F(-1, 3), F(0)][k_of(S)]


def bml(S):
    return 1 - F(2, 3) * k_of(S)


def hyp(S):
    return F(j_of(S) - 1, 2) - bml(S) / 2


def check_only_the_total_exchange_reverses_the_charges_and_keeps_the_gauge_algebra():
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    premise("standard-model.proton-decay-only-through-slot-pair")
    ok = len(STATES) == 32 and len(EVEN) == 16
    # n_B on the sixteen agrees with ((B - L) + chi)/4
    ok = ok and all(n_b(S) == (bml(S) - (-1) ** j_of(S)) / 4 for S in EVEN)
    reverse_nb, keep_y, reverse_all = [], [], []
    for A in STATES:
        img = lambda S: S ^ A
        if all(n_b(img(S)) == -n_b(S) for S in STATES):
            reverse_nb.append(A)
        signs = {s for s in (1, -1) if all(hyp(img(S)) == s * hyp(S) for S in STATES)}
        blocks = (A & PAIR) in (frozenset(), PAIR) and (A & SLOT) in (frozenset(), SLOT)
        if signs and blocks:
            keep_y.append(A)
        if all((n_b(img(S)), bml(img(S)), hyp(img(S))) == (-n_b(S), -bml(S), -hyp(S)) for S in STATES):
            reverse_all.append(A)
    full = frozenset(MODES)
    ok = ok and sorted(map(sorted, reverse_nb)) == [[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 5]]
    ok = ok and sorted(map(sorted, keep_y)) == [[], [1, 2, 3, 4, 5]]
    ok = ok and reverse_all == [full]
    ok = ok and all(len(S ^ full) % 2 == 1 for S in EVEN)
    species = {}
    for S in EVEN:
        species.setdefault((j_of(S), k_of(S)), []).append(hyp(S))
    data = sorted((len(v), v[0]) for v in species.values())
    ok = ok and all(len(set(v)) == 1 for v in species.values())
    ok = ok and data == [(1, F(0)), (1, F(1)), (2, F(-1, 2)), (3, F(-2, 3)), (3, F(1, 3)), (6, F(1, 6))]
    GA.check("32 exchanges: 4 reverse n_B, 2 keep the gauge algebra, 1 reverses all charges; Q is the only 6", ok)
    return ok


def mat_mul(A, B):
    return [[sum((A[i][m] * B[m][j] for m in range(3)), QI(0)) for j in range(3)] for i in range(3)]


def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)]


def dagger(A):
    return [[A[j][i].conj() for j in range(3)] for i in range(3)]


def conj(A):
    return [[A[i][j].conj() for j in range(3)] for i in range(3)]


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def comm_det(Hu, Hd):
    return det3(mat_sub(mat_mul(Hu, Hd), mat_mul(Hd, Hu)))


def hermitian(d, a, b, c):
    """diagonal d (three rationals), upper entries a, b, c (Gaussian rationals)."""
    return [[QI(d[0]), a, b], [a.conj(), QI(d[1]), c], [b.conj(), c.conj(), QI(d[2])]]


def check_commutator_determinant_is_odd_under_conjugation():
    premise("synthesis.imported-jarlskog-commutator-identity")
    samples = [
        (hermitian((1, 2, 5), QI(1, 1), QI(0, 2), QI(3, -1)), hermitian((2, -1, 3), QI(2, -1), QI(1, 0), QI(0, 1))),
        (hermitian((0, 1, 7), QI(F(1, 2), 1), QI(1, 0), QI(0, F(1, 3))), hermitian((4, 2, 1), QI(1, 2), QI(-1, 1), QI(2, 0))),
        (hermitian((3, 1, 2), QI(1, 0), QI(2, 0), QI(1, 0)), hermitian((1, 5, 2), QI(0, 1), QI(1, 0), QI(1, 0))),
    ]
    # a unitary over the Gaussian rationals: a rotation by the (3, 4, 5) angle in the first two families
    # followed by the phases (3 + 4i)/5, i, 1
    R = [[QI(F(3, 5)), QI(F(-4, 5)), QI(0)], [QI(F(4, 5)), QI(F(3, 5)), QI(0)], [QI(0), QI(0), QI(1)]]
    P = [[QI(F(3, 5), F(4, 5)), QI(0), QI(0)], [QI(0), QI(0, 1), QI(0)], [QI(0), QI(0), QI(1)]]
    U = mat_mul(P, R)
    one = [[QI(1 if i == j else 0) for j in range(3)] for i in range(3)]
    ok = mat_sub(mat_mul(U, dagger(U)), one) == [[QI(0)] * 3 for _ in range(3)]
    for Hu, Hd in samples:
        D = comm_det(Hu, Hd)
        ok = ok and Hu == dagger(Hu) and Hd == dagger(Hd)
        ok = ok and D != QI(0) and D + D.conj() == QI(0)
        ok = ok and comm_det(conj(Hu), conj(Hd)) == QI(0) - D
        rot = lambda H: mat_mul(mat_mul(U, H), dagger(U))
        ok = ok and comm_det(rot(Hu), rot(Hd)) == D
        ok = ok and comm_det(rot(conj(Hu)), rot(conj(Hd))) == QI(0) - D
    real_u = hermitian((1, 2, 5), QI(1, 0), QI(2, 0), QI(3, 0))
    real_d = hermitian((2, -1, 3), QI(2, 0), QI(1, 0), QI(-1, 0))
    ok = ok and mat_sub(mat_mul(real_u, real_d), mat_mul(real_d, real_u)) != [[QI(0)] * 3 for _ in range(3)]
    ok = ok and comm_det(real_u, real_d) == QI(0)
    ok = ok and [comm_det(a, b) for a, b in samples] == [QI(0, 576), QI(0, F(-27815, 27)), QI(0, 14)]
    GA.check("det[H_u, H_d]: no real part, unitary-invariant, odd under conjugation, zero for real pairs", ok)
    return ok
