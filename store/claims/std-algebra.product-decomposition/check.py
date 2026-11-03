from fractions import Fraction as F
from itertools import combinations, permutations

import GA
import stdalg as S
from tp_premise import premise


def smp(n, seed, grades=None):
    """Deterministic sample element; coefficients ((3 seed + 1)(j + 1) + seed j^2) mod 7 - 3."""
    out = {}
    for j, b in enumerate(GA.all_blades(n)):
        if grades is not None and len(b) not in grades:
            continue
        c = ((3 * seed + 1) * (j + 1) + seed * j * j) % 7 - 3
        if c:
            out[b] = F(c)
    return out


def smpv(n, seed):
    return smp(n, seed, grades=(1,))


def check_vector_times_multivector():
    premise("std-algebra.orthogonal-anticommute")
    premise("std-algebra.grade-decomposition")
    premise("std-algebra.involution-properties")
    ok = True
    tested = 0
    for p, q, r in S.signatures(4):
        sq = GA.sig(p, q, r)
        n = len(sq)
        for seed in range(1, 4):
            a = smpv(n, seed)
            X = smp(n, seed + 3)
            aX = GA.mul(a, X, sq)
            Xa = GA.mul(GA.grade_inv(X), a, sq)
            c, w = S.lc(a, X, sq), S.outer(a, X, sq)
            ok = ok and GA.eq(aX, GA.add(c, w))
            ok = ok and GA.eq(c, GA.scal(F(1, 2), GA.sub(aX, Xa)))
            ok = ok and GA.eq(w, GA.scal(F(1, 2), GA.add(aX, Xa)))
            for k in range(n + 1):
                Xk = S.grade(X, k)
                ok = ok and all(len(b) in (k - 1, k + 1) for b in GA.mul(a, Xk, sq))
            tested += 1
    # a b = B(a, b) + a ^ b for two vectors
    sq = GA.sig(1, 2, 1)
    a, b = smpv(4, 1), smpv(4, 2)
    ok = ok and GA.eq(GA.mul(a, b, sq), GA.add(GA.sc(GA.dot(a, b, sq)), S.outer(a, b, sq)))
    ok = ok and GA.dot(a, b, sq) == -2
    ok = ok and tested == 102
    GA.check("aX = a lc X + a ^ X, with the two symmetrisation formulas; grades k-1 and k+1", ok)
    return ok
