"""dark-tower-matter.imported-unit-ball-rule: exact checks of the imported shares and fractions.

pi is held as the indeterminate of GA.RF (rational functions in pi), so identities are identities in
Q(pi); decimals use rational pi bounds from Machin's formula (alternating-series brackets).
- Unit-ball volumes from the recursion V_0 = 1, V_1 = 2, V_D = (2 pi/D) V_(D-2): V_2 = pi, V_3 = 4 pi/3,
  V_4 = pi^2/2. Under R1-R3 (premises) a tower of space dimension D has share V_3/V_D (the T14 rule,
  premise dark-matter.unit-ball-rule): 1 (mirror, D = 3), 4/3 (three-dimensional towers, D = 2) and
  8/(3 pi) (five-dimensional towers, D = 4), each odd pair counted twice.
- The total 1 + 2 x 4/3 + 2 x 8/(3 pi) equals (11 pi + 16)/(3 pi) in Q(pi), and lies in (5.364, 5.365).
- As fractions of the dark matter: the mirror 3 pi/(11 pi + 16) in (0.1855, 0.1865) (18.6 percent), each
  three-dimensional tower 4 pi/(11 pi + 16) in (0.2485, 0.2495) (24.9), each five-dimensional tower
  8/(11 pi + 16) in (0.1575, 0.1585) (15.8); the five fractions sum to 1 identically.
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
PI = GA.RF.var()


def c(x):
    return GA.RF.const(F(x))


def ball(D):
    v = {0: c(1), 1: c(2)}
    for d in range(2, D + 1):
        v[d] = c(2) * PI * c(F(1, d)) * v[d - 2]
    return v[D]


def at(rf, p):
    return rf.eval(p)


def check_shares_and_total():
    premise("dark-matter.unit-ball-rule")
    premise("dark-matter.r1-equal-mass-per-quantum")
    premise("dark-matter.r2-one-quantum-per-unit-ball")
    premise("dark-matter.r3-one-cell-per-unshared-direction")
    ok = ball(2).eqrf(PI) and ball(3).eqrf(c(F(4, 3)) * PI) and ball(4).eqrf(c(F(1, 2)) * PI * PI)
    share = {D: ball(3) / ball(D) for D in (2, 3, 4)}
    ok = ok and share[3].eqrf(c(1)) and share[2].eqrf(c(F(4, 3))) and share[4].eqrf(c(F(8, 3)) / PI)
    total = share[3] + c(2) * share[2] + c(2) * share[4]
    ok = ok and total.eqrf((c(11) * PI + c(16)) / (c(3) * PI))
    # total decreases in pi
    ok = ok and F(5364, 1000) < at(total, PI_HI) and at(total, PI_LO) < F(5365, 1000)
    GA.check("imported unit-ball rule: shares 1, 4/3, 8/(3 pi) from V_3/V_D; total (11 pi + 16)/(3 pi) in "
             "(5.364, 5.365)", ok)
    return ok


def check_fractions_of_the_dark_matter():
    premise("dark-matter.unit-ball-rule")
    share = {D: ball(3) / ball(D) for D in (2, 3, 4)}
    total = share[3] + c(2) * share[2] + c(2) * share[4]
    fr = {D: share[D] / total for D in (2, 3, 4)}
    ok = fr[3].eqrf(c(3) * PI / (c(11) * PI + c(16))) and fr[2].eqrf(c(4) * PI / (c(11) * PI + c(16)))
    ok = ok and fr[4].eqrf(c(8) / (c(11) * PI + c(16)))
    ok = ok and (fr[3] + c(2) * fr[2] + c(2) * fr[4]).eqrf(c(1))
    # fr[3], fr[2] increase with pi; fr[4] decreases
    ok = ok and F(1855, 10 ** 4) < at(fr[3], PI_LO) and at(fr[3], PI_HI) < F(1865, 10 ** 4)
    ok = ok and F(2485, 10 ** 4) < at(fr[2], PI_LO) and at(fr[2], PI_HI) < F(2495, 10 ** 4)
    ok = ok and F(1575, 10 ** 4) < at(fr[4], PI_HI) and at(fr[4], PI_LO) < F(1585, 10 ** 4)
    GA.check("imported unit-ball rule: mirror 18.6, each 3D tower 24.9, each 5D tower 15.8 percent; sum 1", ok)
    return ok
