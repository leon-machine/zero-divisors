"""Certified enclosures with integer arithmetic: intervals [lo/P, hi/P] with P = 2^96, rounded outward,
and jets (value, first and second derivative) of functions of one variable with interval coefficients."""
from fractions import Fraction as F

BITS = 128
P = 1 << BITS


def fl(n, d):
    return n // d


def ce(n, d):
    return -((-n) // d)


def iv(a, b=None):
    """Interval enclosing the rational a (or [a, b])."""
    a = F(a)
    b = a if b is None else F(b)
    return (fl(a.numerator * P, a.denominator), ce(b.numerator * P, b.denominator))


def iadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def ineg(x):
    return (-x[1], -x[0])


def isub(x, y):
    return (x[0] - y[1], x[1] - y[0])


def imul(x, y):
    c = (x[0] * y[0], x[0] * y[1], x[1] * y[0], x[1] * y[1])
    return (fl(min(c), P), ce(max(c), P))


def irecip(x):
    assert x[0] > 0 or x[1] < 0
    if x[0] > 0:
        return (fl(P * P, x[1]), ce(P * P, x[0]))
    return ineg(irecip(ineg(x)))


def isqrt_int(n):
    if n < 2:
        return n
    x = 1 << ((n.bit_length() + 1) // 2)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def isqrt(x):
    assert x[0] > 0
    lo = isqrt_int(x[0] * P)
    hi = isqrt_int(x[1] * P)
    if hi * hi < x[1] * P:
        hi += 1
    return (lo, hi)


def iexp(x):
    """exp of an interval: Taylor series of exp(t), |t| <= 1/2, after halving, with a remainder bound,
    then repeated squaring.  exp is increasing, so the two ends are treated separately."""
    def point(t, up):
        s = 0
        while abs(t) > P // 2:
            # halve: exp(t) = exp(t/2)^2; keep an enclosure of t/2
            t = fl(t, 2) if not up else ce(t, 2)
            s += 1
        # sum_{k<=N} t^k/k! with interval terms, N = 30; remainder |t|^31/31! * 2 <= 2^-31/31! * 2 < 2^-140
        term = (P, P)
        tot = (P, P)
        T = (t, t)
        for k in range(1, 31):
            term = imul(term, T)
            term = (fl(term[0], k), ce(term[1], k))
            tot = iadd(tot, term)
        tot = (tot[0] - 1, tot[1] + 1)
        for _ in range(s):
            tot = imul(tot, tot) if tot[0] >= 0 else (0, max(tot[0] * tot[0], tot[1] * tot[1]) // P + 1)
        return tot
    lo = point(x[0], False)[0]
    hi = point(x[1], True)[1]
    return (max(lo, 0), hi)


def pi_interval():
    """pi = 16 atan(1/5) - 4 atan(1/239) (Machin); alternating series bracket each arctangent."""
    def atan_inv(n, terms):
        lo = hi = F(0)
        s = F(0)
        for k in range(terms):
            s += F((-1) ** k, (2 * k + 1) * n ** (2 * k + 1))
            if k == terms - 2:
                a = s
            if k == terms - 1:
                b = s
        return (min(a, b), max(a, b))
    a5 = atan_inv(5, 46)
    a239 = atan_inv(239, 14)
    return iv(16 * a5[0] - 4 * a239[1], 16 * a5[1] - 4 * a239[0])


PI = pi_interval()


# ---- jets: triples (f, f', f'') of intervals ---------------------------------------------------------------

def jconst(c):
    return (iv(c), (0, 0), (0, 0))


def jvar(x):
    return (x, (P, P), (0, 0))


def jadd(a, b):
    return tuple(iadd(u, v) for u, v in zip(a, b))


def jsub(a, b):
    return tuple(isub(u, v) for u, v in zip(a, b))


def jscale(c, a):
    c = iv(c)
    return tuple(imul(c, u) for u in a)


def jmul(a, b):
    two = iv(2)
    return (imul(a[0], b[0]),
            iadd(imul(a[1], b[0]), imul(a[0], b[1])),
            iadd(iadd(imul(a[2], b[0]), imul(two, imul(a[1], b[1]))), imul(a[0], b[2])))


def jrecip(g):
    h = irecip(g[0])
    h2 = imul(h, h)
    h3 = imul(h2, h)
    two = iv(2)
    return (h, ineg(imul(g[1], h2)), iadd(ineg(imul(g[2], h2)), imul(two, imul(imul(g[1], g[1]), h3))))


def jexp(g):
    e = iexp(g[0])
    return (e, imul(g[1], e), imul(iadd(g[2], imul(g[1], g[1])), e))


def jsqrt(g):
    s = isqrt(g[0])
    r = irecip(s)
    half = iv(F(1, 2))
    quarter = iv(F(1, 4))
    r3 = imul(imul(r, r), r)
    return (s, imul(half, imul(g[1], r)),
            isub(imul(half, imul(g[2], r)), imul(quarter, imul(imul(g[1], g[1]), r3))))


def jfermi(g):
    """Jet of s(g) = 1/(exp(g) + 1): s' = -s(1 - s), s'' = s(1 - s)(1 - 2s) in the argument, then the chain rule."""
    e = iexp(g[0])
    s = irecip(iadd(e, (P, P)))
    one = (P, P)
    t = imul(s, isub(one, s))
    s1 = ineg(t)
    s2 = imul(t, isub(one, imul(iv(2), s)))
    return (s, imul(s1, g[1]), iadd(imul(s2, imul(g[1], g[1])), imul(s1, g[2])))


def to_float(x):
    return (x[0] / P, x[1] / P)
