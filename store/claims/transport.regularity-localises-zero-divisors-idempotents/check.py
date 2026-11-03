"""transport.regularity-localises-zero-divisors-idempotents: exact checks.

Real Clifford algebras of nondegenerate forms in GA.py, n <= 4. Zero divisors are certified by a singular
left-multiplication matrix. For each sample a, the linear system a x a = a is solved exactly for x
(GA.field_kernel on the augmented system), i.e. regularity is computed, not assumed.
(1) Regularity: a x a = a has a solution for each of 23 sample zero divisors (null vectors, nilpotents,
    1 + B with B^2 = 1, products of these with invertible elements, 1 + omega in type C), in Cl(1,1),
    Cl(2,0), Cl(1,2), Cl(2,1), Cl(1,3), Cl(2,2), Cl(3,1), Cl(0,3), each certified a zero divisor.
(2) For every nonzero zero divisor a and its computed x: e = x a and f = a x are idempotents,
    a(1 - e) = 0, (1 - f) a = 0, a e = a, f a = a, and e, f are not 0 or 1.
(3) Controls: in Cl(0,2) = H every nonzero sample is invertible (no zero divisors), and for an
    invertible a the computed e and f equal 1.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

ONE = GA.sc(1)


def el(spec):
    return GA.add(*[{tuple(b): F(c)} for b, c in spec]) if spec else {}


SAMPLES = {
    (1, 1): [[((0,), 1), ((1,), 1)], [((), 1), ((0, 1), 1)], [((), 1), ((0,), 1), ((1,), 2), ((0, 1), 2)]],
    (2, 0): [[((), 1), ((0,), 1)], [((0,), 1), ((0, 1), 1)], [((), 1), ((0,), 1), ((1,), 2), ((0, 1), 2)]],
    (1, 2): [[((0,), 1), ((1,), 1)], [((), 1), ((0,), 1)], [((0, 2), 1), ((1, 2), 1)]],
    (2, 1): [[((0,), 1), ((2,), 1)], [((), 1), ((0,), 1)]],
    (1, 3): [[((0,), 1), ((1,), 1)], [((), 1), ((0, 1), 1)], [((0,), 5), ((1,), 3), ((2,), 4)],
             [((), 1), ((2,), 1), ((0, 1), 1), ((0, 1, 2), 1)]],
    (2, 2): [[((0,), 1), ((2,), 1)], [((), 1), ((0, 2), 1)], [((), 1), ((0, 1, 2, 3), 1)]],
    (3, 1): [[((0,), 1), ((3,), 1)], [((), 1), ((0,), 1)], [((), 2), ((1,), 1), ((0, 3), 2), ((0, 1, 3), -1)]],
    (0, 3): [[((), 1), ((0, 1, 2), 1)], [((0,), 1), ((1, 2), 1)]],
}
INVERTIBLE = {(1, 3): [[((), 2), ((0,), 1)], [((0,), 1)]], (2, 2): [[((), 1), ((0, 1), 1)]]}
QUATERNION = [[((), 1), ((0,), 2)], [((0,), 3), ((1,), -1), ((0, 1), 2)], [((), F(1, 2)), ((0, 1), 1)]]


def left_matrix(a, S):
    bl = GA.all_blades(len(S))
    return [[GA.mul(a, {b: F(1)}, S).get(c, F(0)) for b in bl] for c in bl]


def is_zero_divisor(a, S):
    return GA.field_rank(left_matrix(a, S)) < 2 ** len(S)


def regular_inverse(a, S):
    """A solution x of a x a = a, or None."""
    bl = GA.all_blades(len(S))
    cols = [GA.mul(GA.mul(a, {b: F(1)}, S), a, S) for b in bl]
    M = [[cols[j].get(c, F(0)) for j in range(len(bl))] + [-a.get(c, F(0))] for c in bl]
    for k in GA.field_kernel(M):
        if k[-1] != 0:
            return {bl[j]: k[j] / k[-1] for j in range(len(bl)) if k[j] != 0}
    return None


def check_regularity_and_idempotents():
    premise("transport.classification-real-clifford-algebras")
    ok = True
    nzd = 0
    for (p, q), specs in SAMPLES.items():
        S = GA.sig(p, q)
        for sp in specs:
            a = el(sp)
            ok = ok and is_zero_divisor(a, S)
            x = regular_inverse(a, S)
            ok = ok and x is not None and GA.eq(GA.mul(GA.mul(a, x, S), a, S), a)
            e = GA.mul(x, a, S)
            f = GA.mul(a, x, S)
            ok = ok and GA.eq(GA.mul(e, e, S), e) and GA.eq(GA.mul(f, f, S), f)
            ok = ok and GA.is_zero(GA.mul(a, GA.sub(ONE, e), S)) and GA.is_zero(GA.mul(GA.sub(ONE, f), a, S))
            ok = ok and GA.eq(GA.mul(a, e, S), a) and GA.eq(GA.mul(f, a, S), a)
            ok = ok and not GA.is_zero(e) and not GA.eq(e, ONE) and not GA.is_zero(f) and not GA.eq(f, ONE)
            nzd += 1
    ok = ok and nzd == 23
    _tp_rv = (ok); assert _tp_rv is not False, "check_regularity_and_idempotents"; return _tp_rv


def check_controls_invertible_and_quaternions():
    premise("transport.classification-real-clifford-algebras")
    ok = True
    for (p, q), specs in INVERTIBLE.items():
        S = GA.sig(p, q)
        for sp in specs:
            a = el(sp)
            ok = ok and not is_zero_divisor(a, S)
            x = regular_inverse(a, S)
            ok = ok and GA.eq(GA.mul(x, a, S), ONE) and GA.eq(GA.mul(a, x, S), ONE)
    S = GA.sig(0, 2)
    for sp in QUATERNION:
        a = el(sp)
        ok = ok and not is_zero_divisor(a, S)
        # norm a a~ (conjugate) is a positive scalar
        conj = GA.reverse(GA.grade_inv(a))
        nrm = GA.mul(a, conj, S)
        ok = ok and list(nrm) == [()] and nrm[()] > 0
    ok = ok and GA.mul(el(QUATERNION[0]), GA.reverse(GA.grade_inv(el(QUATERNION[0]))), S) == {(): F(5)}
    _tp_rv = (ok); assert _tp_rv is not False, "check_controls_invertible_and_quaternions"; return _tp_rv
