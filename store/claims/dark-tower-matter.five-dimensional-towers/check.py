"""dark-tower-matter.five-dimensional-towers: exact checks of (i) and (ii).

Exact rationals; cube roots compared through cubes; pi bracketed by Machin's formula.
Inputs (the paper's K5 and K7): the fifth direction one cell radius deep and co-expanding (premise R3),
d_b = 0.98 m; T_0 = 2.7255 K, k_B = 8.617333e-5 eV/K, hbar c = 1.97327e-7 eV m; g_s = 3.91 today,
61.75 at a GeV, 106.75 early.
(i) L T today = d_b k_B T_0/(hbar c) lies in (1150, 1180) ("1170"); with L T scaling as g_s^(-1/3)
(co-expanding L, entropy conservation) it is in (385, 395) at g_s = 106.75 ("390"); both exceed 120 pi,
so the Kaluza-Klein spacing pi/L stays below T/120 throughout.
(ii) The K7 estimate: below the quark mass only the gluons run (b_4 = 11); at the five-dimensional
strong-coupling limit for a 1 GeV quark, g_5^2 = 8 pi^3 GeV^-1, and L (in GeV^-1) read at the
freeze-out temperature T = m/20, m = 0.938 GeV (L T scaled to g_s = 61.75), the four-dimensional
coupling g_4^2 = g_5^2/L gives Lambda/(pi/L) below exp(-8 pi^2/(b_4 g_4^2)) = exp(-L/(11 pi)), with
exponent in (280, 290): below e^-250.
(iii)-(vi) rest on numerical Kaluza-Klein sums and on the supplementary D5C computations and are not
checked here; the gauge algebra and content of the premises enter only through b_4 (pure SU(3) glue).
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
D_B = F(98, 100)
T0, KB, HBARC = F(27255, 10 ** 4), F(8617333, 10 ** 11), F(197327, 10 ** 12)
M_Q = F(938, 1000)
G_S_TODAY, G_S_EARLY = F(391, 100), F(10675, 100)   # entropy degrees of freedom today and early
# The proposition's stated brackets for L T (today, early) and its Kaluza-Klein margin (L T > 120 pi).
STATED_TODAY, STATED_EARLY, STATED_KK = (F(1150), F(1180)), (F(385), F(395)), 120


def floor_cbrt(x):
    """The integer part of the cube root of a nonnegative rational."""
    return iroot_bracket(x, 3, 1)[0]


def lt_today():
    return D_B * KB * T0 / HBARC


def check_five_dimensional_at_every_epoch():
    premise("dark-matter.r3-one-cell-per-unshared-direction")
    lt0 = lt_today()
    early3 = lt0 ** 3 * G_S_TODAY / G_S_EARLY
    # By hand from the inputs: L T today = 0.98 * 8.617333e-5 * 2.7255 / 1.97327e-7 = 1166.43;
    # early, times (3.91/106.75)^(1/3) = 0.3321: 387.4 = 123.3 pi. Integer parts pinned exactly.
    ok = int(lt0) == 1166 and floor_cbrt(early3) == 387
    ok = ok and floor_cbrt(early3 / PI_HI ** 3) == 123 and floor_cbrt(early3 / PI_LO ** 3) == 123
    ok = ok and STATED_TODAY[0] < lt0 < STATED_TODAY[1]
    ok = ok and STATED_EARLY[0] ** 3 < early3 < STATED_EARLY[1] ** 3
    ok = ok and early3 > (STATED_KK * PI_HI) ** 3 and lt0 > STATED_KK * PI_HI
    GA.check("prop:fiveD(i): L T from 385-395 (g_s = 106.75) to 1150-1180 today, always above 120 pi", ok)
    return ok


def check_confinement_scale_negligible():
    premise("dark-matter.r3-one-cell-per-unshared-direction")
    premise("dark-tower-matter.gauge-algebras")
    lt0 = lt_today()
    # L in GeV^-1 at T = m/20: L^3 = (L T)^3 / T^3 with L T scaled to g_s = 61.75
    L3 = lt0 ** 3 * F(391, 100) / F(6175, 100) / (M_Q / 20) ** 3
    b4 = 11
    # exponent 8 pi^2 L/(b4 g5^2) with g5^2 = 8 pi^3 GeV^-1 (a 1 GeV quark): = L/(b4 pi); compare cubes
    e3_lo = L3 / (b4 * PI_HI) ** 3
    e3_hi = L3 / (b4 * PI_LO) ** 3
    ok = F(280) ** 3 < e3_lo and e3_hi < F(290) ** 3 and e3_lo > F(250) ** 3
    GA.check("prop:fiveD(ii): the four-dimensional confinement scale is below pi/L by exp(-(280 to 290)), below "
             "e^-250", ok)
    return ok
