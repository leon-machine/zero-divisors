"""singularity.pseudo-inverse-identities-hyperbolic-atom: exact checks of the computable part.

(1) From the CAR alone (v^2 = 0, v*^2 = 0, v v* + v* v = 1): v v* v = v(1 - v v*) = v - v^2 v* = v,
and likewise v* v v* = v*; checked on several realisations of the CAR, in the hyperbolic atom
Cl(1,1) (e0^2 = 1, e1^2 = -1) with v = (e0 + e1)/2, v* = (e0 - e1)/2 and its rescalings
v -> lambda v, v* -> v*/lambda (lambda = 2, 3/7, -5), and in Cl(2,2) with the pair built from e1, e2.
(2) The atom satisfies the CAR exactly; v is a zero divisor (v v = 0, v != 0) with no inverse:
v Cl(1,1) has dimension 2 < 4 and 1 is not in it (rank goes up when 1 is added); the same for v*.
(3) The identities use the normalisation v v* + v* v = 1: with 2v in place of v and v* unchanged,
(2v) v* (2v) = 4v != 2v.
The uniqueness sentence (the atom as the unit needing no ascent, cited to T1 Rem. 4.5) is a citation
with no finite computable content here and is not checked.
"""
from fractions import Fraction as F
import GA

CL11 = GA.sig(1, 1)


def car(v, vs, sq):
    return (GA.is_zero(GA.mul(v, v, sq)) and GA.is_zero(GA.mul(vs, vs, sq))
            and GA.eq(GA.add(GA.mul(v, vs, sq), GA.mul(vs, v, sq)), GA.sc(1)))


def realisations():
    out = []
    e0, e1 = GA.gen(0), GA.gen(1)
    for lam in (F(1), F(2), F(3, 7), F(-5)):
        v = GA.scal(lam / 2, GA.add(e0, e1))
        vs = GA.scal(1 / (2 * lam), GA.sub(e0, e1))
        out.append((v, vs, CL11))
    sq = GA.sig(2, 2)
    v = GA.scal(F(1, 2), GA.add(GA.gen(1), GA.gen(2)))
    vs = GA.scal(F(1, 2), GA.sub(GA.gen(1), GA.gen(2)))
    out.append((v, vs, sq))
    return out


def check_pseudo_inverse_identities():
    ok = True
    for v, vs, sq in realisations():
        ok = ok and car(v, vs, sq)
        ok = ok and GA.eq(GA.mul(GA.mul(v, vs, sq), v, sq), v)
        ok = ok and GA.eq(GA.mul(GA.mul(vs, v, sq), vs, sq), vs)
    # the derivation's step: v v* v - v = -v^2 v* = 0, using v v* + v* v = 1
    v, vs, sq = realisations()[0]
    step = GA.mul(v, GA.sub(GA.sc(1), GA.mul(v, vs, sq)), sq)
    ok = ok and GA.eq(step, v) and GA.eq(GA.mul(GA.mul(v, vs, sq), v, sq), step)
    # without the normalisation the identity fails: (2v) v* (2v) = 4v, not 2v
    w = GA.scal(2, v)
    ok = ok and GA.eq(GA.mul(GA.mul(w, vs, sq), w, sq), GA.scal(4, v))
    GA.check("v v* v = v and v* v v* = v* on every CAR realisation", ok)
    return ok


def check_atom_is_car_and_zero_divisor():
    e0, e1 = GA.gen(0), GA.gen(1)
    v = GA.scal(F(1, 2), GA.add(e0, e1))
    vs = GA.scal(F(1, 2), GA.sub(e0, e1))
    ok = car(v, vs, CL11) and not GA.is_zero(v)
    ok = ok and GA.eq(GA.add(v, vs), e0) and GA.eq(GA.sub(v, vs), e1)
    bl = GA.all_blades(2)
    for x in (v, vs):
        imgs = [GA.mul(x, {b: F(1)}, CL11) for b in bl]
        vecs = [[y.get(b, F(0)) for b in bl] for y in imgs]
        one = [[F(1) if b == () else F(0) for b in bl]]
        ok = ok and GA.rank_of_vectors(vecs) == 2 and GA.rank_of_vectors(vecs + one) == 3
    GA.check("the hyperbolic atom realises the CAR in Cl(1,1); v and v* are zero divisors, not invertible", ok)
    return ok
