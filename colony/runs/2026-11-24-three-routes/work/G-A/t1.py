import time
from fractions import Fraction as F
from spin2 import *
T = Torus(4)
def lcg(seed):
    s = seed
    while True:
        s = (s * 1103515245 + 12345) % (2**31)
        yield (s >> 8) % 11 - 5
def rnd(ncomp, seed):
    g = lcg(seed)
    return {(c, x): F(next(g)) for c in range(ncomp) for x in T.sites}
h, h2, pi, xi = rnd(6, 1), rnd(6, 2), rnd(6, 3), rnd(3, 4)
dh = T.gauge(xi)
print("G gauge = 0:", T.einstein(dh) == {})
print("D gauge = 0:", T.ham(dh) == {})
Gh = T.einstein(h)
print("div G = 0:", T.mom(Gh) == {})
print("self-adjoint:", T.pair(h2, Gh) == T.pair(T.einstein(h2), h))
tr = {}
for (c, x), v in Gh.items():
    if c < 3: tr[x] = tr.get(x, 0) + v
Dh = T.ham(h)
print("tr G = -D/2:", all(tr.get(x, 0) == -Dh.get(x, 0) / 2 for x in T.sites))
# D p = sum_i b_i C_i
Dp = T.ham(T.pmap(pi))
C = T.mom(pi)
bC = {}
for (i, x), v in C.items():
    for o, c in B[i].items():
        k = T.sh(x, o, -1)
        bC[k] = bC.get(k, 0) + c * v
print("D p = b.C:", all(Dp.get(x, 0) == bC.get(x, 0) for x in T.sites))
# gauge map adjoint of momentum: <pi, gauge xi> = -2 sum xi_i C_i
lhs = T.pair(pi, dh)
rhs = -2 * sum(xi[(i, x)] * C.get((i, x), 0) for i in range(3) for x in T.sites)
print("adjoint:", lhs == rhs)
# rank: kernel of G on torus L=2? skip. wave identity: G h = -1/2 Lap h + 1/2 gauge(V) - 1/2 delta D h, V_j = div h_j - 1/2 grad_j tr h
