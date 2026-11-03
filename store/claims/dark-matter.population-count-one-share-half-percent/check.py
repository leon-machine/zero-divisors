"""dark-matter.population-count-one-share-half-percent: exact checks of the computable part.

(i) The asymmetric dark matter: from the census rule (P3 representatives on the grid p + q <= 6), the
towers that are oriented (dimension 0 mod 4, the flag-bit criterion of which-towers-can-carry-arrow)
and causal (min(p,q) = 1) are r = 6, 2; removing this tower leaves the mirror alone, the sterile
r = 0, 4 and the odd towers excluded. Its share f_2 = 1 is the mirror theorem's (P4 and the copy: a
premise, not recomputed); on the burning branch the mean mass per baryon m_He/4 against ours gives a
factor in (0.994, 0.996), within half a percent (premise: mirror-share-one-how-fragile(i)).
The observed ratio: 0.1200/0.02237 in (5.36, 5.37), rounding to 5.364; its uncertainty, 5.364 times the
quadrature relative error of (0.1200 +- 0.0012, 0.02237 +- 0.00015), in (0.064, 0.066) ("0.065").
(ii) The remainder (5.364 - 1) Omega_b h^2 = 0.0976 to rounding, equal to 0.1200 - 0.02237 to 1e-5,
with uncertainty 4.364 x 0.02237 times the relative error in (0.00115, 0.0012) ("0.0012").
(iii) The unit-ball expression 2 x 4/3 + 2 x 8/(3 pi), with pi bracketed by Machin's formula, lies in
(4.364, 4.365): it returns the remainder 4.364. Nothing else in (iii) is computable.
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


OC, DOC = F(1200, 10 ** 4), F(12, 10 ** 4)
OB, DOB = F(2237, 10 ** 5), F(15, 10 ** 5)
M_P, M_HE = F(938272, 1000), F(3727379, 1000)
SIGS = [(p, q) for p in range(7) for q in range(7) if 1 <= p + q <= 6]


def p3(r):
    if r % 2 == 0:
        return sorted(s for s in SIGS if sum(s) == 4 and (s[0] - s[1]) % 8 == r)
    three = [s for s in SIGS if sum(s) == 3 and (s[0] - s[1]) % 8 == r]
    if any(min(s) == 1 for s in three):
        return sorted(three)
    return sorted(s for s in SIGS if sum(s) == 5 and (s[0] - s[1]) % 8 == r)


def check_asymmetric_share_is_the_mirror_alone():
    premise("dark-matter.which-towers-can-carry-arrow")
    premise("dark-matter.p3-nearest-dimension-representatives")
    premise("dark-matter.mirror-share-one-how-fragile")
    reps = {r: p3(r) for r in range(8)}
    carriers = sorted(r for r in range(8) if all((p + q) % 4 == 0 for p, q in reps[r])
                      and any(min(p, q) == 1 for p, q in reps[r]))
    ok = carriers == [2, 6] and [r for r in carriers if r != 6] == [2]
    ok = ok and sorted(r for r in range(8) if not any(min(p, q) == 1 for p, q in reps[r])) == [0, 4]
    ratio = (M_HE / 4) / (F(3, 4) * M_P + F(1, 4) * M_HE / 4)
    ok = ok and F(994, 1000) < ratio < F(996, 1000)
    GA.check("prop:count(i): only the mirror carries asymmetric dark matter; f_2 = 1, to half a percent on the "
             "burning branch", ok)
    return ok


def check_observed_ratio_and_uncertainty():
    obs = F(5364, 1000)
    rel2 = (DOC / OC) ** 2 + (DOB / OB) ** 2
    # by hand: 0.1200/0.02237 = 5.364327..., which rounds to the quoted 5.364
    ok = rounds_to(OC / OB, 5364327, -6) and rounds_to(OC / OB, 5364, -3)
    # by hand: 5.364 x sqrt(0.01^2 + (0.00015/0.02237)^2) = 0.0645828, which rounds to the quoted 0.065
    ok = ok and root_rounds_to(obs ** 2 * rel2, 645828, -7)
    GA.check("prop:count(i): Omega_c/Omega_b = 5.364 +- 0.065", ok)
    return ok


def check_remainder():
    obs = F(5364, 1000)
    rel2 = (DOC / OC) ** 2 + (DOB / OB) ** 2
    rem = (obs - 1) * OB
    ok = F(9755, 10 ** 5) < rem < F(9765, 10 ** 5) and abs(rem - (OC - OB)) < F(1, 10 ** 5)
    ok = ok and F(115, 10 ** 5) ** 2 < rem ** 2 * rel2 < F(12, 10 ** 4) ** 2
    GA.check("prop:count(ii): the remainder 4.364 Omega_b h^2 = 0.0976 +- 0.0012", ok)
    return ok


def check_unit_ball_expression_returns_the_remainder():
    lo = 2 * F(4, 3) + 2 * F(8, 3) / PI_HI
    hi = 2 * F(4, 3) + 2 * F(8, 3) / PI_LO
    ok = F(4364, 1000) < lo and hi < F(4365, 1000)
    GA.check("prop:count(iii): 2 x 4/3 + 2 x 8/(3 pi) lies in (4.364, 4.365)", ok)
    return ok
