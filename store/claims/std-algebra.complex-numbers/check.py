from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise

GRID = [(1, 0), (0, 1), (2, -3), (-1, 4), (3, 5)]


def check_two_copies_of_the_complex_numbers():
    premise("std-algebra.orthogonal-anticommute")
    premise("std-algebra.z2-grading")
    ok = True
    pairs = 0
    for sq, u in ((GA.sig(0, 1), GA.gen(0)), (GA.sig(2, 0), GA.mul(GA.gen(0), GA.gen(1), GA.sig(2, 0)))):
        ok = ok and GA.eq(GA.mul(u, u, sq), GA.sc(-1))
        for a, b in GRID:
            for c, d in GRID:
                x = GA.add(GA.sc(a), GA.scal(b, u))
                y = GA.add(GA.sc(c), GA.scal(d, u))
                z = GA.qi(a, b) * GA.qi(c, d)
                ok = ok and GA.eq(GA.mul(x, y, sq), GA.add(GA.sc(z.re), GA.scal(z.im, u)))
                pairs += 1
    # Cl(0,1) as a 1x1 complex matrix algebra: real dimension 2
    ok = ok and S.check_matrix_rep([[[GA.QI(0, 1)]]], GA.sig(0, 1), 2)
    # the even part of Cl(2,0) is spanned by 1 and e_1 e_2, and e_1 (a + b e_1 e_2) = a e_1 + b e_2
    sq = GA.sig(2, 0)
    ok = ok and [b for b in GA.all_blades(2) if len(b) % 2 == 0] == [(), (0, 1)]
    w = GA.mul(GA.gen(0), GA.add(GA.sc(3), GA.scal(4, GA.mul(GA.gen(0), GA.gen(1), sq))), sq)
    ok = ok and GA.eq(w, S.vec([3, 4]))
    ok = ok and pairs == 50
    GA.check("Cl(0,1) and the even part of Cl(2,0) multiply as the complex numbers", ok)
    return ok
