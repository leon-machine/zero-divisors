from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


GRAMS_B = [
    [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[2, 1, 0], [1, 0, 3], [0, 3, -1]],
    [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]],
    [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
]


def check_symbol_images_independent():
    """For several Gram matrices, degenerate and non-diagonal included, the symbols of the
    2^n increasing products are linearly independent in the exterior algebra."""
    premise("std-algebra.existence-uniqueness")
    premise("std-algebra.vector-squares")
    grams = GRAMS_B
    ok = True
    nterms = 0
    dims = []
    for G in grams:
        n = len(G)
        keys = [frozenset(I) for k in range(n + 1) for I in combinations(range(n), k)]
        rows = []
        for k in range(n + 1):
            for I in combinations(range(n), k):
                st = GA.ext_sigma_blade(list(I), G, n)
                rows.append([st.get(K, F(0)) for K in keys])
                # leading term: the wedge of the same indices, coefficient 1
                ok = ok and st.get(frozenset(I), F(0)) == 1
                ok = ok and all(len(K) <= k for K in st)
                nterms += len(st)
        dims.append(GA.rank_of_vectors(rows))
    ok = ok and dims == [8, 8, 8, 16, 16]
    ok = ok and nterms == 94
    # control: the symbol of e_0 e_0 in a non-null direction is a scalar, not a new basis element
    st = GA.ext_sigma_blade([0, 0], [[3, 0], [0, 1]], 2)
    ok = ok and st == {frozenset(): F(3)}
    GA.check("symbols of the increasing products are triangular and independent: dim = 2^n", ok)
    return ok
