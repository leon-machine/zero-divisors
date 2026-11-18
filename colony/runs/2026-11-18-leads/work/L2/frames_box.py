"""Lead 1: the frame system on the rational rays with integer entries bounded by B, in dimension n (3 or 4).
Unknowns: one per ray.  Equations: sum over each orthogonal frame inside the set = w (homogeneous form with an extra
unknown w).  Nullity over F_P bounds the nullity over Q from above.  The quadratic forms give n(n+1)/2.
Usage: python3 frames_box.py n B"""
import sys, itertools
from math import gcd
import numpy as np
n = int(sys.argv[1]); B = int(sys.argv[2])
P = 2147483647
def prim_ok(v):
    g = 0
    for c in v: g = gcd(g, abs(c))
    if g != 1: return False
    for c in v:
        if c != 0: return c > 0
rays = [v for v in itertools.product(range(-B, B+1), repeat=n) if prim_ok(v)]
idx = {v: i for i, v in enumerate(rays)}
N = len(rays)
orth = [[] for _ in range(N)]
for i in range(N):
    a = rays[i]
    for j in range(i+1, N):
        if sum(x*y for x, y in zip(a, rays[j])) == 0:
            orth[i].append(j)
osets = [set(o) for o in orth]
frames = []
if n == 3:
    for i in range(N):
        for j in orth[i]:
            for k in orth[j]:
                if k in osets[i]: frames.append((i, j, k))
else:
    for i in range(N):
        for j in orth[i]:
            cj = [k for k in orth[j] if k in osets[i]]
            for k in cj:
                for l in orth[k]:
                    if l in osets[i] and l in osets[j]: frames.append((i, j, k, l))
print("dimension", n, "bound", B, "rays", N, "frames", len(frames), flush=True)
# rays in no frame are free unknowns: count them apart
used = set(x for f in frames for x in f)
print("rays in at least one frame:", len(used))
cols = sorted(used); cmap = {c: t for t, c in enumerate(cols)}
M = len(cols)
A = np.zeros((len(frames), M + 1), dtype=np.int64)
for r, f in enumerate(frames):
    for x in f: A[r, cmap[x]] = 1
    A[r, M] = P - 1          # minus w
r = 0
for c in range(M + 1):
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
    if r == len(frames): break
print("rank", r, "unknowns (rays in frames + weight)", M + 1, "nullity", M + 1 - r, "quadratic forms:", n*(n+1)//2)
