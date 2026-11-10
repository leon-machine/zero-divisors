import sys; sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, functools
ONE=GA.sc(1)
sq=(1,-1,1,-1); e=[GA.gen(0),GA.gen(2)]; f=[GA.gen(1),GA.gen(3)]
M=lambda *xs: functools.reduce(lambda a,b: GA.mul(a,b,sq), xs)
s0=lambda x: x.get((),F(0))
p=[M(f[k],e[k]) for k in range(2)]
v=[GA.scal(F(1,2),GA.add(e[k],f[k])) for k in range(2)]; w=[GA.scal(F(1,2),GA.sub(e[k],f[k])) for k in range(2)]
E2=M(e[1],p[0])
def pair(c,s):
    r=c*c-s*s
    return GA.add(GA.scal(F(1,4),M(GA.add(ONE,M(p[0],p[1])),GA.add(ONE,GA.scal(r,p[0])))),GA.scal(c*s,GA.add(M(w[0],w[1]),M(v[1],v[0]))))
for c,s in ((F(3,5),F(4,5)),(F(20,29),F(21,29)),(F(5,13),F(12,13))):
    rho=pair(c,s)
    assert GA.eq(M(rho,rho),rho)
    T=[[4*s0(M(rho,a,b)) for b in (E2,p[1])] for a in (e[0],p[0])]
    loc=[4*s0(M(rho,a)) for a in (e[0],p[0],E2,p[1])]
    # max CHSH over planar directions = 2 sqrt(sum of squared singular values) = 2 sqrt(tr T^T T)
    tt=sum(x*x for row in T for x in row)
    print(c,s,'T',T,'local',loc,'max^2 = 4*trTTT =',4*tt,' 4(1+4c^2s^2)=',4*(1+4*c*c*s*s),' (2(c+s))^2=',4*(c+s)**2)
