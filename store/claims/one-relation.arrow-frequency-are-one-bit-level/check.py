"""one-relation.arrow-frequency-are-one-bit-level: exact checks in Cl(1,3) (GA.py, gamma_0^2 = +1,
gamma_i^2 = -1, I = gamma_0 gamma_1 gamma_2 gamma_3), C = I gamma_3.

(1) Linearity of the bijection J -> gamma_0 = C J of Lemma one-relation.one-datum-not-two-imaginary-unit:
    for five J on both sheets, C(-J) = -(CJ), and -J is again a square root of -1 commuting with C,
    so with C fixed J -> -J is gamma_0 -> -gamma_0 (the frame's time direction reverses).
(2) The pi-rotations, at J = e1e2 (so gamma_0 = CJ): the rotation by pi about an axis a of the spin
    plane is the unit bivector R = a' e3, a' the unit vector of the spin plane orthogonal to a (axis
    e1 gives R = e2e3, as in the paper; also the axes e2 and (3e1 + 4e2)/5). Each fixes a, flips J
    (R~ J R = -J), fixes gamma_0 and flips C (R~ C R = -C), so it is not a symmetry of the fixed law.
(3) Consistency: for every sample rotor R, R~ (C J) R = (R~ C R)(R~ J R); a rotor fixing C and gamma_0
    fixes J = C^-1 gamma_0. Checked on the boost 5/4 + 3/4 e0e1 and the rotation 3/5 + 4/5 e1e2.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ = GA.sig(1, 3)
E = [GA.gen(i) for i in range(4)]


def m(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, SQ)
    return out


I4 = m(E[0], E[1], E[2], E[3])
C = m(I4, E[3])
B01, B02, B12 = m(E[0], E[1]), m(E[0], E[2]), m(E[1], E[2])
SHEET = [(F(0), F(0), F(1)), (F(3, 4), F(0), F(5, 4)), (F(0), F(5, 12), F(13, 12)), (F(3, 4), F(0), F(-5, 4)),
         (F(4, 3), F(0), F(-5, 3))]
ROTORS = [GA.add(GA.sc(F(5, 4)), GA.scal(F(3, 4), B01)), GA.add(GA.sc(F(3, 5)), GA.scal(F(4, 5), B12))]


def J_of(b, c, d):
    return GA.add(GA.scal(b, B01), GA.scal(c, B02), GA.scal(d, B12))


def check_reversing_j_reverses_gamma0():
    premise("one-relation.one-datum-not-two-imaginary-unit")
    ok = True
    for b, c, d in SHEET:
        J = J_of(b, c, d)
        g = m(C, J)
        mJ = GA.neg(J)
        ok = ok and GA.eq(m(C, mJ), GA.neg(g))
        ok = ok and GA.eq(m(mJ, mJ), GA.sc(-1)) and GA.eq(m(mJ, C), m(C, mJ))
        ok = ok and GA.dot(g, g, SQ) == 1 and not GA.eq(g, GA.neg(g))
    ok = ok and GA.eq(m(C, B12), E[0])
    GA.check("with C fixed, J -> -J sends gamma_0 = CJ to -gamma_0 (five J, both sheets)", ok)
    return ok


def check_pi_rotation_flipping_j_flips_c():
    ok = True
    # reference case: J = e1e2, axis e1 in the spin plane, R = e2 e3 (rotation by pi about e1)
    J = B12
    R = m(E[2], E[3])
    Rt = GA.reverse(R)
    ok = ok and GA.eq(m(R, Rt), GA.sc(1))
    ok = ok and GA.eq(m(Rt, J, R), GA.neg(J))
    ok = ok and GA.eq(m(Rt, E[0], R), E[0])
    ok = ok and GA.eq(m(Rt, C, R), GA.neg(C))
    ok = ok and GA.eq(m(Rt, E[1], R), E[1])
    # the other axis in the plane, e2: R = e3 e1, and a rational axis (3 e1 + 4 e2)/5
    for a, aperp in ((E[2], E[1]), (GA.scal(F(1, 5), GA.add(GA.scal(3, E[1]), GA.scal(4, E[2]))),
                                     GA.scal(F(1, 5), GA.add(GA.scal(-4, E[1]), GA.scal(3, E[2]))))):
        Rn = m(aperp, E[3])
        Rnt = GA.reverse(Rn)
        ok = ok and GA.eq(m(Rn, Rnt), GA.sc(1))
        ok = ok and GA.eq(m(Rnt, J, Rn), GA.neg(J)) and GA.eq(m(Rnt, E[0], Rn), E[0])
        ok = ok and GA.eq(m(Rnt, C, Rn), GA.neg(C)) and GA.eq(m(Rnt, a, Rn), a)
    GA.check("the pi-rotation about an axis in the spin plane flips J, fixes gamma_0 and flips C", ok)
    return ok


def check_frame_and_unit_transform_together():
    ok = True
    for R in ROTORS:
        Rt = GA.reverse(R)
        ok = ok and GA.eq(m(R, Rt), GA.sc(1))
        for b, c, d in SHEET:
            J = J_of(b, c, d)
            lhs = m(Rt, m(C, J), R)
            rhs = m(m(Rt, C, R), m(Rt, J, R))
            ok = ok and GA.eq(lhs, rhs)
    # the rotation in the spin plane fixes C and gamma_0, hence J = C^-1 gamma_0
    R = ROTORS[1]
    Rt = GA.reverse(R)
    ok = ok and GA.eq(m(Rt, C, R), C) and GA.eq(m(Rt, E[0], R), E[0]) and GA.eq(m(Rt, B12, R), B12)
    # the boost moves gamma_0 and keeps C, so it moves J
    R = ROTORS[0]
    Rt = GA.reverse(R)
    ok = ok and GA.eq(m(Rt, C, R), C) and not GA.eq(m(Rt, E[0], R), E[0])
    GA.check("R~(CJ)R = (R~CR)(R~JR); a rotor fixing C and gamma_0 fixes J", ok)
    return ok
