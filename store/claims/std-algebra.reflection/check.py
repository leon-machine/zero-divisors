from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


US = [[1, 0, 0, 0], [1, 2, 0, 0], [0, 1, 1, 1], [2, 0, -1, 1], [1, 1, 1, 0]]
XS = [[0, 1, 0, 0], [1, -1, 2, 0], [3, 0, 1, -2]]


def refl(u, x, sq):
    return GA.sub(x, GA.scal(2 * GA.dot(x, u, sq) / GA.dot(u, u, sq), u))


def check_sandwich_is_reflection():
    premise("std-algebra.inverse-of-vector")
    premise("std-algebra.vector-squares")
    premise("std-algebra.orthogonal-anticommute")
    ok = True
    tested = 0
    for p, q, r in S.signatures(4):
        sq = GA.sig(p, q, r)
        n = len(sq)
        for uc in US:
            u = S.vec(uc[:n])
            Qu = GA.dot(u, u, sq) if u else F(0)
            if Qu == 0:
                continue
            uinv = GA.scal(1 / Qu, u)
            ok = ok and GA.eq(GA.neg(GA.mul(GA.mul(u, u, sq), uinv, sq)), GA.neg(u))
            for xc in XS:
                x = S.vec(xc[:n])
                y = GA.neg(GA.mul(GA.mul(u, x, sq), uinv, sq))
                ok = ok and GA.eq(y, refl(u, x, sq))
                ok = ok and GA.dot(y, y, sq) == GA.dot(x, x, sq)
                ok = ok and GA.eq(refl(u, y, sq), x)
                tested += 1
            # radical vectors are fixed
            for i in range(n):
                if sq[i] == 0:
                    ok = ok and GA.eq(refl(u, GA.gen(i), sq), GA.gen(i))
            # determinant -1: the matrix of s_u on V
            M = [[refl(u, GA.gen(j), sq).get((i,), F(0)) for j in range(n)] for i in range(n)]
            ok = ok and GA.rf_mat_det([[GA.RF.const(a) for a in row] for row in M]).eval(F(0)) == -1
    ok = ok and tested == 411
    # exchange: Q(a) = Q(b) and a - b non-null
    sq = GA.sig(2, 1)
    a, b = S.vec([2, 1, 2]), S.vec([1, 0, 0])
    ok = ok and GA.dot(a, a, sq) == GA.dot(b, b, sq) == 1
    ok = ok and GA.eq(refl(GA.sub(a, b), a, sq), b)
    GA.check("-u x u^-1 = x - 2 B(x,u)/Q(u) u: isometric involution, det -1, fixes the radical", ok)
    return ok
