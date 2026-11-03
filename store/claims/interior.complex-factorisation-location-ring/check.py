"""interior.complex-factorisation-location-ring: exact checks in Cl(1,3) and Gauge Theory Gravity.

I = gamma0 gamma1 gamma2 gamma3; sigma = gamma0 gamma1 stands for the principal plane pair (sigma^2 = 1);
S(B) = -(B + 3 sigma B sigma)/2. The Kerr curvature itself is the imported Fact (not recomputed from Kerr gauge
fields); its a = 0 member is recomputed from the Schwarzschild interior gauge fields.
(1) R + R I: I^2 = -1, I commutes with all 8 even blades and anticommutes with the 4 vectors; z = x + I y times
    z~ = x - I y is x^2 + y^2, and z~/(x^2 + y^2) is the inverse; x + I y -> x + i y is multiplicative on samples.
(2) With M_frak = -M z^{-3} (z = r - I a cos(theta)), the Fact's (M/2) z^{-3} (B + 3 sigma B sigma) equals
    M_frak S(B) on all six frame planes; S^2 + S = 2 on complexified bivectors, S commutes with the scale;
    eigenvalues -2 M_frak on {sigma, I sigma} and M_frak on the four mixed planes: ratio 2 : (-1) with values
    in R + R I. Several (M, r, a cos(theta)).
(3) Locus: for a != 0, z z~ = r^2 + a^2 cos^2(theta) vanishes on a grid of rational (r, cos(theta)) only at
    r = 0, cos(theta) = 0 (the ring). On the disc (r = 0, a cos(theta) = c != 0): z^3 = I c^3 and
    M_frak = M I c^{-3}, finite and purely pseudoscalar.
(4) a = 0: M_frak = -M/r^3, and M_frak S(B) equals the store curvature calR(B) = -R(hb(B)) computed from the
    Schwarzschild interior gauge fields (hb, Omega) (torsion-free Omega) on all six frame planes, at three radii,
    with sigma = e_0 ^ e_1 the (tau, t) plane.
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise

# ---- GTG engine: lib/gtg.py (jets, Field, torsion, curvature) ----
S13 = gtg.S13
# the Schwarzschild(-de Sitter) interior field in synchronous gauge, labels (r, t, theta, phi), 2M = 1:
# interior_field(r0, w, s0, c0) -> (field, Lambda, (r, A, sA, s1, s2, sn, cs))
interior_field = gtg.sync_interior_field

I4 = GA.mul(GA.mul(GA.gen(0), GA.gen(1), S13), GA.mul(GA.gen(2), GA.gen(3), S13), S13)
SIG = GA.mul(GA.gen(0), GA.gen(1), S13)
PLANES = [(a, b) for a in range(4) for b in range(a + 1, 4)]
KERR = [(F(1), F(2), F(3, 4)), (F(3), F(1, 2), F(-2)), (F(1, 2), F(5), F(7, 3))]   # (M, r, a cos theta)
ZS = [(F(3), F(-2)), (F(1, 2), F(5, 3)), (F(0), F(1))]
INTERIOR = [(F(1, 2), F(1), F(3, 5), F(4, 5)), (F(1, 5), F(2), F(5, 13), F(12, 13)),
            (F(4, 5), F(1, 2), F(4, 5), F(3, 5))]


def cplx(x, y):
    return GA.add(GA.sc(x), GA.scal(y, I4))


def shape(B):
    return GA.scal(F(-1, 2), GA.add(B, GA.scal(3, GA.mul(GA.mul(SIG, B, S13), SIG, S13))))


def inv_cube(x, y):
    n = x * x + y * y
    zb = cplx(x, -y)
    return GA.scal(1 / (n * n * n), GA.mul(GA.mul(zb, zb, S13), zb, S13))


def check_pseudoscalar_subalgebra_is_a_field():
    ok = GA.eq(GA.mul(I4, I4, S13), GA.sc(-1))
    for bl in GA.all_blades(4):
        e = {bl: F(1)}
        ok = ok and (GA.commutes(I4, e, S13) if len(bl) % 2 == 0 else GA.anticommutes(I4, e, S13))
    for x, y in ZS:
        z, zb = cplx(x, y), cplx(x, -y)
        ok = ok and GA.eq(GA.mul(z, zb, S13), GA.sc(x * x + y * y))
        ok = ok and GA.eq(GA.mul(z, GA.scal(1 / (x * x + y * y), zb), S13), GA.sc(1))
        for u, v in ZS:
            prod = GA.mul(z, cplx(u, v), S13)
            w = GA.QI(x, y) * GA.QI(u, v)
            ok = ok and GA.eq(prod, cplx(w.re, w.im))
    _tp_rv = (ok); assert _tp_rv is not False, "check_pseudoscalar_subalgebra_is_a_field"; return _tp_rv


def check_kerr_scale_times_shape():
    premise("interior.imported-kerr-curvature")
    premise("interior.exact-scale-decoupling")
    ok = True
    for M, r, c in KERR:
        zi3 = inv_cube(r, -c)                                   # z = r - I c
        z = cplx(r, -c)
        ok = ok and GA.eq(GA.mul(GA.mul(GA.mul(z, z, S13), z, S13), zi3, S13), GA.sc(1))
        Mf = GA.scal(-M, zi3)
        for (a, b) in PLANES:
            B = GA.mul(GA.gen(a), GA.gen(b), S13)
            fact = GA.mul(GA.scal(M / 2, zi3), GA.add(B, GA.scal(3, GA.mul(GA.mul(SIG, B, S13), SIG, S13))), S13)
            ok = ok and GA.eq(fact, GA.mul(Mf, shape(B), S13))
            for zz in (cplx(1, 0), cplx(F(2), F(-3))):
                X = GA.mul(zz, B, S13)
                SX = shape(X)
                ok = ok and GA.eq(SX, GA.mul(zz, shape(B), S13))
                ok = ok and GA.eq(GA.add(shape(SX), SX), GA.scal(2, X))
            lam = -2 if (a, b) in ((0, 1), (2, 3)) else 1
            ok = ok and GA.eq(GA.mul(Mf, shape(B), S13), GA.scal(lam, GA.mul(Mf, B, S13)))
        ok = ok and GA.eq(GA.mul(I4, SIG, S13), GA.mul(GA.gen(2), GA.gen(3), S13))
    _tp_rv = (ok); assert _tp_rv is not False, "check_kerr_scale_times_shape"; return _tp_rv


def check_noninvertibility_locus_is_the_ring():
    premise("interior.imported-kerr-curvature")
    ok = True
    grid = [F(0), F(1, 3), F(-2), F(5, 7), F(1)]
    for a in (F(1), F(3, 2)):
        for r in grid:
            for ct in grid:
                n = r * r + (a * ct) ** 2
                ok = ok and GA.eq(GA.mul(cplx(r, -a * ct), cplx(r, a * ct), S13), GA.sc(n))
                ok = ok and (n == 0) == (r == 0 and ct == 0)
    for M, c in ((F(1), F(5, 4)), (F(2), F(-1, 3))):
        zd = cplx(F(0), -c)
        z3 = GA.mul(GA.mul(zd, zd, S13), zd, S13)
        ok = ok and GA.eq(z3, GA.scal(c ** 3, I4))
        Mf = GA.scal(-M, inv_cube(F(0), -c))
        ok = ok and GA.eq(Mf, GA.scal(M / c ** 3, I4))
    _tp_rv = (ok); assert _tp_rv is not False, "check_noninvertibility_locus_is_the_ring"; return _tp_rv


def check_a_zero_is_schwarzschild_from_gauge_fields():
    premise("interior.exact-scale-decoupling")
    ok = True
    M = F(1, 2)
    for r0, w, s0, c0 in INTERIOR:
        fld, lam, jets = interior_field(r0, w, s0, c0)
        ok = ok and lam == 0 and fld.torsion_free() and fld.torsion_rank() == 24
        Rc = fld.curvature()
        Mf = GA.scal(-M, inv_cube(r0, F(0)))
        ok = ok and GA.eq(Mf, GA.sc(-M / r0 ** 3))
        for (a, b) in PLANES:
            ok = ok and GA.eq(Rc[(a, b)], GA.mul(Mf, shape(GA.mul(GA.gen(a), GA.gen(b), S13)), S13))
    _tp_rv = (ok); assert _tp_rv is not False, "check_a_zero_is_schwarzschild_from_gauge_fields"; return _tp_rv
