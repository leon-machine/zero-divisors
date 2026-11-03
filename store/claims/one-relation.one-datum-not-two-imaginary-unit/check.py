"""one-relation.one-datum-not-two-imaginary-unit: exact checks in Cl(1,3) (GA.py, gamma_0^2 = +1,
gamma_i^2 = -1, I = gamma_0 gamma_1 gamma_2 gamma_3), with C = I u, u = gamma_3.

(1) The commutant of C in Cl^+(1,3), an exact kernel, has dimension 4 and equals
    span{1, e0e1, e0e2, e1e2}; I is even with I^2 = -1 and anticommutes with C.
(2) On the commutant, J = a + b e0e1 + c e0e2 + d e1e2 has J^2 = (a^2 + b^2 + c^2 - d^2) + 2a B
    (B the bivector part): J^2 = -1 iff a = 0 and d^2 - b^2 - c^2 = 1. Tested as a verdict on a grid
    of 6^4 rational (a, b, c, d) against the stated condition (the condition holds on 6 grid points,
    on both sheets d > 0 and d < 0).
(3) The bijection: for J on both sheets (rational points of the hyperboloid), CJ is a vector, unit
    timelike and orthogonal to u, and C^-1 (CJ) = J; conversely for unit timelike g orthogonal to u,
    C^-1 g lies in the commutant with square -1. At J = e1e2, CJ = +gamma_0 (the choice of sheet).
(4) The joint commutant of (C, J) in Cl^+ is 2-dimensional, span{1, J}, for three J; its unit
    elements cos + sin J are rotors (R R~ = 1) fixing both.
(5) Alignment (Lemma one-relation.odd-square-roots-chiral-phase): for u' = R~ gamma_3 R with
    R = 5/4 + 3/4 gamma_0 gamma_3, u'.gamma_0 = 15/8 != 0 and R u' R~ = gamma_3 is again orthogonal to
    gamma_0.
(6) The ideal picture: P = (1 + gamma_0)/2 is idempotent, P Cl P has dimension 4 with P e_ij squaring
    to -P, and P J = P J P for J = I sigma_3 but not for I.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

SQ = GA.sig(1, 3)
E = [GA.gen(i) for i in range(4)]
BL = GA.all_blades(4)
EVEN = [b for b in BL if len(b) % 2 == 0]


def m(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, SQ)
    return out


I4 = m(E[0], E[1], E[2], E[3])
U = E[3]
C = m(I4, U)
B01, B02, B12 = m(E[0], E[1]), m(E[0], E[2]), m(E[1], E[2])
GRID = [F(0), F(1), F(-1), F(3, 4), F(5, 4), F(-5, 4)]
SHEET = [(F(0), F(0), F(1)), (F(3, 4), F(0), F(5, 4)), (F(0), F(5, 12), F(13, 12)), (F(3, 4), F(0), F(-5, 4)),
         (F(4, 3), F(0), F(-5, 3))]
FRAMES = [[1, 0, 0, 0], [F(5, 4), F(3, 4), 0, 0], [F(13, 12), 0, F(5, 12), 0], [-1, 0, 0, 0]]


def J_of(a, b, c, d):
    return GA.add(GA.sc(a), GA.scal(b, B01), GA.scal(c, B02), GA.scal(d, B12))


def coords(x, blades):
    return [x.get(b, F(0)) for b in blades]


def commutant(elems):
    rows = []
    for b in EVEN:
        x = {b: F(1)}
        col = []
        for y in elems:
            col += coords(GA.sub(m(x, y), m(y, x)), BL)
        rows.append(col)
    M = [[rows[j][i] for j in range(len(EVEN))] for i in range(len(rows[0]))]
    return [{b: c for b, c in zip(EVEN, kv) if c != 0} for kv in GA.field_kernel(M)]


def check_commutant_of_c():
    ok = True
    ker = commutant([C])
    ok = ok and len(ker) == 4
    span = [GA.sc(1), B01, B02, B12]
    ok = ok and all(GA.is_zero(GA.sub(m(x, C), m(C, x))) for x in span)
    ok = ok and GA.field_rank([coords(x, EVEN) for x in span + ker]) == 4
    ok = ok and GA.eq(m(I4, I4), GA.sc(-1)) and GA.anticommutes(I4, C, SQ)
    GA.check("the commutant of C = I gamma_3 in Cl^+ is span{1, e0e1, e0e2, e1e2}; I anticommutes with C", ok)
    return ok


def check_complex_structures_are_a_two_sheeted_hyperboloid():
    ok = True
    hits = 0
    for a, b, c, d in product(GRID, repeat=4):
        J = J_of(a, b, c, d)
        root = GA.eq(m(J, J), GA.sc(-1))
        want = a == 0 and d * d - b * b - c * c == 1
        ok = ok and root == want
        hits += want
    ok = ok and hits == 6
    GA.check("J^2 = -1 on the commutant iff a = 0 and d^2 - b^2 - c^2 = 1 (6^4 grid, 6 roots)", ok)
    return ok


def check_j_to_gamma0_bijection():
    ok = True
    Cinv = GA.neg(C)
    ok = ok and GA.eq(m(C, Cinv), GA.sc(1))
    for b, c, d in SHEET:
        J = J_of(F(0), b, c, d)
        ok = ok and GA.eq(m(J, J), GA.sc(-1))
        g = m(C, J)
        ok = ok and all(len(bl) == 1 for bl in g)
        ok = ok and GA.dot(g, g, SQ) == 1 and GA.dot(g, U, SQ) == 0
        ok = ok and GA.eq(m(Cinv, g), J)
    for fc in FRAMES:
        g = GA.add(*[GA.scal(fc[i], E[i]) for i in range(4) if fc[i]])
        ok = ok and GA.dot(g, g, SQ) == 1 and GA.dot(g, U, SQ) == 0
        J = m(Cinv, g)
        ok = ok and GA.eq(m(J, J), GA.sc(-1)) and GA.is_zero(GA.sub(m(J, C), m(C, J)))
        ok = ok and all(len(bl) == 2 for bl in J)
    ok = ok and GA.eq(m(C, B12), E[0]) and GA.eq(m(C, GA.neg(B12)), GA.neg(E[0]))
    GA.check("J -> C J is a bijection onto unit timelike vectors orthogonal to u, inverse C^-1 g", ok)
    return ok


def check_joint_commutant_is_the_spin_plane_u1():
    ok = True
    for b, c, d in SHEET[:3]:
        J = J_of(F(0), b, c, d)
        ker = commutant([C, J])
        ok = ok and len(ker) == 2
        ok = ok and GA.field_rank([coords(x, EVEN) for x in ker + [GA.sc(1), J]]) == 2
        R = GA.add(GA.sc(F(3, 5)), GA.scal(F(4, 5), J))
        ok = ok and GA.eq(m(R, GA.reverse(R)), GA.sc(1))
        ok = ok and GA.eq(m(R, C, GA.reverse(R)), C) and GA.eq(m(R, J, GA.reverse(R)), J)
    GA.check("the joint commutant of (C, J) in Cl^+ is span{1, J}: the U(1) of the spin plane", ok)
    return ok


def check_alignment_and_ideal_picture():
    premise("one-relation.odd-square-roots-chiral-phase")
    ok = True
    R = GA.add(GA.sc(F(5, 4)), GA.scal(F(3, 4), m(E[0], E[3])))
    Rt = GA.reverse(R)
    up = m(Rt, U, R)
    ok = ok and GA.dot(up, E[0], SQ) == F(15, 8) and GA.eq(m(R, up, Rt), U) and GA.dot(m(R, up, Rt), E[0], SQ) == 0
    P = GA.scal(F(1, 2), GA.add(GA.sc(1), E[0]))
    ok = ok and GA.eq(m(P, P), P)
    imgs = [coords(m(P, {b: F(1)}, P), BL) for b in BL]
    ok = ok and GA.field_rank(imgs) == 4
    for x in (B12, m(E[2], E[3]), m(E[3], E[1])):
        px = m(P, x)
        ok = ok and GA.eq(m(P, px, P), px) and GA.eq(m(px, px), GA.neg(P))
    Isig3 = m(I4, E[3], E[0])
    ok = ok and GA.eq(m(P, Isig3), m(P, Isig3, P)) and not GA.eq(m(P, I4), m(P, I4, P))
    GA.check("a rotor realigns a boosted u'; P = (1 + gamma_0)/2 has P Cl P = H and I sigma_3 preserves Cl P", ok)
    return ok
