from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


GRAMS = [
    [[1, 0], [0, -1]],
    [[0, 1], [1, 0]],
    [[2, 1, 0], [1, 0, 3], [0, 3, -1]],
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
]
XS = [[1, 2, -1], [0, 3, 1], [-2, 1, 4]]


def check_polarisation():
    grams, xs = GRAMS, XS
    ok = True
    tested = 0
    qs = []
    for G in grams:
        n = len(G)

        def Q(x):
            return sum(F(G[i][j]) * x[i] * x[j] for i in range(n) for j in range(n))

        def B(u, v):
            w = [a + b for a, b in zip(u, v)]
            return (Q(w) - Q(u) - Q(v)) / 2

        for u in xs:
            u = u[:n]
            ok = ok and B(u, u) == Q(u)
            ok = ok and Q([3 * a for a in u]) == 9 * Q(u)
            for v in xs:
                v = v[:n]
                ok = ok and B(u, v) == B(v, u)
                ok = ok and B(u, v) == sum(F(G[i][j]) * u[i] * v[j] for i in range(n) for j in range(n))
                tested += 1
            qs.append(Q(u))
    # control: a non-symmetric matrix gives a form whose polarisation is its symmetric part, not itself
    A = [[0, 2], [0, 0]]
    ok = ok and F(A[0][1] + A[1][0], 2) != A[0][1]
    ok = ok and qs == [-3, -9, 3, 4, 0, -4, -7, 17, 12, 4, 16, 9]
    ok = ok and tested == 36
    GA.check("polar form symmetric, B(v,v) = Q(v), coordinates x^T G x", ok)
    return ok
