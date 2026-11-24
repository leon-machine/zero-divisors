"""synthesis.sheet-relic-bounds-under-e-fix-the-coupling-not-the-cells-mass: exact checks.

The statement is decimal. Every number is redone in exact rational interval arithmetic, as in the
check of dark-tower-matter.survival-sheets: the inputs are decimal constants read as exact rationals,
pi lies in (333/106, 355/113), e in (2718/1000, 2719/1000), and square and cube roots are bracketed
by integer roots at scale 10^12 (each bracket is verified by powering back).

(1) Premise E with V_2 = pi, V_3 = 4 pi/3 gives a sheet tower the mass per unit area
    Sigma = (4/3) rho_b d, with no reference to the cells; at d = d_b it is one nucleon mass per
    disc of radius d_b.
(2) The depletion term 2 P Sigma ln(a_f/a_i)/(m^2 a^2 H) is X = (d/d_b)(m_N/m)^2 times its value
    at the particle model, and with P = (m/e^2)^2 it is 2 Sigma ln(a_f/a_i)/(e^4 a^2 H): the same
    exact number for every m.
(3) Keeping 99 percent (depletion at most 1/99) at g = 3.36, 10.75, 106.75: P X below 2.164e-16,
    1.782e-16 and 1.21e-16; in phase (T) e^2 at least 6.376e7, 7.025e7 and 8.506e7 GeV times
    sqrt(d/d_b); at m = m_N, d = d_b this is m/e^2 below 1.471e-8, 1.335e-8 and 1.102e-8.
(4) Clusters: sigma_eff/m = lambda s/m with lambda = (4/k) sin^2(delta_0), k = m v/2, is X times its
    particle-model value; the bound 1 cm^2/g in a core (overdensity 1e4, z = 0.3, 3000 km/s) gives
    sin^2(delta_0) X below S* = 2.8415e-14, sqrt(S*) = 1.6856e-7; with sin(delta_0) = m/e^2 the mass
    cancels and e^2 exceeds 5.564e6 GeV at d = d_b, more than eleven times below the survival floor.
(5) At P = 1 the bound is on the mass: 8.7e7 GeV passes and 6.3e7 GeV fails at every g, at d = d_b.
(6) The exponent m_5 L/(11 pi) at T = m_5/20 with L = d comoving is kappa d/d_b, kappa = 224 at
    g_s = 106.75, 269 at 61.75 and 481 at 10.75 (whole parts), with no reference to m_5; (d/pi) e^(kappa d/d_b)
    exceeds 1.37e26 m at d = 0.3 m and falls below it at d = 0.1 m for g_s = 10.75, 61.75, 106.75;
    with d at least 0.3 m the floor of (3) is at least 3.52e7 GeV.
"""
from fractions import Fraction as F

import GA
import series
from tp_premise import premise

PI_LO, PI_HI = F(333, 106), F(355, 113)
E_LO, E_HI = F(2718, 1000), F(2719, 1000)
HBARC = F(197327, 10 ** 21)            # GeV m
D_B = F(98, 100)                       # m
T0 = F(27255, 10 ** 4) * F(8617333, 10 ** 20)    # GeV
MP = F(12209, 10 ** 4) * 10 ** 19      # GeV
M_N = F(938, 1000)                     # GeV
LN_AF_AI = F(258, 10)
GS = [F(336, 100), F(1075, 100), F(10675, 100)]
GS_FREEZE = [F(1075, 100), F(6175, 100), F(10675, 100)]
KEEP = F(1, 99)                        # N_f/N_0 >= 99/100
SCALE = 10 ** 12
GRAM_PER_GEV = F(178266192, 10 ** 32)  # g
SPEED = F(3000 * 1000, 299792458)      # 3000 km/s over c
OVERDENSITY, REDSHIFT = 10 ** 4, F(3, 10)
BOUND_CM2_PER_G = F(1)
HUBBLE_RADIUS = F(137, 100) * 10 ** 26  # m
# (cell mass in GeV, common length in m) samples
SAMPLES = [(F(1, 10 ** 6), F(1, 10 ** 9)), (M_N, D_B), (F(50), F(3, 10)), (F(10 ** 7), F(7, 2)), (F(77, 3), F(10 ** 3))]
COUPLINGS = [F(10 ** 8), F(31415, 7), F(5 * 10 ** 6)]
LENGTHS = [D_B, F(3, 10), F(10 ** 3)]
QUARK_MASSES = [F(938, 1000), F(1), F(2000)]
DEPTH_TIMES_T = [F(467), F(1166, 3)]
D_BIG, D_SMALL = F(3, 10), F(1, 10)    # m
UNDER, OVER = F(99, 100), F(101, 100)
E3, E4, E5, E11, E18, E20 = 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 11, 10 ** 18, 10 ** 20


def root_bounds(r, k):
    lo, hi = series.iroot_bracket(r, k, SCALE)
    assert lo ** k <= r < hi ** k
    return lo, hi


def units(lo, hi, unit):
    """The whole number of units in an interval whose two ends agree on it."""
    n_lo, n_hi = (lo * unit).numerator // (lo * unit).denominator, (hi * unit).numerator // (hi * unit).denominator
    assert n_lo == n_hi
    return n_lo


def a2h_bounds(g):
    s_lo, s_hi = root_bounds(g, 2)
    c_lo, c_hi = root_bounds((F(391, 100) / g) ** 2, 3)
    return (F(166, 100) * s_lo * T0 ** 2 * c_lo / MP, F(166, 100) * s_hi * T0 ** 2 * c_hi / MP)


def sigma_times_pi(d):
    """pi times the sheet's mass per unit area, GeV^3: E with V_2 = pi, V_3 = 4 pi/3 and rho_b = 3 m_N/(4 pi d_b^3)."""
    rho_b_pi = 3 * M_N / (4 * D_B ** 3) * HBARC ** 3      # pi rho_b, GeV^4
    return F(4, 3) * rho_b_pi * (d / HBARC)


def depletion_times_pi_a2h(P, m, d):
    """pi a^2 H times the depletion term 2 P Sigma ln(a_f/a_i)/(m^2 a^2 H)."""
    return 2 * P * sigma_times_pi(d) * LN_AF_AI / m ** 2


def depletion_bounds(P, m, d, g):
    lo, hi = a2h_bounds(g)
    x = depletion_times_pi_a2h(P, m, d)
    return x / (PI_HI * hi), x / (PI_LO * lo)


def pmax_bounds(g):
    lo, hi = depletion_bounds(F(1), M_N, D_B, g)
    return KEEP / hi, KEEP / lo


def coupling_floor_bounds(g, d):
    """Interval for c m_N sqrt(d/d_b), GeV: the floor on e^2 in phase (T), and on m at P = 1."""
    p_lo, p_hi = pmax_bounds(g)
    r_lo, r_hi = root_bounds(d / (D_B * p_hi), 2)[0], root_bounds(d / (D_B * p_lo), 2)[1]
    return r_lo * M_N, r_hi * M_N


def check_sheet_density_is_fixed_by_e_alone():
    premise("dark-matter.e-equal-mass-per-unit-ball")
    premise("dark-matter.r3-one-cell-per-unshared-direction")
    premise("dark-matter.projection-every-towers-content-dilutes-ones")
    v2_over_pi, v3_over_pi = F(1), F(4, 3)
    for (_m, d) in SAMPLES:
        rho_b_pi = 3 * M_N / (4 * D_B ** 3) * HBARC ** 3
        # E: Sigma V_2 d^2 = rho_b V_3 d^3 (lengths in GeV^-1)
        dn = d / HBARC
        assert sigma_times_pi(d) * v2_over_pi * dn ** 2 == rho_b_pi * v3_over_pi * dn ** 3
    # at d = d_b: one nucleon mass per disc of radius d_b
    assert sigma_times_pi(D_B) * (D_B / HBARC) ** 2 == M_N
    return True


def check_depletion_scales_as_x_and_the_mass_cancels_in_phase_t():
    premise("dark-tower-matter.three-dimensional-phases")
    base = depletion_times_pi_a2h(F(1), M_N, D_B)
    for (m, d) in SAMPLES:
        x = (d / D_B) * (M_N / m) ** 2
        assert depletion_times_pi_a2h(F(1), m, d) == x * base
    for e2 in COUPLINGS:
        for d in LENGTHS:
            values = {depletion_times_pi_a2h((m / e2) ** 2, m, d) for (m, _d) in SAMPLES}
            assert values == {2 * sigma_times_pi(d) * LN_AF_AI / e2 ** 2}
    return True


def check_phase_t_floor_on_the_coupling():
    # per g: P_max in units of 1e-20 (1e-18 at the last), the floor in GeV in units of 1e4, sqrt(P_max) in 1e-11
    expect = [(E20, 21640, E4, 6376, 1471), (E20, 17827, E4, 7025, 1335), (E18, 121, E4, 8506, 1102)]
    for g, (p_unit, p_n, f_unit, f_n, r_n) in zip(GS, expect):
        p_lo, p_hi = pmax_bounds(g)
        assert units(p_lo, p_hi, p_unit) == p_n
        f_lo, f_hi = coupling_floor_bounds(g, D_B)
        assert units(f_lo, f_hi, F(1, f_unit)) == f_n
        # the particle model's reading, m = m_N: m/e^2 <= sqrt(P_max)
        assert units(root_bounds(p_lo, 2)[0], root_bounds(p_hi, 2)[1], E11) == r_n
        # the floor is a floor: one percent under it the depletion exceeds 1/99, one percent over it does not,
        # for every sample mass
        for (m, _d) in SAMPLES:
            assert depletion_bounds((m / (f_lo * UNDER)) ** 2, m, D_B, g)[0] > KEEP
            assert depletion_bounds((m / (f_hi * OVER)) ** 2, m, D_B, g)[1] < KEEP
    return True


def cluster_quantities(m, d):
    """Exact (spacing bounds in cm, k in 1/cm, m in g) for a core of overdensity 1e4 at z = 0.3."""
    cb_lo, cb_hi = root_bounds(F(OVERDENSITY), 3)
    s_lo = d * 100 / (cb_hi * (1 + REDSHIFT))
    s_hi = d * 100 / (cb_lo * (1 + REDSHIFT))
    k = (m / 2) * SPEED / (HBARC * 100)
    return s_lo, s_hi, k, m * GRAM_PER_GEV


def sin2_bound(m, d):
    """Interval for the largest sin^2(delta_0) with (4/k) sin^2 s/m <= 1 cm^2/g."""
    s_lo, s_hi, k, grams = cluster_quantities(m, d)
    return BOUND_CM2_PER_G * grams * k / (4 * s_hi), BOUND_CM2_PER_G * grams * k / (4 * s_lo)


def check_cluster_bound_scales_as_x_and_loses_the_mass():
    premise("simulations.imported-low-energy-scattering-two-dimensions")
    premise("simulations.imported-bullet-cluster")
    b_lo, b_hi = sin2_bound(M_N, D_B)
    assert units(b_lo, b_hi, E18) == 28415                       # S* = 2.8415e-14
    assert units(root_bounds(b_lo, 2)[0], root_bounds(b_hi, 2)[1], E11) == 16856    # sqrt(S*) = 1.6856e-7
    for (m, d) in SAMPLES:
        x = (d / D_B) * (M_N / m) ** 2
        lo, hi = sin2_bound(m, d)
        assert lo * x == b_lo and hi * x == b_hi
    # sin(delta_0) = m/e^2: (m/e^2)^2 <= bound(m, d) is the same condition on e^2 for every m
    for d in LENGTHS:
        assert len({m ** 2 / sin2_bound(m, d)[0] for (m, _d) in SAMPLES}) == 1
    f_lo, f_hi = M_N * root_bounds(1 / b_hi, 2)[0], M_N * root_bounds(1 / b_lo, 2)[1]
    assert units(f_lo, f_hi, F(1, E3)) == 5564                   # 5.564e6 GeV at d = d_b
    # weaker than the survival floor at every g
    assert all(f_hi * 11 < coupling_floor_bounds(g, D_B)[0] for g in GS)
    return True


def check_full_strength_puts_the_bound_on_the_mass():
    for g in GS:
        assert depletion_bounds(F(1), F(87 * 10 ** 6), D_B, g)[1] < KEEP
        assert depletion_bounds(F(1), F(63 * 10 ** 6), D_B, g)[0] > KEEP
        # and at the nucleon mass the particle model's density is depleted by more than 4e13
        assert depletion_bounds(F(1), M_N, D_B, g)[0] > 4 * 10 ** 13
    return True


def kappa_bounds(g):
    """Interval for kappa in exponent = kappa d/d_b: 20 (d_b T0/hbar c)(3.91/g)^(1/3)/(11 pi)."""
    c_lo, c_hi = root_bounds(F(391, 100) / g, 3)
    lt0 = D_B * T0 / HBARC
    return 20 * lt0 * c_lo / (11 * PI_HI), 20 * lt0 * c_hi / (11 * PI_LO)


def check_one_length_and_the_five_dimensional_depth():
    # the exponent m_5 L/(11 pi) with L = 20 (L T)/m_5 at T = m_5/20 does not contain m_5
    for m5 in QUARK_MASSES:
        for lt in DEPTH_TIMES_T:
            g5sq = 8 / m5                           # g_5^2/pi^3 at the strong-coupling value 8 pi^3/m_5
            depth = 20 * lt / m5
            assert 8 * depth / (11 * g5sq) == 20 * lt / 11          # pi times the exponent
    for g, kappa in zip(GS_FREEZE, (481, 269, 224)):
        k_lo, k_hi = kappa_bounds(g)
        assert units(k_lo, k_hi, F(1)) == kappa
        x_lo = k_lo * D_BIG / D_B
        assert (D_BIG / PI_HI) * E_LO ** (x_lo.numerator // x_lo.denominator) > HUBBLE_RADIUS
        x_hi = k_hi * D_SMALL / D_B
        assert (D_SMALL / PI_LO) * E_HI ** (-((-x_hi.numerator) // x_hi.denominator)) < HUBBLE_RADIUS
    # with d at least 0.3 m the survival floor of the coupling is above 3.4e7 GeV: 3.52e7 at the lowest
    f_lo, f_hi = coupling_floor_bounds(GS[0], D_BIG)
    assert units(f_lo, f_hi, F(1, E5)) == 352
    assert all(coupling_floor_bounds(g, D_BIG)[0] > f_lo * UNDER for g in GS)
    return True
