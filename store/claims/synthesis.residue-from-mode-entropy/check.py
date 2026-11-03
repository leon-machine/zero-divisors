"""synthesis.residue-from-mode-entropy: exact checks.

ln 2 is a formal symbol L; mode entropies are written as rational multiples t_j L with
0 < t_j <= 1 (Theorem boundary-mode-thermal-entropy: s <= ln 2, equality only at zero weight).
Areas are in units of pi where needed. The check verifies kappa_c = 1/(4 <s>), the bound
kappa_c >= 1/(4 L) with equality exactly when all t_j = 1, and the de Sitter form.
"""
from fractions import Fraction as F
import GA
import series
from tp_premise import premise

SETS = [[F(1)] * 5, [F(1), F(1), F(1, 2)], [F(1, 50), F(1), F(1), F(1)], [F(3, 4)] * 4]
R_SAMPLES = [F(2), F(1, 3), F(50)]       # r = e^x > 0 for the energy tension (v)
MASSES = [F(1), F(3, 2)]                  # hole masses for T S = M/2 (v)


def check_residue():
    premise("synthesis.boundary-mode-thermal-entropy")
    premise("synthesis.quarter-from-temperature")
    premise("synthesis.de-sitter-entropy-pi-n-squared")
    premise("synthesis.de-sitter-temperature-frozen-point-norm")
    premise("singularity.p-univalence")
    premise("singularity.r-regularity-fixed-locus")
    premise("synthesis.r-lambda-regularity-cosmological-horizon")
    kcs = []
    for ts in SETS:
        J = len(ts)
        mean_t = sum(ts) / J                       # <s> = mean_t * L
        # sum s = A/4: A = 4 L sum t; kappa_c = J / A = 1 / (4 L mean_t)
        A_over_L = 4 * sum(ts)
        kc_times_L = J / A_over_L                  # kappa_c * L
        assert kc_times_L == 1 / (4 * mean_t)
        kcs.append(kc_times_L)
        # equality in kappa_c >= 1/(4L) iff every t = 1
        assert (kc_times_L == F(1, 4)) == all(t == 1 for t in ts)
    assert min(kcs) == F(1, 4)                     # the bound kappa_c >= 1/(4L), attained
    # de Sitter: S = pi N^2 and |J| <s> = S, so |J| L / (pi N^2) = 1/mean_t >= 1, equality iff all
    # t = 1; the Definition has omega_j > 0, i.e. every t_j < 1, so the inequality is strict there
    ratios, strict = [], []
    for ts in SETS:
        mean_t = sum(ts) / len(ts)
        ratios.append(1 / mean_t)
        assert (1 / mean_t == 1) == all(t == 1 for t in ts)
        if all(t < 1 for t in ts):
            strict.append(1 / mean_t)
    assert min(ratios) == 1
    assert strict == [F(4, 3)]                     # by hand: the one set with every t < 1 has mean 3/4
    # (v) the energy tension: s(x) - x n = ln(1 + 1/r) > 0 for r = e^x > 0, so beta E < S;
    # T S = (1 / 8 pi M) (4 pi M^2) = M / 2
    for r in R_SAMPLES:
        assert 1 + 1 / r > 1
    for M in MASSES:
        assert F(1, 8) / M * 4 * M * M == M / 2          # the pis cancel
    # (vi) Premise (Q) literally: eps = 2 sum_{k>=1} s(2 pi k), bracketed. Both ends of each bracket
    # round to the stated figure: eps in (0.02724, 0.02726) is 0.02725, ln 2 + eps in (0.7203, 0.7205)
    # is 0.7204, arrays per Planck area 0.3470, the registered 1/(4 ln 2) is 0.3607.
    lo_eps, hi_eps = eps_bounds()
    assert round(10 ** 5 * lo_eps) == round(10 ** 5 * hi_eps) == 2725
    l2lo, l2hi = ln2_bounds()
    assert round(10 ** 4 * (l2lo + lo_eps)) == round(10 ** 4 * (l2hi + hi_eps)) == 7204
    arrays_lo, arrays_hi = 1 / (4 * (l2hi + hi_eps)), 1 / (4 * (l2lo + lo_eps))
    assert round(10 ** 4 * arrays_lo) == round(10 ** 4 * arrays_hi) == 3470
    reg_lo, reg_hi = 1 / (4 * l2hi), 1 / (4 * l2lo)
    assert round(10 ** 4 * reg_lo) == round(10 ** 4 * reg_hi) == 3607
    assert arrays_hi < reg_lo                              # (Q) misses the registered value
    return True


PI_LO, PI_HI = F(314159265358979, 10 ** 14), F(314159265358980, 10 ** 14)


exp_bounds = series.exp_bounds          # rational bounds for e^x, x >= 0


def ln1p_bounds(y):
    """Bounds on ln(1 + y) for rational y > -1."""
    return series.log_bounds(1 + y)


def ln2_bounds():
    return series.ln_bounds(2)


def s_bounds(k):
    """Bounds on s(2 pi k) = ln(1 + q) + x q / (1 + q), q = e^{-x}, x = 2 pi k."""
    xl, xh = 2 * k * PI_LO, 2 * k * PI_HI
    el, _ = exp_bounds(xl)
    _, eh = exp_bounds(xh)
    ql, qh = 1 / eh, 1 / el
    a_lo, _ = ln1p_bounds(ql)
    _, a_hi = ln1p_bounds(qh)
    return a_lo + xl * ql / (1 + ql), a_hi + xh * qh / (1 + qh)


def eps_bounds():
    lo = hi = F(0)
    for k in (1, 2, 3):
        a, b = s_bounds(k)
        lo, hi = lo + a, hi + b
    # tail k >= 4: s(x) < (1 + x) e^{-x}, and e^{-2 pi k} <= e^{-8 pi} (e^{-2 pi})^{k-4}
    el8, _ = exp_bounds(8 * PI_LO)
    el2, _ = exp_bounds(2 * PI_LO)
    q8, q2 = 1 / el8, 1 / el2
    tail = F(0)
    for j in range(0, 30):
        tail += (1 + 2 * (4 + j) * PI_HI) * q8 * q2 ** j
    tail += 1 / el8 * F(1, 10 ** 6)       # generous allowance beyond j = 30
    return 2 * lo, 2 * (hi + tail)
