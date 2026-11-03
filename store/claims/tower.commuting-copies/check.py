"""tower.commuting-copies: exact checks.

Floor T_k = Cl(p+k, q+k) over the ground Cl(p,q) in GA.py's blade engine, with the tower layout:
indices 0..n-1 ground (p squares +1, then q squares -1), plane j at n+2(j-1) (e_j, +1) and
n+2j-1 (f_j, -1). Omega_k = (e_1 f_1)...(e_k f_k); twisted generators x^(k) = x Omega_k.
Grounds: every (p,q) with n <= 3 and k = 1, 2, plus the physical floor (1,3), k = 2 (dim 256);
the matrix-algebra clause (2), which does not depend on the ground, on six of these floors.
(1) A_k = Cl(p,q): the twisted generators satisfy the ground relations ((x^(k))^2 = x^2, distinct
    ones anticommute), the twisted image of each ground blade x_I is exactly x_I Omega^(|I| mod 2),
    and the 2^n images are independent (rank 2^n), so x -> x^(k) is injective on Cl(p,q).
(2) B_k = Cl(k,k) = Mat_{2^k}(R): the plane generators satisfy the split relations and their 4^k
    blades are independent; with v_j = (e_j+f_j)/2, w_j = (e_j-f_j)/2 and P = prod_j v_j w_j,
    P is idempotent, the corner P B P is R P (rank 1), the left ideal B P has dimension 2^k, and
    left multiplication by the 4^k plane blades on B P has rank 4^k = dim End(B P). So B_k acts
    faithfully and fully on a 2^k-dimensional space: B_k = Mat_{2^k}(R).
(3) A_k and B_k commute elementwise (every twisted generator against every plane generator;
    control: the untwisted x does not commute with e_1), and the 2^n * 4^k products a_I b_J of
    A-blades and B-blades have rank 2^(n+2k) = dim T_k, so A_k (x) B_k -> T_k is an isomorphism.
The compatibility with the tower embeddings "up to the twist" is the content of
tower.grade-twist-when-it-inner and tower.compatibility-connecting-maps-transported, checked there.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

CASES = [((p, n - p), k) for n in range(4) for p in range(n + 1) for k in (1, 2)] + [((1, 3), 2)]
CASES_B = [((0, 0), 1), ((0, 0), 2), ((1, 0), 2), ((0, 1), 1), ((1, 1), 2), ((1, 3), 1)]


def floor(p, q, k):
    return tuple([1] * p + [-1] * q + [1, -1] * k)


def span_rank(elems, m):
    blades = GA.all_blades(m)
    return GA.rank_of_vectors([[x.get(b, F(0)) for b in blades] for x in elems])


def setup(p, q, k):
    n = p + q
    S = floor(p, q, k)
    Om = GA.sc(1)
    for j in range(k):
        Om = GA.mul(Om, GA.mul(GA.gen(n + 2 * j), GA.gen(n + 2 * j + 1), S), S)
    tw = [GA.mul(GA.gen(i), Om, S) for i in range(n)]
    planes = list(range(n, n + 2 * k))
    return n, S, Om, tw, planes


def subsets(xs):
    """All subsets of xs (as sorted tuples), by size."""
    out = []
    for r in range(len(xs) + 1):
        out.extend(combinations(xs, r))
    return out


def unit_blade(J):
    """The basis blade e_J as a multivector."""
    return {J: F(1)}


def blade_product(gens, I, S):
    out = GA.sc(1)
    for i in I:
        out = GA.mul(out, gens[i], S)
    return out


def check_twisted_ground_copy():
    premise("tower.volume-elements-planes")
    for (p, q), k in CASES:
        n, S, Om, tw, _ = setup(p, q, k)
        for i in range(n):
            assert GA.eq(GA.mul(tw[i], tw[i], S), GA.sc(S[i]))
            for j in range(i + 1, n):
                assert GA.anticommutes(tw[i], tw[j], S)
        images = []
        for I in GA.all_blades(n):
            img = blade_product(tw, I, S)
            want = {I: F(1)} if len(I) % 2 == 0 else GA.mul({I: F(1)}, Om, S)
            assert GA.eq(img, want), ((p, q), k, I)
            images.append(img)
        assert span_rank(images, n + 2 * k) == 2 ** n
    return True


def check_plane_algebra_is_full_matrix_algebra():
    premise("transport.rule-1-morita-trivial")
    for (p, q), k in CASES_B:
        n, S, _, _, planes = setup(p, q, k)
        m = n + 2 * k
        for a in planes:
            assert GA.eq(GA.mul(GA.gen(a), GA.gen(a), S), GA.sc(1 if (a - n) % 2 == 0 else -1))
            for b in planes:
                if a < b:
                    assert GA.anticommutes(GA.gen(a), GA.gen(b), S)
        bl = []
        for r in range(2 * k + 1):
            bl.extend(combinations(planes, r))
        Bbl = [{J: F(1)} for J in bl]
        assert span_rank(Bbl, m) == 4 ** k
        P = GA.sc(1)
        for j in range(k):
            e, f = GA.gen(n + 2 * j), GA.gen(n + 2 * j + 1)
            v = GA.scal(F(1, 2), GA.add(e, f))
            w = GA.scal(F(1, 2), GA.sub(e, f))
            P = GA.mul(P, GA.mul(v, w, S), S)
        assert GA.eq(GA.mul(P, P, S), P)
        corner = [GA.mul(GA.mul(P, b, S), P, S) for b in Bbl]
        assert span_rank(corner, m) == 1
        left = [GA.mul(b, P, S) for b in Bbl]
        assert span_rank(left, m) == 2 ** k
        # basis of B P, then the matrices of left multiplication by each plane blade on it
        basis = []
        for x in left:
            if span_rank(basis + [x], m) > len(basis):
                basis.append(x)
        allb = GA.all_blades(m)
        ops = []
        for b in Bbl:
            ops.append([c for x in basis for c in [GA.mul(b, x, S).get(bb, F(0)) for bb in allb]])
        assert len(basis) == 2 ** k
        assert GA.rank_of_vectors(ops) == 4 ** k
    return True


def check_commuting_copies_tensor_isomorphism():
    premise("tower.volume-elements-planes")
    for (p, q), k in CASES:
        n, S, Om, tw, planes = setup(p, q, k)
        m = len(S)
        for x in tw:
            for a in planes:
                assert GA.commutes(x, GA.gen(a), S)
        if n:
            assert not GA.commutes(GA.gen(0), GA.gen(n), S)
        bl = subsets(planes)
        prods = []
        for I in GA.all_blades(n):
            aI = blade_product(tw, I, S)
            for J in bl:
                prods.append(GA.mul(aI, unit_blade(J), S))
        assert len(prods) == 2 ** n * 4 ** k
        assert span_rank(prods, m) == 2 ** (n + 2 * k)
    return True
