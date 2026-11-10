import sys; sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, functools
ONE=GA.sc(1)
sq=(1,-1,1,-1); e=[GA.gen(0),GA.gen(2)]; f=[GA.gen(1),GA.gen(3)]
M=lambda *xs: functools.reduce(lambda a,b: GA.mul(a,b,sq), xs)
def dag(x):
    r=GA.reverse(x)
    return {b:(c if sum(1 for i in b if i%2==1)%2==0 else -c) for b,c in r.items()}
s0=lambda x: x.get((),F(0))
p=[M(f[k],e[k]) for k in range(2)]
A1,A2,B1,B2=e[0],p[0],M(e[1],p[0]),p[1]
ch=lambda A1,A2,B1,B2: GA.add(M(A1,GA.add(B1,B2)),M(A2,GA.sub(B1,B2)))
C=ch(A1,A2,B1,B2); K=M(e[0],f[1]); I=M(B1,B2)
Cp=M(C,I); print('Cperp is chsh(A2,-A1,B1,B2)',GA.eq(Cp,ch(A2,GA.neg(A1),B1,B2)), 'anti',GA.anticommutes(C,Cp,sq), GA.eq(M(Cp,Cp),M(C,C)), GA.eq(dag(Cp),Cp))
rho0=GA.scal(F(1,4),M(GA.add(ONE,M(A1,B1)),GA.sub(ONE,M(A2,B2))))
PK=GA.scal(F(1,2),GA.add(ONE,K))
print(GA.eq(rho0, GA.add(GA.scal(F(1,2),PK),GA.scal(F(1,8),GA.sub(C,Cp)))))
om=lambda r,x: s0(M(r,x))/s0(r)
for u in (F(0),F(-1,2),F(-2,5),F(1,3)):
    y=GA.add(ONE,GA.scal(u,I)); r=GA.scal(1/(1+u*u),M(y,rho0,dag(y)))
    c=(1-u*u)/(1+u*u); s=2*u/(1+u*u)
    print(u, om(r,C), om(r,Cp), 2*(c-s), -2*(c+s), GA.eq(M(r,r),r), GA.eq(M(K,r),r))
v=[GA.scal(F(1,2),GA.add(e[k],f[k])) for k in range(2)]; w=[GA.scal(F(1,2),GA.sub(e[k],f[k])) for k in range(2)]
for sg in (1,-1):
    st=GA.add(GA.scal(F(1,4),GA.add(ONE,M(p[0],p[1]))),GA.scal(F(sg,2),GA.add(M(w[0],w[1]),M(v[1],v[0]))))
    print(sg, om(st,C), om(st,Cp), GA.eq(M(st,st),st), GA.eq(st, GA.scal(F(1,4),M(GA.add(ONE,M(p[0],p[1])),GA.sub(ONE,M(e[1],f[0]))))))
