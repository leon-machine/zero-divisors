from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def check_involutions_on_products_and_grades():
    premise("std-algebra.functoriality")
    premise("std-algebra.existence-uniqueness")
    premise("std-algebra.grade-decomposition")
    ok = True
    tested = 0
    for p, q, r in S.signatures(4):
        sq = GA.sig(p, q, r)
        n = len(sq)
        x, y = S.sample(n, 3), S.sample(n, 4)
        xy = GA.mul(x, y, sq)
        ok = ok and GA.eq(GA.grade_inv(xy), GA.mul(GA.grade_inv(x), GA.grade_inv(y), sq))
        ok = ok and GA.eq(GA.reverse(xy), GA.mul(GA.reverse(y), GA.reverse(x), sq))
        ok = ok and GA.eq(S.conj(xy), GA.mul(S.conj(y), S.conj(x), sq))
        for f in (GA.grade_inv, GA.reverse, S.conj):
            ok = ok and GA.eq(f(f(x)), x)
        ok = ok and GA.eq(GA.grade_inv(GA.reverse(x)), GA.reverse(GA.grade_inv(x)))
        for k in range(n + 1):
            xk = S.grade(x, k)
            ok = ok and GA.eq(GA.grade_inv(xk), GA.scal((-1) ** k, xk))
            ok = ok and GA.eq(GA.reverse(xk), GA.scal((-1) ** (k * (k - 1) // 2), xk))
            ok = ok and GA.eq(S.conj(xk), GA.scal((-1) ** (k * (k + 1) // 2), xk))
        tested += 1
    # reversion of a product of vectors reverses the order (a non-orthogonal triple)
    sq = GA.sig(1, 2, 1)
    a, b, c = S.sample_vec(4, 1), S.sample_vec(4, 2), S.sample_vec(4, 6)
    ok = ok and GA.eq(GA.reverse(GA.mul(GA.mul(a, b, sq), c, sq)), GA.mul(GA.mul(c, b, sq), a, sq))
    # control: reversion is not an automorphism
    ok = ok and not GA.eq(GA.reverse(GA.mul(GA.gen(0), GA.gen(1), sq)), GA.mul(GA.gen(0), GA.gen(1), sq))
    ok = ok and tested == 34
    GA.check("grade involution automorphism, reversion and conjugation anti-automorphisms; signs on each grade", ok)
    return ok
