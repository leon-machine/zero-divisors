from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def sorting_sign(I, J):
    return (-1) ** sum(1 for i in I for j in J if i > j)


def check_blade_table():
    premise("std-algebra.vector-squares")
    premise("std-algebra.blade-basis")
    ok = True
    tested = 0
    for p, q, r in S.signatures(4):
        sq = GA.sig(p, q, r)
        n = len(sq)
        bl = GA.all_blades(n)
        for I in bl:
            for J in bl:
                c, K = GA.blade_mul(I, J, sq)
                exp_c = F(sorting_sign(I, J))
                for i in set(I) & set(J):
                    exp_c *= sq[i]
                exp_K = tuple(sorted(set(I) ^ set(J))) if exp_c != 0 else ()
                ok = ok and c == exp_c and K == exp_K
                tested += 1
    ok = ok and tested == 3 * 4 + 6 * 16 + 10 * 64 + 15 * 256
    GA.check("e_I e_J = sorting sign x product of shared squares x e_(I sym diff J), all (p,q,r) with n <= 4", ok)
    return ok


def check_anticommute_iff_orthogonal():
    premise("std-algebra.vector-squares")
    premise("std-algebra.blade-basis")
    ok = True
    hits = 0
    for p, q, r in S.signatures(3):
        sq = GA.sig(p, q, r)
        n = len(sq)
        vs = [S.vec(c) for c in ([1, 0, 0], [0, 1, 0], [1, 1, 0], [1, -1, 1], [0, 1, 1])]
        vs = [{b: c for b, c in v.items() if b[0] < n} for v in vs]
        for u in vs:
            for v in vs:
                anti = GA.anticommutes(u, v, sq)
                orth = GA.dot(u, v, sq) == 0
                ok = ok and anti == orth
                hits += 1 if anti else 0
    ok = ok and hits == 237
    GA.check("uv = -vu exactly when B(u, v) = 0, all (p,q,r) with n <= 3", ok)
    return ok
