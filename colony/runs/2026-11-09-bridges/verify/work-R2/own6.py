# own route for proposal 3 (i): trace of left multiplication on A P as the trace of the linear map on the whole algebra A -> A, y -> x y P, by matrix in blade basis
from own1 import bsign, mul
from fractions import Fraction as F
from itertools import combinations
import random
random.seed(7)
def run(p,q,Pf,nc):
    d=p+q; sq=[1]*p+[-1]*q
    def bl(idx):
        m=0
        for i in idx: m|=1<<i
        # ordered product sign is +1 for increasing index
        return {m:F(1)}
    Fb={}
    for a,b in combinations(range(d),2): Fb[(1<<a)|(1<<b)]=F(random.randint(-9,9),random.randint(1,7))
    F2=mul(Fb,Fb,sq); X=-2*F2.get(0,F(0))
    # vector trace
    tr=F(0)
    for mu in range(d):
        a={1<<mu:F(1)}
        def act(a):
            u=mul(a,Fb,sq); v=mul(Fb,a,sq)
            return {k:(u.get(k,0)-v.get(k,0))/2 for k in set(u)|set(v)}
        tr+=act(act(a)).get(1<<mu,F(0))
    P={0:F(1)}
    for idx in Pf:
        u=bl(idx); assert mul(u,u,sq)=={0:1}
        f=dict(u); f[0]=f.get(0,0)+1
        P=mul(P,{k:v/2 for k,v in f.items()},sq)
    assert mul(P,P,sq)==P
    def T(x):
        t=F(0)
        for b in range(1<<d):
            t+=mul(mul(x,{b:F(1)},sq),P,sq).get(b,F(0))
        return t
    rd=T({0:F(1)})
    ct=T({k:v/4 for k,v in F2.items()})/2
    # commutant P A P : look for an element of square -P
    return (p,q),'vector s',4*tr/X,'real dim',rd,'spinor s',4*ct/X,'expect',F(-nc,2)
for a in (((2,1),((0,2),),2),((1,2),((0,1),),2),((1,3),((0,3),),4),((3,1),((0,3),),4),((4,1),((0,4),(0,3,4)),4),((1,4),((0,1),(2,3,4)),4)):
    print(run(a[0][0],a[0][1],a[1],a[2]))
# Cl(2,1): P A P
sq=[1,1,-1]; P={0:F(1,2),0b101:F(1,2)}
span=set()
for b in range(8):
    r=mul(mul(P,{b:F(1)},sq),P,sq)
    span.add(tuple(sorted(r.items())))
print('Cl(2,1) P b P images:',len(span)-(1 if () in span else 0),'distinct nonzero'); 
for s in span: print('  ',dict(s))
