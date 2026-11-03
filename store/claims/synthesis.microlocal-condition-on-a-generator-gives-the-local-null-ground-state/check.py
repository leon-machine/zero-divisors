"""Microlocal spectrum condition on a horizon generator: exact checks.

Conventions of the store: W(u, v) = omega(psi*(v) psi(u)); the null vacuum W_0 = (i/2pi)(u - v + i0)^-1
has symbol theta(p) (W_0 = (1/2pi) int_0^inf e^{ip(u-v)} dp), the other ordering delta - W_0 has symbol
theta(-p). A translation-invariant gauge-invariant quasi-free state has W = (1/2pi) int e^{ip(u-v)} f(p) dp
with 0 <= f <= 1 (f the occupation symbol).

(1) Affine-KMS states satisfy the condition: W_beta(x) = (i/2beta)/sinh(pi(x + i0)/beta), so with
    y = pi x/beta, (2beta/i)(W_beta - W_0) = 1/sinh(y) - 1/y = (1/y)(g(y^2) - 1), g = (sinh(y)/y)^-1.
    Exact power-series inversion of sinh(y)/y = sum y^{2k}/(2k+1)! gives g_0 = 1 and
    g_n = 2(1 - 2^{2n-1}) B_{2n}/(2n)! (Bernoulli numbers from their recurrence), so the remainder is
    y times a power series: no negative power, odd in y, leading -y/6, i.e. -(i pi/12 beta^2) x.
    On the real line sinh(y)/y >= 1 (all its Taylor coefficients are positive), so the remainder is
    real-analytic on the whole line: smooth everywhere, hence the condition holds at every point.
(2) Symbol criterion (translation-invariant case of the two-ordering lemma): the condition on both
    orderings says f decays rapidly as p -> -inf and 1 - f as p -> +inf, i.e. f - theta is rapidly
    decreasing. Thermal f = 1/(1 + q^p), q = e^{-beta}: |f - theta| <= q^|p| at both ends (rational q
    samples, integer p). Mixture f_t = t theta(p) + (1 - t) theta(-p): |f - theta| = 1 - t at every p != 0,
    no decay at either end for t < 1. Jump example f - theta = -sign(p) c/(1 + |p|), c <= 1/2:
    a state (0 <= f <= 1), odd, square-summable symbol (partial sums of c^2/(1 + p)^2 <= 2 c^2) whose tail
    p|r(p)| tends to c, so the remainder is bounded with a jump -(ic/2) sign(u - v) across the diagonal:
    locally Hilbert-Schmidt and bounded, not smooth (both conditions are strictly weaker).
(3) The mixtures fail the local Hilbert-Schmidt condition at every point: W_t - W_0 = (1 - t)(delta - 2W_0)
    = -(1 - t)(i/pi) PV 1/(u - v) (symbol identity (1 - t)(1 - 2 theta) = -(1 - t) sign). For a
    translation-invariant kernel k on [0, L]^2, ||k||^2 = 2 int_0^L (L - x)|k(x)|^2 dx; for k = 1/x cut off
    at x > eps this is >= (L/2) int_eps^{L/2} x^-2 dx = L/(2 eps) - 1, unbounded as eps -> 0.
(4) The stored half-thermal products omega_c fail the condition at the edge only: at c = 1/2,
    u = a^2, v = b^2, the half-generator difference is -(a - b)/((a + b)(a^2 + b^2)) (times i/2pi),
    homogeneous of degree -1 in (u, v), so unbounded on every neighbourhood of the edge (not smooth there),
    and a rational function with nonvanishing denominator for a, b > 0 (analytic off the edge); the
    cross-edge block -(i/2pi)/(u - v) at (s, -s) is -(i/2pi)/(2s), unbounded as s -> 0. The boost rotor
    dilates the generator about its edge, which is what makes stationarity a homogeneity condition.
Exact arithmetic only (Fractions); no transcendental number is evaluated.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SQ4 = (1, -1, -1, -1)
ORDER = 9
Q_SAMPLES = (F(1, 3), F(2, 5), F(7, 8))
P_RANGE = 40
Y_SAMPLES = (F(1, 10), F(1), F(5, 2), F(-3), F(-1, 7))
T_SAMPLES = (F(0), F(1, 4), F(1, 2), F(9, 10))
C_SAMPLES = (F(1, 2), F(1, 3), F(1, 10))
L_SAMPLES = (F(1), F(3, 2), F(10))
HALF_PTS = ((F(2), F(1)), (F(1, 3), F(5, 4)), (F(7, 2), F(3)), (F(1, 9), F(1, 11)))
HOM_S = (F(1, 2), F(3), F(1, 100))
ROTOR_R = (F(3, 2), F(1, 4))


def _fact(n):
    out = 1
    for k in range(2, n + 1):
        out *= k
    return out


def _binom(n, k):
    return _fact(n) // (_fact(k) * _fact(n - k))


def _bernoulli(nmax):
    B = [F(1)]
    for m in range(1, nmax + 1):
        B.append(-sum(_binom(m + 1, k) * B[k] for k in range(m)) / (m + 1))
    return B


def _inverse_series(a, order):
    """g with (sum a_k z^k)(sum g_n z^n) = 1 up to z^order; a_0 = 1."""
    g = [F(1)]
    for n in range(1, order + 1):
        g.append(-sum(a[k] * g[n - k] for k in range(1, n + 1)))
    return g


def check_affine_kms_remainder_is_smooth_at_every_point():
    premise("synthesis.local-normality-at-the-edge-gives-the-null-ground-state")
    premise("synthesis.positive-null-energy-gives-r-premises")
    # sinh(y)/y = sum_k y^{2k}/(2k+1)!, as a series in z = y^2
    a = [F(1, _fact(2 * k + 1)) for k in range(ORDER + 1)]
    g = _inverse_series(a, ORDER)
    B = _bernoulli(2 * ORDER)
    GA.check("Bernoulli B_2 = 1/6, B_4 = -1/30", B[2] == F(1, 6) and B[4] == F(-1, 30))
    GA.check("odd Bernoulli numbers beyond B_1 vanish", all(B[k] == 0 for k in range(3, 2 * ORDER, 2)))
    for n in range(ORDER + 1):
        GA.check("1/sinh coefficients are 2(1 - 2^{2n-1}) B_2n/(2n)!",
                 g[n] == 2 * (1 - F(2) ** (2 * n - 1)) * B[2 * n] / _fact(2 * n))
    # 1/sinh(y) - 1/y = sum_{n>=1} g_n y^{2n-1}: the y^-1 terms cancel exactly because g_0 = 1
    GA.check("the pole of the KMS kernel is the vacuum's: g_0 = 1", g[0] == 1)
    GA.check("leading remainder -y/6", g[1] == F(-1, 6))
    GA.check("next remainder 7 y^3/360", g[2] == F(7, 360))
    # (2 beta/i) R = g_1 y + ...; with y = pi x/beta: R = (i/2beta) g_1 (pi/beta) x = -(i pi/12 beta^2) x
    GA.check("leading remainder coefficient -1/12 of i pi x/beta^2", F(1, 2) * g[1] == F(-1, 12))
    # analyticity on the real line: sinh(y)/y >= 1 since every Taylor coefficient is positive
    GA.check("all Taylor coefficients of sinh(y)/y positive", all(c > 0 for c in a))
    for y in Y_SAMPLES:
        partial = sum(a[k] * y ** (2 * k) for k in range(ORDER + 1))
        GA.check("sinh(y)/y >= 1 on the real line (partial sums of positive terms)", partial >= 1)
        # truncated product identity: (sinh(y)/y) * g = 1 + O(y^{2(ORDER+1)})
        prod = [sum(a[k] * g[n - k] for k in range(n + 1)) for n in range(ORDER + 1)]
        GA.check("series inverse", prod == [F(1)] + [F(0)] * ORDER)


def check_symbol_criterion_separates_thermal_mixture_and_jump_states():
    premise("synthesis.positive-null-energy-gives-r-premises")
    premise("synthesis.local-normality-at-the-edge-gives-the-null-ground-state")
    for q in Q_SAMPLES:
        GA.check("0 < q < 1", 0 < q < 1)
        for p in range(-P_RANGE, P_RANGE + 1):
            if p == 0:
                continue
            f = 1 / (1 + q ** p)
            theta = 1 if p > 0 else 0
            GA.check("thermal occupation is a state", 0 < f < 1)
            GA.check("|f - theta| <= q^|p| at both ends", abs(f - theta) <= q ** abs(p))
            GA.check("the two orderings: f + (1 - f) = 1", f + (1 - f) == 1)
        GA.check("the bound q^|p| halves within a fixed number of steps (geometric decay)",
                 q ** 6 < F(1, 2))
    for t in T_SAMPLES:
        for p in (-P_RANGE, -1, 1, P_RANGE):
            f = t if p > 0 else 1 - t
            theta = 1 if p > 0 else 0
            sign = 1 if p > 0 else -1
            GA.check("mixture is a state", 0 <= f <= 1)
            GA.check("mixture remainder symbol is -(1 - t) sign(p)", f - theta == -(1 - t) * sign)
            GA.check("no decay at either end for t < 1", abs(f - theta) == 1 - t and 1 - t > 0)
    for c in C_SAMPLES:
        GA.check("c <= 1/2", c <= F(1, 2))
        total = F(0)
        for p in range(1, P_RANGE + 1):
            up = 1 - c / (1 + p)
            down = c / (1 + p)
            GA.check("jump example is a state", 0 <= up <= 1 and 0 <= down <= 1)
            r_plus, r_minus = up - 1, down - 0
            GA.check("remainder symbol is odd: r(-p) = -r(p)", r_minus == -r_plus)
            GA.check("remainder symbol is -sign(p) c/(1 + |p|)", r_plus == -c / (1 + p))
            GA.check("tail coefficient: c - p|r(p)| = c/(1 + p) (jump height c across the diagonal)",
                     c - p * abs(r_plus) == c / (1 + p))
            total += 2 * (c / (1 + p)) ** 2
            GA.check("p times the symbol does not tend to zero", p * c / (1 + p) >= c / 2)
        GA.check("square-summable: partial sums <= 2 * 2 c^2", total <= 4 * c * c)


def check_mixture_fails_the_local_hilbert_schmidt_condition_everywhere():
    premise("synthesis.local-normality-at-the-edge-gives-the-null-ground-state")
    for t in T_SAMPLES:
        # (1 - t)(delta - 2 W_0) in symbols: (1 - t)(1 - 2 theta) = -(1 - t) sign
        for p in (-3, 2):
            theta = 1 if p > 0 else 0
            sign = 1 if p > 0 else -1
            GA.check("delta - 2 W_0 has symbol -sign(p)", 1 - 2 * theta == -sign)
            mix = t * theta + (1 - t) * (1 - theta)
            GA.check("W_t - W_0 = (1 - t)(delta - 2 W_0)", mix - theta == (1 - t) * (1 - 2 * theta))
    for L in L_SAMPLES:
        prev = None
        for k in range(1, 12):
            eps = L / (2 ** (k + 1))
            # lower bound of 2 int_eps^L (L - x)/x^2 dx: (L - x) >= L/2 on [eps, L/2]
            lower = (L / 2) * (1 / eps - 2 / L)
            GA.check("lower bound L/(2 eps) - 1", lower == L / (2 * eps) - 1)
            GA.check("bound equals 2^k - 1", lower == 2 ** k - 1)
            if prev is not None:
                GA.check("grows without bound as eps -> 0", lower > prev)
            prev = lower


def _rotor(r):
    m = GA.mul(GA.gen(1), GA.gen(0), SQ4)
    return GA.add(GA.sc((r + 1 / r) / 2), GA.scal((r - 1 / r) / 2, m))


def check_half_thermal_products_fail_the_condition_at_the_edge_only():
    premise("synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit")
    premise("synthesis.local-normality-at-the-edge-gives-the-null-ground-state")
    l = GA.add(GA.gen(0), GA.gen(1))
    for r in ROTOR_R:
        Bm = _rotor(r)
        GA.check("rotor", GA.eq(GA.mul(Bm, GA.reverse(Bm), SQ4), GA.sc(1)))
        GA.check("the boost dilates the generator about its edge",
                 GA.eq(GA.mul(GA.mul(Bm, l, SQ4), GA.reverse(Bm), SQ4), GA.scal(r * r, l)))

    def W(a, b, half):
        u, v = a * a, b * b
        if half == 1:
            return 1 / (u - v)
        tt = u / v
        return 1 / (a * b) / (F(1, 2) * (tt - 1 / tt))

    for (a, b) in HALF_PTS:
        D = W(a, b, 2) - W(a, b, 1)
        den = (a + b) * (a * a + b * b)
        GA.check("D = -(a - b)/((a + b)(a^2 + b^2))", D == -(a - b) / den)
        GA.check("denominator positive off the edge: analytic there", den > 0)
        for s in HOM_S:
            GA.check("degree -1 in (u, v): unbounded at the edge",
                     W(s * a, s * b, 2) - W(s * a, s * b, 1) == D / (s * s))
    prev = None
    for k in range(1, 9):
        s = F(1, 3 ** k)
        cross = 1 / (s - (-s))
        GA.check("cross-edge block at (s, -s) is 1/(2s)", cross == F(3 ** k, 2))
        if prev is not None:
            GA.check("unbounded as s -> 0", cross > prev)
        prev = cross
