"""dark-matter.seeding-gravity-floor-dark-towers-temperature: exact checks.

Exact rationals throughout; pi is bracketed by Machin's formula with alternating-series bounds and
never approximated. Square roots are avoided by squaring: kappa_s^2 = (pi^2 g*/90)(2 pi^2/45)^2 g_s^2
is a polynomial in pi, and xi^8 = (4 Y g*/g_d)^2 with Y kappa_s rational.
- Boltzmann step: with Gamma = c T^8/M^4 (premise: the imported graviton rate), H = h T^2/M and
  s = sigma T^3 for arbitrary positive h, sigma (h sigma = kappa_s), Gamma/(H T s) = c T^2/(kappa_s M^3)
  identically (checked at sample T, h, sigma); the yield from T_desc down to 0 is the integral
  c T_desc^3/(3 kappa_s M^3): the antiderivative T^3/3 is checked by exact differentiation, and lies
  strictly between the lower and upper Riemann sums with 200 steps (the sums within two percent).
  Gravitational production is the only source (premise: superselection leaves only the metric).
- kappa_s in (145.25, 145.30) at g* = g_s = 100 ("145.3"); 1.66 = sqrt(8 pi) sqrt(pi^2/90) to three
  figures (the two Planck-mass conventions give one rate).
- the floor formula: xi^4 = 4 Y g*/g_d, and at c = 1, g_d = 16, T_desc = 6e14 GeV, M_P = 2.435e18 GeV,
  xi in (9.6, 9.7) x 10^-4; the scaling xi^4 proportional to c (16/g_d) (T/6e14)^3 holds exactly at
  sample inputs (kappa cancels).
- the ceiling range (premise: 3.5e11 to 6e14 GeV): (3.5e11/6e14)^(3/4) lies in (3.745, 3.755) x 10^-3,
  the stated 3.75 x 10^-3, about 4 x 10^-3 at one figure.
- later evolution: with g_d T_d^3 a^3 and g_s T^3 a^3 separately conserved, (T_d/T)^3 changes by
  (g_d_seed/g_d)(g_s/g_s_seed), checked at sample histories.
EXPORTS: kappa2_bracket(), xi8_bracket(c, gd, T), y_kappa(c, T), MPRED, TCEIL, GSTAR.
"""
from fractions import Fraction as F
import GA
from series import root_rounds_to, rounds_to
from tp_premise import premise

# --- exact bracketing helpers (rationals only) ---
def _arctan_inv(k, terms):
    """Partial sums of arctan(1/k) (alternating series): returns (lo, hi)."""
    s, lo, hi = F(0), None, None
    for j in range(terms):
        t = F((-1) ** j, (2 * j + 1) * k ** (2 * j + 1))
        s += t
        if j % 2 == 0:
            hi = s
        else:
            lo = s
    return lo, hi


def pi_bracket(terms=24):
    """Machin: pi = 16 arctan(1/5) - 4 arctan(1/239), with alternating-series brackets."""
    a_lo, a_hi = _arctan_inv(5, terms)
    b_lo, b_hi = _arctan_inv(239, terms)
    return 16 * a_lo - 4 * b_hi, 16 * a_hi - 4 * b_lo


def iroot_bracket(x, k, denom):
    """(lo, hi), multiples of 1/denom, with lo^k <= x < hi^k (integer bisection)."""
    n = x * denom ** k
    t = n.numerator // n.denominator
    lo, hi = 0, 1
    while hi ** k <= t:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** k <= t:
            lo = mid
        else:
            hi = mid
    return F(lo, denom), F(lo + 1, denom)


def exp_bracket(x, terms=40):
    """(lo, hi) with lo <= e^x <= hi for rational x, by the Taylor series with remainder."""
    if x < 0:
        lo, hi = exp_bracket(-x, terms)
        return 1 / hi, 1 / lo
    s, t = F(1), F(1)
    for j in range(1, terms + 1):
        t = t * x / j
        s += t
    bound = 3 ** (x.numerator // x.denominator + 1)
    return s, s + t * x / (terms + 1) * bound


PI_LO, PI_HI = pi_bracket()
MPRED = F(2435, 1000) * 10 ** 18
TCEIL = F(6) * 10 ** 14
GSTAR = F(100)
H_SAMPLES = [(F(3), F(7, 2)), (F(5, 4), F(11)), (F(9, 2), F(2, 3))]
T_SAMPLES = [F(2), F(7, 5), F(10) ** 3]
HISTORIES = [(F(1, 1000), F(10675, 100), F(100), F(375, 100), F(6175, 100)),
             (F(3, 10 ** 4), F(18), F(100), F(18), F(391, 100))]
# sample (c, g_d, T_desc) points for the scaling of xi^4
SCALING_SAMPLES = ((F(3, 100), F(10675, 100), F(35) * 10 ** 10), (F(10), F(18), F(3) * 10 ** 14),
                   (F(1, 100), F(16), TCEIL))


def kappa2_bracket(gstar=GSTAR, gs=GSTAR):
    k = lambda p: (p ** 2 * gstar / 90) * (2 * p ** 2 / 45) ** 2 * gs ** 2
    return k(PI_LO), k(PI_HI)


def y_kappa(c, T, M=MPRED):
    """Y kappa_s = c T^3/(3 M^3), rational."""
    return c * T ** 3 / (3 * M ** 3)


def xi8_bracket(c, gd, T=TCEIL):
    k_lo, k_hi = kappa2_bracket()
    num = (4 * y_kappa(c, T) * GSTAR / gd) ** 2
    return num / k_hi, num / k_lo


def check_boltzmann_yield():
    premise("dark-matter.imported-massless-graviton-production-rate")
    premise("dark-matter.superselected-hence-dark-exactly-stable")
    ok = True
    c, M = F(3, 50), F(7)
    for h, sigma in H_SAMPLES:
        for T in T_SAMPLES:
            Gamma = c * T ** 8 / M ** 4
            H, s = h * T ** 2 / M, sigma * T ** 3
            ok = ok and Gamma / (H * T * s) == c * T ** 2 / (h * sigma * M ** 3)
    ok = ok and GA.pderiv([F(0), F(0), F(0), F(1, 3)]) == [F(0), F(0), F(1)]
    N = 200
    lower = sum(F(k, N) ** 2 for k in range(N)) / N
    upper = sum(F(k + 1, N) ** 2 for k in range(N)) / N
    ok = ok and lower < F(1, 3) < upper and upper / lower < F(102, 100)
    GA.check("prop:gravseed: dY/dT = -c T^2/(kappa_s M^3) from Gamma/(H T s); Y = c T^3/(3 kappa_s M^3), between "
             "the 200-step Riemann sums", ok)
    return ok


def check_kappa_and_convention():
    k_lo, k_hi = kappa2_bracket()
    # by hand: kappa_s = (2 pi^2/45) 100 sqrt(100 pi^2/90) = 145.25993, in the quoted (145.25, 145.30)
    ok = all(root_rounds_to(k, 1452599, -4) and root_rounds_to(k, 1453, -1) for k in (k_lo, k_hi))
    # by hand: sqrt(8 pi) sqrt(pi^2/90) = sqrt(8 pi^3/90) = 1.6601547, the quoted 1.66
    ok = ok and all(root_rounds_to(8 * p * p ** 2 / 90, 16601547, -7) and root_rounds_to(8 * p * p ** 2 / 90, 166, -2)
                    for p in (PI_LO, PI_HI))
    GA.check("prop:gravseed: kappa_s in (145.25, 145.30) at g* = g_s = 100; sqrt(8 pi) sqrt(pi^2/90) in (1.660, 1.661)",
             ok)
    return ok


def check_floor_prefactor_and_scaling():
    premise("dark-matter.imported-massless-graviton-production-rate")
    lo, hi = xi8_bracket(F(1), F(16))
    # by hand: xi^4 = 4 (6e14)^3 100/(3 (2.435e18)^3 16 x 145.25993), xi = 9.625149e-4, in the quoted
    # (9.6, 9.7)e-4
    ok = all(root_rounds_to(x, 9625149, -10, 8) and root_rounds_to(x, 96, -5, 8) for x in (lo, hi))
    base = 4 * y_kappa(F(1), TCEIL) * GSTAR / 16
    for c, gd, T in SCALING_SAMPLES:
        val = 4 * y_kappa(c, T) * GSTAR / gd
        ok = ok and val / base == c * (16 / gd) * (T / TCEIL) ** 3
    GA.check("prop:gravseed: xi_floor = 9.6e-4 c^(1/4) (16/g_d)^(1/4) (T/6e14)^(3/4): prefactor in (9.6, 9.7)e-4 "
             "and the scaling exact", ok)
    return ok


def check_ceiling_range_factor():
    premise("dark-matter.ceiling-valued-inherited-success")
    r = F(35) * 10 ** 10 / TCEIL
    ok = F(3745, 10 ** 6) ** 4 < r ** 3 < F(3755, 10 ** 6) ** 4
    ok = ok and F(35, 10 ** 4) ** 4 < r ** 3 < F(45, 10 ** 4) ** 4
    GA.check("prop:gravseed: (3.5e11/6e14)^(3/4) in (3.745, 3.755)e-3: 3.75e-3, about 4e-3", ok)
    return ok


def check_later_evolution_of_the_ratio():
    ok = True
    for xi0, gd0, gs0, gd1, gs1 in HISTORIES:
        T0, a0, a1 = F(1), F(1), F(37, 3)
        Td0 = xi0 * T0
        T1_cubed = gs0 * T0 ** 3 * a0 ** 3 / (gs1 * a1 ** 3)
        Td1_cubed = gd0 * Td0 ** 3 * a0 ** 3 / (gd1 * a1 ** 3)
        ok = ok and Td1_cubed / T1_cubed == xi0 ** 3 * (gd0 / gd1) * (gs1 / gs0)
    GA.check("prop:gravseed: separate entropy conservation evolves (T_d/T)^3 by (g_d_seed/g_d)(g_s/g_s_seed)", ok)
    return ok


EXPORTS = {"kappa2_bracket": kappa2_bracket, "xi8_bracket": xi8_bracket, "y_kappa": y_kappa,
           "MPRED": MPRED, "TCEIL": TCEIL, "GSTAR": GSTAR, "PI": (PI_LO, PI_HI)}
