"""Own route for P5: Dicke states on N two-level blocks as uniform superpositions over k-subsets (no Clifford
algebra), exact Fractions. Moments of B = K/sqrt(N) with K = sum_i sigma^-_i acting on subsets; compare with
(k)_m (N-k+1)^(m)/N^m; marginal P_m weight and the bound; pair correlation."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial
def ff(a, m):
    r = 1
    for i in range(m): r *= a - i
    return r
def rf(a, m):
    r = 1
    for i in range(m): r *= a + i
    return r
def K(vec):  # unflip one flipped block: subset A -> A \ {i}
    out = {}
    for A, c in vec.items():
        for i in A:
            B = tuple(x for x in A if x != i); out[B] = out.get(B, 0) + c
    return out
for N in range(1, 8):
    for k in range(N + 1):
        psi = {A: F(1) for A in combinations(range(N), k)}
        nrm = sum(c * c for c in psi.values())
        phi = psi
        for m in range(N + 2):
            val = sum(c * c for c in phi.values()) / nrm / F(N) ** m
            assert val == F(ff(k, m) * rf(N - k + 1, m), N ** m), (N, k, m)
            phi = K(phi)
        for m in range(N + 1):
            w = F(comb(N - m, k), comb(N, k))
            assert w >= 1 - F(k * m, N - k + 1) if k * m < N - k + 1 else True
        if N >= 2 and k >= 1:
            # <b_0* b_1>: amplitude moving the flip from block 1 to block 0
            s = sum(psi.get(tuple(sorted((set(A) - {1}) | {0})), 0) * c for A, c in psi.items() if 1 in A and 0 not in A)
            assert s / nrm == F(k * (N - k), N * (N - 1))
print("Dicke-subset route: moments, marginal bound and pair correlation agree for N = 1..7, all k")
# numbers at N = 100, k = 2: marginal error on m = 3 blocks and the second moment
N, k, m = 100, 2, 3
eps = F(k * m, N - k + 1); print("N=100,k=2,m=3: eps =", eps, float(eps), " bound 2sqrt(eps)+eps =", 2 * float(eps) ** 0.5 + float(eps))
print("omega_k(B*^2 B^2) at N=100,k=2:", F(ff(k, 2) * rf(N - k + 1, 2), N ** 2), "-> limit", ff(k, 2), "; Gaussian would give", 2 * k * k)
