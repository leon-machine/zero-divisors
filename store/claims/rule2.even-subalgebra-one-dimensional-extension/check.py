"""rule2.even-subalgebra-one-dimensional-extension: exact checks.

For every nondegenerate (p,q) with 1 <= p + q <= 5 and nu adjoined orthogonally (index n = p + q):
(1) nu^2 = -1: the images e_i nu square to e_i^2 and anticommute pairwise, so e_i -> e_i nu extends
to a homomorphism Cl(p,q) -> Cl(p,q+1); the images are even and the 2^n ordered products of them
span a space of dimension 2^n = dim Cl^0(p,q+1), so the map is an isomorphism onto Cl^0(p,q+1).
(2) nu^2 = +1: the images square to -e_i^2 (the relations of Cl(q,p)) and the same span argument
gives Cl(q,p) = Cl^0(p+1,q).
"""
from fractions import Fraction as F
from itertools import combinations
import GA


def images_data(p, q, nu_sq):
    n = p + q
    sq = GA.sig(p, q) + (nu_sq,)
    nu = GA.gen(n)
    imgs = [GA.mul(GA.gen(i), nu, sq) for i in range(n)]
    return n, sq, imgs


def relations_hold(imgs, sq, target):
    n = len(imgs)
    ok = all(GA.eq(GA.mul(imgs[i], imgs[i], sq), GA.sc(target[i])) for i in range(n))
    ok = ok and all(GA.anticommutes(imgs[i], imgs[j], sq) for i in range(n) for j in range(i + 1, n))
    return ok


def span_of_products(imgs, sq, nbig):
    prods = []
    for k in range(len(imgs) + 1):
        for S in combinations(range(len(imgs)), k):
            x = GA.sc(1)
            for i in S:
                x = GA.mul(x, imgs[i], sq)
            prods.append(x)
    even = all(len(b) % 2 == 0 for x in prods for b in x)
    bl = GA.all_blades(nbig)
    return even, GA.rank_of_vectors([[x.get(b, F(0)) for b in bl] for x in prods])


def even_dim(nbig):
    return sum(1 for b in GA.all_blades(nbig) if len(b) % 2 == 0)


def check_spacelike_nu_gives_cl_pq():
    ok = True
    cases = 0
    for n in range(1, 6):
        for p in range(n + 1):
            q = n - p
            n_, sq, imgs = images_data(p, q, -1)
            ok = ok and relations_hold(imgs, sq, GA.sig(p, q))
            even, r = span_of_products(imgs, sq, n + 1)
            ok = ok and even and r == 2 ** n and even_dim(n + 1) == 2 ** n
            cases += 1
    ok = ok and cases == 20
    GA.check("nu^2 = -1: e_i -> e_i nu is an isomorphism Cl(p,q) -> Cl^0(p,q+1), all p + q <= 5", ok)
    return ok


def check_timelike_nu_gives_cl_qp():
    ok = True
    for n in range(1, 6):
        for p in range(n + 1):
            q = n - p
            n_, sq, imgs = images_data(p, q, 1)
            # relations of Cl(q,p): squares -e_i^2
            ok = ok and relations_hold(imgs, sq, tuple(-s for s in GA.sig(p, q)))
            ok = ok and not relations_hold(imgs, sq, GA.sig(p, q)) if p > 0 else ok
            even, r = span_of_products(imgs, sq, n + 1)
            ok = ok and even and r == 2 ** n
    # one explicit instance: in Cl(2,1) (nu = e2, square -1) and Cl(3,0) (nu = e2, square +1)
    sq = GA.sig(2, 1)
    ok = ok and GA.mul(GA.mul(GA.gen(0), GA.gen(2), sq), GA.mul(GA.gen(0), GA.gen(2), sq), sq) == GA.sc(1)
    sq = GA.sig(3, 0)
    ok = ok and GA.mul(GA.mul(GA.gen(0), GA.gen(2), sq), GA.mul(GA.gen(0), GA.gen(2), sq), sq) == GA.sc(-1)
    GA.check("nu^2 = +1: e_i -> e_i nu is an isomorphism Cl(q,p) -> Cl^0(p+1,q), all p + q <= 5", ok)
    return ok
