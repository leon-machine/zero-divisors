"""scratch: first-order perturbations of a flat RW h-field through lib/gtg.py with dual-number coefficients"""
import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, gtg
from gtg import Jet

class Dual(object):
    """a + b eps, eps^2 = 0, exact"""
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)
    def _c(self, o):
        return o if isinstance(o, Dual) else Dual(o, 0)
    def __add__(self, o):
        o = self._c(o); return Dual(self.a + o.a, self.b + o.b)
    __radd__ = __add__
    def __neg__(self): return Dual(-self.a, -self.b)
    def __sub__(self, o):
        o = self._c(o); return Dual(self.a - o.a, self.b - o.b)
    def __rsub__(self, o):
        o = self._c(o); return Dual(o.a - self.a, o.b - self.b)
    def __mul__(self, o):
        if isinstance(o, Jet): return o.__mul__(self)
        o = self._c(o); return Dual(self.a * o.a, self.a * o.b + self.b * o.a)
    __rmul__ = __mul__
    def __truediv__(self, o):
        o = self._c(o); return self * Dual(1 / o.a, -o.b / (o.a * o.a))
    def __rtruediv__(self, o):
        return self._c(o) / self
    def __pow__(self, n):
        out = Dual(1, 0)
        for _ in range(n): out = out * self
        return out
    def __eq__(self, o):
        o = self._c(o); return self.a == o.a and self.b == o.b
    def __ne__(self, o): return not self.__eq__(o)
    __hash__ = None
    def __bool__(self): return bool(self.a) or bool(self.b)
    def __repr__(self): return "(%s + %s eps)" % (self.a, self.b)

EPS = Dual(0, 1)

def tay(i, coeffs, nv=4):
    """one-variable jet with given derivatives-at-point Taylor coefficients (value, f', f''/2, ...)"""
    return Jet.from_taylor(i, coeffs, nv)

if __name__ == "__main__":
    # background test: a(t) generic jet; FLRW; G(n).n
    a = tay(0, [F(2), F(3), F(5, 7), F(1, 3)])
    one = Jet.const(1, 4)
    TH = [[F(0)] * 4 for _ in range(4)]
    TH[0][0] = one
    for i in range(1, 4):
        TH[i][i] = a
    fld = gtg.Field(TH)
    Rc = fld.curvature()
    G0 = gtg.einstein(Rc, GA.gen(0))
    print("G(e0) =", G0, " H^2 =", F(3, 2) ** 2)
    # dual test
    b = tay(0, [Dual(2, 1), Dual(3, 0), F(5, 7), F(1, 3)])
    TH = [[F(0)] * 4 for _ in range(4)]
    TH[0][0] = one
    for i in range(1, 4):
        TH[i][i] = b
    fld = gtg.Field(TH)
    Rc = fld.curvature()
    print("dual G(e0) =", gtg.einstein(Rc, GA.gen(0)))
