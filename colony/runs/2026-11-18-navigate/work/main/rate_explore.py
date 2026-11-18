import sys
sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
from GA import mul, add, sub, scal, sc, gen, dot
S=GA.sig(1,3)
e=[gen(i) for i in range(4)]
rec=[e[0]]+[GA.neg(x) for x in e[1:]]   # reciprocal frame
def vec(c): 
    out={}
    for i,x in enumerate(c):
        if x: out[(i,)]=F(x)
    return out
def d(a,b): return dot(a,b,S)
def s0(x): return x.get((),F(0))
def contract(T1,T2): return sum(d(T1(e[m]),T2(rec[m])) for m in range(4))
def tr(T): return sum(d(rec[m],T(e[m])) for m in range(4))
def bracket(T1,T2): return contract(T1,T2)-F(1,2)*tr(T1)*tr(T2)
def Tscalar(p,q,xi=F(0)):
    k=add(p,q); k2=d(k,k)
    def T(a):
        return add(scal(-d(a,q),p),scal(-d(a,p),q),scal(d(p,q),a),scal(2*xi*d(a,k),k),scal(-2*xi*k2,a))
    return T
def wedge(a,b): return scal(F(1,2),sub(mul(a,b,S),mul(b,a,S)))
def Tvec(F1,F2):
    def T(a):
        x=add(mul(mul(F1,a,S),F2,S),mul(mul(F2,a,S),F1,S))
        return {b:-c/2 for b,c in x.items() if len(b)==1}
    return T
def kin(c,s_):
    p1=vec([1,0,0,1]); p2=vec([1,0,0,-1]); p3=vec([1,s_,0,c]); p4=vec([1,-s_,0,-c])
    return p1,p2,p3,p4
for (c,s_) in [(F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(-7,25),F(24,25))]:
    p1,p2,p3,p4=kin(c,s_)
    s=d(add(p1,p2),add(p1,p2)); t=d(sub(p1,p3),sub(p1,p3)); u=d(sub(p1,p4),sub(p1,p4))
    assert s+t+u==0
    B=bracket(Tscalar(p1,p2),Tscalar(p3,p4))
    print('scalar-scalar',B, -t*u, B==-t*u or B==t*u)
    xi1,xi2=F(1,7),F(2,5)
    Bx=bracket(Tscalar(p1,p2,xi1),Tscalar(p3,p4,xi2))
    # predicted: J=2 part (s^2/4)(c^2-1/3) and J=0 part -(s^2/6)(1-6xi1)(1-6xi2), up to overall sign
    pred=(s*s/4)*(c*c-F(1,3)) - (s*s/6)*(1-6*xi1)*(1-6*xi2)
    print('  xi',Bx,pred, Bx==pred or Bx==-pred)
    # vectors, linear polarisations
    tot=0
    for a1 in (e[1],e[2]):
        for a2 in (e[1],e[2]):
            F1=wedge(p1,a1); F2=wedge(p2,a2)
            Bv=bracket(Tvec(F1,F2),Tscalar(p3,p4))
            tot+=Bv*Bv
    print('vector-scalar sum',tot, 2*t*t*u*u, tot==2*t*t*u*u)
    # vector trace-free
    print('  trace',tr(Tvec(wedge(p1,e[1]),wedge(p2,e[2]))), tr(Tvec(wedge(p1,e[1]),wedge(p2,e[1]))))
    # fermion: M=1/2 vbar wslash u, w=R2(d), R2=T2-1/2 id tr T2 ; sum = 1/2 <p2 w p1 w>_0
    T2=Tscalar(p3,p4); trT2=tr(T2)
    dd=sub(p1,p2)
    w=sub(T2(dd),scal(F(1,2)*trT2,dd))
    val=F(1,2)*s0(mul(mul(mul(p2,w,S),p1,S),w,S))
    print('weyl-scalar',val,(t-u)**2*t*u/4, val==(t-u)**2*t*u/4)
