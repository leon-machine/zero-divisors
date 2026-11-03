"""dark-matter.stored-asymmetry-charge-not-number: exact checks of the arithmetic.

Inputs and brackets come from the coefficients proposition's export cosmo(): eta = 2.74e-8 x 0.02237,
n_B/s = 0.1413 eta, the mirror floor's xi^8 bracket (pi bracketed by Machin's formula, kappa_s^2 a
polynomial in pi), the hot-deposit xi^4 = 4 (n_B/s) g*/g_d (rational), and Delta N_eff coefficient
7.447 = (8/7)(11/4)^(4/3) + 3.044 (exact cube-root bracket). Roots are compared through integer powers.
(i)/(iv) The two readings: the charge reading gives f_2 = Q_2 m/(Q_6 m) = 1 for every xi (Q = eps N,
the same eps and N in both towers, checked at sample xi), the thermal reading f_2 ~ xi^3, at most
0.448^3 in (0.0899, 0.0900) under the cap and below 1e-7 anywhere in [floor, hot deposit]; they differ.
(ii) Origin: the gravitational yield at the ceiling falls short of n_B/s by more than 1e4 (both
countings).
(iii) eta in (6.1, 6.2) x 10^-10; the crossover eta^(1/3) in (8.4, 8.6) x 10^-4 ("8.5e-4"); eta' = eta/xi^3
in (19, 26) at the floor and (0.007, 0.009) at the hot deposit, and eta'/eta = xi^-3 above 1e7
throughout; Delta N_eff = 7.447 xi^4 at least eight orders below the cap 0.3 on the whole interval;
the bottom of the ceiling range lowers the floor by a factor in (3.7, 3.8) x 10^-3 ("four parts in a
thousand").
Not computed: the nucleosynthesis caveat (T14c composition), the boundary-mode count.
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
XI_SAMPLES = [F(3, 10 ** 4), F(1, 10 ** 3), F(4, 10 ** 3), F(448, 1000)]
EPS_N = [(F(6, 10 ** 10), F(10) ** 60), (F(1, 10 ** 9), F(7) * 10 ** 59)]


def cosmo():
    return premise("dark-matter.coefficients-floors-they-give-what-gravity")["cosmo"]()


def check_charge_reading_against_thermal_reading():
    premise("dark-matter.asymmetry-arrow-counted-fifteenth-refutation")
    premise("dark-matter.p1-single-frozen-point")
    k = cosmo()
    ok = True
    for eps, N in EPS_N:
        Q6 = Q2 = eps * N
        for xi in XI_SAMPLES:
            ok = ok and Q2 / Q6 == 1 and xi ** 3 < 1
    ok = ok and F(899, 10 ** 4) < F(448, 1000) ** 3 < F(900, 10 ** 4)
    ok = ok and k["xi_hot4"] ** 3 < F(1, 10 ** 7) ** 4
    GA.check("prop:charge(i, iv): f_2 = 1 for every xi on the charge reading; the thermal reading's xi^3 is at most "
             "0.090 under the cap and below 1e-7 on the interval", ok)
    return ok


def check_origin_gravity_cannot_supply_the_charge():
    premise("dark-matter.coefficients-floors-they-give-what-gravity")
    premise("dark-matter.seeding-gravity-floor-dark-towers-temperature")
    k = cosmo()
    s = k["seeding"]
    k2lo, k2hi = s["kappa2_bracket"]()
    Y2_hi = s["y_kappa"](k["c_hi"], s["TCEIL"]) ** 2 / k2lo
    ok = k["nb_s"] ** 2 > F(10 ** 4) ** 2 * Y2_hi
    ok = ok and F(86, 10 ** 12) < k["nb_s"] < F(87, 10 ** 12)
    GA.check("prop:charge(ii): gravitational production at the ceiling is more than four orders short of n_B/s", ok)
    return ok


def check_eta_prime_and_radiation_over_the_interval():
    premise("dark-matter.coefficients-floors-they-give-what-gravity")
    premise("dark-matter.mirror-tower-copy-one")
    k = cosmo()
    eta = k["eta"]
    # by hand: eta = 2.74e-8 x 0.02237 = 6.12938e-10, in the quoted (6.1, 6.2)e-10
    ok = eta == F(612938, 10 ** 15)
    # crossover eta^(1/3) = 8.494520e-4, the quoted 8.5e-4
    ok = ok and root_rounds_to(eta, 8494520, -10, 3) and root_rounds_to(eta, 85, -5, 3)
    f_lo, f_hi = k["floor8"]
    # eta' = eta/xi^3 at the two ends of the floor (decimal evaluation of the export's brackets):
    # 19.35951 and 25.79277, the quoted 19 to 26
    ok = ok and root_rounds_to(eta ** 8 / f_hi ** 3, 1935951, -5, 8)
    ok = ok and root_rounds_to(eta ** 8 / f_lo ** 3, 2579277, -5, 8)
    h4 = k["xi_hot4"]
    # at the hot deposit eta' = 0.00801638 (the quoted 0.008) and eta'/eta = xi^-3 = 1.307862e7, the
    # smallest over the interval, above the quoted 1e7
    ok = ok and root_rounds_to(eta ** 4 / h4 ** 3, 801638, -8, 4)
    ok = ok and root_rounds_to(1 / h4 ** 3, 1307862, 1, 4)
    # Delta N_eff = 7.447 xi^4 below the cap 0.3 by 1.24130e8 at the hot end (the largest xi of the
    # interval): at least eight orders
    ok = ok and all(rounds_to(F(3, 10) / (m * h4), 124130, 3) for m in k["mirror"])
    GA.check("prop:charge(iii): eta in (6.1, 6.2)e-10, eta^(1/3) in (8.4, 8.6)e-4; eta' from (19, 26) at the floor to "
             "(0.007, 0.009) at the hot deposit; eta'/eta > 1e7; Delta N_eff eight orders below the cap", ok)
    return ok


def check_bottom_of_ceiling_range_factor():
    premise("dark-matter.seeding-gravity-floor-dark-towers-temperature")
    r = F(35) * 10 ** 10 / (F(6) * 10 ** 14)
    ok = F(37, 10 ** 4) ** 4 < r ** 3 < F(38, 10 ** 4) ** 4
    GA.check("prop:charge(iii): the floor at the bottom of the ceiling range is (3.7, 3.8)e-3 of its top value", ok)
    return ok
