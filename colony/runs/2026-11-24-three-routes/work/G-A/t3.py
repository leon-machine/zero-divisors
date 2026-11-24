import time
from fractions import Fraction as F
from spin2 import *
def rank(rows):
    rows = [r[:] for r in rows]; rk = 0; ncol = len(rows[0]) if rows else 0
    for c in range(ncol):
        piv = next((r for r in range(rk, len(rows)) if rows[r][c] != 0), None)
        if piv is None: continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        pv = rows[rk][c]
        rows[rk] = [x / pv for x in rows[rk]]
        for r in range(len(rows)):
            if r != rk and rows[r][c] != 0:
                f = rows[r][c]; rows[r] = [x - f*y for x, y in zip(rows[r], rows[rk])]
        rk += 1
    return rk
for L in (2, 3):
    t0 = time.time()
    T = Torus(L)
    hidx = {(c, x): n for n, (c, x) in enumerate((c, x) for c in range(6) for x in T.sites)}
    N = len(hidx)
    # gauge images
    grows = []
    for i in range(3):
        for x in T.sites:
            img = T.gauge({(i, x): F(1)})
            r = [F(0)]*N
            for k, v in img.items(): r[hidx[k]] = v
            grows.append(r)
    rg = rank(grows)
    # D as rows: D^T unit site -> use adjoint: compute D on unit h
    cols = {}
    drows = [[F(0)]*N for _ in T.sites]
    sidx = {x: n for n, x in enumerate(T.sites)}
    grow = [[F(0)]*N for _ in range(N)]
    for k, n in hidx.items():
        for x, v in T.ham({k: F(1)}).items(): drows[sidx[x]][n] = v
        for k2, v in T.einstein({k: F(1)}).items(): grow[hidx[k2]][n] = v
    rd = rank(drows); rG = rank(grow)
    print(L, "N", N, "rank gauge", rg, "rank D", rd, "rank G", rG, "phys = N - rd - rg =", N - rd - rg, "ker G", N - rG, time.time()-t0)
