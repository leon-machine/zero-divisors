"""The ring Q[z, 1/z, 1/(1 - z^2), s, 1/s, c] / (c^2 = 1 - s^2), exact.

z stands for sqrt f on the Schwarzschild exterior with M = 1 (so r = 2/(1 - z^2)), s and c for the sine and cosine
of the polar angle. An element is a polynomial numerator {(i, j, k): Fraction} (z^i s^j c^k, k in {0, 1}) over a
denominator z^a (1 - z^2)^b s^d. Division is by units only (a rational number times a monomial in z, 1 - z^2, s);
anything else raises, so a computation that completes has stayed inside the ring and its equalities are identities
in z and in the angle. Mixed arithmetic with Fractions and ints, so that gtg.Jet can carry these coefficients."""
from fractions import Fraction as F
from gtg import Jet


def _padd(a, b):
    out = dict(a)
    for m, x in b.items():
        y = out.get(m, 0) + x
        if y:
            out[m] = y
        else:
            out.pop(m, None)
    return out


def _pmul(a, b):
    out = {}
    for (i1, j1, k1), x in a.items():
        for (i2, j2, k2), y in b.items():
            v = x * y
            if k1 + k2 == 2:                       # c^2 = 1 - s^2
                for m, w in (((i1 + i2, j1 + j2, 0), v), ((i1 + i2, j1 + j2 + 2, 0), -v)):
                    t = out.get(m, 0) + w
                    if t:
                        out[m] = t
                    else:
                        out.pop(m, None)
            else:
                m = (i1 + i2, j1 + j2, k1 + k2)
                t = out.get(m, 0) + v
                if t:
                    out[m] = t
                else:
                    out.pop(m, None)
    return out


def _div_1mz2(p):
    """p / (1 - z^2) if the division is exact, else None (long division from the top degree in z)."""
    groups = {}
    for (i, j, k), x in p.items():
        groups.setdefault((j, k), {})[i] = x
    out = {}
    for (j, k), co in groups.items():
        co = dict(co)
        while co:
            n = max(co)
            if n < 2:
                return None                         # a remainder of degree below two is left
            x = co.pop(n)
            out[(n - 2, j, k)] = -x                 # -x z^(n-2) (1 - z^2) = x z^n - x z^(n-2)
            t = co.get(n - 2, 0) + x
            if t:
                co[n - 2] = t
            else:
                co.pop(n - 2, None)
    return out


_ONE = {(0, 0, 0): F(1)}
_1MZ2 = {(0, 0, 0): F(1), (2, 0, 0): F(-1)}


class U(object):
    __slots__ = ("n", "d")

    def __init__(self, n, d=(0, 0, 0)):
        a, b, e = d
        if not n:
            self.n, self.d = {}, (0, 0, 0)
            return
        if a:
            m = min(min(i for (i, _, _) in n), a)
            if m:
                n = {(i - m, j, k): x for (i, j, k), x in n.items()}
                a -= m
        if e:
            m = min(min(j for (_, j, _) in n), e)
            if m:
                n = {(i, j - m, k): x for (i, j, k), x in n.items()}
                e -= m
        while b:
            if any(sum(x for (i, j, k), x in n.items() if (j, k) == key and i % 2 == par) != 0
                   for key in {(j, k) for (_, j, k) in n} for par in (0, 1)):
                break                               # not divisible by 1 - z^2 (values at z = 1 and z = -1)
            q = _div_1mz2(n)
            if q is None:
                break
            n = q
            b -= 1
        self.n, self.d = n, (a, b, e)

    @staticmethod
    def const(x):
        x = F(x)
        return U({(0, 0, 0): x} if x else {})

    @staticmethod
    def z():
        return U({(1, 0, 0): F(1)})

    @staticmethod
    def s():
        return U({(0, 1, 0): F(1)})

    @staticmethod
    def c():
        return U({(0, 0, 1): F(1)})

    @staticmethod
    def _c(o):
        return o if isinstance(o, U) else U.const(o)

    @staticmethod
    def _den_poly(d):
        a, b, e = d
        p = {(a, e, 0): F(1)}
        for _ in range(b):
            p = _pmul(p, _1MZ2)
        return p

    def __add__(self, o):
        if isinstance(o, Jet):
            return NotImplemented
        o = U._c(o)
        if not self.n:
            return o
        if not o.n:
            return self
        (a1, b1, e1), (a2, b2, e2) = self.d, o.d
        d = (max(a1, a2), max(b1, b2), max(e1, e2))
        n1 = _pmul(self.n, U._den_poly((d[0] - a1, d[1] - b1, d[2] - e1)))
        n2 = _pmul(o.n, U._den_poly((d[0] - a2, d[1] - b2, d[2] - e2)))
        return U(_padd(n1, n2), d)
    __radd__ = __add__

    def __neg__(self):
        r = U({})
        r.n, r.d = {m: -x for m, x in self.n.items()}, self.d
        return r

    def __sub__(self, o):
        if isinstance(o, Jet):
            return NotImplemented
        return self + (-U._c(o))

    def __rsub__(self, o):
        return U._c(o) + (-self)

    def __mul__(self, o):
        if isinstance(o, Jet):
            return NotImplemented
        o = U._c(o)
        if not self.n or not o.n:
            return U({})
        return U(_pmul(self.n, o.n), tuple(x + y for x, y in zip(self.d, o.d)))
    __rmul__ = __mul__

    def inv(self):
        if not self.n:
            raise ZeroDivisionError
        n, pw = self.n, 0
        while len(n) > 1:
            if any(sum(x for (i, j, k), x in n.items() if (j, k) == key and i % 2 == par) != 0
                   for key in {(j, k) for (_, j, k) in n} for par in (0, 1)):
                raise ArithmeticError("U: division by a non-unit %r" % (self,))
            q = _div_1mz2(n)
            if q is None:
                raise ArithmeticError("U: division by a non-unit %r" % (self,))
            n, pw = q, pw + 1
        ((i, j, k), x), = n.items()
        if k:
            raise ArithmeticError("U: division by a non-unit (cosine) %r" % (self,))
        a, b, e = self.d
        num = _pmul({(a, e, 0): 1 / x}, U._den_poly((0, b, 0)))
        return U(num, (i, pw, j))

    def __truediv__(self, o):
        if isinstance(o, Jet):
            return NotImplemented
        return self * U._c(o).inv()

    def __rtruediv__(self, o):
        return U._c(o) * self.inv()

    def __pow__(self, n):
        if n < 0:
            return self.inv() ** (-n)
        out = U.const(1)
        for _ in range(n):
            out = out * self
        return out

    def __bool__(self):
        return bool(self.n)

    def __eq__(self, o):
        return not (self - U._c(o)).n

    def __ne__(self, o):
        return not self.__eq__(o)
    __hash__ = None

    def __repr__(self):
        return "U(%r / z^%d (1-z^2)^%d s^%d)" % ((self.n,) + self.d)
