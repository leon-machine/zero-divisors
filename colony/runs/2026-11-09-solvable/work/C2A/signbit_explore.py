import sys, time
from fractions import Fraction as F
sys.path.insert(0, '/home/claude/phys-graph/lib')
import fock, GA
NM = 5; DIM = 32
def mono(M):
    """sparse matrix {(row, col): c} -> tuple over cols of (row, sign)"""
    out = [None]*DIM
    for (r, c), v in M.items():
        assert out[c] is None and v in (1, -1)
        out[c] = (r, int(v))
    return tuple(out)
def mmul(A, B):  # (AB) col j: B maps j -> (r, s), A maps r -> (r2, s2)
    return tuple((A[B[j][0]][0], A[B[j][0]][1]*B[j][1]) for j in range(DIM))
I = tuple((j, 1) for j in range(DIM)); NEG = tuple((j, -1) for j in range(DIM))
tw = [mono(fock.majorana(p, NM)) for p in range(2*NM)]
pp = fock.parity(NM, modes=[2,3,4])
PP = mono(pp)
untw = [mmul(tw[p], PP) if p < 4 else tw[p] for p in range(2*NM)]
def group(gens):
    G = {I}; frontier = [I]
    while frontier:
        nf = []
        for g in frontier:
            for h in gens:
                x = mmul(g, h)
                if x not in G: G.add(x); nf.append(x)
        frontier = nf
    return G
t=time.time()
G = group(tw + [NEG]); print(len(G), time.time()-t)
G0 = group(untw + [NEG]); print(len(G0))
sq = [mmul(g,g) for g in tw]; print([ 1 if s==I else -1 if s==NEG else 0 for s in sq])
def rel(A,B):
    ab, ba = mmul(A,B), mmul(B,A)
    return 1 if ab==ba else -1 if ab==mmul(NEG,ba) else 0
print([[rel(tw[i],tw[j]) for j in range(10)] for i in range(10)])
print([[rel(untw[i],untw[j]) for j in range(10)] for i in range(10)])
