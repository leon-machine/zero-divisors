"""Positive conformal energy gives positive null translations: exact checks in Cl(2,4).

Generators e0 (+1), e1, e2, e3 (-1), e+ = nu (+1), e- (-1); n_inf = e+ + e-, n0 = (e+ - e-)/2, <n0, n_inf> = 1,
X(x) = n0 + x - Q(x)/2 n_inf. Z = e0 nu is the central rotation of the maximal compact subalgebra; the
translation by a is exp(P_a), P_a = (1/2) a n_inf, a nilpotent bivector.
(1) Z^2 = -1; Z commutes with the six rotations of {e1, e2, e3, e-} and not with the boost e0 e1; Z = P_{e0} + e0 n0.
(2) The dilation D_rho (X(x) -> rho^{-2} X(rho^2 x)) gives Ad(D_rho) Z = rho^2 P_{e0} + rho^{-2} e0 n0, so
    rho^{-2} Ad(D_rho) Z - P_{e0} = rho^{-4} e0 n0 -> 0 (tabulated).
(3) The boost orbit of P_{e0}: Ad(B_rho) P_{e0} = P_{cosh e0 + sinh e1} (tabulated at rho = 2, 3), and
    (2/rho^2) Ad(B_rho) P_{e0} - P_{e0 + e1} = rho^{-4} P_{e0 - e1} -> 0: the future null translation is a limit.
    A two-reflection versor carries e1 to any rational unit direction; forward timelike vectors are positive
    combinations of two future null vectors (tabulated).
(4) Controls: Ad(e1 e2) P_{e1} = -P_{e1} (a spacelike translation is conjugate to its negative); -Z gives the past
    cone; translations and Lorentz rotors fix n_inf, the dilation scales it; the wedge reflection
    Ad(e0 e1) sends X(x0, x1, x2, x3) to X(-x0, -x1, x2, x3).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
NINF = GA.add(E[4], E[5])
N0 = GA.scal(F(1, 2), GA.sub(E[4], E[5]))


def _m(*xs):
    out = xs[0]
    for y in xs[1:]:
        out = GA.mul(out, y, SQ)
    return out


def _sand(R, x):
    return _m(R, x, GA.reverse(R))


def _vec(c0, c1, c2, c3):
    return GA.add(GA.scal(c0, E[0]), GA.scal(c1, E[1]), GA.scal(c2, E[2]), GA.scal(c3, E[3]))


def _P(a):
    return GA.scal(F(1, 2), _m(a, NINF))


def _X(x):
    return GA.add(N0, x, GA.scal(-F(1, 2) * GA.dot(x, x, SQ), NINF))


def _rotor(rho, biv):
    c, s = (rho + 1 / rho) / 2, (rho - 1 / rho) / 2
    return GA.add(GA.sc(c), GA.scal(s, biv))


def check_central_rotation_contains_time_translation():
    premise("synthesis.positive-energy-selects-rule-2-sign")
    premise("mass.chart-form-spin-isomorphism")
    Z = _m(E[0], E[4])
    GA.check("Z^2 = -1 (a rotation)", GA.eq(_m(Z, Z), GA.sc(-1)))
    so4 = [_m(E[i], E[j]) for (i, j) in [(1, 2), (1, 3), (2, 3), (1, 5), (2, 5), (3, 5)]]
    GA.check("Z commutes with the rotations of {e1, e2, e3, e-}", all(GA.commutes(Z, b, SQ) for b in so4))
    GA.check("Z does not commute with the boost e0 e1", not GA.commutes(Z, _m(E[0], E[1]), SQ))
    GA.check("Z = P_{e0} + e0 n0", GA.eq(Z, GA.add(_P(E[0]), _m(E[0], N0))))
    GA.check("P_{e0} is nilpotent", GA.is_zero(_m(_P(E[0]), _P(E[0]))))
    pa, pb = _P(_vec(F(1), F(2), F(0), F(-1))), _P(_vec(F(3), F(0), F(1, 2), F(4)))
    GA.check("translation generators multiply to zero, so they commute", GA.is_zero(_m(pa, pb)) and GA.is_zero(_m(pb, pa)))
    for t in [F(1), F(-5, 3)]:
        T = GA.add(GA.sc(1), GA.scal(t, _P(E[0])))
        x = _vec(F(2), F(1, 3), F(0), F(-1))
        GA.check("exp(t P_{e0}) translates by t e0", GA.eq(_sand(T, _X(x)), _X(GA.add(x, GA.scal(t, E[0])))))
    # dilation orbit: tabulated coefficients (rho^2/2 on e0 n_inf, rho^-2 on e0 n0)
    for rho, c_inf, c_0 in [(F(2), F(2), F(1, 4)), (F(3, 2), F(9, 8), F(4, 9)), (F(10), F(50), F(1, 100))]:
        D = _rotor(rho, _m(E[5], E[4]))
        GA.check("D_rho is a rotor", GA.eq(_m(D, GA.reverse(D)), GA.sc(1)))
        AZ = _sand(D, Z)
        GA.check("Ad(D_rho) Z = rho^2 P_{e0} + rho^-2 e0 n0 (tabulated)",
                 GA.eq(AZ, GA.add(GA.scal(c_inf, _m(E[0], NINF)), GA.scal(c_0, _m(E[0], N0)))))
        x = _vec(F(1), F(2), F(0), F(0))
        GA.check("D_rho dilates: X(x) -> rho^-2 X(rho^2 x)",
                 GA.eq(_sand(D, _X(x)), GA.scal(1 / (rho * rho), _X(GA.scal(rho * rho, x)))))
    # the normalised orbit converges to P_{e0}: remainder 16^{-k} e0 n0 at rho = 2^k
    for k, rem in [(1, F(1, 16)), (2, F(1, 256)), (3, F(1, 4096))]:
        rho = F(2) ** k
        D = _rotor(rho, _m(E[5], E[4]))
        diff = GA.sub(GA.scal(1 / (rho * rho), _sand(D, Z)), _P(E[0]))
        GA.check("rho^-2 Ad(D_rho) Z - P_{e0} = rho^-4 e0 n0", GA.eq(diff, GA.scal(rem, _m(E[0], N0))))
    return True


def check_boost_orbit_reaches_null_translations():
    premise("mass.chart-form-spin-isomorphism")
    premise("angle.imported-theorems-deliver-their-hypotheses")
    for rho, ch, sh in [(F(2), F(17, 8), F(15, 8)), (F(3), F(41, 9), F(40, 9))]:
        B = _rotor(rho, _m(E[1], E[0]))
        GA.check("Ad(B) P_{e0} = P_{cosh e0 + sinh e1} (tabulated)",
                 GA.eq(_sand(B, _P(E[0])), _P(_vec(ch, sh, F(0), F(0)))))
        GA.check("Ad(B) fixes n_inf", GA.eq(_sand(B, NINF), NINF))
        rem = GA.sub(GA.scal(2 / (rho * rho), _sand(B, _P(E[0]))), _P(GA.add(E[0], E[1])))
        GA.check("(2/rho^2) Ad(B) P_{e0} - P_{l} = rho^-4 P_{e0 - e1}",
                 GA.eq(rem, GA.scal(1 / rho ** 4, _P(GA.sub(E[0], E[1])))))
    # two-reflection versor V = (a + b) a carries a = e1 to a rational unit direction b
    for (b1, b2, b3) in [(F(2, 3), F(2, 3), F(1, 3)), (F(-2, 7), F(3, 7), F(-6, 7)), (F(0), F(-1), F(0))]:
        b = _vec(F(0), b1, b2, b3)
        a = E[1]
        V = _m(GA.add(a, b), a)
        n2 = _m(V, GA.reverse(V))
        GA.check("V V~ is a nonzero scalar", set(n2.keys()) <= {()} and n2.get((), F(0)) != 0)
        sc_ = n2.get((), F(0))
        img = GA.scal(1 / sc_, _sand(V, a))
        GA.check("V e1 V~ / (V V~) = b", GA.eq(img, b))
        GA.check("V fixes e0 and n_inf", GA.eq(GA.scal(1 / sc_, _sand(V, E[0])), E[0])
                 and GA.eq(GA.scal(1 / sc_, _sand(V, NINF)), NINF))
        GA.check("V carries P_{e0 + e1} to P_{e0 + b}",
                 GA.eq(GA.scal(1 / sc_, _sand(V, _P(GA.add(E[0], E[1])))), _P(GA.add(E[0], b))))
    # forward timelike vectors as positive combinations of two future null vectors (tabulated)
    for a, al, be, nh in [(_vec(F(5), F(3), F(0), F(0)), F(4), F(1), _vec(F(0), F(1), F(0), F(0))),
                          (_vec(F(9), F(2), F(-3), F(6)), F(8), F(1), _vec(F(0), F(2, 7), F(-3, 7), F(6, 7)))]:
        l1, l2 = GA.add(E[0], nh), GA.sub(E[0], nh)
        GA.check("l1, l2 future null", GA.dot(l1, l1, SQ) == 0 and GA.dot(l2, l2, SQ) == 0)
        GA.check("a = alpha l1 + beta l2 with alpha, beta > 0",
                 al > 0 and be > 0 and GA.eq(a, GA.add(GA.scal(al, l1), GA.scal(be, l2))))
        GA.check("P is linear: P_a = alpha P_{l1} + beta P_{l2}",
                 GA.eq(_P(a), GA.add(GA.scal(al, _P(l1)), GA.scal(be, _P(l2)))))
    return True


def check_controls_spacelike_past_and_wedge_reflection():
    premise("synthesis.positive-energy-selects-rule-2-sign")
    premise("angle.imported-theorems-deliver-their-hypotheses")
    R = _m(E[1], E[2])
    GA.check("e1 e2 is a rotor", GA.eq(_m(R, GA.reverse(R)), GA.sc(1)))
    GA.check("spacelike: Ad(e1 e2) P_{e1} = -P_{e1}", GA.eq(_sand(R, _P(E[1])), GA.neg(_P(E[1]))))
    GA.check("timelike: no rotation reverses P_{e0} (e1 e2 fixes it)", GA.eq(_sand(R, _P(E[0])), _P(E[0])))
    mZ = GA.neg(_m(E[0], E[4]))
    for rho, rem in [(F(2), F(1, 16)), (F(4), F(1, 256))]:
        D = _rotor(rho, _m(E[5], E[4]))
        diff = GA.sub(GA.scal(1 / (rho * rho), _sand(D, mZ)), GA.neg(_P(E[0])))
        GA.check("-Z: the orbit tends to the past translation -P_{e0}", GA.eq(diff, GA.scal(-rem, _m(E[0], N0))))
    # translations and Lorentz rotors fix n_inf; the dilation scales it
    T = GA.add(GA.sc(1), _P(_vec(F(1), F(2), F(-1), F(3))))
    GA.check("translation fixes n_inf", GA.eq(_sand(T, NINF), NINF))
    D = _rotor(F(3), _m(E[5], E[4]))
    GA.check("dilation scales n_inf by 9", GA.eq(_sand(D, NINF), GA.scal(F(9), NINF)))
    # wedge reflection: Ad(e0 e1) on X(x)
    W = _m(E[0], E[1])
    GA.check("e0 e1 squares to 1", GA.eq(_m(W, W), GA.sc(1)))
    for (x0, x1, x2, x3) in [(F(1), F(3), F(2), F(0)), (F(-2, 3), F(5), F(0), F(1, 2))]:
        img = _m(W, _X(_vec(x0, x1, x2, x3)), GA.reverse(W))
        # W W~ = -1, so W X W~ = -X(reflected): the same null ray, the wedge reflection
        GA.check("W W~ = -1", GA.eq(_m(W, GA.reverse(W)), GA.sc(-1)))
        GA.check("e0 e1 X(x) (e0 e1)~ = -X(-x0, -x1, x2, x3)", GA.eq(img, GA.scal(-1, _X(_vec(-x0, -x1, x2, x3)))))
        GA.check("control: not X(x) itself", not GA.eq(img, GA.scal(-1, _X(_vec(x0, x1, x2, x3)))))
    return True
