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
def M(sq, *xs):
    r = GA.sc(1)
    for x in xs: r = GA.mul(r, x, sq)
    return r
def chsh(sq, A1, A2, B1, B2):
    return GA.add(M(sq, A1, B1), M(sq, A1, B2), M(sq, A2, B1), GA.neg(M(sq, A2, B2)))
ONE = GA.sc(1)
# --- one mode per party, Cl(2,2): e1 f1 e2 f2 = gens 0,1,2,3
sq = (1, -1, 1, -1)
e1, f1, e2, f2 = [GA.gen(i) for i in range(4)]
p1, p2 = M(sq, f1, e1), M(sq, f2, e2)
# twisted B: e2 p1, p2
B1t = M(sq, e2, p1)
for x in (e1, p1, B1t, p2):
    assert dagger(x, sq) == x and M(sq, x, x) == ONE
print('twist commute', [GA.commutes(a, b, sq) for a in (e1, p1) for b in (B1t, p2)], 'untwisted e1,e2 anticommute', GA.anticommutes(e1, e2, sq))
C = chsh(sq, e1, p1, B1t, p2)
C2 = M(sq, C, C); print('twisted C', C, 'C^2', C2)
# even state (|00>+|11>)/sqrt2 : rho = 1/4 (1+p1p2)(1) + 1/2 (w1w2 + v2v1)
v = [GA.scal(F(1,2), GA.add(e, f)) for e, f in ((e1, f1), (e2, f2))]
w = [GA.scal(F(1,2), GA.sub(e, f)) for e, f in ((e1, f1), (e2, f2))]
rho = GA.add(GA.scal(F(1,4), GA.add(ONE, M(sq, p1, p2))), GA.scal(F(1,2), GA.add(M(sq, w[0], w[1]), M(sq, v[1], v[0]))))
print('rho', rho, 'pure', M(sq, rho, rho) == rho, 'herm', dagger(rho, sq) == rho)
G = M(sq, p1, p2); print('even', GA.commutes(rho, G, sq))
val = lambda x: 4 * M(sq, rho, x).get((), F(0))
print('corrs', [val(M(sq, a, b)) for a in (e1, p1) for b in (B1t, p2)])
# rotated: A1 = p1, A2 = e1 ; B1=(p2 + e2p1)*(3/5,4/5)..., use rational rotor
def comb(c, s, x, y): return GA.add(GA.scal(c, x), GA.scal(s, y))
for (c, s) in ((F(3,5), F(4,5)), (F(5,13), F(12,13)), (F(20,29), F(21,29)), (F(119,169), F(120,169))):
    Bp = comb(c, s, p2, B1t); Bm = comb(c, -s, p2, B1t)
    A1 = p1; A2 = e1
    Cc = chsh(sq, A1, A2, Bp, Bm)
    print(c, s, 'val', val(Cc), 'C2', M(sq, Cc, Cc))
# graded hermitian part
X, Y, Z = M(sq, e1, p2), M(sq, p1, e2), M(sq, p1, p2)
Hh = GA.add(X, Y, GA.neg(Z)); print('graded herm part sq', M(sq, Hh, Hh), 'e1e2 dagger anti', dagger(M(sq, e1, e2), sq) == GA.neg(M(sq, e1, e2)))
# --- two modes per party Cl(4,4): gens e_k=2k, f_k=2k+1
sq8 = (1, -1) * 4
e = [GA.gen(2*k) for k in range(4)]; f = [GA.gen(2*k+1) for k in range(4)]
A1 = M(sq8, f[0], e[0]); A2 = M(sq8, e[0], f[1]); B1 = M(sq8, f[2], e[2]); B2 = M(sq8, e[2], f[3])
for x in (A1, A2, B1, B2): assert dagger(x, sq8) == x and M(sq8, x, x) == ONE
print('even commute', all(GA.commutes(a, b, sq8) for a in (A1, A2) for b in (B1, B2)), GA.anticommutes(A1, A2, sq8), GA.anticommutes(B1, B2, sq8))
C = chsh(sq8, A1, A2, B1, B2); print('C^2 two modes', M(sq8, C, C))
# other even hermitian involutions of two modes
