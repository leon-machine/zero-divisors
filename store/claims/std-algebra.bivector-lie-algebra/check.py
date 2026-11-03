from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def check_commutators_and_skewness():
    premise("std-algebra.grade-decomposition")
    premise("std-algebra.involution-properties")
    premise("std-algebra.z2-grading")
    premise("std-algebra.vector-squares")
    premise("primer.centre")
    ok = True
    ranks = []
    for p, q, r in S.signatures(4):
        sq = GA.sig(p, q, r)
        n = len(sq)
        if n < 2:
            continue
        A, C = S.sample(n, 3, grades_=(2,)), S.sample(n, 6, grades_=(2,))
        x, y = S.sample_vec(n, 2), S.sample_vec(n, 4)
        AC = GA.sub(GA.mul(A, C, sq), GA.mul(C, A, sq))
        ok = ok and GA.eq(AC, GA.scal(2, S.grade(GA.mul(A, C, sq), 2)))
        Ax = GA.sub(GA.mul(A, x, sq), GA.mul(x, A, sq))
        Ay = GA.sub(GA.mul(A, y, sq), GA.mul(y, A, sq))
        ok = ok and GA.eq(Ax, GA.scal(2, S.grade(GA.mul(A, x, sq), 1)))
        ok = ok and GA.dot(Ax, y, sq) + GA.dot(x, Ay, sq) == 0
        X, Y = S.sample(n, 1), S.sample(n, 5)
        ok = ok and S.grade(GA.mul(X, Y, sq), 0) == S.grade(GA.mul(Y, X, sq), 0)
        # the map from bivectors to End(V): rank
        rows = []
        for b in GA.all_blades(n):
            if len(b) == 2:
                img = [S.grade(GA.sub(GA.mul({b: F(1)}, GA.gen(i), sq), GA.mul(GA.gen(i), {b: F(1)}, sq)), 1)
                       for i in range(n)]
                rows.append([img[i].get((j,), F(0)) for i in range(n) for j in range(n)])
        ranks.append((r, GA.rank_of_vectors(rows)))
    ok = ok and all(rk == n * (n - 1) // 2 for (r, rk), n in zip(ranks, [2] * 6 + [3] * 10 + [4] * 15) if r == 0)
    ok = ok and [rk for r, rk in ranks if r > 0] == [1, 1, 0, 3, 3, 3, 2, 2, 0, 6, 6, 6, 6, 5, 5, 5, 3, 3, 0]
    ok = ok and len(ranks) == 31
    GA.check("bivector commutators are bivectors, A x x is a skew vector map, rank C(n,2) when nondegenerate", ok)
    return ok
