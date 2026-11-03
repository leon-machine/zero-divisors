"""dark-matter.direction-nesting-adds-algebra: exact checks in GA.py.

Generators are numbered e_0 .. e_4 as in the statement; GA.sig(p, q) puts the p generators of
square +1 first, so e_0 is the timelike generator of Cl(1,4) and Cl(1,3), and e_0, e_1, e_2, e_3
of Cl(4,1) square to +1 with e_4 of square -1 (the mirror's time).
(i)   Residue 5, Cl(1,4) over Cl(1,3): omega = e0e1e2e3e4 central with omega^2 = +1; P = e0e1e2e3,
      P^2 = -1; e_4 = P^-1 omega; P -> -P with omega fixed gives -e_4; (1 +- omega)/2 central
      orthogonal idempotents summing to 1, with e_4 (1 +- omega)/2 = +-P^-1 (1 +- omega)/2; the
      reflection v -> -e_4 v e_4^-1 fixes e_0..e_3 and P, negates e_4 and sends omega to -omega.
(ii)  Residue 3, Cl(4,1) over the slice {e0, e1, e2, e4}: P = e0e1e2e4 with P^2 = -1, omega central
      with omega^2 = -1, e_3 = -P^-1 omega, and +P^-1 omega after P -> -P.
(iii) Residue 7, Cl(1,2) in Cl(1,3): omega = e0e1e2 central in the slice, omega^2 = -1,
      e_3 = omega^-1 P.
(iv)  Residue 1, Cl(2,1) in Cl(3,1), slice {e0, e1, e3}: omega = e0e1e3 central in the slice,
      omega^2 = +1, e_2 = -omega^-1 P.
The number of modules (two where omega^2 = +1, one where -1) is read from the central idempotents:
(1 +- omega)/2 are nonzero central idempotents exactly when omega^2 = +1.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def prod(gens, sq):
    x = GA.sc(1)
    for i in gens:
        x = GA.mul(x, GA.gen(i), sq)
    return x


def inv_unit(x, sq):
    """inverse of an element with x^2 = +-1"""
    s = GA.mul(x, x, sq)
    assert s in (GA.sc(1), GA.sc(-1))
    return x if s == GA.sc(1) else GA.scal(-1, x)


def is_central_in(x, gens, sq):
    return all(GA.commutes(x, GA.gen(i), sq) for i in gens)


def splits(w, sq):
    """(1 + w)/2 an idempotent (equivalently w^2 = 1)"""
    e = GA.scal(F(1, 2), GA.add(GA.sc(1), w))
    return GA.eq(GA.mul(e, e, sq), e)


def check_residue_five():
    premise("dark-matter.nesting")
    premise("dark-matter.type-residue-what-each-tower-can")
    sq = GA.sig(1, 4)
    P, w = prod([0, 1, 2, 3], sq), prod([0, 1, 2, 3, 4], sq)
    assert is_central_in(w, range(5), sq) and GA.eq(GA.mul(w, w, sq), GA.sc(1))
    assert GA.eq(GA.mul(P, P, sq), GA.sc(-1))
    Pinv = inv_unit(P, sq)
    assert GA.eq(GA.mul(Pinv, w, sq), GA.gen(4))
    assert GA.eq(GA.mul(inv_unit(GA.scal(-1, P), sq), w, sq), GA.scal(-1, GA.gen(4)))
    ep = GA.scal(F(1, 2), GA.add(GA.sc(1), w))
    em = GA.scal(F(1, 2), GA.sub(GA.sc(1), w))
    assert GA.eq(GA.mul(ep, ep, sq), ep) and GA.eq(GA.mul(em, em, sq), em)
    assert GA.eq(GA.mul(ep, em, sq), {}) and GA.eq(GA.add(ep, em), GA.sc(1))
    assert is_central_in(ep, range(5), sq)
    assert GA.eq(GA.mul(GA.gen(4), ep, sq), GA.mul(Pinv, ep, sq))
    assert GA.eq(GA.mul(GA.gen(4), em, sq), GA.scal(-1, GA.mul(Pinv, em, sq)))
    e4inv = inv_unit(GA.gen(4), sq)

    def refl(v):
        return GA.scal(-1, GA.mul(GA.mul(GA.gen(4), v, sq), e4inv, sq))
    images = [refl(GA.gen(i)) for i in range(5)]
    assert all(GA.eq(images[i], GA.gen(i)) for i in range(4))
    assert GA.eq(images[4], GA.scal(-1, GA.gen(4)))
    rP = GA.sc(1)
    for i in range(4):
        rP = GA.mul(rP, images[i], sq)
    rw = GA.mul(rP, images[4], sq)
    assert GA.eq(rP, P) and GA.eq(rw, GA.scal(-1, w))
    return True


def check_residue_three():
    premise("dark-matter.nesting")
    premise("dark-matter.type-residue-what-each-tower-can")
    sq = GA.sig(4, 1)
    P, w = prod([0, 1, 2, 4], sq), prod([0, 1, 2, 3, 4], sq)
    assert is_central_in(w, range(5), sq) and GA.eq(GA.mul(w, w, sq), GA.sc(-1))
    assert not splits(w, sq) and not splits(GA.scal(-1, w), sq)
    assert GA.eq(GA.mul(P, P, sq), GA.sc(-1))
    assert GA.eq(GA.mul(inv_unit(P, sq), w, sq), GA.scal(-1, GA.gen(3)))
    assert GA.eq(GA.mul(inv_unit(GA.scal(-1, P), sq), w, sq), GA.gen(3))
    return True


def check_residue_seven():
    premise("dark-matter.nesting")
    premise("dark-matter.type-residue-what-each-tower-can")
    sq = GA.sig(1, 3)
    w, P = prod([0, 1, 2], sq), prod([0, 1, 2, 3], sq)
    assert is_central_in(w, [0, 1, 2], sq) and GA.eq(GA.mul(w, w, sq), GA.sc(-1))
    assert not splits(w, sq)
    assert GA.eq(GA.mul(inv_unit(w, sq), P, sq), GA.gen(3))
    return True


def check_residue_one():
    premise("dark-matter.nesting")
    premise("dark-matter.type-residue-what-each-tower-can")
    sq = GA.sig(3, 1)
    w, P = prod([0, 1, 3], sq), prod([0, 1, 2, 3], sq)
    assert is_central_in(w, [0, 1, 3], sq) and GA.eq(GA.mul(w, w, sq), GA.sc(1))
    assert splits(w, sq) and splits(GA.scal(-1, w), sq)
    assert GA.eq(GA.mul(inv_unit(w, sq), P, sq), GA.scal(-1, GA.gen(2)))
    return True
