"""R3: independent spectrum of D = -(x ^ d) - 5/2 on S-valued polynomials of degree k <= 3 on R^(0,6),
with my own spinor ideal (idempotent (1+e0e1e2)(1+e0e4e5)(1+e1e3e5)/8) and exact ranks.

Kill condition (before running): the sign of every eigenvalue on P_k must be negative exactly on the blocks
x^j M_(k-j) with j even, i.e. eigenvalue -(m + 5/2) with multiplicity 8 C(m+4,4) for m = k, k-2, ... and
+(m + 5/2) for m = k-1, k-3, ...; anything else kills the parity pattern of clause (iv).
"""
import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as Fr
from itertools import combinations_with_replacement
import GA

S = GA.sig(0, 6)
one = GA.sc(1)
def bl(*ix): return {tuple(ix): Fr(1)}
P = GA.scal(Fr(1, 8), GA.mul(GA.mul(GA.add(one, bl(0, 1, 2)), GA.add(one, bl(0, 4, 5)), S), GA.add(one, bl(1, 3, 5)), S))
assert GA.mul(P, P, S) == P
blades = GA.all_blades(6)
# basis of the left ideal Cl P
cands = [GA.mul({b: Fr(1)}, P, S) for b in blades]
basis = []
for c in cands:
    if GA.rank_of_vectors([GA.basis_vector_of(x, blades) for x in basis + [c]]) > len(basis):
        basis.append(c)
DIM = len(basis)
print("ideal dimension", DIM)
B = [GA.basis_vector_of(x, blades) for x in basis]
PIV = []
for r in range(64):
    if GA.field_rank([[B[i][rr] for i in range(DIM)] for rr in PIV + [r]]) > len(PIV):
        PIV.append(r)
assert len(PIV) == DIM
def coords(x):
    # solve sum c_i B_i = x on pivot rows, then verify on all 64 coordinates
    v = GA.basis_vector_of(x, blades)
    sol = GA.field_solve([[B[i][r] for i in range(DIM)] for r in PIV], [v[r] for r in PIV])
    assert all(sum(sol[i] * B[i][r] for i in range(DIM)) == v[r] for r in range(64))
    return sol
def lmat(g):
    return [list(col) for col in zip(*[coords(GA.mul(g, basis[i], S)) for i in range(DIM)])]
E = [lmat(GA.gen(a)) for a in range(6)]
EB = {(a, b): lmat(bl(a, b)) for a in range(6) for b in range(a + 1, 6)}

def monos(k):
    out = []
    for c in combinations_with_replacement(range(6), k):
        m = [0] * 6
        for i in c: m[i] += 1
        out.append(tuple(m))
    return out
def spectrum(k):
    ms = monos(k); idx = {(m, a): n for n, (m, a) in enumerate((m, a) for m in ms for a in range(DIM))}
    N = len(idx); M = [[Fr(0)] * N for _ in range(N)]
    for (m, a), col in idx.items():
        M[col][col] -= Fr(5, 2)
        for (i, j), G in EB.items():
            for up, down, s in ((i, j, 1), (j, i, -1)):   # (x_i d_j - x_j d_i)
                if m[down]:
                    m2 = list(m); m2[down] -= 1; m2[up] += 1; m2 = tuple(m2)
                    for b in range(DIM):
                        if G[b][a]:
                            M[idx[(m2, b)]][col] -= s * m[down] * G[b][a]
    spec = {}
    lam = -(k + Fr(5, 2))
    while lam <= k + Fr(5, 2):
        d = N - GA.field_rank([[M[r][c] - (lam if r == c else 0) for c in range(N)] for r in range(N)])
        if d: spec[lam] = d
        lam += 1
    return spec, N
def C(n, r):
    from math import comb
    return comb(n, r)
allok = True
for k in range(4):
    spec, N = spectrum(k)
    expect = {}
    for j in range(k + 1):
        m = k - j
        lam = -(m + Fr(5, 2)) if j % 2 == 0 else (m + Fr(5, 2))
        expect[lam] = 8 * C(m + 4, 4)
    ok = spec == expect and sum(spec.values()) == N
    allok = allok and ok
    print("k=%d dim P_k=%d spectrum %s %s" % (k, N, {str(a): b for a, b in sorted(spec.items())}, "ok" if ok else "FAIL"))
print("ALL OK" if allok else "FAILED")
