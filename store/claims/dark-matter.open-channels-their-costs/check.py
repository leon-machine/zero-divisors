"""dark-matter.open-channels-their-costs: exact checks of the arithmetic.

(11/4)^(1/3) and (61.75/3.91)^(1/3) are bracketed by integer cube roots; fourth roots are compared
through fourth powers. Delta N_eff of a two-polarisation boson at T_gamma is (8/7)(11/4)^(4/3).
Mirror (premise: its relativistic content is a copy of ours, one photon and three neutrinos):
N_eff_tot = (8/7)(11/4)^(4/3) + 3.044 in (7.446, 7.448); the cap 0.3 needs T'/T_gamma below a value in
(0.4480, 0.4481); with the heaviest neutrino non-relativistic the coefficient is 4.403 + 2 in
(6.40, 6.41) and the threshold in (0.464, 0.466) ("0.47"); at the hot-deposit estimate xi^4 = 4 (n_B/s) g*/g_d
(xi = 4.24e-3, the hot end; n_B/s = 0.1413 x 2.74e-8 x 0.02237, g* = 100, g_d = 106.75) the mirror is
more than eight orders below the cap; P2's xi = 1 gives 7.447, excluded.
Five-dimensional towers: (4/7)(11/4)^(4/3) per polarisation in (2.201, 2.203) ("2.2 g"); one species
meets the cap iff T_r/T_gamma is below (0.3/(2.2 g))^(1/4), in (0.51, 0.52) for g = 2 and (0.46, 0.47)
for g = 3. Route (a): (61.75/3.91)^(1/3) in (2.50, 2.52); a two-polarisation species colder by that
factor gives Delta N_eff in (0.10, 0.12); two five-dimensional towers with two polarisations each in
(0.21, 0.23) (under 0.3), with three each in (0.32, 0.34) (over).
Routes (b) and (c) are content derivations and are not computed.
"""
from fractions import Fraction as F
import GA
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
CAP = F(3, 10)
NNU = F(3044, 1000)
# inputs of the hot-deposit estimate xi^4 = 4 (n_B/s) g*/g_d: n_B/s = 0.1413 x 2.74e-8 x 0.02237,
# g* = 100, g_d = 106.75
NB_OVER_S = F(1413, 10 ** 4) * F(274, 10 ** 10) * F(2237, 10 ** 5)
G_STAR, G_D = 100, F(10675, 100)
# route (a) inputs: g_* at a GeV and today, and the resolution of the cube-root bracket of their ratio
G_STAR_GEV, G_STAR_NOW = F(6175, 100), F(391, 100)
ROUTE_A_DENOM = 10 ** 6


def photon_bracket():
    lo, hi = iroot_bracket(F(11, 4), 3, 10 ** 7)
    return F(8, 7) * F(11, 4) * lo, F(8, 7) * F(11, 4) * hi


def check_mirror_radiation_and_threshold():
    premise("dark-matter.mirror-tower-copy-one")
    p_lo, p_hi = photon_bracket()
    m_lo, m_hi = p_lo + NNU, p_hi + NNU
    # by hand: (8/7)(11/4)^(4/3) = 4.4032046..., so N_eff_tot = 7.4472046... (the quoted 7.447)
    ok = all(F(7447204, 10 ** 6) < m < F(7447205, 10 ** 6) for m in (m_lo, m_hi))
    # threshold (0.3/7.4472046)^(1/4) = 0.44800410... (the quoted 0.448)
    ok = ok and F(448004, 10 ** 6) ** 4 < CAP / m_hi and CAP / m_lo < F(448005, 10 ** 6) ** 4
    n_lo, n_hi = p_lo + 2, p_hi + 2
    # heaviest neutrino non-relativistic: 4.4032046 + 2 = 6.4032046..., threshold 0.46524420... ("0.47")
    ok = ok and all(F(6403204, 10 ** 6) < n < F(6403205, 10 ** 6) for n in (n_lo, n_hi))
    ok = ok and F(465244, 10 ** 6) ** 4 < CAP / n_hi and CAP / n_lo < F(465245, 10 ** 6) ** 4
    # the hot-deposit estimate xi^4 = 4 (n_B/s) g*/g_d, the hotter end of the interval;
    # by hand xi = 4.2443...e-3 (the quoted 4.24e-3)
    xi_hot4 = 4 * NB_OVER_S * G_STAR / G_D
    ok = ok and F(4244, 10 ** 6) ** 4 < xi_hot4 < F(4245, 10 ** 6) ** 4
    # eight orders or more below the cap: 7.4472 x 3.2453e-10 / 0.3 = 8.056e-9
    ok = ok and all(F(8055, 10 ** 12) < m * xi_hot4 / CAP < F(8057, 10 ** 12) for m in (m_lo, m_hi))
    ok = ok and m_hi * xi_hot4 * 10 ** 8 < CAP
    # xi = 1 is excluded: 7.4472/0.3 = 24.82, more than 24 times the cap
    ok = ok and all((m / CAP) // 1 == 24 for m in (m_lo, m_hi))
    GA.check("prop:openchannel: N_eff_tot = 7.447, threshold 0.448 (0.47 with one neutrino non-relativistic); the "
             "seeded mirror is eight orders below the cap; xi = 1 is excluded", ok)
    return ok


def check_five_dimensional_thresholds():
    p_lo, p_hi = photon_bracket()
    per_lo, per_hi = p_lo / 2, p_hi / 2
    ok = F(2201, 1000) < per_lo and per_hi < F(2203, 1000)
    for g, lo_t, hi_t in ((2, F(51, 100), F(52, 100)), (3, F(46, 100), F(47, 100))):
        ok = ok and lo_t ** 4 < CAP / (per_hi * g) and CAP / (per_lo * g) < hi_t ** 4
    GA.check("prop:openchannel: 2.2 g (T_r/T_gamma)^4 per species; thresholds 0.51 (g = 2) and 0.46 (g = 3)", ok)
    return ok


def check_route_a_colder_sector():
    p_lo, p_hi = photon_bracket()
    c_lo, c_hi = iroot_bracket(G_STAR_GEV / G_STAR_NOW, 3, ROUTE_A_DENOM)
    # by hand: (61.75/3.91)^(1/3) = 2.50891954... (the quoted 2.51)
    ok = c_lo == F(2508919, 10 ** 6) and c_hi == F(2508920, 10 ** 6)
    one_lo, one_hi = p_lo / c_hi ** 4, p_hi / c_lo ** 4
    # by hand: 4.4032046/2.5089195^4 = 0.11112760... per two-polarisation species (the quoted 0.11)
    ok = ok and all(F(1111270, 10 ** 7) < x < F(1111280, 10 ** 7) for x in (one_lo, one_hi))
    # two towers with two polarisations each: 0.2222552... (the quoted 0.22), under the cap
    ok = ok and all(F(222254, 10 ** 6) < 2 * x < F(222256, 10 ** 6) for x in (one_lo, one_hi))
    ok = ok and 2 * one_hi < CAP
    # two towers with three polarisations each: 0.3333828... (the quoted 0.33), over the cap
    ok = ok and all(F(333381, 10 ** 6) < 3 * x < F(333385, 10 ** 6) for x in (one_lo, one_hi))
    ok = ok and 3 * one_lo > CAP
    GA.check("prop:openchannel(a): (61.75/3.91)^(1/3) in (2.50, 2.52); 0.11 per two-polarisation species; two towers "
             "at 0.22 (two polarisations each, under) and 0.33 (three each, over)", ok)
    return ok


EXPORTS = {"photon_bracket": photon_bracket}
