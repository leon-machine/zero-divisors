"""Y3 scratch: the order-four element of Cl(10,0) and the charges of the sixteen (exact)."""
import sys
sys.path.insert(0, 'lib')
from fractions import Fraction as F
from itertools import combinations
import GA
SQ = GA.sig(10, 0)
g = [GA.gen(i) for i in range(10)]
def mul(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, SQ)
    return out
w = mul(*g)
print('omega^2 =', mul(w, w))
print('anticommutes with every generator:', all(GA.anticommutes(w, x, SQ) for x in g))
print('commutes with every bivector:', all(GA.commutes(w, mul(g[i], g[j]), SQ) for i, j in combinations(range(10), 2)))
print('anticommutes with a five-blade (Majorana-type, 126):', GA.anticommutes(w, mul(*g[:5]), SQ))
print('commutes with a four-blade:', GA.commutes(w, mul(*g[:4]), SQ))
# charges: X = 5 - 2N on the even half N = 0, 2, 4 (1 + 10 + 5 components)
from math import comb
for content, Ns in (('sixteen', (0, 2, 4)), ('fifteen', (2, 4))):
    q = []
    for N in Ns:
        q += [5 - 2 * N] * comb(5, N)
    print(content, 'n =', len(q), 'X mod 4:', sorted(set(x % 4 for x in q)), 'sum X =', sum(q), 'sum X^3 =', sum(x**3 for x in q),
          'count mod 2, 4, 16:', len(q) % 2, len(q) % 4, len(q) % 16)
