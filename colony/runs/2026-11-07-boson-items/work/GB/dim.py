import sys, itertools, time; sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
mul,add,sub,neg,scal,sc,gen,eq=GA.mul,GA.add,GA.sub,GA.neg,GA.scal,GA.sc,GA.gen,GA.eq
def dag(x,sq):
    out={}
    for b,c in x.items():
        g=len(b); s=(-1)**(g*(g-1)//2)*(-1)**sum(1 for i in b if sq[i]==-1)
        out[b]=c*s
    return {b:c for b,c in out.items() if c!=0}
def comm(x,y,sq): return sub(mul(x,y,sq),mul(y,x,sq))
class Modes:
    def __init__(self, labels):
        self.labels=list(labels); self.idx={l:i for i,l in enumerate(self.labels)}
        self.sq=tuple([1,-1]*len(self.labels))
    def cr(self,l): i=self.idx[l]; return scal(F(1,2),add(gen(2*i),gen(2*i+1)))
    def an(self,l): i=self.idx[l]; return scal(F(1,2),sub(gen(2*i),gen(2*i+1)))
    def n(self,l): return mul(self.cr(l),self.an(l),self.sq)
    def bil(self,l1,l2): return mul(self.cr(l1),self.an(l2),self.sq)
    def proj(self,filled):
        r=sc(1)
        for l in self.labels:
            nl=self.n(l); r=mul(r, nl if l in filled else sub(sc(1),nl), self.sq)
        return r
    def omega(self,rho,X): return GA_scalar(mul(rho,X,self.sq))*2**len(self.labels)
def GA_scalar(x): return x.get((),F(0))
def vadd(a,b): return tuple(x+y for x,y in zip(a,b))
def vsub(a,b): return tuple(x-y for x,y in zip(a,b))
# ---- d=2 window identity
t0=time.time()
W=[(x,y) for x in range(3) for y in range(2)]
Wset=set(W); m=Modes(W); sq=m.sq
def rho(q):
    r={}
    for k in W:
        if vadd(k,q) in Wset: r=add(r,m.bil(k,vadd(k,q)))
    return r
qs=[(1,0),(0,1),(1,1),(2,0),(2,1),(1,-1),(-1,1)]
ok=True
for q in qs:
    R=rho(q); Rd=dag(R,sq)
    lhs=comm(R,Rd,sq)
    rhs={}
    for k in W:
        if vadd(k,q) in Wset: rhs=add(rhs,m.n(k))
        if vsub(k,q) in Wset: rhs=sub(rhs,m.n(k))
    ok&=eq(lhs,rhs)
    for q2 in qs:
        if q2==q: continue
        R2d=dag(rho(q2),sq); lhs2=comm(R,R2d,sq); d=vsub(q,q2); r2={}
        for k in W:
            kd=vadd(k,d)
            inA = vadd(k,q) in Wset and vadd(kd,q2) in Wset and kd in Wset   # k in W, k+q in W, k+q-q' in W
            inB = vsub(k,q2) in Wset and vsub(kd,q) in Wset and kd in Wset   # k in W, k-q' in W, k+q-q'-q = k-q' ... 
            if inA and kd in Wset: r2=add(r2,m.bil(k,kd))
            if inB and kd in Wset: r2=sub(r2,m.bil(k,kd))
        ok&=eq(lhs2,r2)
print("2D window strip identity and cross formula:",ok, round(time.time()-t0,2),"s")
# ---- 1D generator window with two labels (a = 1, 2)
from math import comb, factorial
for N in (2,3):
    t0=time.time()
    I=list(range(-N,N)); L=[(k,a) for a in (1,2) for k in I]; m=Modes(L); sq=m.sq
    def rq(q,a,b):
        r={}
        for k in I:
            if k+q in I: r=add(r,m.bil((k,a),(k+q,b)))
        return r
    sea=[(k,a) for (k,a) in L if k<0]
    rho_s=m.proj(sea)
    Q1=add(*[m.n((k,1)) for k in I]); Q2=add(*[m.n((k,2)) for k in I])
    res=[]
    for q in range(1,N+1):
        for (a,b) in [(1,1),(2,2),(1,2),(2,1)]:
            R=rq(q,a,b); lhs=comm(R,dag(R,sq),sq)
            rhs={}
            for k in I:
                if k+q in I: rhs=add(rhs,m.n((k,a)))
                if k-q in I: rhs=sub(rhs,m.n((k,b)))
            res.append(eq(lhs,rhs))
        # value on sea and on charge-imbalanced edge-clean states
        R12=rq(q,1,2); c12=comm(R12,dag(R12,sq),sq)
        v=m.omega(rho_s,c12)
        # state with one extra label-1 particle at 0 and one fewer label-2 particle at -1 (edge-clean if N>q)
        st=[x for x in sea if x!=(-1,2)]+[(0,1)]
        v2=m.omega(m.proj(st),c12)
        R11=rq(q,1,1); c11=comm(R11,dag(R11,sq),sq); v3=m.omega(m.proj(st),c11)
        print(f"N={N} q={q}: sea value of [rho12,rho12*] = {v}; on Q1-Q2=+2 state: {v2}; Cartan on same state: {v3}")
    # hard-core: C_q = rho_q(E12)^* = sum a*_{k+q,2} a_{k,1}
    for q in range(1,N+1):
        C=dag(rq(q,1,2),sq); x=rho_s; norms=[]
        for p in range(1,q+2):
            x=mul(C,x,sq)
            nrm=GA_scalar(mul(dag(x,sq),x,sq))*2**len(L)
            norms.append(nrm)
        pred=[ (factorial(p)**2)*comb(q,p) for p in range(1,q+2)]
        # Cartan density creation for comparison (window-limited)
        D=dag(rq(q,1,1),sq); y=rho_s; dn=[]
        for p in range(1,3):
            y=mul(D,y,sq); dn.append(GA_scalar(mul(dag(y,sq),y,sq))*2**len(L))
        print(f"  N={N} q={q}: |C^p Omega|^2 p=1..{q+1}: {norms} predicted (p!)^2 C(q,p): {pred}; Cartan |D^p Omega|^2 p=1,2: {dn} (boson: q^p p! = {[q, 2*q*q]})")
    print("  identities", all(res), round(time.time()-t0,2),"s")
