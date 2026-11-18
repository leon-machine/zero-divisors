"""Lead 1: certificate that f((2,1,0,0)) is fixed by the 24 rays of norm 1, 2, 4 with entries in {0,1,-1}, from
frames in the box of entries up to 4.  LP for a sparse combination (floating point), rationalised, verified exactly,
written to cert_2100.py as a Python literal."""
import itertools, collections
from math import gcd
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix, hstack
B = 4; target = (2, 1, 0, 0); n = 4
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
inS = [max(abs(c) for c in v) <= 1 and sum(c*c for c in v) in (1, 2, 4) for v in rays]
assert sum(inS) == 24
rows = [i for i in range(N) if not inS[i]]
rpos = {c: t for t, c in enumerate(rows)}
M = lil_matrix((len(rows), len(frames)))
for c, f in enumerate(frames):
    for x in f:
        if x in rpos: M[rpos[x], c] = 1
rhs = np.zeros(len(rows)); rhs[rpos[idx[target]]] = 1
M = M.tocsr()
res = linprog(np.ones(2*len(frames)), A_eq=hstack([M, -M]).tocsr(), b_eq=rhs, bounds=(0, None), method='highs')
print("status", res.status, "L1", res.fun)
lam = res.x[:len(frames)] - res.x[len(frames):]
cert = []
for c in range(len(frames)):
    if abs(lam[c]) > 1e-9:
        q = Fraction(float(lam[c])).limit_denominator(1000)
        cert.append((q, tuple(rays[x] for x in frames[c])))
tot = collections.defaultdict(Fraction); wsum = Fraction(0)
for q, fr in cert:
    wsum += q
    for v in fr: tot[v] += q
bad = [(v, c) for v, c in tot.items() if c != 0 and not inS[idx[v]] and v != target]
assert not bad and tot[target] == 1, (bad, tot[target])
print("frames", len(cert), "weight coefficient", wsum, "denominators", sorted(set(q.denominator for q, _ in cert)))
with open('cert_2100.py', 'w') as fh:
    fh.write("# (numerator, denominator, frame) : sum of coeff * indicator(frame) = e_(2,1,0,0) + sum over the 24 rays\n")
    fh.write("CERT = [\n")
    for q, fr in sorted(cert, key=lambda t: (-abs(t[0]), t[1])):
        fh.write("    (%d, %d, %r),\n" % (q.numerator, q.denominator, fr))
    fh.write("]\n")
print("support on the 24 rays:", sorted((v, str(c)) for v, c in tot.items() if c != 0 and v != target))
