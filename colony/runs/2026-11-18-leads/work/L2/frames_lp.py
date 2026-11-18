"""Lead 1, K1d: linear programme on a box of rays.  Floating point (HiGHS): exploration only.
Usage: python3 frames_lp.py n B  target...   (target ray as comma list, e.g. 1,1,0,0)"""
import sys, itertools
from math import gcd
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
n = int(sys.argv[1]); B = int(sys.argv[2])
targets = [tuple(int(c) for c in s.split(',')) for s in sys.argv[3:]]
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
if n == 3:
    for i in range(N):
        for j in orth[i]:
            for k in orth[j]:
                if G[i, k]: frames.append((i, j, k))
else:
    for i in range(N):
        for j in orth[i]:
            for k in orth[j]:
                if not G[i, k]: continue
                for l in orth[k]:
                    if G[i, l] and G[j, l]: frames.append((i, j, k, l))
print("n", n, "B", B, "rays", N, "frames", len(frames), flush=True)
A = lil_matrix((len(frames) + 1, N))
b = np.ones(len(frames) + 1)
for r, f in enumerate(frames):
    for x in f: A[r, x] = 1
e0 = tuple([1] + [0]*(n-1))
A[len(frames), idx[e0]] = 1
A = A.tocsr()
for t in targets:
    c = np.zeros(N); c[idx[t]] = 1
    lo = linprog(c, A_eq=A, b_eq=b, bounds=(0, 1), method='highs')
    hi = linprog(-c, A_eq=A, b_eq=b, bounds=(0, 1), method='highs')
    q = t[0]**2 / sum(x*x for x in t)
    print("target", t, "min", round(lo.fun, 9) if lo.status == 0 else lo.message, "max", round(-hi.fun, 9) if hi.status == 0 else hi.message, "quadratic value", q, flush=True)
