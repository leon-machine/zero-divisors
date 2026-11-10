import sys
sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
NM=4
SQ=GA.sig(NM,NM)  # e_0..e_3 (+), f = gen(4..7) (-)
ONE=GA.sc(1)
def mul(*xs):
    r=xs[0]
    for x in xs[1:]: r=GA.mul(r,x,SQ)
    return r
v=[GA.scal(F(1,2),GA.add(GA.gen(j),GA.gen(NM+j))) for j in range(NM)]
w=[GA.scal(F(1,2),GA.sub(GA.gen(j),GA.gen(NM+j))) for j in range(NM)]
n=[mul(v[j],w[j]) for j in range(NM)]
comm=lambda x,y: GA.sub(mul(x,y),mul(y,x))
a,a2,c,c2=0,1,2,3   # nu shell (a,a'), nu^c shell (c,c')
def Hblock(K,m,M):
    H=GA.scal(K,GA.add(*n))
    for (i,j,mu) in ((a,c,m),(a2,c2,m),(c,c2,M)):
        H=GA.add(H,GA.scal(mu,GA.add(mul(w[i],w[j]),mul(v[j],v[i]))))
    return H
ops=v+w
def vec(x):  # coordinates on mode operators
    # x is a vector (grade 1): express in e,f basis
    return [x.get((i,),F(0)) for i in range(2*NM)]
for (K,m,M) in [(F(0),F(1,3),F(5,2)),(F(2,7),F(3,4),F(11,5)),(F(1),F(1),F(0))]:
    H=Hblock(K,m,M)
    ok=True
    for o in ops:
        x1=comm(H,o); x2=comm(H,x1); x3=comm(H,x2); x4=comm(H,x3)
        assert all(len(b)==1 for b in x1 if x1[b]!=0)
        # ad^4 - (2K^2+2m^2+M^2) ad^2 + (K^2+ ...) 
        s=2*m*m+M*M; p=m**4
        # roots z=ad^2 : z = K^2 + E^2, E^2 roots of y^2 - s y + p
        # (z-K^2)^2 - s (z-K^2) + p = z^2 - (2K^2+s) z + K^4 + sK^2 + p
        r=GA.add(x4,GA.scal(-(2*K*K+s),x2),GA.scal(K**4+s*K*K+p,o))
        ok&=GA.is_zero({k:val for k,val in r.items() if val!=0})
    print((K,m,M),'quartic on mode operators:',ok)
# charges
N=GA.add(*n)
Lep=GA.sub(GA.add(n[a],n[a2]),GA.add(n[c],n[c2]))
Pm=mul(w[c],w[c2]); Pd=mul(w[a],w[c])
print('[N,P_M]=-2P_M',GA.eq(comm(N,Pm),GA.scal(-2,Pm)),' [N,P_D]=-2P_D',GA.eq(comm(N,Pd),GA.scal(-2,Pd)))
print('[Lep,P_D]=0',GA.is_zero({k:x for k,x in comm(Lep,Pd).items() if x!=0}),' [Lep,P_M]=+2P_M',GA.eq(comm(Lep,Pm),GA.scal(2,Pm)))
# quasi-spin
Jp=mul(v[c2],v[c]); Jm=Pm; Jz=GA.scal(F(1,2),GA.sub(GA.add(n[c],n[c2]),ONE))
print('quasi-spin: [Jz,J+]=J+',GA.eq(comm(Jz,Jp),Jp),'[J+,J-]=2Jz',GA.eq(comm(Jp,Jm),GA.scal(2,Jz)))
