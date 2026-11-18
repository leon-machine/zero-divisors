"""simulations.imported-mirror: exact checks of the computable figures.

Inputs are T14's (legacy/verify_T14.py, prop:coefficients and prop:charge), except the per-species
gravitational production coefficients, which are the derived ones the stored propositions now use
(per creation event, over pi^3: 5789/82944000 for a real scalar, 16087/82944000 for a chiral fermion,
16087/20736000 for a real massless vector; T14's 1.9e-4, 1.1e-3, 2.3e-3 were too small); the mirror's g_d =
4 + 45 x 1.75 + 24 = 106.75; g* = 100; reduced Planck mass 2.435e18 GeV; ceiling 6e14 GeV;
eta = 2.74e-8 x 0.02237; n_gamma/s = 0.1413; m_p = 938.272, m_He4 = 3727.379 MeV; a_0 = 0.529e-8 cm,
m_H = 1.67e-24 g, m_He = 6.64e-24 g. Everything is exact rational interval arithmetic: pi from
Machin's series with remainder, sqrt(10) from integer square roots, fourth and cube roots handled
by comparing powers.
(1) Omega_b' / Omega_b = 0.995 to 1: a mirror burnt to helium has mean mass per baryon m_He4/4
    against ours 0.75 m_p + 0.25 m_He4/4 (75/25 by baryon number), ratio in (0.994, 0.996) (the
    proton-only branch is the ratio 1 by definition).
(2) The temperature ratio: the gravitational floor xi^4 = (4/3)(E/T) Y g*/g_d with
    Y = c (T/M_P)^3/(3 kappa), kappa = sqrt(pi^2 g*/90)(2 pi^2/45) g*, c = 1519247 pi^3/82944000 in
    (0.5679, 0.5680) (each of the 45 chiral fermions weighted once; pi from its Machin bounds), and E the
    mean energy per creation event of the stored seeding proposition, E/T = (8 B + (60/7) F)/(B + F) x
    90 zeta(5)/pi^4 with B = 41964/225 and F = 283 x 2205/4800 the Bose and Fermi parts of 17280 c/pi^3
    (zeta(5) from its partial sum to 60 terms with integral bounds on the tail), in (7.889, 7.890); this
    gives xi in (6.6, 6.7) x 10^-4, rounding to the stated 6.6 x 10^-4 (T14 printed 2.8 to 3.2 x 10^-4,
    with energy 3T per event and coefficients since corrected);
    the hot deposit xi^4 = 3 (n_B/s)/(3/4) g*/g_d, n_B/s = 8.66081394e-11, gives xi in (4.2, 4.3) x 10^-3
    ("about 4 x 10^-3"), above the floor and inside the helium window (3 x 10^-3, 2 x 10^-2) stated from T14c.
(3) eta' = eta/xi^3 (equal baryon number, photon number proportional to T^3): checked as the identity
    n_b / (xi^3 n_gamma) at sample xi (eta = 6.12938e-10), and at the computed floor eta' in (2.1, 2.2),
    at the hot deposit in (0.0080, 0.0081).
(4) Neutral-atom cross-section per mass: sigma = pi (2 a_0)^2 in (3.5, 3.6) x 10^-16 cm^2, so sigma/m in
    (2.1, 2.2) x 10^8 cm^2/g for hydrogen and (5.2, 5.3) x 10^7 for helium: of order 2 x 10^8 and 5 x 10^7.
Not computable here: the helium/neutron composition (the burning network is not modelled), and the
plasma behaviour inside halos.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

A_S, A_F, A_V = F(5789, 82944000), F(16087, 82944000), F(16087, 20736000)     # over pi^3, per creation event
GD = 4 + 45 * F(175, 100) + 24
GSTAR = F(100)
MPRED = F(2435, 1000) * 10 ** 18
M_CEIL = F(6) * 10 ** 14
ETA = F(274, 10 ** 10) * F(2237, 10 ** 5)
NGS = F(1413, 10 ** 4)
M_P, M_HE4 = F(938272, 1000), F(3727379, 1000)
A0 = F(529, 1000) * F(1, 10 ** 8)
M_H, M_HE = F(167, 100) * F(1, 10 ** 24), F(664, 100) * F(1, 10 ** 24)
# yield coefficient over pi^3: c/pi^3 = 4 A_S + 45 A_F + 12 A_V, each chiral fermion weighted once
C_OVER_PI3 = 4 * A_S + 45 * A_F + 12 * A_V
# Bose and Fermi parts of 17280 c/pi^3 for a copy of the bath (4, 45, 12): per species
# (c_j 148 + 20 tau_j)/225 and 49 x 45 c_j/4800 with c_j = 1, 3, 12 and tau_j = 1, 0, 0
BOSE_PART = F(4 * (148 + 20) + (45 * 3 + 12 * 12) * 148, 225)
FERMI_PART = F((4 + 45 * 3 + 12 * 12) * 49 * 45, 4800)
ZETA_TERMS = 60
# T14c's helium window for xi (a cited input)
HELIUM_WINDOW = (F(3, 10 ** 3), F(2, 10 ** 2))
# a common photon-number normalisation and sample xi for the identity eta' = n_b / (xi^3 n_gamma)
N_GAMMA_SAMPLE = F(411)
XI_SAMPLES = (F(1, 1000), F(3, 10 ** 4), F(1, 7))


def inside(iv, a, b):
    """iv is an interval (lower end <= upper end) lying strictly inside (a, b)."""
    return a < iv[0] <= iv[1] < b


def inside4(iv, a, b):
    """iv is an interval for x^4 (x > 0): the x interval lies strictly inside (a, b)."""
    return a ** 4 < iv[0] <= iv[1] < b ** 4


def scaled(iv, c):
    """The interval iv times a positive rational c."""
    return (iv[0] * c, iv[1] * c)


def scaled4(iv, c):
    """An interval for x^4 rescaled to one for (c x)^4, c > 0."""
    return (iv[0] * c ** 4, iv[1] * c ** 4)


def eta_prime4(iv4):
    """The interval of eta'^4 = (eta / xi^3)^4 = eta^4 / (xi^4)^3 from an interval of xi^4."""
    return (ETA ** 4 / iv4[1] ** 3, ETA ** 4 / iv4[0] ** 3)


def _arctan_bounds(x, terms):
    s = F(0)
    for k in range(terms):
        s += F((-1) ** k) * x ** (2 * k + 1) / (2 * k + 1)
    err = x ** (2 * terms + 1) / (2 * terms + 1)
    return s - err, s + err


def _pi_bounds():
    a_lo, a_hi = _arctan_bounds(F(1, 5), 12)
    b_lo, b_hi = _arctan_bounds(F(1, 239), 4)
    return 16 * a_lo - 4 * b_hi, 16 * a_hi - 4 * b_lo


def _isqrt(m):
    x = 1 << ((m.bit_length() + 1) // 2)        # integer Newton iteration from above
    while True:
        y = (x + m // x) // 2
        if y >= x:
            return x
        x = y


def _sqrt10_bounds():
    k = 10 ** 12
    r = _isqrt(10 * k * k)
    return F(r, k), F(r + 1, k)


def _kappa_bounds():
    plo, phi = _pi_bounds()
    slo, shi = _sqrt10_bounds()
    c = F(40, 27)                       # sqrt(g*/90) (2/45) g* = (sqrt(10)/3)(2/45)(100)
    return plo ** 3 * slo * c, phi ** 3 * shi * c


def _c_bounds():
    plo, phi = _pi_bounds()
    return C_OVER_PI3 * plo ** 3, C_OVER_PI3 * phi ** 3


def _zeta5_bounds():
    s = sum(F(1, n ** 5) for n in range(1, ZETA_TERMS + 1))
    return s + F(1, 4 * (ZETA_TERMS + 1) ** 4), s + F(1, 4 * ZETA_TERMS ** 4)


def _energy_bounds():
    """Mean energy per creation event over T: a Bose pair carries 8 zeta(5)/zeta(4), a Fermi pair
    (60/7) zeta(5)/zeta(4), zeta(4) = pi^4/90, weighted by the Bose and Fermi parts of the rate."""
    plo, phi = _pi_bounds()
    zlo, zhi = _zeta5_bounds()
    w = (8 * BOSE_PART + F(60, 7) * FERMI_PART) / (BOSE_PART + FERMI_PART)
    return w * 90 * zlo / phi ** 4, w * 90 * zhi / plo ** 4


def _xi4_floor(cc):
    klo, khi = _kappa_bounds()
    elo, ehi = _energy_bounds()
    base = F(4, 3) * cc * (M_CEIL / MPRED) ** 3 * GSTAR / (3 * GD)
    return elo * base / khi, ehi * base / klo


def _xi4_floor_interval():
    c_lo, c_hi = _c_bounds()
    return _xi4_floor(c_lo)[0], _xi4_floor(c_hi)[1]


def check_mirror_share_from_mass_per_baryon():
    premise("dark-matter.mirror-share-one-how-fragile")
    premise("dark-matter.mirror-tower-copy-one")
    ok = True
    ours = F(3, 4) * M_P + F(1, 4) * M_HE4 / 4
    ratio = (M_HE4 / 4) / ours
    ok = ok and F(9365, 10) < ours < F(937)
    ok = ok and F(994, 1000) < ratio < F(996, 1000)
    ok = ok and F(514, 10 ** 5) < 1 - ratio < F(516, 10 ** 5)
    GA.check("Omega_b'/Omega_b: 0.995 (helium, ratio in (0.994, 0.996)) to 1 (protons)", ok)
    return ok


def check_temperature_ratio_interval():
    premise("dark-matter.stored-asymmetry-charge-not-number")
    premise("dark-matter.radiation-audit-what-theorem-closes-what")
    ok = True
    c_lo, c_hi = _c_bounds()
    # by hand: (4 x 5789 + 45 x 16087 + 48 x 16087)/82944000 = 1519247/82944000, times pi^3 = 0.56793
    ok = ok and C_OVER_PI3 == F(1519247, 82944000)
    ok = ok and F(5679, 10 ** 4) < c_lo <= c_hi < F(5680, 10 ** 4)
    ok = ok and GD == F(10675, 100)
    floor = _xi4_floor_interval()
    _, hi_hi = floor
    # the Bose and Fermi parts sum to the coefficient, and the mean energy per event is in (7.889, 7.890) T
    ok = ok and BOSE_PART + FERMI_PART == 17280 * C_OVER_PI3
    ok = ok and BOSE_PART == F(41964, 225) and FERMI_PART == F(283 * 2205, 4800)
    ok = ok and inside(_energy_bounds(), F(7889, 1000), F(7890, 1000))
    # the stated floor "6.6 x 10^-4": xi lies in (6.6, 6.7) x 10^-4 and rounds to 6.6 (in (6.55, 6.65))
    ok = ok and inside4(scaled4(floor, 10 ** 5), 66, 67)
    ok = ok and inside4(scaled4(floor, 10 ** 6), 655, 665)
    nbs = ETA * NGS
    # by hand: 612938e-18 x 0.1413 = 866081394e-19 (= 8.66e-11)
    ok = ok and nbs == F(866081394, 10 ** 19)
    xi4_hot = 3 * nbs / F(3, 4) * GSTAR / GD
    # by hand: xi^4 = 400 x 8.6608e-11 / 106.75 = 3.2453e-10, xi = 4.244e-3 ("about 4 x 10^-3")
    ok = ok and inside4(scaled4((xi4_hot, xi4_hot), 10 ** 4), 42, 43)
    ok = ok and hi_hi < xi4_hot
    ok = ok and inside4((xi4_hot, xi4_hot), *HELIUM_WINDOW)
    GA.check("floor xi in (6.6, 6.7)e-4, hot deposit in (4.2, 4.3)e-3, inside (3e-3, 2e-2)", ok)
    return ok


def check_eta_prime():
    premise("dark-matter.stored-asymmetry-charge-not-number")
    ok = True
    n_gamma = N_GAMMA_SAMPLE                           # any common normalisation
    n_b = ETA * n_gamma
    for xi in XI_SAMPLES:
        ok = ok and n_b / (xi ** 3 * n_gamma) == ETA / xi ** 3
    # by hand: 2.74e-8 x 0.02237 = 612938e-18 (= 6.13e-10)
    ok = ok and ETA == F(612938, 10 ** 15)
    # eta' = eta/xi^3 at the floor, through fourth powers: in (2.1, 2.2) (by hand
    # 6.129e-10 / (6.621e-4)^3 = 2.11)
    ok = ok and inside4(scaled4(eta_prime4(_xi4_floor_interval()), 10), 21, 22)
    xi4_hot = 3 * ETA * NGS / F(3, 4) * GSTAR / GD
    # at the hot deposit, by hand 6.129e-10 / (4.244e-3)^3 = 8.02e-3: in (8.0, 8.1) x 10^-3
    ok = ok and inside4(scaled4(eta_prime4((xi4_hot, xi4_hot)), 10 ** 4), 80, 81)
    GA.check("eta' = eta/xi^3: (2.1, 2.2) at the floor, (0.0080, 0.0081) at the hot deposit", ok)
    return ok


def check_atomic_cross_section_per_mass():
    premise("dark-matter.radiation-audit-what-theorem-closes-what")
    ok = True
    plo, phi = _pi_bounds()
    s_lo, s_hi = plo * (2 * A0) ** 2, phi * (2 * A0) ** 2
    # by hand: (1.058e-8)^2 = 1.11936e-16, times pi = 3.5166e-16 cm^2; over m_H = 2.1057e8 and over
    # m_He = 5.2961e7 cm^2/g. Both ends of each interval lie in the one-decimal enclosure.
    ok = ok and inside(scaled((s_lo, s_hi), 10 ** 17), 35, 36)
    ok = ok and inside(scaled((s_lo / M_H, s_hi / M_H), F(1, 10 ** 7)), 21, 22)
    ok = ok and inside(scaled((s_lo / M_HE, s_hi / M_HE), F(1, 10 ** 6)), 52, 53)
    GA.check("sigma = pi (2 a0)^2: sigma/m in (2, 3)e8 (H) and (5, 10)e7 (He) cm^2/g", ok)
    return ok
