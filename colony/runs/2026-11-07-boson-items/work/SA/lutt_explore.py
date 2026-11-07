import sys; sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, time, itertools
M=2; L=2*M
s=tuple([1,-1]*(2*L)); mul=lambda x,y: GA.mul(x,y,s)
cre=lambda j: GA.add(GA.scal(F(1,2),GA.gen(2*j)),GA.scal(F(1,2),GA.gen(2*j+1)))
ann=lambda j: GA.add(GA.scal(F(1,2),GA.gen(2*j)),GA.scal(F(-1,2),GA.gen(2*j+1)))
R=list(range(L)); Lm=list(range(L,2*L))
n=[mul(cre(j),ann(j)) for j in range(2*L)]
vac=GA.sc(1)
for j in range(2*L): vac=mul(vac,mul(ann(j),cre(j)))
def basis(occ):
    st=vac
    for j in reversed(range(2*L)):
        if occ[j]: st=mul(cre(j),st)
    return st
rhoR=lambda q: GA.add(*[mul(cre(R[j]),ann(R[j+q])) for j in range(L-q)])
rhoL=lambda q: GA.add(*[mul(cre(Lm[j+q]),ann(Lm[j])) for j in range(L-q)])
def star(x):
    out={}
    for b,c in x.items():
        g=len(b); sg=(-1)**(g*(g-1)//2)*(-1)**sum(1 for i in b if s[i]==-1); out[b]=sg*c
    return out
H0=GA.add(*[GA.scal(F(2*j+1,2)-M,n[R[j]]) for j in range(L)], *[GA.scal(M-F(2*j+1,2),n[Lm[j]]) for j in range(L)])
g4,g2=F(1,2),F(9,10)
q=1
V=GA.add(GA.scal(g4,GA.add(mul(star(rhoR(q)),rhoR(q)),mul(star(rhoL(q)),rhoL(q)))), GA.scal(g2,GA.add(mul(rhoR(q),rhoL(q)),mul(star(rhoL(q)),star(rhoR(q))))))
H=GA.add(H0,V)
beta=GA.add(star(rhoR(q)),GA.scal(F(1,3),rhoL(q)))
C=GA.sub(mul(H,beta),mul(beta,H))
good=bad=0
for occ in itertools.product((0,1),repeat=2*L):
    psi=basis(occ)
    lhs=mul(C,psi); rhs=GA.scal(F(6,5)*q,mul(beta,psi))
    ec = occ[R[0]]==1 and occ[R[-1]]==0 and occ[Lm[0]]==0 and occ[Lm[-1]]==1
    e=GA.eq(lhs,rhs)
    if ec and not e: print("edge-clean but fails",occ)
    if e: good+=1
    if not ec and not e: bad+=1
print(good,bad)
