"""Lead 1: a sparse certificate that the value at a target ray is fixed by the values on S (entries bounded by b),
from frames inside the box B.  L1-minimal combination by LP (floating point, exploration), then rationalised and
verified exactly.  Usage: python3 frames_cert.py b B t0,t1,t2,t3"""
import sys, itertools, collections
from math import gcd
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix, hstack
b = int(sys.argv[1]); B = int(sys.argv[2]); target = tuple(int(c) for c in sys.argv[3].split(','))
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
inS = [max(abs(c) for c in v) <= b for v in rays]
rows = [i for i in range(N) if not inS[i]]
rpos = {c: t for t, c in enumerate(rows)}
M = lil_matrix((len(rows), len(frames)))
for c, f in enumerate(frames):
    for x in f:
        if x in rpos: M[rpos[x], c] = 1
rhs = np.zeros(len(rows)); rhs[rpos[idx[target]]] = 1
M = M.tocsr()
Aeq = hstack([M, -M]).tocsr()
res = linprog(np.ones(2*len(frames)), A_eq=Aeq, b_eq=rhs, bounds=(0, None), method='highs')
print("status", res.status, "L1", res.fun)
lam = res.x[:len(frames)] - res.x[len(frames):]
supp = [c for c in range(len(frames)) if abs(lam[c]) > 1e-9]
print("frames used", len(supp))
cert = []
for c in supp:
    q = Fraction(float(lam[c])).limit_denominator(1000)
    cert.append((q, [rays[x] for x in frames[c]]))
# exact verification
tot = collections.defaultdict(Fraction)
wsum = Fraction(0)
for q, fr in cert:
    wsum += q
    for v in fr: tot[v] += q
bad = [(v, c) for v, c in tot.items() if c != 0 and not (max(abs(x) for x in v) <= b) and v != target]
print("exact check: residual outside S:", bad[:5], "coefficient at target:", tot[target], "sum of coefficients (weight):", wsum)
print("identity:  f(target) =", wsum, "* w  -  sum over S of:")
for v, c in sorted(tot.items()):
    if c != 0 and v != target: print("   ", c, v)
print("certificate frames:")
for q, fr in sorted(cert, key=lambda t: -abs(t[0])): print("  ", q, fr)
