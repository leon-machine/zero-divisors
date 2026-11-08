# Referee F: independent recomputation (own Clifford product, own Hilbert symbols). Not GA.py.
from fractions import Fraction as F
from itertools import product
SQ=(1,-1,-1,-1,1,-1)
def bmul(a,b,sq):
    s=1; x=a
    # sign of reordering
    t=a>>1; c=0
    while t: c+=bin(t&b).count('1'); t>>=1
    s=-1 if c&1 else 1
    m=a&b; i=0
    while m:
        if m&1: s*=sq[i]
        m>>=1; i+=1
    return s,a^b
def mul(A,B,sq):
    out={}
    for a,x in A.items():
        for b,y in B.items():
            s,k=bmul(a,b,sq); out[k]=out.get(k,0)+s*x*y
    return {k:v for k,v in out.items() if v}
def vec(c): return {1<<i:F(v) for i,v in enumerate(c) if v}
def frame(L):
    n0=[0,0,0,0,F(1,2),F(1,2)]; ni=[0,0,0,0,1,-1]
    W=[ni[i]-F(L,6)*n0[i] for i in range(6)]
    return vec(W)
for L in (F(6),F(7,3),F(-3),F(27,4)):
    d=L/3; W=frame(L); bas=[vec([1 if j==i else 0 for j in range(6)]) for i in range(4)]+[W]
    om={0:F(1)}
    for v in bas: om=mul(om,v,SQ)
    rev=tuple(-s for s in SQ); omr={0:F(1)}
    for v in bas: omr=mul(omr,v,rev)
    print("L",L,"omega^2",mul(om,om,SQ),"d",d,"omega'^2",mul(omr,omr,rev))
# Hilbert symbols over Q_p (p odd and p=2), standard formulas
def vp(x,p):
    x=F(x); n,dd=x.numerator,x.denominator; v=0
    while n%p==0: n//=p; v+=1
    while dd%p==0: dd//=p; v-=1
    return v
def unit(x,p):
    x=F(x); v=vp(x,p); return x/F(p)**v
def leg(a,p):
    a%=p; return 1 if pow(a,(p-1)//2,p)==1 else -1
def hil(a,b,p):
    a,b=F(a),F(b); al,be=vp(a,p),vp(b,p); u,w=unit(a,p),unit(b,p)
    u=u.numerator*u.denominator; w=w.numerator*w.denominator  # same square class unit
    if p!=2:
        e=(-1)**(al*be*((p-1)//2))
        return e*leg(u,p)**be*leg(w,p)**al
    eps=lambda x:((x-1)//2)%2; om=lambda x:((x*x-1)//8)%2
    e=eps(u)*eps(w)+al*om(w)+be*om(u)
    return -1 if e%2 else 1
def hasse(form,p):
    h=1
    for i in range(len(form)):
        for j in range(i+1,len(form)): h*=hil(form[i],form[j],p)
    return h
def disc_sqclass(form):
    r=F(1)
    for a in form: r*=a
    return r
std=[1,-1,-1,-1,-1]
for d in (F(2),F(3),F(7,9),F(5),F(1,2)):
    q=[1,-1,-1,-1,-d]; c=d  # forced c = d mod squares by the discriminant
    cq=[c*a for a in q]
    same=all(hasse(cq,p)==hasse(std,p) for p in (2,3,5,7))
    print("d",d,"similar (local invariants at 2,3,5,7, signature ok):",same, "  -1,d Hilbert at 2,3,7:",[hil(-1,d,p) for p in (2,3,7)])
# sphere: <1,1,1> represents 7/9 iff <1,1,1,-7> isotropic: 2-adic test via Hasse/disc of the 3-dim complement
print("7 sum of three squares? brute over denominators<=12:",any((F(a,D)**2+F(b,D)**2+F(c,D)**2)==7 for D in range(1,13) for a in range(0,3*D) for b in range(0,3*D) for c in range(0,3*D)))
