# Referee R3 independent recomputation: full (non-orbit) cell complex, own data structures.
import itertools, random, sys
from collections import defaultdict

def make(m, top):
    # cells (k,a); integer boundary
    def bd(c):
        k,a=c
        if k==0: return {}
        if k%2: 
            return {(k-1,(a+1)%m):1,(k-1,a):-1}
        return {(k-1,(a+c_)%m):1 for c_ in range(m)}
    cells=[(k,a) for k in range(top+1) for a in range(m)]
    return cells,bd

def addto(d,k,v):
    d[k]=d.get(k,0)+v
    if d[k]==0: del d[k]

def D0(k,m):   # integral-free; we only need mod 2, but keep as multiset dict
    out={}
    for p in range(k+1):
        q=k-p
        if p%2==0: T=[(0,0)]
        elif q%2==0: T=[(0,1)]
        else: T=[(r,j) for r in range(m) for j in range(r+1,m)]
        for r,j in T: addto(out,((p,r),(q,j)),1)
    return out

def D1(k,m):
    N=range(m); Np=range(1,m)
    t={0:[],1:[((1,0),(1,0))],2:[((1,a),(2,0)) for a in N],
       3:[((3,0),(1,0))]+[((1,a),(3,0)) for a in Np],
       4:[((3,a),(2,0)) for a in N],
       5:[((1,0),(5,0)),((5,0),(1,0))]+[((3,a),(3,0)) for a in Np]}
    return {x:1 for x in t[k]}

def closure(c,m):
    k,a=c
    s={c}
    low=k
    if k%2: s|={(k-1,a),(k-1,(a+1)%m)}; low=k-1
    for j in range(low):
        for b in range(m): s.add((j,b))
    return s

class Prod:
    def __init__(s,m,top=5,act=1,ftop=3):
        s.m=m; s.top=top; s.act=act; s.ftop=ftop
        s.C,s.bC=make(m,top); s.D,s.bD=make(2,ftop)
        s.cells=[(c,d) for c in s.C for d in s.D]
    def dim(s,x): return x[0][0]+x[1][0]
    def g(s,x,n=1):
        (k,a),(q,b)=x
        return ((k,(a+n)%s.m),(q,(b+n*s.act)%2))
    def bd(s,x):
        c,d=x; out={}
        for cc,v in s.bC(c).items(): addto(out,(cc,d),v)
        for dd,v in s.bD(d).items(): addto(out,(c,dd),v*(-1)**c[0])
        return out
    def bd2(s,x): return [y for y,v in s.bd(x).items() if v%2]
    def rep(s,x):
        (k,a),(q,b)=x
        return s.g(x,-a)
    def reps(s,n): return [x for x in s.cells if s.dim(x)==n and x[0][1]==0]
    # diagonals on a rep cell (a=0, b arbitrary): act by fibre T^b separately (T commutes, D-maps are T-equivariant)
    def _inter(s,TC,TD,b):
        out=set()
        for (c1,c2) in TC:
            for (d1,d2) in TD:
                e=((c1,(d1[0],(d1[1]+b)%2)),(c2,(d2[0],(d2[1]+b)%2)))
                out^={e}
        return out
    def diag(s,x):
        (k,a),(q,b)=x; assert a==0
        return s._inter([p for p,v in D0(k,s.m).items() if v%2],[p for p,v in D0(q,2).items() if v%2],b)
    def high(s,x,formula=0):
        (k,a),(q,b)=x; assert a==0
        sw=lambda T:[(y,x_) for (x_,y) in T]
        d0c=[p for p,v in D0(k,s.m).items() if v%2]; d0d=[p for p,v in D0(q,2).items() if v%2]
        d1c=list(D1(k,s.m)); d1d=list(D1(q,2))
        if formula==0: return s._inter(d1c,sw(d0d),b)^s._inter(d0c,d1d,b)
        return s._inter(d1c,d0d,b)^s._inter(sw(d0c),d1d,b)
    def ext(s,f):
        # extend a map defined on reps to all cells equivariantly: f(g^a x)=g^a f(x) (diagonal on pairs)
        def F(x):
            a=x[0][1]; r=s.g(x,-a)
            return {(s.g(u,a),s.g(v,a)) for (u,v) in f(r)}
        return F
    def bdpairs(s,T):
        out=set()
        for (u,v) in T:
            for z in s.bd2(u): out^={(z,v)}
            for z in s.bd2(v): out^={(u,z)}
        return out
    def clos(s,x):
        return {(c,d) for c in closure(x[0],s.m) for d in closure(x[1],2)}

def span_solve(gens,target):
    piv={}
    for g_ in gens:
        g_=set(g_)
        while g_:
            k=min(g_)
            if k in piv: g_^=piv[k]
            else: piv[k]=g_; break
    t=set(target)
    while t:
        k=min(t)
        if k not in piv: return False
        t^=piv[k]
    return True

def run(m,top=5,act=1,formula=0,verbose=True,thetaval=None):
    P=Prod(m,top,act)
    # factor identity (own code): on C_m up to top, on D up to 3
    for (mm,tp) in ((m,top),(2,3)):
        cells,bd=make(mm,tp)
        def b2(c): return [y for y,v in bd(c).items() if v%2]
        for k in range(tp+1):
            lhs=set()
            for (u,v) in D1(k,mm):
                for z in b2(u): lhs^={(z,v)}
                for z in b2(v): lhs^={(u,z)}
            for (kk,aa) in b2((k,0)):
                for (u,v) in D1(kk,mm): lhs^={((u[0],(u[1]+aa)%mm),(v[0],(v[1]+aa)%mm))}
            d0={p for p,v in D0(k,mm).items() if v%2}
            rhs=d0^{(v,u) for (u,v) in d0}
            assert lhs==rhs,("factor identity fails",mm,k)
    # product identity on all cells
    H=P.ext(lambda x:P.high(x,formula)); Dg=P.ext(P.diag)
    n_orb=0
    for x in P.cells:
        if x[0][1]!=0: continue
        n_orb+=1
        lhs=P.bdpairs(H(x))
        for z in P.bd2(x): lhs^=H(z)
        d=Dg(x); rhs=d^{(v,u) for (u,v) in d}
        assert lhs==rhs,("product identity fails",x)
        cl=P.clos(x)
        assert all(u in cl and v in cl for (u,v) in H(x)|d)
    # equivariance fully: by construction of ext. D0 chain map mod 2 on product:
    for x in P.cells:
        if x[0][1]!=0: continue
        l=P.bdpairs(Dg(x)); r=set()
        for z in P.bd2(x): r^=Dg(z)
        assert l==r
    # theta
    th=defaultdict(int)
    val=-(m//4) if thetaval is None else thetaval
    for x in P.cells:
        (k,a),(q,b)=x
        if (k,q)==(0,3) and (b-a*act)%2==0: th[x]=1
        if (k,q)==(1,2) and (b-a*act)%2==0: th[x]=1
        if (k,q)==(2,1): th[x]=val
    # invariance
    assert all(th[P.g(x)]==th[x] for x in P.cells)
    cocyc=all(sum(v*th[y] for y,v in P.bd(x).items())==0 for x in P.cells if P.dim(x)==4)
    fib=th[((0,0),(3,0))]+th[((0,0),(3,1))]
    a={x for x in P.cells if th[x]%2}
    sq={x for x in P.reps(5) if sum(1 for (u,v) in H(x) if u in a and v in a)%2}
    # invariant coboundaries mod 2 from invariant 4-cochains (orbit indicator functions)
    def cob(rep4):
        orb={P.g(rep4,n) for n in range(m)}
        return {x for x in P.reps(5) if sum(1 for y in P.bd2(x) if y in orb)%2}
    gens=[cob(r) for r in P.reps(4)]
    top_=[x for x in P.reps(5) if x[0][0]==top and x[1][0]==0] if top==5 else []
    pt=set(top_)
    res=dict(cocycle=cocyc,fibre=fib,sq=sorted(sq),sq_cob=span_solve(gens,sq),top_cob=span_solve(gens,pt),diff_cob=span_solve(gens,sq^pt),orbits=n_orb)
    # sq is cocycle
    for x in P.reps(6):
        assert sum(1 for y in P.bd2(x) if P.rep(y) in sq)%2==0
    return res

if __name__=="__main__":
    for m in (4,8,12,16):
        for f in (0,1):
            print(m,f,run(m,formula=f))
    print("trivial act",run(4,act=0,thetaval=0))
