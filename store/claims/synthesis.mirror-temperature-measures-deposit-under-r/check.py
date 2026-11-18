"""synthesis.mirror-temperature-measures-deposit-under-r: exact arithmetic.

xi = T'/T is the mirror-to-visible temperature ratio. Inputs (stored, decimal values written as
exact rationals): the mirror's gravitational floor, at most 6.63e-4 at T_ref = 6e14 GeV, and the
nine-vector tower's, at most 8.12e-4 there (the coefficients proposition's values at the derived
production coefficients and the mean energy per creation event, 6.621e-4 and 8.118e-4, each below
the figure used here; the export is compared with the two
figures below); floor^4 scales as T^3; Premise (R) caps T_desc at alpha, at most
1e13 GeV at either end of Hypothesis (U); baryons per entropy Y_B = 8.7e-11; helium interval
3e-3 <= xi <= 2e-2; Neff cap xi < 0.448. With g = 106.75 in both towers above the electroweak
scale, rho = (pi^2/30) g T^4 and s = (2 pi^2/45) g T^3, so a deposit eps*T per unit charge gives
xi^4 = eps * Y_B * (2/45)/(1/30) = (4/3) Y_B eps, pi cancelling.
"""
from fractions import Fraction as F
import GA
from series import root_rounds_to, rounds_to
from tp_premise import premise


def check_mirror_temperature_measures_deposit():
    premise("neutrino.r-descent-reheats-below-lower-heavy")
    premise("dark-matter.seeding-gravity-floor-dark-towers-temperature")
    co = premise("dark-matter.coefficients-floors-they-give-what-gravity")["cosmo"]()
    premise("dark-matter.stored-asymmetry-charge-not-number")
    premise("dark-tower-matter.mirrors-composition")
    premise("dark-matter.open-channels-their-costs")
    premise("dark-matter.mirror-tower-copy-one")

    t_ref = F(6) * 10 ** 14
    t_cap = F(10) ** 13
    mirror_floor_hi = F(663, 10 ** 6)
    five_dim_floor = F(812, 10 ** 6)
    # the two figures bound the exported floors (xi^8 brackets of the coefficients proposition), which
    # round to 6.621e-4 and 8.118e-4, from above
    assert all(root_rounds_to(f8, 6621, -7, 8) and f8 < mirror_floor_hi ** 8 for f8 in co["floor8"])
    assert all(root_rounds_to(f8, 8118, -7, 8) and f8 < five_dim_floor ** 8 for f8 in co["floor8_nine"])
    yb = F(87, 10 ** 12)
    he_lo, he_hi = F(3, 1000), F(2, 100)
    cap = F(448, 1000)

    # (i) floors under (R): xi^4 scales as T^3
    scale = (t_cap / t_ref) ** 3
    fm4 = mirror_floor_hi ** 4 * scale
    f5_4 = five_dim_floor ** 4 * scale
    # by hand: 6.63e-4 / 60^(3/4) = 3.075e-5 and 8.12e-4 / 60^(3/4) = 3.767e-5, below 3.1e-5 and 3.8e-5
    assert root_rounds_to(fm4, 3075, -8, 4) and fm4 < F(31, 10 ** 6) ** 4
    assert root_rounds_to(f5_4, 3767, -8, 4) and f5_4 < F(38, 10 ** 6) ** 4
    # the mirror's floor sits 97 to 98 times below 3e-3
    assert (97 ** 4) * fm4 < he_lo ** 4 < (98 ** 4) * fm4
    # the nine-vector tower's floor sits 79 to 80 times below 3e-3
    assert (79 ** 4) * f5_4 < he_lo ** 4 < (80 ** 4) * f5_4
    # without (R): the ceiling floor shifts xi^4 at the helium edge by 2.385e-3 (0.221^4), between 2.3e-3
    # and 2.4e-3 and under a quarter of a percent
    rel = mirror_floor_hi ** 4 / he_lo ** 4
    assert rel == F(221, 1000) ** 4 and rounds_to(rel, 2385, -6) and rel < F(24, 10 ** 4) < F(1, 400)
    assert mirror_floor_hi ** 4 * (F(4, 10 ** 13) / t_ref) ** 3 < fm4  # monotone in T

    # (ii) deposit law: xi^4 = (4/3) Y_B eps (pi cancels between rho and s)
    g = F(10675, 100)
    rho_coef, s_coef = F(1, 30) * g, F(2, 45) * g   # times pi^2
    k = yb * s_coef / rho_coef
    assert k == F(4, 3) * yb
    ours = F(3, 4) / yb                              # our energy per unit charge / T_desc
    assert 86 * 10 ** 8 < ours < 87 * 10 ** 8
    assert k * ours == 1                             # equal deposit per charge gives xi = 1

    # (iii) windows for eps = deposit per unit charge in units of T_desc
    eps_lo, eps_hi, eps_cap = he_lo ** 4 / k, he_hi ** 4 / k, cap ** 4 / k
    assert F(69, 100) < eps_lo < F(70, 100)
    assert 1379 < eps_hi < 1380
    assert 347 * 10 ** 6 < eps_cap < 348 * 10 ** 6
    hot = k * 3                                      # T14's hot deposit, 3 T per unit charge
    assert F(43, 10000) ** 4 < hot < F(44, 10000) ** 4 and he_lo ** 4 < hot < he_hi ** 4
    # the floor is negligible inside the window: under (R) it changes xi^4 at the helium edge by less than
    # 2e-8 of its value (and no longer by less than 1e-8)
    # (by hand 1.104e-8 with the figure 6.63e-4)
    assert rounds_to(fm4 / he_lo ** 4, 1104, -11) and fm4 * 10 ** 8 < 2 * he_lo ** 4
    # the lower side from the exported floor itself, not from the figure that bounds it from above:
    # by hand 1.098e-8, above 1e-8
    assert all(root_rounds_to(f8 * scale ** 2 / he_lo ** 8, 1098, -11) for f8 in co["floor8"])
    return True
