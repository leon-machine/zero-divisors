from fractions import Fraction as F
from spin2 import *
T = Torus(4)
def lcg(seed):
    s = seed
    while True:
        s = (s * 1103515245 + 12345) % (2**31)
        yield (s >> 8) % 11 - 5
g = lcg(7)
h = {(c, x): F(next(g)) for c in range(6) for x in T.sites}
def lapf(u):   # componentwise site/plaquette laplacian
    out = {}
    for (c, x), v in u.items():
        out[(c, x)] = out.get((c, x), 0) - 6*v
        for i in range(3):
            for s in (1, -1):
                k = (c, T.sh(x, e(i), s)); out[k] = out.get(k, 0) + v
    return out
tr = {}
for (c, x), v in h.items():
    if c < 3: tr[x] = tr.get(x, 0) + v
C = T.mom(h)                      # s_i h_ii + sum b_j h_ij on links
V = dict(C)
for x, t in tr.items():
    for i in range(3):
        # -(1/2) s_i tr
        V[(i, x)] = V.get((i, x), 0) + t/2
        y = T.sh(x, e(i), -1)
        V[(i, y)] = V.get((i, y), 0) - t/2
gV = T.gauge(V)
Dh = T.ham(h)
Gh = T.einstein(h); L_ = lapf(h)
ok = True
for c in range(6):
    for x in T.sites:
        rhs = -L_.get((c, x), 0)/2 + gV.get((c, x), 0)/2 - (Dh.get(x, 0)/2 if c < 3 else 0)
        ok = ok and rhs == Gh.get((c, x), 0)
print("G = -1/2 Lap + 1/2 gauge(V) - 1/2 delta D :", ok)
