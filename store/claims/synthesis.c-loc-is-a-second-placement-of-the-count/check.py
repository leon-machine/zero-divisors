"""synthesis.c-loc-is-a-second-placement-of-the-count: exact checks.

pi is a formal symbol: a quantity c pi^k is stored as its rational coefficient c with k tracked in the
comments; where pi enters a comparison with 1 it is bounded by Archimedes' rationals 3 < pi < 22/7.
(i) the curvature-cutoff locus lies strictly inside the Schwarzschild horizon exactly when M > 1/2, and the
curvature scale on the horizon is 1/(4M^2); on Kerr test holes the cutoff tube |z| = (2M)^{1/3} lies inside
r_-, so no horizon point is on it. (ii) the outgoing null generators of r = 2M have zero expansion there.
(iii) the double count: with two independent copies of the count the area law halves eta and Jacobson's
G_cl = 1/(4 eta) doubles. (iv) two Kerr test holes where the literal tube count and the (C_loc) horizon count
of the same hole differ, one below and one above.
"""
from fractions import Fraction as F
import GA
from GA import RF
import series
from tp_premise import premise


def icbrt(n):
    """exact integer cube root of a perfect cube, else None"""
    return series.iroot(n, 3)


def isqrt(n):
    """exact integer square root of a perfect square, else None (not series.isqrt, the floor)"""
    return series.iroot(n, 2)


def check_cutoff_meets_no_horizon():
    premise("singularity.stretched-singularity-count")
    premise("synthesis.kerr-ring-count-misses-area-law")
    M = RF.var()
    # r_c < r_h  <=>  r_c^3 < r_h^3  <=>  (2M)^3 - 2M > 0, and (2M)^3 - 2M = 2M (2M - 1)(2M + 1)
    gap = (RF.const(2) * M) * (RF.const(2) * M) * (RF.const(2) * M) - RF.const(2) * M
    GA.check("(2M)^3 - 2M = 2M(2M - 1)(2M + 1)",
             gap.eqrf(RF.const(2) * M * (RF.const(2) * M - RF.const(1)) * (RF.const(2) * M + RF.const(1))))
    GA.check("threshold M = 1/2", gap.eval(F(1, 2)) == 0 and gap.eval(F(3, 5)) > 0 and gap.eval(F(1, 3)) < 0)
    # curvature scale on the horizon: 2M/(2M)^3 = 1/(4 M^2)
    on_h = RF.const(2) * M / ((RF.const(2) * M) * (RF.const(2) * M) * (RF.const(2) * M))
    GA.check("horizon curvature scale 1/(4M^2)", on_h.eqrf(RF.const(1) / (RF.const(4) * M * M)))
    # Kerr test holes: 2M = 10^3, rho_c = 10; r_- = a^2/(M + sqrt(M^2 - a^2)) recomputed two ways
    expect = {300: (400, 100), 400: (300, 200), 480: (140, 360)}
    for a, (s_exp, rm_exp) in expect.items():
        Mk = 500
        rho = icbrt(2 * Mk)
        s = isqrt(Mk * Mk - a * a)
        GA.check("rho_c = 10, sqrt exact", rho == 10 and s == s_exp)
        GA.check("r_- = M - s = a^2/(M + s)", Mk - s == rm_exp and F(a * a, Mk + s) == rm_exp)
        GA.check("regime a^2 >= 8 M rho_c", a * a - 8 * Mk * rho >= 0)
        GA.check("tube inside r_-: rho_c < r_-", rm_exp - rho > 0)
        GA.check("outer horizon curvature 2M/r_+^3 < 1", F(2 * Mk, (Mk + s) ** 3) < 1)
    return True


def check_killing_patch_is_local_rindler():
    premise("synthesis.imported-jacobson-clausius-1995")
    # ingoing Eddington-Finkelstein, outgoing radial null k = d_v + (f/2) d_r; expansion of the round
    # cross-sections theta = (f/2) d(r^2)/dr / r^2 = f/r; shear zero by spherical symmetry
    r = RF.var()
    for m in (F(1), F(5, 3), F(500)):
        f = RF.const(1) - RF.const(2 * m) / r
        theta = f * RF.const(F(1, 2)) * (r * r).deriv() / (r * r)
        GA.check("theta = f/r", theta.eqrf(f / r))
        GA.check("theta = 0 on r = 2M", theta.eval(2 * m) == 0)
        GA.check("control: theta != 0 off the horizon", theta.eval(3 * m) != 0)
    return True


def check_double_count_doubles_newton_constant():
    premise("scrambling.epoch-modular-period-two-unknowns-become")
    premise("scrambling.area-law-test")
    premise("synthesis.clausius-route-newton-constant-is-residue")
    premise("synthesis.imported-jacobson-clausius-1995")
    # write x = pi nu <s> (a pure number). Epoch count entropy per unit horizon area: 4 x.
    # (C_loc)(i) horizon density: eta = 4 x. Area law S = A/4 (G = 1).
    premise("synthesis.quarter-from-temperature")
    # (S_tot): S_BH = int dM/T with T = 1/(8 pi M): coefficient of pi in int_0^M 8 m dm = 4 M^2 = A/4
    m = RF.var()
    s_bh = (RF.const(8) * m)                   # dS/dM = 1/T, coefficient of pi
    for mm in (F(1), F(7, 3)):
        integral = 4 * mm * mm                 # antiderivative 4 m^2 vanishing at m = 0
        GA.check("S_BH = int dM/T = 4 pi M^2 = A/4",
                 (RF.const(4) * m * m).deriv().eqrf(s_bh) and integral == 4 * (2 * mm) ** 2 / 4)       # A = 4 pi (2M)^2
    for copies in (1, 2, 3):
        # copies independent sets each carrying 4 x per unit area: copies * 4 x = 1/4
        x = F(1, 4) / (4 * copies)
        eta = 4 * x
        g_cl = 1 / (4 * eta)                  # Jacobson: G = 1/(4 eta)
        GA.check("G_cl/G = number of independent copies (%d)" % copies, g_cl == copies)
    # the registered value: one set, 16 x = 1, eta = 1/4, G_cl = G
    x = F(1, 16)
    GA.check("single set: eta = 1/4", 4 * x == F(1, 4))
    # with nu kept registered and both sets counted: the hole carries 2 S_BH
    GA.check("both sets at registered nu: entropy per area 1/2", 2 * (4 * x) == F(1, 2))
    return True


def check_two_placements_on_kerr():
    premise("synthesis.kerr-ring-count-misses-area-law")
    premise("synthesis.imported-kerr-surface-gravity-entropy")
    premise("scrambling.epoch-modular-period-two-unknowns-become")
    pi_lo, pi_hi = F(3), F(22, 7)
    out = {}
    for (M, a) in ((500, 300), (500, 480)):
        rho = icbrt(2 * M)
        s = isqrt(M * M - a * a)
        r_plus, r_minus = M + s, M - s
        kappa = F(r_plus - r_minus, 2 * (r_plus ** 2 + a * a))
        GA.check("kappa_+ = sqrt(M^2-a^2)/(2 M r_+)", kappa == F(s, 2 * M * r_plus))
        area = 4 * (r_plus ** 2 + a * a)            # coefficient of pi
        GA.check("A_+ = 8 pi M r_+", area == 8 * M * r_plus)
        eps = F(rho * rho, a * a)
        delta = F(2 * M * rho, a * a)
        GA.check("delta <= 1/4", delta <= F(1, 4))
        eta_k_max = eps * eps / 4 + 5 * delta * delta / 32
        # literal count N = nu V' dt, nu = 1/(16 pi), V' = 4 pi^2 rho^2 (1 - eta_K), dt = 2 pi/kappa
        # N = pi^2 rho^2 (1 - eta_K)/(2 kappa): coefficient of pi^2 per unit (1 - eta_K)
        n_coeff = F(rho * rho) / (2 * kappa)
        # ratio N/(A_+/4) = [pi^2 n_coeff (1 - eta_K)] / [pi area/4] = pi * c * (1 - eta_K)
        c = n_coeff / F(area, 4)
        GA.check("c = rho^2/(2 sqrt(M^2 - a^2))", c == F(rho * rho, 2 * s))
        upper = pi_hi * c
        lower = pi_lo * c * (1 - eta_k_max)
        out[(M, a)] = (lower, upper)
        # (C_loc)(i) at eta = 1/4: horizon entropy / (A_+/4) is exactly one
        eta = 4 * F(1, 16)                          # (C_loc)(i) at the registered value pi nu <s> = 1/16
        GA.check("C_loc horizon count is A_+/4", eta * area == F(area, 4))
    lo, up = out[(500, 300)]
    GA.check("(500,300): literal count below 11/28 of A_+/4", up == F(11, 28) and up < 1)
    lo, up = out[(500, 480)]
    GA.check("(500,480): literal count above A_+/4", lo > 1)
    return True
