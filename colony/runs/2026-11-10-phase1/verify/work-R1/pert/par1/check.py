"""synthesis.chsh-with-parity-even-observables-needs-two-modes-per-party-and-no-klein-twist: exact checks.

Modes are the null pairs of Cl(l,l): generators e_k (square +1, index 2k) and f_k (square -1, index 2k+1),
mode parity p_k = f_k e_k, total parity Gamma = product of the p_k. The dagger sends a blade to its inverse.
An observable is self-adjoint of square one; it is even if it commutes with Gamma.

(1) even elements of disjoint mode sets commute with no twist, the twist does nothing to them, and the even
    observables of one mode are 1 and p only, so a one-mode party gives C^2 = 4;
(2) two modes per party: even observables with C^2 = 4 + 4K and even states with values 8r;
(3) one mode per party with the Klein twist: values 2(c + s) on the even pair state, but through observables
    that anticommute with the parity and are erased by the parity average; without the twist the odd
    observables anticommute and their product has value 0 in every state.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

ONE = GA.sc(F(1))


def dsign(b, sq):
    g = len(b)
    s = (-1) ** (g * (g - 1) // 2)
    for i in b:
        s *= sq[i]
    return s


def dagger(x, sq):
    return {b: c * dsign(b, sq) for b, c in x.items()}


def prod(sq, *xs):
    r = ONE
    for x in xs:
        r = GA.mul(r, x, sq)
    return r


def comm(x, y, sq):
    return GA.sub(GA.mul(x, y, sq), GA.mul(y, x, sq))


def chsh(sq, a1, a2, b1, b2):
    return GA.add(prod(sq, a1, b1), prod(sq, a1, b2), prod(sq, a2, b1), GA.neg(prod(sq, a2, b2)))


def s0(x):
    return x.get((), F(0))


def modes(m):
    sq = tuple(s for _ in range(m) for s in (1, -1))
    e = [GA.gen(2 * k) for k in range(m)]
    f = [GA.gen(2 * k + 1) for k in range(m)]
    p = [GA.mul(f[k], e[k], sq) for k in range(m)]
    return sq, e, f, p, prod(sq, *p)


def is_obs(x, sq):
    return dagger(x, sq) == x and prod(sq, x, x) == ONE


def parity_average(x, gam, sq):
    return GA.scal(F(1, 2), GA.add(x, prod(sq, gam, x, gam)))


def check_even_observables_commute_without_twist_and_one_mode_has_only_the_parity():
    premise("synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product")
    premise("singularity.descent-parity-average")
    sq, e, f, p, gam = modes(3)
    # party A = mode 0, party B = modes 1, 2
    a_idx, b_idx = (0, 1), (2, 3, 4, 5)
    a_blades = [b for k in range(3) for b in combinations(a_idx, k)]
    b_blades = [b for k in range(5) for b in combinations(b_idx, k)]
    a_even = [b for b in a_blades if len(b) % 2 == 0]
    b_even = [b for b in b_blades if len(b) % 2 == 0]
    assert len(a_even) == 2 and len(b_even) == 8
    for a in a_even:
        for b in b_even:
            assert GA.commutes({a: F(1)}, {b: F(1)}, sq)
    assert GA.anticommutes(e[0], e[1], sq)
    # the twist by the parity of A does nothing to even elements of B
    tw = [prod(sq, y, p[0]) for y in (e[1], f[1], e[2], f[2])]
    un = [e[1], f[1], e[2], f[2]]
    for i, j in combinations(range(4), 2):
        assert prod(sq, tw[i], tw[j]) == prod(sq, un[i], un[j])
    # self-adjoint blades of one mode: 1, e, p; the even ones: 1, p
    herm = [b for b in a_blades if dsign(b, sq) == 1]
    assert herm == [(), (0,), (0, 1)]
    assert [b for b in herm if GA.commutes({b: F(1)}, gam, sq)] == [(), (0, 1)]
    x = GA.add(GA.scal(F(3, 5), p[0]), GA.scal(F(4, 5), e[0]))
    assert is_obs(x, sq) and not GA.commutes(x, gam, sq)
    assert parity_average(x, gam, sq) == GA.scal(F(3, 5), p[0])
    # a one-mode party with even observables against a two-mode party with non-commuting even observables
    b1, b2 = p[1], prod(sq, e[1], f[2])
    assert is_obs(b1, sq) and is_obs(b2, sq) and GA.anticommutes(b1, b2, sq)
    for a1, a2 in ((p[0], p[0]), (p[0], GA.neg(p[0])), (ONE, p[0])):
        c = chsh(sq, a1, a2, b1, b2)
        assert prod(sq, c, c) == GA.sc(F(4))
    return True


def check_two_modes_per_party_reach_square_eight_with_even_observables_and_even_states():
    premise("synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product")
    sq, e, f, p, gam = modes(4)
    a1, a2 = p[0], prod(sq, e[0], f[1])
    b1, b2 = p[2], prod(sq, e[2], f[3])
    for o in (a1, a2, b1, b2):
        assert is_obs(o, sq) and GA.commutes(o, gam, sq)
    assert GA.anticommutes(a1, a2, sq) and GA.anticommutes(b1, b2, sq)
    for a in (a1, a2):
        for b in (b1, b2):
            assert GA.commutes(a, b, sq)
    c = chsh(sq, a1, a2, b1, b2)
    k = GA.neg(prod(sq, f[0], f[1], f[2], f[3]))
    assert prod(sq, c, c) == GA.add(GA.sc(F(4)), GA.scal(F(4), k))
    assert is_obs(k, sq) and GA.commutes(k, c, sq) and GA.commutes(k, gam, sq)
    for r in (F(1, 3), F(239, 676)):
        assert 8 * r * r <= 1
        rho = prod(sq, GA.add(ONE, k), GA.add(ONE, GA.scal(r, c)))
        assert dagger(rho, sq) == rho and GA.commutes(rho, gam, sq)
        assert s0(rho) == 1 and s0(prod(sq, rho, c)) == 8 * r and s0(prod(sq, rho, c, c)) == 8
        assert 4 < (8 * r) ** 2 < 8
    return True


def check_twisted_one_mode_split_exceeds_two_only_through_odd_observables():
    premise("synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product")
    premise("singularity.descent-parity-average")
    sq, e, f, p, gam = modes(2)
    tw = e[1]
    for o in (p[0], e[0], p[1], tw):
        assert is_obs(o, sq)
    for a in (p[0], e[0]):
        for b in (p[1], tw):
            assert GA.commutes(a, b, sq)
    assert GA.anticommutes(p[0], e[0], sq) and GA.anticommutes(p[1], tw, sq)
    # the two observables the violation needs are odd: they anticommute with the parity and the average erases them
    for o in (e[0], tw):
        assert GA.anticommutes(o, gam, sq) and parity_average(o, gam, sq) == {}
    # the stored pair state at equal weights, an even pure state
    v = [GA.scal(F(1, 2), GA.add(e[k], f[k])) for k in range(2)]
    w = [GA.scal(F(1, 2), GA.sub(e[k], f[k])) for k in range(2)]
    rho = GA.add(GA.scal(F(1, 4), GA.add(ONE, prod(sq, p[0], p[1]))),
                 GA.scal(F(1, 2), GA.add(prod(sq, w[0], w[1]), prod(sq, v[1], v[0]))))
    assert dagger(rho, sq) == rho and prod(sq, rho, rho) == rho and GA.commutes(rho, gam, sq)
    val = lambda x: 4 * s0(prod(sq, rho, x))
    assert val(ONE) == 1
    assert [val(prod(sq, a, b)) for a in (p[0], e[0]) for b in (p[1], tw)] == [1, 0, 0, 1]
    for (cc, ss, expect) in ((F(3, 5), F(4, 5), F(14, 5)), (F(20, 29), F(21, 29), F(82, 29)),
                             (F(119, 169), F(120, 169), F(478, 169))):
        assert cc * cc + ss * ss == 1
        bp = GA.add(GA.scal(cc, p[1]), GA.scal(ss, tw))
        bm = GA.sub(GA.scal(cc, p[1]), GA.scal(ss, tw))
        assert is_obs(bp, sq) and is_obs(bm, sq)
        c = chsh(sq, p[0], e[0], bp, bm)
        assert val(c) == expect == 2 * (cc + ss) and 4 < expect * expect < 8
        # after the parity average of the observables the square of the CHSH element is 4
        ca = chsh(sq, p[0], parity_average(e[0], gam, sq), parity_average(bp, gam, sq), parity_average(bm, gam, sq))
        assert val(ca) == 2 * cc and val(ca) <= 2
    # without the twist: e_1 and e_2 anticommute, their product is anti-self-adjoint, and has value 0 in a state
    g = prod(sq, e[0], e[1])
    assert GA.anticommutes(e[0], e[1], sq) and dagger(g, sq) == GA.neg(g) and val(g) == 0
    cu = chsh(sq, e[0], p[0], e[1], p[1])
    h = GA.scal(F(1, 2), GA.add(cu, dagger(cu, sq)))
    assert h == GA.add(prod(sq, e[0], p[1]), prod(sq, p[0], e[1]), GA.neg(prod(sq, p[0], p[1])))
    assert prod(sq, h, h) == GA.sc(F(3))
    return True
