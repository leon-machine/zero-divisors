"""simulations.confinement-scale-does-not-matter: exact interval checks.

The interval arithmetic (rational brackets of pi and gamma, series bounds on logarithms, integer
square roots) and the stated wave number k = 0.0238 fm^-1 come from the cluster-bound computation's
check through premise() EXPORTS.

Rounded statements are checked as: both ends of the computed interval round to the stated value.
(1) A hard disk of radius a = 10^-30 fm: ln(ka/2) = -73.5, and the logarithmic form
    lambda = pi^2/(k (ln(ka/2) + gamma)^2) = 0.08 fm.
(2) sigma_eff = lambda s is linear in lambda at fixed spacing, so the table's floor 9.5 x 10^7 cm^2/g
    at lambda = 0.21 fm becomes at least 9.5 x 10^7 x lambda/0.21 = 3.5 x 10^7 > 3 x 10^7 cm^2/g:
    still a fluid. The table's isotropic value is reproduced: 0.21 fm x 3.5 cm / m_N = 4.4 x 10^10.
(3) The size enters only through the logarithm: lambda at a = 10^-100 fm (ln(ka/2) + gamma < -200)
    is 7.6 x 10^-3 fm (ln(ka/2) = -234.7), which still exceeds the cluster bound on lambda by more than 10^8 (1.6 x 10^9) (the bound is reached only near
    log10(a/fm) = -4 x 10^6, as the cluster-bound check computes): no physical confinement scale.
(4) Phase-shift limits: the isotropic one, sqrt(k lambda_max/4), is about 2 x 10^-7 (one figure);
    the normal-compression one is larger by sqrt(4.4 x 10^10/9.5 x 10^7), about 22, giving about
    4 x 10^-6.
The table values 9.5 x 10^7 and 4.4 x 10^10 cm^2/g are inputs from the paper's table.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

TABLE_NORMAL = F(95, 10) * 10 ** 7          # cm^2/g at lambda = 0.21 fm, normal compression
TABLE_ISO = F(44, 10) * 10 ** 10            # cm^2/g at lambda = 0.21 fm, isotropic
LAMBDA_TABLE = F(21, 100)                   # fm
A_SMALL = F(1, 10 ** 30)                    # fm
A_TINY = F(1, 10 ** 100)                    # fm


def scaled(iv, c):
    """The interval iv multiplied by a positive rational c."""
    return (iv[0] * c, iv[1] * c)


def check_tiny_composite_still_scatters():
    X = premise("simulations.cluster-bound-two-dimensions")
    premise("simulations.imported-low-energy-scattering-two-dimensions")
    k = X["K"]
    rnd = X["rounded"]
    assert rnd(X["ln_iv"](k * A_SMALL / 2), 10) == F(-735, 10)
    assert rnd(X["log_form_lambda"](k, A_SMALL), 100) == F(8, 100)
    return True


def check_still_a_fluid():
    X = premise("simulations.cluster-bound-two-dimensions")
    premise("simulations.effective-cross-section-sheet-matter")
    k = X["K"]
    lam = X["log_form_lambda"](k, A_SMALL)
    floor = (TABLE_NORMAL * lam[0] / LAMBDA_TABLE, TABLE_NORMAL * lam[1] / LAMBDA_TABLE)
    assert floor[0] > 3 * 10 ** 7
    assert X["rounded"]((floor[0] / 10 ** 6, floor[1] / 10 ** 6), 1) == 35
    iso = LAMBDA_TABLE / X["FM_PER_CM"] * X["S_CORE_CM"] / X["M_N_G"] / 10 ** 10
    assert X["rounded"]((iso, iso), 10) == F(44, 10)
    return True


def check_size_enters_only_through_the_log():
    X = premise("simulations.cluster-bound-two-dimensions")
    premise("simulations.imported-low-energy-scattering-two-dimensions")
    k = X["K"]
    L = X["ln_iv"](k * A_TINY / 2)
    # by hand: ln(0.0238/2) - 100 ln 10 = -4.431 - 230.259 = -234.69 (so ln(ka/2) + gamma < -200)
    assert X["rounded"](L, 10) == F(-2347, 10)
    lam = X["log_form_lambda"](k, A_TINY)
    assert X["rounded"](lam, 10 ** 4) == F(76, 10 ** 4)
    # by hand: 7.57e-3 fm / 4.78e-12 fm = 1.58e9, so lambda exceeds the cluster bound by more than 10^8
    ratio = scaled(lam, 1 / X["lambda_max_fm"]())
    assert X["rounded"](scaled(ratio, F(1, 10 ** 9)), 10) == F(16, 10)
    return True


def check_phase_shift_limits():
    X = premise("simulations.cluster-bound-two-dimensions")
    premise("simulations.effective-cross-section-sheet-matter")
    k, lmax = X["K"], X["lambda_max_fm"]()
    rnd = X["rounded"]
    iso = X["sqrt_iv"]((k * lmax / 4, k * lmax / 4))
    assert rnd((iso[0] * 10 ** 7, iso[1] * 10 ** 7), 1) == 2
    ratio = TABLE_ISO / TABLE_NORMAL
    fac = X["sqrt_iv"]((ratio, ratio))
    assert rnd(fac, 1) == 22
    normal = (iso[0] * fac[0], iso[1] * fac[1])
    assert rnd((normal[0] * 10 ** 6, normal[1] * 10 ** 6), 1) == 4
    return True
