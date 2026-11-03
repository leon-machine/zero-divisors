"""singularity.area-law-test: exact checks of the capacity calibration and the scalings.

pi is a formal factor (quantities are divided by pi); ln 2 is carried as an indeterminate L (GA.RF), so
every identity below holds for the actual value of ln 2 because it holds identically in L.
(1) With dN/dt = 8 pi nu M at leading order, C = N L = 8 pi M (nu Delta t) L. As a polynomial in
    x = nu Delta t, C - 4 pi M^2 = 8 pi M L x - 4 pi M^2 is linear with nonzero slope, and its unique
    root is x = M/(2L): C = S_BH = 4 pi M^2 iff nu Delta t = M/(2 ln 2), for several M; then
    N = S_BH/L. The former calibration nu Delta t = M/2 gives C = 4 pi M^2 L, off by exactly ln 2.
(2) Leading order: along the (C1) locus 2M = c^3 the exact rate carries sqrt(1 - r_c/2M), whose square
    is 1 - c^{-2}, so C_exact^2 / C_leading^2 -> 1. The calibration is an epoch of order one Schwarzschild
    time: with Delta t = M k (k independent of M, the causal epoch of the counted crossing), the implied
    nu = (M/(2L))/(M k) is the same rational function of L for every M.
(3) Lifetime counting: with dN/dt of degree 1 in M and a lifetime of degree 3, N has degree 4; the
    Christodoulou-Rovelli rate dV/dv of degree 2 gives V of degree 5 (degrees of polynomials in M).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

MASSES = [F(3, 2), F(5), F(1, 7), F(12)]
K_EPOCH = [F(2), F(7, 3)]


def check_capacity_matches_entropy_iff_calibration():
    premise("singularity.stretched-singularity-count")
    premise("singularity.c2-cell-density")
    L = GA.RF.var()
    for M in MASSES:
        Mc = GA.RF.const(M)
        slope = GA.RF.const(8) * Mc * L                     # C/pi = slope * x
        target = GA.RF.const(4) * Mc * Mc                   # S_BH/pi
        x_root = target / slope
        assert x_root.eqrf(Mc / (GA.RF.const(2) * L))
        assert not slope.is_zero()
        cap_new = slope * x_root
        assert cap_new.eqrf(target)
        N = GA.RF.const(8) * Mc * x_root                     # N/pi
        assert N.eqrf(target / L)
        cap_old = slope * (Mc / GA.RF.const(2))
        assert cap_old.eqrf(target * L) and not cap_old.eqrf(target)


def check_leading_order_and_epoch_scale():
    premise("singularity.c1-curvature-cutoff")
    premise("singularity.c3-counted-epoch")
    premise("singularity.causal-epoch-computed-exactly")
    c = GA.RF.var()
    twoM = c * c * c
    ratio_sq = GA.RF1 - c / twoM
    assert ratio_sq.eqrf(GA.RF1 - GA.RF1 / (c * c))
    for rc in (F(10), F(100), F(1000)):
        assert 1 - ratio_sq.eval(rc) == 1 / rc ** 2
    L = GA.RF.var()
    for k in K_EPOCH:
        nus = []
        for M in MASSES:
            Mc = GA.RF.const(M)
            nus.append((Mc / (GA.RF.const(2) * L)) / (Mc * GA.RF.const(k)))
        assert all(v.eqrf(nus[0]) for v in nus)
        assert nus[0].eqrf(GA.RF1 / (GA.RF.const(2 * k) * L))


def check_lifetime_scalings():
    m = GA.RF.var()
    rate = GA.RF.const(8) * m                       # dN/dt / (pi nu)
    lifetime = GA.RF.const(F(5120, 1)) * m * m * m  # evaporation lifetime ~ M^3 (coefficient immaterial)
    N_life = rate * lifetime
    assert len(N_life.num) - 1 == 4 and len(N_life.den) == 1
    cr_rate = GA.RF.const(3) * m * m                 # dV/dv ~ M^2
    V_life = cr_rate * lifetime
    assert len(V_life.num) - 1 == 5 and len(V_life.den) == 1
    assert (len(V_life.num) - 1) - (len(N_life.num) - 1) == 1
