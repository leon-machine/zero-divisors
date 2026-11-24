"""P-B scratch, kill condition P1 on a finite family (K-B4).
Rays of Q^8 with entries in {0,1,-1} (3280). Unknowns: one value per ray. Relations, each valid for every function
on the rational self-adjoint idempotents of Mat_8(Q) that adds on orthogonal ones:
  (a) two orthogonal pairs of rays spanning the same plane have equal sums;
  (b) an orthogonal frame of 8 rays has the sum of the standard frame.
Rank over F_p (p = 999983) by exact modular elimination; all intermediate integers stay below 2^53, so the
double-precision matrix products are exact. rank_p <= rank_Q, so nullity_Q <= nullity_p; the 36 functions
r -> (r^T S r)/(r.r), S symmetric, are solutions, so nullity_p = 36 proves that the solution space is exactly these.
"""
import sys, itertools, random, time
import numpy as np
P = 999983
n = 8
random.seed(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
NFR = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
rays = []
for v in itertools.product((0, 1, -1), repeat=n):
    nz = [x for x in v if x != 0]
    if nz and nz[0] == 1:
        rays.append(v)
V = np.array(rays, dtype=np.int64)
N = len(rays)
idx = {r: i for i, r in enumerate(rays)}
G = V @ V.T
orth = (G == 0)
print('rays', N, 'orthogonal pairs', int(orth.sum()) // 2, flush=True)

class Elim:
    def __init__(self, ncol):
        self.B = np.zeros((0, ncol)); self.piv = []; self.ncol = ncol
    def add(self, M):
        M = np.mod(M, P).astype(np.float64)
        if self.piv:
            M = np.mod(M - np.mod(M[:, self.piv] @ self.B, P), P)
        new = []; newpiv = []
        for row in M:
            row = row.copy()
            for q, r in zip(newpiv, new):
                if row[q] != 0:
                    row = np.mod(row - row[q] * r, P)
            nzs = np.nonzero(row)[0]
            if len(nzs) == 0:
                continue
            q = int(nzs[0]); inv = pow(int(row[q]), P - 2, P)
            row = np.mod(row * inv, P)
            for k in range(len(new)):
                if new[k][q] != 0:
                    new[k] = np.mod(new[k] - new[k][q] * row, P)
            new.append(row); newpiv.append(q)
        if not new:
            return 0
        Mn = np.array(new)
        if self.piv:
            self.B = np.mod(self.B - np.mod(self.B[:, newpiv] @ Mn, P), P)
        self.B = np.vstack([self.B, Mn]); self.piv += newpiv
        return len(new)
    def rank(self):
        return len(self.piv)

E = Elim(N)
t0 = time.time()
# (a) plane relations
ii, jj = np.nonzero(np.triu(orth, 1))
print('pairs', len(ii), flush=True)
cols = list(itertools.combinations(range(n), 2))
A, Bv = V[ii], V[jj]
pl = np.stack([A[:, a] * Bv[:, b] - A[:, b] * Bv[:, a] for a, b in cols], axis=1)
g = np.gcd.reduce(np.abs(pl), axis=1); pl = pl // g[:, None]
first = np.array([row[np.nonzero(row)[0][0]] for row in pl]); pl = pl * np.sign(first)[:, None]
uniq, inv = np.unique(pl, axis=0, return_inverse=True)
inv = inv.ravel()
print('planes', len(uniq), flush=True)
order = np.argsort(inv, kind='stable'); rows = []
start = 0; cnt = np.bincount(inv)
nrel = 0
batch = []
def flush():
    global batch
    if batch:
        M = np.zeros((len(batch), N))
        for k, (pos, negs) in enumerate(batch):
            for x in pos: M[k, x] += 1
            for x in negs: M[k, x] -= 1
        E.add(M); batch = []
for c in cnt:
    grp = order[start:start + c]; start += c
    if c < 2: continue
    a0 = (ii[grp[0]], jj[grp[0]])
    for k in grp[1:]:
        batch.append((a0, (ii[k], jj[k]))); nrel += 1
        if len(batch) >= 400: flush()
flush()
print('plane relations', nrel, 'rank', E.rank(), 'nullity', N - E.rank(), 'time', round(time.time() - t0), flush=True)
# (b) random orthogonal frames by randomised depth-first search
std = [idx[tuple(1 if k == j else 0 for k in range(n))] for j in range(n)]
nb = [np.nonzero(orth[i])[0] for i in range(N)]
def rand_frame():
    while True:
        fr = [random.randrange(N)]
        cand = set(nb[fr[0]].tolist())
        while len(fr) < n and cand:
            x = random.choice(tuple(cand)); fr.append(x); cand &= set(nb[x].tolist())
        if len(fr) == n:
            return fr
last = E.rank(); stall = 0; done = 0
while done < NFR:
    for _ in range(300):
        batch.append((rand_frame(), std)); done += 1
    flush()
    r = E.rank()
    print('frames', done, 'rank', r, 'nullity', N - r, 'time', round(time.time() - t0), flush=True)
    stall = stall + 1 if r == last else 0; last = r
    if N - r == 36 or stall >= 4: break
print('FINAL nullity', N - E.rank(), '(quadratic forms: 36)')
