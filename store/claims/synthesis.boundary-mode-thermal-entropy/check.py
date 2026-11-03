"""synthesis.boundary-mode-thermal-entropy: exact checks.

With r = e^x kept rational, n = 1/(r+1). Checked exactly: the two forms of the entropy agree
term by term (the ln r and ln(1+r) coefficients), dn/dx = -n(1-n) and d/dx ln(1 + e^{-x}) = -n (the two pieces from which
s' = -x n (1-n) follows), evenness under r -> 1/r,
and n = 1/2 exactly at r = 1. The numerical value at x = 2 pi is bracketed with rational bounds
on e^{-2 pi} from a certified rational enclosure of pi and the exponential series.
"""
from fractions import Fraction as F
import GA
import series
from tp_premise import premise

RS = [F(1), F(2), F(1, 3), F(7, 2), F(100)]


exp_bounds = series.exp_bounds          # rational bounds for e^x, x >= 0


def ln1p_bounds(y):
    """Bounds for ln(1 + y), y > -1 rational."""
    return series.log_bounds(1 + y)


def check_mode_entropy():
    premise("singularity.rate-discharge-hypothesis-iii")
    premise("singularity.p-univalence")
    premise("singularity.r-regularity-fixed-locus")
    for r in RS:
        n = 1 / (r + 1)
        m = 1 - n
        assert m == r / (r + 1)
        # -n ln n - m ln m = ln(r+1) - (r/(r+1)) ln r: coefficients of ln(r+1) and ln r
        # -n ln n = n ln(r+1); -m ln m = -m (ln r - ln(r+1)) = m ln(r+1) - m ln r
        coeff_ln_r1 = n + m
        coeff_ln_r = -m
        assert coeff_ln_r1 == 1 and coeff_ln_r == -r / (r + 1)
        # second form ln(1+e^{-x}) + x n = ln(r+1) - ln r + n ln r: coefficient of ln r is n - 1
        assert n - 1 == coeff_ln_r
        # dn/dx = (dn/dr) r = -r/(r+1)^2 = -n m
        assert -r / (r + 1) ** 2 == -n * m
        # s' = d/dx[ln(1+e^{-x})] + n + x dn/dx with d/dx ln(1+e^{-x}) = -(1/r)/(1+1/r) = -n
        assert -(1 / r) / (1 + 1 / r) == -n
        # evenness: r -> 1/r exchanges n and m
        assert 1 / (1 / r + 1) == m
    assert 1 / (F(1) + 1) == F(1, 2)
    # the value at x = 2 pi: pi in (3.14159265358979, 3.14159265358980)
    pl, ph = F(314159265358979, 10 ** 14), F(314159265358980, 10 ** 14)
    el, _ = exp_bounds(2 * pl)
    _, eh = exp_bounds(2 * ph)
    ql, qh = 1 / eh, 1 / el                    # e^{-2 pi} in [ql, qh]
    nl, nh = ql / (1 + ql), qh / (1 + qh)     # n = e^{-x}/(1 + e^{-x})
    l1, _ = ln1p_bounds(ql)
    _, h1 = ln1p_bounds(qh)
    s_lo = l1 + 2 * pl * nl
    s_hi = h1 + 2 * ph * nh
    assert F(1357, 100000) < s_lo and s_hi < F(1359, 100000)
    # under 2 per cent of ln 2 (ln 2 > 0.6931)
    assert s_hi < F(2, 100) * F(6931, 10000)
    return True
