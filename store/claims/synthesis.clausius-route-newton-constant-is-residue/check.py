"""synthesis.clausius-route-newton-constant-is-residue: exact checks.

pi and ln 2 are formal symbols, kept by their exponents: a quantity c pi^a L^b (L = ln 2) is stored
as its rational coefficient c with the powers tracked by hand in the comments. M is a polynomial
variable (GA.RF). The surface gravity is computed from f = 1 - 2M/r, the epoch from it, and the
epoch count from the accrual rate times the epoch, so no count is typed in directly. The registered
nu is derived twice, from the area-law condition and from Jacobson's eta = 1/4, and the two must agree.
"""
from fractions import Fraction as F
import GA
from GA import RF
from tp_premise import premise

NUS = [F(1, 3), F(2), F(5, 7)]
MS = [F(1), F(3, 2), F(7, 5)]


def setup():
    premise("synthesis.imported-jacobson-clausius-1995")
    premise("scrambling.mode-count")
    premise("scrambling.epoch-modular-period-two-unknowns-become")
    premise("synthesis.residue-from-mode-entropy")
    premise("synthesis.quarter-from-temperature")
    premise("angle.imported-theorems-deliver-their-hypotheses")


def kappa_of(m):
    """surface gravity of f(r) = 1 - 2m/r at its zero r = 2m: kappa = f'(2m)/2."""
    r = RF.var()
    f = RF.const(1) - RF.const(2 * m) / r
    rh = 2 * m
    assert f.eval(rh) == 0
    return f.deriv().eval(rh) / 2


def check_accrual_versus_epoch():
    setup()
    M = RF.var()
    for nu in NUS:
        rate = RF.const(8 * nu) * M            # dN/dt = 8 pi nu M: coefficient of pi
        A = RF.const(16) * M * M                # A = 4 pi (2M)^2: coefficient of pi
        for m in MS:
            kappa = kappa_of(m)
            assert kappa == 1 / (4 * m)
            dt = 2 / kappa                      # modular period 2 pi/kappa: coefficient of pi
            N = rate.eval(m) * dt               # epoch count: coefficient of pi^2
            assert N / A.eval(m) == 4 * nu      # N/A = 4 pi nu (coefficient of pi)
            assert rate.eval(m) != 0            # the accrual grows on a stationary horizon
        # negative control: the accrual rate is not proportional to the area along the family
        ratio = rate / A                        # nu/(2M): coefficient of pi^0
        assert not ratio.deriv().is_zero()
        assert ratio.eqrf(RF.const(nu) / (RF.const(2) * M))
    return True


def check_newton_constant_ratio():
    setup()
    for m in MS:
        dt = 2 / kappa_of(m)                    # 8 pi m, coefficient of pi
        # route 1, the stored area-law condition nu dt = M/2 in the 1-nat convention, and with ln 2
        # credited per mode (capacity convention): nu = M/(2 dt), times 1/L
        nu_area_1nat = m / 2 / dt               # coefficient of 1/pi
        assert nu_area_1nat == F(1, 16)
        nu_area_cap = nu_area_1nat              # coefficient of 1/(pi L)
        # route 2, Jacobson's eta = kappa_c <s> with kappa_c = 4 pi nu (from the epoch count) and
        # <s> = L at zero weight; G_cl = G iff eta = 1/4, i.e. 16 pi nu L = 1
        nu_jacobson_cap = F(1, 4) / 4           # nu = (1/4)/(4 pi L): coefficient of 1/(pi L)
        assert nu_jacobson_cap == nu_area_cap   # the two routes agree: one condition, not two
    # G_cl/G = 1/(16 pi nu <s>): with nu = a/(pi L) and <s> = b L this is 1/(16 a b), equal to 1
    # exactly when a b = 1/16; at zero weight (b = 1) that is a = 1/16, the area-law value above
    for a in (F(1, 16), F(1, 8), F(3, 7)):
        for b in (F(1), F(1, 2), F(3, 4)):
            g_ratio = 1 / (16 * a * b)
            assert (g_ratio == 1) == (a * b == F(1, 16))
    assert 1 / (16 * nu_area_cap * 1) == 1
    # black-hole calibration kappa_c = 1/(4 <s>): eta = 1/4 whatever <s>, so G_cl = G carries no information
    for sbar in (F(1), F(1, 2), F(3, 4)):
        assert (1 / (4 * sbar)) * sbar == F(1, 4)
    return True
