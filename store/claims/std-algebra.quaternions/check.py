from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def units_even_cl30():
    sq = GA.sig(3, 0)
    e = [GA.gen(a) for a in range(3)]
    return sq, [GA.mul(e[2], e[1], sq), GA.mul(e[0], e[2], sq), GA.mul(e[1], e[0], sq)]


def units_cl02():
    sq = GA.sig(0, 2)
    return sq, [GA.gen(0), GA.gen(1), GA.mul(GA.gen(0), GA.gen(1), sq)]


def check_hamilton_relations():
    premise("std-algebra.orthogonal-anticommute")
    premise("std-algebra.z2-grading")
    premise("std-algebra.blade-basis")
    ok = True
    spans = []
    for sq, (i, j, k) in (units_even_cl30(), units_cl02()):
        m = -1
        for u in (i, j, k):
            ok = ok and GA.eq(GA.mul(u, u, sq), GA.sc(m))
        ok = ok and GA.eq(GA.mul(GA.mul(i, j, sq), k, sq), GA.sc(m))
        ok = ok and GA.eq(GA.mul(i, j, sq), k) and GA.eq(GA.mul(j, i, sq), GA.neg(k))
        ok = ok and GA.eq(GA.mul(j, k, sq), i) and GA.eq(GA.mul(k, i, sq), j)
        spans.append(S.span_rank([GA.sc(1), i, j, k], len(sq)))
    ok = ok and spans == [4, 4]
    # the even part of Cl(3,0) has dimension 4, so the span is all of it
    ok = ok and len([b for b in GA.all_blades(3) if len(b) % 2 == 0]) == 4
    # Cl(0,2) as 2x2 complex matrices with entries in H: generator images square to -1, span real dim 4
    i_ = GA.QI(0, 1)
    qi = [[i_, GA.QI(0)], [GA.QI(0), -i_]]
    qj = S.mat([[0, 1], [-1, 0]])
    ok = ok and S.check_matrix_rep([qi, qj], GA.sig(0, 2), 4)
    GA.check("Hamilton's relations in the even part of Cl(3,0) and in Cl(0,2)", ok)
    return ok
