"""synthesis.koide-channel-phase-target-depends-on-mass-definition: exact checks.

The stored channel-phase window delta* (synthesis.koide-channel-phase-is-no-symmetry-angle) is computed
from pole masses. One QED loop relates pole and MSbar masses,
m_pole = mbar(mu) (1 + a (1 + (3/2) ln(mu/m))), a = alpha/pi, so to first order in a the MSbar masses at
any common scale mu are m_i (1 + kappa ln m_i) up to a common factor, kappa = 3 alpha/(2 pi), and
mass ratios become rbar = r (1 + kappa ln r). Everything below is certified interval arithmetic over
Fractions (ln by the atanh series with its geometric remainder, pi by Machin, sin/cos by alternating
Taylor polynomials, square roots by integer square roots), every interval end rounded outwards.
(1) first-order algebra: the non-universal part of the one-loop factor is -kappa ln m_i (mu drops out).
(2) for alpha between 1/138 and the stored alpha(M_Z), rbar = m_mu/m_e at a common scale lies in
    (210.58, 210.89) and the Koide phase reproducing it at exact Koide lies in (0.22254, 0.22258).
(3) its distance from delta* exceeds 3.1e-4, more than 1800 times the distance of 2/9 from delta*,
    and 2/9 lies between delta* and the common-scale phase.
(4) Koide's Q at common-scale masses, first order: Q - 2/3 in (1.0e-3, 1.3e-3), against
    |Q - 2/3| < 1e-5 at the pole masses (tau within its stored uncertainty).
(5) least denominators in the common-scale band: 319 for delta (2/9 is outside the band), 367 for
    delta/pi, so no orbit point +-delta + (pi/6)Z in the band is a pi/b with b <= 61.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise, quantity

GRID = 10 ** 40
D_LO_POLE = F(22222204589, 10 ** 11)     # stored window of delta* (recertified in check 3)
D_HI_POLE = F(22222204830, 10 ** 11)
DMU = F(23, 10 ** 7)
DE = F(1, 10 ** 9)
DTAU = F(9, 100)
B_LO = F(22254, 10 ** 5)                  # common-scale band, certified below
B_HI = F(22258, 10 ** 5)
DEN_DELTA = 319                           # least denominator of a rational in the band
DEN_PI = 367                              # least denominator of a rational in the band over pi
ORBIT_B = 61                              # hence no orbit point is a pi/b with b <= 61


def down(x): return F((x.numerator * GRID) // x.denominator, GRID)
def up(x): return F(-((-x.numerator * GRID) // x.denominator), GRID)
def iadd(a, b): return (down(a[0] + b[0]), up(a[1] + b[1]))
def isub(a, b): return (down(a[0] - b[1]), up(a[1] - b[0]))
def ineg(a): return (-a[1], -a[0])
def pt(v): return (F(v), F(v))


def imul(a, b):
    ps = [a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]]
    return (down(min(ps)), up(max(ps)))


def iinv(a):
    assert a[0] > 0
    return (down(1 / a[1]), up(1 / a[0]))


def isqrt(n):
    if n < 2:
        return n
    r = 1 << ((n.bit_length() + 1) // 2)
    while True:
        y = (r + n // r) // 2
        if y >= r:
            return r
        r = y


def sqrt_iv(a):
    """interval square root of a positive interval"""
    lo, hi = F(a[0]), F(a[1])
    k1 = isqrt((lo.numerator * GRID * GRID) // lo.denominator)
    k2 = isqrt(-((-hi.numerator * GRID * GRID) // hi.denominator))
    l, h = F(k1, GRID), F(k2 + 1, GRID)
    assert l * l <= lo and h * h >= hi
    return (l, h)


def atanh_iv(z, terms=40):
    z = F(z)
    assert abs(z) <= F(1, 3)
    s, t = F(0), z
    for k in range(terms):
        s += t / (2 * k + 1)
        t = t * z * z
    err = abs(t) / (2 * terms + 1) / (1 - z * z)
    return (down(s - err), up(s + err))


LN2 = imul(pt(2), atanh_iv(F(1, 3)))


def ln_iv(x):
    """certified ln of a positive rational: x = 2^k y with y in [2/3, 4/3]"""
    x, k = F(x), 0
    while x > F(4, 3):
        x, k = x / 2, k + 1
    while x < F(2, 3):
        x, k = x * 2, k - 1
    y = imul(pt(2), atanh_iv((x - 1) / (x + 1)))
    return iadd(imul(pt(k), LN2), y)


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
    return (p - e, p + e)


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


R2, R3 = sqrt_iv((F(2), F(2))), sqrt_iv((F(3), F(3)))


def ratio(delta):
    """(p_2/p_1)^2 at the Koide depth, p_k = 1 + sqrt2 cos(delta + 2 pi k/3)"""
    s, c = sincos(delta)
    a = imul(pt(F(1, 2)), c)
    b = imul(imul(pt(F(1, 2)), R3), s)
    p1 = iadd(pt(1), imul(R2, ineg(iadd(a, b))))
    p2 = iadd(pt(1), imul(R2, iadd(ineg(a), b)))
    q = imul(p2, iinv(p1))
    return imul(q, q)


def kappa_range():
    """kappa = 3 alpha/(2 pi) for alpha in [1/138, 1/alpha^-1(M_Z)]"""
    pl, ph = pi_bounds()
    ainv = quantity("quantity.inverse-fine-structure-mz")
    return (down(F(3, 2) / (138 * ph)), up(F(3, 2) / (ainv * pl)))


def pole_window():
    me = quantity("quantity.electron-mass")
    mm = quantity("quantity.muon-mass")
    return ((mm - 3 * DMU) / (me + DE), (mm + 3 * DMU) / (me - DE))


def common_scale_window():
    r = pole_window()
    k = kappa_range()
    lo = imul(pt(r[0]), iadd(pt(1), imul(pt(k[0]), ln_iv(r[0]))))[0]
    hi = imul(pt(r[1]), iadd(pt(1), imul(pt(k[1]), ln_iv(r[1]))))[1]
    return lo, hi


def smallest_denominator(lo, hi):
    d = 1
    while True:
        k = -((-lo.numerator * d) // lo.denominator)
        if k * hi.denominator <= hi.numerator * d:
            return d, F(k, d)
        d += 1


def check_first_order_factor_is_mu_free():
    premise("synthesis.koide-channel-phase-is-no-symmetry-angle")
    # with symbols replaced by distinct rationals: ln mu = Lm, ln m_i = Li, ln m_j = Lj.
    # (1 + aA)/(1 + aB) = 1 + a (A - B) + a^2 B (B - A) + O(a^3), A = 1 + 3/2 (Lm - Lj),
    # B = 1 + 3/2 (Lm - Li): the a-coefficient A - B = (3/2)(Li - Lj) is mu-free; the a^2 one is not
    # zero, so the statement is first order only. Tabulated values for the three instances.
    table = [((F(7), F(1, 3), F(5)), F(-7), F(77)),
             ((F(-2), F(9, 4), F(1, 7)), F(177, 56), F(7611, 448)),
             ((F(11, 3), F(2), F(-3)), F(15, 2), F(-105, 4))]
    ok = True
    for (Lm, Li, Lj), c1_want, c2_want in table:
        A, B = 1 + F(3, 2) * (Lm - Lj), 1 + F(3, 2) * (Lm - Li)
        c1, c2 = A - B, B * (B - A)
        ok = ok and c1 == c1_want == F(3, 2) * (Li - Lj) and c2 == c2_want
        # mu-freedom: shifting ln mu leaves c1 unchanged
        A2, B2 = A + F(3, 2), B + F(3, 2)
        ok = ok and A2 - B2 == c1_want
    GA.check("one loop: mbar_i/mbar_j = (m_i/m_j)(1 + kappa ln(m_i/m_j)) + O(alpha^2), mu-free", ok)
    return ok


def check_common_scale_phase_band():
    premise("synthesis.koide-channel-phase-is-no-symmetry-angle")
    premise("synthesis.coherent-face-vector-real-slices")
    premise("families.koide-nullity-condition-one-member-invariant")
    lo, hi = common_scale_window()
    ok = F(21058, 100) < lo < hi < F(21089, 100)
    ok = ok and ratio(B_LO)[1] < lo and ratio(B_HI)[0] > hi
    # tight at 10^-5: one step inwards is not certified
    ok = ok and not (ratio(B_LO + F(1, 10 ** 5))[1] < lo) and not (ratio(B_HI - F(1, 10 ** 5))[0] > hi)
    pl, _ = pi_bounds()
    ok = ok and B_HI < pl / 12          # still on the positive-root branch where r is monotone
    GA.check("common-scale m_mu/m_e in (210.58, 210.89); Koide phase in (0.22254, 0.22258)", ok)
    return ok


def check_shift_dwarfs_the_two_ninths_gap():
    premise("synthesis.koide-channel-phase-is-no-symmetry-angle")
    r = pole_window()
    ok = ratio(D_LO_POLE)[1] < r[0] and ratio(D_HI_POLE)[0] > r[1]     # pole window recertified
    shift = B_LO - D_HI_POLE
    gap = F(2, 9) - D_HI_POLE
    ok = ok and shift > F(31, 10 ** 5) and shift > 1800 * gap
    ok = ok and D_HI_POLE < F(2, 9) < B_LO
    GA.check("the common-scale phase is > 3.1e-4 from delta*, > 1800 times the 2/9 gap; 2/9 between", ok)
    return ok


def koide_q(ms):
    s1 = iadd(iadd(ms[0], ms[1]), ms[2])
    s2 = iadd(iadd(sqrt_iv(ms[0]), sqrt_iv(ms[1])), sqrt_iv(ms[2]))
    return (down(s1[0] / s2[1] ** 2), up(s1[1] / s2[0] ** 2))


def check_koide_defect_at_common_scale():
    premise("families.koide-nullity-condition-one-member-invariant")
    me = quantity("quantity.electron-mass")
    mm = quantity("quantity.muon-mass")
    mt = quantity("quantity.tau-mass")
    third = F(2, 3)
    e = 10 ** 8
    # pole masses at the stored centres of m_e, m_mu and both ends of m_tau (Q increases with m_tau
    # on this window: dQ/dm_tau has the sign of S2 - S1/sqrt(m_tau) > 0, proof text); tabulated at 10^-8
    pole = [(mt - DTAU, -729, -728), (mt, -221, -220), (mt + DTAU, 287, 288)]
    ok = True
    for tt, lo, hi in pole:
        q = koide_q([pt(me), pt(mm), pt(tt)])
        ok = ok and third + F(lo, e) < q[0] and q[1] < third + F(hi, e)
    # common scale, first order: mbar_i proportional to m_i (1 + kappa ln(m_i/m_e)) (common factor
    # dropped); tabulated at the two ends of the kappa range (centre of m_tau), at 10^-7
    k = kappa_range()
    lm, lt = ln_iv(F(mm, me)), ln_iv(F(mt, me))
    for kk, lo, hi in ((k[0], 11144, 11145), (k[1], 12000, 12001)):
        mb = [pt(me), imul(pt(mm), iadd(pt(1), imul(pt(kk), lm))), imul(pt(mt), iadd(pt(1), imul(pt(kk), lt)))]
        q = koide_q(mb)
        ok = ok and third + F(lo, 10 ** 7) < q[0] and q[1] < third + F(hi, 10 ** 7)
        # with m_tau over its stored interval the defect stays in (1.0e-3, 1.3e-3)
        t = (mt - DTAU, mt + DTAU)
        mbt = [pt(me), mb[1], imul(t, iadd(pt(1), imul(pt(kk), lt)))]
        qt = koide_q(mbt)
        ok = ok and third + F(1, 1000) < qt[0] and qt[1] < third + F(13, 10000)
    GA.check("first-order common-scale Koide Q - 2/3 in (1.0e-3, 1.3e-3); pole |Q - 2/3| < 1e-5", ok)
    return ok


def check_look_elsewhere_in_the_band():
    premise("synthesis.koide-channel-phase-is-no-symmetry-angle")
    lo, hi = common_scale_window()
    ok = ratio(B_LO)[1] < lo and ratio(B_HI)[0] > hi
    d, frac = smallest_denominator(B_LO, B_HI)
    ok = ok and (d, frac) == (DEN_DELTA, F(71, DEN_DELTA))
    pl, ph = pi_bounds()
    d2, frac2 = smallest_denominator(B_LO / ph, B_HI / pl)
    ok = ok and (d2, frac2) == (DEN_PI, F(26, DEN_PI))
    # an orbit point a pi/b makes delta/pi a rational of denominator dividing 6 b: 6 b >= DEN_PI
    ok = ok and -((-DEN_PI) // 6) - 1 == ORBIT_B
    GA.check("least denominators in the common-scale band: 319 for delta, 367 for delta/pi (orbit b >= 62)", ok)
    return ok
