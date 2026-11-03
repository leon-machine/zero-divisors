"""standard-model.proton-condition-candidates: exact checks.

All arithmetic is rational. The one-loop meeting data (x = ln(M_U/M_Z)/2 pi, y, a_U) are the exact
rationals of the one-threshold theorem (solver exported by its check) and of the two-threshold line;
GeV values M_Z e^(2 pi x) are enclosed by rigorous rational bounds on pi and exp (exported by the
two-loop check), so every scale and lifetime below is a rational interval, not a float.
The lifetime is the imported formula tau = 1.6e33 yr [ (1/5.2)(a_U/45)(M_U/1e15 GeV)^2 ]^2 and the
proton condition is (a_U/45)(M_U/1e15)^2 > 5.2 sqrt(15), compared through squares (> 405.6).
(1) The three admissible rows: M_U rounds to 2.5, 1.6, 1.5 x 10^14 GeV, the lifetimes to 2e29, 3e28,
2e28 yr, each short of 2.4e34 yr by a factor between 10^5 and 10^7.
(2) Along the exact segment of split (d), the condition changes from failing to holding between
f = 0.86811 and f = 0.86813; there (f, f') rounds to (0.868, 0.759), the light set to 6 x 10^3 GeV,
the heavy set to 1.9 x 10^5 GeV, M_U to 5.6 x 10^15 GeV. It holds at sample points above the crossing,
up to the near-degenerate end (1, 0.991), and fails at sample points below it, down to (0.438, 0)
where the light set sits at 7 x 10^8 GeV.
(3) The two-loop central run (bracketed by the two-loop check) gives a lifetime rounding to 3e35 yr,
meeting the condition.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

LIMIT = F(24, 10) * 10 ** 34          # yr, Super-Kamiokande
TAU0 = F(16, 10) * 10 ** 33           # yr
K52 = F(52, 10)


def lifetime(mu_lo, mu_hi, au_lo, au_hi):
    """Rational interval for tau_p (increasing in M_U and alpha_U^-1)."""
    def tau(mu, au):
        return TAU0 * ((au / 45) * (mu / 10 ** 15) ** 2 / K52) ** 2
    return tau(mu_lo, au_lo), tau(mu_hi, au_hi)


def condition(mu, au):
    """(a_U/45)(M_U/1e15)^2 compared with 5.2 sqrt 15 via squares; returns the signed difference."""
    lhs = (au / 45) * (mu / 10 ** 15) ** 2
    return lhs * lhs - K52 * K52 * 15


def record(aem_inv, s2, as_inv):
    a2 = s2 * aem_inv
    return (F(3, 5) * (aem_inv - a2), a2, as_inv)


A_T12 = record(F(128), F(2312, 10000), F(500, 59))
B_SM = (F(41, 10), F(-19, 6), F(-7))
ROWS = [(F(0), F(4, 3), F(0)),                 # wino
        (F(2, 5), F(2), F(0)),                 # wino + bino + higgsinos
        (F(5, 2), F(25, 6), F(2))]             # supersymmetric content without the gluino
LIGHT_D = (F(2, 5), F(2), F(0))                # (d): wino, bino, higgsinos
HEAVY_D = (F(21, 10), F(13, 6), F(4))          # (d): gluino, sfermions, second doublet
F_BRACKET = (F(86811, 100000), F(86813, 100000))
F_ABOVE = (F(87, 100), F(9, 10), F(95, 100), F(1))
F_BELOW = (F(86, 100), F(8, 10), F(6, 10), F(5, 10))


def tools():
    tl = premise("standard-model.supersymmetric-row-two-loops")
    return tl["gev"], tl["pi_bounds"](), tl["rounds_to"]


def scale(gev, pis, x):
    """GeV interval of M_Z e^(2 pi x)."""
    lo, hi = sorted((2 * pis[0] * x, 2 * pis[1] * x))
    return gev(lo, hi)


def on_segment(f):
    """(f', x, a_U) on the two-threshold line of split (d)."""
    D12, D23 = A_T12[0] - A_T12[1], A_T12[1] - A_T12[2]
    R = D12 / D23
    b12, b23 = B_SM[0] - B_SM[1], B_SM[1] - B_SM[2]
    l12, l23 = LIGHT_D[0] - LIGHT_D[1], LIGHT_D[1] - LIGHT_D[2]
    h12, h23 = HEAVY_D[0] - HEAVY_D[1], HEAVY_D[1] - HEAVY_D[2]
    P, Q, C = l12 - R * l23, h12 - R * h23, R * b23 - b12
    fp = (C - P * f) / Q
    x = D12 / (b12 + f * l12 + fp * h12)
    aU = A_T12[0] - x * (B_SM[0] + f * LIGHT_D[0] + fp * HEAVY_D[0])
    return fp, x, aU, C / P


def check_three_admissible_rows_fail():
    premise("standard-model.imported-proton-condition")
    premise("standard-model.spectrum-run")
    solve = premise("standard-model.one-threshold-exact-criterion")["solve"]
    gev, pis, rounds_to = tools()
    stated = [((25, 13), (2, 29)), ((16, 13), (3, 28)), ((15, 13), (2, 28))]
    ok = True
    for d, (mu_r, tau_r) in zip(ROWS, stated):
        x, y, aU, f = solve(A_T12, B_SM, d)
        ok = ok and 0 <= f <= 1 and aU > 0
        mu_lo, mu_hi = scale(gev, pis, x)
        ok = ok and rounds_to(mu_lo, mu_hi, *mu_r)
        t_lo, t_hi = lifetime(mu_lo, mu_hi, aU, aU)
        ok = ok and rounds_to(t_lo, t_hi, *tau_r)
        ok = ok and 10 ** 5 < LIMIT / t_hi and LIMIT / t_lo < 10 ** 7
        ok = ok and condition(mu_hi, aU) < 0
    GA.check("proton (1): the three admissible one-loop rows miss the limit by five to six orders", ok)
    return ok


def check_segment_crossing():
    premise("standard-model.imported-proton-condition")
    premise("standard-model.spectrum-run")
    premise("standard-model.two-threshold-criterion")
    premise("standard-model.four-supersymmetric-splits")
    gev, pis, rounds_to = tools()
    ok = True
    (fl, fh) = F_BRACKET
    fpl, xl, aul, f_end = on_segment(fl)
    fph, xh, auh, _ = on_segment(fh)
    mu_l, mu_h = scale(gev, pis, xl), scale(gev, pis, xh)
    ok = ok and condition(mu_l[1], aul) < 0 < condition(mu_h[0], auh)
    ok = ok and rounds_to(fl, fh, 868, -3) and rounds_to(min(fpl, fph), max(fpl, fph), 759, -3)
    li = [scale(gev, pis, x * (1 - f)) for f, x in ((fl, xl), (fh, xh))]
    he = [scale(gev, pis, x * (1 - fp)) for fp, x in ((fpl, xl), (fph, xh))]
    ok = ok and rounds_to(min(v[0] for v in li), max(v[1] for v in li), 6, 3)
    ok = ok and rounds_to(min(v[0] for v in he), max(v[1] for v in he), 19, 4)
    ok = ok and rounds_to(min(mu_l[0], mu_h[0]), max(mu_l[1], mu_h[1]), 56, 14)
    for f in F_ABOVE:
        fp, x, aU, _ = on_segment(f)
        ok = ok and 0 <= fp <= f and condition(scale(gev, pis, x)[0], aU) > 0
    ok = ok and on_segment(F(1))[0] > F(99, 100)
    for f in F_BELOW + (f_end,):
        fp, x, aU, _ = on_segment(f)
        ok = ok and 0 <= fp <= f and condition(scale(gev, pis, x)[1], aU) < 0
    # the far end (0.438, 0): electroweak-inos at 7 x 10^8 GeV, excluded
    fp, x, aU, _ = on_segment(f_end)
    lo, hi = scale(gev, pis, x * (1 - f_end))
    ok = ok and fp == 0 and rounds_to(f_end, f_end, 438, -3) and rounds_to(lo, hi, 7, 8)
    GA.check("proton (2): the segment of (d) meets the condition down to (0.868, 0.759), and fails beyond", ok)
    return ok


def check_two_loop_row_meets():
    premise("standard-model.imported-proton-condition")
    tl = premise("standard-model.supersymmetric-row-two-loops")
    r = tl["central"]()
    ok = r is not None
    if ok:
        _, (mu_lo, mu_hi), (au_lo, au_hi) = r
        t_lo, t_hi = lifetime(mu_lo, mu_hi, au_lo, au_hi)
        ok = tl["rounds_to"](t_lo, t_hi, 3, 35) and t_lo > LIMIT
        ok = ok and condition(mu_lo, au_lo) > 0
    GA.check("proton (3): the two-loop supersymmetric row has tau_p about 3e35 yr and meets the condition", ok)
    return ok


EXPORTS = {"lifetime": lifetime, "condition": condition}
