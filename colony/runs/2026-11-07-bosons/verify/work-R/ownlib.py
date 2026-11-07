"""Referee R own-route recomputations, exact (Fractions, lib/GA.py). Independent constructions:
(1) rank of sigma_omega on the even algebra of a block, in the basis of the 8 even BLADES of Cl(2,2) (not matrix units);
(2) fluctuation variance for Q = b + b*, R = b - b* at (3/4, 1/4), N = 2, built from scratch;
(3) the pinned Fermi-Dirac total 331/33 by direct arithmetic;
(4) a deeper infinite-band test on a 10-mode window: psi = rho_2* rho_1* sea, [rho_3, rho_3*] psi = 3 psi, [rho_1, rho_3*] psi = 0;
(5) real states: sigma vanishes on pairs of self-adjoint elements (where the complex QCLT form would need i)."""
import sys
from fractions import Fraction as F
from itertools import combinations
sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA

def setup(m):
    sq = tuple([1, -1] * m)
    mul = lambda x, y: GA.mul(x, y, sq)
    v = [GA.scal(F(1, 2), GA.add(GA.gen(2*j), GA.gen(2*j+1))) for j in range(m)]
    w = [GA.scal(F(1, 2), GA.sub(GA.gen(2*j), GA.gen(2*j+1))) for j in range(m)]
    return sq, mul, v, w

def adj(x, sq):
    # T03 adjoint: reversion composed with sign flip of each negative-square generator
    out = {}
    for b, c in x.items():
        g = len(b); s = (-1) ** (g*(g-1)//2) * (-1) ** sum(1 for i in b if sq[i] == -1)
        out[b] = s * c
    return {b: c for b, c in out.items() if c}

def comm(mul, x, y): return GA.sub(mul(x, y), mul(y, x))

