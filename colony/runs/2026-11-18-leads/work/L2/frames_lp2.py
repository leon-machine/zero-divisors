"""Lead 1, K1d continued: mixed case.  Fix f(e_0) = f(e_1) = 1/2 and f((1,1,0,0)) = 1/2; the only quadratic form is
rho = diag(1/2, 1/2, 0, 0).  Ranges of f at other rays on the box.  Floating point: exploration only."""
import sys, itertools
from math import gcd
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
B = int(sys.argv[1])
targets = [tuple(int(c) for c in s.split(',')) for s in sys.argv[2:]]
n = 4
def prim_ok(v):
    g = 0
    for c in v: g = gcd(g, abs(c))
    if g != 1: return False
    for c in v:
        if c != 0: return c > 0
rays = [v for v in itertools.product(range(-B, B+1), repeat=n) if prim_ok(v)]
idx = {v: i for i, v in enumerate(rays)}
N = len(rays)
R = np.array(rays, dtype=np.int64)
G = (R @ R.T) == 0
orth = [np.nonzero(G[i, i+1:])[0] + i + 1 for i in range(N)]
frames = []
for i in range(N):
    for j in orth[i]:
        for k in orth[j]:
            if not G[i, k]: continue
            for l in orth[k]:
                if G[i, l] and G[j, l]: frames.append((i, j, k, l))
fixed = [((1,0,0,0), 0.5), ((0,1,0,0), 0.5), ((1,1,0,0), 0.5)]
A = lil_matrix((len(frames) + len(fixed), N)); b = np.ones(len(frames) + len(fixed))
for r, f in enumerate(frames):
    for x in f: A[r, x] = 1
for t, (v, val) in enumerate(fixed):
    A[len(frames) + t, idx[v]] = 1; b[len(frames) + t] = val
A = A.tocsr()
print("B", B, "rays", N, "frames", len(frames), flush=True)
for t in targets:
    c = np.zeros(N); c[idx[t]] = 1
    lo = linprog(c, A_eq=A, b_eq=b, bounds=(0, 1), method='highs')
    hi = linprog(-c, A_eq=A, b_eq=b, bounds=(0, 1), method='highs')
    q = (t[0]**2 + t[1]**2) / (2*sum(x*x for x in t))
    print("target", t, "min", round(lo.fun, 6), "max", round(-hi.fun, 6), "quadratic value", round(q, 6), flush=True)
