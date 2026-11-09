import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
sys.path.insert(0, "/home/claude/phys-graph/colony/runs/2026-11-08-colour-lattice/work/B/aside/synthesis.a-finite-subgroup-of-colour-shares-its-strong-coupling-expansion-through-link-degree-three")
import check as c
from fractions import Fraction as F
import GA
gb4, inv4 = c.invariant_data(4)
gb2, inv2 = c.invariant_data(2)
def proj_entry(inv, a, b):
    # P = B (B^T B)^-1 B^T
    keys = None
    k = len(inv)
    G = [[sum(x * inv[j].get(t, 0) for t, x in inv[i].items()) for j in range(k)] for i in range(k)]
    va = [v.get(a, 0) for v in inv]; vb = [v.get(b, 0) for v in inv]
    y = GA.field_solve(G, vb)
    return sum(p * q for p, q in zip(va, y))
print("E x^2", proj_entry(inv2, (0, 0), (0, 0)))
print("E x^4", proj_entry(inv4, (0, 0, 0, 0), (0, 0, 0, 0)))
for a in range(6):
    for b in range(6):
        v = proj_entry(inv4, (a, 0, 0, 0), (b, 0, 0, 0))
        if v: print("E U_ab x^3", a, b, v)
print("G E x^4", sum(F(1) for g in c.G if g[0] == (0, 1) ) , sum((1 if g[0]==(0,1) else (1 if g[0]==(0,-1) else 0)) for g in c.G)/F(96))
