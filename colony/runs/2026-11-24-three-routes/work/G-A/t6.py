import time, sys
from fractions import Fraction as F
from spin2 import *
L = int(sys.argv[1])
T = Torus(L); c0 = (L//2,)*3
string = [(c0[0]+d, c0[1], c0[2]) for d in (-1, 0, 1)]
f = {}
for x in string:
    f[(0, x)] = F(1, 2); f[(1, x)] = F(-1, 2); f[(2, x)] = F(-1, 2)
rho = T.ham(f)
def lap(u):
    out = {}
    for x, v in u.items():
        out[x] = out.get(x, 0) - 6*v
        for i in range(3):
            for s in (1, -1):
                y = T.sh(x, e(i), s)
                out[y] = out.get(y, 0) + v
    return {x: v for x, v in out.items() if v != 0}
def solve_poisson(rho):
    """phi with lap phi = rho, by the first linear relation among rho, lap rho, lap^2 rho, ... (exact)."""
    vs = [dict(rho)]
    basis = []      # (pivot site, reduced vector, combination over vs)
    while True:
        j = len(vs) - 1
        r = dict(vs[j]); comb = {j: F(1)}
        for piv, bv, bc in basis:
            c = r.get(piv, 0)
            if c != 0:
                for x, v in bv.items():
                    nv = r.get(x, 0) - c*v
                    if nv == 0: r.pop(x, None)
                    else: r[x] = nv
                for k, v in bc.items():
                    comb[k] = comb.get(k, 0) - c*v
        if not r:
            break
        piv = min(r)
        pv = r[piv]
        basis.append((piv, {x: v/pv for x, v in r.items()}, {k: v/pv for k, v in comb.items()}))
        vs.append(lap(vs[j]))
    # sum_k comb[k] lap^k rho = 0, comb[0] != 0
    c0_ = comb[0]
    phi = {}
    for k, c in comb.items():
        if k >= 1:
            for x, v in vs[k-1].items():
                phi[x] = phi.get(x, 0) - (c/c0_)*v
    return {x: v for x, v in phi.items() if v != 0}, len(vs) - 1
t0 = time.time()
# -2 lap phi = rho
phi, deg = solve_poisson({x: -v/2 for x, v in rho.items()})
print("krylov degree", deg, "time", time.time()-t0, "nonzero phi", len(phi))
print("check:", lap(phi) == {x: -v/2 for x, v in rho.items()})
newt = {(c, x): v for x, v in phi.items() for c in range(3)}
print("D newt == rho:", T.ham(newt) == rho)
kap = T.einstein(newt)
Gf = T.einstein(f)
off = [(c, x) for c in range(6) for x in T.sites if (c, x) not in Gf]
fail = [k for k in off if kap.get(k, 0) != 0]
print("comps", 6*len(T.sites), "supp G[f]", len(Gf), "off", len(off), "newtonian nonzero off", len(fail))
bysite = {x for (c, x) in fail}
print("sites failing", len(bysite), "of", len({x for (c,x) in off}))
# by component
print({c: sum(1 for (cc, x) in fail if cc == c) for c in range(6)})
# sample values
x0 = (c0[0]+3, c0[1], c0[2]); print("kap at +3 on axis:", [kap.get((c, x0), 0) for c in range(6)])
# static?
tau = F(1,2)
h, pi = dict(newt), {}
for n in range(2): h, pi = T.step(h, pi, tau)
print("newtonian curvature static:", T.einstein(h) == kap, "h changed on", sum(1 for k in set(h)|set(newt) if h.get(k,0)!=newt.get(k,0)))
h, pi = dict(f), {}
for n in range(2): h, pi = T.step(h, pi, tau)
G2 = T.einstein(h)
print("string curvature changed on", sum(1 for k in set(G2)|set(Gf) if G2.get(k,0)!=Gf.get(k,0)))
print("total time", time.time()-t0)
