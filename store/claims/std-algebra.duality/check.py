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


VECS = [[1, 2, 0, -1], [0, 1, 1, 2], [2, 0, -1, 1], [1, 0, 0, 3]]


def null_space(Y, sq):
    n = len(sq)
    cols = [S.coords(S.outer(GA.gen(i), Y, sq), n) for i in range(n)]
    M = [[cols[j][k] for j in range(n)] for k in range(len(cols[0]))]
    return S.nullspace(M)


def check_duality_identities_all_signatures():
    premise("std-algebra.product-decomposition")
    premise("std-algebra.grade-decomposition")
    ok = True
    tested = 0
    for p, q, r in S.signatures(4):
        sq = GA.sig(p, q, r)
        n = len(sq)
        I = S.pseudoscalar(n)
        a = smpv(n, 3)
        X = smp(n, 4)
        XI = GA.mul(X, I, sq)
        ok = ok and GA.eq(S.lc(a, XI, sq), GA.mul(S.outer(a, X, sq), I, sq))
        ok = ok and GA.eq(S.outer(a, XI, sq), GA.mul(S.lc(a, X, sq), I, sq))
        for k in range(n + 1):
            ok = ok and all(len(b) == n - k for b in GA.mul(S.grade(X, k), I, sq))
        tested += 1
    ok = ok and tested == 34
    GA.check("a lc (XI) = (a ^ X) I and a ^ (XI) = (a lc X) I, all (p,q,r) with n <= 4", ok)
    return ok


def check_dual_blade_is_orthogonal_complement():
    premise("std-algebra.pseudoscalar-commutation")
    premise("std-algebra.contraction-expansion")
    premise("std-algebra.blade-subspace")
    ok = True
    tested = 0
    for p, q in ((4, 0), (1, 3), (2, 2)):
        sq = GA.sig(p, q)
        I = S.pseudoscalar(4)
        vs = [S.vec(c) for c in VECS]
        for k in range(1, 4):
            for idx in combinations(range(4), k):
                sub = [vs[i] for i in idx]
                A = GA.sc(1)
                for v in sub:
                    A = S.outer(A, v, sq)
                AI = GA.mul(A, I, sq)
                ns = null_space(AI, sq)
                ok = ok and len(ns) == 4 - k
                for w in ns:
                    wv = {(i,): c for i, c in enumerate(w) if c != 0}
                    ok = ok and all(GA.dot(wv, v, sq) == 0 for v in sub)
                tested += 1
        # duality is injective on each grade
        for k in range(5):
            imgs = [GA.mul({b: F(1)}, I, sq) for b in GA.all_blades(4) if len(b) == k]
            ok = ok and S.span_rank(imgs, 4) == len(imgs)
    # control: in a degenerate algebra duality is not injective
    sq = GA.sig(3, 0, 1)
    ok = ok and GA.mul(GA.gen(3), S.pseudoscalar(4), sq) == {}
    ok = ok and tested == 3 * 14
    GA.check("for r = 0, AI is a blade of [A]^perp and X -> XI is injective on each grade", ok)
    return ok
