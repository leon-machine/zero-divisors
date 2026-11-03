"""field-theory.imported-one-datum-massive-law: exact checks in the spacetime algebra Cl(1,3).

Setting of the source lemma (one-relation.one-datum-not-two-imaginary-unit): the mass datum aligned
as C = I u, u a unit spacelike vector, I = g0 g1 g2 g3; the complex structures the massive law needs
are the constant even J with J^2 = -1 commuting with C. For u = g3, u = (3 g1 + 4 g3)/5 and
u = (3 g0 + 5 g1)/4 (all u^2 = -1):
(1) The pseudoscalar is even with I^2 = -1 but anticommutes with C, so it is excluded.
(2) The commutant of C in Cl+(1,3) (exact kernel on the 8 even blades) has dimension 4 and does not
    contain I; for u = g3 it is spanned by 1, g0g1, g0g2, g1g2.
(3) On that commutant (u = g3), J = s + a g1g2 + b g0g1 + c g0g2 has
    J^2 = (s^2 - a^2 + b^2 + c^2) + 2s(a g1g2 + b g0g1 + c g0g2) at 30 rational points, so J^2 = -1
    iff s = 0 and a^2 - b^2 - c^2 = 1: a two-sheeted hyperboloid (points on both sheets).
(4) The datum is one: for such J, C J is a unit timelike vector orthogonal to u, J = C^{-1}(C J), and
    the joint commutant of (C, J) in Cl+ is span{1, J} (dimension 2).
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

SQ = GA.sig(1, 3)
G = [GA.gen(i) for i in range(4)]
EVEN = [b for b in GA.all_blades(4) if len(b) % 2 == 0]
ALL = GA.all_blades(4)
I4 = GA.mul(GA.mul(G[0], G[1], SQ), GA.mul(G[2], G[3], SQ), SQ)


def vec(c):
    return GA.add(*[GA.scal(F(c[i]), G[i]) for i in range(4)])


US = [vec([0, 0, 0, 1]), vec([0, F(3, 5), 0, F(4, 5)]), vec([F(3, 4), F(5, 4), 0, 0])]
B12, B01, B02 = (GA.mul(G[1], G[2], SQ), GA.mul(G[0], G[1], SQ), GA.mul(G[0], G[2], SQ))
SAMPLES = [(s, a, b, c) for s, a, b, c in product((F(0), F(1, 2), F(-2)), (F(3), F(-1)),
                                                     (F(2), F(0), F(1, 3)), (F(2), F(-5, 7)))][:30]
HYPER = [(F(3), F(2), F(2)), (F(-3), F(2), F(-2)), (F(5, 3), F(4, 3), F(0)), (F(1), F(0), F(0))]


def commutant_even(xs):
    rows = []
    for x in xs:
        cols = [GA.basis_vector_of(GA.sub(GA.mul(x, {b: F(1)}, SQ), GA.mul({b: F(1)}, x, SQ)), ALL)
                for b in EVEN]
        rows.extend([[cols[j][i] for j in range(len(EVEN))] for i in range(len(ALL))])
    return GA.field_kernel(rows)


def check_pseudoscalar_excluded_and_commutant_four_dimensional():
    premise("one-relation.one-datum-not-two-imaginary-unit")
    ok = True
    ok = ok and all(len(b) == 4 for b in I4) and GA.eq(GA.mul(I4, I4, SQ), GA.sc(-1))
    for u in US:
        ok = ok and GA.dot(u, u, SQ) == -1
        C = GA.mul(I4, u, SQ)
        ok = ok and GA.anticommutes(I4, C, SQ)
        ker = commutant_even([C])
        ok = ok and len(ker) == 4
        iv = [I4.get(b, F(0)) for b in EVEN]
        ok = ok and GA.rank_of_vectors(ker + [iv]) == 5
    C3 = GA.mul(I4, US[0], SQ)
    named = [GA.sc(1), B01, B02, B12]
    ok = ok and all(GA.commutes(x, C3, SQ) for x in named)
    ok = ok and GA.rank_of_vectors([[x.get(b, F(0)) for b in EVEN] for x in named]) == 4
    GA.check("I even, I^2 = -1, anticommutes with C = I u; the commutant of C in Cl+ is 4-dimensional without I", ok)
    return ok


def check_complex_structures_form_hyperboloid():
    premise("one-relation.one-datum-not-two-imaginary-unit")
    ok = True
    for s, a, b, c in SAMPLES:
        J = GA.add(GA.sc(s), GA.scal(a, B12), GA.scal(b, B01), GA.scal(c, B02))
        want = GA.add(GA.sc(s * s - a * a + b * b + c * c), GA.scal(2 * s, GA.sub(J, GA.sc(s))))
        ok = ok and GA.eq(GA.mul(J, J, SQ), want)
    ok = ok and len(SAMPLES) == 30
    for a, b, c in HYPER:
        ok = ok and a * a - b * b - c * c == 1
        J = GA.add(GA.scal(a, B12), GA.scal(b, B01), GA.scal(c, B02))
        ok = ok and GA.eq(GA.mul(J, J, SQ), GA.sc(-1))
    ok = ok and {h[0] > 0 for h in HYPER} == {True, False}
    GA.check("J^2 = -1 on the commutant iff s = 0 and a^2 - b^2 - c^2 = 1 (two sheets)", ok)
    return ok


def check_imaginary_unit_and_rest_frame_one_choice():
    premise("one-relation.one-datum-not-two-imaginary-unit")
    ok = True
    u = US[0]
    C = GA.mul(I4, u, SQ)
    Cinv = GA.scal(F(1) / GA.mul(C, C, SQ)[()], C)
    ok = ok and GA.eq(GA.mul(Cinv, C, SQ), GA.sc(1))
    for a, b, c in HYPER:
        J = GA.add(GA.scal(a, B12), GA.scal(b, B01), GA.scal(c, B02))
        g0 = GA.mul(C, J, SQ)
        ok = ok and all(len(bl) == 1 for bl in g0)
        ok = ok and GA.dot(g0, g0, SQ) == 1 and GA.dot(g0, u, SQ) == 0
        ok = ok and GA.eq(GA.mul(Cinv, g0, SQ), J)
        joint = commutant_even([C, J])
        ok = ok and len(joint) == 2
        span = [[x.get(bl, F(0)) for bl in EVEN] for x in (GA.sc(1), J)]
        ok = ok and GA.rank_of_vectors(joint + span) == 2
    GA.check("J -> C J is a unit timelike vector orthogonal to u with inverse C^{-1}; joint commutant span{1, J}", ok)
    return ok
