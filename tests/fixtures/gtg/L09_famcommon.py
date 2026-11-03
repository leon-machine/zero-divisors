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
