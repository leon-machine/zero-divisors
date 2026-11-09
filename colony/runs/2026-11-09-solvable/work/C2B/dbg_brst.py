import sys
sys.path.insert(0,'/home/claude/phys-graph/lib'); sys.path.insert(0,'synthesis.higgs-sector-brst-does-not-fix-the-breaking-pattern-of-two-doublets')
import tp_premise; tp_premise.configure('/home/claude/phys-graph/store')
from check import *
counts={}; bad=[]
for c in product((-1,0,1),repeat=8):
    P=(q(c[:4]),q(c[4:])); r=rank_at(P); N1,N2,K,Kp=invariants(P)
    counts[r]=counts.get(r,0)+1
    zero=all(x==0 for x in c); want=0 if zero else (3 if Kp==0 else 4)
    if r!=want or K+Kp!=N1*N2: bad.append((c,r,want,K,Kp,N1,N2))
print(counts, len(bad), bad[:5])
H2=F(1)
pts = [(q([2, 0, 0, 0]), q([F(-1, 2), 0, 0, 0]), True), (q([1, 0, 0, 0]), q([-1, 3, 0, 0]), False),
       (q([1, 1, 0, 0]), q([F(-1, 2), F(-1, 2), 0, 0]), True), (q([1, 0, 0, 0]), q([-1, 0, 2, 1]), False),
       (q([0, 1, 1, 0]), q([0, F(-1, 2), F(-1, 2), 3]), False)]
for p1,p2,b in pts:
    psi=GA.mul(GA.reverse(p2),p1,SQ); print(coords(psi), invariants((p1,p2)), rank_at((p1,p2)), b)
