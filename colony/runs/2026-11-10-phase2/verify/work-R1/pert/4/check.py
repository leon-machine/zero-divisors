"""synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects: exact checks.

Cl_Q(p,q) on blades, dagger the blade inverse, tau the scalar part; modes e_k (square +1, index 2k),
f_k (square -1, index 2k+1), p_k = f_k e_k.

(i)   the self-adjoint elements are the span of the blades of square +1 (their number is pinned in six
      signatures), 1 -+ b is half the hermitian square of 1 -+ b, and (sum |c_b|) - s is a combination
      of such squares with non-negative coefficients: 1 is an order unit.
(ii)  an exact relation among effects of one mode forces the weight of the projector with direction
      (3/5, 4/5) in the state sharp on (1 + p)/2 to be 9/10, the Born weight; a weight on projectors
      that is additive on orthogonal pairs only (value (1 + c^3)/2) gives 189/250 and breaks the relation.
(iii) the parity average commutes with the dagger, sends y y^dagger to a sum of two hermitian squares of
      even elements, and an even normalised real functional can be negative on a projector.
(iv)  for an even state the value of the CHSH element of mixed-parity directions is that of its parity
      average X u + Z Gamma, not of the CHSH element of the averaged directions: an even atom gives 14/5
      where the averaged directions give 7/5.
The extension theorem itself (an additive weight on effects is linear) is the proof's.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

ONE = GA.sc(F(1))
HALF = F(1, 2)
SIGS = [(1, 1), (2, 0), (0, 2), (3, 0), (1, 3), (2, 2)]
SEEDS = [[1, 2, 0, -1, 3, 0, 1, 1, -2, 1, 0, 2, 1, -1, 0, 3], [2, 0, 1, 0, 0, 1, 0, -1, 1, 1, 3, 0, 0, -2, 1, 0],
         [0, 1, -1, 2, 0, 2, 0, 1, 1, 0, 0, -1, 2, 0, 1, 1]]
DIR_B1 = (F(3, 5), F(4, 5))
DIR_B2 = (F(4, 5), F(-3, 5))


def dsign(b, sq):
    g = len(b)
    s = (-1) ** (g * (g - 1) // 2)
    for i in b:
        s *= sq[i]
    return s


def dagger(x, sq):
    return {b: c * dsign(b, sq) for b, c in x.items()}


def clean(x):
    return {b: c for b, c in x.items() if c != 0}


def prod(sq, *xs):
    r = ONE
    for x in xs:
        r = GA.mul(r, x, sq)
    return clean(r)


def lin(*terms):
    r = {}
    for c, x in terms:
        r = GA.add(r, GA.scal(F(c), x))
    return clean(r)


def tau(x):
    return x.get((), F(0))


def blade(b):
    return {tuple(b): F(1)}


def element(sq, seed, shift):
    blades = GA.all_blades(len(sq))
    return clean({b: F(seed[(i + shift) % len(seed)]) for i, b in enumerate(blades)})


def modes(m):
    sq = tuple(s for _ in range(m) for s in (1, -1))
    e = [GA.gen(2 * k) for k in range(m)]
    f = [GA.gen(2 * k + 1) for k in range(m)]
    p = [prod(sq, f[k], e[k]) for k in range(m)]
    return sq, e, f, p


def order_unit_report(p, q):
    """(number of self-adjoint blades, whether the order-unit certificate holds on three samples)."""
    sq = GA.sig(p, q)
    blades = GA.all_blades(p + q)
    sa = [b for b in blades if dsign(b, sq) == 1]
    ok = all((dagger(blade(b), sq) == blade(b)) == (prod(sq, blade(b), blade(b)) == ONE) for b in blades)
    for b in sa:
        for s in (1, -1):
            h = lin((1, ONE), (s, blade(b)))
            ok = ok and lin((HALF, prod(sq, h, dagger(h, sq)))) == h
    for k, seed in enumerate(SEEDS):
        x = element(sq, seed, k)
        s = lin((HALF, x), (HALF, dagger(x, sq)))
        ok = ok and all(b in sa for b in s)
        n = sum(abs(c) for c in s.values())
        cert = {}
        for b, c in s.items():
            h = lin((1, ONE), (-1 if c > 0 else 1, blade(b)))
            cert = GA.add(cert, GA.scal(abs(c) * HALF, prod(sq, h, dagger(h, sq))))
        ok = ok and clean(GA.sub(cert, lin((n, ONE), (-1, s)))) == {}
    return len(sa), ok


def one_mode_projector(direction):
    sq, e, f, p = modes(1)
    return lin((HALF, ONE), (HALF * direction[0], e[0]), (HALF * direction[1], p[0]))


def parity_average(sq, gamma, x):
    return lin((HALF, x), (HALF, prod(sq, gamma, x, gamma)))


def chsh(sq, a1, a2, b1, b2):
    return clean(GA.add(prod(sq, a1, b1), prod(sq, a1, b2), prod(sq, a2, b1), GA.neg(prod(sq, a2, b2))))


def check_self_adjoint_blades_and_the_order_unit():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate")
    reports = [order_unit_report(p, q) for p, q in SIGS]
    assert all(r[1] for r in reports)
    assert [r[0] for r in reports] == [3, 3, 1, 4, 6, 10]


def check_an_effect_relation_forces_the_born_weight_on_one_mode():
    premise("synthesis.premise-positivity-of-values")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    sq, e, f, p = modes(1)
    Pe, Pp, Ea = one_mode_projector((F(1), F(0))), one_mode_projector((F(0), F(1))), one_mode_projector(DIR_B1)
    for E in (Pe, Pp, Ea):
        assert dagger(E, sq) == E and prod(sq, E, E) == E and tau(E) == HALF
    left = lin((HALF, Ea), (F(1, 10), ONE))
    right = lin((F(3, 10), Pe), (F(4, 10), Pp))
    assert left == right
    # both sides are effects: the complement is a combination of projectors and 1 with coefficients >= 0
    comp = lin((HALF, GA.sub(ONE, Ea)), (F(4, 10), ONE))
    assert clean(GA.add(left, comp)) == ONE
    born = lambda x: tau(prod(sq, Pp, x)) / tau(Pp)
    forced = (F(3, 10) * born(Pe) + F(4, 10) * born(Pp) - F(1, 10)) * 2
    assert born(Pe) == HALF and born(Pp) == 1 and forced == F(9, 10) == born(Ea)
    frame = lambda direction: (1 + direction[1] ** 3) * HALF
    assert frame((F(0), F(1))) == 1 and frame((F(1), F(0))) == HALF and frame(DIR_B1) == F(189, 250)
    assert frame(DIR_B1) + frame((-DIR_B1[0], -DIR_B1[1])) == 1
    assert HALF * frame(DIR_B1) + F(1, 10) == F(239, 500) != F(3, 10) * HALF + F(4, 10)


def check_parity_average_keeps_the_cone_and_adds_no_positivity():
    premise("singularity.descent-parity-average")
    premise("synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product")
    sq, e, f, p = modes(2)
    gamma = prod(sq, p[0], p[1])
    assert dagger(gamma, sq) == gamma and prod(sq, gamma, gamma) == ONE
    for k, seed in enumerate(SEEDS):
        y = element(sq, seed, k)
        ye, yo = parity_average(sq, gamma, y), clean(GA.sub(y, parity_average(sq, gamma, y)))
        assert parity_average(sq, gamma, dagger(y, sq)) == dagger(parity_average(sq, gamma, y), sq)
        yg = prod(sq, yo, e[0])
        assert parity_average(sq, gamma, yg) == yg
        sq_sum = clean(GA.add(prod(sq, ye, dagger(ye, sq)), prod(sq, yg, dagger(yg, sq))))
        assert parity_average(sq, gamma, prod(sq, y, dagger(y, sq))) == sq_sum
    m = lin((1, ONE), (F(1, 2), p[0]))
    om = lambda x: tau(prod(sq, m, x))
    E = lin((HALF, ONE), (-HALF, p[0]))
    assert parity_average(sq, gamma, m) == m and dagger(m, sq) == m and om(ONE) == 1 and om(E) == F(-1, 2)


def check_even_atom_sees_the_products_of_odd_directions():
    premise("singularity.descent-parity-average")
    premise("synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate")
    sq, e, f, p = modes(2)
    gamma = prod(sq, p[0], p[1])
    avg = lambda x: parity_average(sq, gamma, x)
    twist = prod(sq, e[1], p[0])
    a1, a2 = e[0], p[0]
    b1 = lin((DIR_B1[0], twist), (DIR_B1[1], p[1]))
    b2 = lin((DIR_B2[0], twist), (DIR_B2[1], p[1]))
    for o in (a1, a2, b1, b2):
        assert dagger(o, sq) == o and prod(sq, o, o) == ONE
    assert all(GA.commutes(a, b, sq) for a in (a1, a2) for b in (b1, b2))
    c = chsh(sq, a1, a2, b1, b2)
    u = prod(sq, e[1], f[0])
    assert dagger(u, sq) == u and prod(sq, u, u) == ONE and GA.commutes(u, gamma, sq) and avg(u) == u
    assert avg(c) == lin((F(7, 5), u), (F(7, 5), gamma)) and avg(c) != c
    assert chsh(sq, avg(a1), avg(a2), avg(b1), avg(b2)) == lin((F(7, 5), gamma))
    atom = prod(sq, lin((HALF, ONE), (HALF, u)), lin((HALF, ONE), (HALF, gamma)))
    assert dagger(atom, sq) == atom and prod(sq, atom, atom) == atom and avg(atom) == atom and tau(atom) == F(1, 4)
    value = lambda x: tau(prod(sq, atom, x)) / tau(atom)
    assert value(c) == value(avg(c)) == F(14, 5) and value(e[0]) == 0 and value(twist) == 0
    assert value(prod(sq, a1, b1)) == F(3, 5) and value(prod(sq, avg(a1), avg(b1))) == 0
