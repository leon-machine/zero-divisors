"""dark-matter.seeding-gravity-floor-dark-towers-temperature: exact checks.

Exact rationals throughout; pi is bracketed by Machin's formula with alternating-series bounds and
never approximated; zeta(5) is bracketed by a partial sum with an exact integral bound on the tail.
Square roots are avoided by squaring: kappa_s^2 = (pi^2 g*/90)(2 pi^2/45)^2 g_s^2 is a polynomial in
pi, and xi^8 = ((4/3)(E/T) Y g*/g_d)^2 with Y kappa_s rational and E the mean energy per event.
- Boltzmann step: with Gamma = c T^8/M^4 (premises: the rate derived in the store, clause (v) of the
  pair-production theorem, and the imported Fact for its published values), H = h T^2/M and
  s = sigma T^3 for arbitrary positive h, sigma (h sigma = kappa_s), Gamma/(H T s) = c T^2/(kappa_s M^3)
  identically (checked at sample T, h, sigma); the yield from T_desc down to 0 is the integral
  c T_desc^3/(3 kappa_s M^3): the antiderivative T^3/3 is checked by exact differentiation, and lies
  strictly between the lower and upper Riemann sums with 200 steps (the sums within two percent).
  Gamma counts creation events of two quanta each, so Y is the yield of events and the quanta obey the
  same equation with source 2 Gamma (yield 2 Y, checked at the same samples). The energy fraction
  f = rho_d/rho obeys df/dT = -u Gamma/(H rho) for mean energy u T per event and rho = r T^4, the same
  integrand times u sigma/r, so f = u (sigma/r) Y (checked at the same samples).
  Gravitational production is the only source (premise: superselection leaves only the metric).
- kappa_s in (145.25, 145.30) at g* = g_s = 100 ("145.3"); 1.66 = sqrt(8 pi) sqrt(pi^2/90) to three
  figures (the two Planck-mass conventions give one rate).
- the mean energy per event (premise: clause (v) of the theorem, whose rate integral weights each
  incoming leg by E^3 times its occupation): the moments int E^k f dE are Gamma(k+1) zeta(k+1) T^(k+1)
  for Bose and (1 - 2^-k) times that for Fermi occupation, so the mean energy of a leg is
  (4!/3!) zeta(5)/zeta(4) = 4 zeta(5)/zeta(4) (Bose) and (15/16)(24)/((7/8)(6)) = 30/7 times
  zeta(5)/zeta(4) (Fermi), in units of T. zeta(5) lies in (1.0369277, 1.0369278) (partial sum to 60 with
  the tail between 1/(4 x 61^4) and 1/(4 x 60^4)); zeta(4) = pi^4/90, and the Machin bracket of pi^4/90
  lies inside the partial-sum bracket of zeta(4) (tail between 1/(3 x 61^3) and 1/(3 x 60^3)). The legs
  round to 3.832 and 4.106, the events to 7.664 (Bose pair) and 8.212 (Fermi pair), inside (7.66, 8.22).
  The Bose and Fermi parts of alpha_j are those of the theorem's closed form,
  (c_j (N_s + 12 N_v) + 5 tau_j sum tau_i)/225 and 49 c_j N_w/4800 (their sum over 17280 reproduces the
  theorem's rationals 5789/82944000, 16087/82944000, 16087/20736000, 1519247/82944000 at the bath
  (4, 45, 12) with zero curvature couplings, and 49/4800 = 3 (7/8)^2/225 is the square of the Fermi E^3
  moment against the Bose one, times the fermion weight 3). Weighted by them, the mean energy per
  event is 7.873 T (real scalar), 7.890 T (chiral fermion, real massless vector), 7.889 T (a copy of
  the bath's content); the energy fraction (4/3)(E/T) Y is between 10.49 Y and 10.52 Y.
- the floor formula: xi^4 = (4/3)(E/T) Y g*/g_d (the energy fraction E n/rho with n = Y s is
  (2/45) 30 = 4/3 times (E/T) Y at g* = g_s), and at c = 1, g_d = 16, T_desc = 6e14 GeV,
  M_P = 2.435e18 GeV the prefactor is 1.225073e-3 (scalar's energy), 1.225718e-3 (fermion's, vector's),
  1.225708e-3 (the copy's), each in (1.225, 1.226) x 10^-3 and rounding to 1.23e-3; for a Bose-only and a
  Fermi-only bath it is in (1.21, 1.24) x 10^-3; the scaling xi^4 proportional to (E/T) c (16/g_d)
  (T/6e14)^3 holds exactly at sample inputs (kappa cancels). Against energy 3T per event, the value of
  the deposited paper and of the series script (prefactor 9.625149e-4), the ratio (E/3T)^(1/4) rounds to
  1.273 (in (1.272, 1.274)).
- the ceiling range (premise: 3.5e11 to 6e14 GeV): (3.5e11/6e14)^(3/4) lies in (3.745, 3.755) x 10^-3,
  the stated 3.75 x 10^-3, about 4 x 10^-3 at one figure.
- later evolution: with g_d T_d^3 a^3 and g_s T^3 a^3 separately conserved, (T_d/T)^3 changes by
  (g_d_seed/g_d)(g_s/g_s_seed), checked at sample histories.
EXPORTS: kappa2_bracket(), xi8_bracket(c, gd, energy, T) with energy a bracket (lo, hi) of E/T,
y_kappa(c, T), MPRED, TCEIL, GSTAR, PI, QUANTA_PER_EVENT, ZETA5, rate_parts(kind), event_energy(bose,
fermi), EVENT_ENERGY (brackets of E/T for 'scalar', 'weyl', 'vector', 'mirror' at the bath (4, 45, 12)).
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
QUANTA_PER_EVENT = 2      # the rate of the pair-production theorem counts creation events of two quanta
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


def zeta_bracket(k, terms=60):
    """(lo, hi) for zeta(k), k >= 2: the partial sum to `terms` plus the tail, which lies strictly between
    the integrals of x^-k from terms + 1 and from terms, 1/((k-1)(terms+1)^(k-1)) and 1/((k-1) terms^(k-1))."""
    s = sum(F(1, n ** k) for n in range(1, terms + 1))
    return s + F(1, (k - 1) * (terms + 1) ** (k - 1)), s + F(1, (k - 1) * terms ** (k - 1))


ZETA5 = zeta_bracket(5)
ZETA4 = (PI_LO ** 4 / 90, PI_HI ** 4 / 90)          # zeta(4) = pi^4/90
RATIO54 = (ZETA5[0] / ZETA4[1], ZETA5[1] / ZETA4[0])    # zeta(5)/zeta(4)


def moment_factor(k, fermi):
    """int_0^inf E^k f(E) dE / (zeta(k+1) T^(k+1)): k! for Bose occupation, (1 - 2^-k) k! for Fermi."""
    fact = 1
    for j in range(2, k + 1):
        fact *= j
    return (1 - F(1, 2 ** k)) * fact if fermi else F(fact)


# mean energy of one incoming leg, weight E^3 f(E), in units of T zeta(5)/zeta(4)
LEG_BOSE = moment_factor(4, False) / moment_factor(3, False)
LEG_FERMI = moment_factor(4, True) / moment_factor(3, True)
BATH = (4, 45, 12)        # real scalars, chiral fermions, vectors of the Standard Model's content
SPIN_TWO_WEIGHT = {"scalar": 1, "weyl": 3, "vector": 12}
TRACE_WEIGHT = {"scalar": 1, "weyl": 0, "vector": 0}       # (1 - 6 xi)^2 at xi = 0 on scalars


def rate_parts(kind, bath=BATH):
    """(Bose part, Fermi part) of 17280 alpha_j/pi^3 in clause (v) of the pair-production theorem:
    (c_j (N_s + 12 N_v) + 5 tau_j sum tau_i)/225 from Bose incoming pairs and 49 c_j N_w/4800 from Fermi
    ones, bath scalars at zero curvature coupling. 'mirror' is the sum over a copy of the bath's content."""
    n_s, n_w, n_v = bath
    if kind == "mirror":
        parts = [rate_parts(k, bath) for k in ("scalar", "weyl", "vector")]
        return (sum(n * p[0] for n, p in zip(bath, parts)), sum(n * p[1] for n, p in zip(bath, parts)))
    cj, tj = SPIN_TWO_WEIGHT[kind], TRACE_WEIGHT[kind]
    return F(cj * (n_s + 12 * n_v) + 5 * tj * n_s, 225), F(49 * cj * n_w, 4800)


def event_energy(bose, fermi):
    """(lo, hi) for the mean energy per creation event in units of T: the two legs of a Bose pair carry
    2 LEG_BOSE zeta(5)/zeta(4) and those of a Fermi pair 2 LEG_FERMI zeta(5)/zeta(4), weighted by the
    Bose and Fermi parts of the rate."""
    w = (2 * LEG_BOSE * bose + 2 * LEG_FERMI * fermi) / (bose + fermi)
    return w * RATIO54[0], w * RATIO54[1]


EVENT_ENERGY = {k: event_energy(*rate_parts(k)) for k in ("scalar", "weyl", "vector", "mirror")}


def xi8_bracket(c, gd, energy, T=TCEIL):
    """(lo, hi) for xi_floor^8 = ((4/3)(E/T) Y g*/g_d)^2, with energy = (lo, hi) a bracket of E/T."""
    k_lo, k_hi = kappa2_bracket()
    num = (F(4, 3) * y_kappa(c, T) * GSTAR / gd) ** 2
    return energy[0] ** 2 * num / k_hi, energy[1] ** 2 * num / k_lo


def check_boltzmann_yield():
    premise("synthesis.gravitational-pair-production-from-the-operator-source-at-first-order")
    premise("dark-matter.imported-massless-graviton-production-rate")
    premise("dark-matter.superselected-hence-dark-exactly-stable")
    ok = True
    c, M = F(3, 50), F(7)
    for h, sigma in H_SAMPLES:
        for T in T_SAMPLES:
            Gamma = c * T ** 8 / M ** 4
            H, s = h * T ** 2 / M, sigma * T ** 3
            ok = ok and Gamma / (H * T * s) == c * T ** 2 / (h * sigma * M ** 3)
            # the rate counts events of QUANTA_PER_EVENT quanta: the quanta have source 2 Gamma, yield 2 Y
            ok = ok and QUANTA_PER_EVENT * Gamma / (H * T * s) == 2 * c * T ** 2 / (h * sigma * M ** 3)
            # energy: d(rho_d/rho)/dT = -u T Gamma/(H T rho) with rho = r T^4 is u sigma/r times dY/dT,
            # so the energy fraction is u (sigma/r) Y for a mean energy u T per event
            u, r = F(79, 10), F(13, 4)
            ok = ok and u * T * Gamma / (H * T * r * T ** 4) == (u * sigma / r) * Gamma / (H * T * s)
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


def check_mean_energy_per_event():
    premise("synthesis.gravitational-pair-production-from-the-operator-source-at-first-order")
    # zeta(5) in (1.0369277, 1.0369278), from the partial sum and the integral bounds on the tail
    ok = F(10369277, 10 ** 7) < ZETA5[0] < ZETA5[1] < F(10369278, 10 ** 7)
    # zeta(4) = pi^4/90: the Machin bracket lies inside the partial-sum bracket of zeta(4)
    z4 = zeta_bracket(4)
    ok = ok and z4[0] < ZETA4[0] < ZETA4[1] < z4[1] and z4[1] - z4[0] < F(1, 10 ** 7)
    # legs: Gamma(5)/Gamma(4) = 4 for Bose; (15/16) 24 / ((7/8) 6) = 30/7 for Fermi
    ok = ok and LEG_BOSE == 4 and LEG_FERMI == F(30, 7)
    ok = ok and moment_factor(3, True) == F(7, 8) * 6 and moment_factor(4, True) == F(15, 16) * 24
    for leg, m in ((LEG_BOSE, 3832), (LEG_FERMI, 4106)):
        ok = ok and all(rounds_to(leg * x, m, -3) for x in RATIO54)
    # events: 8 zeta(5)/zeta(4) = 7.664 (Bose pair), (60/7) zeta(5)/zeta(4) = 8.212 (Fermi pair)
    for leg, m in ((LEG_BOSE, 7664), (LEG_FERMI, 8212)):
        ok = ok and all(rounds_to(2 * leg * x, m, -3) for x in RATIO54)
    ok = ok and F(766, 100) < 2 * LEG_BOSE * RATIO54[0] and 2 * LEG_FERMI * RATIO54[1] < F(822, 100)
    # the Bose and Fermi parts are the theorem's closed form: their sum over 17280 gives its rationals,
    # and the Fermi part is the fermion weight 3 times the squared ratio 7/8 of the E^3 moments over 225
    printed = {"scalar": F(5789, 82944000), "weyl": F(16087, 82944000), "vector": F(16087, 20736000),
               "mirror": F(1519247, 82944000)}
    for kind, alpha in printed.items():
        b, f = rate_parts(kind)
        ok = ok and (b + f) / 17280 == alpha
    ok = ok and rate_parts("weyl")[0] == F(3 * (4 + 12 * 12), 225) and rate_parts("scalar")[0] == F(148 + 20, 225)
    ok = ok and F(49, 4800) == 3 * (moment_factor(3, True) / moment_factor(3, False)) ** 2 / 225
    ok = ok and rate_parts("scalar")[1] == F(49 * 45, 4800)
    # the mean energy per event in units of T: 7.873 (scalar), 7.890 (fermion, vector), 7.889 (copy)
    for kind, m in (("scalar", 7873), ("weyl", 7890), ("vector", 7890), ("mirror", 7889)):
        ok = ok and all(rounds_to(x, m, -3) for x in EVENT_ENERGY[kind])
    ok = ok and EVENT_ENERGY["weyl"] == EVENT_ENERGY["vector"]
    # every content lies between the Bose-pair and Fermi-pair values, and the energy fraction
    # (4/3)(E/T) Y between 10.49 Y and 10.52 Y for the three species and the copy
    for kind in printed:
        lo, hi = EVENT_ENERGY[kind]
        ok = ok and 2 * LEG_BOSE * RATIO54[1] < lo and hi < 2 * LEG_FERMI * RATIO54[0]
        ok = ok and F(1049, 100) < F(4, 3) * lo and F(4, 3) * hi < F(1052, 100)
    GA.check("prop:gravseed: mean energy per event from the E^3 leg weights: 4 zeta(5)/zeta(4) T = 3.832 T (Bose leg), "
             "(30/7) zeta(5)/zeta(4) T = 4.106 T (Fermi leg); 7.873 T, 7.890 T, 7.889 T per event for a scalar, a "
             "fermion or vector, a copy of the bath (4, 45, 12); energy fraction in (10.49, 10.52) Y", ok)
    return ok


def check_floor_prefactor_and_scaling():
    premise("synthesis.gravitational-pair-production-from-the-operator-source-at-first-order")
    premise("dark-matter.imported-massless-graviton-production-rate")
    ok = True
    # by hand: xi^4 = (4/3)(E/T) (6e14)^3 100/(3 (2.435e18)^3 16 x 145.25993), with E/T = 7.872984,
    # 7.889576, 7.889323: xi = 1.225073e-3, 1.225718e-3, 1.225708e-3, each in (1.225, 1.226)e-3 and
    # rounding to the quoted 1.23e-3
    for kind, m in (("scalar", 1225073), ("weyl", 1225718), ("vector", 1225718), ("mirror", 1225708)):
        for x in xi8_bracket(F(1), F(16), EVENT_ENERGY[kind]):
            ok = ok and root_rounds_to(x, m, -9, 8) and root_rounds_to(x, 123, -5, 8)
    # any bath and content: between the Bose-pair value, by hand 1.2169e-3, and the Fermi-pair value,
    # 1.2381e-3, so inside (1.21, 1.24)e-3
    for x in xi8_bracket(F(1), F(16), event_energy(F(1), F(0))):
        ok = ok and root_rounds_to(x, 12169, -7, 8)
    for x in xi8_bracket(F(1), F(16), event_energy(F(0), F(1))):
        ok = ok and root_rounds_to(x, 12381, -7, 8)
    # energy fraction E n/rho with n = Y s, s = (2 pi^2/45) g T^3, rho = (pi^2/30) g T^4: (2/45) 30 = 4/3
    # times (E/T) Y; the scaling of xi^4 is exact in (E/T) c (16/g_d) (T/6e14)^3
    ok = ok and F(2, 45) * 30 == F(4, 3)
    u0 = F(789, 100)
    base = F(4, 3) * u0 * y_kappa(F(1), TCEIL) * GSTAR / 16
    for (c, gd, T), u in zip(SCALING_SAMPLES, (F(77, 10), F(82, 10), u0)):
        val = F(4, 3) * u * y_kappa(c, T) * GSTAR / gd
        ok = ok and val / base == (u / u0) * c * (16 / gd) * (T / TCEIL) ** 3
        b = xi8_bracket(c, gd, (u, u), T)
        ok = ok and b[0] * kappa2_bracket()[1] == val ** 2 == b[1] * kappa2_bracket()[0]
    # against energy 3T per event (the deposited paper and the series script): prefactor 9.625149e-4, and
    # the stated floor is (E/3T)^(1/4) times it, in (1.272, 1.274)
    for x in xi8_bracket(F(1), F(16), (F(3), F(3))):
        ok = ok and root_rounds_to(x, 9625149, -10, 8)
    for kind in ("scalar", "weyl", "vector", "mirror"):
        for u in EVENT_ENERGY[kind]:
            ok = ok and root_rounds_to(u / 3, 1273, -3, 4)
    GA.check("prop:gravseed: xi_floor = 1.23e-3 c^(1/4) (16/g_d)^(1/4) (T/6e14)^(3/4) at the mean energy per event: "
             "prefactor in (1.225, 1.226)e-3 for the bath (4, 45, 12), in (1.21, 1.24)e-3 for any bath, and the scaling "
             "exact; energy fraction (4/3)(E/T) Y", ok)
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
           "MPRED": MPRED, "TCEIL": TCEIL, "GSTAR": GSTAR, "PI": (PI_LO, PI_HI),
           "QUANTA_PER_EVENT": QUANTA_PER_EVENT, "ZETA5": ZETA5, "rate_parts": rate_parts,
           "event_energy": event_energy, "EVENT_ENERGY": EVENT_ENERGY}
