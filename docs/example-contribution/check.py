"""example.null-vector-zero-divisor: exact checks.

For every signature (p, q) with p, q >= 1 and p + q <= 5, the null vectors e_i + e_j and e_i - e_j
(e_i^2 = +1, e_j^2 = -1) are nonzero and square to exactly zero.
"""
import GA
from tp_premise import premise


def check_null_vectors_square_to_zero():
    premise("std-algebra.vector-squares")
    ok, count = True, 0
    for n in range(2, 6):
        for p in range(1, n):
            sq = GA.sig(p, n - p)
            for i in range(p):
                for j in range(p, n):
                    for v in (GA.add(GA.gen(i), GA.gen(j)), GA.sub(GA.gen(i), GA.gen(j))):
                        ok = ok and not GA.is_zero(v) and GA.is_zero(GA.mul(v, v, sq))
                        count += 1
    ok = ok and count == 70
    GA.check("null vectors e_i +- e_j are nonzero and square to zero in every Cl(p,q), p + q <= 5", ok)
    return ok
