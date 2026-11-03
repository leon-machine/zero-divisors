from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def half(a, sign, b, sq):
    """(1 + sign * e_a e_b) / 2"""
    return GA.scal(F(1, 2), GA.add(GA.sc(1), GA.scal(sign, GA.mul(GA.gen(a), GA.gen(b), sq))))


def invertible(x, sq):
    n = len(sq)
    return GA.mat_rank(S.left_matrix(x, sq)) == 2 ** n


# (signature, x, right idempotent e with x e = 0, left idempotent f with f x = 0)
def cases():
    out = []
    sq = GA.sig(1, 1)
    out.append((sq, GA.add(GA.gen(0), GA.gen(1)), half(0, -1, 1, sq), half(0, 1, 1, sq)))
    sq = GA.sig(2, 0)
    x = GA.add(GA.sc(1), GA.gen(0))
    e = GA.scal(F(1, 2), GA.sub(GA.sc(1), GA.gen(0)))
    out.append((sq, x, e, e))
    sq = GA.sig(1, 3)
    out.append((sq, GA.add(GA.gen(0), GA.gen(1)), half(0, -1, 1, sq), half(0, 1, 1, sq)))
    return out


DEGENERATE = [((0, 0, 1), 0), ((1, 0, 1), 1)]


def check_nondegenerate_zero_divisors_kill_idempotents():
    premise("std-algebra.blade-basis")
    premise("primer.classification-real-clifford-algebras")
    ok = True
    ranks = []
    for sq, x, e, f in cases():
        ok = ok and not invertible(x, sq)
        ranks.append(GA.mat_rank(S.left_matrix(x, sq)))
        for g in (e, f):
            ok = ok and GA.eq(GA.mul(g, g, sq), g) and g != {}
        ok = ok and GA.mul(x, e, sq) == {} and GA.mul(f, x, sq) == {}
    ok = ok and ranks == [2, 2, 8]
    # an invertible element: full rank, and its inverse from the linear solve is two-sided
    sq = GA.sig(2, 1)
    y = GA.add(GA.sc(2), GA.gen(0))
    ok = ok and invertible(y, sq)
    yinv = GA.scal(F(1, 3), GA.sub(GA.sc(2), GA.gen(0)))
    ok = ok and GA.eq(GA.mul(y, yinv, sq), GA.sc(1)) and GA.eq(GA.mul(yinv, y, sq), GA.sc(1))
    GA.check("non-invertible elements of Cl(1,1), Cl(2,0), Cl(1,3) annihilate nonzero idempotents on both sides", ok)
    return ok


def check_degenerate_annihilators_hold_no_idempotent():
    premise("std-algebra.blade-basis")
    ok = True
    dims = []
    for (p, q, r), a in DEGENERATE:
        sq = GA.sig(p, q, r)
        n = len(sq)
        x = GA.gen(a)
        ok = ok and not invertible(x, sq)
        L = S.left_matrix(x, sq)
        ns = S.nullspace(L)
        dims.append(len(ns))
        ys = [{b: c for b, c in zip(GA.all_blades(n), v) if c != 0} for v in ns]
        # every product of two annihilator elements vanishes, so every y in r(x) has y^2 = 0,
        # and y^2 = y forces y = 0: r(x) holds no nonzero idempotent
        ok = ok and all(GA.mul(u, v, sq) == {} for u in ys for v in ys)
    ok = ok and dims == [1, 2]
    GA.check("the null generator of Cl(0,0,1) and Cl(1,0,1) is a zero divisor whose annihilator is nilpotent", ok)
    return ok
