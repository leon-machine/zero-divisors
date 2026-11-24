"""P-B scratch, K-B4 second stage. Rays of Q^8 with entries in {0,1,-1}. Constraint used: for every
four-dimensional subspace U with an orthogonal basis of four family rays of EQUAL norm (so U is similar to the
standard Q^4), q(x) = f(x)(x.x) restricted to the family rays in U is a quadratic form on U. This is what the stored
two-mode theorem gives for an additive function on the rational projectors of Mat_8(Q) (frames of U completed by a
fixed frame of the complement). Null spaces are computed over Q (Fractions) and reduced mod p; rank mod p.
"""
import sys, itertools, random, time
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, '.')
P = 999983
n = 8
random.seed(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
NU = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
rays = []
for v in itertools.product((0, 1, -1), repeat=n):
    nz = [x for x in v if x != 0]
    if nz and nz[0] == 1:
        rays.append(v)
V = np.array(rays, dtype=np.int64); N = len(rays)
norm = (V * V).sum(axis=1)
G = V @ V.T
orth = (G == 0)
from p1_search_lib import Elim
E = Elim(N, P)
def left_null(rows):
    """rational left null space of the matrix with the given rows (list of lists of Fractions)."""
    m = len(rows); k = len(rows[0])
    A = [list(r) + [F(int(i == j)) for j in range(m)] for i, r in enumerate(rows)]
    r = 0
    for c in range(k):
        pv = next((i for i in range(r, m) if A[i][c] != 0), None)
        if pv is None: continue
        A[r], A[pv] = A[pv], A[r]
        inv = 1 / A[r][c]; A[r] = [x * inv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                fac = A[i][c]; A[i] = [x - fac * y for x, y in zip(A[i], A[r])]
        r += 1
    return [A[i][k:] for i in range(r, m)], r
mons = [(i, j) for i in range(4) for j in range(i, 4)]
def constraints(us):
    nu = [int(norm[u]) for u in us]
    proj = [G[u] for u in us]                      # x.u_i for all rays
    inU = (sum(proj[i] * proj[i] * (np.prod(nu) // nu[i]) for i in range(4)) == norm * np.prod(nu))
    members = np.nonzero(inU)[0]
    rows = []
    for x in members:
        c = [F(int(proj[i][x]), nu[i]) for i in range(4)]
        rows.append([c[i] * c[j] for i, j in mons])
    null, rk = left_null(rows)
    out = []
    for w in null:
        den = 1
        for x in w: den = den * x.denominator // np.gcd(den, x.denominator)
        row = np.zeros(N)
        for x, wk in zip(members, w):
            row[x] = (int(wk * den) * int(norm[x])) % P
        out.append(row)
    return out, len(members), rk
bynorm = {k: np.nonzero(norm == k)[0] for k in range(1, 9)}
nbn = {}
def rand_quad():
    while True:
        k = random.choice([1, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7, 8])
        fr = [int(random.choice(bynorm[k]))]
        cand = set(np.nonzero(orth[fr[0]] & (norm == k))[0].tolist())
        while len(fr) < 4 and cand:
            x = random.choice(tuple(cand)); fr.append(x)
            cand &= set(np.nonzero(orth[x] & (norm == k))[0].tolist())
        if len(fr) == 4: return fr
t0 = time.time(); done = 0; last = 0; stall = 0; seen = set(); sizes = {}
# the 70 coordinate four-spaces first
std = {tuple(r): i for i, r in enumerate(rays)}
for S in itertools.combinations(range(n), 4):
    us = [std[tuple(1 if k == j else 0 for k in range(n))] for j in S]
    rows, m, rk = constraints(us)
    if rows: E.add(np.array(rows))
print('coordinate four-spaces: rank', E.rank(), 'nullity', N - E.rank(), flush=True)
while done < NU:
    batch = []
    for _ in range(40):
        us = rand_quad(); done += 1
        rows, m, rk = constraints(us)
        sizes[m] = sizes.get(m, 0) + 1
        batch += rows
    if batch: E.add(np.array(batch))
    r = E.rank()
    if done % 200 == 0:
        print('subspaces', done, 'rank', r, 'nullity', N - r, 'time', round(time.time() - t0), flush=True)
    stall = stall + 1 if r == last else 0; last = r
    if N - r == 36 or stall >= 25: break
print('sizes of U cap family seen:', sorted(sizes.items()))
print('FINAL nullity', N - E.rank(), '(quadratic forms: 36) after', done, 'subspaces')
