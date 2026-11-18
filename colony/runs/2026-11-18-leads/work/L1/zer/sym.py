"""Exact differential algebra for the radial identities (no sympy).

Ring A = Q[r, lam, w][1/r, 1/(r - 2), 1/(lam r + 3), 1/w] (M = 1; w stands for omega^2): a polynomial numerator
{(i, j, k): Fraction} (r^i lam^j w^k) over r^a (r - 2)^b (lam r + 3)^c w^d. Division by units only.
LF: linear forms in jet symbols (name, p, q) = d_t^p d_r^q name with coefficients in A, with d(0) = d/dt and
d(1) = d/dr, so that the closed forms written for gtg.Jet evaluate on them unchanged."""
from fractions import Fraction as F


def padd(a, b):
    out = dict(a)
    for m, x in b.items():
        y = out.get(m, 0) + x
        if y:
            out[m] = y
        else:
            out.pop(m, None)
    return out


def pmul(a, b):
    out = {}
    for (i1, j1, k1), x in a.items():
        for (i2, j2, k2), y in b.items():
            m = (i1 + i2, j1 + j2, k1 + k2)
            t = out.get(m, 0) + x * y
            if t:
                out[m] = t
            else:
                out.pop(m, None)
    return out


def pscal(c, a):
    return {m: c * x for m, x in a.items()} if c else {}


def pdr(a):
    return {(i - 1, j, k): i * x for (i, j, k), x in a.items() if i}


P_R = {(1, 0, 0): F(1)}
P_RM2 = {(1, 0, 0): F(1), (0, 0, 0): F(-2)}
P_LR3 = {(1, 1, 0): F(1), (0, 0, 0): F(3)}
P_W = {(0, 0, 1): F(1)}
ATOMS = (P_R, P_RM2, P_LR3, P_W)


def ppow(p, n):
    out = {(0, 0, 0): F(1)}
    for _ in range(n):
        out = pmul(out, p)
    return out


def div_rm2(p):
    """p / (r - 2) if exact, else None (long division in r, monic divisor)."""
    co = dict(p)
    out = {}
    while co:
        m = max(co)                                # highest power of r first (tuple order: r leads)
        i, j, k = m
        if i < 1:
            return None
        x = co.pop(m)
        out[(i - 1, j, k)] = x                     # x r^(i-1) (r - 2) = x r^i - 2x r^(i-1)
        t = co.get((i - 1, j, k), 0) + 2 * x
        if t:
            co[(i - 1, j, k)] = t
        else:
            co.pop((i - 1, j, k), None)
    return out


def div_lr3(p):
    """p / (lam r + 3) if exact, else None (long division in lam; the leading coefficient r is a monomial)."""
    co = dict(p)
    out = {}
    while co:
        m = max(co, key=lambda t: (t[1], t[0], t[2]))
        i, j, k = m
        if j < 1 or i < 1:
            return None
        x = co.pop(m)
        out[(i - 1, j - 1, k)] = x                 # x r^(i-1) lam^(j-1) (lam r + 3)
        t = co.get((i - 1, j - 1, k), 0) - 3 * x
        if t:
            co[(i - 1, j - 1, k)] = t
        else:
            co.pop((i - 1, j - 1, k), None)
    return out


class A(object):
    __slots__ = ("n", "d")

    def __init__(self, n, d=(0, 0, 0, 0)):
        if not n:
            self.n, self.d = {}, (0, 0, 0, 0)
            return
        a, b, c, e = d
        if a:
            m = min(min(i for (i, _, _) in n), a)
            if m:
                n = {(i - m, j, k): x for (i, j, k), x in n.items()}
                a -= m
        if e:
            m = min(min(k for (_, _, k) in n), e)
            if m:
                n = {(i, j, k - m): x for (i, j, k), x in n.items()}
                e -= m
        while b:
            q = div_rm2(n)
            if q is None:
                break
            n, b = q, b - 1
        while c:
            q = div_lr3(n)
            if q is None:
                break
            n, c = q, c - 1
        self.n, self.d = n, (a, b, c, e)

    @staticmethod
    def const(x):
        x = F(x)
        return A({(0, 0, 0): x} if x else {})

    @staticmethod
    def var(i):
        return A({tuple(1 if k == i else 0 for k in range(3)): F(1)})

    @staticmethod
    def _c(o):
        return o if isinstance(o, A) else A.const(o)

    @staticmethod
    def _den(d):
        p = {(0, 0, 0): F(1)}
        for atom, e in zip(ATOMS, d):
            for _ in range(e):
                p = pmul(p, atom)
        return p

    def __add__(self, o):
        if isinstance(o, LF):
            return NotImplemented
        o = A._c(o)
        if not self.n:
            return o
        if not o.n:
            return self
        d = tuple(max(x, y) for x, y in zip(self.d, o.d))
        n1 = pmul(self.n, A._den(tuple(x - y for x, y in zip(d, self.d))))
        n2 = pmul(o.n, A._den(tuple(x - y for x, y in zip(d, o.d))))
        return A(padd(n1, n2), d)
    __radd__ = __add__

    def __neg__(self):
        r = A({})
        r.n, r.d = {m: -x for m, x in self.n.items()}, self.d
        return r

    def __sub__(self, o):
        if isinstance(o, LF):
            return NotImplemented
        return self + (-A._c(o))

    def __rsub__(self, o):
        return A._c(o) + (-self)

    def __mul__(self, o):
        if isinstance(o, LF):
            return NotImplemented
        o = A._c(o)
        if not self.n or not o.n:
            return A({})
        return A(pmul(self.n, o.n), tuple(x + y for x, y in zip(self.d, o.d)))
    __rmul__ = __mul__

    def inv(self):
        """Inverse of a unit: a rational number times a product of powers of r, r - 2, lam r + 3, w."""
        if not self.n:
            raise ZeroDivisionError
        n, e = self.n, [0, 0, 0, 0]
        while True:
            q = div_rm2(n)
            if q is None:
                break
            n, e[1] = q, e[1] + 1
        while True:
            q = div_lr3(n)
            if q is None:
                break
            n, e[2] = q, e[2] + 1
        if len(n) != 1:
            raise ArithmeticError("A: division by a non-unit")
        ((i, j, k), x), = n.items()
        if j:
            raise ArithmeticError("A: division by a non-unit (lam)")
        e[0], e[3] = i, k
        return A(pscal(1 / x, A._den(self.d)), tuple(e))

    def __truediv__(self, o):
        if isinstance(o, LF):
            return NotImplemented
        return self * A._c(o).inv()

    def __rtruediv__(self, o):
        return A._c(o) * self.inv()

    def __pow__(self, n):
        if n < 0:
            return self.inv() ** (-n)
        out = A.const(1)
        for _ in range(n):
            out = out * self
        return out

    def dr(self):
        """d/dr."""
        if not self.n:
            return self
        a, b, c, e = self.d
        lead = pmul(pmul(pdr(self.n), P_R), pmul(P_RM2, P_LR3))
        corr = padd(padd(pscal(F(a), pmul(P_RM2, P_LR3)), pscal(F(b), pmul(P_R, P_LR3))),
                    pscal(F(c), pmul({(1, 1, 0): F(1)}, P_RM2)))
        return A(padd(lead, pscal(F(-1), pmul(self.n, corr))), (a + 1, b + 1, c + 1, e))

    def __bool__(self):
        return bool(self.n)

    def __eq__(self, o):
        return not (self - A._c(o)).n

    def __ne__(self, o):
        return not self.__eq__(o)
    __hash__ = None

    def __repr__(self):
        return "A(%r / r^%d (r-2)^%d (lr+3)^%d w^%d)" % ((self.n,) + self.d)


class LF(object):
    """Linear form sum c[sym] sym, sym = (name, p, q) standing for d_t^p d_r^q name."""
    __slots__ = ("c",)

    def __init__(self, c=None):
        self.c = {s: x for s, x in (c or {}).items() if x}

    @staticmethod
    def sym(name, p=0, q=0):
        return LF({(name, p, q): A.const(1)})

    def __add__(self, o):
        if not isinstance(o, LF):
            if not o:
                return self
            return NotImplemented
        out = dict(self.c)
        for s, x in o.c.items():
            out[s] = out[s] + x if s in out else x
        return LF(out)
    __radd__ = __add__

    def __neg__(self):
        return LF({s: -x for s, x in self.c.items()})

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o):
        if isinstance(o, LF):
            raise TypeError("LF * LF")
        o = A._c(o)
        return LF({s: x * o for s, x in self.c.items()})
    __rmul__ = __mul__

    def __truediv__(self, o):
        return self * A._c(o).inv()

    def d(self, i):
        out = LF()
        for (name, p, q), x in self.c.items():
            if i == 0:
                out = out + LF({(name, p + 1, q): x})
            else:
                out = out + LF({(name, p, q + 1): x, (name, p, q): x.dr()})
        return out

    def __bool__(self):
        return bool(self.c)

    def __eq__(self, o):
        if not isinstance(o, LF):
            return not self.c and not o
        return not (self - o).c
    __hash__ = None

    def __repr__(self):
        return "LF(%s)" % ", ".join("%s: %r" % (s, x) for s, x in sorted(self.c.items()))


def substitute(lf, rule):
    """Replace symbols by linear forms until none is left to replace: rule(sym) -> LF or None."""
    while True:
        out, changed = LF(), False
        for s, x in lf.c.items():
            rep = rule(s)
            if rep is None:
                out = out + LF({s: x})
            else:
                out = out + rep * x
                changed = True
        lf = out
        if not changed:
            return lf
