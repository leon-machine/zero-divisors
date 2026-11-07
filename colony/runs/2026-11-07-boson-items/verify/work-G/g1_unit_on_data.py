"""Referee G, own route: which sign does I4 take on the null data of N (E_perp = transverse part of n.F)?"""
import sys; sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
SQ = (1, -1, -1, -1)
m = lambda *xs: __import__('functools').reduce(lambda a, b: GA.mul(a, b, SQ), xs, GA.sc(1))
g = GA.gen
n = GA.add(g(0), g(3)); nb = GA.sub(g(0), g(3))
I4 = m(g(0), g(1), g(2), g(3)); J = m(g(1), g(2))
grade = lambda x, k: {b: c for b, c in x.items() if len(b) == k}
def Eperp(Fb):
    v = grade(m(n, Fb), 1)
    return GA.add(GA.scal(v.get((1,), 0), g(1)), GA.scal(v.get((2,), 0), g(2)))
for u in (g(1), g(2), GA.add(GA.scal(3, g(1)), GA.scal(-2, g(2)))):
    a = grade(m(n, u), 2); b = grade(m(nb, u), 2)
    print('I4(n^u) = (n^u)J :', GA.eq(m(I4, a), m(a, J)), '  I4(nb^u) = (nb^u)J :', GA.eq(m(I4, b), m(b, J)),
          '  I4(nb^u) = -(nb^u)J = J(nb^u):', GA.eq(m(I4, b), GA.neg(m(b, J))) and GA.eq(m(I4, b), m(J, b)))
    print('   E_perp(n^u) =', Eperp(a), '  E_perp(nb^u) =', Eperp(b))
# generic bivector: E_perp(I4 F) versus E_perp(F) J
import itertools
for seed in range(3):
    Fb = {}
    for j, bl in enumerate(itertools.combinations(range(4), 2)):
        c = F((j * 5 + 3 + seed * 2) % 7 - 3, 1 + (j + seed) % 2)
        if c: Fb[bl] = c
    E = Eperp(Fb); EI = Eperp(m(I4, Fb))
    print('seed', seed, ' E(I4F) = E J :', GA.eq(EI, m(E, J)), '  E(I4F) = -E J = J E :', GA.eq(EI, GA.neg(m(E, J))))
    # in terms of eps = g1 E
    eps = m(g(1), E); epsI = m(g(1), EI)
    print('      eps(I4F) = eps J:', GA.eq(epsI, m(eps, J)), '  eps(I4F) = -eps J:', GA.eq(epsI, GA.neg(m(eps, J))))
# plane wave along nb (varies along the generators of N) vs along n (constant along them)
print('n . nb =', GA.dot(n, nb, SQ) if hasattr(GA,'dot') else None)
