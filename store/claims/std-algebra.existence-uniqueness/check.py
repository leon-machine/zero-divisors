from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


GRAMS = [
    [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
    [[0, 1, 0], [1, 0, 0], [0, 0, 1]],
    [[2, 1, 0], [1, 0, 3], [0, 3, -1]],
    [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
]


def states(n):
    out = []
    for k in range(n + 1):
        for I in combinations(range(n), k):
            out.append({frozenset(I): F(1)})
    return out


VS = [[1, 0, 0], [1, 2, -1], [0, 3, 1], [2, -1, 1]]


def check_model_squares_to_form():
    premise("std-algebra.polarisation")
    vs = VS
    ok = True
    tested = 0
    qs = []
    for G in GRAMS:
        n = len(G)
        for v in vs:
            v = [F(a) for a in v]
            Qv = sum(F(G[i][j]) * v[i] * v[j] for i in range(n) for j in range(n))
            qs.append(Qv)
            for st in states(n):
                lhs = GA.ext_c(v, G, GA.ext_c(v, G, st))
                rhs = {k: Qv * c for k, c in st.items() if Qv != 0}
                ok = ok and GA.ext_state_eq(lhs, rhs)
                tested += 1
    ok = ok and qs == [1, -3, -9, 3, 0, 5, 1, -3, 2, -7, 17, -3, 0, -4, 6, -2]
    ok = ok and tested == 128
    GA.check("c(v)^2 = Q(v) on every basis state of the exterior model, four Gram matrices", ok)
    return ok
