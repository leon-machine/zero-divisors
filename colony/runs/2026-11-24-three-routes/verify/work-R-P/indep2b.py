import sys; sys.path.insert(0,'/home/claude/leon-machine/zero-divisors/lib')
from fractions import Fraction as F
import GA
sq=(1,-1,1,-1)
def P(*xs):
    o=GA.sc(F(1))
    for x in xs: o=GA.mul(o,x,sq)
    return o
def dag(x):
    out={}
    for b,c in x.items():
        g=len(b); s=F(-1)**(g*(g-1)//2)
        for k in b: s*=sq[k]
        out[b]=s*c
    return out
ONE=GA.sc(F(1)); s0=lambda x:x.get((),F(0))
e1,f1,e2,f2=[GA.gen(i) for i in range(4)]
# own route to the atom: the projector onto a ray via the ideal basis, built from the CAR vacuum
v=[GA.scal(F(1,2),GA.add(e1,f1)),GA.scal(F(1,2),GA.add(e2,f2))]
w=[GA.scal(F(1,2),GA.sub(e1,f1)),GA.scal(F(1,2),GA.sub(e2,f2))]
p0=P(w[0],v[0],w[1],v[1]); s=[p0,P(v[0],p0),P(v[1],p0),P(v[0],v[1],p0)]
r=(-1,2,-2,-1); y=GA.add(*[GA.scal(F(c),si) for c,si in zip(r,s)])
Pi=GA.scal(F(1,10),P(y,dag(y)))
assert GA.eq(P(Pi,Pi),Pi)
A=[e1,P(f1,e1)]; B=[P(e2,f1,e1),P(f2,e2)]
om=lambda x: s0(P(Pi,x))/s0(Pi)
corr=[om(P(A[i],B[j])) for i in range(2) for j in range(2)]
S=corr[0]+corr[1]+corr[2]-corr[3]
print(corr,S,S*S<8, float(S))
