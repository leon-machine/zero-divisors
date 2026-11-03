"""dark-matter.mirror-share-one-how-fragile: exact checks.

All numbers are exact rationals; irrational quantities are bracketed: pi by Machin's formula with
alternating-series bounds, e^x by its Taylor series with a remainder bound, and powers
(M/Lambda)^(a/b) by comparing integer powers (x^(a/b) in (lo, hi) iff lo^b < x^a < hi^b).
(i) With Lambda_2 = Lambda_6 and c_2 = c_6 (premise: the mirror theorem), f_2 is the ratio of mean mass
per baryon: ours 0.75 m_p + 0.25 m_He/4 in (936.5, 937.0) MeV, a helium mirror m_He/4 in
(931.8, 931.9), ratio in (0.994, 0.996), so 1 on the proton-only branch and 0.995 on the burning one.
(ii) One loop: with ln(M/Lambda) = 2 pi/(b alpha(M)) and a common alpha(M), b_6 L_6 = b_2 L_2, so
ln(Lambda_2/Lambda_6) = Delta b/(b_6 + Delta b) ln(M/Lambda_6) when the content differs by Delta b
throughout (checked as exact algebra at sample values); and the bound's inequality chain
b_6 L >= Delta b (L0 - L) => L >= Delta b L0/(b_6 + Delta b) on a 41-point rational grid with equality at
the bound. One Dirac flavour (Delta b = 2/3) at Lambda_6 = 0.3 GeV over the ceiling range
3.5e11 to 6e14 GeV (premise: the ceiling's value): factor in (4.88, 4.90) at the bottom with b_6 = 11
(below 5.364), (21.3, 21.5) at the top with b_6 = 7, and above 5.364 at the other two corners.
A coupling departure delta moves Lambda_2/Lambda_6 by e^(-2 pi delta/b): e^(2 pi/7) in (2.45, 2.46),
and at b = 7 the share stays within ten percent of one for delta = +-0.106 but not for 0.107.
(iii) is a scope statement and is not computed.
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
M_P, M_HE = F(938272, 1000), F(3727379, 1000)
LAM6 = F(3, 10)
L_SAMPLES = [F(35), F(28), F(101, 3)]
# sample (b_6, Delta b) pairs for the one-loop relation, and for the inequality chain
ONE_LOOP_CASES = ((F(11), F(2, 3)), (F(7), F(2, 3)), (F(9), F(1)), (F(11), F(1)))
CHAIN_CASES = ((11, 1), (9, 1), (7, 2), (9, 2), (11, F(2, 3)), (7, F(2, 3)))
# sample L0 = ln(M/Lambda_6) for the chain, and the number of steps of its rational grid on [0, L0]
CHAIN_L0 = F(35)
GRID_STEPS = 40


def frac_power_between(x, a, b, lo, hi):
    """lo < x^(a/b) < hi for positive rationals, by integer powers."""
    return lo ** b < x ** a < hi ** b


def check_mean_mass_per_baryon_share():
    premise("dark-matter.mirror-tower-copy-one")
    ours = F(3, 4) * M_P + F(1, 4) * M_HE / 4
    helium = M_HE / 4
    ratio = helium / ours
    ok = F(9365, 10) < ours < F(937) and F(9318, 10) < helium < F(9319, 10)
    ok = ok and F(994, 1000) < ratio < F(996, 1000) and F(5, 1000) < 1 - ratio < F(6, 1000)
    GA.check("prop:massbound(i): mean mass per baryon 936.7 against 931.8 MeV; f_2 = 0.995 in the completion "
             "limit, a half-percent one-sided systematic", ok)
    return ok


def check_one_loop_bound_and_chain():
    ok = True
    for b6, db in ONE_LOOP_CASES:
        for L6 in L_SAMPLES:
            inv_alpha_over_2pi = b6 * L6        # 2 pi/alpha = b6 L6
            L2 = inv_alpha_over_2pi / (b6 + db)  # mirror with b2 = b6 + db over the whole range
            ok = ok and L6 - L2 == db / (b6 + db) * L6
    L0 = CHAIN_L0
    for b6, db in CHAIN_CASES:
        Ls = db * L0 / (b6 + db)
        ok = ok and b6 * Ls == db * (L0 - Ls)
        for k in range(GRID_STEPS + 1):
            L = L0 * k / GRID_STEPS
            if b6 * L >= db * (L0 - L):
                ok = ok and L >= Ls
    ok = ok and F(1) * L0 / 12 == L0 / (11 + 1) and F(2, 3) * L0 / (11 + F(2, 3)) == 2 * L0 / 35 \
        and F(2, 3) * L0 / (7 + F(2, 3)) == 2 * L0 / 23
    GA.check("prop:massbound(ii): ln(Lambda2/Lambda6) = Db/(b6 + Db) ln(M/Lambda6) at one loop; the chain holds on "
             "the grid; L0/12, 2 L0/35, 2 L0/23", ok)
    return ok


def check_one_flavour_factors_over_the_ceiling_range():
    premise("dark-matter.ceiling-valued-inherited-success")
    premise("dark-matter.mirror-tower-copy-one")
    top, bottom = F(6) * 10 ** 14 / LAM6, F(35) * 10 ** 10 / LAM6
    obs = F(5364, 1000)
    ok = frac_power_between(bottom, 2, 35, F(488, 100), F(490, 100))
    ok = ok and frac_power_between(top, 2, 23, F(213, 10), F(215, 10))
    ok = ok and frac_power_between(top, 2, 35, F(74, 10), F(76, 10))
    ok = ok and frac_power_between(bottom, 2, 23, F(11), F(115, 10))
    # past 5.364 except at the bottom on the b6 = 11 branch
    ok = ok and bottom ** 2 < obs ** 35 and top ** 2 > obs ** 35 and bottom ** 2 > obs ** 23
    GA.check("prop:massbound(ii): one Dirac flavour moves the share by 4.89 (bottom, b6 = 11) to 21.4 (top, "
             "b6 = 7), past 5.364 except at the bottom on the b6 = 11 branch", ok)
    return ok


def check_coupling_departure_window():
    lo, hi = exp_bracket(2 * PI_LO / 7)
    lo2, hi2 = exp_bracket(2 * PI_HI / 7)
    ok = F(245, 100) < lo and hi2 < F(246, 100)
    up = exp_bracket(2 * PI_HI * F(106, 1000) / 7)[1]
    down = exp_bracket(-2 * PI_HI * F(106, 1000) / 7)[0]
    beyond = exp_bracket(2 * PI_LO * F(107, 1000) / 7)[0]
    ok = ok and up < F(11, 10) and down > F(9, 10) and beyond > F(11, 10)
    GA.check("prop:massbound(ii): e^(2 pi/7) in (2.45, 2.46); within ten percent for |delta| <= 0.106, not at 0.107",
             ok)
    return ok
