"""Reversing baryon number is a conjugation, and a conjugation reverses the Jarlskog invariant: exact checks.

Part 1, on the five-mode module (pair modes 1, 2, 3, slot modes 4, 5; occupation states): the 32 partial
exchanges of set and clear, S -> S symmetric-difference A. n_B = 0, 1/3, -1/3, 0 and B - L = 1 - (2/3)k at pair
number k, Y = (j - 1)/2 + (B - L)/2 at slot number j, on all 32 states. Exactly four exchanges reverse n_B (A
contains the three pair modes); exactly two normalise su(3) + su(2)_L + u(1)_Y, tested as membership of the
image of each of the twelve generators in their span as operators on the 32 states (identity and the total
exchange); the exchange on modes 1, 2, 3, 4 maps the sixteen to itself, reverses n_B and does not normalise; the total exchange reverses Y, B - L, n_B and maps the even states to the odd
ones. The six species of the sixteen have pairwise distinct (dimension, Y), with Q the only one of dimension 6.
Part 2, on 3 x 3 Hermitian matrices over the Gaussian rationals (GA.QI): D = det[H_u, H_d] has no real part,
is unchanged by a common unitary change of family basis, changes sign under entrywise conjugation, and vanishes
for real symmetric pairs. The imported identity det[H_u, H_d] = 2 I J F_u F_d is verified, sign included, on one
pair built from two Cayley unitaries, with J from V = U_u^dagger U_d, and conjugation sends that J to -J. The
stored J is read and is not zero.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from GA import QI
from tp_premise import premise, quantity

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
    return F(j_of(S) - 1, 2) + bml(S) / 2


def word(ops, st):
    """Apply a product of mode operators (rightmost first) to a state {set: coefficient}."""
    for kind, i in reversed(ops):
        out = {}
        for S, a in st.items():
            if kind == "v" and i not in S:
                T = S | {i}
            elif kind == "w" and i in S:
                T = S - {i}
            else:
                continue
            sign = -1 if sum(1 for m in S if m < i) % 2 else 1
            out[T] = out.get(T, 0) + sign * a
        st = out
    return st


def operator(terms, A=frozenset()):
    """Matrix {(T, S): coefficient} on the 32 states of a sum of (coefficient, word), after exchanging set and
    clear on the modes of A."""
    flip = {"v": "w", "w": "v"}
    out = {}
    for coeff, ops in terms:
        ops = [(flip[kind] if i in A else kind, i) for kind, i in ops]
        for S in STATES:
            for T, a in word(ops, {S: F(1)}).items():
                out[(T, S)] = out.get((T, S), 0) + coeff * a
    return {key: val for key, val in out.items() if val != 0}


def number(i):
    return [("v", i), ("w", i)]


GENERATORS = [[(F(1), [("v", a), ("w", b)])] for a in (1, 2, 3) for b in (1, 2, 3) if a != b]
GENERATORS += [[(F(1), number(1)), (F(-1), number(2))], [(F(1), number(2)), (F(-1), number(3))]]
GENERATORS += [[(F(1), [("v", 4), ("w", 5)])], [(F(1), [("v", 5), ("w", 4)])],
               [(F(1), number(4)), (F(-1), number(5))]]
GENERATORS += [[(F(1, 2), number(4)), (F(1, 2), number(5))] + [(F(-1, 3), number(a)) for a in (1, 2, 3)]]


def echelon(vectors):
    pivots = []
    for v in vectors:
        v = reduce_by(v, pivots)
        if v:
            key = min(v, key=lambda t: (sorted(t[0]), sorted(t[1])))
            pivots.append((key, {m: x / v[key] for m, x in v.items()}))
    return pivots


def reduce_by(v, pivots):
    v = dict(v)
    for key, p in pivots:
        if key in v:
            f = v[key]
            for m, x in p.items():
                v[m] = v.get(m, 0) - f * x
            v = {m: x for m, x in v.items() if x != 0}
    return v


def normalises(A, pivots):
    return all(not reduce_by(operator(g, A), pivots) for g in GENERATORS)


def check_only_the_total_exchange_reverses_the_charges_and_keeps_the_gauge_algebra():
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    premise("standard-model.proton-decay-only-through-slot-pair")
    ok = len(STATES) == 32 and len(EVEN) == 16
    # n_B on the sixteen agrees with ((B - L) + chi)/4
    ok = ok and all(n_b(S) == (bml(S) - (-1) ** j_of(S)) / 4 for S in EVEN)
    pivots = echelon([operator(g) for g in GENERATORS])
    ok = ok and len(GENERATORS) == 12 and len(pivots) == 12
    # the hypercharge generator acts as the function hyp on every state
    ok = ok and operator(GENERATORS[11]) == {(S, S): hyp(S) for S in STATES if hyp(S) != 0}
    reverse_nb, normal, reverse_all = [], [], []
    for A in STATES:
        img = lambda S: S ^ A
        if all(n_b(img(S)) == -n_b(S) for S in STATES):
            reverse_nb.append(A)
        if normalises(A, pivots):
            normal.append(A)
        if all((n_b(img(S)), bml(img(S)), hyp(img(S))) == (-n_b(S), -bml(S), -hyp(S)) for S in STATES):
            reverse_all.append(A)
    full = frozenset(MODES)
    ok = ok and sorted(map(sorted, reverse_nb)) == [[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 5]]
    ok = ok and sorted(map(sorted, normal)) == [[], [1, 2, 3, 4, 5]]
    ok = ok and reverse_all == [full]
    ok = ok and all(len(S ^ full) % 2 == 1 for S in EVEN)
    # the exchange on modes 1, 2, 3, 4: a linear map of the sixteen to itself reversing n_B, not normalising
    four = frozenset((1, 2, 3, 4))
    ok = ok and all(len(S ^ four) % 2 == 0 and n_b(S ^ four) == -n_b(S) for S in EVEN) and four not in normal
    species = {}
    for S in EVEN:
        species.setdefault((j_of(S), k_of(S)), []).append(hyp(S))
    data = sorted((len(v), v[0]) for v in species.values())
    ok = ok and all(len(set(v)) == 1 for v in species.values())
    ok = ok and data == [(1, F(0)), (1, F(1)), (2, F(-1, 2)), (3, F(-2, 3)), (3, F(1, 3)), (6, F(1, 6))]
    GA.check("32 exchanges: 4 reverse n_B, 2 normalise the gauge algebra, 1 reverses all charges; Q is the only 6", ok)
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


def cayley(K):
    """(1 - K)(1 + K)^(-1) for skew-Hermitian K: a unitary over the Gaussian rationals."""
    one = [[QI(1 if i == j else 0) for j in range(3)] for i in range(3)]
    plus = [[one[i][j] + K[i][j] for j in range(3)] for i in range(3)]
    minus = mat_sub(one, K)
    cols = [GA.field_solve(plus, [one[i][j] for i in range(3)]) for j in range(3)]
    inverse = [[cols[j][i] for j in range(3)] for i in range(3)]
    return mat_mul(minus, inverse)


def check_imported_identity_and_sign_of_j_on_a_rational_pair():
    premise("synthesis.imported-jarlskog-commutator-identity")
    one = [[QI(1 if i == j else 0) for j in range(3)] for i in range(3)]
    zero = [[QI(0)] * 3 for _ in range(3)]
    Ku = [[QI(0, 1), QI(1, 1), QI(2, 0)], [QI(-1, 1), QI(0, 0), QI(0, 1)], [QI(-2, 0), QI(0, 1), QI(0, 2)]]
    Kd = [[QI(0, 0), QI(1, 0), QI(1, 2)], [QI(-1, 0), QI(0, 1), QI(3, 0)], [QI(-1, 2), QI(-3, 0), QI(0, 0)]]
    Uu, Ud = cayley(Ku), cayley(Kd)
    ok = mat_sub(mat_mul(Uu, dagger(Uu)), one) == zero and mat_sub(mat_mul(Ud, dagger(Ud)), one) == zero

    def diag(d):
        return [[QI(d[i] if i == j else 0) for j in range(3)] for i in range(3)]

    def jarlskog(A, B):
        V = mat_mul(dagger(A), B)
        return (V[0][1] * V[1][2] * V[0][2].conj() * V[1][1].conj()).im

    mu, md = (1, 4, 9), (2, 3, 7)
    Hu = mat_mul(mat_mul(Uu, diag(mu)), dagger(Uu))
    Hd = mat_mul(mat_mul(Ud, diag(md)), dagger(Ud))
    fu = (mu[2] - mu[1]) * (mu[2] - mu[0]) * (mu[1] - mu[0])
    fd = (md[2] - md[1]) * (md[2] - md[0]) * (md[1] - md[0])
    J = jarlskog(Uu, Ud)
    ok = ok and (fu, fd) == (120, 20) and J != 0
    ok = ok and comm_det(Hu, Hd) == QI(0, 2 * J * fu * fd)
    # entrywise conjugation: H* = U* diag U*^dagger, and J goes to -J
    ok = ok and jarlskog(conj(Uu), conj(Ud)) == -J
    ok = ok and comm_det(conj(Hu), conj(Hd)) == QI(0, -2 * J * fu * fd)
    stored = quantity("quantity.jarlskog-invariant")
    ok = ok and stored == F(312, 10 ** 7) and stored != 0
    GA.check("det[H_u, H_d] = 2 I J F_u F_d with sign on a rational pair; conjugation sends J to -J; stored J != 0", ok)
    return ok
