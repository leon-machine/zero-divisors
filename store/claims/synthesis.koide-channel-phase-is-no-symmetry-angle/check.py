"""synthesis.koide-channel-phase-is-no-symmetry-angle: exact checks.

At the Koide depth lambda^2 = 2 the projected coherent face vector of Proposition
synthesis.coherent-face-vector-real-slices(iii)-(iv) is p_k = 1 + sqrt2 cos(delta + 2 pi k/3) (up to a
common factor). With c = cos delta, s = sin delta: cos(delta + 2pi/3) = -c/2 - (sqrt3/2) s and
cos(delta + 4pi/3) = -c/2 + (sqrt3/2) s, so no value of pi is needed to evaluate the split
r(delta) = (p_2/p_1)^2. Everything is certified interval arithmetic over Fractions:
sin and cos of a rational in (0, 1) by Taylor polynomials with twice the first omitted term as the error,
sqrt2 and sqrt3 by integer square roots at 10^-40, every interval end rounded outwards to 10^-40, pi by Machin's formula with the alternating-series remainder.
(1) The window: r(d_lo) < r_min and r(d_hi) > r_max at d_lo = 22222204589/10^11 and
    d_hi = 22222204830/10^11, tight at resolution 10^-11; r monotone on (0, pi/12) (samples; proof).
(2) r(2/9) lies in (206.7703, 206.7704), above r_max: delta = 2/9 is excluded at lambda^2 = 2.
(3) No rational of denominator below 630131 lies in (d_lo, d_hi).
(4) No rational of denominator below 25249 lies in (d_lo/pi, d_hi/pi), hence no point of the orbit
    +-delta* + (pi/6) Z is a rational multiple of pi with denominator at most 4208.
(5) The elasticity (delta/r) dr/ddelta lies in (12, 13) on the window (difference quotient).
Data: the stored electron and muon masses; the window is the muon's stored uncertainty times 3 and,
for the electron, 10^-9 MeV, which covers the store's eight-decimal cut of the CODATA value.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise, quantity

D_LO = F(22222204589, 10 ** 11)
D_HI = F(22222204830, 10 ** 11)
RES = F(1, 10 ** 11)
DMU = F(23, 10 ** 7)          # stored uncertainty of quantity.muon-mass (MeV)
DE = F(1, 10 ** 9)            # electron: covers the stored eight-decimal cut (MeV)


GRID = 10 ** 40


def down(x): return F((x.numerator * GRID) // x.denominator, GRID)
def up(x): return F(-((-x.numerator * GRID) // x.denominator), GRID)


def isqrt(n):
    x = n
    if x < 2:
        return x
    r = 1 << ((x.bit_length() + 1) // 2)
    while True:
        y = (r + x // r) // 2
        if y >= r:
            return r
        r = y


def sqrt_bounds(n):
    k = isqrt(n * GRID * GRID)
    lo, hi = F(k, GRID), F(k + 1, GRID)
    assert lo * lo <= n <= hi * hi
    return lo, hi


def sincos(x, terms=24):
    x = F(x)
    assert 0 < x < 1
    s, c, t = F(0), F(0), F(1)
    for n in range(2 * terms):
        if n % 2 == 0:
            c += (-1) ** (n // 2) * t
        else:
            s += (-1) ** (n // 2) * t
        t = t * x / (n + 1)
    return (down(s - 2 * t), up(s + 2 * t)), (down(c - 2 * t), up(c + 2 * t))


def iadd(a, b): return (down(a[0] + b[0]), up(a[1] + b[1]))
def ineg(a): return (-a[1], -a[0])
def imul(a, b):
    ps = [a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]]
    return (down(min(ps)), up(max(ps)))
def pt(v): return (F(v), F(v))


R2, R3 = sqrt_bounds(2), sqrt_bounds(3)


def roots(delta):
    """intervals for p_1 (electron), p_2 (muon), p_0 (tau) at lambda = sqrt2"""
    s, c = sincos(delta)
    a = imul(pt(F(1, 2)), c)
    b = imul(imul(pt(F(1, 2)), R3), s)
    c0 = c
    c1 = ineg(iadd(a, b))
    c2 = iadd(ineg(a), b)
    return [iadd(pt(1), imul(R2, ck)) for ck in (c1, c2, c0)]


def ratio(delta):
    p1, p2, _ = roots(delta)
    assert p1[0] > 0
    q = imul(p2, (down(1 / p1[1]), up(1 / p1[0])))
    return imul(q, q)


def window():
    me = quantity("quantity.electron-mass")
    mm = quantity("quantity.muon-mass")
    return (mm - 3 * DMU) / (me + DE), (mm + 3 * DMU) / (me - DE)


def pi_bounds():
    def atan_inv(n, terms=40):
        x = F(1, n)
        s, t = F(0), x
        for k in range(terms):
            s += (-1) ** k * t / (2 * k + 1)
            t = t * x * x
        return s, t / (2 * terms + 1)
    a, ea = atan_inv(5)
    b, eb = atan_inv(239)
    p, e = 16 * a - 4 * b, 16 * ea + 4 * eb
    return p - e, p + e


def smallest_denominator(lo, hi):
    """least d with an integer k, lo <= k/d <= hi (0 < lo < hi)"""
    d = 1
    while True:
        k = -((-lo.numerator * d) // lo.denominator)
        if k * hi.denominator <= hi.numerator * d:
            return d, F(k, d)
        d += 1


def check_phase_window_from_the_split():
    premise("synthesis.coherent-face-vector-real-slices")
    premise("families.koide-nullity-condition-one-member-invariant")
    premise("synthesis.light-cone-koide-is-quarter-turn")
    r_min, r_max = window()
    ok = ratio(D_LO)[1] < r_min and ratio(D_HI)[0] > r_max
    # tight at resolution 10^-11: one step inwards is no longer certified
    ok = ok and not (ratio(D_LO + RES)[1] < r_min) and not (ratio(D_HI - RES)[0] > r_max)
    # positivity of all three roots on the window, the electron root negative past pi/12 (0.2618...)
    p = roots(D_HI)
    ok = ok and all(x[0] > 0 for x in p) and p[0][1] < p[1][0] < p[2][0]
    ok = ok and roots(F(27, 100))[0][1] < 0
    pl, _ = pi_bounds()
    ok = ok and D_HI < F(2, 9) < pl / 12
    # monotone samples on (0, pi/12): r strictly increasing
    pts = [F(1, 100), F(5, 100), F(1, 10), F(15, 100), F(2, 10), D_LO, D_HI, F(2, 9), F(25, 100), F(26, 100)]
    rs = [ratio(x) for x in pts]
    ok = ok and all(rs[i][1] < rs[i + 1][0] for i in range(len(rs) - 1))
    GA.check("at lambda^2 = 2 the measured m_mu/m_e puts delta* in (0.22222204589, 0.22222204830)", ok)
    return ok


def check_two_ninths_is_excluded():
    premise("synthesis.coherent-face-vector-real-slices")
    premise("families.koide-nullity-condition-one-member-invariant")
    r_min, r_max = window()
    r29 = ratio(F(2, 9))
    ok = F(2067703, 10000) < r29[0] and r29[1] < F(2067704, 10000) and r29[0] > r_max
    # excluded by more than 400 standard deviations of the muon mass (sigma_r < 23/10^7 / me)
    me = quantity("quantity.electron-mass")
    ok = ok and (r29[0] - r_max) * me > 400 * DMU
    # tabulated: r(2/9) = 206.770315972729..., distance 448.58 sigma-units, 2/9 - d_hi = 1.7392222...e-7
    ok = ok and F(20677031597, 10 ** 8) < r29[0] and r29[1] < F(20677031598, 10 ** 8)
    ok = ok and F(44858, 100) * DMU < (r29[0] - r_max) * me < F(44859, 100) * DMU
    ok = ok and F(2, 9) - D_HI == F(2, 9) - F(22222204830, 10 ** 11)
    ok = ok and F(1739, 10 ** 10) < F(2, 9) - D_HI < F(1740, 10 ** 10)
    GA.check("delta = 2/9 gives m_mu/m_e in (206.7703, 206.7704), outside the measured window", ok)
    return ok


def certified_window():
    """the constants D_LO, D_HI bracket delta* for the stored masses (recomputed here, so that
    clauses (iii) and (iv) fail if the stored masses change)"""
    r_min, r_max = window()
    return ratio(D_LO)[1] < r_min and ratio(D_HI)[0] > r_max


def check_no_simple_rational_phase():
    premise("synthesis.coherent-face-vector-real-slices")
    premise("families.koide-nullity-condition-one-member-invariant")
    d, frac = smallest_denominator(D_LO, D_HI)
    ok = certified_window() and d == 630131 and frac == F(140029, 630131)
    GA.check("the least denominator of a rational in the delta* window is 630131", ok)
    return ok


def check_no_symmetry_angle():
    premise("synthesis.coherent-face-vector-real-slices")
    premise("synthesis.real-structure-breaks-source-stabiliser-to-z2")
    premise("families.koide-nullity-condition-one-member-invariant")
    pl, ph = pi_bounds()
    ok = certified_window() and F(314159265358979, 10 ** 14) < pl < ph < F(314159265358980, 10 ** 14)
    lo, hi = D_LO / ph, D_HI / pl
    d, frac = smallest_denominator(lo, hi)
    ok = ok and d == 25249 and frac == F(1786, 25249)
    # orbit element a pi / b gives delta*/pi with denominator dividing 6 b: excluded for 6 b < 25249
    ok = ok and 6 * 4208 < d <= 6 * 4209
    GA.check("no point of the orbit of delta* is a rational multiple of pi with denominator <= 4208", ok)
    return ok


def check_elasticity_of_the_split():
    premise("synthesis.coherent-face-vector-real-slices")
    premise("families.classification-displaced-gaussian-class-solved-level")
    eps = F(1, 10 ** 6)
    ok = True
    for d0 in (D_LO, D_HI):
        a, b = ratio(d0), ratio(d0 * (1 + eps))
        lo = (b[0] - a[1]) / (a[1] * eps)
        hi = (b[1] - a[0]) / (a[0] * eps)
        ok = ok and F(124, 10) < lo and hi < F(125, 10)
        # tabulated to 10^-5: 12.47646 at both ends
        ok = ok and F(1247646, 10 ** 5) < lo and hi < F(1247647, 10 ** 5)
    GA.check("the split's elasticity with respect to the channel phase is about 12.5, not 1", ok)
    return ok
