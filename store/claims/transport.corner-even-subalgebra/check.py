"""transport.corner-even-subalgebra: exact checks.

Setting: A = Cl(p,q) with p - q = 1 mod 4 (so n = p + q is odd and omega^2 = +1), eps_+- =
(1 +- omega)/2, and B_gamma = Cl(p,q) extended by an orthogonal generator nu (generator n) with
nu^2 = gamma = +-1. Signatures: every (p,q) with p - q = 1 mod 4 and n <= 7 (10 of them).

(1) eps_+ is a central idempotent of A, and phi(a) = eps_+ a is multiplicative on every pair of even
blades with phi(1) = eps_+ acting as the unit of eps_+ A (pairs for n <= 5).
(2) phi is injective on Cl^0 (the images of the 2^(n-1) even blades have rank 2^(n-1)), and its image
is all of eps_+ A: the images eps_+ x of all 2^n blades x of A have the same rank 2^(n-1), and the
span of the even images contains each of them.
(3) eps_+ B_gamma eps_+ = eps_+ A for both gamma: the elements eps_+ x eps_+ over the 2^(n+1) blades of
B_gamma (a blade of A or a blade of A times nu, the decomposition B = A + A nu) span exactly the
space spanned by eps_+ A; the A nu half gives zero because nu eps_+ = eps_- nu.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

HALF = F(1, 2)


def cases():
    out = []
    for n in range(1, 8):
        for p in range(n + 1):
            q = n - p
            if (p - q) % 4 == 1:
                out.append((p, q))
    return out


def eps(n, sign):
    return GA.add(GA.sc(HALF), GA.scal(sign * HALF, {tuple(range(n)): F(1)}))


def vecs(elems, m):
    bl = GA.all_blades(m)
    return [GA.basis_vector_of(x, bl) for x in elems]


# Size limit for the multiplicativity check (all pairs of even blades; n <= 5 keeps it fast).
MAX_N_PRODUCTS = 5


def even_units(n):
    """The even basis blades of Cl(n), each with coefficient 1."""
    return [{b: F(1)} for b in GA.all_blades(n) if len(b) % 2 == 0]


def check_corner_map_is_unital_homomorphism():
    ok = True
    for p, q in cases():
        n = p + q
        if n > MAX_N_PRODUCTS:
            continue
        sq = GA.sig(p, q)
        ep, em = eps(n, 1), eps(n, -1)
        ok = ok and GA.eq(GA.mul(ep, ep, sq), ep) and GA.is_zero(GA.mul(ep, em, sq))
        ok = ok and all(GA.commutes(ep, GA.gen(i), sq) for i in range(n))
        even = even_units(n)
        ok = ok and len(even) == 2 ** (n - 1)
        for a in even:
            pa = GA.mul(ep, a, sq)
            ok = ok and GA.eq(GA.mul(ep, pa, sq), pa) and GA.eq(GA.mul(pa, ep, sq), pa)
            for b in even:
                lhs = GA.mul(pa, GA.mul(ep, b, sq), sq)
                ok = ok and GA.eq(lhs, GA.mul(ep, GA.mul(a, b, sq), sq))
        ok = ok and GA.eq(GA.mul(ep, GA.sc(1), sq), ep)
    GA.check("eps_+ central idempotent; a -> eps_+ a multiplicative and unital on Cl^0, n <= 5", ok)
    return ok


def check_corner_map_is_bijective():
    ok = True
    for p, q in cases():
        n = p + q
        sq = GA.sig(p, q)
        ep = eps(n, 1)
        even_img = [GA.mul(ep, {b: F(1)}, sq) for b in GA.all_blades(n) if len(b) % 2 == 0]
        all_img = [GA.mul(ep, {b: F(1)}, sq) for b in GA.all_blades(n)]
        r_even = GA.rank_of_vectors(vecs(even_img, n))
        r_all = GA.rank_of_vectors(vecs(all_img, n))
        r_both = GA.rank_of_vectors(vecs(even_img + all_img, n))
        ok = ok and r_even == 2 ** (n - 1) and r_all == 2 ** (n - 1) and r_both == r_even
    ok = ok and len(cases()) == 10
    GA.check("eps_+ Cl^0 has rank 2^(n-1) = dim eps_+ A: the corner map is bijective, n <= 7", ok)
    return ok


def check_extension_adds_nothing_to_corner():
    premise("transport.decomposition-commutation")
    premise("transport.ascent-renders-grade-involution-inner")
    ok = True
    for p, q in cases():
        n = p + q
        if n > 5:
            continue
        for gamma in (1, -1):
            big = GA.sig(p, q) + (gamma,)
            nu = GA.gen(n)
            ep, em = eps(n, 1), eps(n, -1)
            ok = ok and GA.eq(GA.mul(nu, ep, big), GA.mul(em, nu, big))
            sandwiches = [GA.mul(GA.mul(ep, {b: F(1)}, big), ep, big) for b in GA.all_blades(n + 1)]
            nu_half = [s for b, s in zip(GA.all_blades(n + 1), sandwiches) if n in b]
            ok = ok and all(GA.is_zero(s) for s in nu_half) and len(nu_half) == 2 ** n
            corner = [GA.mul(ep, {b: F(1)}, big) for b in GA.all_blades(n)]
            r_s = GA.rank_of_vectors(vecs(sandwiches, n + 1))
            r_c = GA.rank_of_vectors(vecs(corner, n + 1))
            r_u = GA.rank_of_vectors(vecs(sandwiches + corner, n + 1))
            ok = ok and r_s == 2 ** (n - 1) and r_c == r_s and r_u == r_s
    GA.check("eps_+ B_gamma eps_+ = eps_+ A for gamma = +-1 (the A nu half vanishes), n <= 5", ok)
    return ok
