"""R3: C in both conventions of clause (5) on Cl(2,4). Kill: grade-4 part of phi(XY) differs from that of XY."""
import sys; sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as Fr
from itertools import combinations
import GA
S = GA.sig(2, 4); I6 = {tuple(range(6)): Fr(1)}; I6i = GA.scal(-1, I6)
P = list(combinations(range(6), 2))
X = {p: Fr(c) for p, c in zip(P, [1, 0, -3, 2, 5, 0, 1, -1, 4, 2, 0, 3, -2, 1, 7]) if c}
Y = {p: Fr(c) for p, c in zip(P, [0, 2, 1, -5, 3, 1, 0, 2, -1, 1, 6, 0, 1, -3, 2]) if c}
C = lambda x: GA.mul(GA.mul(I6, x, S), I6i, S)
phi = lambda x: GA.reverse(C(x))
g = lambda x, k: {b: c for b, c in x.items() if len(b) == k}
XY = GA.mul(X, Y, S)
print("conv1 C fixes X, Y:", C(X) == X and C(Y) == Y)
print("conv2 phi(XY) == YX:", phi(XY) == GA.mul(Y, X, S), " grade4 equal:", g(phi(XY), 4) == g(XY, 4), g(XY,4) != {})
print("phi(I6) = -I6:", phi(I6) == GA.scal(-1, I6))
