"""synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase: exact checks.

At the order of the breaking lemma each quark sector's light states are the left singular vectors of
B_q = [[k, x_q], [y_q, 0]] (compression to the light plane, as for the leptons). For a one-type stage
|x_q| = |y_q| and tan^2 theta_q = sigma2/sigma1 = m_light/m_heavy (the Gatto-Sartori-Tonin / Fritzsch
relation). With x = m_d/m_s, y = m_u/m_c and phi the relative phase of the off-diagonal entries of
B_u B_u^dag and B_d B_d^dag,
    |V_us|^2 = (x + y - 2 cos(phi) sqrt(x y)) / ((1 + x)(1 + y)).
(1) exact Gaussian-rational instances: for |x| = |y| (symmetric, antisymmetric, complex) the light
    angle obeys cos^2(2 theta) = (tr H - 2|det B|)/(tr H + 2|det B|), i.e. tan^2 theta = sigma2/sigma1;
    a lopsided block (y = 2x) violates it; the projector overlap equals the formula above.
(2) with m_s/m_d in [18, 22] and m_c/m_u in [440, 580] (lattice ratios, proof text) and |V_us| in
    W = (0.22176, 0.22705) (three standard deviations of the stored global fit and of the stored direct
    value, joined), cos phi = 1, 1/2, -1/2, -1 give |V_us| outside W.
(3) cos phi = 0 gives |V_us| in (0.2111, 0.2350), which contains W; at the Nf = 2+1+1 central lattice
    ratios |V_us| is in (0.22256, 0.22257), inside W; at the Nf = 2+1 central ratios it is in
    (0.22054, 0.22055), below W; the stored M_Z masses have central ratios inside both windows.
(4) every (x, y, |V_us|) in the boxes needs cos phi in (-0.42, 0.36): |cos phi| < 1/2.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise, quantity

X_LO, X_HI = F(1, 22), F(1, 18)          # m_d/m_s
Y_LO, Y_HI = F(1, 580), F(1, 440)        # m_u/m_c
GRID = 10 ** 30


def window():
    g = quantity("quantity.ckm-vus-magnitude")
    # global fit 0.22501 +- 0.00068 (stored value); direct 0.22431 +- 0.00085 (stored note)
    return (F(22431, 10 ** 5) - 3 * F(85, 10 ** 5), g + 3 * F(68, 10 ** 5))


def isqrt(n):
    if n < 2:
        return n
    r = 1 << ((n.bit_length() + 1) // 2)
    while True:
        z = (r + n // r) // 2
        if z >= r:
            return r
        r = z


def sqrt_lo(q):
    q = F(q)
    return F(isqrt((q.numerator * GRID * GRID) // q.denominator), GRID)


def sqrt_hi(q):
    return sqrt_lo(q) + F(1, GRID)


def v2(x, y, c, s):
    """|V_us|^2 for given x, y, cos phi = c and a value s of sqrt(x y)"""
    return (x + y - 2 * c * s) / ((1 + x) * (1 + y))


def v2_bounds(c):
    """certified bounds of |V_us|^2 over the box, for fixed cos phi = c (monotone pieces separately:
    numerator and denominator bounded independently, so the bounds are safe, not tight)"""
    den_lo, den_hi = (1 + X_LO) * (1 + Y_LO), (1 + X_HI) * (1 + Y_HI)
    s_lo, s_hi = sqrt_lo(X_LO * Y_LO), sqrt_hi(X_HI * Y_HI)
    if c >= 0:
        num_lo, num_hi = X_LO + Y_LO - 2 * c * s_hi, X_HI + Y_HI - 2 * c * s_lo
    else:
        num_lo, num_hi = X_LO + Y_LO - 2 * c * s_lo, X_HI + Y_HI - 2 * c * s_hi
    assert num_lo > 0
    return num_lo / den_hi, num_hi / den_lo


def herm(b):
    """B B^dag for B = [[k, x], [y, 0]] given as ((k, x), (y, 0)) with complex entries"""
    (k, x), (y, z) = b
    a = k * k.conjugate() + x * x.conjugate()
    off = k * y.conjugate() + x * z.conjugate()
    d = y * y.conjugate() + z * z.conjugate()
    return a.real, off, d.real


class G:
    """Gaussian rationals"""
    def __init__(self, re, im=0):
        self.re, self.im = F(re), F(im)
    def __add__(self, o): o = o if isinstance(o, G) else G(o); return G(self.re + o.re, self.im + o.im)
    def __sub__(self, o): o = o if isinstance(o, G) else G(o); return G(self.re - o.re, self.im - o.im)
    def __mul__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    def __neg__(self): return G(-self.re, -self.im)
    def conjugate(self): return G(self.re, -self.im)
    @property
    def real(self): return self.re
    def abs2(self): return self.re ** 2 + self.im ** 2


def gst_identity(k, x, y):
    """returns (lhs, rhs) of cos^2(2 theta) = (trH - 2|det B|)/(trH + 2|det B|) with |det B| = |x||y|
    taken as |x|^2 (valid when |x| = |y|)"""
    a, off, d = herm(((G(k), x), (y, G(0))))
    z2 = ((a - d) / 2) ** 2
    h2 = z2 + off.abs2()
    tr = a + d
    det2 = x.abs2() * y.abs2()            # |det B|^2
    return z2 / h2, (tr - 2 * x.abs2()) / (tr + 2 * x.abs2()), det2 == x.abs2() ** 2


def check_light_angle_is_the_gst_relation():
    premise("neutrino.breaking-relation")
    premise("synthesis.solar-angle-light-plane-sum-rule")
    premise("synthesis.series-family-structures-give-no-lopsided-second-stage")
    k = F(2, 3)
    cases = [(G(1, 2), 1, 46), (G(1, 2), -1, 46), (G(3, -5), 1, 307), (G(-2, 7), -1, 478), (G(1, 9), 1, 739)]
    ok = True
    for x, sgn, den in cases:
        y = x * sgn                       # symmetric (y = x) or antisymmetric (y = -x) stage
        l, r, same = gst_identity(k, x, y)
        # both sides equal k^2/(k^2 + 4|x|^2) = 1/(1 + 9|x|^2), tabulated
        ok = ok and same and l == r == F(1, den) == 1 / (1 + 9 * x.abs2())
        yc = x.conjugate()               # Hermitian odd stage, y = conj(x): also |x| = |y|
        l, r, same = gst_identity(k, x, yc)
        ok = ok and same and l == r == F(1, den)
    # tabulated: x = y = 1 + 2i gives cos^2(2 theta) = 1/46
    l, r, _ = gst_identity(k, G(1, 2), G(1, 2))
    ok = ok and l == F(1, 46)
    # control: a lopsided block y = 2x breaks the relation
    l, r, same = gst_identity(k, G(1, 2), G(1, 2) * 2)
    ok = ok and not same and l != r
    GA.check("one-type light planes: tan^2 theta = sigma2/sigma1 (GST), lopsided blocks excluded", ok)
    return ok


def overlap(bu, bd):
    """|<light_u | heavy_d>|^2 = (1 - h_u.h_d/(|h_u||h_d|))/2, returned as the pair (h_u.h_d)^2 and
    |h_u|^2 |h_d|^2 with the sign of h_u.h_d, so that no square root is needed"""
    au, ou, du = herm(bu)
    ad, od, dd = herm(bd)
    zu, zd = (au - du) / 2, (ad - dd) / 2
    dot = zu * zd + (ou * od.conjugate()).real
    return dot, (zu * zu + ou.abs2()) * (zd * zd + od.abs2())


def check_overlap_formula():
    premise("synthesis.solar-angle-light-plane-sum-rule")
    premise("synthesis.residual-s2-decouples-first-family-from-ckm-and-pmns")
    k = G(F(2, 3))
    ok = True
    # instances: up x_u, down x_d with relative phase; formula through squared quantities:
    # 1 - 2V^2 = cos(Theta) = cos2tu cos2td + sin2tu sin2td cos(phi)
    table = [(G(F(1, 10)), G(F(1, 3)), F(26, 405), F(872, 164025)),
             (G(0, F(1, 10)), G(F(1, 3)), F(4, 81), F(872, 164025)),
             (G(F(1, 10)), G(F(-1, 3)), F(14, 405), F(872, 164025)),
             (G(F(3, 4), F(1, 20)), G(F(2, 5), F(-1, 7)), F(509, 2835), F(7822876, 200930625))]
    for xu, xd, dot_want, nn_want in table:
        dot, nn = overlap(((k, xu), (xu, G(0))), ((k, xd), (xd, G(0))))
        au, ou, du = herm(((k, xu), (xu, G(0))))
        ad, od, dd = herm(((k, xd), (xd, G(0))))
        zu, zd = (au - du) / 2, (ad - dd) / 2
        # h_u.h_d = z_u z_d + |b_u||b_d| cos(phi), with |b_u||b_d| cos(phi) = Re(b_u conj(b_d))
        ok = ok and dot == zu * zd + (ou * od.conjugate()).real == dot_want and nn == nn_want
        # cos(phi) from the phases of the off-diagonal entries: Re(b_u conj b_d)^2 <= |b_u|^2 |b_d|^2
        ok = ok and (ou * od.conjugate()).real ** 2 <= ou.abs2() * od.abs2()
    # tabulated: the quarter-turn instance (x_u imaginary, x_d real) has Re(b_u conj b_d) = 0
    au, ou, du = herm(((k, G(0, F(1, 10))), (G(0, F(1, 10)), G(0))))
    ad, od, dd = herm(((k, G(F(1, 3))), (G(F(1, 3)), G(0))))
    ok = ok and (ou * od.conjugate()).real == 0 and (ou * od.conjugate()).im == F(-2, 135)
    GA.check("|V_us|^2 = (1 - cos Theta)/2, cos Theta = c2u c2d + s2u s2d cos(phi), phi physical", ok)
    return ok


def check_real_and_third_turn_phases_miss_vus():
    premise("synthesis.solar-angle-light-plane-sum-rule")
    premise("families.faces-ordered-what-identification-requires-first")
    w_lo, w_hi = window()
    ok = (w_lo, w_hi) == (F(22176, 10 ** 5), F(22705, 10 ** 5))
    hi1 = v2_bounds(F(1))[1]
    hi2 = v2_bounds(F(1, 2))[1]
    lo3 = v2_bounds(F(-1, 2))[0]
    lo4 = v2_bounds(F(-1))[0]
    ok = ok and hi1 < F(196, 1000) ** 2 and hi2 < F(2163, 10 ** 4) ** 2
    ok = ok and lo3 > F(2301, 10 ** 4) ** 2 and lo4 > F(247, 1000) ** 2
    ok = ok and F(2163, 10 ** 4) < w_lo and w_hi < F(2301, 10 ** 4)
    GA.check("cos phi = 1, 1/2, -1/2, -1 give |V_us| < 0.196, < 0.2163, > 0.2301, > 0.247: outside W", ok)
    return ok


def check_quarter_turn_band_contains_vus():
    premise("synthesis.solar-angle-light-plane-sum-rule")
    premise("families.faces-ordered-what-identification-requires-first")
    w_lo, w_hi = window()
    lo, hi = v2_bounds(F(0))
    ok = F(2111, 10 ** 4) ** 2 < lo and hi < F(2350, 10 ** 4) ** 2
    ok = ok and lo < w_lo ** 2 and w_hi ** 2 < hi
    # central lattice ratios: m_s/m_ud = 27.227, m_u/m_d = 0.465, m_c/m_s = 11.766
    sud, ud, cs = F(27227, 1000), F(465, 1000), F(11766, 1000)
    x0 = 2 / (sud * (1 + ud))                      # m_d/m_s
    y0 = 2 * ud / (cs * sud * (1 + ud))            # m_u/m_c
    c2 = v2(x0, y0, F(0), F(0))
    ok = ok and F(22256, 10 ** 5) ** 2 < c2 < F(22257, 10 ** 5) ** 2
    ok = ok and X_LO < x0 < X_HI and Y_LO < y0 < Y_HI
    # the Nf = 2+1 central ratios (m_s/m_ud = 27.42, m_u/m_d = 0.485, m_c/m_s = 11.82) give a quarter-turn
    # value below W: the central value depends on which lattice average is used
    sud3, ud3, cs3 = F(2742, 100), F(485, 1000), F(1182, 100)
    x3 = 2 / (sud3 * (1 + ud3))
    y3 = 2 * ud3 / (cs3 * sud3 * (1 + ud3))
    c3 = v2(x3, y3, F(0), F(0))
    ok = ok and F(22054, 10 ** 5) ** 2 < c3 < F(22055, 10 ** 5) ** 2 and c3 < w_lo ** 2
    ok = ok and X_LO < x3 < X_HI and Y_LO < y3 < Y_HI
    # the stored M_Z running masses: central ratios inside both windows
    md, ms = quantity("quantity.down-quark-mass-mz"), quantity("quantity.strange-quark-mass-mz")
    mu, mc = quantity("quantity.up-quark-mass-mz"), quantity("quantity.charm-quark-mass-mz")
    xs, ys = md / ms, mu / (1000 * mc)
    ok = ok and X_LO < xs < X_HI and Y_LO < ys < Y_HI
    GA.check("cos phi = 0: |V_us| in (0.2111, 0.2350), containing W; central values 0.22257 (2+1+1), 0.22055 (2+1)", ok)
    return ok


def check_phase_window():
    premise("synthesis.solar-angle-light-plane-sum-rule")
    w_lo, w_hi = window()
    # cos phi = (x + y - V^2 (1 + x)(1 + y)) / (2 sqrt(x y)); safe bounds over the boxes
    s_lo = sqrt_lo(X_LO * Y_LO)
    c_hi = (X_HI + Y_HI - w_lo ** 2 * (1 + X_LO) * (1 + Y_LO)) / (2 * s_lo)
    c_lo = (X_LO + Y_LO - w_hi ** 2 * (1 + X_HI) * (1 + Y_HI)) / (2 * s_lo)
    ok = c_lo < 0 < c_hi
    ok = ok and F(-42, 100) < c_lo < F(-41, 100) and F(35, 100) < c_hi < F(36, 100)
    ok = ok and F(-1, 2) < c_lo and c_hi < F(1, 2)
    GA.check("every admissible point needs cos phi in (-0.42, 0.36): |cos phi| < 1/2", ok)
    return ok
