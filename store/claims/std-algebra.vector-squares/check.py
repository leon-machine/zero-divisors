from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def check_anticommutator_is_twice_the_polar_form():
    """In the exterior model with non-diagonal and degenerate Gram matrices,
    c(u)c(v) + c(v)c(u) = 2 B(u, v) on every basis state."""
    premise("std-algebra.polarisation")
    grams = [
        [[2, 1, 0], [1, 0, 3], [0, 3, -1]],
        [[0, 1, 0], [1, 0, 0], [0, 0, 0]],
        [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
    ]
    vs = [[1, 2, -1], [0, 3, 1], [2, -1, 1]]
    ok = True
    tested = 0
    for G in grams:
        n = len(G)
        sts = [{frozenset(I): F(1)} for k in range(n + 1) for I in combinations(range(n), k)]
        for u in vs:
            for v in vs:
                uu, vv = [F(a) for a in u], [F(a) for a in v]
                Buv = sum(F(G[i][j]) * uu[i] * vv[j] for i in range(n) for j in range(n))
                for st in sts:
                    a = GA.ext_c(uu, G, GA.ext_c(vv, G, st))
                    b = GA.ext_c(vv, G, GA.ext_c(uu, G, st))
                    s = {k: a.get(k, F(0)) + b.get(k, F(0)) for k in set(a) | set(b)}
                    ok = ok and GA.ext_state_eq(s, {k: 2 * Buv * c for k, c in st.items()})
                    tested += 1
    ok = ok and tested == 216
    GA.check("uv + vu = 2 B(u, v) in the exterior model", ok)
    return ok
