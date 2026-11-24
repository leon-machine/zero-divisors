"""Scratch: Cl(l,l) as Mat_{2^l}(Q) through the Fock states; even subalgebra = two blocks. l = 3."""
import sys, time
sys.path.insert(0, '/home/claude/leon-machine/zero-divisors/lib')
from fractions import Fraction as F
from itertools import combinations
import GA

L = 3
SQ = tuple([1, -1] * L)   # e_j index 2j (square +1), f_j index 2j+1 (square -1)
def dag(x):
    out = {}
    for b, c in x.items():
        g = len(b)
        s = F(-1) ** (g * (g - 1) // 2)
        for k in b:
            s *= SQ[k]
        out[b] = s * c
    return out
def M(*xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out
v = [GA.scal(F(1, 2), GA.add(GA.gen(2 * j), GA.gen(2 * j + 1))) for j in range(L)]
w = [GA.scal(F(1, 2), GA.sub(GA.gen(2 * j), GA.gen(2 * j + 1))) for j in range(L)]
for j in range(L):
    assert GA.eq(dag(v[j]), w[j])
P0 = GA.sc(1)
for j in range(L):
    P0 = M(P0, w[j], v[j])
subsets = [S for k in range(L + 1) for S in combinations(range(L), k)]
s = [M(*([v[j] for j in S] + [P0])) for S in subsets]
N = len(s)
t0 = time.time()
ok = True
for i in range(N):
    for j in range(N):
        z = M(dag(s[i]), s[j])
        ok &= GA.eq(z, P0 if i == j else {})
print('orthonormal', ok)
tot = {}
for i in range(N):
    tot = GA.add(tot, M(s[i], dag(s[i])))
print('resolution', GA.eq(tot, GA.sc(1)))
print('P0 scalar part', P0.get((), 0))
def mat(x):
    out = []
    for i in range(N):
        row = []
        xi = M(dag(s[i]), x)
        for j in range(N):
            z = M(xi, s[j])
            # z = c P0
            c = z.get((), F(0)) / P0[()]
            assert GA.eq(z, GA.scal(c, P0))
            row.append(c)
        out.append(row)
    return out
blades = GA.all_blades(2 * L)
mats = {}
for b in blades:
    mats[b] = mat({b: F(1)})
print('time', time.time() - t0)
# rank 64
rows = [[c for row in mats[b] for c in row] for b in blades]
print('rank', GA.mat_rank(rows))
# transpose
okT = all(mat(dag({b: F(1)})) == [list(r) for r in zip(*mats[b])] for b in blades)
print('adjoint is transpose', okT)
# even blades: block diagonal for parity of |S|
par = [len(S) % 2 for S in subsets]
okE = all(all(mats[b][i][j] == 0 for i in range(N) for j in range(N) if par[i] != par[j]) for b in blades if len(b) % 2 == 0)
okO = all(all(mats[b][i][j] == 0 for i in range(N) for j in range(N) if par[i] == par[j]) for b in blades if len(b) % 2 == 1)
print('even blades block diagonal', okE, 'odd blades block off-diagonal', okO)
erows = [[c for row in mats[b] for c in row] for b in blades if len(b) % 2 == 0]
print('even rank', GA.mat_rank(erows))
print('time', time.time() - t0)
