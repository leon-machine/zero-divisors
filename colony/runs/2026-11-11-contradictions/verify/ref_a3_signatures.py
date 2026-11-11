#!/usr/bin/env python3
"""Referee check for A3: signature bookkeeping of clauses (2) and (3) of the wall-class theorem on a
one-dimensional transversal model, exact (GA.congruence_signature).  Model: G = diag(lam, +1.., -1..) with
the dying eigenvalue lam (> 0 physical side, < 0 far side, 0 on the wall); p = 2, q = 3 on the physical side."""
import sys
from fractions import Fraction as F
sys.path.insert(0, '/home/claude/phys-graph/lib')
import GA
check = GA.check
sig = GA.congruence_signature
p, q = 2, 3
n = p + q


def G(lam):
    return [lam] + [1] * (p - 1) + [-1] * q   # sig (p, q) for lam > 0, (p-1, q+1) for lam < 0


def diag(v):
    return [[F(v[i]) if i == j else F(0) for j in range(len(v))] for i in range(len(v))]


# clause (2): D = [[S, beta 1], [beta 1, -S]]
for lam, beta in ((F(1), F(0)), (F(-1), F(0)), (F(0), F(1)), (F(1, 3), F(1)), (F(-2, 5), F(1, 2))):
    S = G(lam)
    M = [[F(0)] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        M[i][i] = F(S[i]); M[n + i][n + i] = -F(S[i]); M[i][n + i] = beta; M[n + i][i] = beta
    s = sig(M)
    check(f"A3 clause (2) lam={lam} beta={beta}: signature (n,n) = ({n},{n}), nondegenerate", s == (n, n, 0))

# clause (3): exterior forms G + H (physical) and G + K_- (far), and the wall block
H = [[F(0), F(1)], [F(1), F(0)]]
phys = sig(diag(G(F(1)) + [1, -1]))
far = sig(diag(G(F(-1)) + [2, 2]))
check(f"A3 clause (3): physical exterior G+H {phys[:2]} equals far exterior G+K_- {far[:2]} = (p+1, q+1)",
      phys == far == (p + 1, q + 1, 0))
for mu, vs in ((F(1, 3), F(1)), (F(2), F(-1)), (F(1, 2), F(0))):
    # on the wall: Gbar (sig (p-1, q)) + block of (k, a, b)
    Gbar = [1] * (p - 1) + [-1] * q
    m = len(Gbar) + 3
    M = [[F(0)] * m for _ in range(m)]
    for i, g in enumerate(Gbar):
        M[i][i] = F(g)
    o = len(Gbar)
    M[o][o + 1] = M[o + 1][o] = mu
    M[o + 1][o + 1] = -2 * vs
    M[o + 2][o + 2] = F(2)
    check(f"A3 clause (3) wall block mu={mu}, varsigma={vs}: signature (p+1, q+1)", sig(M) == (p + 1, q + 1, 0))
# strict reading: one K on both sides cannot give equal totals
for K in ([1, -1], [1, 1], [-1, -1]):
    a = sig(diag(G(F(1)) + K)); b = sig(diag(G(F(-1)) + K))
    check(f"A3 strict reading K={K}: totals differ {a[:2]} vs {b[:2]}", a != b)
print("FAILURES:", GA.FAILURES)
