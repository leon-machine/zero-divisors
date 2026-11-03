"""synthesis.seeding-remainder-excludes-perturbative-pati-salam: exact checks.

All quantities in GeV, as exact rationals. Inputs are the stored record-level values, each
taken at the end of its rounding or error interval that weakens the conclusion:
remainder over the baryons 4.364 - 0.065, baryons per unit entropy 8.65e-11 (8.7e-11 rounded),
kappa_s = 145.3, reduced Planck mass 2.435e18, v_R = 4.25e10 (4.2e10 rounded), 4 pi with
pi < 355/113, m_3 = 49.4 meV, m_b = 4.23 GeV. The proton mass 0.938272 GeV is the PDG value.
Square and fourth roots are never taken: every comparison is made between fourth powers,
and the stated values are pinned by exact floors.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise


def floor(x):
    return x.numerator // x.denominator


def gauge_dimension(a, b, over_c):
    return a * a + b * b - 1 if over_c else (a * (a - 1) + b * (b - 1)) // 2


def check_seeding_remainder_excludes_perturbative_pati_salam():
    premise("dark-matter.seeding-gravity-floor-dark-towers-temperature")
    premise("dark-matter.imported-massless-graviton-production-rate")
    premise("dark-matter.population-count-one-share-half-percent")
    premise("dark-matter.coefficients-floors-they-give-what-gravity")
    premise("standard-model.what-angle-asks-neutrino-sector")
    premise("standard-model.chain")
    premise("dark-matter.ceiling-valued-inherited-success")
    premise("neutrino.r-descent-reheats-below-lower-heavy")
    premise("synthesis.gauge-algebra-by-tower")
    E = F(10)
    rem = F(4364, 1000) - F(65, 1000)
    eta = F(865, 100) / E ** 11
    mp = F(938272, 10 ** 6)
    kappa = F(1453, 10)
    MP = F(2435, 1000) * E ** 18
    vR = F(425, 100) * E ** 10
    pi_hi = F(355, 113)
    m3 = F(494, 10) / E ** 12
    mb = F(423, 100)

    # kappa_s from its formula at g = g_s = 100: kappa^2 = (pi^2 g/90)(2 pi^2 g_s/45)^2
    for pi in (F(333, 106), pi_hi):
        k2 = pi ** 2 * 100 / 90 * (2 * pi ** 2 * 100 / 45) ** 2
        assert (k2 - kappa ** 2) ** 2 < 400

    # A = c T_seed^4 (no factor 2): 3 kappa M_P^3 times the remainder's mass per unit entropy
    A = 3 * kappa * MP ** 3 * rem * mp * eta
    assert floor(A / E ** 44) == 21958
    assert (F(1217, 1000) * E ** 12) ** 4 < A < (F(1218, 1000) * E ** 12) ** 4

    # (i) Pati-Salam chain, f_J <= 4 pi, T_desc <= M_3
    M3_ps = 4 * pi_hi * vR
    assert floor(M3_ps / E ** 8) == 5340
    c_star = A / (2 * M3_ps ** 4)
    assert floor(c_star * 10 ** 4) == 134949
    assert floor(c_star / F(23, 10000)) == 5867

    dims = [gauge_dimension(2, 2, False), gauge_dimension(2, 2, False),
            gauge_dimension(1, 3, True), gauge_dimension(1, 3, True)]
    assert dims == [2, 2, 9, 9]
    c_vec = sum(dims) * F(23, 10000)
    c_four_sm = 4 * F(78, 1000)
    assert c_vec == F(506, 10000) and c_four_sm == F(312, 1000)
    assert A / (2 * c_four_sm) > (F(256, 100) * M3_ps) ** 4
    assert A / (2 * c_vec) > (F(404, 100) * M3_ps) ** 4
    assert A / (2 * c_four_sm) > (F(136, 100) * E ** 12) ** 4
    assert A / (2 * c_four_sm) > (32 * vR) ** 4
    assert (F(82, 10) ** 2 / m3) ** 4 < A / (2 * c_four_sm)
    assert m3 * M3_ps < F(52, 10) ** 2
    # one-loop M_I of the same chain over the two-loop value exceeds the tolerance 2.56
    assert floor(F(32, 10) * E ** 11 / (F(19, 10) * E ** 10)) == 16

    # (ii) bottom end of (U): M_3 = m_b^2 / m_3
    M3_b = mb ** 2 / m3
    assert floor(M3_b / E ** 8) == 3622
    assert floor(A / (2 * M3_b ** 4) * 1000) == 63789

    # (iii) top end of (U), low-scale reading
    M3_t = F(17228, 100) ** 2 / (F(505, 10) / E ** 12)
    assert floor(M3_t / E ** 11) == 5877
    assert (M3_t / 66) ** 4 > A / c_vec
    assert M3_t / vR > 4 * pi_hi * 1000
    # ceiling reading (both ends lowered by 10): T_desc <= M_3 still met, the /66 clause fails
    assert (M3_t / 10) ** 4 > A / c_vec
    M3_t_hi = F(17286, 100) ** 2 / m3
    assert M3_t_hi < F(61, 10) * E ** 14
    assert (M3_t_hi / 660) ** 4 < A / (2 * c_vec)

    # the chain's Dirac mass at f_J = 1: m_D^2 = m_3 v_R at 50 meV and 4.2e10 lies in (1.44^2, 1.45^2)
    md2 = F(50, 1000) / E ** 9 * F(42, 10) * E ** 10
    assert F(144, 100) ** 2 < md2 < F(145, 100) ** 2
    return True
