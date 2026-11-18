"""dark-matter.radiation-audit-what-theorem-closes-what: exact checks of the computable part.

- The scale of the problem: one two-polarisation species at T_gamma is Delta N_eff = (8/7)(11/4)^(4/3),
  in (4.40, 4.41) (the photon bracket exported by open-channels-their-costs, an exact cube root); five
  such are in (22, 22.1), and one alone exceeds the cap 0.3 more than tenfold.
- Ground level (type computation exported by type-residue-what-each-tower-can): an intrinsic U(1) exactly
  at the complex members r = 3, 7 (D = C), none at the real mirror r = 2 (D = R, group Z2).
- Odd dimension is vector-like: for (2,1), (1,2), (4,1), (1,4) the pseudoscalar is central and no nonzero
  element anticommutes with every generator (the solution space, computed blade-wise, is zero), so there
  is no chirality grading; in (1,3) the pseudoscalar anticommutes with every generator (control).
- Closing margins on the interval (premises: seeding floor, stored-asymmetry hot deposit; mirror content):
  the hot deposit xi^4 = 4 (n_B/s) g*/g_d (n_B/s = 0.1413 x 2.74e-8 x 0.02237, g* = 100, g_d = 106.75);
  the floor's xi^8 from the seeding export at the mirror's coefficient 1519247 pi^3/82944000 = 0.568
  (the coefficients proposition's value at the derived production coefficients; pi by Machin, both
  ends of its bracket), where the floor is 5.2e-4. Mirror channel (7.447 xi^4): more than 1e11 and
  less than 1e12 below the cap at the floor (5.5e11), and more than 1e8 at the hot deposit; a five-dimensional
  tower with three light polarisations (2.2 x 3 xi^4) more than 1e8 at the hot deposit; a nine-vector
  tower (2.202 x 18 xi^4) at the hot deposit is between 10^7.3 and 10^7.4 below the cap (the one case
  below eight, "7.4").
- Self-interaction: sigma = pi (2 a_0)^2 with a_0 = 0.529e-8 cm (pi by Machin) lies in (3, 4) x 10^-16
  cm^2; per mass (2, 3) x 10^8 cm^2/g for hydrogen (1.67e-24 g) and (5, 10) x 10^7 for helium (6.64e-24 g).
Not computed: Polyakov confinement, the phases of the three-dimensional towers, the Goldstone estimate.
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
CAP = F(3, 10)
A0 = F(529, 10 ** 11)
M_H, M_HE = F(167, 10 ** 26), F(664, 10 ** 26)
NNU = F(3044, 1000)
# inputs of the hot deposit xi^4 = 4 (n_B/s) g*/g_d: n_B/s = 0.1413 x 2.74e-8 x 0.02237, g* = 100,
# g_d = 106.75
NB_OVER_S = F(1413, 10 ** 4) * F(274, 10 ** 10) * F(2237, 10 ** 5)
G_STAR, G_D = 100, F(10675, 100)
# the mirror's production coefficient (the seeding export's input), a copy of the Standard Model's
# content at the derived per-species coefficients: (4 x 5789 + 45 x 16087 + 12 x 4 x 16087) pi^3/82944000
MIRROR_COEFF_OVER_PI3 = F(4 * 5789 + 45 * 16087 + 12 * 4 * 16087, 82944000)
MIRROR_COEFF_LO, MIRROR_COEFF_HI = MIRROR_COEFF_OVER_PI3 * PI_LO ** 3, MIRROR_COEFF_OVER_PI3 * PI_HI ** 3


def anticommuting_dim(p, q):
    n = p + q
    sq = GA.sig(p, q)
    bl = GA.all_blades(n)
    rows = []
    for i in range(n):
        e = GA.gen(i)
        cols = [GA.add(GA.mul(e, {b: F(1)}, sq), GA.mul({b: F(1)}, e, sq)) for b in bl]
        for out in bl:
            rows.append([c.get(out, F(0)) for c in cols])
    return len(bl) - GA.rank_of_vectors(rows)


def check_one_photon_like_species_breaks_the_cap():
    p_lo, p_hi = premise("dark-matter.open-channels-their-costs")["photon_bracket"]()
    ok = F(440, 100) < p_lo and p_hi < F(441, 100)
    ok = ok and 22 < 5 * p_lo and 5 * p_hi < F(221, 10) and p_lo > 10 * CAP
    GA.check("prop:audit: one photon-like species 4.40-4.41, five 22-22.1, one alone over ten times the cap", ok)
    return ok


def check_ground_level_and_vector_like_odd_towers():
    ct = premise("dark-matter.type-residue-what-each-tower-can")["clifford_type"]
    reps = {2: (3, 1), 6: (1, 3), 1: (2, 1), 7: (1, 2), 3: (4, 1), 5: (1, 4)}
    complex_members = sorted(r for r, s in reps.items() if ct(*s)["D"] == "C")
    ok = complex_members == [3, 7] and ct(3, 1)["D"] == "R"
    for p, q in ((2, 1), (1, 2), (4, 1), (1, 4)):
        n = p + q
        sq = GA.sig(p, q)
        om = {tuple(range(n)): F(1)}
        ok = ok and all(GA.commutes(om, GA.gen(i), sq) for i in range(n)) and anticommuting_dim(p, q) == 0
    ok = ok and anticommuting_dim(1, 3) == 1
    GA.check("prop:audit: intrinsic U(1) exactly at r = 3, 7; no chirality grading in dimensions three and five", ok)
    return ok


def check_closing_margins_on_the_interval():
    premise("dark-matter.mirror-tower-copy-one")
    premise("dark-matter.stored-asymmetry-charge-not-number")
    s = premise("dark-matter.seeding-gravity-floor-dark-towers-temperature")
    p_lo, p_hi = premise("dark-matter.open-channels-their-costs")["photon_bracket"]()
    mirror_hi = p_hi + NNU
    per_hi, per_lo = p_hi / 2, p_lo / 2
    hot4 = 4 * NB_OVER_S * G_STAR / G_D
    # the coefficient is 1519247 pi^3/82944000 = 0.56793, the quoted 0.568
    ok = MIRROR_COEFF_OVER_PI3 == F(1519247, 82944000)
    ok = ok and all(rounds_to(c, 56793, -5) and rounds_to(c, 568, -3) for c in (MIRROR_COEFF_LO, MIRROR_COEFF_HI))
    floor8 = s["xi8_bracket"](MIRROR_COEFF_HI, G_D)[1]
    # the floor is the quoted 5.2e-4
    ok = ok and root_rounds_to(floor8, 52, -5, 8)
    # eleven orders at the floor, and not twelve
    ok = ok and (mirror_hi * 10 ** 11) ** 2 * floor8 < CAP ** 2 < (mirror_hi * 10 ** 12) ** 2 * floor8
    # by hand (decimal evaluation): at the floor the cap exceeds the mirror's 7.447 xi^4 by 5.5138e11
    ok = ok and root_rounds_to(CAP ** 2 / (mirror_hi ** 2 * floor8), 55138, 7)
    ok = ok and mirror_hi * hot4 * 10 ** 8 < CAP
    # at the hot deposit: by 1.241301e8 (mirror) and 1.400640e8 (2.2 x 3 xi^4)
    ok = ok and rounds_to(CAP / (mirror_hi * hot4), 1241301, 2)
    ok = ok and F(22, 10) * 3 * hot4 * 10 ** 8 < CAP
    ok = ok and rounds_to(CAP / (F(22, 10) * 3 * hot4), 1400640, 2)
    nine_hi, nine_lo = per_hi * 18 * hot4, per_lo * 18 * hot4
    # 10^7.3 < CAP/nine < 10^7.4, by tenth powers; 2.33270e7 = 10^7.368, above 10^7.35, so "7.4"
    ok = ok and F(10) ** 73 < (CAP / nine_hi) ** 10 and (CAP / nine_lo) ** 10 < F(10) ** 74
    ok = ok and all(rounds_to(CAP / x, 233270, 2) for x in (nine_lo, nine_hi))
    ok = ok and F(10) ** 147 < (CAP / nine_hi) ** 20
    GA.check("prop:audit: mirror eleven orders below the cap at the floor and eight at the hot deposit; 5D towers "
             "eight; a nine-vector tower 7.3-7.4 orders at the hot deposit", ok)
    return ok


def check_mirror_atomic_cross_section():
    s_lo, s_hi = PI_LO * (2 * A0) ** 2, PI_HI * (2 * A0) ** 2
    # by hand: pi (1.058e-8)^2 = 3.5165857e-16 cm^2, in the quoted (3, 4)e-16; per mass 2.10574e8 cm^2/g
    # for hydrogen, in (2, 3)e8, and 5.29606e7 for helium, in (5, 10)e7
    ok = all(rounds_to(x, 35165857, -23) for x in (s_lo, s_hi))
    ok = ok and all(rounds_to(x / M_H, 210574, 3) for x in (s_lo, s_hi))
    ok = ok and all(rounds_to(x / M_HE, 529606, 2) for x in (s_lo, s_hi))
    GA.check("prop:audit: pi (2 a_0)^2 in (3, 4)e-16 cm^2; sigma/m (2, 3)e8 (H) and (5, 10)e7 (He) cm^2/g", ok)
    return ok
