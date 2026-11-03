from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def transpose(M):
    return [list(r) for r in zip(*M)]


MS = [
        [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
        [[0, 1, 0], [1, 0, 0], [0, 0, 2]],
        [[2, 1, 0], [1, 0, 3], [0, 3, -1]],
        [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
    [[0, 2, 1], [2, 0, 1], [1, 1, 0]],
]
PS = [
    [[1, 2, 0], [0, 1, 0], [0, 0, 1]],
    [[1, 0, 1], [1, 1, 0], [0, 1, 1]],
    [[2, 0, 0], [0, -3, 1], [0, 1, 0]],
]


def check_inertia_under_congruence():
    """The signature found by exact congruence diagonalisation is unchanged by P^T M P for
    invertible P, and r is the nullity of M."""
    Ms, Ps = MS, PS
    expected = [(1, 1, 1), (2, 1, 0), (2, 1, 0), (1, 0, 2), (1, 2, 0)]
    ok = True
    tested = 0
    for M, exp in zip(Ms, expected):
        s = GA.congruence_signature(M)
        ok = ok and s == exp
        ok = ok and s[0] + s[1] == GA.mat_rank(GA.frac_matrix(M))
        ok = ok and s[2] == len(S.nullspace(M))
        for P in Ps:
            ok = ok and GA.mat_rank(GA.frac_matrix(P)) == 3
            C = GA.mat_mul(transpose(GA.frac_matrix(P)), GA.mat_mul(GA.frac_matrix(M), GA.frac_matrix(P)))
            ok = ok and GA.congruence_signature(C) == exp
            tested += 1
    ok = ok and tested == 15
    GA.check("signature (p, q, r) invariant under congruence; r = nullity, p + q = rank", ok)
    return ok
