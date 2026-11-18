"""Lead 1: does the frame system on the box T (entries bounded by B) force every solution to be a quadratic form on
the small box S (entries bounded by b)?  Dimension of the projection of the solution space of T onto the unknowns of
S (and the weight).  10 would be rigidity of S (in dimension 4).  Exact over F_P; rank over F_P is at most the rank
over Q, so the printed projection dimension can be off in either direction only if P divides a pivot; it is rerun
with a second prime.  Usage: python3 frames_proj.py n b B [prime]"""
import sys, itertools
from math import gcd
import numpy as np
n = int(sys.argv[1]); b = int(sys.argv[2]); B = int(sys.argv[3])
P = int(sys.argv[4]) if len(sys.argv) > 4 else 2147483647
def prim_ok(v):
    g = 0
    for c in v: g = gcd(g, abs(c))
    if g != 1: return False
    for c in v:
        if c != 0: return c > 0
rays = [v for v in itertools.product(range(-B, B+1), repeat=n) if prim_ok(v)]
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
inS = [max(abs(c) for c in v) <= b for v in rays]
print("n", n, "S bound", b, "T bound", B, "rays", N, "frames", len(frames), "rays of S", sum(inS), flush=True)
def rank(A):
    A = A.copy(); r = 0
    for c in range(A.shape[1]):
        nz = np.nonzero(A[r:, c])[0]
        if len(nz) == 0: continue
        p = r + nz[0]
        if p != r: A[[r, p]] = A[[p, r]]
        inv = pow(int(A[r, c]), P - 2, P)
        A[r] = (A[r] * inv) % P
        col = A[:, c].copy(); col[r] = 0
        ii = np.nonzero(col)[0]
        if len(ii): A[ii] = (A[ii] - (col[ii, None] * A[r][None, :]) % P) % P
        r += 1
        if r == A.shape[0]: break
    return r
A = np.zeros((len(frames), N + 1), dtype=np.int64)
for r_, f in enumerate(frames):
    for x in f: A[r_, x] = 1
    A[r_, N] = P - 1
rA = rank(A)
out = [i for i in range(N) if not inS[i]]
rO = rank(A[:, out])
nS = sum(inS)
print("rank", rA, "rank outside S", rO, "projection dimension onto S and w:", nS + 1 - rA + rO, "quadratic forms:", n*(n+1)//2)
