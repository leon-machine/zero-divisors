"""dark-tower-matter.mirrors-temperature-p2: exact check of the number.

Computable part: the value Delta N_eff = (8/7)(11/4)^(4/3) + 3.044 = 7.45 of a mirror at xi = 1 and
the factor of about 25 by which the bound Delta N_eff < 0.3 excludes it. The P2 reach argument is a
reading of T14's premises and is not computable.

(1) The photon term is derived, not typed: the entropy ratio across e+e- annihilation is
    (2 + (7/8) 4)/2 = 11/4 = (T_gamma/T_nu)^3, and one photon (2 states) against one neutrino
    species ((7/8) 2 states at T_nu) gives rho_gamma/rho_nu1 = (8/7)(11/4)^(4/3); verified in
    cubed form, (rho_gamma/rho_nu1)^3 = (8/7)^3 (11/4)^4, exactly.
(2) Exact bounds: 3.852 < (11/4)^(4/3) < 3.853 (comparing cubes with 14641/256), so the photon
    term is 4.40 to two decimals, Delta N_eff lies in (7.4463, 7.4475) and rounds to 7.45, and
    Delta N_eff / 0.3 lies in (24.8, 24.9): excluded by a factor of about 25.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

NEFF_SM = F(3044, 1000)
BOUND = F(3, 10)
LO, HI = F(3852, 1000), F(3853, 1000)


def check_photon_term_derived():
    premise("dark-matter.mirror-tower-copy-one")
    ratio_entropy = (2 + F(7, 8) * 4) / 2
    assert ratio_entropy == F(11, 4)
    g_gamma, g_nu = 2, F(7, 8) * 2
    # rho_gamma / rho_nu1 = (g_gamma / g_nu) (T_gamma/T_nu)^4, with (T_gamma/T_nu)^3 = 11/4
    cube = (g_gamma / g_nu) ** 3 * ratio_entropy ** 4
    assert cube == F(8, 7) ** 3 * F(11, 4) ** 4
    assert F(11, 4) ** 4 == F(14641, 256)
    return True


def check_delta_neff_and_exclusion():
    premise("dark-matter.mirror-tower-copy-one")
    x3 = F(11, 4) ** 4                       # ((11/4)^(4/3))^3
    assert LO ** 3 < x3 < HI ** 3
    photon_lo, photon_hi = F(8, 7) * LO, F(8, 7) * HI
    # Both ends of each bracket round to the stated figure, so the figure is fixed exactly.
    assert round(100 * photon_lo) == round(100 * photon_hi) == 440                   # 4.40
    tot_lo, tot_hi = photon_lo + NEFF_SM, photon_hi + NEFF_SM
    assert round(100 * tot_lo) == round(100 * tot_hi) == 745                         # 7.45
    assert int(10 * tot_lo / BOUND) == int(10 * tot_hi / BOUND) == 248               # in (24.8, 24.9)
    assert round(tot_lo / BOUND) == round(tot_hi / BOUND) == 25                      # about 25
    return True
