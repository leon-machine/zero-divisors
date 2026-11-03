"""interior.complex-scale-inverse-cube-killing-spinor: exact checks in Cl(1,3).

R + R I is identified with C by x + I y -> x + i y (multiplicative, checked). The Killing-spinor scalar of the
imported Walker-Penrose Fact, normalised to chi = r - i a cos(theta), corresponds to chi = r - I a cos(theta).
(1) The scale M_frak = -M z^{-3} of the Kerr curvature Fact (z = r - I a cos(theta), inverse cube built
    independently as conj(z)^3/|z|^6) satisfies chi^3 M_frak = -M exactly at several (M, r, a cos(theta)),
    off the ring and on the disc; the power is three: chi^2 M_frak and chi^4 M_frak are not -M.
(2) Winding: on a loop around the ring in the (r, -a cos(theta)) plane, chi = rho u with u running through 20 rational
    points of the unit circle (consecutive points less than 30 degrees apart, checked exactly), the quadrant-
    counted winding number of chi about 0 is 1 and that of M_frak = -M chi^{-3} is -3: three times the winding of
    the Killing spinor's scalar (in absolute value), opposite in sense.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S13 = GA.sig(1, 3)
I4 = GA.mul(GA.mul(GA.gen(0), GA.gen(1), S13), GA.mul(GA.gen(2), GA.gen(3), S13), S13)
KERR = [(F(1), F(2), F(3, 4)), (F(3), F(1, 2), F(-2)), (F(1, 2), F(5), F(7, 3)), (F(1), F(0), F(5, 4))]
TS = [F(0), F(1, 6), F(1, 3), F(1, 2), F(3, 4), F(1), F(4, 3), F(2), F(3), F(6), None,
      F(-6), F(-3), F(-2), F(-4, 3), F(-1), F(-3, 4), F(-1, 2), F(-1, 3), F(-1, 6)]
RHO = F(1, 2)
# Second factor for the check that the pseudoscalar-complex product agrees with QI multiplication.
CPLX_PROBE = (F(2), F(1, 3))


def cplx(x, y):
    return GA.add(GA.sc(x), GA.scal(y, I4))


def inv_cube(x, y):
    n = x * x + y * y
    zb = cplx(x, -y)
    return GA.scal(1 / (n * n * n), GA.mul(GA.mul(zb, zb, S13), zb, S13))


def power(z, k):
    out = GA.sc(1)
    for _ in range(k):
        out = GA.mul(out, z, S13)
    return out


def unit(t):
    if t is None:
        return GA.QI(-1, 0)
    d = 1 + t * t
    return GA.QI((1 - t * t) / d, 2 * t / d)


def quadrant(w):
    if w.im >= 0:
        return 0 if w.re > 0 else 1
    return 2 if w.re <= 0 else 3


def winding(ws):
    tot = 0
    for a, b in zip(ws, ws[1:] + ws[:1]):
        d = (quadrant(b) - quadrant(a)) % 4
        assert d in (0, 1, 3)
        tot += {0: 0, 1: 1, 3: -1}[d]
    return F(tot, 4)


def check_scale_is_minus_m_inverse_cube_of_killing_scalar():
    premise("interior.imported-kerr-curvature")
    premise("interior.complex-factorisation-location-ring")
    premise("interior.imported-walker-penrose-killing-spinor")
    ok = True
    for M, r, c in KERR:
        chi = cplx(r, -c)
        Mf = GA.scal(-M, inv_cube(r, -c))
        ok = ok and GA.eq(GA.mul(power(chi, 3), Mf, S13), GA.sc(-M))
        ok = ok and not GA.eq(GA.mul(power(chi, 2), Mf, S13), GA.sc(-M))
        # one power too many leaves exactly one factor of chi: chi^4 (-M / chi^3) = -M chi
        ok = ok and GA.eq(GA.mul(power(chi, 4), Mf, S13), GA.scal(-M, chi))
        (x, y), (u, v) = (r, -c), CPLX_PROBE
        p = GA.mul(cplx(x, y), cplx(u, v), S13)
        w = GA.QI(x, y) * GA.QI(u, v)
        ok = ok and GA.eq(p, cplx(w.re, w.im))
    _tp_rv = (ok); assert _tp_rv is not False, "check_scale_is_minus_m_inverse_cube_of_killing_scalar"; return _tp_rv


def check_winding_is_three_times_the_spinor_scalar():
    premise("interior.imported-walker-penrose-killing-spinor")
    us = [unit(t) for t in TS]
    ok = all((u * u.conj()) == GA.QI(1) for u in us)
    for a, b in zip(us, us[1:] + us[:1]):
        dot = (b * a.conj()).re
        ok = ok and dot > 0 and 4 * dot * dot > 3                    # angle below 30 degrees
    chis = [GA.QI(RHO) * u for u in us]
    M = F(1)
    mfs = [GA.QI(-M) / (c * c * c) for c in chis]
    ok = ok and winding(chis) == 1 and winding(mfs) == -3
    _tp_rv = (ok); assert _tp_rv is not False, "check_winding_is_three_times_the_spinor_scalar"; return _tp_rv
