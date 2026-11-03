"""scrambling.mode-count (version 2): exact check of the count on the (C1) locus.

pi is kept as a formal factor (coefficients are of 4 pi and 8 pi). Along the (C1) locus, parametrised
by rational r_c with 2M := r_c^3, the leading-order slice volume per unit Killing time over 4 pi is
r_c^2 sqrt(2M / r_c) = r_c^2 * r_c (sqrt(r_c^2) = r_c for r_c > 0) = 2M, so the volume is 8 pi M;
with nu modes per cell (C2) the count over a span dt is 8 pi nu M dt, and nu / T_H = 8 pi nu M.
The subleading factor sqrt(1 - r_c/2M) of the T05 count is checked to tend to 1 through
1 - r_c/2M = 1 - r_c^{-2}.
"""
from fractions import Fraction as F
import GA
from GA import pmul, padd, pneg, peval
from tp_premise import premise


def check_mode_count_placement():
    premise("singularity.stretched-singularity-count")
    premise("scrambling.slice-volume-exactly-per-unit-killing")
    # as polynomials in r_c (GA): with 2M := r_c^3, (2M / r_c) * r_c^2 - (r_c^2)^2 = 0 identically,
    # i.e. sqrt(2M / r_c) = r_c along the whole (C1) locus, and r_c^2 * r_c - 2M = 0
    rc_p = [F(0), F(1)]
    rc2 = pmul(rc_p, rc_p)
    twoM_p = pmul(rc2, rc_p)
    assert padd(pmul(rc2, rc2), pneg(pmul(twoM_p, rc_p))) == []
    assert padd(pmul(rc2, rc_p), pneg(twoM_p)) == []
    for rc in (F(2), F(3), F(7, 2), F(10), F(1000)):
        assert peval(twoM_p, rc) == rc ** 3
        twoM = rc ** 3
        M = twoM / 2
        # sqrt(2M / r_c) = r_c exactly on the (C1) locus
        assert (twoM / rc) == rc * rc
        lead_over_4pi = rc * rc * rc            # r_c^2 * sqrt(2M/r_c)
        assert lead_over_4pi == 2 * M           # volume = 4 pi * 2M = 8 pi M
        assert 1 - rc / twoM == 1 - 1 / (rc * rc)   # correction factor squared, -> 1
        for nu in (F(1, 7), F(1, 3), F(2)):
            for dt in (F(1), F(5, 2)):
                N_over_pi = nu * 4 * lead_over_4pi * dt
                assert N_over_pi == 8 * nu * M * dt
            TH_times_pi = 1 / (8 * M)               # T_H = 1/(8 pi M), times pi
            assert nu / TH_times_pi == 8 * nu * M   # dN/dt = nu / T_H, both over pi
    return True
