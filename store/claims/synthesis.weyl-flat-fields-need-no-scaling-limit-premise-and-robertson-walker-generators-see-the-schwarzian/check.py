"""Null generators of a Robertson-Walker (Weyl-flat) field and the conformal vacuum: exact checks.

Field hb(b) = b/a(t), t = x . e0 the conformal time; along a null line x0 + lambda k (k null, k . e0 = 1)
t = t0 + lambda, and the physical affine parameter psi has psi' = a(t)^2 (the flat lambda is affine for the
flat metric). With the transverse labels the flat ones, the CAR on the generator forces the generator field
to carry weight 1/2 in the affine parameter, so the conformal vacuum's generator kernel, read in psi, is the
weight-1/2 pullback of the null vacuum W0 = (i/2 pi)(u - v + i0)^-1 by the inverse map.
(1) Schwarzian: S_psi = psi'''/psi' - (3/2)(psi''/psi')^2 = 2 a''/a - 4 (a'/a)^2 (conformal-time
    derivatives), checked at rational times for polynomial a; and S_psi = -2a (1/a)'' exactly, so S_psi
    vanishes identically exactly when 1/a is linear in t.
(2) Families, computed as rational functions from the derivatives of a^2: a = t^n gives S = -2 n (n + 1)/t^2, zero exactly for n = 0 (flat) and n = -1 (de Sitter in
    conformal time, a = -1/(H t)); radiation (n = 1) S = -4/t^2, matter (n = 2) S = -12/t^2; for
    a = 1/(alpha t + beta) S = 0, and psi = -1/(alpha (alpha t + beta)) is Moebius in t with psi' = a^2.
(3) Kernels: for a Moebius psi the squared ratio psi'(u) psi'(v) (u - v)^2 / (psi(u) - psi(v))^2 is exactly 1
    (the pulled-back null vacuum is the null vacuum); for the radiation field (psi = ((t0 + l)^3 - t0^3)/3)
    it is 1 + S_psi(v) x^2/6 + O(x^3), x = u - v, with S_psi(v) = -4/(t0 + v)^2 nonzero: the remainder is the
    Schwarzian kernel, continuous and zero on the diagonal, not zero.
(4) Bulk scaling with a conformal factor a = s^2: the flat massless kernel W(z) = z/Q(z)^2 obeys
    c^3 W(c z) = W(z), so a(t0)^-3 W(z) = W(a(t0) z); the factor (s(t0 + l t1) s(t0 + l t2))^-3 tends to
    s(t0)^-6 with an error at most K l (checked on a decreasing sequence of l).
(0) Conformal-covariance lemma: along x0 + f k the geodesic equation of the derived metric is
    f'' + 2 f'^2 phi'/phi = 0, solved by f' = phi^-2 (f' = phi^-1 leaves phi'/phi^3), and the covector
    phi^2 f' (k . ) is the flat one, so the microlocal sets C^pm agree.
(5) In the physical parameter: with image points u = Psi(u_l), v = Psi(v_l) the squared ratio is the
    reciprocal of the lambda one, and (r^2 - 1)/x~^2 tends to S_Phi/6 with S_Phi = -S/a^4 (radiation:
    4/t^6), the leading coefficient of the kernel (i/2 pi)(1/12) S_Phi (u - v).
Exact arithmetic only (Fractions); i = I4 enters only through the stored null vacuum and is not needed here.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S4 = (1, -1, -1, -1)
E = [GA.gen(i) for i in range(4)]
ONE = GA.sc(1)
APOLYS = [[F(1), F(1), F(1)], [F(2), F(0), F(1, 3), F(1, 5)], [F(1, 2), F(3)], [F(0), F(0), F(1)]]
TIMES = (F(1, 2), F(3), F(1, 7), F(2), F(5, 3))
POWERS = (-3, -2, -1, 0, 1, 2, 3)
DS = [(F(1), F(2)), (F(-1, 2), F(3)), (F(3), F(-1, 4))]
T0S = (F(1), F(1, 3), F(4))
XS = [F(1, 10 ** j) for j in range(1, 9)]
PTS = [(F(1), F(3), F(0), F(1)), (F(2), F(1, 2), F(-1), F(1, 3)), (F(5), F(1), F(2), F(-2))]
SPOLY = [F(1), F(1, 2), F(1, 3)]


def schwarzian(p1, p2, p3):
    return p3 / p1 - F(3, 2) * (p2 / p1) ** 2


def check_schwarzian_of_the_physical_affine_parameter():
    premise("synthesis.imported-gtg-dictionary")
    premise("synthesis.local-normality-at-the-edge-gives-the-null-ground-state")
    ok = True
    for a in APOLYS:
        da, dda = GA.pderiv(a), GA.pderiv(GA.pderiv(a))
        p1 = GA.pmul(a, a)                              # psi' = a^2
        p2, p3 = GA.pderiv(p1), GA.pderiv(GA.pderiv(p1))
        for t in TIMES:
            av, d1, d2 = GA.peval(a, t), GA.peval(da, t), GA.peval(dda, t)
            ok &= av > 0
            S = schwarzian(GA.peval(p1, t), GA.peval(p2, t), GA.peval(p3, t))
            ok &= S == 2 * d2 / av - 4 * (d1 / av) ** 2
            inv2 = (2 * d1 * d1 - av * d2) / av ** 3       # (1/a)''
            ok &= S == -2 * av * inv2
    GA.check("Schwarzian of the physical affine parameter psi' = a^2: S = 2a''/a - 4(a'/a)^2 = -2a (1/a)''", ok)
    return ok


def rf_schwarzian_of_psi(a):
    """S_Psi for Psi' = a^2, computed from the derivatives of a^2 as a rational function."""
    p1 = a * a
    p2 = p1.deriv()
    p3 = p2.deriv()
    r = p2 / p1
    return p3 / p1 - GA.RF.const(F(3, 2)) * r * r


def t_power(n):
    T = GA.RF.var()
    out = GA.RF1
    for _ in range(abs(n)):
        out = out * T
    return out if n >= 0 else GA.RF1 / out


def check_schwarzian_vanishes_exactly_on_de_sitter_and_flat():
    premise("synthesis.imported-gtg-dictionary")
    premise("synthesis.null-vacuum-on-a-horizon-generator")
    ok = True
    T = GA.RF.var()
    zero_at = []
    for n in POWERS:
        S = rf_schwarzian_of_psi(t_power(n))
        target = GA.RF.const(F(-2 * n * (n + 1))) / (T * T)
        ok &= S.eqrf(target)
        if S.is_zero():
            zero_at.append(n)
    ok &= zero_at == [-1, 0]
    ok &= rf_schwarzian_of_psi(t_power(1)).eqrf(GA.RF.const(F(-4)) / (T * T))
    ok &= rf_schwarzian_of_psi(t_power(2)).eqrf(GA.RF.const(F(-12)) / (T * T))
    for al, be in DS:
        w = GA.RF([be, al])                                   # alpha t + beta
        a = GA.RF1 / w
        ok &= rf_schwarzian_of_psi(a).is_zero()
        psi = GA.RF.const(F(-1)) / (GA.RF.const(al) * w)      # a Moebius map of t
        ok &= psi.deriv().eqrf(a * a)
    # a non-de-Sitter rational a (1/a quadratic) has S != 0
    ok &= not rf_schwarzian_of_psi(GA.RF1 / GA.RF([F(1), F(0), F(1)])).is_zero()
    GA.check("S computed from the derivatives of a^2: -2n(n+1)/t^2 for a = t^n, zero only at n = 0, -1; "
             "radiation -4/t^2, matter -12/t^2; zero for a = 1/(alpha t + beta) with Moebius Psi", ok)
    return ok


def check_pulled_back_vacuum_differs_by_the_schwarzian_kernel():
    premise("synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes")
    premise("synthesis.local-normality-at-the-edge-gives-the-null-ground-state")
    premise("synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state")
    ok = True
    # Moebius (de Sitter): psi(t) = -1/(al (al t + be)): squared ratio exactly 1
    for al, be in DS:
        psi = lambda t: -1 / (al * (al * t + be))
        dpsi = lambda t: 1 / (al * t + be) ** 2
        for v in (F(1), F(2, 3)):
            for x in XS[:4]:
                u = v + x
                if (al * u + be) == 0 or (al * v + be) == 0:
                    continue
                ok &= dpsi(u) * dpsi(v) * x * x == (psi(u) - psi(v)) ** 2
    # radiation: psi = ((t0 + l)^3 - t0^3)/3, psi' = (t0 + l)^2
    for t0 in T0S:
        psi = lambda l: ((t0 + l) ** 3 - t0 ** 3) / 3
        dpsi = lambda l: (t0 + l) ** 2
        v = F(0)
        S = -F(4) / (t0 + v) ** 2
        ok &= S == schwarzian(dpsi(v), 2 * (t0 + v), F(2))
        prev = None
        for x in XS:
            u = v + x
            r2 = dpsi(u) * dpsi(v) * x * x / (psi(u) - psi(v)) ** 2
            ok &= r2 != 1
            dev = (r2 - 1) / (x * x) - S / 6
            ok &= abs(dev) <= 2 * x / t0 ** 3
            if prev is not None:
                ok &= abs(dev) < abs(prev)
            prev = dev
    GA.check("de Sitter: pulled-back null vacuum is the null vacuum exactly; radiation: squared ratio "
             "1 + S x^2/6 + O(x^3) with S = -4/t^2, the Schwarzian kernel", ok)
    return ok


def Qf(x):
    return GA.dot(x, x, S4)


def W(x):
    q = Qf(x)
    return GA.scal(1 / (q * q), x)


def vec(c):
    return GA.add(*[GA.scal(F(c[i]), E[i]) for i in range(4)])


def check_conformal_factor_scales_to_local_inertial_coordinates():
    premise("synthesis.imported-microlocal-hadamard-condition")
    premise("field-theory.second-quantisation")
    ok = True
    for t0 in T0S:
        s0 = GA.peval(SPOLY, t0)
        c = s0 * s0                                    # a(t0) = s(t0)^2
        for p in PTS:
            z = vec(p)
            ok &= GA.eq(GA.scal(c ** 3, W(GA.scal(c, z))), W(z))
            ok &= GA.eq(GA.scal(1 / c ** 3, W(z)), W(GA.scal(c, z)))
        t1, t2 = F(1), F(-2)
        prev = None
        for l in XS:
            fac = 1 / (GA.peval(SPOLY, t0 + l * t1) * GA.peval(SPOLY, t0 + l * t2)) ** 3
            err = abs(fac - 1 / s0 ** 6)
            ok &= err <= 30 * l
            if prev is not None:
                ok &= err < prev
            prev = err
    GA.check("conformal factor: a(t0)^-3 W(z) = W(a(t0) z) and the factor tends to a(t0)^-3 at rate l: "
             "the scaling limit is the flat massless vacuum in local inertial coordinates", ok)
    return ok


def check_conformal_null_geodesics_keep_their_covectors():
    premise("synthesis.imported-gtg-dictionary")
    premise("synthesis.imported-microlocal-hadamard-condition")
    ok = True
    for a in APOLYS[:3]:
        da = GA.pderiv(a)
        for t in TIMES:
            av, dav = GA.peval(a, t), GA.peval(da, t)
            ok &= av > 0 and dav != 0
            fp = 1 / av ** 2                           # f' = phi^-2
            fpp = -2 * dav * fp / av ** 3              # d/dlambda~ (phi^-2) = -2 phi^-3 phi' f'
            ok &= fpp + 2 * fp * fp * dav / av == 0    # the geodesic equation along the null line
            ok &= av * av * fp == 1                    # covector phi^2 f' (k . ) = (k . )
            gp = 1 / av                                # f' = phi^-1 is not affine
            gpp = -1 * dav * gp / av ** 2
            ok &= gpp + 2 * gp * gp * dav / av == dav / av ** 3
    for n1, n2, n3 in ((F(3, 13), F(4, 13), F(12, 13)), (F(1, 3), F(2, 3), F(2, 3))):
        k = vec((1, n1, n2, n3))
        ok &= GA.dot(k, k, S4) == 0 and GA.dot(k, E[0], S4) == 1
    GA.check("conformally flat field: flat null lines with f' = phi^-2 are affine null geodesics with the flat "
             "covector (f' = phi^-1 leaves the residual phi'/phi^3)", ok)
    return ok


def check_leading_term_in_the_physical_parameter():
    premise("synthesis.local-normality-at-the-edge-gives-the-null-ground-state")
    premise("synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state")
    ok = True
    for t0 in T0S:
        psi = lambda l: ((t0 + l) ** 3 - t0 ** 3) / 3        # radiation, a = t, Psi' = (t0 + l)^2
        dpsi = lambda l: (t0 + l) ** 2
        vl = F(1, 2)
        a2 = dpsi(vl)
        S_psi = -F(4) / (t0 + vl) ** 2
        S_phi = -S_psi / (a2 * a2)                          # inversion rule, -S/a^4
        prev = None
        for x in XS:
            ul = vl + x
            u, v = psi(ul), psi(vl)                          # image points in the physical parameter
            xt = u - v
            # squared ratio in lambda~: Phi'(u) Phi'(v) xt^2 / (Phi(u) - Phi(v))^2 with Phi' = 1/Psi'
            r2t = xt * xt / (dpsi(ul) * dpsi(vl) * x * x)
            dev = (r2t - 1) / (xt * xt) - S_phi / 6
            ok &= r2t != 1
            if prev is not None:
                ok &= abs(dev) < abs(prev)
            prev = dev
        ok &= abs(prev) < F(1, 10 ** 5)
        ok &= S_phi == F(4) / (t0 + vl) ** 6
    GA.check("in the physical parameter the Schwarzian kernel's coefficient is S_Phi = -S/a^4 (radiation: "
             "4/t^6), the squared ratio approaching 1 + S_Phi x~^2/6", ok)
    return ok


if __name__ == "__main__":
    for fn in (check_conformal_null_geodesics_keep_their_covectors, check_leading_term_in_the_physical_parameter,
               check_schwarzian_of_the_physical_affine_parameter,
               check_schwarzian_vanishes_exactly_on_de_sitter_and_flat,
               check_pulled_back_vacuum_differs_by_the_schwarzian_kernel,
               check_conformal_factor_scales_to_local_inertial_coordinates):
        fn()
    print("FAILURES:", GA.FAILURES)
