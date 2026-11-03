"""dark-matter.coefficients-floors-they-give-what-gravity: exact checks.

The floor formula, kappa_s^2 (a polynomial in pi, pi bracketed by Machin's formula) and the yield
Y kappa_s = c T^3/(3 M_P^3) come from the seeding proposition's exports; every comparison of a root is
made on an integer power (xi^8 against a bound^8, eta'^8 = eta^8/xi^24, cube roots by cubes). The
per-species coefficients 1.9e-4, 1.1e-3, 2.3e-3 (scalar, fermion, vector) are the imported graviton
rate's. eta = 2.74e-8 Omega_b h^2 with Omega_b h^2 = 0.02237; baryons per entropy n_B/s = 0.1413 eta.
(i) Nine vectors: c = 9 x 2.3e-3 = 0.0207, g_d = 18, xi_floor in (3.5, 3.6) x 10^-4 at 6e14 GeV.
(ii) Mirror (premise: its content is the Standard Model's: 4 real scalars, 45 Weyl fermions, 12
vectors): c in (0.053, 0.054) with 22.5 Dirac species and (0.077, 0.078) counting 45 singly;
g_d = 4 + 45 x 7/4 + 24 = 106.75; xi_floor in (2.8, 3.2) x 10^-4 for both; eta' = eta/xi^3 in (19, 26);
eta' > 1 at c = 4 and < 1 at c = 4.1 (decreasing in c).
(iii) Y in (1.8, 2.7) x 10^-15 at the ceiling; n_B/s in (8.6, 8.7) x 10^-11; shortfall in (3, 5) x 10^4;
the rescue temperature T_desc (n_B/(s Y))^(1/3) in (1.9, 2.2) x 10^16 GeV, 31.9 to 36.2 times the
ceiling (each end of the range to that decimal);
there the floor's xi^4 equals 4 (n_B/s) g*/g_d exactly, the hot-deposit value (energy 3T per unit of
baryon number against (3/4) T s), with xi in (4.0, 4.5) x 10^-3, above eta^(1/3).
(iv) Delta N_eff of the mirror, 7.447 xi^4 with 7.447 = (8/7)(11/4)^(4/3) + 3.044 bracketed exactly:
below 1e-13 at the floor and 1e-8 at the hot deposit; per polarisation (4/7)(11/4)^(4/3) in
(2.201, 2.203), and 2.202 x 18 xi^4 below 1e-12 at the nine-vector floor.
EXPORTS: cosmo() returns the shared inputs and brackets (eta, n_B/s, xi^4 at the hot deposit, the
Delta N_eff coefficients, the mirror floor's xi^8 bracket).
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
A_S, A_F, A_V = F(19, 10 ** 5), F(11, 10 ** 4), F(23, 10 ** 4)
OMEGA_B = F(2237, 10 ** 5)
ETA = F(274, 10 ** 10) * OMEGA_B
NB_S = ETA * F(1413, 10 ** 4)
GD_MIRROR = 4 + 45 * F(7, 4) + 24


def neff_coeffs():
    lo, hi = iroot_bracket(F(11, 4), 3, 10 ** 7)
    photon = (F(8, 7) * F(11, 4) * lo, F(8, 7) * F(11, 4) * hi)
    mirror = (photon[0] + F(3044, 1000), photon[1] + F(3044, 1000))
    per_pol = (photon[0] / 2, photon[1] / 2)
    return photon, mirror, per_pol


def seeding():
    return premise("dark-matter.seeding-gravity-floor-dark-towers-temperature")


def cosmo():
    s = seeding()
    c_lo = 4 * A_S + F(45, 2) * A_F + 12 * A_V
    c_hi = 4 * A_S + 45 * A_F + 12 * A_V
    photon, mirror, per_pol = neff_coeffs()
    xi_hot4 = 4 * NB_S * s["GSTAR"] / GD_MIRROR
    return dict(eta=ETA, nb_s=NB_S, c_lo=c_lo, c_hi=c_hi, gd=GD_MIRROR, xi_hot4=xi_hot4,
                floor8=(s["xi8_bracket"](c_lo, GD_MIRROR)[0], s["xi8_bracket"](c_hi, GD_MIRROR)[1]),
                photon=photon, mirror=mirror, per_pol=per_pol, seeding=s)


def check_nine_vector_floor():
    premise("dark-matter.imported-massless-graviton-production-rate")
    s = seeding()
    c = 9 * A_V
    lo, hi = s["xi8_bracket"](c, F(18))
    ok = c == F(207, 10 ** 4) and F(35, 10 ** 5) ** 8 < lo and hi < F(36, 10 ** 5) ** 8
    GA.check("prop:coefficients(i): c = 0.0207, g_d = 18, xi_floor in (3.5, 3.6)e-4", ok)
    return ok


def check_mirror_floor_and_eta_prime():
    premise("dark-matter.imported-massless-graviton-production-rate")
    premise("dark-matter.mirror-tower-copy-one")
    s = seeding()
    k = cosmo()
    ok = F(53, 1000) < k["c_lo"] < F(54, 1000) and F(77, 1000) < k["c_hi"] < F(78, 1000)
    ok = ok and k["gd"] == F(10675, 100)
    lo_a, hi_a = s["xi8_bracket"](k["c_lo"], k["gd"])
    lo_b, hi_b = s["xi8_bracket"](k["c_hi"], k["gd"])
    ok = ok and F(28, 10 ** 5) ** 8 < lo_a and hi_b < F(32, 10 ** 5) ** 8
    # eta'^8 = eta^8 / xi^24
    ok = ok and F(19) ** 8 < ETA ** 8 / hi_b ** 3 and ETA ** 8 / lo_a ** 3 < F(26) ** 8
    hi4 = s["xi8_bracket"](F(4), k["gd"])[1]
    lo41 = s["xi8_bracket"](F(41, 10), k["gd"])[0]
    ok = ok and ETA ** 8 / hi4 ** 3 > 1 and ETA ** 8 / lo41 ** 3 < 1
    GA.check("prop:coefficients(ii): mirror c in (0.053, 0.054) / (0.077, 0.078), g_d = 106.75, xi in (2.8, 3.2)e-4, "
             "eta' in (19, 26), eta' = 1 between c = 4 and 4.1", ok)
    return ok


def check_yield_shortfall_and_rescue():
    premise("dark-matter.seeding-gravity-floor-dark-towers-temperature")
    s = seeding()
    k = cosmo()
    k2lo, k2hi = s["kappa2_bracket"]()
    yk_lo, yk_hi = s["y_kappa"](k["c_lo"], s["TCEIL"]), s["y_kappa"](k["c_hi"], s["TCEIL"])
    # Y^2 = (Y kappa)^2 / kappa^2
    Y2_lo, Y2_hi = yk_lo ** 2 / k2hi, yk_hi ** 2 / k2lo
    ok = F(18, 10 ** 16) ** 2 < Y2_lo and Y2_hi < F(27, 10 ** 16) ** 2
    ok = ok and F(86, 10 ** 12) < NB_S < F(87, 10 ** 12)
    short2_lo, short2_hi = NB_S ** 2 / Y2_hi, NB_S ** 2 / Y2_lo
    ok = ok and F(3 * 10 ** 4) ** 2 < short2_lo and short2_hi < F(5 * 10 ** 4) ** 2
    # rescue: (T/Tceil)^3 = n_B/(s Y), so (T/Tceil)^6 = shortfall^2; the factor runs from 31.9 to 36.2
    # (each end to the stated decimal: lower end in (31.85, 31.95), upper end in (36.15, 36.25))
    ok = ok and F(3185, 100) ** 6 < short2_lo < F(3195, 100) ** 6
    ok = ok and F(3615, 100) ** 6 < short2_hi < F(3625, 100) ** 6
    ok = ok and (F(19) * 10 ** 15 / s["TCEIL"]) ** 6 < short2_lo and short2_hi < (F(22) * 10 ** 15 / s["TCEIL"]) ** 6
    # at the rescue temperature Y = n_B/s, so xi^4 = 4 (n_B/s) g*/g_d: the hot-deposit value
    floor_at_rescue = 4 * NB_S * s["GSTAR"] / k["gd"]
    hot = 3 * NB_S / F(3, 4) * s["GSTAR"] / k["gd"]
    ok = ok and floor_at_rescue == hot == k["xi_hot4"]
    ok = ok and F(40, 10 ** 4) ** 4 < hot < F(45, 10 ** 4) ** 4 and ETA ** 4 < hot ** 3
    GA.check("prop:coefficients(iii): Y in (1.8, 2.7)e-15 against 8.7e-11; shortfall (3, 5)e4; rescue at 31.9 to 36.2 times "
             "the ceiling, (1.9, 2.2)e16 GeV, where the floor equals the hot deposit, xi in (4.0, 4.5)e-3", ok)
    return ok


def check_neff_contributions():
    premise("dark-matter.open-channels-their-costs")
    k = cosmo()
    s = seeding()
    photon, mirror, per_pol = neff_coeffs()
    ok = F(7446, 1000) < mirror[0] and mirror[1] < F(7448, 1000)
    ok = ok and F(2201, 1000) < per_pol[0] and per_pol[1] < F(2203, 1000)
    ok = ok and mirror[1] ** 2 * k["floor8"][1] < F(1, 10 ** 13) ** 2
    ok = ok and mirror[1] * k["xi_hot4"] < F(1, 10 ** 8)
    nine = s["xi8_bracket"](9 * A_V, F(18))[1]
    ok = ok and (per_pol[1] * 18) ** 2 * nine < F(1, 10 ** 12) ** 2
    GA.check("prop:coefficients(iv): 7.447 xi^4 below 1e-13 at the floor and 1e-8 at the hot deposit; 2.202 x 18 xi^4 "
             "below 1e-12 at the nine-vector floor", ok)
    return ok


EXPORTS = {"cosmo": cosmo, "neff_coeffs": neff_coeffs}
