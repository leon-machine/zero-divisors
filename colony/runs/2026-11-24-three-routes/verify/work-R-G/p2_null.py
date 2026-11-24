import sys, random
sys.path.insert(0, '/home/claude/leon-machine/zero-divisors/lib')
import GA
from fractions import Fraction as F
SQ = (1, -1, -1, -1)
g = [GA.gen(i) for i in range(4)]
n = GA.add(g[0], g[3]); nb = GA.sub(g[0], g[3])
def Q(x): return GA.mul(x, x, SQ)
random.seed(7)
for trial in range(200):
    a1, a2 = F(random.randint(1, 9), random.randint(1, 9)), F(random.randint(1, 9), random.randint(1, 9))
    p1p = (F(random.randint(-5, 5)), F(random.randint(-5, 5)))
    if trial % 3 == 0:
        p2p = (a2 / a1 * p1p[0], a2 / a1 * p1p[1])   # parallel case
    else:
        p2p = (F(random.randint(-5, 5)), F(random.randint(-5, 5)))
    def nullv(a, pp):
        b = (pp[0] ** 2 + pp[1] ** 2) / (4 * a)
        return GA.add(GA.scal(a, nb), GA.scal(pp[0], g[1]), GA.scal(pp[1], g[2]), GA.scal(b, n))
    P1, P2 = nullv(a1, p1p), nullv(a2, p2p)
    assert GA.is_zero(Q(P1)) and GA.is_zero(Q(P2))
    S = Q(GA.add(P1, P2))
    d = (a2 * p1p[0] - a1 * p2p[0], a2 * p1p[1] - a1 * p2p[1])
    pred = (d[0] ** 2 + d[1] ** 2) / (a1 * a2)
    assert GA.eq(S, GA.sc(pred)), (S, pred)
    if pred == 0:
        assert GA.eq(GA.scal(a1, P2), GA.scal(a2, P1))
print('(iv) identity holds on 200 rational samples, incl. parallel cases')
