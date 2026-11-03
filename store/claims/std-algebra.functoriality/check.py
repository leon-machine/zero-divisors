from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def extend(images, sq_target):
    """The linear map on blades defined by e_I -> f(e_{i1}) ... f(e_{ik})."""
    def F_(x):
        out = {}
        for b, c in x.items():
            y = GA.sc(1)
            for i in b:
                y = GA.mul(y, images[i], sq_target)
            out = GA.add(out, GA.scal(c, y))
        return out
    return F_


def check_isometry_extends_multiplicatively():
    premise("std-algebra.existence-uniqueness")
    premise("std-algebra.blade-basis")
    # a rational boost of R^{2,1}: (5/4, 3/4) mixes e0 and e2 (Q(e2) = -1); e1 fixed
    sq = GA.sig(2, 1)
    boost = [S.vec([F(5, 4), 0, F(3, 4)]), S.vec([0, 1, 0]), S.vec([F(3, 4), 0, F(5, 4)])]
    # a degenerate isometry R^{1,0,1}: e0 -> e0 + e1 (e1 null), e1 -> 2 e1
    sqd = GA.sig(1, 0, 1)
    shear = [S.vec([1, 1]), S.vec([0, 2])]
    ok = True
    tested = 0
    for sqx, ims in ((sq, boost), (sqd, shear)):
        n = len(sqx)
        ok = ok and all(GA.dot(ims[i], ims[i], sqx) == sqx[i] for i in range(n))
        ok = ok and all(GA.dot(ims[i], ims[j], sqx) == 0 for i in range(n) for j in range(n) if i != j)
        f = extend(ims, sqx)
        bl = GA.all_blades(n)
        for a in bl:
            for b in bl:
                x, y = {a: F(1)}, {b: F(1)}
                ok = ok and GA.eq(f(GA.mul(x, y, sqx)), GA.mul(f(x), f(y), sqx))
                tested += 1
        ok = ok and S.span_rank([f({b: F(1)}) for b in bl], n) == 2 ** n
    # control: scaling by 2 is not an isometry, and its extension is not multiplicative
    g = extend([S.vec([2, 0, 0]), S.vec([0, 2, 0]), S.vec([0, 0, 2])], sq)
    e0 = GA.gen(0)
    ok = ok and not GA.eq(g(GA.mul(e0, e0, sq)), GA.mul(g(e0), g(e0), sq))
    ok = ok and tested == 64 + 16
    GA.check("isometries extend to injective homomorphisms (a boost of R^{2,1}, a degenerate shear)", ok)
    return ok
