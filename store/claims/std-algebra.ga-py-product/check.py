from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def check_product_associative_unital_and_relations():
    premise("std-algebra.existence-uniqueness")
    premise("std-algebra.blade-basis")
    premise("std-algebra.orthogonal-anticommute")
    ok = True
    triples = 0
    for p, q, r in S.signatures(3):
        sq = GA.sig(p, q, r)
        n = len(sq)
        bl = [{b: F(1)} for b in GA.all_blades(n)]
        for x in bl:
            ok = ok and GA.eq(GA.mul(GA.sc(1), x, sq), x) and GA.eq(GA.mul(x, GA.sc(1), sq), x)
            for y in bl:
                for z in bl:
                    ok = ok and GA.eq(GA.mul(GA.mul(x, y, sq), z, sq), GA.mul(x, GA.mul(y, z, sq), sq))
                    triples += 1
        for i in range(n):
            ok = ok and GA.eq(GA.mul(GA.gen(i), GA.gen(i), sq), GA.sc(sq[i]))
            for j in range(n):
                if i != j:
                    ok = ok and GA.anticommutes(GA.gen(i), GA.gen(j), sq)
    ok = ok and triples == 3 * 8 + 6 * 64 + 10 * 512
    # n = 4: associativity on sampled general elements
    for p, q, r in S.signatures(4)[19:]:
        sq = GA.sig(p, q, r)
        x, y, z = S.sample(4, 1), S.sample(4, 2), S.sample(4, 3)
        ok = ok and GA.eq(GA.mul(GA.mul(x, y, sq), z, sq), GA.mul(x, GA.mul(y, z, sq), sq))
        triples += 1
    ok = ok and triples == 5528 + 15
    GA.check("GA.mul associative, unital, e_i^2 = Q(e_i), e_i e_j = -e_j e_i: all (p,q,r), n <= 3 exhaustive, n = 4 sampled", ok)
    return ok
