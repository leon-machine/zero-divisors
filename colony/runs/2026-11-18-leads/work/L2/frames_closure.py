"""Lead 1: which rays of the box T (entries bounded by B) have their value determined by the values on the small
box S (entries bounded by b), by the frame equations inside T?  Exact over F_P (exploration; certificates redone
over Q).  Usage: python3 frames_closure.py b B"""
import sys, itertools, collections
from math import gcd
import numpy as np
b = int(sys.argv[1]); B = int(sys.argv[2]); n = 4
P = 2147483647
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
for i in range(N):
    for j in orth[i]:
        for k in orth[j]:
            if not G[i, k]: continue
            for l in orth[k]:
                if G[i, l] and G[j, l]: frames.append((i, j, k, l))
inS = np.array([max(abs(c) for c in v) <= b for v in rays])
out = [i for i in range(N) if not inS[i]]; ins = [i for i in range(N) if inS[i]]
order = out + ins            # eliminate outside columns first
A = np.zeros((len(frames), N + 1), dtype=np.int64)
pos = {c: t for t, c in enumerate(order)}
for r_, f in enumerate(frames):
    for x in f: A[r_, pos[x]] = 1
    A[r_, N] = P - 1
r = 0; piv = {}
for c in range(len(out)):
    nz = np.nonzero(A[r:, c])[0]
    if len(nz) == 0: continue
    p = r + nz[0]
    if p != r: A[[r, p]] = A[[p, r]]
    inv = pow(int(A[r, c]), P - 2, P)
    A[r] = (A[r] * inv) % P
    col = A[:, c].copy(); col[r] = 0
    ii = np.nonzero(col)[0]
    if len(ii): A[ii] = (A[ii] - (col[ii, None] * A[r][None, :]) % P) % P
    piv[c] = r; r += 1
    if r == len(frames): break
free = [c for c in range(len(out)) if c not in piv]
det = []
for c, row in piv.items():
    if not A[row, free].any(): det.append(order[c])
print("box", B, "rays", N, "outside S", len(out), "pivots", len(piv), "free outside", len(free), "determined by S:", len(det))
norm = lambda v: sum(x*x for x in v)
cnt_all = collections.Counter(norm(rays[i]) for i in out)
cnt_det = collections.Counter(norm(rays[i]) for i in det)
print("norm: determined/total outside S")
print(" ".join("%d:%d/%d" % (k, cnt_det.get(k, 0), cnt_all[k]) for k in sorted(cnt_all)))
import pickle
pickle.dump({'det': [rays[i] for i in det], 'rays': rays}, open('closure_%d_%d.pkl' % (b, B), 'wb'))
