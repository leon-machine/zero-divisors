from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise



def check_even_subalgebra_is_clifford():
    premise("std-algebra.z2-grading")
    premise("std-algebra.existence-uniqueness")
    premise("std-algebra.blade-basis")
    premise("std-algebra.orthogonal-anticommute")
    ok = True
    sigs = []
    for p, q, r in S.signatures(5):
        sq = GA.sig(p, q, r)
        n = len(sq)
        choices = ([p + q - 1] if q >= 1 else []) + ([0] if p >= 1 else [])
        for k in choices:
            e = GA.gen(k)
            s = sq[k]
            others = [i for i in range(n) if i != k]
            ims = [GA.mul(GA.gen(i), e, sq) for i in others]
            for a, i in enumerate(others):
                ok = ok and GA.eq(GA.mul(ims[a], ims[a], sq), GA.sc(-s * sq[i]))
                for b in range(a + 1, len(others)):
                    ok = ok and GA.anticommutes(ims[a], ims[b], sq)
            prods = []
            for kk in range(len(others) + 1):
                for idx in combinations(range(len(others)), kk):
                    x = GA.sc(1)
                    for a in idx:
                        x = GA.mul(x, ims[a], sq)
                    prods.append(x)
            ok = ok and all(len(b) % 2 == 0 for x in prods for b in x)
            ok = ok and S.span_rank(prods, n) == 2 ** (n - 1)
            new = [-s * sq[i] for i in others]
            sigs.append((new.count(1), new.count(-1), new.count(0)) == ((p, q - 1, r) if s == -1 else (q, p - 1, r)))
    ok = ok and all(sigs) and len(sigs) == 70
    GA.check("Cl+(p,q,r) = Cl(p,q-1,r) and Cl(q,p-1,r) by u -> ue, every signature with n <= 5", ok)
    return ok
