"""synthesis.five-dimensional-plasma-exposure-is-one-inequality-in-coupling-mass-and-depth: exact checks.

The statement is decimal. Every number is redone in exact rational interval arithmetic: the inputs are
decimal constants read as exact rationals, pi lies in (333/106, 355/113), and square roots are bracketed
by integer roots at scale 10^12 (each bracket is verified by powering back). A quantity is compared by the
whole number of stated units on which the two ends of its interval agree.

(1) alpha_4 = g_5^2/(4 pi L) with g_5^2 = 8 pi^3/E_s is 2 pi^2/(E_s L): no mass in it. At E_s = 1e11 GeV,
    L = d_b: 3.974e-26.
(2) alpha_4 <= c (m_c/TeV)^2 is E_s m_c^2 (d/d_b) >= K(c), K(c) = 2 pi^2 hbar c TeV^2/(c d_b):
    9.46e15 GeV^3 at c = 4.2e-25 and 5.09e12 GeV^3 at c = 7.8e-22.
(3) Readings: at 1 GeV, d_b the thresholds on E_s are K; a deposit at E_s = 1e11 GeV is over the limits by
    50 and 9.46e4 there; at E_s = 1e11 GeV, d_b the thresholds on m_c are 7.1 GeV and 307 GeV (whole parts);
    m_c^2 E_s d is constant along the threshold.
(4) A tower's share of the dark matter is 8/(11 pi + 16) = 0.158; a limit going as 1/rho relaxes by its
    inverse and the mass thresholds fall by 2.51.
(5) At fixed coupling sigma_eff/m goes as 1/m_c^2; binding needs m_c above 3 E_s/(8 pi) = 0.119 E_s.
(6) The coefficient 7.8e-22 is the square of the charge bound 2.8e-14 per GeV at a TeV; divided by 4 pi it
    is 6.2e-23, K is 6.37e13 GeV^3 and the threshold at E_s = 1e11 GeV is 25 GeV.
"""
from fractions import Fraction as F

import GA
import series
from tp_premise import premise

PI_LO, PI_HI = F(333, 106), F(355, 113)
HBARC = F(197327, 10 ** 21)            # GeV m
D_B = F(98, 100)                       # m
TEV = 10 ** 3                          # GeV
C_STRONG = F(42, 10 ** 26)             # limit coefficient, alpha_4 <= c (m/TeV)^2
C_WEAK = F(78, 10 ** 23)
Q_BOUND = F(28, 10 ** 15)              # charge bound per GeV of mass
E_RUNG = F(10 ** 11)                   # GeV
SCALE = 10 ** 12
E10, E13, E26, E29, E8 = 10 ** 10, 10 ** 13, 10 ** 26, 10 ** 29, 10 ** 8
# (E_s in GeV, m_c in GeV, d in m) samples
SAMPLES = [(F(10 ** 11), F(1), D_B), (F(10 ** 11), F(300), D_B), (F(10 ** 7), F(5000), F(3, 10)),
           (F(10 ** 16), F(1, 2), F(10)), (F(3 * 10 ** 9), F(77), F(7, 2))]
MASSES = [F(1), F(300), F(77, 3)]


def root_bounds(r, k):
    lo, hi = series.iroot_bracket(r, k, SCALE)
    assert lo ** k <= r < hi ** k
    return lo, hi


def units(lo, hi, unit):
    """The whole number of units in an interval whose two ends agree on it."""
    n_lo, n_hi = (lo * unit).numerator // (lo * unit).denominator, (hi * unit).numerator // (hi * unit).denominator
    assert n_lo == n_hi
    return n_lo


def alpha4_over_pi2(e_s, d):
    """alpha_4/pi^2 = 2/(E_s L), L = d/(hbar c) in GeV^-1."""
    return 2 * HBARC / (e_s * d)


def alpha4_bounds(e_s, d):
    a = alpha4_over_pi2(e_s, d)
    return a * PI_LO ** 2, a * PI_HI ** 2


def k_over_pi2(c):
    """K(c)/pi^2, GeV^3: E_s m_c^2 (d/d_b) >= K(c) is alpha_4 <= c (m_c/TeV)^2."""
    return 2 * HBARC * TEV ** 2 / (c * D_B)


def k_bounds(c):
    return k_over_pi2(c) * PI_LO ** 2, k_over_pi2(c) * PI_HI ** 2


def check_zero_mode_coupling_does_not_contain_the_mass():
    premise("dark-matter.e-equal-mass-per-unit-ball")
    premise("dark-matter.r3-one-cell-per-unshared-direction")
    premise("dark-tower-matter.five-dimensional-content")
    for (e_s, _m, d) in SAMPLES:
        g5sq_over_pi3 = 8 / e_s                       # g_5^2 = 8 pi^3/E_s
        depth = d / HBARC                             # GeV^-1
        assert g5sq_over_pi3 / (4 * depth) == alpha4_over_pi2(e_s, d)      # alpha_4/pi^2 = g_5^2/(4 pi L)/pi^2
    lo, hi = alpha4_bounds(E_RUNG, D_B)
    assert units(lo, hi, E29) == 3974                 # 3.974e-26
    return True


def check_the_inequality_and_its_constant():
    for c, unit, n in ((C_STRONG, F(1, E13), 946), (C_WEAK, F(1, E10), 509)):
        k_lo, k_hi = k_bounds(c)
        assert units(k_lo, k_hi, unit) == n
        for (e_s, m, d) in SAMPLES:
            under_limit = alpha4_over_pi2(e_s, d) <= c * (m / TEV) ** 2 / PI_HI ** 2      # safely under
            over_limit = alpha4_over_pi2(e_s, d) > c * (m / TEV) ** 2 / PI_LO ** 2        # safely over
            lhs = e_s * m ** 2 * d / D_B
            if under_limit:
                assert lhs >= k_hi
            if over_limit:
                assert lhs < k_lo
            # the two forms are one statement: alpha_4/(c (m/TeV)^2) = K/(E_s m^2 d/d_b), exactly
            assert alpha4_over_pi2(e_s, d) / (c * (m / TEV) ** 2) == k_over_pi2(c) / lhs
    return True


def check_readings_at_one_gev_and_at_the_rung_scale():
    for c, excess_unit, excess, mass_unit, mass in ((C_STRONG, F(1, 100), 946, F(1), 307), (C_WEAK, F(1), 50, F(10), 71)):
        k_lo, k_hi = k_bounds(c)
        # at m_c = 1 GeV, d = d_b the threshold on E_s is K; a deposit at the rung scale is over the limit by K/E_s
        assert units(k_lo / E_RUNG, k_hi / E_RUNG, excess_unit) == excess
        # at E_s = 1e11 GeV, d = d_b the threshold on m_c is sqrt(K/E_s)
        m_lo, m_hi = root_bounds(k_lo / E_RUNG, 2)[0], root_bounds(k_hi / E_RUNG, 2)[1]
        assert units(m_lo, m_hi, mass_unit) == mass
        # along the threshold m_c^2 E_s d is constant
        for (e_s, _m, d) in SAMPLES:
            assert (k_over_pi2(c) * D_B / (e_s * d)) * e_s * d == k_over_pi2(c) * D_B
    return True


def check_a_tower_share_relaxes_the_limit():
    # share of one five-dimensional tower: (8/(3 pi))/((11 pi + 16)/(3 pi)) = 8/(11 pi + 16)
    f_lo, f_hi = 8 / (11 * PI_HI + 16), 8 / (11 * PI_LO + 16)
    assert units(f_lo, f_hi, F(1000)) == 158
    r_lo, r_hi = root_bounds(1 / f_hi, 2)[0], root_bounds(1 / f_lo, 2)[1]
    assert units(r_lo, r_hi, F(100)) == 251           # mass thresholds fall by 2.51
    return True


def check_short_range_bound_and_binding():
    # sigma_5 = 100 beta^2/(mu v)^3, beta = m g C_F/(4 pi^2), mu = m/2; sigma_eff/m = sigma_5/(L m)
    cf, g, v, depth = F(4, 3), F(1, 7), F(1, 1000), F(5)
    def sigma_eff_over_m_pi4(m):
        beta_pi2 = m * g * cf / 4
        return 100 * beta_pi2 ** 2 / ((m / 2) * v) ** 3 / (depth * m)
    base = sigma_eff_over_m_pi4(MASSES[0])
    for m in MASSES:
        assert sigma_eff_over_m_pi4(m) * m ** 2 == base * MASSES[0] ** 2
    # binding: m g_5^2 C_F >= 4 pi^2 with g_5^2 = 8 pi^3/E_s is m >= 3 E_s/(8 pi)
    b_lo, b_hi = 3 * E_RUNG / (8 * PI_HI), 3 * E_RUNG / (8 * PI_LO)
    assert units(b_lo, b_hi, F(1, E8)) == 119         # 1.19e10 GeV at E_s = 1e11 GeV
    assert (8 / E_RUNG) * b_lo * cf / 4 < 1 / PI_LO and (8 / E_RUNG) * b_hi * cf / 4 > 1 / PI_HI
    return True


def check_the_weaker_coefficient_is_the_square_of_the_charge_bound():
    c_from_q = Q_BOUND ** 2 * TEV ** 2                # (q per GeV)^2 at a TeV
    assert units(c_from_q, c_from_q, F(10 ** 23)) == 78 and units(C_WEAK, C_WEAK, F(10 ** 23)) == 78
    # with alpha = q^2/(4 pi) the coefficient is 4 pi smaller
    c_lo, c_hi = c_from_q / (4 * PI_HI), c_from_q / (4 * PI_LO)
    assert units(c_lo, c_hi, F(10 ** 24)) == 62       # 6.2e-23
    k_lo, k_hi = k_over_pi2(c_hi) * PI_LO ** 2, k_over_pi2(c_lo) * PI_HI ** 2
    assert units(k_lo, k_hi, F(1, 10 ** 12)) == 63    # 6.37e13 GeV^3
    m_lo, m_hi = root_bounds(k_lo / E_RUNG, 2)[0], root_bounds(k_hi / E_RUNG, 2)[1]
    assert units(m_lo, m_hi, F(1)) == 25              # 25 GeV at the rung scale
    return True
