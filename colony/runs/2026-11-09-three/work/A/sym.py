import sys, time
sys.path.insert(0, '/home/claude/phys-graph/lib')
sys.path.insert(0, '/home/claude/phys-graph/proposals/synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional')
from fractions import Fraction as F
import GA, gtg
from GA import RF
from gtg import Jet
import check as C

class K(object):
    """Element of Q(w) (GA.RF) with mixed arithmetic."""
    __slots__ = ("x",)
    def __init__(self, x):
        self.x = x if isinstance(x, RF) else RF.const(F(x))
    @staticmethod
    def _c(o):
        return o if isinstance(o, K) else K(o)
    def __add__(self, o): return K(self.x + K._c(o).x)
    __radd__ = __add__
    def __sub__(self, o): return K(self.x - K._c(o).x)
    def __rsub__(self, o): return K(K._c(o).x - self.x)
    def __mul__(self, o):
        if isinstance(o, Jet): return NotImplemented
        return K(self.x * K._c(o).x)
    __rmul__ = __mul__
    def __truediv__(self, o): return K(self.x / K._c(o).x)
    def __rtruediv__(self, o): return K(K._c(o).x / self.x)
    def __neg__(self): return K(-self.x)
    def __pow__(self, n):
        out = K(1)
        for _ in range(n): out = out * self
        return out
    def __bool__(self): return not self.x.is_zero()
    def __eq__(self, o): return (self.x - K._c(o).x).is_zero()
    def __ne__(self, o): return not self.__eq__(o)
    __hash__ = None

def run(M, s0, c0, L, ca, cb, a, b):
    w = K(RF.var())
    r0 = 2 * M / (1 - w * w)
    f = gtg.f_static(M)
    KK = 2
    fld = gtg.static_field(r0, s0, c0, f, order=KK - 1, sqrt_f=w)
    t = Jet.var(0, F(0), 4, KK); r = Jet.var(1, r0, 4, KK)
    sn, cs = gtg.sincos(2, s0, c0, 4, KK)
    fj = f(r); sf = fj.pw(F(1, 2), w)
    h0, h1 = C.generic(ca, t, r - r0), C.generic(cb, t, r - r0)
    S = C.angular(sn, cs, L, a, b, 1, KK)
    Z = Jet.const(0, 4)
    TH1 = [[Z] * 4 for _ in range(4)]
    TH1[0][3] = h0 * S / sf
    TH1[1][3] = -h1 * S * sf
    ric = [{k: gtg._val(v) for k, v in x.items() if gtg._val(v)} for x in C.lin_ricci(fld, TH1)]
    Et, Er, Eth = [x.v for x in C.odd_equations(h0, h1, fj, r, M, L)]
    pre = -a / (2 * r0 * s0 * w)
    ang = (b - 2 * (c0 / s0) * a) / (2 * r0 * r0 * s0)
    want = {(0,): pre * Et, (1,): pre * Er, (2,): ang * Eth}
    return ric, want

if __name__ == '__main__':
    t0 = time.time()
    ric, want = run(F(1), F(3, 5), F(4, 5), F(7, 2), C.H_COEF[0][0], C.H_COEF[0][1], F(2), F(-1))
    print(time.time() - t0)
    print(sorted(ric[3].keys()), all(ric[3][k] == want[k] for k in want), len(ric[3]) == 3)
    print(ric[0].keys(), ric[1].keys(), ric[2].keys())
