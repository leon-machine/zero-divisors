import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
from itertools import combinations
import GA

def dag_sign(b, sq):
    g = len(b); s = (-1) ** (g * (g - 1) // 2)
    for i in b: s *= sq[i]
    return s
def dagger(x, sq): return {b: c * dag_sign(b, sq) for b, c in x.items()}
def bl(b): return {tuple(b): F(1)}
def comm(x, y, sq): return GA.sub(GA.mul(x, y, sq), GA.mul(y, x, sq))

def analyse(p, q):
    n = p + q; sq = GA.sig(p, q)
    blades = [b for k in range(n + 1) for b in combinations(range(n), k)]
    herm = [b for b in blades if dag_sign(b, sq) == 1]
    for b in herm:
        assert GA.mul(bl(b), bl(b), sq) == {(): F(1)}
    top = tuple(range(n))
    central = [b for b in herm if b and all(GA.commutes(bl(b), GA.gen(i), sq) for i in range(n))]
    nonc = [b for b in herm if b and b not in central]
    # witness: commuting pair h,k of noncentral hermitian blades with product not central and not scalar
    wit = None
    for h, k in combinations(nonc, 2):
        if GA.commutes(bl(h), bl(k), sq):
            pr = GA.mul(bl(h), bl(k), sq); pb = list(pr)[0]
            if pb != () and pb not in central:
                wit = (h, k); break
    # full CHSH witness among blades
    chsh = None
    for a1, a2 in combinations(nonc, 2):
        if not GA.anticommutes(bl(a1), bl(a2), sq): continue
        cands = [b for b in nonc if GA.commutes(bl(b), bl(a1), sq) and GA.commutes(bl(b), bl(a2), sq)]
        for b1, b2 in combinations(cands, 2):
            if GA.anticommutes(bl(b1), bl(b2), sq):
                chsh = (a1, a2, b1, b2); break
        if chsh: break
    return len(herm), central, wit, chsh

for n in range(1, 7):
    for p in range(n, -1, -1):
        q = n - p
        h, c, wit, chsh = analyse(p, q)
        print((p, q), 'dimH', h, 'central', c, 'commuting-noncentral-pair', wit, 'CHSH blades', chsh)
