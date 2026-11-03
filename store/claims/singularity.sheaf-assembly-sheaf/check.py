"""singularity.sheaf-assembly-sheaf: exact checks of the fibrewise content (GA blade engine).

The sheaf axioms (locality, gluing) are inherited from sections of a bundle and are not computed. The
fibrewise statements are checked on the one-mode fibre Cl(1,1) with the ladder of the completion,
k = lambda (e+ + e-)/2, k^* = (e+ - e-)/(2 lambda) (lambda != 0 stands for the point-dependent normalisation
k^* = nO/(2 nu) of Fact singularity.imported-one-sided-completion-singularity), sigma = k^* k - k k^*:
(1) k^2 = k^*^2 = 0, k k^* + k^* k = 1 at every sample lambda, and sigma = e+e- does not depend on lambda: the
    parity section is constant along the family.
(2) The fibre projection (id + Ad sigma)/2 is idempotent on all four blades with rank 2 at every sample
    (constant rank, so its image is a locally trivial subbundle), and its image is span{1, sigma}, closed under
    products (a subalgebra: multiplication preserves evenness).
(3) Sign insensitivity: (k, k^*) -> (-k, -k^*) leaves sigma, hence the projection, unchanged, while the odd
    part (k itself) changes sign.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ = (1, -1)
LAMBDAS = [F(1), F(2), F(-1, 3), F(5, 7)]
BLADES = GA.all_blades(2)


def ladder(lam):
    k = GA.scal(lam * F(1, 2), GA.add(GA.gen(0), GA.gen(1)))
    ks = GA.scal(F(1, 2) / lam, GA.sub(GA.gen(0), GA.gen(1)))
    return k, ks


def sigma_of(k, ks):
    return GA.sub(GA.mul(ks, k, SQ), GA.mul(k, ks, SQ))


def proj(x, s):
    return GA.scal(F(1, 2), GA.add(x, GA.mul(GA.mul(s, x, SQ), s, SQ)))


def check_parity_section_constant_along_ladder_family():
    premise("singularity.imported-one-sided-completion-singularity")
    ok = True
    for lam in LAMBDAS:
        k, ks = ladder(lam)
        ok = ok and GA.mul(k, k, SQ) == {} and GA.mul(ks, ks, SQ) == {}
        ok = ok and GA.add(GA.mul(k, ks, SQ), GA.mul(ks, k, SQ)) == GA.sc(1)
        ok = ok and sigma_of(k, ks) == {(0, 1): F(1)}
    GA.check("ladder family: CAR at every lambda, sigma = e+e- independent of lambda", ok)
    return ok


def check_even_projection_constant_rank_subalgebra():
    premise("singularity.imported-one-sided-completion-singularity")
    ok = True
    for lam in LAMBDAS:
        s = sigma_of(*ladder(lam))
        imgs = []
        for b in BLADES:
            x = {b: F(1)}
            px = proj(x, s)
            ok = ok and proj(px, s) == px
            imgs.append(px)
        rows = [GA.basis_vector_of(x, BLADES) for x in imgs if x]
        ok = ok and GA.rank_of_vectors(rows) == 2
        ok = ok and proj(GA.sc(1), s) == GA.sc(1) and proj(s, s) == s
        even = [GA.sc(1), s]
        ok = ok and all(proj(GA.mul(x, y, SQ), s) == GA.mul(x, y, SQ) for x in even for y in even)
    GA.check("(id + Ad sigma)/2: idempotent of constant rank 2, image span{1, sigma}, a subalgebra", ok)
    return ok


def check_sign_of_ladder_invisible():
    ok = True
    for lam in LAMBDAS:
        k, ks = ladder(lam)
        s = sigma_of(k, ks)
        s2 = sigma_of(GA.neg(k), GA.neg(ks))
        ok = ok and s2 == s
        ok = ok and all(proj({b: F(1)}, s) == proj({b: F(1)}, s2) for b in BLADES)
        ok = ok and proj(k, s) == {} and GA.mul(GA.mul(s, k, SQ), s, SQ) == GA.neg(k)
    GA.check("(k, k*) -> (-k, -k*) fixes sigma and the projection; k itself is odd", ok)
    return ok
