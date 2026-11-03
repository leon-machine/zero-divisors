"""transport.even-subalgebra-one-dimensional-extension: exact checks.

Cl(p,q) has generators 0..n-1 (n = p + q) and nu is generator n of the extension. For every
nondegenerate (p,q) with 1 <= n <= 5 and both signs of nu^2:
(1) the images f_i = e_i nu are even, pairwise anticommute and square to -Q(e_i) Q(nu): the
relations of Cl(p,q) when nu^2 = -1 and of Cl(q,p) when nu^2 = +1 (and, for p != q, not those of
the other one);
(2) the map phi on blades, phi(e_I) = f_{i_1}...f_{i_k}, is multiplicative on every pair of blades of
the source algebra (Cl(p,q) or Cl(q,p) with its own signature), which is the universal-property
homomorphism, for n <= 4;
(3) its image lies in the even subalgebra and has rank 2^n, equal to the number of even blades of the
extension, so phi is an isomorphism onto Cl^0(p,q+1), respectively Cl^0(p+1,q).
Self-contained lemma: no premises.
"""
from fractions import Fraction as F
from itertools import combinations

import GA


def setting(p, q, nu_sq):
    n = p + q
    big = GA.sig(p, q) + (nu_sq,)
    imgs = [GA.mul(GA.gen(i), GA.gen(n), big) for i in range(n)]
    # source signature: f_i^2 = -Q(e_i) Q(nu)
    src = tuple(-s * nu_sq for s in GA.sig(p, q))
    return n, big, src, imgs


def phi(blade, imgs, big):
    x = GA.sc(1)
    for i in blade:
        x = GA.mul(x, imgs[i], big)
    return x


def apply_phi(x, imgs, big):
    return GA.add(*[GA.scal(c, phi(b, imgs, big)) for b, c in x.items()]) if x else {}


def relations(imgs, big, target):
    n = len(imgs)
    ok = all(GA.eq(GA.mul(imgs[i], imgs[i], big), GA.sc(target[i])) for i in range(n))
    return ok and all(GA.anticommutes(imgs[i], imgs[j], big)
                      for i in range(n) for j in range(i + 1, n))


def even_blade_count(m):
    return sum(1 for b in GA.all_blades(m) if len(b) % 2 == 0)


def check_images_satisfy_the_relations():
    ok = True
    cases = 0
    for n in range(1, 6):
        for p in range(n + 1):
            q = n - p
            for nu_sq in (-1, 1):
                _, big, src, imgs = setting(p, q, nu_sq)
                ok = ok and all(all(len(b) == 2 for b in x) for x in imgs)
                want = GA.sig(p, q) if nu_sq == -1 else tuple(-s for s in GA.sig(p, q))
                ok = ok and src == want and relations(imgs, big, want)
                if p != q:
                    other = tuple(-s for s in want)
                    ok = ok and not relations(imgs, big, other)
                cases += 1
    ok = ok and cases == 40
    GA.check("(e_i nu)^2 = -Q(e_i)Q(nu), anticommuting: Cl(p,q) for nu^2=-1, Cl(q,p) for nu^2=+1", ok)
    return ok


# Sample settings: every signature (p, q) with 1 <= p + q <= 4 (products) or <= 5 (bijectivity), and
# both signs of nu^2.
HOM_SIGNATURES = [(p, n - p) for n in range(1, 5) for p in range(n + 1)]
BIJ_SIGNATURES = [(p, n - p) for n in range(1, 6) for p in range(n + 1)]
NU_SQUARES = (-1, 1)


def check_map_is_a_homomorphism():
    ok = True
    for p, q in HOM_SIGNATURES:
        n = p + q
        for nu_sq in NU_SQUARES:
            _, big, src, imgs = setting(p, q, nu_sq)
            bl = GA.all_blades(n)
            for b1 in bl:
                for b2 in bl:
                    prod_src = GA.mul({b1: F(1)}, {b2: F(1)}, src)
                    lhs = GA.mul(phi(b1, imgs, big), phi(b2, imgs, big), big)
                    ok = ok and GA.eq(lhs, apply_phi(prod_src, imgs, big))
    GA.check("phi(x) phi(y) = phi(xy) on all blade pairs of the source algebra, n <= 4", ok)
    return ok


def check_bijective_onto_even_subalgebra():
    ok = True
    for p, q in BIJ_SIGNATURES:
        n = p + q
        for nu_sq in NU_SQUARES:
            _, big, src, imgs = setting(p, q, nu_sq)
            images = [phi(b, imgs, big) for b in GA.all_blades(n)]
            ok = ok and all(len(b) % 2 == 0 for x in images for b in x)
            amb = GA.all_blades(len(big))
            r = GA.rank_of_vectors([GA.basis_vector_of(x, amb) for x in images])
            ok = ok and r == 2 ** n and even_blade_count(n + 1) == 2 ** n
    GA.check("phi is injective with image the whole even subalgebra (rank 2^n), all p + q <= 5", ok)
    return ok
