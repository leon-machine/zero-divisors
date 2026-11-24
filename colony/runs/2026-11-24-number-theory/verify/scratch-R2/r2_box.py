"""Referee R2: box test. Primitive integer rays with |entries| <= B, all orthogonal frames among them,
dimension of {f on rays, c : sum_F f = c for every frame F}, computed as (n+1) - rank mod p (exact integer
arithmetic mod p).  rank_p <= rank_Q, so dim_Q <= dim_p; and dim_Q >= 10 + (#rays in no frame), so dim_p equal to
that lower bound is an exact result.  Usage: python3 r2_box.py B [p]"""
import sys
import numpy as np
from itertools import product
from math import gcd

B = int(sys.argv[1]); P = int(sys.argv[2]) if len(sys.argv) > 2 else 33554393

def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
assert isprime(P) and P < 5 * 10**7

def prim(v):
    g = 0
    for c in v: g = gcd(g, c)
    if g != 1: return None
    for c in v:
        if c: return v if c > 0 else None

rays = sorted({v for v in product(range(-B, B + 1), repeat=4) if any(v) and prim(v) == v})
n = len(rays); idx = {r: i for i, r in enumerate(rays)}
A = np.array(rays, dtype=np.int64)
G = A @ A.T
orth = [np.nonzero(G[i] == 0)[0] for i in range(n)]
orthset = [set(o.tolist()) for o in orth]
frames = []
for i in range(n):
    for j in orth[i]:
        if j <= i: continue
        common = orthset[i] & orthset[j]
        for k in common:
            if k <= j: continue
            for l in common & orthset[k]:
                if l <= k: continue
                frames.append((i, j, k, l))
inframe = set(x for f in frames for x in f)
iso = n - len(inframe)

ncol = n + 1
piv = []            # pivot columns
Bm = np.zeros((0, ncol), dtype=np.int64)
def reduce_chunk(C):
    global Bm, piv
    if len(piv):
        C = (C - (C[:, piv] @ Bm) % P) % P
    # eliminate within chunk
    rows = C
    newrows = []
    while rows.shape[0]:
        nzr = np.nonzero(rows.any(axis=1))[0]
        if not len(nzr): break
        rows = rows[nzr]
        r0 = rows[0]
        c = int(np.nonzero(r0)[0][0])
        inv = pow(int(r0[c]), P - 2, P)
        r0 = (r0 * inv) % P
        rows = (rows[1:] - np.outer(rows[1:, c], r0) % P) % P
        # make r0 reduced against previously found new rows and vice versa
        for t in range(len(newrows)):
            cc = newrows[t][1]
            if r0[cc]:
                r0 = (r0 - r0[cc] * newrows[t][0]) % P
        for t in range(len(newrows)):
            v, cc = newrows[t]
            if v[c]:
                newrows[t] = ((v - v[c] * r0) % P, cc)
        newrows.append((r0, c))
    if newrows:
        NR = np.array([v for v, c in newrows], dtype=np.int64)
        nc = [c for v, c in newrows]
        if len(piv):
            Bm = (Bm - (Bm[:, nc] @ NR) % P) % P
        Bm = np.vstack([Bm, NR]); piv = piv + nc

CH = 400
for s in range(0, len(frames), CH):
    fr = frames[s:s + CH]
    C = np.zeros((len(fr), ncol), dtype=np.int64)
    for t, f in enumerate(fr):
        C[t, list(f)] = 1
        C[t, n] = P - 1
    reduce_chunk(C)
rk = len(piv)
dim = ncol - rk
print(f"B={B} p={P} rays={n} frames={len(frames)} rays_in_no_frame={iso} rank_p={rk} dim_p={dim} "
      f"excess_over_10_plus_isolated={dim - 10 - iso}")

# projection of the solution space onto S + {c}: rank increase when unit rows of S and c are added
def proj_dim(S):
    global Bm, piv
    saveB, savep = Bm.copy(), list(piv)
    C = np.zeros((len(S) + 1, ncol), dtype=np.int64)
    for t, i in enumerate(S): C[t, i] = 1
    C[len(S), n] = 1
    reduce_chunk(C)
    d = len(piv) - rk
    Bm, piv = saveB, savep
    return d
S1 = [idx[r] for r in rays if max(abs(c) for c in r) <= 1]
print(f"  projection onto the {len(S1)} rays of box 1 and c: dim {proj_dim(S1)} (10 = quadratic forms only)")
if B >= 2:
    S2 = [idx[r] for r in rays if max(abs(c) for c in r) <= 2]
    print(f"  projection onto the {len(S2)} rays of box 2 and c: dim {proj_dim(S2)}")
if B >= 3:
    S3 = [idx[r] for r in rays if max(abs(c) for c in r) <= 3]
    print(f"  projection onto the {len(S3)} rays of box 3 and c: dim {proj_dim(S3)}")
