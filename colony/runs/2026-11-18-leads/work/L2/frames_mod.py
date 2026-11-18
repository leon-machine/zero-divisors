"""Lead 1, route R2: frame functions on rational rays of Q^4 that depend only on the primitive integer vector
modulo m (up to sign).  Exploration script: exact arithmetic modulo a prime P (rank over F_P bounds the rank over Q
from below, so "only constants" is rigorous; a surviving solution is only a candidate).
Usage: python3 frames_mod.py m nframes seed [units]
  units=1 identifies r with u*r for every unit u mod m (two-adic projective points); default: sign only."""
import sys, random
from math import gcd
import numpy as np

m = int(sys.argv[1]); NF = int(sys.argv[2]); seed = int(sys.argv[3])
UNITS = len(sys.argv) > 4 and sys.argv[4] == '1'
P = 2147483647
random.seed(seed)

def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3,
            a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 - a1*b3 + a2*b0 + a3*b1,
            a0*b3 + a1*b2 - a2*b1 + a3*b0)

def prim(v):
    g = 0
    for c in v: g = gcd(g, abs(c))
    return tuple(c // g for c in v)

def cross(a, b):
    return (a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0])

def rnd3(B):
    while True:
        v = tuple(random.randint(-B, B) for _ in range(3))
        if any(v): return v

def rnd4(B):
    while True:
        v = tuple(random.randint(-B, B) for _ in range(4))
        if any(v): return v

units = [u for u in range(m) if gcd(u, m) == 1]
def key(v):
    r = tuple(c % m for c in v)
    if UNITS:
        return min(tuple((u*c) % m for c in r) for u in units)
    n = tuple((-c) % m for c in r)
    return min(r, n)

def frame(B):
    while True:
        u2 = prim(rnd3(B)); w = rnd3(B)
        u3 = cross(u2, w)
        if not any(u3): continue
        u3 = prim(u3); u4 = prim(cross(u2, u3))
        x = prim(rnd4(B))
        fr = [x] + [prim(qmul((0,) + u, x)) for u in (u2, u3, u4)]
        # sanity: pairwise orthogonal
        for i in range(4):
            for j in range(i):
                assert sum(a*b for a, b in zip(fr[i], fr[j])) == 0
        return fr

index = {}
rows = []
for n in range(NF):
    B = random.choice([1, 2, 3, 5, 9, 17])
    fr = frame(B)
    row = {}
    for v in fr:
        k = key(v)
        if k not in index: index[k] = len(index)
        row[index[k]] = row.get(index[k], 0) + 1
    rows.append(row)
N = len(index)
print("modulus", m, "classes seen", N, "frames", NF, flush=True)
A = np.zeros((NF, N), dtype=np.int64)
for i, row in enumerate(rows):
    for j, c in row.items(): A[i, j] = c
# rank over F_P by elimination
rank = 0; r = 0
piv_cols = []
for c in range(N):
    nz = np.nonzero(A[r:, c])[0]
    if len(nz) == 0: continue
    p = r + nz[0]
    if p != r: A[[r, p]] = A[[p, r]]
    inv = pow(int(A[r, c]), P - 2, P)
    A[r] = (A[r] * inv) % P
    col = A[:, c].copy(); col[r] = 0
    idx = np.nonzero(col)[0]
    if len(idx):
        A[idx] = (A[idx] - (col[idx, None] * A[r][None, :]) % P) % P
    piv_cols.append(c); r += 1
    if r == NF: break
print("rank", r, "of", N, "nullity", N - r, flush=True)
if N - r > 0 and N - r < 40:
    free = [c for c in range(N) if c not in set(piv_cols)]
    inv_index = {v: k for k, v in index.items()}
    print("free classes (first 20):", [inv_index[c] for c in free[:20]])
