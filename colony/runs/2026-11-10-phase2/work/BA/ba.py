import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
from itertools import combinations, product
import GA
ONE = GA.sc(F(1))
def dsign(b, sq):
    g = len(b); s = (-1) ** (g * (g - 1) // 2)
    for i in b: s *= sq[i]
    return s
def dag(x, sq): return {b: c * dsign(b, sq) for b, c in x.items()}
def prod(sq, *xs):
    r = ONE
    for x in xs: r = GA.mul(r, x, sq)
    return r
def s0(x): return x.get((), F(0))
def clean(x): return {b: c for b, c in x.items() if c != 0}
def blade(b): return {tuple(b): F(1)}
def bsq(b, sq): return s0(prod(sq, blade(b), blade(b)))
def bcomm(b1, b2):
    # blades commute iff |b1||b2| - |b1 & b2| even
    return (len(b1) * len(b2) - len(set(b1) & set(b2))) % 2 == 0
def maximal_T(sq, order):
    """greedy maximal set of independent commuting blades of square +1 whose group omits -1"""
    n = len(sq); gens = []; group = {(): 1}  # blade -> sign
    for b in order:
        if not b or bsq(b, sq) != 1: continue
        if any(not bcomm(b, g) for g in gens): continue
        if b in group: continue
        new = {}
        for t, s in group.items():
            c, bb = GA.blade_mul(t, b, sq)
            new[bb] = s * c
        group.update(new); gens.append(b)
    return gens, group
def idem(sq, gens):
    P = ONE
    for b in gens:
        P = prod(sq, P, GA.scal(F(1, 2), GA.add(ONE, blade(b))))
    return clean(P)
def vec(x, blades): return [x.get(b, F(0)) for b in blades]
def corner_dims(sq, P):
    n = len(sq); blades = GA.all_blades(n)
    full = []; sym = []
    for b in blades:
        y = clean(prod(sq, P, blade(b), P))
        full.append(vec(y, blades))
        ys = clean(GA.add(y, dag(y, sq)))
        sym.append(vec(ys, blades))
    return GA.rank_of_vectors(full), GA.rank_of_vectors(sym)
