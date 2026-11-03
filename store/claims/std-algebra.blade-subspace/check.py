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


VECS = [[1, 2, 0, -1], [0, 1, 1, 2], [2, 0, -1, 1], [1, 3, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1]]


def outer_all(vs, sq):
    x = GA.sc(1)
    for v in vs:
        x = S.outer(x, v, sq)
    return x


def null_dim(Y, sq):
    """dim {x in V : x ^ Y = 0}."""
    n = len(sq)
    cols = [S.coords(S.outer(GA.gen(i), Y, sq), n) for i in range(n)]
    M = [[cols[j][k] for j in range(n)] for k in range(len(cols[0]))]
    return len(S.nullspace(M))


def gram_det(vs, sq):
    G = [[GA.dot(u, v, sq) for v in vs] for u in vs]
    k = len(G)
    tot = F(0)
    for perm in permutations(range(k)):
        sign = 1
        for i in range(k):
            for j in range(i + 1, k):
                if perm[i] > perm[j]:
                    sign = -sign
        t = F(sign)
        for i in range(k):
            t *= G[i][perm[i]]
        tot += t
    return tot


def check_blades_and_subspaces():
    premise("std-algebra.exterior-isomorphism")
    premise("std-algebra.sylvester-inertia")
    premise("std-algebra.involution-properties")
    premise("std-algebra.grade-decomposition")
    ok = True
    tested = 0
    zero_divisors = 0
    for p, q, r in [s for s in S.signatures(4) if sum(s) == 4]:
        sq = GA.sig(p, q, r)
        vs = [S.vec(c) for c in VECS]
        for k in range(1, 5):
            for idx in combinations(range(6), k):
                sub = [vs[i] for i in idx]
                A = outer_all(sub, sq)
                rk = GA.rank_of_vectors([S.coords(v, 4) for v in sub])
                ok = ok and ((A == {}) == (rk < k))
                if A:
                    ok = ok and null_dim(A, sq) == k
                    AA = GA.mul(A, GA.reverse(A), sq)
                    g = gram_det(sub, sq)
                    ok = ok and GA.eq(AA, GA.sc(g))
                    if g == 0:
                        zero_divisors += 1
                        ok = ok and GA.mul(A, GA.reverse(A), sq) == {} and GA.reverse(A) != {}
                    else:
                        inv = GA.scal(1 / g, GA.reverse(A))
                        ok = ok and GA.eq(GA.mul(A, inv, sq), GA.sc(1)) and GA.eq(GA.mul(inv, A, sq), GA.sc(1))
                tested += 1
    # (iii): a 2-vector that is not a blade (e1e2 + e3e4) has a zero null space
    sq = GA.sig(4, 0)
    Y = GA.add(S.blade(0, 1), S.blade(2, 3))
    ok = ok and null_dim(Y, sq) == 0
    ok = ok and null_dim(S.blade(0, 1), sq) == 2
    # (ii): a change of factors multiplies the blade by the determinant
    u, v = S.vec([1, 2, 0, 0]), S.vec([0, 1, 3, 0])
    A = S.outer(u, v, sq)
    A2 = S.outer(GA.add(GA.scal(2, u), v), GA.add(u, GA.scal(-1, v)), sq)
    ok = ok and GA.eq(A2, GA.scal(-3, A))
    ok = ok and tested == 15 * 56
    ok = ok and zero_divisors == 319
    GA.check("blade nonzero iff independent; dim [A] = k; A A~ = Gram det; degenerate blades are zero divisors", ok)
    return ok
