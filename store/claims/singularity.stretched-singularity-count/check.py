"""singularity.stretched-singularity-count: exact checks of the slice volume and the mode rate.

pi is carried as a formal factor (the identities are compared after dividing by pi, or squared with
pi^2 cancelled); square roots are handled by comparing squares of nonnegative quantities.
(1) Induced geometry, blade-exact in Cl(1,3) (GA): the Painleve-Gullstrand physical-vector map
    hbar^{-1}(a) = a + beta (a . e_t) e_r gives g(e_t, e_t) = 1 - beta^2 = f, g(e_t, e_r) = -beta,
    g(e_r, e_r) = -1 at rational beta (beta^2 = 2M/r); inside the horizon (beta > 1) g_tt = f < 0, so the
    Killing direction is spacelike on r = const with |f| = 2M/r - 1.
(2) Slice volume, as rational-function identities: r^4 |f(r)| = 2M r^3 (1 - r/2M) in r for several M (the
    square of 4 pi r^2 sqrt|f| = 4 pi sqrt(2M) r^{3/2} sqrt(1 - r/2M)); along the whole (C1) locus,
    parametrised by an indeterminate c = r_c with 2M = c^3, 2M r_c^3 = (2M)^2, so the volume squared over
    (4 pi)^2 is (2M)^2 (1 - r_c/2M) (that is 8 pi M sqrt(1 - r_c/2M)); r_c/2M = c^{-2} = (2M)^{-2/3}; and
    (1 - r_c/2M) - 1 = -c^{-2}, the O(M^{-2/3}) correction.
(3) The rate: kappa = f'(2M)/2 = 1/(4M) from the derivative of f, T_H = kappa/(2 pi) = 1/(8 pi M), so
    (dN/dt / pi)^2 = (nu vol / pi)^2 = (nu/(pi T_H))^2 (1 - r_c/2M) along (C1) for several nu.
(4) Control: a mass-independent cutoff radius r_0 gives a squared volume of degree 1 in M (scaling M^{1/2})
    that differs from the linear-in-M form, as rational functions of M.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

STA = (1, -1, -1, -1)
BETAS_OUT = [F(3, 7), F(1, 2), F(5, 6)]
BETAS_IN = [F(7, 3), F(2), F(9, 4)]
MASSES = [F(1), F(5, 2), F(7, 3)]
NUS = [F(1), F(3), F(2, 7)]
R0 = F(9, 4)
# Sample radii r_c on the (C1) locus at which the squared volume is evaluated.
RC_SAMPLES = (F(2), F(3), F(10))


def metric(beta):
    et, er = GA.gen(0), GA.gen(1)

    def him(a):
        return GA.add(a, GA.scal(beta * GA.dot(a, et, STA), er))

    return lambda a, b: GA.dot(him(a), him(b), STA), et, er


def check_induced_metric_on_the_slice():
    premise("singularity.imported-induced-geometry-interior-slice")
    for beta in BETAS_OUT + BETAS_IN:
        g, et, er = metric(beta)
        assert g(et, et) == 1 - beta * beta
        assert g(et, er) == -beta and g(er, er) == -1
        for M in MASSES:
            r = 2 * M / (beta * beta)
            f = 1 - 2 * M / r
            assert g(et, et) == f
            if beta > 1:
                assert f < 0 and -f == 2 * M / r - 1
            else:
                assert f > 0


def check_slice_volume_identities():
    premise("singularity.c1-curvature-cutoff")
    r = GA.RF.var()
    one = GA.RF1
    for M in MASSES:
        twoM = GA.RF.const(2 * M)
        absf = twoM / r - one
        lhs = r * r * r * r * absf
        rhs = twoM * r * r * r * (one - r / twoM)
        assert lhs.eqrf(rhs)
        assert absf.eval(2 * M) == 0                   # the horizon r = 2M, where f vanishes
    c = GA.RF.var()
    twoM = c * c * c
    absf = twoM / c - one
    vol_sq = c * c * c * c * absf                      # (volume / 4 pi)^2 = r_c^4 |f(r_c)|
    assert (twoM * c * c * c).eqrf(twoM * twoM)
    assert vol_sq.eqrf(twoM * twoM * (one - c / twoM))
    ratio = c / twoM
    assert ratio.eqrf(one / (c * c))
    assert (ratio * ratio * ratio).eqrf(one / (twoM * twoM))
    corr = (one - c / twoM) - one
    assert corr.eqrf(GA.RF.const(-1) / (c * c))
    # at sample radii: (volume / 4 pi)^2 = (2M)^2 (1 - r_c/2M) with 2M = r_c^3, that is r_c^6 - r_c^4
    # (so 0 < 1 - r_c/2M = 1 - r_c^-2 < 1 for r_c > 1)
    for rc in RC_SAMPLES:
        v = vol_sq.eval(rc)
        twoM_v = rc ** 3
        assert v == twoM_v * twoM_v * (1 - rc / twoM_v) and v == rc ** 6 - rc ** 4


def check_mode_rate_keeps_hawking_time():
    premise("singularity.c2-cell-density")
    premise("singularity.modular-descent")
    r = GA.RF.var()
    one = GA.RF1
    for M in MASSES:
        f = one - GA.RF.const(2 * M) / r
        kappa = f.deriv().eval(2 * M) / 2
        assert kappa == 1 / (4 * M)
        T_H_times_pi = kappa / 2                       # pi T_H = kappa / 2 (pi formal)
        assert 1 / T_H_times_pi == 8 * M
    c = GA.RF.var()
    twoM = c * c * c
    absf = twoM / c - one
    for nu in NUS:
        rate_sq = GA.RF.const(16 * nu * nu) * c * c * c * c * absf        # (dN/dt / pi)^2
        inv_piT = GA.RF.const(4) * twoM                                     # 1/(pi T_H) = 8 M = 4 (2M)
        assert rate_sq.eqrf(GA.RF.const(nu * nu) * inv_piT * inv_piT * (one - c / twoM))


def check_fixed_cutoff_radius_fails():
    m = GA.RF.var()
    r0 = GA.RF.const(R0)
    two = GA.RF.const(2)
    vol_sq = r0 * r0 * r0 * r0 * (two * m / r0 - GA.RF1)
    assert len(vol_sq.num) - 1 == 1 and len(vol_sq.den) == 1
    area_form = (two * m) * (two * m) * (GA.RF1 - r0 / (two * m))
    assert not vol_sq.eqrf(area_form)
    assert len(area_form.num) - len(area_form.den) == 2
