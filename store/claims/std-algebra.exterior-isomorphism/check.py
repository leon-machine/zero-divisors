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


GRAM_NONDIAG = [[2, 1, 0], [1, 0, 3], [0, 3, -1]]


def ext_antisym_symbol(I, G, n):
    """Symbol (action on 1) of the antisymmetrised product of basis vectors e_I in the model of G."""
    out = {}
    for perm in permutations(I):
        sign = 1
        for x in range(len(perm)):
            for y in range(x + 1, len(perm)):
                if perm[x] > perm[y]:
                    sign = -sign
        st = GA.ext_sigma_blade(list(perm), G, n)
        for K, c in st.items():
            out[K] = out.get(K, F(0)) + sign * c
    fact = 1
    for i in range(2, len(I) + 1):
        fact *= i
    return {K: c / fact for K, c in out.items() if c != 0}


def check_outer_product_is_exterior():
    premise("std-algebra.blade-basis")
    premise("std-algebra.grade-decomposition")
    premise("std-algebra.orthogonal-anticommute")
    premise("std-algebra.existence-uniqueness")
    premise("std-algebra.sylvester-inertia")
    ok = True
    tested = 0
    # structure constants on blades: the same for every signature with the same n
    for n in range(1, 5):
        table = None
        for p, q, r in [s for s in S.signatures(4) if sum(s) == n]:
            sq = GA.sig(p, q, r)
            bl = GA.all_blades(n)
            t = [S.outer({I: F(1)}, {J: F(1)}, sq) for I in bl for J in bl]
            for I in bl:
                for J in bl:
                    w = S.outer({I: F(1)}, {J: F(1)}, sq)
                    if set(I) & set(J):
                        ok = ok and w == {}
                    else:
                        ok = ok and len(w) == 1 and tuple(sorted(I + J)) in w
            ok = ok and (table is None or t == table)
            table = t
            tested += 1
    # associativity and v ^ v = 0 on sampled elements
    for p, q, r in S.signatures(4)[19:]:
        sq = GA.sig(p, q, r)
        x, y, z = smp(4, 1), smp(4, 2), smp(4, 3)
        ok = ok and GA.eq(S.outer(S.outer(x, y, sq), z, sq), S.outer(x, S.outer(y, z, sq), sq))
        v = smpv(4, 5)
        ok = ok and S.outer(v, v, sq) == {}
        # iterated outer product of vectors = antisymmetrised product
        vs = [smpv(4, s) for s in (1, 2, 4)]
        w = S.outer(S.outer(vs[0], vs[1], sq), vs[2], sq)
        anti = {}
        for perm in permutations(range(3)):
            sign = 1
            for i in range(3):
                for j in range(i + 1, 3):
                    if perm[i] > perm[j]:
                        sign = -sign
            prod = GA.mul(GA.mul(vs[perm[0]], vs[perm[1]], sq), vs[perm[2]], sq)
            anti = GA.add(anti, GA.scal(F(sign, 6), prod))
        ok = ok and GA.eq(w, anti)
        tested += 1
    # the symbol map of the exterior model with a non-diagonal Gram matrix sends the
    # antisymmetrised product of basis vectors to their wedge
    G = GRAM_NONDIAG
    for k in range(4):
        for I in combinations(range(3), k):
            st = ext_antisym_symbol(I, G, 3)
            ok = ok and st == {frozenset(I): F(1)}
            tested += 1
    # control: the plain symbol of a product of non-orthogonal basis vectors has a lower term
    ok = ok and GA.ext_sigma_blade([0, 1], G, 3).get(frozenset(), F(0)) == 1
    ok = ok and tested == 34 + 15 + 8
    GA.check("(Cl, ^) has the exterior structure constants for every signature; associative; symbol map", ok)
    return ok
