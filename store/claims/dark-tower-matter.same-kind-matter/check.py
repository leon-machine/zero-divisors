"""dark-tower-matter.same-kind-matter: exact checks of the algebra-level rows of the table.

Checked (GA.py, centres computed blade-wise, which is exact since conjugation by generators acts
diagonally on blades):
(1) Module types. Cl(2,1) (r = 1) and Cl(1,4) (r = 5) have centre span{1, omega} with
    omega^2 = +1, so (1 +- omega)/2 are two nonzero central idempotents: two module types;
    Cl(1,2) (r = 7) and Cl(4,1) (r = 3) have omega^2 = -1, the centre is a copy of C with no
    nontrivial idempotent: one type. At r = 1 the grade involution sends omega to -omega and so
    exchanges the two components: the two modules are of the same type.
(2) Slot rotation at r = 7, exact at every rung: along Cl(1,2), Cl(2,3), Cl(3,4), Cl(4,5) the
    pseudoscalar is central with square -1 (and along Cl(2,1), Cl(3,2), Cl(4,3), Cl(5,4) central
    with square +1). Left multiplication by c + s omega (rational points c^2 + s^2 = 1) commutes
    with the Clifford action and sends X + omega Y to (cX - sY) + omega(sX + cY); a charge-two
    (number-violating) term picks up (c + s omega)^2 = (c^2 - s^2) + 2cs omega, not 1 for s != 0,
    so it is not invariant.
(3) The pair unit at r = 3: in the conformal completion Cl(5,2) the pseudoscalar I_7 is central with
    I_7^2 = -1, a unit fixed by the algebra; at r = 5, in Cl(2,5), the centre is span{1, omega}
    with omega^2 = +1 (R + R), which contains no element of square -1, so the algebra fixes none.
Not checked: the shared rows (constituent field, mass onset, gauge algebra, content), the
invariant-form row and the S^2 of choices, which rest on the constituent ideal and supplementary
scripts not in the lab.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

ROT = [(F(3, 5), F(4, 5)), (F(5, 13), F(-12, 13)), (F(-8, 17), F(15, 17))]
XY_SAMPLES = [({(): F(1), (0, 1): F(2)}, {(0,): F(1), (2,): F(-3)})]


def blade(b):
    return {b: F(1)}


def centre_blades(p, q):
    n, sq = p + q, GA.sig(p, q)
    return [b for b in GA.all_blades(n) if all(GA.commutes(blade(b), GA.gen(i), sq) for i in range(n))]


def omega_sq(p, q):
    n = p + q
    w = blade(tuple(range(n)))
    return GA.mul(w, w, GA.sig(p, q))[()]


def split_idempotent(p, q):
    sq = GA.sig(p, q)
    w = blade(tuple(range(p + q)))
    e = GA.scal(F(1, 2), GA.add(GA.sc(1), w))
    return GA.eq(GA.mul(e, e, sq), e)


def check_module_types():
    premise("dark-tower-matter.residue-seven-unit")
    premise("dark-tower-matter.third-pairs-unit-five-dimensions")
    types = {}
    for (p, q), r in (((2, 1), 1), ((1, 2), 7), ((4, 1), 3), ((1, 4), 5)):
        n = p + q
        assert centre_blades(p, q) == [(), tuple(range(n))]
        types[r] = 2 if split_idempotent(p, q) else 1
        assert types[r] == (2 if omega_sq(p, q) == 1 else 1)
    assert types == {1: 2, 7: 1, 3: 1, 5: 2}
    w = blade((0, 1, 2))
    assert GA.eq(GA.grade_inv(w), GA.scal(-1, w))
    return True


def check_slot_rotation_rows():
    premise("dark-tower-matter.residue-seven-unit")
    for k in range(4):
        p7, q7 = 1 + k, 2 + k
        p1, q1 = 2 + k, 1 + k
        assert centre_blades(p7, q7) == [(), tuple(range(p7 + q7))] and omega_sq(p7, q7) == -1
        assert centre_blades(p1, q1) == [(), tuple(range(p1 + q1))] and omega_sq(p1, q1) == 1
    sq = GA.sig(1, 2)
    w = blade((0, 1, 2))
    for c, s in ROT:
        assert c * c + s * s == 1
        u = GA.add(GA.sc(c), GA.scal(s, w))
        assert all(GA.commutes(u, GA.gen(i), sq) for i in range(3))
        for X, Y in XY_SAMPLES:
            lhs = GA.mul(u, GA.add(X, GA.mul(w, Y, sq)), sq)
            rhs = GA.add(GA.sub(GA.scal(c, X), GA.scal(s, Y)),
                         GA.mul(w, GA.add(GA.scal(s, X), GA.scal(c, Y)), sq))
            assert GA.eq(lhs, rhs)
        u2 = GA.mul(u, u, sq)
        assert GA.eq(u2, GA.add(GA.sc(c * c - s * s), GA.scal(2 * c * s, w)))
        assert not GA.eq(u2, GA.sc(1))
    return True


def check_pair_unit_rows():
    premise("dark-tower-matter.third-pairs-unit-five-dimensions")
    assert centre_blades(5, 2) == [(), tuple(range(7))] and omega_sq(5, 2) == -1
    assert centre_blades(2, 5) == [(), tuple(range(7))] and omega_sq(2, 5) == 1
    # a central element a + b omega of Cl(2,5) squares to (a^2 + b^2) + 2ab omega
    sq = GA.sig(2, 5)
    w = blade(tuple(range(7)))
    for a, b in ((F(1), F(1)), (F(2), F(-3)), (F(0), F(1))):
        z = GA.add(GA.sc(a), GA.scal(b, w))
        assert GA.eq(GA.mul(z, z, sq), GA.add(GA.sc(a * a + b * b), GA.scal(2 * a * b, w)))
    return True
