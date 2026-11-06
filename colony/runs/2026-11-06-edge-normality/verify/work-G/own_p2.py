# Own route for proposal 2, with plain integer 2x2 matrices (no GA): e+ = [[0,1],[1,0]], e- = [[0,1],[-1,0]].
from itertools import product
from fractions import Fraction as F
def mm(X, Y): return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
I = ((1,0),(0,1)); EP = ((0,1),(1,0)); EM = ((0,1),(-1,0)); EPM = mm(EP, EM)
assert mm(EP,EP) == I and mm(EM,EM) == ((-1,0),(0,-1)) and EPM == ((-1,0),(0,1))
def comb(a,b,c,d): return tuple(tuple(a*I[i][j]+b*EP[i][j]+c*EM[i][j]+d*EPM[i][j] for j in range(2)) for i in range(2))
# Lambda_O inside a box of matrices: membership <=> alpha = delta and beta = gamma mod 2
LO = {comb(*v) for v in product(range(-4,5), repeat=4)}
box = list(product(range(-3,4), repeat=4))
for A,B,C,D in box:
    M = ((A,B),(C,D))
    assert (M in LO) == ((A-D) % 2 == 0 and (B-C) % 2 == 0), M
# index: residues of M2(Z) mod 2 hit by Lambda_O
res = {tuple(x % 2 for row in M for x in row) for M in LO}
print("Lambda_O mod 2 has", len(res), "of 16 residues -> index", 16 // len(res))
# idempotents of Lambda_O: trace of a nontrivial idempotent is 1, but trace on Lambda_O is 2*alpha (even)
for v in product(range(-3,4), repeat=4):
    M = comb(*v)
    if mm(M,M) == M: assert M in (I, ((0,0),(0,0)))
# integer idempotents of Lambda_W with Witt coordinates in {-1,0,1}: x = s + b a + c a' + d aa' -> [[s+d,b],[c,s]]
cnt = 0
for s,b,c,d in product((-1,0,1), repeat=4):
    M = ((s+d,b),(c,s))
    if mm(M,M) == M and M not in (I, ((0,0),(0,0))):
        cnt += 1; assert F(s) + F(d,2) == F(1,2)
print("nontrivial idempotents of Lambda_W in the {-1,0,1} box:", cnt)
# dagger = transpose: a -> E12, a' -> E21; MP inverse of E12 is E21 (Penrose equations with transpose)
E12 = ((0,1),(0,0)); E21 = ((0,0),(1,0))
T = lambda M: tuple(zip(*M))
assert mm(mm(E12,E21),E12) == E12 and mm(mm(E21,E12),E21) == E21
assert T(mm(E12,E21)) == mm(E12,E21) and T(mm(E21,E12)) == mm(E21,E12)
assert T(EP) == EP and T(EM) == tuple(tuple(-x for x in r) for r in EM)
print("dagger acts as transpose on e+, e-; E21 is the Moore-Penrose inverse of E12")
# every generalised inverse g of E12 (E12 g E12 = E12) gives g*(f(x+n)-f(x)) = f'(x) * (g E12), an idempotent
for g in product(range(-2,3), repeat=4):
    G = ((g[0],g[1]),(g[2],g[3]))
    if mm(mm(E12,G),E12) == E12:
        P = mm(G,E12); assert mm(P,P) == P
print("any generalised inverse of the null step gives derivative times an idempotent (not only the partner)")
