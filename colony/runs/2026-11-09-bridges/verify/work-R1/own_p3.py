import sys, random
sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
SQ=GA.sig(1,3); G=[GA.gen(i) for i in range(4)]; GUP=[GA.scal(SQ[i],G[i]) for i in range(4)]
def mul(*xs):
    o=xs[0]
    for x in xs[1:]: o=GA.mul(o,x,SQ)
    return o
def vec(c): 
    o={}
    for i,x in enumerate(c):
        if x: o=GA.add(o,GA.scal(F(x),G[i]))
    return o
def grade(x,k): return {b:c for b,c in x.items() if len(b)==k and c!=0}
def s0(x): return x.get((),F(0))
random.seed(7)
rv=lambda: vec([F(random.randint(-9,9),random.randint(1,5)) for _ in range(4)])
# (1) trace identity with unnormalised even versors V = v1 v2 v3 v4, V V~ = N
for t in range(40):
    V=mul(rv(),rv(),rv(),rv()); Vt=GA.reverse(V); N=s0(mul(V,Vt)); assert grade(mul(V,Vt),2)=={} and grade(mul(V,Vt),4)=={} and N!=0
    a,b,s=rv(),rv(),rv()
    sp=GA.neg(mul(Vt,s,V))      # N * s'
    bh=mul(V,b,Vt)              # N * b^
    lhs=s0(mul(a,mul(s,V),b,mul(sp,Vt)))      # N^2 * trace
    rhs=-(2*GA.dot(a,s,SQ)*GA.dot(bh,s,SQ)-GA.dot(a,bh,SQ)*GA.dot(s,s,SQ))*N
    assert lhs==rhs, (lhs,rhs)
print("trace identity OK on 40 random versors")
# (2) the space of linear maps on bivectors obeying the protraction identity; Weyl subspace; contraction
BIV=[(i,j) for i in range(4) for j in range(i+1,4)]
def wedge(a,b): return grade(GA.scal(F(1,2),GA.sub(mul(a,b),mul(b,a))),2)
def bvec(B): return [B.get(k,F(0)) for k in BIV]
# unknown map M[k] = sum_l m[k][l] E_l ; 36 unknowns. constraint: grade3( sum_mu GUP[mu] * M(G[mu]^G[n]) ) = 0 for each n
import itertools
def unit(k,l):
    M={kk:{} for kk in BIV}; M[k]={l:F(1)}; return M
def apply(M,B):
    o={}
    for k in BIV:
        c=B.get(k,F(0))
        if c: o=GA.add(o,GA.scal(c,M[k]))
    return o
def contr(M,xi):
    t={}
    for m in range(4): t=GA.add(t,mul(GUP[m],apply(M,wedge(G[m],xi))))
    return t
tri=[(0,1,2),(0,1,3),(0,2,3),(1,2,3)]
rows_prot=[];rows_ric=[]
units=[unit(k,l) for k in BIV for l in BIV]
for n in range(4):
    cs=[contr(U,G[n]) for U in units]
    for T in tri: rows_prot.append([c.get(T,F(0)) for c in cs])
    for i in range(4): rows_ric.append([c.get((i,),F(0)) for c in cs])
r1=GA.mat_rank(rows_prot); r2=GA.mat_rank(rows_prot+rows_ric)
print("protraction-free maps: dim",36-r1,"; and Ricci-free (Weyl type): dim",36-r2)
# (3) vacuum Van Vleck: tidal map K(a) = Riem(a^xi).xi ; tr K^2 for the type-D Weyl example
SIG=mul(G[1],G[0])
W={k:GA.scal(F(-1,2),GA.add(mul(G[k[0]],G[k[1]]),GA.scal(3,mul(SIG,mul(G[k[0]],G[k[1]]),SIG)))) for k in BIV}
def ddot(B,v): return grade(GA.scal(F(1,2),GA.sub(mul(B,v),mul(v,B))),1)
for xi in (vec((0,0,1,0)),vec((1,0,0,0)),vec((0,1,1,0)),vec((2,1,0,3))):
    assert grade(contr(W,xi),1)=={} and grade(contr(W,xi),3)=={}
    Kmat=[[GA.dot(GUP[i],ddot(apply(W,wedge(G[j],xi)),xi),SQ) for j in range(4)] for i in range(4)]
    tr=sum(Kmat[i][i] for i in range(4)); K2=GA.mat_mul(Kmat,Kmat); tr2=sum(K2[i][i] for i in range(4))
    print("xi",bvec({}) and 0 or [str(xi.get((i,),0)) for i in range(4)],"tr K =",tr,"tr K^2 =",tr2," => Delta-1 ~ trK^2/180 =",tr2/180)
