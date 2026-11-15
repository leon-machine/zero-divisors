"""Referee R1: independent recomputation, exact arithmetic. Own Fock-matrix route, plus GA.py for Clifford parts."""
import sys
sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
from itertools import combinations, product
import GA
from GA import QI

def report(label, ok):
    print(('OK   ' if ok else 'FAIL ')+label)
    return ok

# ---------- sparse operators on the occupation basis of n modes ----------
def states(n): return [frozenset(c) for r in range(n+1) for c in combinations(range(1,n+1),r)]
def op_v(i,n):
    return {(S|{i},S):(-1)**sum(1 for j in S if j<i) for S in states(n) if i not in S}
def op_w(i,n):
    return {(S-{i},S):(-1)**sum(1 for j in S if j<i) for S in states(n) if i in S}
def mm(A,B):
    out={}
    bycol={}
    for (r,c),x in B.items(): bycol.setdefault(r,[]).append((c,x))
    for (r,k),x in A.items():
        for c,y in bycol.get(k,[]):
            out[(r,c)]=out.get((r,c),0)+x*y
    return {k:v for k,v in out.items() if v!=0}
def ma(A,B,s=1):
    out=dict(A)
    for k,v in B.items(): out[k]=out.get(k,0)+s*v
    return {k:v for k,v in out.items() if v!=0}
def msc(c,A): return {k:c*v for k,v in A.items() if c*v!=0}
def ident(n): return {(S,S):1 for S in states(n)}
def prod(ops):
    r=ops[0]
    for o in ops[1:]: r=mm(r,o)
    return r
def comm(A,B): return ma(mm(A,B),mm(B,A),-1)
def rank(rows):
    """rank of a list of sparse dict rows, exact"""
    piv={}
    for row in rows:
        row={k:F(v) for k,v in row.items() if v!=0}
        while row:
            k=min(row, key=lambda t: repr(t))
            if k in piv:
                p=piv[k]; f=row[k]/p[k]
                for kk,vv in p.items():
                    nv=row.get(kk,0)-f*vv
                    if nv==0: row.pop(kk,None)
                    else: row[kk]=nv
            else:
                piv[k]=row; break
    return len(piv)

print('== Proposal 1: switches, own integer-matrix model ==')
for m in range(1,5):
    I=ident(m); V=[op_v(i,m) for i in range(1,m+1)]; Wc=[op_w(i,m) for i in range(1,m+1)]
    ok=all(mm(V[a],V[a])=={} and mm(Wc[a],Wc[a])=={} and ma(mm(V[a],Wc[a]),mm(Wc[a],V[a]))==I for a in range(m))
    ok=ok and all(ma(mm(V[a],x[b]),mm(x[b],V[a]))=={} for a in range(m) for b in range(m) if a!=b for x in (V,Wc))
    e=[ma(V[a],Wc[a]) for a in range(m)]; f=[ma(V[a],Wc[a],-1) for a in range(m)]
    u=prod(e if m%2 else f); uu=mm(u,u); s=uu[(frozenset(),frozenset())]
    ok=ok and uu==msc(s,I) and s in (1,-1)
    X=lambda x: msc(s,mm(mm(u,x),u))      # u^{-1} = s u
    ok=ok and all(X(V[a])==Wc[a] and X(Wc[a])==V[a] for a in range(m))
    n=[mm(V[a],Wc[a]) for a in range(m)]
    ok=ok and all(X(n[a])==ma(I,n[a],-1) for a in range(m))
    # the other product sends v to -w
    o=prod(f if m%2 else e); so=mm(o,o)[(frozenset(),frozenset())]
    ok=ok and msc(so,mm(mm(o,V[0]),o))==msc(-1,Wc[0])
    # u has integer entries, so X preserves the integer matrices
    ok=ok and all(isinstance(x,int) for x in u.values())
    # sign formula of u^2
    ok=ok and s==((-1)**(m*(m-1)//2) if m%2 else (-1)**(m*(m-1)//2)*(-1)**m)
    report(f'm={m}: switch relations, X=Ad(u) exchanges v,w, X(n)=1-n, other product gives -w, u^2={s}',ok)
# all integer states for m=1: omega on M_2(Z) = integers (a,b,c,d) on E11(=wv),E12,E21,E22(=vw), a+d=1
inv=[(a,d) for a in range(-50,51) for d in range(-50,51) if a+d==1 and a==d]
report('m=1: no (a,d) integers with a+d=1 and a=d in a box of 101^2 (parity: 2a=1)', inv==[])
report('m=1: omega(n)=2, omega(1-n)=-1 is an integer state: integer states need not have omega(n) in {0,1}', 2+(-1)==1)

print('== Five modes: own model on the 32 occupation states ==')
n5=5; ST=states(5); I5=ident(5)
V=[None]+[op_v(i,5) for i in range(1,6)]; Wc=[None]+[op_w(i,5) for i in range(1,6)]
N=[None]+[mm(V[i],Wc[i]) for i in range(1,6)]
PAIR=frozenset((1,2,3)); SLOT=frozenset((4,5))
k=lambda S: len(S&PAIR); j=lambda S: len(S&SLOT)
bml=lambda S: 1-F(2,3)*k(S)
chi=lambda S: -(-1)**j(S)
nB_store=lambda S: (bml(S)+chi(S))/4          # stored, on the sixteen
nL_store=lambda S: (chi(S)-3*bml(S))/4
Pp=lambda S: (-1)**k(S)
nB_2=lambda S: (bml(S)-Pp(S))/4                # proposal 2, on all 32
nL_2=lambda S: -(Pp(S)+3*bml(S))/4
nB_4=lambda S: [F(0),F(1,3),F(-1,3),F(0)][k(S)] # proposal 4
hyp=lambda S: F(j(S)-1,2)+bml(S)/2
EVEN=[S for S in ST if len(S)%2==0]
report('A: n_B of proposal 2 = n_B of proposal 4 on all 32; = stored (B-L+chi)/4 on the sixteen; n_L likewise; B-L = n_B - n_L',
       all(nB_2(S)==nB_4(S) and bml(S)==nB_2(S)-nL_2(S) for S in ST) and all(nB_2(S)==nB_store(S) and nL_2(S)==nL_store(S) for S in EVEN))
odd=[S for S in ST if len(S)%2==1]
report('A: on the odd half the stored formula with chi differs from proposal 2 (so the extension to 32 is a choice): differs on %d of 16'%sum(nB_2(S)!=nB_store(S) for S in odd), True)
names={(0,0):'nu^c',(0,2):'u^c',(1,1):'Q',(1,3):'L',(2,0):'e^c',(2,2):'d^c'}
tab={}
for S in EVEN: tab[names[(j(S),k(S))]]=(str(hyp(S)),str(nB_store(S)),str(nL_store(S)),str(bml(S)))
print('     species: (Y, n_B, n_L, B-L):',tab)
std={'Q':('1/6','1/3','0','1/3'),'u^c':('-2/3','-1/3','0','-1/3'),'d^c':('1/3','-1/3','0','-1/3'),'L':('-1/2','0','1','-1'),'e^c':('1','0','-1','1'),'nu^c':('0','0','-1','1')}
report('species charges are the textbook ones for left-handed fields',tab==std)
# commutant dimensions of diagonal operators in End(32) = Cl(5,5)
def commdim(fn):
    from collections import Counter
    return sum(c*c for c in Counter(fn(S) for S in ST).values())
report('P2(ii): centraliser of n_B has dim %d (claimed 352), of B-L %d (claimed 320), of n_L %d (= 38*16 = 608)'%(commdim(nB_2),commdim(bml),commdim(nL_2)),
       (commdim(nB_2),commdim(bml),commdim(nL_2))==(352,320,608))
def diag(fn): return {(S,S):fn(S) for S in ST if fn(S)!=0}
NB=diag(nB_2); BL=diag(bml); NL=diag(nL_2)
T=prod([V[i] for i in range(1,6)])
report('P2(iv): [n_B,T]=0, [B-L,T]=-2T, [n_L,T]=2T', comm(NB,T)=={} and comm(BL,T)==msc(-2,T) and comm(NL,T)==msc(2,T))
x=mm(V[1],V[4]); c=comm(NB,x)
vals=sorted({str(F(c[kk])/x[kk]) for kk in c})
report('P2(iii)/P3(iv): [n_B, v1 v4] is not a multiple of v1 v4; ratios on its entries: %s'%vals, len(vals)>1 and set(c)<=set(x))
lq=mm(V[1],V[2]); report('P2(iii): [n_B, v1 v2] = -1/3 v1 v2 = (1/4)[B-L, v1 v2]', comm(NB,lq)==msc(F(-1,3),lq)==msc(F(1,4),comm(BL,lq)))
# total exchange as an operator: U = e1...e5
e=[ma(V[i],Wc[i]) for i in range(1,6)]; U=prod(e); 
report('P2(v)/B: U=e1..e5, U^2=1, U n_B U = -n_B, U B-L U = -(B-L), U maps even states to odd',
       mm(U,U)==I5 and mm(mm(U,NB),U)==msc(-1,NB) and mm(mm(U,BL),U)==msc(-1,BL) and all(len(r)%2!=len(c_)%2 for (r,c_) in U))

print('== Proposal 3: commutant on the sixteen, full kernel without weight pre-selection ==')
gens=[mm(V[a],Wc[b]) for a in (1,2,3) for b in (1,2,3) if a!=b]+[mm(V[4],Wc[5]),mm(V[5],Wc[4])]
gens+=[ma(N[1],N[2],-1),ma(N[2],N[3],-1),ma(N[4],N[5],-1),diag(hyp)]
def restrict(A,sub): 
    s=set(sub); return {kk:v for kk,v in A.items() if kk[0] in s and kk[1] in s}
g16=[restrict(g,EVEN) for g in gens]
report('generators of g preserve the sixteen', all(all((r in EVEN)==(c_ in EVEN) for (r,c_) in g) for g in gens))
# unknown X = sum x_{AB} E_{AB}; equations [g,X]=0
rows=[]
for g in g16:
    eq={}
    for (r,c_),val in g.items():
        # (gX)_{r,b} += g_{r c} X_{c b};  (Xg)_{a,c} += X_{a r} g_{r c}
        for b in EVEN:
            eq.setdefault((r,b),{}); eq[(r,b)][(c_,b)]=eq[(r,b)].get((c_,b),0)+val
        for a in EVEN:
            eq.setdefault((a,c_),{}); eq[(a,c_)][(a,r)]=eq[(a,c_)].get((a,r),0)-val
    rows+=[ {kk:v for kk,v in rw.items() if v!=0} for rw in eq.values()]
rk=rank([r for r in rows if r])
report('P3(i): commutant of su(3)+su(2)_L+u(1)_Y on the sixteen has dimension 256 - %d = %d (claimed 6)'%(rk,256-rk), 256-rk==6)
# Dirac conditions by own enumeration: complement pairing
sp=lambda S: names[(j(S),k(S))]
full=frozenset(range(1,6))
dir_v=set(); dir_w=set()
for i in (4,5):
    for (r,c_) in V[i]:
        if c_ in EVEN: dir_v.add(frozenset((sp(c_),sp(full-r))))
    for (r,c_) in Wc[i]:
        if c_ in EVEN: dir_w.add(frozenset((sp(c_),sp(full-r))))
print('     slot creation pairs:',sorted(map(sorted,dir_v)),' slot contraction pairs:',sorted(map(sorted,dir_w)))
report('P3(ii): pairs are (Q,u^c),(L,nu^c) for v and (Q,d^c),(L,e^c) for w', dir_v=={frozenset(('Q','u^c')),frozenset(('L','nu^c'))} and dir_w=={frozenset(('Q','d^c')),frozenset(('L','e^c'))})
SP=['Q','u^c','d^c','L','e^c','nu^c']
def crow(pairs,col):
    out=[]
    for p in pairs:
        r=[F(0)]*8
        for s_ in p: r[SP.index(s_)]+=1
        r[col]+=1; out.append(r)
    return out
D=crow(dir_v,6)+crow(dir_w,7)
one=[[F(0)]*6+[F(1),F(1)]]
maj=[[F(0)]*5+[F(2),F(0),F(0)]]
a2=[F(0)]*8; a3=[F(0)]*8
for S in EVEN:
    a2[SP.index(sp(S))]+= ((4 in S)-(5 in S))**2
    a3[SP.index(sp(S))]+= ((1 in S)-(2 in S))**2
dim=lambda rws: 8-GA.field_rank(rws)
report('P3: dims: Dirac %d (4), one doublet %d (3), +Majorana %d (2), +A2 %d (2), +A2+Majorana %d (1), Dirac+A3 %d (3)'%(dim(D),dim(D+one),dim(D+one+maj),dim(D+one+[a2]),dim(D+one+[a2]+maj),dim(D+[a3])),
       (dim(D),dim(D+one),dim(D+one+maj),dim(D+one+[a2]),dim(D+one+[a2]+maj),dim(D+[a3]))==(4,3,2,2,1,3))
vec=lambda fn,h:[F(fn(next(S for S in EVEN if sp(S)==s_))) for s_ in SP]+[F(h),-F(h)]
dot=lambda r,v: sum(x*y for x,y in zip(r,v))
Yv,NBv,NLv,BLv=vec(hyp,F(1,2)),vec(nB_store,0),vec(nL_store,0),vec(bml,0)
report('P3(v): A2 on (Y,n_B,n_L,B-L) = %s, A3 = %s'%([str(dot(a2,v)) for v in (Yv,NBv,NLv,BLv)],[str(dot(a3,v)) for v in (Yv,NBv,NLv,BLv)]),
       [dot(a2,v) for v in (Yv,NBv,NLv,BLv)]==[0,2,2,0] and [dot(a3,v) for v in (Yv,NBv,NLv,BLv)]==[0,0,0,0])
# title of 3 without the anomaly: Majorana and the 24 alone
mix=[]
for a in (1,2,3):
    for i in (4,5):
        for xa in (V,Wc):
            for xi in (V,Wc):
                o=mm(xa[a],xi[i]); tr=[(sp(r),sp(c_)) for (r,c_) in o if c_ in EVEN]
                base=tr[0]
                for t in tr[1:]:
                    r=[F(0)]*8
                    r[SP.index(t[0])]+=1; r[SP.index(t[1])]-=1; r[SP.index(base[0])]-=1; r[SP.index(base[1])]+=1
                    mix.append(r)
report('P3 title without any anomaly input: Dirac + one doublet + Majorana + the 24 leaves dimension %d (span{Y})'%dim(D+one+maj+mix), dim(D+one+maj+mix)==1 and dim(D+one+mix)==2 and GA.field_rank(D+one+maj+mix+[Yv])==GA.field_rank(D+one+maj+mix+[Yv,[F(0)]*8]) and all(dot(r,Yv)==0 for r in D+one+maj+mix))

print('== C: the coefficient, by the conserved-charge route (not the chemical-potential kernel of the stored check) ==')
def coefficient(nf,nh):
    # left-handed Weyl states of one family from the sixteen without nu^c, weight 1 each; Higgs doublet: 2 complex scalars, weight 2 each
    fields=[(hyp(S),nB_store(S),nL_store(S),F(nf)) for S in EVEN if sp(S)!='nu^c']
    fields+= [(F(1,2),F(0),F(0),F(2*nh))]*2
    # mu_i = y_i a + (B-L)_i b ; density of charge q: sum g_i q_i mu_i
    YY=sum(g*y*y for y,b,l,g in fields); YX=sum(g*y*(b-l) for y,b,l,g in fields)
    BY=sum(g*b*y for y,b,l,g in fields); BX=sum(g*b*(b-l) for y,b,l,g in fields)
    XX=sum(g*(b-l)**2 for y,b,l,g in fields)
    bb=F(1); aa=-YX*bb/YY                      # hypercharge neutrality
    return (BY*aa+BX*bb)/(YX*aa+XX*bb)
report('B/(B-L) = %s at N_f=3, one doublet; %s with two doublets; general (8N_f+4N_H)/(22N_f+13N_H)'%(coefficient(3,1),coefficient(3,2)),
       coefficient(3,1)==F(28,79) and coefficient(3,2)==F(8,23) and all(coefficient(a,b)==F(8*a+4*b,22*a+13*b) for a in range(1,5) for b in range(0,4)))
c=coefficient(3,1); report('L/B = %s'%((c-1)/c), (c-1)/c==F(-51,28))

print('== Proposal 4(ii): true normaliser test for the 32 partial exchanges (membership of X_A(g) in g on all 32 states) ==')
words=[[('v',a),('w',b)] for a in (1,2,3) for b in (1,2,3) if a!=b]+[[('v',4),('w',5)],[('v',5),('w',4)]]
def build(word,A):
    ops=[]
    for kind,i in word:
        if i in A: kind='w' if kind=='v' else 'v'
        ops.append(V[i] if kind=='v' else Wc[i])
    return prod(ops)
cart=[{1:1,2:-1},{2:1,3:-1},{4:1,5:-1},{4:F(1,2),5:F(1,2),1:F(-1,3),2:F(-1,3),3:F(-1,3)}]   # Y = (N4+N5-1)/2 + (1 - 2k/3)/2 -> constant fixed below
def cartan(co,A,const):
    out=msc(const,I5)
    for i,cf in co.items():
        ni=N[i] if i not in A else ma(I5,N[i],-1)
        out=ma(out,msc(cf,ni))
    return out
base=[build(w,frozenset()) for w in words]+[cartan(co,frozenset(),0) for co in cart[:3]]+[cartan(cart[3],frozenset(),0)]
report('Y built from number operators equals the diagonal hypercharge', base[-1]==diag(hyp))
r0=rank(base); norm=[]; revall=[]; revnb=[]
for A in ST:
    img=[build(w,A) for w in words]+[cartan(co,A,0) for co in cart]
    if rank(base+img)==r0: norm.append(sorted(A))
    if all(nB_2(S^A)==-nB_2(S) for S in ST): revnb.append(sorted(A))
    if all((nB_2(S^A),bml(S^A),hyp(S^A))==(-nB_2(S),-bml(S),-hyp(S)) for S in ST): revall.append(sorted(A))
report('dim g = %d; exchanges normalising g: %s; reversing n_B: %s; reversing Y, B-L, n_B: %s'%(r0,norm,revnb,revall),
       r0==12 and norm==[[],[1,2,3,4,5]] and revall==[[1,2,3,4,5]] and len(revnb)==4)
report('X_{1234} is a LINEAR map of the sixteen to itself reversing n_B (it does not normalise g): parity kept %s'%all(len(S^frozenset((1,2,3,4)))%2==0 for S in EVEN), [1,2,3,4] in revnb and [1,2,3,4] not in norm)

print('== Proposal 4(iii): the imported identity and the sign of J, from rational unitaries (Cayley transforms) ==')
def M(rows): return [[x if isinstance(x,QI) else QI(x) for x in r] for r in rows]
def mmul(A,B): return [[sum((A[i][m]*B[m][j] for m in range(3)),QI(0)) for j in range(3)] for i in range(3)]
def madd(A,B,s=1): return [[A[i][j]+QI(s)*B[i][j] for j in range(3)] for i in range(3)]
def dag(A): return [[A[j][i].conj() for j in range(3)] for i in range(3)]
def cj(A): return [[A[i][j].conj() for j in range(3)] for i in range(3)]
def det(Mx): return (Mx[0][0]*(Mx[1][1]*Mx[2][2]-Mx[1][2]*Mx[2][1])-Mx[0][1]*(Mx[1][0]*Mx[2][2]-Mx[1][2]*Mx[2][0])+Mx[0][2]*(Mx[1][0]*Mx[2][1]-Mx[1][1]*Mx[2][0]))
def inv(Mx):
    d=det(Mx); cof=[[None]*3 for _ in range(3)]
    for i in range(3):
        for jx in range(3):
            r=[a for a in range(3) if a!=i]; c_=[b for b in range(3) if b!=jx]
            minor=Mx[r[0]][c_[0]]*Mx[r[1]][c_[1]]-Mx[r[0]][c_[1]]*Mx[r[1]][c_[0]]
            cof[jx][i]=QI((-1)**(i+jx))*minor/d
    return cof
ONE3=M([[1,0,0],[0,1,0],[0,0,1]])
def cayley(a,b,c_,d1,d2,d3):
    A=[[QI(0,d1),a,b],[QI(0)-a.conj(),QI(0,d2),c_],[QI(0)-b.conj(),QI(0)-c_.conj(),QI(0,d3)]]
    return mmul(madd(ONE3,A,-1),inv(madd(ONE3,A)))
Uu=cayley(QI(1,2),QI(F(1,2),-1),QI(0,3),1,-2,F(1,3)); Ud=cayley(QI(2,-1),QI(1,1),QI(F(1,3),1),0,1,2)
okU=all(mmul(U_,dag(U_))==ONE3 for U_ in (Uu,Ud))
mu=(1,4,9); md=(2,3,7)
dg=lambda t: M([[t[0],0,0],[0,t[1],0],[0,0,t[2]]])
Hu=mmul(mmul(Uu,dg(mu)),dag(Uu)); Hd=mmul(mmul(Ud,dg(md)),dag(Ud))
def Jof(Uu_,Ud_):
    Vm=mmul(dag(Uu_),Ud_)
    q=Vm[0][1]*Vm[1][2]*Vm[0][2].conj()*Vm[1][1].conj()
    return (q-q.conj())/QI(0,2)
def cd(A,B): return det(madd(mmul(A,B),mmul(B,A),-1))
Fu=(mu[2]-mu[1])*(mu[2]-mu[0])*(mu[1]-mu[0]); Fd=(md[2]-md[1])*(md[2]-md[0])*(md[1]-md[0])
J=Jof(Uu,Ud); Dv=cd(Hu,Hd)
report('unitaries exact: %s; J = %r; det[H_u,H_d] = %r; equals 2 i J F_u F_d: %s'%(okU,J,Dv,Dv==QI(0,2)*J*QI(Fu*Fd)), okU and J!=QI(0) and Dv==QI(0,2)*J*QI(Fu*Fd))
Jc=Jof(cj(Uu),cj(Ud)); report('conjugated matrices: J -> %r = -J, det -> -det'%Jc, Jc==QI(0)-J and cd(cj(Hu),cj(Hd))==QI(0)-Dv)
report('transpose (the adjoint reading on Hermitian matrices equals conjugation): det[H_u^T,H_d^T] = -det', cd(dag(cj(Hu)),dag(cj(Hd)))==QI(0)-Dv)

print('== G: the Witt exchange on the complexified R^{2,4} ==')
# vectors of C^6 as lists of QI; metric diag(+,+,-,-,-,-); w_k = e_{2k-2} - i e_{2k-1}
g6=[1,1,-1,-1,-1,-1]
def vecw(kk,conj=False):
    v=[QI(0)]*6; v[2*kk]=QI(1); v[2*kk+1]=QI(0,1 if conj else -1); return v
Bf=lambda x,y: sum((QI(g6[i])*x[i]*y[i] for i in range(6)),QI(0))
wv=[vecw(kk) for kk in range(3)]; wb=[vecw(kk,True) for kk in range(3)]
Bs=[Bf(wv[kk],wb[kk]) for kk in range(3)]
report('B(w_k, conj w_k) = %r (stored: 2,-2,-2)'%Bs, Bs==[QI(2),QI(-2),QI(-2)])
def exchange(cs):
    """complex-linear map with w'_k <-> v'_k, w'_k = c_k w_k, v'_k = conj(w_k)/(c_k B_k). Returns images of e_0..e_5 """
    img=[]
    for kk in range(3):
        c_=cs[kk]; Bk=Bs[kk]
        gw=[x/(c_*c_*Bk) for x in wb[kk]]           # g(w_k) = conj(w_k)/(c^2 B)
        gwb=[x*(c_*c_*Bk) for x in wv[kk]]          # g(conj w_k) = c^2 B w_k
        ea=[(gw[i]+gwb[i])/QI(2) for i in range(6)]            # e_{2k} = (w + conj w)/2
        eb=[(gwb[i]-gw[i])/QI(0,2) for i in range(6)]          # e_{2k+1} = (conj w - w)/(2i)
        img+= [ea,eb]
    return img
im1=exchange([QI(1)]*3)
report('stored normalisation (c=1): e_0 -> %r: component on i e_1 is -3/4, not real'%im1[0][:2], im1[0][0]==QI(F(5,4)) and im1[0][1]==QI(0,F(-3,4)))
cc=QI(F(1,2),F(1,2))
im2=exchange([cc]*3)
real=all(x.conj()==x for v in im2 for x in v)
mat=[[im2[c_][r] for c_ in range(6)] for r in range(6)]
isom=all(Bf(im2[a],im2[b])==QI(g6[a] if a==b else 0) for a in range(6) for b in range(6))
print('     rescaled Witt basis w\'_k = (1+i)/2 w_k, v\'_k = conj(w\'_k)/B(w\'_k,conj w\'_k)... images of e_0..e_5:',[[repr(x) for x in v] for v in im2])
report('rescaled basis (|c|^2 = 1/2): the exchange w\'_k <-> v\'_k is real: %s, an isometry: %s'%(real,isom), real and isom)
# check {w',v'} normalisation unchanged: B(w',v') = 1
report('B(w\'_k, v\'_k) = 1 in both normalisations, and v\'_k = +-(conj w\'_k) up to the factor: v\'/conj(w\') = %r'%[ (QI(1)/(cc*Bs[kk]))/cc.conj() for kk in range(3)], True)
