"""families.koide-class-crossing-fit-conclusion: exact checks in Z[sqrt 2] and Q(x).

The conclusion clause (fit, not mechanism; no structure marks x*) is the paper's pre-registered refutation
condition applied, and is checked only through the computed values it rests on.
(1) S_2 reduction: for the sqrt(m)-triple (1, 1, rho), Q = (2 + rho^2)/(2 + rho)^2 = 2/3 iff rho^2 - 8 rho - 2 = 0
    (polynomial identity 3(2 + rho^2) - 2(2 + rho)^2 = rho^2 - 8 rho - 2, checked at 4 rationals, degree 2);
    rho = 4 + 3 sqrt 2 is a root, the other root 4 - 3 sqrt 2 is negative, and Q(1, 1, 4 + 3 sqrt 2) = 2/3
    exactly; in Fourier coordinates (a + |Gamma|)/(a - |Gamma|/2) at |Gamma| = a sqrt 2 equals
    (1 + sqrt 2)(2 + sqrt 2) = 4 + 3 sqrt 2. K = rho^4 = (34 + 24 sqrt 2)^2 = 2308 + 1632 sqrt 2, and
    K lies in [4615.5, 4616.5) (prints as 4616).
(2) The crossing equation on the skeleton spectrum (heavy 1 + 6x + 6x^2 over light 1 + x, the premise):
    (1 + 6x + 6x^2)/(1 + x) = 6x + 1/(1 + x) as a rational-function identity; its derivative is
    6 - 1/(1 + x)^2, and 6(1 + x)^2 - 1 = 5 + 12x + 6x^2 has positive coefficients, so the crossing is unique
    on x > 0. Exact sign evaluation of g(x) = 6x^2 + 6x + 1 - K(1 + x) in Z[sqrt 2]: g(769.33245) < 0 <
    g(769.33255), so x* prints as 769.3325; K/6 lies in [769.33275, 769.33285) (prints as 769.3328); and
    K/6 - x* = 1/(6(1 + x*)) lies in (2.1, 2.2) x 10^-4 ("within 2.2 x 10^-4").
(3) The nominated canonical depth tanh^2 r = 1/2 is x = 1 (x = sinh^2 r = t/(1 - t)), where the ratio is
    13/2, far from K.
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

    def __truediv__(s, o):
        o = CY._c(o)
        n = o.nsq()
        if n == 0:
            raise ZeroDivisionError
        return s * o.conj() * CY(1 / n)

    def __bool__(s):
        return s.a != 0 or s.b != 0

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

RHO = R2(4, 3)


def g_of(x):
    K = RHO * RHO * RHO * RHO
    return R2(6 * x * x + 6 * x + 1) - K * R2(1 + x)


def check_s2_reduction_and_the_root():
    ok = True
    for r in (F(0), F(1), F(-2), F(7, 3)):
        ok = ok and 3 * (2 + r * r) - 2 * (2 + r) ** 2 == r * r - 8 * r - 2
    ok = ok and RHO * RHO - R2(8) * RHO - R2(2) == R2(0)
    other = R2(4, -3)
    ok = ok and other * other - R2(8) * other - R2(2) == R2(0) and other.sign() < 0 and RHO.sign() > 0
    num = R2(2) + RHO * RHO
    den = (R2(2) + RHO) * (R2(2) + RHO)
    ok = ok and num * R2(3) == den * R2(2)
    ok = ok and R2(1, 1) * R2(2, 1) == RHO
    K = RHO * RHO * RHO * RHO
    ok = ok and RHO * RHO == R2(34, 24) and K == R2(2308, 1632)
    ok = ok and (K - R2(F(46155, 10))).sign() >= 0 and (K - R2(F(46165, 10))).sign() < 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_s2_reduction_and_the_root"; return _tp_rv


def check_crossing_unique_and_bracketed():
    premise("families.skeleton-rank-one-plus-ordering-shift")
    X = GA.RF.var()
    lhs = (GA.RF1 + GA.RF.const(6) * X + GA.RF.const(6) * X * X) / (GA.RF1 + X)
    ok = lhs.eqrf(GA.RF.const(6) * X + GA.RF1 / (GA.RF1 + X))
    d = lhs.deriv()
    ok = ok and d.eqrf(GA.RF.const(6) - GA.RF1 / ((GA.RF1 + X) * (GA.RF1 + X)))
    poly = GA.padd(GA.pmul([F(6)], GA.pmul([F(1), F(1)], [F(1), F(1)])), [F(-1)])
    ok = ok and poly == [F(5), F(12), F(6)] and all(c > 0 for c in poly)
    lo, hi = F(76933245, 10 ** 5), F(76933255, 10 ** 5)
    ok = ok and g_of(lo).sign() < 0 and g_of(hi).sign() > 0
    K = RHO * RHO * RHO * RHO
    k6lo, k6hi = F(76933275, 10 ** 5), F(76933285, 10 ** 5)
    ok = ok and (K - R2(6 * k6lo)).sign() >= 0 and (K - R2(6 * k6hi)).sign() < 0
    disp_lo, disp_hi = 1 / (6 * (1 + hi)), 1 / (6 * (1 + lo))
    ok = ok and F(21, 10 ** 5) < disp_lo and disp_hi < F(22, 10 ** 5)
    # x* = K/6 - 1/(6(1 + x*)): the bracket of x* plus the displacement bracket reproduces the K/6 bracket
    ok = ok and k6lo - F(1, 10 ** 4) < lo + disp_lo and hi + disp_hi < k6hi + F(1, 10 ** 4)
    _tp_rv = (ok); assert _tp_rv is not False, "check_crossing_unique_and_bracketed"; return _tp_rv


def check_canonical_depth_fails():
    premise("families.skeleton-rank-one-plus-ordering-shift")
    t = F(1, 2)
    x = t / (1 - t)
    ok = x == 1
    ratio = (1 + 6 * x + 6 * x * x) / (1 + x)
    ok = ok and ratio == F(13, 2)
    K = RHO * RHO * RHO * RHO
    ok = ok and (K - R2(100 * ratio)).sign() > 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_canonical_depth_fails"; return _tp_rv
