from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def antisym(vs, sq):
    from itertools import permutations
    out = {}
    k = len(vs)
    for perm in permutations(range(k)):
        sign = 1
        for i in range(k):
            for j in range(i + 1, k):
                if perm[i] > perm[j]:
                    sign = -sign
        x = GA.sc(1)
        for i in perm:
            x = GA.mul(x, vs[i], sq)
        out = GA.add(out, GA.scal(sign, x))
    fact = 1
    for i in range(2, k + 1):
        fact *= i
    return GA.scal(F(1, fact), out)


def check_antisymmetrised_products_have_one_grade():
    premise("std-algebra.blade-basis")
    premise("std-algebra.orthogonal-anticommute")
    premise("synthesis.completion-recovers-the-real-clifford-algebras")
    ok = True
    tested = 0
    for p, q, r in S.signatures(4):
        sq = GA.sig(p, q, r)
        n = len(sq)
        for k in range(0, n + 1):
            vs = [S.sample_vec(n, s) for s in range(1, k + 1)]
            x = antisym(vs, sq)
            ok = ok and all(len(b) == k for b in x)
            # independent vectors: the antisymmetrised product is never zero, degenerate forms included
            ok = ok and x != {}
            tested += 1
    # dimensions of the grades: 1, n, C(n,2), ..., summing to 2^n
    dims = [[len([b for b in GA.all_blades(n) if len(b) == k]) for k in range(n + 1)] for n in range(1, 5)]
    ok = ok and dims == [[1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    # scalar and bivector parts of a product of two vectors
    sq = GA.sig(2, 1, 1)
    u, v = S.sample_vec(4, 2), S.sample_vec(4, 5)
    uv = GA.mul(u, v, sq)
    ok = ok and S.grade(uv, 0).get((), F(0)) == GA.dot(u, v, sq)
    ok = ok and GA.eq(S.grade(uv, 2), GA.scal(F(1, 2), GA.sub(uv, GA.mul(v, u, sq))))
    ok = ok and tested == 3 * 2 + 6 * 3 + 10 * 4 + 15 * 5
    GA.check("antisymmetrised products of k vectors are pure grade k; dims are binomial; <uv>_0 and <uv>_2", ok)
    return ok
