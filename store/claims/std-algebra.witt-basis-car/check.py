from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise

SIGS = [(1, 1, 0), (2, 2, 0), (3, 3, 0), (2, 2, 1)]
HALF = F(1, 2)
# control: two vectors of the same plane that are not a Witt pair (B = 1/4)
CONTROL = ({(0,): F(1, 2), (1,): F(1, 2)}, {(0,): F(1, 4), (1,): F(-1, 4)})


def check_null_pairs_satisfy_the_car():
    premise("std-algebra.vector-squares")
    ok = True
    relations = 0
    for p, q, r in SIGS:
        sq = GA.sig(p, q, r)
        k = p
        half = HALF
        vs = [{(i,): half, (k + i,): half} for i in range(k)]
        ws = [{(i,): half, (k + i,): -half} for i in range(k)]
        for i in range(k):
            ok = ok and GA.mul(vs[i], vs[i], sq) == {} and GA.mul(ws[i], ws[i], sq) == {}
            for j in range(k):
                d = GA.sc(1) if i == j else {}
                ok = ok and GA.add(GA.mul(vs[i], vs[j], sq), GA.mul(vs[j], vs[i], sq)) == {}
                ok = ok and GA.add(GA.mul(ws[i], ws[j], sq), GA.mul(ws[j], ws[i], sq)) == {}
                ok = ok and GA.eq(GA.add(GA.mul(vs[i], ws[j], sq), GA.mul(ws[j], vs[i], sq)), d)
                relations += 3
        Ns = [GA.mul(ws[i], vs[i], sq) for i in range(k)]
        for i in range(k):
            ok = ok and GA.eq(GA.mul(Ns[i], Ns[i], sq), Ns[i])
            ok = ok and GA.eq(GA.add(Ns[i], GA.mul(vs[i], ws[i], sq)), GA.sc(1))
            for j in range(k):
                ok = ok and GA.commutes(Ns[i], Ns[j], sq)
    ok = ok and relations == 3 * (1 + 4 + 9 + 4)
    sq = GA.sig(1, 1)
    a, b = CONTROL
    ok = ok and GA.dot(a, b, sq) == F(1, 4)
    ok = ok and not GA.eq(GA.add(GA.mul(a, b, sq), GA.mul(b, a, sq)), GA.sc(1))
    GA.check("null Witt pairs satisfy the CAR in Cl(k,k), k = 1, 2, 3, and in Cl(2,2,1); number elements are commuting idempotents", ok)
    return ok
