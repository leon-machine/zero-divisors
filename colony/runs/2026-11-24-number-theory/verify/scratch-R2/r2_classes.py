"""Referee R2: try to refute with class functions.  For a map cls: primitive ray -> finite class set, find all
g on classes and c with sum_{r in F} g(cls(r)) = c on many random frames F = {x, ax, bx, abx}.  The constants always
solve.  dim computed as (#classes + 1) - rank mod p; since rank_p <= rank_Q, dim_p == 1 proves dim_Q == 1 exactly
(for the frames used).  Integer arithmetic only."""
import random
from math import gcd
from itertools import product

P = 33554393
import numpy as np
import sys

def qm(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 + a2*b0 + a3*b1 - a1*b3, a0*b3 + a3*b0 + a1*b2 - a2*b1)
def prim(v):
    g = 0
    for c in v: g = gcd(g, c)
    v = tuple(c // g for c in v)
    for c in v:
        if c: return v if c > 0 else tuple(-t for t in v)
def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

random.seed(20261124)
def rand_frame(H):
    while True:
        x = tuple(random.randint(-H, H) for _ in range(4))
        a = tuple(random.randint(-H, H) for _ in range(3))
        w = tuple(random.randint(-H, H) for _ in range(3))
        b = cross(a, w)
        if any(x) and any(a) and any(b): break
    A, Bq = (0,) + a, (0,) + b
    fr = [prim(x), prim(qm(A, x)), prim(qm(Bq, x)), prim(qm(qm(A, Bq), x))]
    assert all(sum(p*q for p, q in zip(fr[i], fr[j])) == 0 for i in range(4) for j in range(i))
    return fr

def v(p, n):
    k = 0
    while n % p == 0: n //= p; k += 1
    return k
def sqfree_class(n, ps=(2, 3, 5, 7, 11)):
    return tuple(v(p, n) % 2 for p in ps)

def modN(N):
    def f(r):
        a = tuple(c % N for c in r); b = tuple((-c) % N for c in r)
        return min(a, b)
    return f
FAMILIES = {
    "primitive vector mod 2": modN(2), "mod 3": modN(3), "mod 4": modN(4), "mod 5": modN(5), "mod 8": modN(8),
    "v2(r.r)": lambda r: min(v(2, sum(c*c for c in r)), 6),
    "v5(r.r)": lambda r: min(v(5, sum(c*c for c in r)), 6),
    "v3(r.r)": lambda r: min(v(3, sum(c*c for c in r)), 6),
    "r.r mod squares (2,3,5,7,11 parity)": lambda r: sqfree_class(sum(c*c for c in r)),
    "r.r mod 8 and mod 5": lambda r: (sum(c*c for c in r) % 8, sum(c*c for c in r) % 5),
    "(r mod 4, v2(r.r))": lambda r: (modN(4)(r), min(v(2, sum(c*c for c in r)), 4)),
}

def rank_mod_p(rows, ncol):
    M = np.array(rows, dtype=np.int64) % P
    rk = 0
    for c in range(ncol):
        nz = np.nonzero(M[rk:, c])[0]
        if not len(nz): continue
        p = rk + nz[0]
        M[[rk, p]] = M[[p, rk]]
        M[rk] = (M[rk] * pow(int(M[rk, c]), P - 2, P)) % P
        col = M[:, c].copy(); col[rk] = 0
        M = (M - np.outer(col, M[rk]) % P) % P
        rk += 1
        if rk == M.shape[0]: break
    return rk

frames = [rand_frame(9) for _ in range(6000)]
SKIP = set(sys.argv[1:])
for name, cls in FAMILIES.items():
    if any(k in name for k in SKIP): continue
    labels = {}
    rows = []
    for fr in frames:
        cs = [cls(r) for r in fr]
        for c in cs: labels.setdefault(c, len(labels))
    m = len(labels)
    for fr in frames:
        row = [0] * (m + 1)
        for r in fr: row[labels[cls(r)]] += 1
        row[m] = -1
        rows.append(row)
    # dedupe rows to speed up
    rows = [list(t) for t in set(tuple(r) for r in rows)]
    rk = rank_mod_p(rows, m + 1)
    print(f"{name:40s} classes seen={m:5d} distinct frame rows={len(rows):5d} dim of solutions={m + 1 - rk}"
          f"{'  (only constants: exact)' if m + 1 - rk == 1 else '  EXCESS'}")
