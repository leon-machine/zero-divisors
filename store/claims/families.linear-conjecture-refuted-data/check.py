"""families.linear-conjecture-refuted-data: exact checks on the stated (PDG 2024) charged-lepton masses.

All square roots are bracketed by rational interval arithmetic (integer square roots); degrees are converted
with rational bounds on pi and alternating-series bounds on sin and cos. The repair argument (light masses
second order, the flagged heavy-family assumption) is a reading and is checked only through its algebraic
core, the chain Q_v = 1/(3 cos^2 theta).
(1) Equal singlet-doublet split gives Q_v = 2/3 for any v: Q_v = |v|^2/(3 s^2) with s = v.u, and
    |v|^2 = s^2 + |d|^2, so s^2 = |d|^2 iff Q_v = 2/3 (checked on sample vectors, both sides of the condition).
(2) Linear coordinate refuted: Q_m = sum m^2/(sum m)^2 lies in [0.89355, 0.89365) (prints as 0.8936),
    exceeds 2/3 by more than 1/5, and theta_m = arccos(sqrt(1/(3 Q_m))) lies in [52.35, 52.45) degrees
    (prints as 52.4), through tan^2 theta_m = 3 Q_m - 1.
(3) sqrt(m) coordinate passes: Q_sqrt(m) lies in [0.66666445, 0.66666455), the stated 0.6666645; 2/3 - Q lies in (1.5, 2.5) x 10^-6 (two parts in
    10^6) and (2/3 - Q)/(2/3) in (2.5, 3.5) x 10^-6 (three relative).
(4) The Koide prediction of m_tau: the larger root of t^2 - 4 S t + 3 M - 2 S^2 = 0 (S = sqrt(m_e) + sqrt(m_mu),
    M = m_e + m_mu) gives m_tau = t^2 in [1776.965, 1776.975) (prints as 1776.97), and (pred - 1776.93)/0.09
    lies in (0.4, 0.5) and rounds to 0.4: agreement within half a standard deviation. The quadratic is checked to be the Koide
    condition 2 (S + t)^2 = 3 (M + t^2).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

# ---- exact helpers: Q(zeta_3), Z[sqrt 2], integer square roots, rational bounds ----
class CY(object):
    """a + b zeta with zeta^2 = -1 - zeta (zeta = e^{2 pi i/3}), exact."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def _c(o):
        return o if isinstance(o, CY) else CY(o)

    def __add__(s, o):
        o = CY._c(o)
        return CY(s.a + o.a, s.b + o.b)
    __radd__ = __add__

    def __sub__(s, o):
        o = CY._c(o)
        return CY(s.a - o.a, s.b - o.b)

    def __rsub__(s, o):
        return CY._c(o) - s

    def __neg__(s):
        return CY(-s.a, -s.b)

    def __mul__(s, o):
        o = CY._c(o)
        return CY(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a - s.b * o.b)
    __rmul__ = __mul__

    def conj(s):
        return CY(s.a - s.b, -s.b)

    def re(s):
        return s.a - s.b / 2

    def nsq(s):
        """|z|^2 = a^2 - ab + b^2 (rational)."""
        return s.a * s.a - s.a * s.b + s.b * s.b

    def __eq__(s, o):
        o = CY._c(o)
        return s.a == o.a and s.b == o.b

    def __ne__(s, o):
        return not s.__eq__(o)

    def __hash__(s):
        return hash((s.a, s.b))


ZETA = CY(0, 1)
Z2 = ZETA * ZETA
ISQ3 = Z2 - ZETA          # zeta^2 - zeta = -i sqrt(3)


class R2(object):
    """p + q sqrt(2), exact."""
    __slots__ = ("p", "q")

    def __init__(self, p=0, q=0):
        self.p, self.q = F(p), F(q)

    @staticmethod
    def _c(o):
        return o if isinstance(o, R2) else R2(o)

    def __add__(s, o):
        o = R2._c(o)
        return R2(s.p + o.p, s.q + o.q)
    __radd__ = __add__

    def __sub__(s, o):
        o = R2._c(o)
        return R2(s.p - o.p, s.q - o.q)

    def __mul__(s, o):
        o = R2._c(o)
        return R2(s.p * o.p + 2 * s.q * o.q, s.p * o.q + s.q * o.p)
    __rmul__ = __mul__

    def __eq__(s, o):
        o = R2._c(o)
        return s.p == o.p and s.q == o.q

    def __ne__(s, o):
        return not s.__eq__(o)

    def sign(s):
        """Exact sign of p + q sqrt 2."""
        if s.q == 0 or s.p == 0 or (s.p > 0) == (s.q > 0):
            v = s.p if s.q == 0 else (s.q if s.p == 0 else s.p)
            return (v > 0) - (v < 0)
        big_p = s.p * s.p > 2 * s.q * s.q
        lead = s.p if big_p else s.q
        return (lead > 0) - (lead < 0)


def isqrt(n):
    """floor(sqrt(n)) for an integer n >= 0 (Newton)."""
    if n < 2:
        return n
    x = 1 << ((n.bit_length() + 1) // 2)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def sqrt_bounds(m, digits=10):
    """Rationals lo <= sqrt(m) <= hi with hi - lo = 10^-digits / den(m)."""
    m = F(m)
    scale = 10 ** digits
    lo_int = isqrt(m.numerator * m.denominator * scale * scale)
    lo, hi = F(lo_int, m.denominator * scale), F(lo_int + 1, m.denominator * scale)
    assert lo * lo <= m <= hi * hi
    return lo, hi


# PDG 2024 charged-lepton masses (MeV) and the tau uncertainty
ME, MU, MT = F(51099895, 10 ** 8), F(1056583755, 10 ** 7), F(177693, 100)
MT_ERR = F(9, 100)
# ---- end of exact helpers ----

PI_LO, PI_HI = F(314159265358, 10 ** 11), F(314159265359, 10 ** 11)
SAMPLE_V = [[F(1), F(2), F(3)], [F(3), F(-1), F(5, 2)], [F(1), F(1), F(1)], [F(7), F(0), F(-2)]]


def sin_cos_bounds(x, terms=9):
    """Rational brackets of sin x and cos x for 0 < x < 1 (alternating series with decreasing terms)."""
    sp, cp = [], []
    s, term = F(0), x
    for k in range(terms):
        s += term
        sp.append(s)
        term = -term * x * x / ((2 * k + 2) * (2 * k + 3))
    c, term = F(0), F(1)
    for k in range(terms):
        c += term
        cp.append(c)
        term = -term * x * x / ((2 * k + 1) * (2 * k + 2))
    return (min(sp[-2:]), max(sp[-2:])), (min(cp[-2:]), max(cp[-2:]))


def tan2_bounds(deg_lo, deg_hi):
    """Bounds on tan^2 at angles deg (degrees, rational) from pi bounds: (upper of tan^2(deg_lo), lower of tan^2(deg_hi))."""
    out = []
    for deg, want_upper in ((deg_lo, True), (deg_hi, False)):
        x = deg * (PI_HI if want_upper else PI_LO) / 180
        (slo, shi), (clo, chi) = sin_cos_bounds(x)
        t = shi / clo if want_upper else slo / chi
        out.append(t * t)
    return out


def sqrt_sum_bounds(ms):
    bs = [sqrt_bounds(m) for m in ms]
    return sum(b[0] for b in bs), sum(b[1] for b in bs), bs


def check_equal_split_means_two_thirds():
    premise("families.alignment-computed-thirteenth-refutation-democracy-one")
    ok = True
    for v in SAMPLE_V:
        s_sq = sum(v) ** 2 / 3                       # s = v . (1,1,1)/sqrt 3
        nv = sum(x * x for x in v)
        d_sq = nv - s_sq
        Q = nv / sum(v) ** 2
        ok = ok and Q == nv / (3 * s_sq)
        ok = ok and (Q == F(2, 3)) == (s_sq == d_sq)
    # a vector on the cone: (1 + sqrt2, 1 - sqrt2/2, 1 - sqrt2/2) has s^2 = |d|^2 and Q = 2/3 exactly
    w = [R2(1, 1), R2(1, F(-1, 2)), R2(1, F(-1, 2))]
    tot = w[0] + w[1] + w[2]
    nw = w[0] * w[0] + w[1] * w[1] + w[2] * w[2]
    ok = ok and nw * R2(3) == tot * tot * R2(2)
    _tp_rv = (ok); assert _tp_rv is not False, "check_equal_split_means_two_thirds"; return _tp_rv


def check_linear_coordinate_refuted():
    Qm = (ME ** 2 + MU ** 2 + MT ** 2) / (ME + MU + MT) ** 2
    ok = F(89355, 10 ** 5) <= Qm < F(89365, 10 ** 5) and Qm - F(2, 3) > F(1, 5)
    t2 = 3 * Qm - 1                                   # tan^2 theta_m, cos^2 theta_m = 1/(3 Q_m)
    up_lo, low_hi = tan2_bounds(F(5235, 100), F(5245, 100))
    ok = ok and up_lo <= t2 < low_hi
    ok = ok and 1 / (1 + t2) == 1 / (3 * Qm)
    _tp_rv = (ok); assert _tp_rv is not False, "check_linear_coordinate_refuted"; return _tp_rv


def check_sqrt_coordinate_passes():
    S_lo, S_hi, _ = sqrt_sum_bounds([ME, MU, MT])
    M = ME + MU + MT
    Q_lo, Q_hi = M / (S_hi * S_hi), M / (S_lo * S_lo)
    ok = F(66666445, 10 ** 8) <= Q_lo and Q_hi < F(66666455, 10 ** 8)
    dev_lo, dev_hi = F(2, 3) - Q_hi, F(2, 3) - Q_lo
    ok = ok and F(15, 10 ** 7) < dev_lo and dev_hi < F(25, 10 ** 7)
    ok = ok and F(25, 10 ** 7) < dev_lo * F(3, 2) and dev_hi * F(3, 2) < F(35, 10 ** 7)
    _tp_rv = (ok); assert _tp_rv is not False, "check_sqrt_coordinate_passes"; return _tp_rv


# sample (S, M, t) points for the polynomial identity relating the quadratic to the Koide condition
KOIDE_SAMPLES = ((F(3), F(2), F(5)), (F(1, 2), F(7, 3), F(-4)), (F(2), F(1), F(1, 3)), (F(5), F(0), F(2)))


def check_tau_mass_prediction():
    ok = True
    # the quadratic is the Koide condition: 2(S + t)^2 - 3(M + t^2) = -(t^2 - 4 S t + 3 M - 2 S^2)
    for S, M, t in KOIDE_SAMPLES:
        ok = ok and 2 * (S + t) ** 2 - 3 * (M + t * t) == -(t * t - 4 * S * t + 3 * M - 2 * S * S)
    (e_lo, e_hi), (m_lo, m_hi) = sqrt_bounds(ME), sqrt_bounds(MU)
    M = ME + MU
    S_lo, S_hi = e_lo + m_lo, e_hi + m_hi
    # the larger root t = (4 S + sqrt(24 S^2 - 12 M)) / 2 increases with S, so the brackets carry over
    d_lo, _ = sqrt_bounds(24 * S_lo * S_lo - 12 * M)
    _, d_hi = sqrt_bounds(24 * S_hi * S_hi - 12 * M)
    pred_lo, pred_hi = ((4 * S_lo + d_lo) / 2) ** 2, ((4 * S_hi + d_hi) / 2) ** 2
    ok = ok and pred_lo <= pred_hi
    # prints as 1776.97: both bounds round to it at two decimals
    ok = ok and round(pred_lo, 2) == F(177697, 100) and round(pred_hi, 2) == F(177697, 100)
    # the pull (pred - 1776.93)/0.09 lies in (0.4, 0.5) and rounds to 0.4, by hand (1776.97 - 1776.93)/0.09 = 0.44
    pull_lo, pull_hi = (pred_lo - MT) / MT_ERR, (pred_hi - MT) / MT_ERR
    ok = ok and F(4, 10) < pull_lo and pull_hi < F(5, 10)
    ok = ok and round(pull_lo, 1) == F(4, 10) and round(pull_hi, 1) == F(4, 10)
    _tp_rv = (ok); assert _tp_rv is not False, "check_tau_mass_prediction"; return _tp_rv
