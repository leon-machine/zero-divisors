#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""series.py: exact truncated power series, rational-function helpers, exact roots, small exact
number fields and certified rational bounds, shared by the store's checks (ROADMAP item 6).

Conventions (fixed here; the GTG conventions of docs/gtg-dictionary.md C1-C11
live in gtg.py, and this module carries none of them):

- Everything is exact: fractions.Fraction, ints, GA.RF, and the classes below. No floats, no math
  module, no integer true division.
- A truncated power series "to order N" is a coefficient list [c0, c1, ..., cN] in a formal
  variable x (the GA.py section 6 convention: coefficients 0..N are kept). Functions that take N
  return lists of length N + 1, except ps_deriv (one shorter: the derivative of a series known to
  order N is known to order N - 1).
- A Laurent series is a pair (v, coeffs) meaning x^v * (coeffs[0] + coeffs[1] x + ...), with
  coeffs[0] != 0 after normalisation (laurent()); the zero series is (0, []).
- Rational functions in one variable are GA.RF (gcd-reduced num/den coefficient lists).
- Certified bounds return a pair (lo, hi) of Fractions with lo <= true value <= hi. Each function
  states the source check whose semantics it reproduces exactly, so migrated checks keep their
  numbers bit for bit.
- Exact number classes: QS (Q(sqrt d), a + b sqrt d), CY (Q(zeta_3), a + b zeta with
  zeta^2 = -1 - zeta, the families checks' class, unchanged), R2(p, q) = p + q sqrt 2 (a QS).

Pure functions; no I/O at import; Brython-safe (no dict.setdefault, no int.bit_count).
"""

from fractions import Fraction

import GA

F = Fraction

__all__ = [
    "ps_trunc", "ps_zero", "ps_one", "ps_var", "ps_const", "ps_add", "ps_sub", "ps_neg",
    "ps_scale", "ps_mul", "ps_inv", "ps_div", "ps_pow_int", "ps_pow_rat", "ps_pow", "ps_sqrt",
    "ps_exp", "ps_log", "ps_compose", "ps_int", "ps_integrate", "ps_deriv", "ps_eval",
    "ps_valuation", "ps_shift", "ps_reversion", "taylor_exp", "taylor_sin", "taylor_cos",
    "taylor_atan", "taylor_log1p", "taylor_binomial",
    "laurent", "laurent_add", "laurent_mul", "laurent_inv", "laurent_shift", "laurent_coeff",
    "rf_var", "rf_const", "rf_poly", "rf_pow", "rf_taylor", "pcompose", "pbinomial",
    "iroot", "isqrt", "qpow", "qsqrt", "is_square",
    "QS", "R2", "CY", "ZETA", "Z2", "ISQ3",
    "round_down", "round_up", "sqrt_bounds", "iroot_bracket", "arctan_inv_bracket", "pi_bracket",
    "atan_bounds", "pi_bounds", "exp_bracket", "exp_bounds", "atanh_bounds", "ln_bounds",
    "log_bounds", "rounds_to", "root_rounds_to", "interval_rounds_to",
]


# ---------------------------------------------------------------------------
# 1. truncated power series (coefficient lists to order N)
# ---------------------------------------------------------------------------

def ps_trunc(a, N):
    """Truncate or zero-pad a coefficient list to order N (length N + 1); GA.ps_trunc."""
    return GA.ps_trunc(a, N)


def ps_zero(N):
    """The zero series to order N."""
    return [F(0)] * (N + 1)


def ps_one(N):
    """The constant series 1 to order N."""
    return ps_const(1, N)


def ps_var(N):
    """The series x to order N (N >= 1)."""
    out = ps_zero(N)
    if N >= 1:
        out[1] = F(1)
    return out


def ps_const(c, N):
    """The constant series c to order N."""
    out = ps_zero(N)
    out[0] = F(c)
    return out


def ps_add(a, b, N):
    """a + b to order N."""
    a, b = GA.ps_trunc(a, N), GA.ps_trunc(b, N)
    return [x + y for x, y in zip(a, b)]


def ps_sub(a, b, N):
    """a - b to order N."""
    a, b = GA.ps_trunc(a, N), GA.ps_trunc(b, N)
    return [x - y for x, y in zip(a, b)]


def ps_neg(a):
    """-a (same length)."""
    return [-x for x in a]


def ps_scale(c, a, N):
    """c a to order N for a scalar c."""
    c = F(c)
    return [c * x for x in GA.ps_trunc(a, N)]


def ps_mul(a, b, N):
    """a b to order N; GA.ps_mul."""
    return GA.ps_mul(a, b, N)


def ps_inv(a, N):
    """1/a to order N for a[0] != 0; GA.ps_inv."""
    return GA.ps_inv(a, N)


def ps_div(a, b, N):
    """a/b to order N for b[0] != 0."""
    return GA.ps_mul(a, GA.ps_inv(b, N), N)


def ps_pow_int(a, n, N):
    """a^n to order N for an integer n (n < 0 needs a[0] != 0), by repeated squaring."""
    if n < 0:
        return ps_pow_int(GA.ps_inv(a, N), -n, N)
    out, base = ps_one(N), GA.ps_trunc(a, N)
    while n:
        if n & 1:
            out = GA.ps_mul(out, base, N)
        n >>= 1
        if n:
            base = GA.ps_mul(base, base, N)
    return out


def ps_pow_rat(a, alpha, N):
    """a^alpha to order N for a[0] == 1 and rational alpha (J.C.P. Miller); GA.ps_pow_rat."""
    return GA.ps_pow_rat(a, alpha, N)


def ps_pow(a, alpha, N):
    """a^alpha to order N for a[0] != 0 with a[0]^alpha rational (qpow), any rational alpha."""
    a = GA.ps_trunc(a, N)
    a0 = F(a[0])
    if a0 == 0:
        raise ZeroDivisionError("ps_pow needs a nonzero constant term")
    lead = qpow(a0, alpha)
    unit = [x / a0 for x in a]
    return [lead * x for x in GA.ps_pow_rat(unit, alpha, N)]


def ps_sqrt(a, N):
    """sqrt(a) to order N for a[0] a rational square (principal, positive root)."""
    return ps_pow(a, F(1, 2), N)


def ps_exp(a, N):
    """exp(a) to order N for a[0] == 0, by b' = a' b."""
    a = GA.ps_trunc(a, N)
    if a[0] != 0:
        raise ValueError("ps_exp needs a(0) = 0 (exp of a nonzero rational is irrational)")
    b = ps_zero(N)
    b[0] = F(1)
    for n in range(1, N + 1):
        b[n] = sum((k * a[k] * b[n - k] for k in range(1, n + 1)), F(0)) / n
    return b


def ps_log(a, N):
    """log(a) to order N for a[0] == 1, as the integral of a'/a."""
    a = GA.ps_trunc(a, N)
    if a[0] != 1:
        raise ValueError("ps_log needs a(0) = 1")
    if N == 0:
        return [F(0)]
    q = GA.ps_mul(ps_deriv(a), GA.ps_inv(a, N - 1), N - 1)
    return ps_integrate(q, N)


def ps_compose(f, g, N):
    """f(g(x)) to order N for g[0] == 0; GA.ps_compose."""
    return GA.ps_compose(f, g, N)


def ps_int(a):
    """Termwise antiderivative with zero constant term, one longer than a; GA.ps_int."""
    return GA.ps_int(a)


def ps_integrate(a, N, c0=0):
    """Antiderivative with constant term c0, to order N."""
    out = GA.ps_trunc(GA.ps_int(a), N)
    out[0] = F(c0)
    return out


def ps_deriv(a):
    """Termwise derivative (length len(a) - 1)."""
    return [F(i) * a[i] for i in range(1, len(a))]


def ps_eval(a, x):
    """Exact value of the polynomial sum a[k] x^k at x (Horner)."""
    if isinstance(x, int):
        x = F(x)
    out = F(0)
    for c in reversed(a):
        out = out * x + c
    return out


def ps_valuation(a):
    """Index of the first nonzero coefficient, or None for the zero series (L09 series.lead)."""
    for k, c in enumerate(a):
        if c != 0:
            return k
    return None


def ps_shift(a, k, N):
    """x^k a to order N for k >= 0, or a / x^(-k) for k < 0 (requires the dropped terms to be 0)."""
    a = list(a)
    if k >= 0:
        return GA.ps_trunc([F(0)] * k + a, N)
    if any(c != 0 for c in a[:-k]):
        raise ValueError("ps_shift: series not divisible by x^%d" % (-k))
    return GA.ps_trunc(a[-k:], N)


def ps_reversion(f, N):
    """Compositional inverse g of f (f[0] == 0, f[1] != 0): f(g(x)) = x to order N."""
    f = GA.ps_trunc(f, N)
    if f[0] != 0 or f[1] == 0:
        raise ValueError("ps_reversion needs f(0) = 0 and f'(0) != 0")
    a1 = F(f[1])
    g = ps_zero(N)
    g[1] = 1 / a1
    x = ps_var(N)
    for _ in range(N):
        resid = ps_sub(GA.ps_compose(f, g, N), x, N)
        if all(c == 0 for c in resid):
            break
        g = ps_sub(g, ps_scale(1 / a1, resid, N), N)
    return g


def taylor_exp(N):
    """Coefficients of exp(x) to order N: 1/k!."""
    out, t = [], F(1)
    for k in range(N + 1):
        out.append(t)
        t = t / (k + 1)
    return out


def taylor_sin(N):
    """Coefficients of sin(x) to order N."""
    e = taylor_exp(N)
    return [(e[k] if k % 4 == 1 else (-e[k] if k % 4 == 3 else F(0))) for k in range(N + 1)]


def taylor_cos(N):
    """Coefficients of cos(x) to order N."""
    e = taylor_exp(N)
    return [(e[k] if k % 4 == 0 else (-e[k] if k % 4 == 2 else F(0))) for k in range(N + 1)]


def taylor_atan(N):
    """Coefficients of atan(x) to order N."""
    return [(F((-1) ** ((k - 1) // 2), k) if k % 2 == 1 else F(0)) for k in range(N + 1)]


def taylor_log1p(N):
    """Coefficients of log(1 + x) to order N."""
    return [F(0)] + [F((-1) ** (k + 1), k) for k in range(1, N + 1)]


def taylor_binomial(alpha, N):
    """Coefficients of (1 + x)^alpha to order N: binomial(alpha, k), rational alpha."""
    alpha = F(alpha)
    out, t = [], F(1)
    for k in range(N + 1):
        out.append(t)
        t = t * (alpha - k) / (k + 1)
    return out


# ---------------------------------------------------------------------------
# 2. Laurent series (v, coeffs) = x^v * sum coeffs[k] x^k
# ---------------------------------------------------------------------------

def laurent(coeffs, v=0):
    """Normalised Laurent series (v', c') with c'[0] != 0 (zero series: (0, []))."""
    coeffs = [F(c) if not hasattr(c, "conj") else c for c in coeffs]
    k = ps_valuation(coeffs)
    if k is None:
        return (0, [])
    return (v + k, coeffs[k:])


def laurent_coeff(L, n):
    """Coefficient of x^n in the Laurent series L."""
    v, c = L
    i = n - v
    return c[i] if 0 <= i < len(c) else F(0)


def laurent_add(A, B, top):
    """A + B keeping exponents up to and including top."""
    if not A[1]:
        return laurent([laurent_coeff(B, n) for n in range(B[0], top + 1)], B[0]) if B[1] else A
    if not B[1]:
        return laurent([laurent_coeff(A, n) for n in range(A[0], top + 1)], A[0])
    lo = min(A[0], B[0])
    return laurent([laurent_coeff(A, n) + laurent_coeff(B, n) for n in range(lo, top + 1)], lo)


def laurent_mul(A, B, top):
    """A B keeping exponents up to and including top."""
    if not A[1] or not B[1]:
        return (0, [])
    v = A[0] + B[0]
    N = top - v
    if N < 0:
        return (0, [])
    return laurent(GA.ps_mul(A[1], B[1], N), v)


def laurent_inv(A, top):
    """1/A keeping exponents up to and including top (A nonzero)."""
    if not A[1]:
        raise ZeroDivisionError("laurent_inv of zero")
    v = -A[0]
    N = top - v
    if N < 0:
        return (0, [])
    return laurent(GA.ps_inv(A[1], N), v)


def laurent_shift(A, k):
    """x^k A."""
    return (A[0] + k, list(A[1])) if A[1] else A


# ---------------------------------------------------------------------------
# 3. rational functions and polynomials (one variable; GA.RF does the arithmetic)
# ---------------------------------------------------------------------------

def rf_var():
    """The rational function t."""
    return GA.RF.var()


def rf_const(c):
    """The constant rational function c."""
    return GA.RF.const(c)


def rf_poly(coeffs):
    """The polynomial sum coeffs[k] t^k as a rational function."""
    return GA.RF([F(c) for c in coeffs])


def rf_pow(r, n):
    """r^n for an integer n (n < 0 needs r nonzero)."""
    if n < 0:
        return GA.RF1 / rf_pow(r, -n)
    out, base = GA.RF1, r
    while n:
        if n & 1:
            out = out * base
        n >>= 1
        if n:
            base = base * base
    return out


def rf_taylor(r, N):
    """Taylor coefficients of the rational function r at t = 0 to order N (den(0) != 0)."""
    if not r.num:
        return ps_zero(N)
    return GA.ps_mul(GA.ps_trunc(r.num, N), GA.ps_inv(GA.ps_trunc(r.den, N), N), N)


def pcompose(p, q):
    """The polynomial p(q(t)) (coefficient lists)."""
    out = []
    for c in reversed(p):
        out = GA.padd(GA.pmul(out, q), GA.pconst(c))
    return out


def pbinomial(n, k):
    """Binomial coefficient C(n, k) for integers (0 outside the range)."""
    if k < 0 or k > n:
        return 0
    out = 1
    for i in range(k):
        out = out * (n - i) // (i + 1)
    return out


# ---------------------------------------------------------------------------
# 4. exact roots
# ---------------------------------------------------------------------------

def iroot(n, k):
    """Exact integer k-th root of n >= 0, or None (the GTG engines' iroot)."""
    if n < 0:
        return None
    lo, hi = 0, 1
    while hi ** k <= n:
        hi *= 2
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** k <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo if lo ** k == n else None


def isqrt(n):
    """floor(sqrt(n)) for an integer n >= 0 (Newton; integers only)."""
    if n < 0:
        raise ValueError("isqrt of a negative integer")
    if n < 2:
        return n
    x = 1 << ((len(bin(n)) - 1) // 2)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def qpow(x, a):
    """x ** a for Fraction x > 0 and rational a, exact; raises ValueError if irrational."""
    x, a = F(x), F(a)
    if x == 0:
        if a > 0:
            return F(0)
        raise ZeroDivisionError("0 to a non-positive power")
    if x < 0:
        if a.denominator % 2 == 1:
            return -qpow(-x, a) if a.numerator % 2 else qpow(-x, a)
        raise ValueError("even root of a negative number")
    num, den = iroot(x.numerator, a.denominator), iroot(x.denominator, a.denominator)
    if num is None or den is None:
        raise ValueError("irrational power")
    return F(num, den) ** a.numerator


def qsqrt(x):
    """The exact nonnegative square root of a rational square; raises ValueError otherwise."""
    return qpow(x, F(1, 2))


def is_square(x):
    """True when the rational x >= 0 is the square of a rational."""
    x = F(x)
    return x >= 0 and iroot(x.numerator, 2) is not None and iroot(x.denominator, 2) is not None


# ---------------------------------------------------------------------------
# 5. exact number fields
# ---------------------------------------------------------------------------

class QS(object):
    """a + b sqrt(d) in Q(sqrt d), exact (d a nonsquare rational; d < 0 allowed)."""
    __slots__ = ("a", "b", "d")

    def __init__(self, a=0, b=0, d=2):
        if isinstance(a, QS):
            self.a, self.b, self.d = a.a, a.b, a.d
            return
        self.a, self.b, self.d = F(a), F(b), F(d)

    def _c(self, o):
        if isinstance(o, QS):
            if o.d != self.d and o.b != 0 and self.b != 0:
                raise ValueError("QS: different fields Q(sqrt %s), Q(sqrt %s)" % (self.d, o.d))
            return o if (o.d == self.d or o.b == 0) else QS(o.a, o.b, o.d)
        return QS(o, 0, self.d)

    def _dd(self, o):
        return self.d if self.b != 0 or not isinstance(o, QS) else o.d

    @property
    def p(self):
        """Rational part (the R2 name)."""
        return self.a

    @property
    def q(self):
        """sqrt-coefficient (the R2 name)."""
        return self.b

    def __add__(self, o):
        d = self._dd(o)
        o = self._c(o)
        return QS(self.a + o.a, self.b + o.b, d)

    __radd__ = __add__

    def __neg__(self):
        return QS(-self.a, -self.b, self.d)

    def __sub__(self, o):
        return self + (-self._c(o))

    def __rsub__(self, o):
        return self._c(o) - self

    def __mul__(self, o):
        d = self._dd(o)
        o = self._c(o)
        return QS(self.a * o.a + d * self.b * o.b, self.a * o.b + self.b * o.a, d)

    __rmul__ = __mul__

    def conj(self):
        """Galois conjugate a - b sqrt d."""
        return QS(self.a, -self.b, self.d)

    def norm(self):
        """Field norm a^2 - d b^2 (rational)."""
        return self.a * self.a - self.d * self.b * self.b

    def __truediv__(self, o):
        o = self._c(o)
        n = o.norm()
        if n == 0:
            raise ZeroDivisionError
        return self * o.conj() * QS(1 / n, 0, o.d)

    def __rtruediv__(self, o):
        return self._c(o) / self

    def __pow__(self, n):
        if n < 0:
            return QS(1, 0, self.d) / (self ** (-n))
        out, base = QS(1, 0, self.d), self
        while n:
            if n & 1:
                out = out * base
            n >>= 1
            if n:
                base = base * base
        return out

    def __eq__(self, o):
        if not isinstance(o, QS):
            try:
                o = QS(o, 0, self.d)
            except (TypeError, ValueError):
                return NotImplemented
        if self.b == 0 and o.b == 0:
            return self.a == o.a
        return self.a == o.a and self.b == o.b and self.d == o.d

    def __ne__(self, o):
        r = self.__eq__(o)
        return r if r is NotImplemented else not r

    def __hash__(self):
        return hash(self.a) if self.b == 0 else hash((self.a, self.b, self.d))

    def __bool__(self):
        return self.a != 0 or self.b != 0

    __nonzero__ = __bool__

    def sign(self):
        """Exact sign (-1, 0, 1) of a + b sqrt d for d > 0."""
        if self.d < 0 and self.b != 0:
            raise ValueError("QS.sign: not real")
        a, b = self.a, self.b
        if b == 0 or a == 0 or (a > 0) == (b > 0):
            v = a if b == 0 else (b if a == 0 else a)
            return (v > 0) - (v < 0)
        lead = a if a * a > self.d * b * b else b
        return (lead > 0) - (lead < 0)

    def __lt__(self, o):
        return (self - self._c(o)).sign() < 0

    def __le__(self, o):
        return (self - self._c(o)).sign() <= 0

    def __gt__(self, o):
        return (self - self._c(o)).sign() > 0

    def __ge__(self, o):
        return (self - self._c(o)).sign() >= 0

    def __repr__(self):
        return "QS(%s, %s, %s)" % (self.a, self.b, self.d)


def R2(p=0, q=0):
    """p + q sqrt(2) (the families checks' R2; attributes .p, .q, method .sign())."""
    return QS(p, q, 2)


class CY(object):
    """a + b zeta with zeta^2 = -1 - zeta (zeta = e^{2 pi i/3}), exact (families checks' class)."""
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
        """Complex conjugate (zeta -> zeta^2)."""
        return CY(s.a - s.b, -s.b)

    def __truediv__(s, o):
        o = CY._c(o)
        n = o.nsq()
        if n == 0:
            raise ZeroDivisionError
        return s * o.conj() * CY(1 / n)

    def __rtruediv__(s, o):
        return CY._c(o) / s

    def __bool__(s):
        return s.a != 0 or s.b != 0

    __nonzero__ = __bool__

    def re(s):
        """Real part a - b/2."""
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

    def __repr__(s):
        return "CY(%s, %s)" % (s.a, s.b)


ZETA = CY(0, 1)
Z2 = ZETA * ZETA
ISQ3 = Z2 - ZETA          # zeta^2 - zeta = -i sqrt(3)


# ---------------------------------------------------------------------------
# 6. certified rational bounds
# ---------------------------------------------------------------------------

def round_down(x, den=2 ** 80):
    """Largest multiple of 1/den that is <= x (standard-model.spectrum-run _round_down)."""
    x = F(x)
    return F((x.numerator * den) // x.denominator, den)


def round_up(x, den=2 ** 80):
    """Smallest multiple of 1/den that is >= x (standard-model.spectrum-run _round_up)."""
    x = F(x)
    return F(-((-x.numerator * den) // x.denominator), den)


def sqrt_bounds(m, digits=10):
    """Rationals lo <= sqrt(m) <= hi with hi - lo = 10^-digits/den(m) (L09 famcommon)."""
    m = F(m)
    scale = 10 ** digits
    lo_int = isqrt(m.numerator * m.denominator * scale * scale)
    lo, hi = F(lo_int, m.denominator * scale), F(lo_int + 1, m.denominator * scale)
    if not (lo * lo <= m <= hi * hi):
        raise ArithmeticError("sqrt_bounds failed")
    return lo, hi


def iroot_bracket(x, k, denom):
    """(lo, hi), multiples of 1/denom, with lo^k <= x < hi^k (dark-tower-matter checks)."""
    n = F(x) * denom ** k
    t = n.numerator // n.denominator
    lo, hi = 0, 1
    while hi ** k <= t:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** k <= t:
            lo = mid
        else:
            hi = mid
    return F(lo, denom), F(lo + 1, denom)


def arctan_inv_bracket(k, terms):
    """(lo, hi) bracketing arctan(1/k) by alternating partial sums (dark-tower _arctan_inv)."""
    s, lo, hi = F(0), None, None
    for j in range(terms):
        t = F((-1) ** j, (2 * j + 1) * k ** (2 * j + 1))
        s += t
        if j % 2 == 0:
            hi = s
        else:
            lo = s
    return lo, hi


def pi_bracket(terms=24):
    """Machin pi = 16 arctan(1/5) - 4 arctan(1/239) with alternating brackets (dark-tower checks)."""
    a_lo, a_hi = arctan_inv_bracket(5, terms)
    b_lo, b_hi = arctan_inv_bracket(239, terms)
    return 16 * a_lo - 4 * b_hi, 16 * a_hi - 4 * b_lo


def atan_bounds(x, n=30):
    """(lo, hi) for arctan(x), 0 <= x <= 1, n alternating terms (standard-model.spectrum-run)."""
    x = F(x)
    s, term = F(0), x
    for k in range(n):
        s += (-1) ** k * term / (2 * k + 1)
        term *= x * x
    nxt = term / (2 * n + 1)
    return (s - nxt, s) if n % 2 == 1 else (s, s + nxt)


def pi_bounds(n=30):
    """Machin bounds on pi via atan_bounds with n terms (standard-model.spectrum-run pi_bounds)."""
    a5, a239 = atan_bounds(F(1, 5), n), atan_bounds(F(1, 239), n)
    return 16 * a5[0] - 4 * a239[1], 16 * a5[1] - 4 * a239[0]


def exp_bracket(x, terms=40):
    """(lo, hi) with lo <= e^x <= hi, Taylor series with remainder (dark-tower exp_bracket)."""
    x = F(x)
    if x < 0:
        lo, hi = exp_bracket(-x, terms)
        return 1 / hi, 1 / lo
    s, t = F(1), F(1)
    for j in range(1, terms + 1):
        t = t * x / j
        s += t
    bound = 3 ** (x.numerator // x.denominator + 1)
    return s, s + t * x / (terms + 1) * bound


def exp_bounds(x, terms=25):
    """Rational lo <= exp(x) <= hi for x >= 0, halving and squaring with outward rounding to
    2^-80 (standard-model.spectrum-run exp_bounds)."""
    x = F(x)
    if x < 0:
        raise ValueError("exp_bounds needs x >= 0 (use exp_bracket for x < 0)")
    m = 0
    while x / 2 ** m > F(1, 2):
        m += 1
    y = x / 2 ** m
    s, term = F(0), F(1)
    for i in range(terms + 1):
        s += term
        term = term * y / (i + 1)
    lo, hi = round_down(s), round_up(s + 2 * term)
    for _ in range(m):
        lo, hi = round_down(lo * lo), round_up(hi * hi)
    return lo, hi


def atanh_bounds(z, K=30):
    """Rational bounds on atanh z for 0 <= z <= 1/3 (singularity.deficit-theorem checks)."""
    z = F(z)
    zz = z * z
    term, part = z, F(0)
    for k in range(K):
        part += term / (2 * k + 1)
        term *= zz
    tail = term / ((2 * K + 1) * (1 - zz))
    return part, part + tail


_LN_DEN = 1 << 160


def _ln_out(lo, hi):
    return (F((lo.numerator * _LN_DEN) // lo.denominator, _LN_DEN),
            F(-((-hi.numerator * _LN_DEN) // hi.denominator), _LN_DEN))


def ln_bounds(n):
    """Rational (lower, upper) bounds on ln n for a positive integer n, rounded outward to
    2^-160 (singularity.deficit-theorem-cost-descent-exactly ln_bounds)."""
    n = int(n)
    if n < 1:
        raise ValueError("ln_bounds needs a positive integer")
    if n == 1:
        return F(0), F(0)
    l2lo, l2hi = atanh_bounds(F(1, 3))
    l2lo, l2hi = 2 * l2lo, 2 * l2hi
    a = len(bin(n)) - 3
    x = F(n, 1 << a)
    zlo, zhi = atanh_bounds((x - 1) / (x + 1))
    return _ln_out(a * l2lo + 2 * zlo, a * l2hi + 2 * zhi)


def log_bounds(x):
    """Rational bounds on ln x for a rational x > 0: ln(num) - ln(den)."""
    x = F(x)
    if x <= 0:
        raise ValueError("log_bounds needs x > 0")
    nlo, nhi = ln_bounds(x.numerator)
    dlo, dhi = ln_bounds(x.denominator)
    return nlo - dhi, nhi - dlo


# ---------------------------------------------------------------------------
# decimal rounding: a quoted value pinned to its last digit
# ---------------------------------------------------------------------------


def rounds_to(x, m, e):
    """x rounds to m x 10^e (m an integer mantissa, last digit included): |x - m 10^e| < 10^e/2."""
    u = F(10) ** e
    return abs(F(x) - m * u) * 2 < u


def root_rounds_to(xk, m, e, k=2):
    """The positive k-th root of xk > 0 rounds to m x 10^e, compared through k-th powers, so no
    root is taken: ((m - 1/2) 10^e)^k < xk < ((m + 1/2) 10^e)^k."""
    u = F(10) ** e
    return ((2 * m - 1) * u / 2) ** k < F(xk) < ((2 * m + 1) * u / 2) ** k


def interval_rounds_to(lo, hi, m, e):
    """Every value in the bracket [lo, hi] rounds to m x 10^e (half-up at the upper edge)."""
    u = F(10) ** e
    return (m - F(1, 2)) * u <= lo and hi < (m + F(1, 2)) * u
