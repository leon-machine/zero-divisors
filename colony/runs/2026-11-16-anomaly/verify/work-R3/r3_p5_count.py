"""R3: the signed count modulo 16 and the sums of X = 5 - 2N, from my own tables.

Kill conditions (before running):
 K1 a torus involution of SU(3) x SU(2) x U(1)_Y on the sixteen reversing a number of states other than 0 or 8,
    or reversing the singlet, kills (vi); the set of counts {2r - 16} must be {-16, 0} and {2r - 15} = {-15, 1};
    the gcd of differences must be 16 (else 16 is not the largest modulus).
 K2 sum X, sum X^3 over the sixteen (by occupation number of the five modes) not (0, 0), over the fifteen not
    (-5, -125), or with the full state for the empty one sum X != -10, kills the anomaly sums of (vi).
"""
import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as Fr
from itertools import combinations, product
from math import gcd
import GA  # noqa: F401

# states: (colour phase coefficients on (a1, a2) as a 3-vector index or None, 2T3, 6Y, name)
col = [(1, 0), (0, 1), (-1, -1)]
states = []
for c in col:
    for t in (1, -1):
        states.append((c, t, 1, "Q"))
for c in col:
    states.append(((-c[0], -c[1]), 0, -4, "u^c"))
    states.append(((-c[0], -c[1]), 0, 2, "d^c"))
for t in (1, -1):
    states.append(((0, 0), t, -3, "L"))
states.append(((0, 0), 0, 6, "e^c"))
states.append(((0, 0), 0, 0, "nu^c"))
assert len(states) == 16
D = 24   # parameters a1, a2, b, c in units of pi/D, ranging over [0, 2D)
patterns = {}
for a1, a2, b, c in product(range(0, 2 * D, 2), range(0, 2 * D, 2), range(2 * D), range(0, 2 * D, 2)):
    ph = [s[0][0] * a1 + s[0][1] * a2 + s[1] * b + s[2] * c for s in states]
    if all(p % D == 0 for p in ph):
        patterns[tuple((p // D) % 2 for p in ph)] = (a1, a2, b, c)
rev = sorted({sum(p) for p in patterns})
singlet_rev = any(p[15] for p in patterns)
print("sign patterns:", len(patterns), " reversed counts:", rev, " singlet ever reversed:", singlet_rev)
c16 = sorted({2 * sum(p) - 16 for p in patterns}); c15 = sorted({2 * sum(p) - 15 for p in patterns})
print("signed counts of omega g: sixteen", c16, " fifteen", c15)
g = 0
for S in (c16, c15):
    for x in S:
        for y in S:
            g = gcd(g, abs(x - y))
print("gcd of differences:", g, " classes mod 16:", {x % 16 for x in c16}, {x % 16 for x in c15})
print("three fifteen-component generations: count", 3 * -15, "->", (3 * -15) % 16)

# K2: X = 5 - 2N on the even states of five modes
even = [S for k in (0, 2, 4) for S in combinations(range(5), k)]
X = lambda S: 5 - 2 * len(S)
sx = lambda L, p: sum(X(S) ** p for S in L)
fifteen = [S for S in even if len(S) != 0]
swapped = fifteen + [tuple(range(5))]
print("sixteen: sum X =", sx(even, 1), " sum X^3 =", sx(even, 3))
print("fifteen: sum X =", sx(fifteen, 1), " sum X^3 =", sx(fifteen, 3))
print("full state for empty: sum X =", sx(swapped, 1), " X(full) mod 4 =", X(tuple(range(5))) % 4)
