"""simulations.cluster-bound-two-dimensions: exact interval checks.

All quantities are rational intervals: pi and Euler's gamma by rational brackets, logarithms by the
series ln y = 2 sum z^(2j+1)/(2j+1), z = (y - 1)/(y + 1), after scaling y into [1, 2) by powers of
two (the truncated sum is a lower bound and the geometric tail gives the upper one), square roots by
integer square roots. Masses: nucleon (proton) mass 938.272 MeV = 1.67262192e-24 g, hbar c =
197.3269804 MeV fm.

Rounded statements are checked as: both ends of the computed interval round to the stated value.
(0) k = (m/2) v / hbar for v = 3000 km/s rounds to 0.0238 fm^-1.
(i) With k = 0.0238 fm^-1 and x = ka: for a = 0.21 fm the s-wave of the partial-wave sum,
    tan delta_0 = J_0(x)/Y_0(x) with J_0 and Y_0 from their power series (alternating tails
    bracketed), Y_0 = (2/pi)[(ln(x/2) + gamma) J_0 + sum_(k>=1) (-1)^(k+1) H_k (x^2/4)^k/(k!)^2],
    gives (4/k) sin^2 delta_0 = 13 fm, and the m = +-1 terms add less than 10^-6 fm
    (|J_1| <= x/2, |Y_1| >= 2/(pi x) - (2/pi)|ln(x/2)| x/2 - x/pi for x < 0.1); |m| >= 2 terms are of
    order x^8 and are not bounded here. The logarithmic form lambda = pi^2/(k (ln(ka/2) + gamma)^2)
    gives 14 fm at a = 0.21 fm and 0.49 fm at a = 10^-11 fm.
(ii) sigma_eff = lambda s with the isotropic core spacing s = 3.5 cm (the value the paper computes
    from R1 and R2 for a cluster core, taken here as input): sigma_eff/m < 1 cm^2/g iff
    lambda < m/s, with m/s = 4.8 x 10^-12 fm.
(iii) Solving the logarithmic form for that lambda: log10(a/fm) = -4.0 x 10^6; through
    lambda = (4/k) sin^2 delta_0, sin delta_0 < sqrt(k lambda/4) = 1.7 x 10^-7, so
    delta_0 < 1.7 x 10^-7 to the stated precision.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

PI = (F(314159265358, 10 ** 11), F(314159265359, 10 ** 11))
GAMMA = (F(57721566490, 10 ** 11), F(57721566491, 10 ** 11))
K_STATED = F(238, 10000)                          # fm^-1
M_N_MEV, HBARC = F(938272, 1000), F(1973269804, 10 ** 7)
M_N_G = F(167262192, 10 ** 8) * F(1, 10 ** 24)    # g
C_KMS, V_KMS = F(299792458, 1000), F(3000)
S_CORE_CM = F(35, 10)
RADII = {"core": F(21, 100), "tiny": F(1, 10 ** 11)}
FM_PER_CM = 10 ** 13


def isqrt(n):
    if n < 2:
        return n
    x, y = n, (n + 1) // 2
    while y < x:
        x, y = y, (y + n // y) // 2
    return x


def sqrt_iv(a, scale=10 ** 30):
    lo = F(isqrt(a[0].numerator * scale * scale // a[0].denominator), scale)
    hi = F(isqrt(a[1].numerator * scale * scale // a[1].denominator) + 1, scale)
    return lo, hi


def ln_series(y, terms=40):
    """bounds on ln y for 1 <= y < 2"""
    z = (y - 1) / (y + 1)
    s, p = F(0), z
    for j in range(terms):
        s += p / (2 * j + 1)
        p *= z * z
    return 2 * s, 2 * s + 2 * p / ((2 * terms + 1) * (1 - z * z))


def ln2_bounds():
    z = F(1, 3)
    s, p = F(0), z
    for j in range(40):
        s += p / (2 * j + 1)
        p *= z * z
    return 2 * s, 2 * s + 2 * p / ((2 * 40 + 1) * (1 - z * z))


def ln_iv(q):
    """bounds on ln q for a rational q > 0 (rounded to 40 digits first)"""
    e, y = 0, q
    while y >= 2:
        y /= 2
        e += 1
    while y < 1:
        y *= 2
        e -= 1
    scale = 10 ** 40
    y_lo = F(y.numerator * scale // y.denominator, scale)
    y_hi = min(y_lo + F(1, scale), F(2) - F(1, scale))
    l2 = ln2_bounds()
    a, b = ln_series(max(y_lo, F(1)))[0], ln_series(y_hi)[1]
    if e >= 0:
        return e * l2[0] + a, e * l2[1] + b
    return e * l2[1] + a, e * l2[0] + b


def imul(a, b):
    ps = [a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]]
    return min(ps), max(ps)


def iadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def idiv(a, b):
    assert b[0] > 0 or b[1] < 0
    return imul(a, (1 / b[1], 1 / b[0]))


def isq(a):
    if a[0] >= 0:
        return a[0] * a[0], a[1] * a[1]
    if a[1] <= 0:
        return a[1] * a[1], a[0] * a[0]
    return F(0), max(a[0] * a[0], a[1] * a[1])


def log_form_lambda(k, a):
    L = iadd(ln_iv(k * a / 2), GAMMA)
    return idiv(isq(PI), imul((k, k), isq(L)))


def s_wave_lambda(k, a):
    x = k * a
    u = x * x / 4
    J0 = (1 - u, 1 - u + u * u / 4)                       # alternating, decreasing terms
    S = (u - F(3, 8) * u * u, u)                           # sum (-1)^(k+1) H_k u^k/(k!)^2
    L = iadd(ln_iv(x / 2), GAMMA)
    Y0 = imul((2 / PI[1], 2 / PI[0]), iadd(imul(L, J0), S))
    t = idiv(J0, Y0)
    t2 = isq(t)
    s2 = (t2[0] / (1 + t2[0]), t2[1] / (1 + t2[1]))        # t^2/(1 + t^2) is increasing
    return 4 * s2[0] / k, 4 * s2[1] / k


def p_wave_bound(k, a):
    x = k * a
    lnx = ln_iv(x / 2)
    y1_lo = 2 / (PI[1] * x) + (2 / PI[1]) * lnx[0] * x / 2 - x / PI[0]
    assert y1_lo > 0
    tan_hi = (x / 2) / y1_lo
    return 2 * 4 * tan_hi * tan_hi / k


def rounded(iv, scale):
    """the common value of both ends of an interval rounded to a multiple of 1/scale, else None"""
    a, b = round(iv[0] * scale), round(iv[1] * scale)
    return F(a, scale) if a == b else None


def check_wave_number():
    k = (M_N_MEV / 2) * (V_KMS / C_KMS) / HBARC
    assert rounded((k, k), 10000) == F(238, 10000)
    return True


def check_hard_disk_lengths():
    premise("simulations.imported-low-energy-scattering-two-dimensions")
    k = K_STATED
    lo, hi = s_wave_lambda(k, RADII["core"])
    extra = p_wave_bound(k, RADII["core"])
    assert rounded((lo, hi + extra), 1) == 13 and extra < F(1, 10 ** 6)
    assert rounded(log_form_lambda(k, RADII["core"]), 1) == 14
    assert rounded(log_form_lambda(k, RADII["tiny"]), 100) == F(49, 100)
    return True


def lambda_max_fm():
    return M_N_G / S_CORE_CM * FM_PER_CM              # (1 cm^2/g) m / s, in fm


def check_cluster_bound_on_lambda():
    premise("simulations.effective-cross-section-sheet-matter")
    premise("dark-matter.r1-equal-mass-per-quantum")
    premise("dark-matter.r2-one-quantum-per-unit-ball")
    lam = lambda_max_fm() * 10 ** 12
    assert rounded((lam, lam), 10) == F(48, 10)
    return True


def check_size_and_phase_shift_limits():
    premise("simulations.imported-low-energy-scattering-two-dimensions")
    premise("simulations.effective-cross-section-sheet-matter")
    k, lam = K_STATED, lambda_max_fm()
    # |L| = pi / sqrt(k lam), L = ln(ka/2) + gamma < 0
    root = sqrt_iv((k * lam, k * lam))
    absL = (PI[0] / root[1], PI[1] / root[0])
    ln_a = iadd(iadd((-absL[1], -absL[0]), (-GAMMA[1], -GAMMA[0])), ln_iv(2 / k))
    ln10 = ln_iv(F(10))
    log10_a = (ln_a[0] / ln10[0], ln_a[1] / ln10[1])
    assert rounded((log10_a[0] / 10 ** 6, log10_a[1] / 10 ** 6), 10) == F(-40, 10)
    s = sqrt_iv((k * lam / 4, k * lam / 4))
    assert rounded((s[0] * 10 ** 7, s[1] * 10 ** 7), 10) == F(17, 10)
    return True


EXPORTS = {"rounded": rounded, "ln_iv": ln_iv, "log_form_lambda": log_form_lambda, "lambda_max_fm": lambda_max_fm,
           "sqrt_iv": sqrt_iv, "PI": PI, "GAMMA": GAMMA, "K": K_STATED, "M_N_G": M_N_G,
           "FM_PER_CM": FM_PER_CM, "S_CORE_CM": S_CORE_CM}
