"""Own route for P3: Jordan-Wigner integer matrices (exact int64 arithmetic), independent of GA.
(i) window identity T = sum_j j n_j - N(N-1)/2 for L = 1..8; (iv) Luttinger relations scaled by 10 to
integers (g4 = 1/2, g2 = 9/10, r = 1/3, omega = 6/5): [10H, 3 beta*] = 12 (3 beta*) and the same for gamma*,
on which occupation vectors it holds."""
import numpy as np
from itertools import product

def ops(L):
    a = np.array([[0, 1], [0, 0]], dtype=np.int64); Z = np.diag([1, -1]).astype(np.int64); I = np.eye(2, dtype=np.int64)
    cs = []
    for j in range(L):
        m = np.array([[1]], dtype=np.int64)
        for k in range(L):
            m = np.kron(m, Z if k < j else (a if k == j else I))
        cs.append(m)   # annihilator of mode j; basis bit k = occupation of mode k (0 = |0>, 1 = |1>)
    return cs

for L in range(1, 9):
    c = ops(L); cd = [x.T for x in c]
    n = [cd[j] @ c[j] for j in range(L)]
    N = sum(n) if L else 0
    T = np.zeros_like(n[0])
    for q in range(1, L):
        rho = sum(cd[j] @ c[j + q] for j in range(L - q))
        T = T + rho.T @ rho
    rhs = sum(j * n[j] for j in range(L)) - (N @ (N - np.eye(2 ** L, dtype=np.int64))) // 2
    print("L =", L, "identity exact:", np.array_equal(T, rhs), "T diagonal:", np.count_nonzero(T - np.diag(np.diag(T))) == 0)

# Luttinger: R modes 0..3 (weights k+1/2, k = j-2: -3/2,-1/2,1/2,3/2), L modes 4..7 with weights +3/2..-3/2
c = ops(8); cd = [x.T for x in c]; n = [cd[j] @ c[j] for j in range(8)]
R = [0, 1, 2, 3]; Lf = [7, 6, 5, 4]       # L family in its own 'lowering' order: energy decreases along Lf? see below
wR = {0: -3, 1: -1, 2: 1, 3: 3}            # 2 * weight
wL = {4: 3, 5: 1, 6: -1, 7: -3}
H0x2 = sum(wR[j] * n[j] for j in R) + sum(wL[j] * n[j] for j in wL)   # 2 * H0
def rho_lower(order):  # moves a particle from order[j+1] to order[j]; lowering when weight increases along order
    return sum(cd[order[j]] @ c[order[j + 1]] for j in range(len(order) - 1))
rR = rho_lower(R)            # R: weight increases along 0,1,2,3
rL = rho_lower(Lf)           # L: weight increases along 7,6,5,4
# 10 H = 5 * (2 H0) + 10 g4 (...) + 10 g2 (...), g4 = 1/2, g2 = 9/10
H10 = 5 * H0x2 + 5 * (rR.T @ rR + rL.T @ rL) + 9 * (rR @ rL + rL.T @ rR.T)
beta3 = 3 * rR.T + rL; gamma3 = 3 * rL.T + rR
dim = 2 ** 8
def holds(Op, psi):
    lhs = (H10 @ Op - Op @ H10) @ psi
    return np.array_equal(lhs, 12 * (Op @ psi))
def vec(occ):
    idx = 0
    for k, o in enumerate(occ):  # bit order: kron puts mode 0 most significant
        idx = idx * 2 + o
    e = np.zeros(dim, dtype=np.int64); e[idx] = 1; return e
edge_ok_b = edge_ok_g = 0; offs_b = offs_g = 0; tot_off = 0
for occ in product((0, 1), repeat=8):
    clean = occ[0] == 1 and occ[3] == 0 and occ[7] == 1 and occ[4] == 0
    hb, hg = holds(beta3, vec(occ)), holds(gamma3, vec(occ))
    if clean:
        edge_ok_b += hb; edge_ok_g += hg
    else:
        tot_off += 1; offs_b += hb; offs_g += hg
print("edge-clean vectors: beta holds on", edge_ok_b, "/16, gamma on", edge_ok_g, "/16")
print("non-edge-clean basis vectors:", tot_off, "; beta relation still holds on", offs_b, ", gamma on", offs_g)
print("all-empty vector (not edge-clean): beta holds", holds(beta3, vec((0,)*8)), ", gamma holds", holds(gamma3, vec((0,)*8)))
