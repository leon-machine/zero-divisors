"""dark-tower-matter.survival-sheets: exact checks (rational interval arithmetic).

The statement is decimal; the source's estimate (verify_T14c K3, K4, in decimals) is redone with
exact rational intervals: the inputs are the source's decimal constants read as exact rationals,
pi lies in (333/106, 355/113), and square and cube roots are bracketed by integer roots at scale
10^12 (each bracket is verified by powering back).
(1) The depletion law: with x = ln a, sigma_1 v = 2P/m and a^2 H constant (radiation domination,
    number per area and H both falling as a^-2), the rate equation dN/dx = -k N^2,
    k = (2P/m)/(a^2 H), is solved by 1/N = 1/N_0 + k x: verified as an identity of rational
    functions of x (GA.RF) for sample N_0, k; and with n = N a^-2, H = h a^-2 the sheet rate
    equation dn/dt = -2 H n - sigma v n^2 reduces to it exactly when h k = sigma v (checked at
    rational sample points).
(2) The numbers: N_0 = (hbar c)^2/(pi d_b^2) (R2's density, one quantum per disc of radius d_b),
    a^2 H = 1.66 sqrt(g*) T_0^2 (3.91/g_s)^(2/3)/M_P, ln(a_f/a_i) = 25.8, m = 0.938 GeV, at
    g = 3.36, 10.75, 106.75. Keeping 99 percent (N_f/N_0 >= 99/100, i.e. depletion term <= 1/99)
    needs P below a bound in (1.2e-16, 2.2e-16) at every g, so P of order 2e-16 or less; at P = 1
    the surviving fraction lies in (1e-14, 2.5e-14).
(3) Phase (T): contact processes scale as (m/e^2)^2, so (m/e^2)^2 <= 2e-16 needs
    e^2/m >= 1/sqrt(2e-16), which lies in (7.0e7, 7.1e7); the collisionless threshold
    1/(1.7e-7) lies in (5.85e6, 5.9e6) and is smaller, so the surviving relic is collisionless.
    "Phase (C) fails R2 by itself" is not computable here (it rests on the imported confinement).
"""
from fractions import Fraction as F

import GA
import series
from tp_premise import premise

PI_LO, PI_HI = F(333, 106), F(355, 113)
HBARC = F(197327, 10 ** 21)            # GeV m
D_B = F(98, 100)                       # m
T0 = F(27255, 10 ** 4) * F(8617333, 10 ** 20)    # GeV
MP = F(12209, 10 ** 4) * 10 ** 19      # GeV
MASS = F(938, 1000)                    # GeV
LN_AF_AI = F(258, 10)
GS = [F(336, 100), F(1075, 100), F(10675, 100)]
SCALE = 10 ** 12
# Sample (N_0, k) for the closed-form solution of dN/dx = -k N^2.
DEPLETION_SAMPLES = [(F(3), F(1, 7)), (F(1, 2), F(5)), (F(10), F(2, 3))]
# Sample (a, N, h, sigma v) for the reduction of the sheet rate equation to dN/dx = -k N^2.
SHEET_SAMPLES = [(F(2), F(3), F(5), F(7)), (F(1, 3), F(1, 2), F(2), F(9, 4))]


def root_bounds(r, k):
    """(lo, hi) with lo^k <= r < hi^k, width 1/SCALE."""
    lo, hi = series.iroot_bracket(r, k, SCALE)
    assert lo ** k <= r < hi ** k
    return lo, hi


def factor_bounds(g):
    """Interval for the depletion factor per unit P: N_0 (2/m) ln(a_f/a_i) / (a^2 H)."""
    s_lo, s_hi = root_bounds(g, 2)
    c_lo, c_hi = root_bounds((F(391, 100) / g) ** 2, 3)
    a2h_lo = F(166, 100) * s_lo * T0 ** 2 * c_lo / MP
    a2h_hi = F(166, 100) * s_hi * T0 ** 2 * c_hi / MP
    n0_lo = HBARC ** 2 / (PI_HI * D_B ** 2)
    n0_hi = HBARC ** 2 / (PI_LO * D_B ** 2)
    return (n0_lo * 2 / MASS * LN_AF_AI / a2h_hi, n0_hi * 2 / MASS * LN_AF_AI / a2h_lo)


def check_logarithmic_depletion_law():
    x = GA.RF.var()
    for (n0, k) in DEPLETION_SAMPLES:
        N = GA.RF.const(1) / (GA.RF.const(1 / n0) + GA.RF.const(k) * x)
        assert (N.deriv() + GA.RF.const(k) * N * N).is_zero()
        assert N.eval(F(0)) == n0
    # the reduction to dN/dx = -k N^2: on a sheet n = N a^-2 (dilution d(n a^2)/dt = 0 without
    # annihilation) and H = h a^-2 (radiation); with d/dt = a H d/da and dN/da = -k N^2 / a (from
    # 1/N = 1/N_0 + k ln a), dn/dt = -2 H n - sigma v n^2 holds exactly when h k = sigma v
    for (a0, nv, h, sv) in SHEET_SAMPLES:
        k = sv / h
        dN = -k * nv * nv / a0
        dn_da = dN / a0 ** 2 - 2 * nv / a0 ** 3
        lhs = a0 * (h / a0 ** 2) * dn_da
        rhs = -2 * (h / a0 ** 2) * (nv / a0 ** 2) - sv * (nv / a0 ** 2) ** 2
        assert lhs == rhs
    return True


def check_survival_numbers():
    premise("dark-matter.r2-one-quantum-per-unit-ball")
    premise("dark-tower-matter.imported-unit-ball-rule")
    keep = F(1, 99)                          # N_f/N_0 = 1/(1 + depletion) >= 99/100
    for g in GS:
        f_lo, f_hi = factor_bounds(g)
        pmax_lo, pmax_hi = keep / f_hi, keep / f_lo
        assert F(12, 10 ** 17) < pmax_lo and pmax_hi < F(22, 10 ** 17)
        surv_lo, surv_hi = 1 / (1 + f_hi), 1 / (1 + f_lo)
        assert F(1, 10 ** 14) < surv_lo and surv_hi < F(25, 10 ** 15)
    return True


def check_phase_t_threshold_and_collisionless():
    premise("dark-tower-matter.three-dimensional-phases")
    premise("simulations.cluster-bound-two-dimensions")
    pbound = F(2, 10 ** 16)
    # (m/e^2)^2 <= pbound  <=>  e^2/m >= 1/sqrt(pbound); bracket 1/sqrt(pbound) by squares
    lo, hi = F(7, 1) * 10 ** 7, F(71, 10) * 10 ** 7
    assert lo ** 2 * pbound < 1 < hi ** 2 * pbound
    thr = 1 / F(17, 10 ** 8)
    assert F(585, 100) * 10 ** 6 < thr < F(59, 10) * 10 ** 6
    assert thr < lo
    return True
