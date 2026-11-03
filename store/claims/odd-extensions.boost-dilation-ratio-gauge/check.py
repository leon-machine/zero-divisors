"""odd-extensions.boost-dilation-ratio-gauge: exact checks.

Conventions: Cl(2,4) with e_+ (+1), the Lorentz frame f0 (+1), f1, f2, f3 (-1), e_- (-1) (indices 0, 1..4, 5);
I = (e_+ + e_-)/2, phi = e_+ - e_-, B = I ^ phi (grade-2 part of I phi).
(i) I phi = 1 - e_+e_-, so B = -e_+e_-; B^2 = +1; B commutes with the four Lorentz vectors and the six
    Lorentz bivectors and anticommutes with e_+ and e_-.
(ii) For the rational rotors R = cosh + B sinh with (cosh, sinh) = (5/4, 3/4), (13/12, 5/12), (17/8, 15/8)
    (cosh^2 - sinh^2 = 1, t = (cosh + sinh)^2 = 4, 9/4, 16): R ~R = 1, R fixes the Lorentz frame,
    R I ~R = t I and R phi ~R = phi / t.
(iii) Frozen points a I + b phi have norm 2ab; under R they go to (t a) I + (b / t) phi with the same norm, so
    the ratio b/a moves by 1/t^2 while 2ab = Lambda/3 stays; for sample pairs of frozen points with the same
    norm and positive ratio of components a'/a = s^2 (s rational) the rotor with cosh = (s + 1/s)/2,
    sinh = (s - 1/s)/2 carries one to the other, so the ratio is a gauge (the O(1,1) orbits are the
    level sets of the norm). That the dynamics does not fix the gauge either is the cited Fact on the point
    at infinity, not checked here.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

SQ = (1, 1, -1, -1, -1, -1)
EP, EM_ = GA.gen(0), GA.gen(5)
LORENTZ = [GA.gen(a) for a in (1, 2, 3, 4)]
LBIV = [GA.mul(GA.gen(a), GA.gen(b), SQ) for a, b in combinations((1, 2, 3, 4), 2)]
I_ = GA.scal(F(1, 2), GA.add(EP, EM_))
PHI = GA.sub(EP, EM_)
ROTORS = [(F(5, 4), F(3, 4)), (F(13, 12), F(5, 12)), (F(17, 8), F(15, 8))]
FROZEN = [(F(1), F(1, 6)), (F(2), F(1, 12)), (F(3), F(-1, 18)), (F(1, 2), F(1, 3))]
TARGET_SCALES = [F(2), F(3, 2), F(1, 3)]
# pairs of frozen points of equal norm whose first components have a rational square-root ratio s
CONNECT = [((F(1), F(1, 6)), (F(4), F(1, 24)), F(2)), ((F(1), F(1, 6)), (F(1, 4), F(2, 3)), F(1, 2)),
           ((F(1), F(-1, 6)), (F(9, 4), F(-2, 27)), F(3, 2))]


def m(x, y):
    return GA.mul(x, y, SQ)


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def sandwich(R, x):
    return m(m(R, x), GA.reverse(R))


def rotor(ch, sh):
    return GA.add(GA.sc(ch), GA.scal(sh, BIV))


BIV = grade(m(I_, PHI), 2)


def check_bivector_is_the_dilation_generator():
    ok = True
    ok = ok and GA.eq(m(I_, PHI), GA.sub(GA.sc(1), m(EP, EM_)))
    ok = ok and GA.eq(BIV, GA.neg(m(EP, EM_)))
    ok = ok and GA.eq(m(BIV, BIV), GA.sc(1))
    ok = ok and all(GA.commutes(BIV, v, SQ) for v in LORENTZ + LBIV)
    ok = ok and GA.anticommutes(BIV, EP, SQ) and GA.anticommutes(BIV, EM_, SQ)
    ok = ok and GA.dot(I_, PHI, SQ) == 1 and GA.dot(I_, I_, SQ) == 0 and GA.dot(PHI, PHI, SQ) == 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_bivector_is_the_dilation_generator"; return _tp_rv


def check_rotor_scales_the_null_pair():
    premise("odd-extensions.transport-constrains-frozen-point-only-through")
    ok = True
    expected_t = [F(4), F(9, 4), F(16)]
    for (ch, sh), t in zip(ROTORS, expected_t):
        R = rotor(ch, sh)
        ok = ok and GA.eq(m(R, GA.reverse(R)), GA.sc(1))
        ok = ok and (ch + sh) * (ch + sh) == t
        ok = ok and all(GA.eq(sandwich(R, v), v) for v in LORENTZ)
        ok = ok and GA.eq(sandwich(R, I_), GA.scal(t, I_))
        ok = ok and GA.eq(sandwich(R, PHI), GA.scal(1 / t, PHI))
    _tp_rv = (ok); assert _tp_rv is not False, "check_rotor_scales_the_null_pair"; return _tp_rv


def check_ratio_is_gauge_and_product_invariant():
    premise("odd-extensions.transport-constrains-frozen-point-only-through")
    ok = True
    for a, b in FROZEN:
        P = GA.add(GA.scal(a, I_), GA.scal(b, PHI))
        ok = ok and GA.dot(P, P, SQ) == 2 * a * b
        for ch, sh in ROTORS:
            t = (ch + sh) * (ch + sh)
            P2 = sandwich(rotor(ch, sh), P)
            ok = ok and GA.eq(P2, GA.add(GA.scal(t * a, I_), GA.scal(b / t, PHI)))
            ok = ok and GA.dot(P2, P2, SQ) == GA.dot(P, P, SQ)
        # any positive rescaling of the ratio that is a rational square is reached by a rotor
        for s in TARGET_SCALES:
            ch, sh = (s + F(1) / s) / 2, (s - F(1) / s) / 2
            target = GA.add(GA.scal(s * s * a, I_), GA.scal(b / (s * s), PHI))
            ok = ok and ch * ch - sh * sh == 1 and GA.eq(sandwich(rotor(ch, sh), P), target)
    # equal norms: the rotor with cosh = (s + 1/s)/2, sinh = (s - 1/s)/2 carries one point to the other
    for (a, b), (a2, b2), s in CONNECT:
        P = GA.add(GA.scal(a, I_), GA.scal(b, PHI))
        P2 = GA.add(GA.scal(a2, I_), GA.scal(b2, PHI))
        ch, sh = (s + F(1) / s) / 2, (s - F(1) / s) / 2
        ok = ok and GA.dot(P, P, SQ) == GA.dot(P2, P2, SQ) and GA.eq(sandwich(rotor(ch, sh), P), P2)
    # the norms in the samples: Lambda = 1 and Lambda = -1 (2ab = +1/3 and -1/3), never exchanged (t > 0)
    norms = sorted({2 * a * b for (a, b), _, _ in CONNECT})
    ok = ok and norms == [F(-1, 3), F(1, 3)]
    _tp_rv = (ok); assert _tp_rv is not False, "check_ratio_is_gauge_and_product_invariant"; return _tp_rv
