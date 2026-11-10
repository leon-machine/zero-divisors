import sys
P='/home/claude/phys-graph/proposals/synthesis.higgs-sector-brst-does-not-fix-the-breaking-pattern-of-two-doublets'
sys.path.insert(0,'/home/claude/phys-graph/lib'); sys.path.insert(0,P)
import tp_premise; tp_premise.configure('/home/claude/phys-graph/store')
from check import *
f = pot(1, 1, -1, F(3, 2))
v_off = [F(1), F(0), F(0), F(0), F(0), F(1, 2), F(0), F(0)]
g=grad(f,v_off); print('grad',[str(x) for x in g], f(from_vec(v_off)))
print([[str(sum(x*y for x,y in zip(g,vec(act(a,from_vec(unit(i))))))) for i in range(8)] for a in range(4)])
for (lam, mu, kap, w), v in (((1, 1, -1, F(3, 2)), [F(1)] + [F(0)] * 3 + [F(1)] + [F(0)] * 3),((1, 1, 1, 2), [F(1)] + [F(0)] * 3 + [F(0), F(0), F(1), F(0)])):
    print('stat', grad(pot(lam,mu,kap,w),v))
I=HYP
def emb(z1, z2):
    a = GA.add(GA.sc(z1[0]), GA.scal(z1[1], I)); b = GA.add(GA.sc(z2[0]), GA.scal(z2[1], I))
    return GA.add(a, GA.mul(BIV[2], b, SQ))
def cmul(z, w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
z=((F(1),F(2)),(F(-1),F(1,2)))
print(GA.eq(GA.mul(I, emb(*z), SQ), emb(cmul((F(0),F(1)),z[0]), cmul((F(0),F(-1)),z[1]))))
pts = [(q([2, 0, 0, 0]), q([F(-1, 2), 0, 0, 0]), True), (q([1, 0, 0, 0]), q([-1, 0, 3, 0]), False),
       (q([1, 1, 0, 0]), q([F(-1, 2), F(-1, 2), 0, 0]), True), (q([1, 0, 0, 0]), q([-1, 0, 2, 0]), False),
       (q([0, 1, 1, 0]), q([0, F(-1, 2), F(-1, 2), 3]), False)]
for p1,p2,b in pts:
    psi=GA.mul(GA.reverse(p2),p1,SQ); print(coords(psi), [str(x) for x in invariants((p1,p2))], rank_at((p1,p2)), b)
