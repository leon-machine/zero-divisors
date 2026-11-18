"""dark-matter.coefficients-floors-they-give-what-gravity: exact checks.

The floor formula, kappa_s^2 (a polynomial in pi, pi bracketed by Machin's formula) and the yield
Y kappa_s = c T^3/(3 M_P^3) come from the seeding proposition's exports; every comparison of a root is
made on an integer power (xi^8 against a bound^8, eta'^8 = eta^8/xi^24, cube roots by cubes).
The per-species coefficients are those of clause (v) of the pair-production theorem (premise), for a
bath of the Standard Model's content (4 real scalars, 45 chiral fermions, 12 vectors, curvature
couplings zero), per creation event of two quanta: alpha = pi^3 times
(1/17280)[(c_j (N_s + 12 N_v) + 5 tau_j N_s)/225 + 49 c_j N_w/4800], c_j = 1, 3, 12, tau_j = 1, 0, 0,
that is 5789/82944000 (real scalar), 16087/82944000 (chiral fermion), 16087/20736000 (real massless
vector), rounding to 2.164e-3, 6.0137e-3, 2.4055e-2; the earlier values 1.9e-4, 1.1e-3, 2.3e-3 of the
imported Fact (premise, kept for the published values) were too small. pi^3 is never approximated:
every coefficient is the exact rational times the cube of an end of the Machin bracket of pi, and the
two ends are carried as (c_lo, c_hi); the earlier bracket between counting the fermions per Dirac and
per Weyl species is gone (each of the 45 is weighted once).
eta = 2.74e-8 Omega_b h^2 with Omega_b h^2 = 0.02237; baryons per entropy n_B/s = 0.1413 eta.
The floors are the seeding proposition's, at its mean energy per creation event (its export EVENT_ENERGY,
brackets of E/T from the E^3 leg weights of the rate integral, zeta(5) bracketed there): 7.889 T for a
copy of the bath's content and 7.890 T for vectors; the Bose and Fermi parts of the rate that weight the
mean (its export rate_parts) sum to the coefficients computed here.
(i) Nine vectors: c = 9 x 16087 pi^3/20736000 in (0.2164, 0.2165), g_d = 18, xi_floor in (8.1, 8.2) x 10^-4
at 6e14 GeV, rounding to 8.1e-4.
(ii) Mirror (premise: its content is the Standard Model's: 4 real scalars, 45 Weyl fermions, 12
vectors): c = 1519247 pi^3/82944000 in (0.5679, 0.5680); g_d = 4 + 45 x 7/4 + 24 = 106.75; xi_floor in
(6.6, 6.7) x 10^-4, rounding to 6.6e-4 (1/xi between 1500 and 1520); eta' = eta/xi^3 in (2.1, 2.2);
eta' > 1 at c = 1.539 and < 1 at c = 1.54 (decreasing in c; the mirror's g_d and energy per event), and
c = 1.539 is between 2.7 and 2.8 times the mirror's c.
(iii) Y in (1.94, 1.96) x 10^-14 creation events per entropy at the ceiling; n_B/s in (8.6, 8.7) x 10^-11;
shortfall in (4.4, 4.5) x 10^3 (half that, in (2.2, 2.3) x 10^3, against the 2Y quanta);
the rescue temperature T_desc (n_B/(s Y))^(1/3) in (9.8, 9.9) x 10^15 GeV, between 16.4 and 16.5 times
the ceiling (these count events and quanta, not energy, and are unchanged);
there the floor's xi^4 is (4/3)(E/T) (n_B/s) g*/g_d, xi in (5.40, 5.41) x 10^-3, above eta^(1/3); the
hot-deposit value is 4 (n_B/s) g*/g_d (energy 3T per unit of baryon number against (3/4) T s), xi in
(4.2, 4.3) x 10^-3, and the floor there is (E/3T)^(1/4) times it, a factor in (1.273, 1.274): the two no
longer coincide.
(iv) Delta N_eff of the mirror, 7.447 xi^4 with 7.447 = (8/7)(11/4)^(4/3) + 3.044 bracketed exactly:
in (1.4, 1.5) x 10^-12 at the floor, so below 2e-12 and no longer below 1e-12, and below 1e-8 at the hot
deposit; per polarisation (4/7)(11/4)^(4/3) in
(2.201, 2.203), and 2.202 x 18 xi^4 in (1.7, 1.8) x 10^-11 at the nine-vector floor, so below 2e-11 and
no longer below 1e-11.
EXPORTS: cosmo() returns the shared inputs and brackets (eta, n_B/s, xi^4 at the hot deposit, the
Delta N_eff coefficients, the mirror floor's xi^8 bracket as floor8 and the nine-vector floor's as
floor8_nine, the mirror's c as (c_lo, c_hi), the ends of its pi bracket, the nine-vector c as c_nine,
and the brackets of E/T as energy and energy_nine); species() returns the exact rationals alpha/pi^3.
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
THEOREM = "synthesis.gravitational-pair-production-from-the-operator-source-at-first-order"
BATH = (4, 45, 12)        # real scalars, chiral fermions, vectors of the Standard Model's content
SPIN_TWO_WEIGHT = {"scalar": 1, "weyl": 3, "vector": 12}
TRACE_WEIGHT = {"scalar": 1, "weyl": 0, "vector": 0}       # (1 - 6 xi)^2 at xi = 0 on scalars


def alpha_over_pi3(kind):
    """alpha/pi^3 of clause (v) of the pair-production theorem for one produced species, per creation event:
    (1/17280)[(c_j (N_s + 12 N_v) + 5 tau_j N_s)/225 + 49 c_j N_w/4800], bath scalars at xi = 0."""
    n_s, n_w, n_v = BATH
    cj, tj = SPIN_TWO_WEIGHT[kind], TRACE_WEIGHT[kind]
    return (F(cj * (n_s + 12 * n_v) + 5 * tj * n_s, 225) + F(49 * cj * n_w, 4800)) / 17280


def species():
    """The exact rationals alpha/pi^3: real scalar, chiral fermion, real massless vector, and their sum over
    a produced copy of the Standard Model's content (4, 45, 12)."""
    r_s, r_w, r_v = (alpha_over_pi3(k) for k in ("scalar", "weyl", "vector"))
    n_s, n_w, n_v = BATH
    return dict(scalar=r_s, weyl=r_w, vector=r_v, mirror=n_s * r_s + n_w * r_w + n_v * r_v)


def pi3(r):
    """(lo, hi) for r pi^3, r a positive rational, from the Machin bracket of pi."""
    return r * PI_LO ** 3, r * PI_HI ** 3


def coefficients_ok():
    """The closed form gives the theorem's printed rationals, and they round to the quoted decimals."""
    sp = species()
    ok = sp["scalar"] == F(5789, 82944000) and sp["weyl"] == F(16087, 82944000)
    ok = ok and sp["vector"] == F(16087, 20736000) and sp["mirror"] == F(1519247, 82944000)
    for r, m, e in ((sp["scalar"], 2164, -6), (sp["weyl"], 60137, -7), (sp["vector"], 24055, -6),
                    (sp["mirror"], 56793, -5), (9 * sp["vector"], 21649, -5)):
        ok = ok and all((2 * m - 1) * F(10) ** e / 2 < x < (2 * m + 1) * F(10) ** e / 2 for x in pi3(r))
    return ok


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
    sp = species()
    # one value of c for the mirror; (c_lo, c_hi) are the two ends of its pi bracket
    c_lo, c_hi = pi3(sp["mirror"])
    photon, mirror, per_pol = neff_coeffs()
    xi_hot4 = 4 * NB_S * s["GSTAR"] / GD_MIRROR
    # mean energy per creation event in units of T (brackets): a copy of the bath's content, and vectors
    energy, energy_nine = s["EVENT_ENERGY"]["mirror"], s["EVENT_ENERGY"]["vector"]
    c_nine = pi3(9 * sp["vector"])
    return dict(eta=ETA, nb_s=NB_S, c_lo=c_lo, c_hi=c_hi, gd=GD_MIRROR, xi_hot4=xi_hot4,
                floor8=(s["xi8_bracket"](c_lo, GD_MIRROR, energy)[0], s["xi8_bracket"](c_hi, GD_MIRROR, energy)[1]),
                floor8_nine=(s["xi8_bracket"](c_nine[0], F(18), energy_nine)[0],
                             s["xi8_bracket"](c_nine[1], F(18), energy_nine)[1]),
                photon=photon, mirror=mirror, per_pol=per_pol, seeding=s,
                c_nine=c_nine, species=sp, energy=energy, energy_nine=energy_nine)


def energies_ok():
    """The seeding proposition's Bose and Fermi parts of the rate sum to the coefficients used here, and its
    mean energies per event are the quoted 7.889 T (a copy of the bath) and 7.890 T (vectors)."""
    s = seeding()
    sp = species()
    ok = all(sum(s["rate_parts"](k)) / 17280 == sp[k] for k in ("scalar", "weyl", "vector", "mirror"))
    # by hand: 7.889323 (a copy of the bath) and 7.889576 (vectors), the quoted 7.889 and 7.890
    ok = ok and all(rounds_to(x, 7889323, -6) and rounds_to(x, 7889, -3) for x in s["EVENT_ENERGY"]["mirror"])
    ok = ok and all(rounds_to(x, 7889576, -6) and rounds_to(x, 7890, -3) for x in s["EVENT_ENERGY"]["vector"])
    return ok


def check_nine_vector_floor():
    premise(THEOREM)
    premise("dark-matter.imported-massless-graviton-production-rate")
    s = seeding()
    c_lo, c_hi = pi3(9 * species()["vector"])
    lo, hi = cosmo()["floor8_nine"]
    ok = coefficients_ok() and energies_ok() and F(2164, 10 ** 4) < c_lo and c_hi < F(2165, 10 ** 4)
    # by hand: xi_floor = 8.1183e-4, in (8.1, 8.2)e-4 and rounding to the quoted 8.1e-4
    ok = ok and all(root_rounds_to(x, 81183, -8, 8) and root_rounds_to(x, 81, -5, 8) for x in (lo, hi))
    GA.check("prop:coefficients(i): c = 9 x 16087 pi^3/20736000 in (0.2164, 0.2165), g_d = 18, xi_floor in "
             "(8.1, 8.2)e-4, 8.1e-4 at two figures", ok)
    return ok


def check_mirror_floor_and_eta_prime():
    premise("dark-matter.imported-massless-graviton-production-rate")
    premise("dark-matter.mirror-tower-copy-one")
    premise(THEOREM)
    s = seeding()
    k = cosmo()
    ok = coefficients_ok() and energies_ok() and F(5679, 10 ** 4) < k["c_lo"] <= k["c_hi"] < F(5680, 10 ** 4)
    ok = ok and k["gd"] == F(10675, 100)
    lo_a, hi_b = k["floor8"]
    for x in (lo_a, hi_b):
        # by hand: xi_floor = 6.6206e-4, in (6.6, 6.7)e-4 and rounding to the quoted 6.6e-4; the lay level's
        # "about fifteen hundred times colder": 1/xi = 1510
        ok = ok and root_rounds_to(x, 66206, -8, 8) and root_rounds_to(x, 66, -5, 8)
        ok = ok and root_rounds_to(1 / x, 1510, 0, 8)
        # eta'^8 = eta^8 / xi^24: by hand eta' = 2.1121, in (2.1, 2.2) and the quoted 2.1
        ok = ok and root_rounds_to(ETA ** 8 / x ** 3, 21121, -4, 8) and root_rounds_to(ETA ** 8 / x ** 3, 21, -1, 8)
    # the crossover eta' = 1, at the mirror's g_d and energy per event: between c = 1.539 and 1.54
    hi_below = s["xi8_bracket"](F(1539, 1000), k["gd"], k["energy"])[1]
    lo_above = s["xi8_bracket"](F(154, 100), k["gd"], k["energy"])[0]
    ok = ok and ETA ** 8 / hi_below ** 3 > 1 and ETA ** 8 / lo_above ** 3 < 1
    # the mirror's c is below the crossover by a factor between 2.7 and 2.8
    ok = ok and F(27, 10) * k["c_hi"] < F(1539, 1000) and F(154, 100) < F(28, 10) * k["c_lo"]
    GA.check("prop:coefficients(ii): mirror c = 1519247 pi^3/82944000 in (0.5679, 0.5680), g_d = 106.75, xi in "
             "(6.6, 6.7)e-4, eta' in (2.1, 2.2), eta' = 1 between c = 1.539 and 1.54, 2.7 times the mirror's c", ok)
    return ok


def check_yield_shortfall_and_rescue():
    premise("dark-matter.seeding-gravity-floor-dark-towers-temperature")
    s = seeding()
    k = cosmo()
    k2lo, k2hi = s["kappa2_bracket"]()
    yk_lo, yk_hi = s["y_kappa"](k["c_lo"], s["TCEIL"]), s["y_kappa"](k["c_hi"], s["TCEIL"])
    # Y^2 = (Y kappa)^2 / kappa^2; by hand Y = 1.950e-14 creation events per unit entropy, in (1.94, 1.96)e-14
    Y2_lo, Y2_hi = yk_lo ** 2 / k2hi, yk_hi ** 2 / k2lo
    ok = all(root_rounds_to(y2, 1950, -17) and root_rounds_to(y2, 195, -16) for y2 in (Y2_lo, Y2_hi))
    # by hand: n_B/s = 0.1413 x 2.74e-8 x 0.02237 = 8.66081394e-11, the quoted 8.7e-11
    ok = ok and NB_S == F(866081394, 10 ** 19) and rounds_to(NB_S, 87, -12)
    q = s["QUANTA_PER_EVENT"]
    for short2 in (NB_S ** 2 / Y2_hi, NB_S ** 2 / Y2_lo):
        # by hand: the shortfall is 4442, the quoted 4.4e3; Y counts creation events, and against the 2Y quanta
        # it is halved, 2221, the quoted 2.2e3
        ok = ok and root_rounds_to(short2, 4442, 0) and root_rounds_to(short2, 44, 2)
        ok = ok and root_rounds_to(short2 / q ** 2, 2221, 0) and root_rounds_to(short2 / q ** 2, 22, 2)
        # rescue: (T/Tceil)^3 = n_B/(s Y), so (T/Tceil)^6 = shortfall^2; by hand the factor is 16.438 (the
        # quoted 16.4) and the temperature 9.863e15 GeV (the quoted 9.9e15)
        ok = ok and root_rounds_to(short2, 16438, -3, 6) and root_rounds_to(short2, 164, -1, 6)
        ok = ok and root_rounds_to(short2 * s["TCEIL"] ** 6, 9863, 12, 6)
        ok = ok and root_rounds_to(short2 * s["TCEIL"] ** 6, 99, 14, 6)
    # the hot deposit: energy 3T per unit of baryon number against rho/s = (3/4) T, xi^4 = 4 (n_B/s) g*/g_d;
    # by hand xi = 4.244e-3 (the quoted 4.2e-3), above the crossover eta^(1/3)
    hot = 3 * NB_S / F(3, 4) * s["GSTAR"] / k["gd"]
    ok = ok and hot == k["xi_hot4"] == 4 * NB_S * s["GSTAR"] / k["gd"]
    ok = ok and root_rounds_to(hot, 4244, -6, 4) and root_rounds_to(hot, 42, -4, 4) and ETA ** 4 < hot ** 3
    # at the rescue temperature Y = n_B/s (one event per unit of baryon number), so the floor's xi^4 is
    # (4/3)(E/T) (n_B/s) g*/g_d: by hand xi = 5.405e-3 (the quoted 5.4e-3), above the hot deposit by
    # (E/3T)^(1/4) = 1.2734 (the quoted 1.27), and so above the crossover as well
    for u in k["energy"]:
        floor_at_rescue = F(4, 3) * u * NB_S * s["GSTAR"] / k["gd"]
        ok = ok and floor_at_rescue / hot == u / 3
        ok = ok and root_rounds_to(floor_at_rescue, 5405, -6, 4) and root_rounds_to(floor_at_rescue, 54, -4, 4)
        ok = ok and root_rounds_to(floor_at_rescue / hot, 12734, -4, 4)
        ok = ok and root_rounds_to(floor_at_rescue / hot, 127, -2, 4)
    GA.check("prop:coefficients(iii): Y in (1.94, 1.96)e-14 against 8.7e-11; shortfall (4.4, 4.5)e3; rescue at 16.4 to "
             "16.5 times the ceiling, (9.8, 9.9)e15 GeV, where the floor is xi in (5.40, 5.41)e-3, 1.27 times the hot "
             "deposit's (4.2, 4.3)e-3", ok)
    return ok


def check_neff_contributions():
    premise("dark-matter.open-channels-their-costs")
    k = cosmo()
    s = seeding()
    photon, mirror, per_pol = neff_coeffs()
    # by hand: (8/7)(11/4)^(4/3) + 3.044 = 7.4472 and (4/7)(11/4)^(4/3) = 2.2016, the quoted 7.447 and 2.202
    ok = all(rounds_to(x, 74472, -4) and rounds_to(x, 7447, -3) for x in mirror)
    ok = ok and all(rounds_to(x, 22016, -4) and rounds_to(x, 2202, -3) for x in per_pol)
    # mirror at its floor: 7.447 xi^4 = 1.4308e-12 (the quoted 1.4e-12), so below 2e-12 and not below 1e-12
    for m, f8 in zip(mirror, k["floor8"]):
        v2 = m ** 2 * f8
        ok = ok and root_rounds_to(v2, 14308, -16) and root_rounds_to(v2, 14, -13)
        ok = ok and F(1, 10 ** 12) ** 2 < v2 < F(2, 10 ** 12) ** 2
    # at the hot deposit: by hand 7.447 xi^4 = 2.4168e-9, below 1e-8
    ok = ok and all(rounds_to(m * k["xi_hot4"], 24168, -13) for m in mirror) and mirror[1] * k["xi_hot4"] < F(1, 10 ** 8)
    # nine vectors at their floor: 2.202 x 18 xi^4 = 1.7213e-11 (the quoted 1.7e-11), so below 2e-11 and not
    # below 1e-11
    for p, f8 in zip(per_pol, k["floor8_nine"]):
        v2 = (p * 18) ** 2 * f8
        ok = ok and root_rounds_to(v2, 17213, -15) and root_rounds_to(v2, 17, -12)
        ok = ok and F(1, 10 ** 11) ** 2 < v2 < F(2, 10 ** 11) ** 2
    GA.check("prop:coefficients(iv): 7.447 xi^4 in (1.4, 1.5)e-12 at the floor (below 2e-12, not below 1e-12) and "
             "below 1e-8 at the hot deposit; 2.202 x 18 xi^4 in (1.7, 1.8)e-11 at the nine-vector floor (below 2e-11, "
             "not below 1e-11)", ok)
    return ok


EXPORTS = {"cosmo": cosmo, "neff_coeffs": neff_coeffs, "species": species, "pi3": pi3}
