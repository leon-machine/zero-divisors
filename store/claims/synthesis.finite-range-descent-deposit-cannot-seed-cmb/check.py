"""synthesis.finite-range-descent-deposit-cannot-seed-cmb: exact checks.

pi is bounded by 3 < pi < 22/7. Record inputs are exact rationals built from decimal strings:
T_0 = 2.7255 K, k_B = 8.617333262e-14 GeV/K, H_0 = 67.4 km/s/Mpc, 1 Mpc = 3.0856775814913673e22 m,
hbar = 6.582119569e-25 GeV s, c = 299792.458 km/s, reduced Planck mass 2.435e18 GeV, g_s(T_0) = 43/11,
A_s >= 2.0e-9 (Planck 2018: 2.100e-9), pivot k_* = 0.05/Mpc, Omega_m = 0.315, Omega_r = 9.2e-5
(H_0, Omega_m, A_s, the pivot, T_0 and Omega_r from synthesis.imported-planck-2018-lcdm-parameters; the
1 MeV reheating floor from synthesis.imported-bbn-reheating-temperature-floor; the passive reading's superhorizon
conservation from synthesis.imported-superhorizon-zeta-conservation).
"""
from fractions import Fraction as F
import GA
from GA import RF
from tp_premise import premise

PI_LO, PI_HI = F(3), F(22, 7)
T0 = F("2.7255") * F("8.617333262e-14")                          # GeV
H0 = F("67.4") * 1000 / F("3.0856775814913673e22") * F("6.582119569e-25")   # GeV
MP = F("2.435e18")
GS0 = F(43, 11)
KAPPA = F("0.05") * F("299792.458") / F("67.4")                  # k_*/(a_0 H_0)
AS_LO = F("2.0e-9")


def rho6_lo(Td, g):
    """lower bound on (a_d H_d / a_0 H_0)^6, H_d = pi sqrt(g/90) T_d^2 / M_P, a_d/a_0 = (T_0/T_d)(g_s0/g)^(1/3)"""
    return (T0 / Td) ** 6 * (GS0 / g) ** 2 * (PI_LO ** 2 * g / 90) ** 3 * Td ** 12 / (MP ** 6 * H0 ** 6)


def check_amplitude_bound_constants():
    premise("synthesis.frozen-phase-spectrum-not-red")
    # Delta^2 = k^3 P / (2 pi^2); P(k) <= int |C| d^3r.
    # compact support: int |C| <= C(0) (4 pi/3) R^3, so Delta^2 <= C(0) (kR)^3 (4 pi/3)/(2 pi^2) = (2/(3 pi)) C(0) (kR)^3
    # store c pi^n as (c, n): (4/3, 1) / (2, 2) = (2/3, -1)
    num, den = (F(4, 3), 1), (F(2), 2)
    GA.check("(4 pi/3)/(2 pi^2) = (2/3) pi^-1", (num[0] / den[0], num[1] - den[1]) == (F(2, 3), -1))
    # exponential clustering |C| <= C(0) e^{-r/xi}: int_0^oo r^2 e^{-r/xi} dr = 2 xi^3, via the antiderivative
    # -xi (r^2 + 2 r xi + 2 xi^2) e^{-r/xi}; d/dr of it is [-xi (2r + 2 xi) + (r^2 + 2 r xi + 2 xi^2)] e^{-r/xi}
    r = RF.var()
    for xi in (F(1), F(3, 2), F(5, 7)):
        X = RF.const(xi)
        poly = r * r + RF.const(2) * r * X + RF.const(2) * X * X
        deriv = RF.const(-1) * X * (RF.const(2) * r + RF.const(2) * X) + poly
        GA.check("antiderivative identity at xi = %s" % xi, deriv.eqrf(r * r))
        GA.check("value at r = 0 gives 2 xi^3", xi * poly.eval(F(0)) == 2 * xi ** 3)
    # so int |C| d^3r <= C(0) 4 pi 2 xi^3 = 8 pi C(0) xi^3 and Delta^2 <= (8 pi)/(2 pi^2) C(0)(k xi)^3 = (4/pi) C(0)(k xi)^3
    GA.check("(8 pi)/(2 pi^2) = 4 pi^-1", (F(8) / F(2), 1 - 2) == (F(4), -1))
    # Cauchy-Schwarz for a covariance: the Gram matrix [[C0, C], [C, C0]] is positive semidefinite iff |C| <= C0
    for C0, C in ((F(1), F(1, 2)), (F(2), F(-2)), (F(1), F(-1, 3))):
        GA.check("PSD 2x2 gives |C| <= C0", C0 * C0 - C * C >= 0 and abs(C) <= C0)
    GA.check("control: |C| > C0 is not PSD", F(1) * F(1) - F(3, 2) * F(3, 2) < 0)
    return True


def check_descent_hubble_ratio_and_pivot():
    premise("synthesis.frozen-phase-spectrum-not-red")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    premise("synthesis.imported-bbn-reheating-temperature-floor")
    # rho(T_d) = a_d H_d/(a_0 H_0); lower bounds at T_d = 1 MeV (g = 10.75) and 1e12 GeV (g = 106.75)
    r6_mev = rho6_lo(F(1, 1000), F(1075, 100))
    r6_hi = rho6_lo(F(10) ** 12, F(10675, 100))
    GA.check("rho(1 MeV) > 4.96e7", r6_mev > (F(496, 10) * F(10) ** 6) ** 6)
    GA.check("rho(1e12 GeV) > 7.27e22", r6_hi > (F(727, 100) * F(10) ** 22) ** 6)
    # upper brackets with pi < 22/7 (rho is proportional to pi)
    GA.check("rho(1 MeV) < 5.21e7", r6_mev * (PI_HI / PI_LO) ** 6 < (F(521, 10) * F(10) ** 6) ** 6)
    GA.check("rho(1e12 GeV) < 7.63e22", r6_hi * (PI_HI / PI_LO) ** 6 < (F(763, 100) * F(10) ** 22) ** 6)
    GA.check("kappa = k_*/(a_0 H_0) = 149896229/674000", KAPPA == F(149896229, 674000) and F(222) < KAPPA < F(223))
    # the pivot is outside the descent's Hubble length by rho/kappa: > 2.2e5 at 1 MeV, > 3.2e20 at 1e12 GeV
    GA.check("pivot outside at 1 MeV by > 2.2e5", r6_mev > (F(22, 10) * 10 ** 5 * KAPPA) ** 6)
    GA.check("pivot outside at 1e12 GeV by > 3.2e20", r6_hi > (F(32, 10) * 10 ** 20 * KAPPA) ** 6)
    return True


def check_correlation_range_needed():
    premise("synthesis.frozen-phase-spectrum-not-red")
    premise("synthesis.quadratic-flows-cannot-thermalise-descent")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    premise("synthesis.imported-superhorizon-zeta-conservation")
    premise("synthesis.imported-bbn-reheating-temperature-floor")
    # Delta^2(k_*) >= A_s and Delta^2 <= (2/(3 pi)) sigma^2 (k_* R)^3 with R = K/(a_d H_d), k_* R = K kappa/rho:
    # K^3 >= (3 pi/2) A_s rho^3 / (sigma^2 kappa^3).  With sigma^2 <= 1: K^6 >= ((3 pi/2) A_s)^2 rho^6 / kappa^6.
    def K6_lo(r6):
        return (F(3, 2) * PI_LO * AS_LO) ** 2 * r6 / KAPPA ** 6
    k6_mev = K6_lo(rho6_lo(F(1, 1000), F(1075, 100)))
    k6_hi = K6_lo(rho6_lo(F(10) ** 12, F(10675, 100)))
    GA.check("K > 460 at T_d = 1 MeV", k6_mev > F(460) ** 6)
    GA.check("K > 6.8e17 at T_d = 1e12 GeV", k6_hi > (F(68, 10) * F(10) ** 17) ** 6)
    GA.check("and K < 500 at 1 MeV with pi < 22/7", k6_mev * (PI_HI / PI_LO) ** 2 < F(500) ** 6)
    # exponential clustering version: Delta^2 <= (4/pi) sigma^2 (k xi)^3, xi = K'/(a_d H_d):
    # K'^6 >= ((pi/4) A_s)^2 rho^6/kappa^6 > (3/4 A_s)^2 rho^6/kappa^6
    k6e = (F(3, 4) * AS_LO) ** 2 * rho6_lo(F(1, 1000), F(1075, 100)) / KAPPA ** 6
    GA.check("clustering length > 250 Hubble lengths at 1 MeV", k6e > F(250) ** 6)
    return True


def check_no_horizon_exit_after_descent():
    premise("synthesis.de-sitter-temperature-frozen-point-norm")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    # adot^2 / H_0^2 = f(a) = Or/a^2 + Om/a + OL a^2, a_0 = 1. f'(a) = -2 Or/a^3 - Om/a^2 + 2 OL a,
    # f''(a) = 6 Or/a^4 + 2 Om/a^3 + 2 OL > 0 (convex).
    Om, Or = F("0.315"), F("9.2e-5")
    OL = 1 - Om - Or
    a = RF.var()
    f = RF.const(Or) / (a * a) + RF.const(Om) / a + RF.const(OL) * a * a
    fp = f.deriv()
    GA.check("f' formula", fp.eqrf(RF.const(-2 * Or) / (a * a * a) - RF.const(Om) / (a * a) + RF.const(2 * OL) * a))
    # f' < 0 on (0, 1/2]: g(a) = a^3 f'(a) = -2 Or - Om a + 2 OL a^4 is convex (g'' = 24 OL a^2 >= 0), so on
    # [0, 1/2] it is at most max(g(0), g(1/2)), and both are negative
    g = lambda x: -2 * Or - Om * x + 2 * OL * x ** 4
    GA.check("g(0) < 0 and g(1/2) < 0", g(F(0)) < 0 and g(F(1, 2)) < 0)
    GA.check("record inputs pinned: g(1/2) = -2 Or - Om/2 + OL/8 = -144141/2000000",
             g(F(1, 2)) == F(-144141, 2000000) and f.eval(F(1, 2)) == F(160319, 200000))
    GA.check("g convex: g'' = 24 OL a^2 >= 0", 24 * OL > 0)
    # convexity: on [1/2, 1], f <= max(f(1/2), f(1)) = f(1) = 1
    GA.check("f(1) = 1", f.eval(F(1)) == 1)
    GA.check("f(1/2) = 4 Or + 2 Om + OL/4 < 1", f.eval(F(1, 2)) == 4 * Or + 2 * Om + OL / 4 and f.eval(F(1, 2)) < 1)
    GA.check("f'' > 0 at sample points", all(fp.deriv().eval(x) > 0 for x in (F(1, 2), F(3, 4), F(1))))
    # so adot decreases from the descent to a = 1/2 and adot <= H_0 on [1/2, 1]; the pivot k_* = kappa a_0 H_0 with
    # kappa > 222 > 1 enters while adot decreases and never leaves: no mode at or below the pivot scale exits after
    # the descent. In the frozen phase proper (de Sitter at H_Lambda = H_0 sqrt(OL)) modes exit only when
    # k = a H_Lambda, i.e. at a = kappa/sqrt(OL) > 222: in the future.
    GA.check("frozen phase: pivot exits only at a in (268, 269)",
             F(268) ** 2 < KAPPA ** 2 / OL < F(269) ** 2)
    return True
