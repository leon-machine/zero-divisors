"""synthesis.unit-i4-keeps-its-three-properties-only-in-dimension-zero-mod-four: exact checks.

Clifford algebra Cl(1, D - 1) on generators g_0, ..., g_{D-1} with g_0^2 = +1 and g_a^2 = -1 (a >= 1),
as in the series' (+, -, -, -) ground for D = 4. I_D = g_0 ... g_{D-1}; I4 = g_0 g_1 g_2 g_3.
Tests every clause: (i) the commutant of the bivectors (blade by blade, which is complete because
conjugation by a bivector blade sends each blade to plus or minus itself), D = 3 to 8; (ii) the square
of I_D, D = 2 to 12, against the closed formula; (iii) the three properties together, D = 2 to 12;
(iv) the four-dimensional I4 inside Cl(1, D - 1), D = 5 to 8 (the Breitenlohner-Maison split);
(v) left against right multiplication by I4 on every even blade, D = 4 to 7, and the right unit
commuting with a mixed boost while the left unit does not; (vi) one adjoined tower plane over the
ground: I4 commutes with its null generators and anticommutes with ground-times-plane bivectors.
Signature dependence: the same squares and the three properties in the mostly-plus signature (D - 1, 1).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from GA import mul, gen, eq, neg, add, scal, sc, all_blades
from tp_premise import premise


def sq(D):
    return tuple([1] + [-1] * (D - 1))


def blade(A):
    return {tuple(A): F(1)}


def commutes(x, y, s):
    return eq(mul(x, y, s), mul(y, x, s))


def anticommutes(x, y, s):
    return eq(mul(x, y, s), neg(mul(y, x, s)))


def bivectors(D):
    return [blade(c) for c in combinations(range(D), 2)]


def commuting_blades(D):
    s = sq(D)
    bv = bivectors(D)
    return [A for A in all_blades(D) if all(commutes(blade(A), b, s) for b in bv)]


def pseudoscalar_square(D):
    I = blade(range(D))
    return mul(I, I, sq(D))


def check_bivector_commutant_is_span_of_one_and_pseudoscalar():
    for D in range(3, 9):
        cb = commuting_blades(D)
        assert len(cb) == 2, (D, cb)
        assert cb[0] == () and cb[1] == tuple(range(D))
    # a non-trivial element outside the span fails: g_0 g_1 g_2 in D = 4 does not commute with g_2 g_3
    s = sq(4)
    assert not commutes(blade((0, 1, 2)), blade((2, 3)), s)


def check_pseudoscalar_square_has_period_four():
    minus = []
    for D in range(2, 13):
        x = pseudoscalar_square(D)
        e = D * (D - 1) // 2 + (D - 1)
        assert x == sc((-1) ** e)
        if x == sc(-1):
            minus.append(D)
    assert minus == [3, 4, 7, 8, 11, 12]
    assert all(D % 4 in (0, 3) for D in minus)


def check_three_properties_only_when_dimension_is_zero_mod_four():
    # candidates commuting with all bivectors and with no scalar part are multiples of I_D (clause i);
    # J = b I_D with J^2 = -1 and J anticommuting with every vector
    good = []
    for D in range(2, 13):
        s = sq(D)
        I = blade(range(D))
        anti_vectors = all(anticommutes(I, gen(a), s) for a in range(D))
        square_minus = mul(I, I, s) == sc(-1)
        if anti_vectors and square_minus:
            good.append(D)
    assert good == [4, 8, 12]
    # D = 5, 6, 7 each lose a different property
    assert pseudoscalar_square(5) == sc(1) and pseudoscalar_square(6) == sc(1)
    s7 = sq(7)
    I7 = blade(range(7))
    assert all(commutes(I7, gen(a), s7) for a in range(7)) and pseudoscalar_square(7) == sc(-1)


def check_four_dimensional_unit_inside_higher_dimensions():
    I4 = blade(range(4))
    for D in range(5, 9):
        s = sq(D)
        assert mul(I4, I4, s) == sc(-1)
        for a in range(4):
            assert anticommutes(I4, gen(a), s)
        for a in range(4, D):
            assert commutes(I4, gen(a), s)
        anti = [b for b in combinations(range(D), 2) if anticommutes(I4, blade(b), s)]
        comm = [b for b in combinations(range(D), 2) if commutes(I4, blade(b), s)]
        assert len(anti) == 4 * (D - 4)
        assert all(b[0] < 4 <= b[1] for b in anti)
        assert len(anti) + len(comm) == D * (D - 1) // 2


def check_left_and_right_unit_differ_exactly_on_mixed_blades():
    I4 = blade(range(4))
    for D in range(4, 8):
        s = sq(D)
        even = [A for A in all_blades(D) if len(A) % 2 == 0]
        differ = []
        for A in even:
            k = len([i for i in A if i < 4])
            left, right = mul(I4, blade(A), s), mul(blade(A), I4, s)
            if eq(left, right):
                assert k % 2 == 0
            else:
                assert k % 2 == 1 and eq(left, neg(right))
                differ.append(A)
        # even blades with an odd number of four-dimensional indices: 2^(D-2) for D > 4, none for D = 4
        assert len(differ) == (0 if D == 4 else 2 ** (D - 2))
    # right multiplication by I4 commutes with a mixed rotor acting on the left; left multiplication does not
    s = sq(6)
    R = add(sc(F(3, 5)), scal(F(4, 5), blade((1, 4))))          # rotor in the mixed plane g_1 g_4
    assert mul(R, GA.reverse(R), s) == sc(1)
    psi = add(sc(2), blade((0, 1)), scal(3, blade((2, 5))), blade((0, 1, 2, 3)))
    right_then_rotor = mul(R, mul(psi, I4, s), s)
    rotor_then_right = mul(mul(R, psi, s), I4, s)
    assert eq(right_then_rotor, rotor_then_right)
    left_then_rotor = mul(R, mul(I4, psi, s), s)
    rotor_then_left = mul(I4, mul(R, psi, s), s)
    assert not eq(left_then_rotor, rotor_then_left)


def check_tower_plane_generators_commute_with_the_unit():
    premise("field-theory.imported-tower-limit")
    # ground Cl(1,3) plus one adjoined plane: g_4^2 = +1, g_5^2 = -1; v = (g_4 + g_5)/2, w = (g_4 - g_5)/2
    s = (1, -1, -1, -1, 1, -1)
    v = add(scal(F(1, 2), gen(4)), scal(F(1, 2), gen(5)))
    w = add(scal(F(1, 2), gen(4)), scal(F(-1, 2), gen(5)))
    assert mul(v, v, s) == {} and mul(w, w, s) == {}
    assert add(mul(v, w, s), mul(w, v, s)) == sc(1)
    I4 = blade(range(4))
    assert commutes(I4, v, s) and commutes(I4, w, s)
    for a in range(4):
        assert anticommutes(I4, mul(gen(a), v, s), s)
        assert anticommutes(I4, mul(gen(a), w, s), s)
    # the number element v w of the plane commutes with I4
    assert commutes(I4, mul(v, w, s), s)


def check_signature_dependence_of_the_odd_dimension_clauses():
    # mostly-plus signature (D - 1, 1): last generator squares to -1
    def sqp(D):
        return tuple([1] * (D - 1) + [-1])
    minus, three = [], []
    for D in range(2, 13):
        s = sqp(D)
        I = blade(range(D))
        x = mul(I, I, s)
        assert x == sc((-1) ** (D * (D - 1) // 2 + 1))
        if x == sc(-1):
            minus.append(D)
            if all(anticommutes(I, gen(a), s) for a in range(D)):
                three.append(D)
    assert minus == [4, 5, 8, 9, 12]
    assert three == [4, 8, 12]
    # D = 5 mostly plus: I_5 squares to -1, commutes with every bivector, fails only the anticommutation
    s5 = sqp(5)
    I5 = blade(range(5))
    assert all(commutes(I5, b, s5) for b in bivectors(5))
    assert all(commutes(I5, gen(a), s5) for a in range(5))
