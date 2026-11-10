import sys; sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, functools
from itertools import product
ONE=GA.sc(1)
def setup(m):
    sq=tuple(s for _ in range(m) for s in (1,-1))
    e=[GA.gen(2*k) for k in range(m)]; f=[GA.gen(2*k+1) for k in range(m)]
    return sq,e,f
def dag(x):
    r=GA.reverse(x)
    return {b:(c if sum(1 for i in b if i%2==1)%2==0 else -c) for b,c in r.items()}
def s0(x): return x.get((),F(0))
sq,e,f=setup(2)
M=lambda *xs: functools.reduce(lambda a,b: GA.mul(a,b,sq), xs)
p=[M(f[k],e[k]) for k in range(2)]
A1,A2,B1,B2=e[0],p[0],M(e[1],p[0]),p[1]
C=GA.add(M(A1,GA.add(B1,B2)),M(A2,GA.sub(B1,B2)))
K=M(e[0],f[1])
bl=[{b:F(1)} for b in GA.all_blades(4)]
print('K commutes C',GA.commutes(K,C,sq))
for L in bl:
    if GA.eq(M(L,L),ONE) and GA.commutes(L,K,sq) and GA.anticommutes(L,C,sq) and GA.eq(dag(L),L): print('L',L)
def om(rho,x): return s0(M(rho,x))/s0(rho)
for L in bl:
    if GA.eq(M(L,L),ONE) and GA.commutes(L,K,sq) and GA.anticommutes(L,C,sq) and GA.eq(dag(L),L):
        rho0=GA.scal(F(1,4),M(GA.add(ONE,K),GA.add(ONE,L)))
        assert GA.eq(M(rho0,rho0),rho0), L
        for r in (F(2),F(3),F(14,5),F(34,12)):
            y=GA.add(GA.sc(r),C); rho=M(y,rho0,dag(y))
            print(L, r, om(rho,C), 16*r/(r*r+8))
        break
# Bell state + rotor directions
for s1 in (1,-1):
  for s2 in (1,-1):
    rb=GA.scal(F(1,4),M(GA.add(ONE,GA.scal(F(s1),M(A1,B1))),GA.add(ONE,GA.scal(F(s2),M(A2,B2)))))
    print(s1,s2,'idem',GA.eq(M(rb,rb),rb),'S',om(rb,C), [om(rb,M(a,b)) for a in (A1,A2) for b in (B1,B2)], 'K',om(rb,K))
IB=M(B1,B2); print('IB^2',M(IB,IB))
rb=GA.scal(F(1,4),M(GA.add(ONE,M(A1,B1)),GA.add(ONE,M(A2,B2))))
for t in (F(1,2),F(2,5),F(5,12)):
    c=(1-t*t)/(1+t*t); s=2*t/(1+t*t)
    R=GA.add(GA.sc(c),GA.scal(-s,IB)); Rt=GA.add(GA.sc(c),GA.scal(s,IB))
    b1=M(R,B1); b2=M(Rt,B1)
    assert GA.eq(M(b1,b1),ONE) and GA.eq(dag(b1),b1) and GA.is_zero(GA.sub(M(b1,A2),M(A2,b1)))
    Ct=GA.add(M(A1,GA.add(b1,b2)),M(A2,GA.sub(b1,b2)))
    print(t,c,s,om(rb,Ct),2*(c+s), 8-om(rb,Ct)**2)
# non self-adjoint
x,y=F(17,8),F(15,8)
A=GA.add(GA.scal(x,e[0]),GA.scal(y,f[0])); print(M(A,A), GA.eq(dag(A),A))
rho=GA.scal(F(1,4),M(GA.add(ONE,e[0]),GA.add(ONE,p[1]))); print(GA.eq(M(rho,rho),rho),GA.eq(dag(rho),rho))
Cn=GA.add(M(A,GA.add(p[1],p[1])),M(A,GA.sub(p[1],p[1]))); print('nonherm S',om(rho,Cn), GA.commutes(A,p[1],sq))
