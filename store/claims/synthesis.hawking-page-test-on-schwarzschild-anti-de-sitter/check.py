"""synthesis.hawking-page-test-on-schwarzschild-anti-de-sitter: exact checks.

pi is a formal symbol: an entropy or a free energy times a temperature is recorded by its
coefficient of pi. Units G = hbar = 1, L2 = ell^2 = -3/Lambda rational. Along the family at fixed
L2 the mass is read as a function of the horizon radius, M(r) = r (1 + r^2/L2)/2.
"""
from fractions import Fraction as F
import GA
from GA import RF
from tp_premise import premise

RADII = [F(1, 5), F(1, 2), F(1), F(3, 2), F(7, 3), F(10)]
ELLS = [F(1), F(2), F(3, 2), F(5, 7)]


def f_val(M, L2, r):
    return 1 - 2 * M / r + r * r / L2


def fprime(M, L2, r):
    return 2 * M / (r * r) + 2 * r / L2


def check_chart_and_first_law():
    premise("synthesis.sds-clausius-fixes-area-constant")
    premise("synthesis.quarter-from-temperature")
    ok = True
    r = RF.var()
    for ell in ELLS:
        L2 = ell * ell
        Mr = r * (RF.const(1) + r * r / RF.const(L2)) / RF.const(2)
        dM = Mr.deriv()
        for rh in RADII:
            M = Mr.eval(rh)
            x2 = rh * rh / L2
            # r_h is a zero of f, and f is increasing, so it is the only positive zero
            ok = ok and f_val(M, L2, rh) == 0 and M > 0
            for t in (F(1, 7), F(1), F(9)):
                ok = ok and fprime(M, L2, t) > 0
            # (o): beta^2 = 2M/r - r^2/L2 is positive at the horizon locus (it equals 1 there),
            # vanishes at r_*^3 = 2 M L2, and r_h^3 < r_*^3; r_h < 2M
            ok = ok and 2 * M / rh - rh * rh / L2 == 1
            ok = ok and rh ** 3 < 2 * M * L2 and rh < 2 * M
            # (i): 4 pi T = f'(r_h) = (1 + 3 x^2)/r_h, and Clausius dM = T dS with S/pi = r^2
            T4pi = fprime(M, L2, rh)
            ok = ok and T4pi == (1 + 3 * x2) / rh
            ok = ok and dM.eval(rh) == T4pi / 4 * (2 * rh)
            ok = ok and dM.eval(rh) == (1 + 3 * x2) / 2
    GA.check("SAdS: one horizon locus inside the PG chart, 4 pi T = (1 + 3x^2)/r_h, dM = T d(pi r^2)", ok)
    return ok


def check_branches_and_free_energy():
    premise("synthesis.sds-clausius-fixes-area-constant")
    ok = True
    x = RF.var()
    # tau(x) = 4 pi ell T = (1 + 3 x^2)/x ; d tau/dx = (3 x^2 - 1)/x^2
    tau = (RF.const(1) + RF.const(3) * x * x) / x
    dtau = tau.deriv()
    for t in (F(1, 9), F(1, 2), F(4, 7)):          # x^2 < 1/3: small branch, T falls as x grows
        ok = ok and 3 * t * t < 1 and dtau.eval(t) < 0
    for t in (F(3, 5), F(1), F(8)):                # x^2 > 1/3: large branch, T rises
        ok = ok and 3 * t * t > 1 and dtau.eval(t) > 0
    # the minimum: tau^2 = (1 + 3 x^2)^2 / x^2 at x^2 = 1/3 is 12, so T_min = sqrt(3)/(2 pi ell)
    x2 = F(1, 3)
    ok = ok and (1 + 3 * x2) ** 2 / x2 == 12
    # tau^2 >= 12 everywhere: (1 + 3 x^2)^2 - 12 x^2 = (1 - 3 x^2)^2
    for t in (F(1, 9), F(1, 2), F(3, 5), F(1), F(8)):
        ok = ok and (1 + 3 * t * t) ** 2 - 12 * t * t == (1 - 3 * t * t) ** 2
    # (iii) under (Z): F/ell = m - tau s /(4 pi ell^2) with m = x (1 + x^2)/2, S = pi ell^2 x^2
    for t in (F(1, 9), F(1, 2), F(3, 5), F(1), F(3, 2), F(8)):
        m = t * (1 + t * t) / 2
        Fz = m - tau.eval(t) * t * t / 4
        ok = ok and Fz == t * (1 - t * t) / 4
        ok = ok and (Fz > 0) == (t < 1) and (Fz == 0) == (t == 1)
    # at x = 1: 4 pi ell T = 4, so T_HP = 1/(pi ell); (T_HP/T_min)^2 = 16/12 = 4/3
    ok = ok and tau.eval(F(1)) == 4 and F(16, 12) == F(4, 3)
    # the jump at x = 1: M = ell, S = pi ell^2, and T_HP S = (1/(pi ell)) pi ell^2 = ell
    ok = ok and F(1) * (1 + 1) / 2 == 1 and tau.eval(F(1)) / 4 * 1 == 1
    GA.check("SAdS: T_min^2 = 3/(2 pi ell)^2 at x^2 = 1/3, F = r_h (1 - x^2)/4, zero at x = 1, T_HP = 1/(pi ell)", ok)
    return ok


def check_dimension_d():
    premise("synthesis.sds-clausius-fixes-area-constant")
    ok = True
    r = RF.var()
    for d in (4, 5, 6, 7):
        for ell in ELLS:
            L2 = ell * ell
            # per unit of Omega_{d-2}: S = r^{d-2}/4 ; 4 pi T = ((d-3) + (d-1) r^2/L2)/r
            S = RF.const(F(1, 4))
            for _ in range(d - 2):
                S = S * r
            T4pi = (RF.const(d - 3) + RF.const(d - 1) * r * r / RF.const(L2)) / r
            # Clausius energy: 16 pi M = (d-2) r^{d-3} (1 + r^2/L2)
            M16 = RF.const(d - 2) * (RF.const(1) + r * r / RF.const(L2))
            for _ in range(d - 3):
                M16 = M16 * r
            for rh in RADII:
                ok = ok and M16.deriv().eval(rh) == 4 * T4pi.eval(rh) * S.deriv().eval(rh)
                # 16 pi F = 16 pi M - 4 (4 pi T) S = r^{d-3} (1 - r^2/L2)
                F16 = M16.eval(rh) - 4 * T4pi.eval(rh) * S.eval(rh)
                ok = ok and F16 == rh ** (d - 3) * (1 - rh * rh / L2)
            # at r_h = ell: 4 pi ell T = 2 (d - 2), so T_HP = (d-2)/(2 pi ell)
            ok = ok and T4pi.eval(ell) * ell == 2 * (d - 2)
        # minimum at x^2 = (d-3)/(d-1): (4 pi ell T)^2 = 4 (d-1)(d-3)
        x2 = F(d - 3, d - 1)
        ok = ok and ((d - 3) + (d - 1) * x2) ** 2 / x2 == 4 * (d - 1) * (d - 3)
    # d = 5: T_HP = 3/(2 pi ell) and T_min^2 = 32/(4 pi ell)^2 = 2/(pi ell)^2
    ok = ok and F(2 * (5 - 2), 4) == F(3, 2) and F(4 * 4 * 2, 16) == 2
    GA.check("d = 4..7: F = Omega r_h^{d-3} (1 - x^2)/(16 pi), T_HP = (d-2)/(2 pi ell), d = 5 gives 3/(2 pi ell)", ok)
    return ok


def check_wald_constant_removes_the_transition():
    premise("synthesis.euler-term-horizon-entropy-shift")
    premise("synthesis.imported-wald-noether-charge-entropy")
    ok = True
    # the shift -3 pi chi/(2 Lambda G) at chi = 2, Lambda = -3/L2: coefficient of pi is +L2
    for ell in ELLS:
        L2 = ell * ell
        Lam = -3 / L2
        ok = ok and F(-3) * 2 / (2 * Lam) == L2
    # in units of ell: F_W/ell = x (1 - x^2)/4 - tau/4, tau = (1 + 3 x^2)/x, equals -(1 + x^2)^2/(4 x)
    for t in (F(1, 9), F(1, 2), F(3, 5), F(1), F(3, 2), F(8)):
        tau = (1 + 3 * t * t) / t
        Fw = t * (1 - t * t) / 4 - tau / 4
        ok = ok and Fw == -(1 + t * t) ** 2 / (4 * t) and Fw < 0
        # orientation: beta F_W = -(L2/(64 pi)) * integral of the Weyl square 48 M^2/r^6 over the
        # Euclidean exterior, beta * 4 pi * 16 M^2/r_h^3; in units ell = 1, coefficient of pi
        m = t * (1 + t * t) / 2
        beta_over_pi = 4 * t / (1 + 3 * t * t)
        ok = ok and beta_over_pi * Fw == -F(1, 64) * beta_over_pi * 4 * 16 * m * m / t ** 3
    # at equal temperature x_s x_l = 1/3, and g(x) = (1 + x^2)^2/x is larger on the large branch
    for xl in (F(3, 5), F(1), F(3, 2), F(8)):
        xs = 1 / (3 * xl)
        ok = ok and (1 + 3 * xs * xs) / xs == (1 + 3 * xl * xl) / xl
        g = lambda t: (1 + t * t) ** 2 / t
        ok = ok and g(xl) - g(xs) == (3 * xl * xl - 1) ** 3 / (27 * xl ** 3) and g(xl) > g(xs)
    GA.check("Wald constant +pi ell^2: F_W = -ell (1 + x^2)^2/(4x) < 0 on both branches, no zero at x = 1", ok)
    return ok
