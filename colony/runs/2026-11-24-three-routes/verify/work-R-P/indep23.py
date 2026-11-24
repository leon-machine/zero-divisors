import sys; sys.path.insert(0,'/home/claude/leon-machine/zero-divisors/lib')
from fractions import Fraction as F
from itertools import product, combinations
import GA, random
random.seed(3)
def mk(sq):
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
    return P,dag
ONE=GA.sc(F(1)); s0=lambda x:x.get((),F(0))
lin=lambda *cs: GA.add(*[GA.scal(F(c),x) for c,x in cs])
# ---------------- P3 (i): certificate with non-blade observables, l=3, m=2
sq3=(1,-1,1,-1,1,-1); P,dag=mk(sq3)
e=[GA.gen(2*j) for j in range(3)]; f=[GA.gen(2*j+1) for j in range(3)]
p=[P(f[j],e[j]) for j in range(3)]
gam=P(p[0],p[1])
def atomA(r):  # rank-one projector of party-1 algebra Cl(2,2) on modes 1,2
    v=[lin((F(1,2),e[j]),(F(1,2),f[j])) for j in range(2)]
    w=[lin((F(1,2),e[j]),(F(-1,2),f[j])) for j in range(2)]
    p0=P(w[0],v[0],w[1],v[1]); s=[p0,P(v[0],p0),P(v[1],p0),P(v[0],v[1],p0)]
    y=GA.add(*[GA.scal(F(r[i]),s[i]) for i in range(4)])
    return GA.scal(1/sum(F(x)**2 for x in r),P(y,dag(y)))
E1=atomA((1,2,-1,3)); E2=GA.add(atomA((2,0,1,1)),atomA((0,1,0,0)))  # rank-2 needs orthogonal: check
assert GA.eq(P(E1,E1),E1)
if not GA.eq(P(E2,E2),E2): E2=atomA((2,-1,1,1))
assert GA.eq(P(E2,E2),E2) and GA.eq(dag(E2),E2)
A0=GA.sub(ONE,GA.scal(2,E1)); A1=GA.sub(ONE,GA.scal(2,E2))
assert not GA.commutes(A0,A1,sq3) and not GA.anticommutes(A0,A1,sq3)
X3=P(gam,e[2]); Z3=P(P(gam,f[2]),P(gam,e[2]))
B0=lin((F(3,5),X3),(F(4,5),Z3)); B1=Z3
for x in (A0,A1,B0,B1): assert GA.eq(dag(x),x) and GA.eq(P(x,x),ONE)
assert all(GA.commutes(a,b,sq3) for a in (A0,A1) for b in (B0,B1))
S=GA.add(A0,A1); D=GA.sub(A0,A1)
C=GA.add(P(A0,B0),P(A0,B1),P(A1,B0),GA.neg(P(A1,B1)))
Fp=GA.scal(F(1,2),GA.add(ONE,B0)); Fm=GA.scal(F(1,2),GA.sub(ONE,B0))
Gp=GA.scal(F(1,2),GA.add(ONE,B1)); Gm=GA.scal(F(1,2),GA.sub(ONE,B1))
for t in (F(0),F(1),F(-7,3),F(5,2)):
    T=GA.sc(t)
    rhs=GA.add(P(GA.sub(S,T),GA.sub(S,T),Fp),P(GA.add(S,T),GA.add(S,T),Fm),P(GA.sub(D,T),GA.sub(D,T),Gp),P(GA.add(D,T),GA.add(D,T),Gm))
    lhs=GA.sub(GA.sc(4+2*t*t),GA.scal(2*t,C))
    assert GA.eq(lhs,rhs)
print("P3(i) certificate holds on l=3 with non-blade, non-(anti)commuting A0,A1 and non-blade B0")
# perturbation: drop the commutation (use B0 in party 1) -> identity fails
Bbad=lin((F(3,5),e[0]),(F(4,5),p[0]))
Cb=GA.add(P(A0,Bbad),P(A0,B1),P(A1,Bbad),GA.neg(P(A1,B1)))
Fpb=GA.scal(F(1,2),GA.add(ONE,Bbad)); Fmb=GA.scal(F(1,2),GA.sub(ONE,Bbad)); t=F(1);T=GA.sc(t)
rhs=GA.add(P(GA.sub(S,T),GA.sub(S,T),Fpb),P(GA.add(S,T),GA.add(S,T),Fmb),P(GA.sub(D,T),GA.sub(D,T),Gp),P(GA.add(D,T),GA.add(D,T),Gm))
print("  identity with a non-commuting B0 holds?", GA.eq(GA.sub(GA.sc(4+2*t*t),GA.scal(2*t,Cb)),rhs))
# ---------------- theta on l=2, m=n=1, built from scratch
sq=(1,-1,1,-1); P2,dag2=mk(sq)
e1,f1,e2,f2=[GA.gen(i) for i in range(4)]
g=P2(f1,e1)
tw=[P2(g,e2),P2(g,f2)]
Ab=[ONE,e1,f1,P2(e1,f1)]
Bb=[ONE,tw[0],tw[1],P2(tw[0],tw[1])]
prods=[(i,j,P2(Ab[i],Bb[j])) for i in range(4) for j in range(4)]
# matrix of the products in the blade basis must be invertible
bl=GA.all_blades(4)
M=[[x.get(b,F(0)) for b in bl] for (_,_,x) in prods]
assert GA.mat_rank(M)==16
def coords(x):
    # solve x = sum c_ij Ab_i Bb_j
    Mt=[list(col) for col in zip(*M)]
    sol=GA.field_solve(Mt,[x.get(b,F(0)) for b in bl])
    return sol
def theta(x):
    c=coords(x); out={}
    for k,(i,j,_) in enumerate(prods):
        if c[k]!=0: out=GA.add(out,GA.scal(c[k],P2(Ab[i],dag2(Bb[j]))))
    return out
X1=e1; Z1=g; X2=P2(e2,g); Z2=P2(f2,e2); Y1=P2(X1,Z1); Y2=P2(X2,Z2); U=P2(X1,X2); V=P2(Z1,Z2); K=P2(e1,f2)
assert GA.eq(K,GA.neg(P2(Y1,Y2)))
lam=lambda c:(lambda x: s0(P2(lin((1,ONE),(-1,U),(-1,V),(c,K)),x)))
for b in bl:
    x={b:F(1)}
    assert GA.eq(theta(theta(x)),x) and GA.eq(theta(dag2(x)),dag2(theta(x)))
    for c in (F(-1),F(1,3),F(2)):
        assert lam(c)(theta(x))==lam(-c)(x)
print("theta: involutive, commutes with dagger, lambda_c o theta = lambda_{-c} on all 16 blades")
# products of local observables, one per party: fixed
locA=[ONE,X1,Z1]; locB=[ONE,X2,Z2]
assert all(GA.eq(theta(P2(a,b)),P2(a,b)) for a in locA for b in locB)
# product of several local observables of each party: not fixed
w4=P2(X1,Z1,X2,Z2)
print("X1 Z1 X2 Z2 = -K:",GA.eq(w4,GA.neg(K)),"; lambda_-1 =",lam(F(-1))(w4)," lambda_1 =",lam(F(1))(w4)," theta(w)=-w:",GA.eq(theta(w4),GA.neg(w4)))
# theta not multiplicative
print("theta multiplicative on X2,Z2?",GA.eq(theta(P2(X2,Z2)),P2(theta(X2),theta(Z2))))
# palindromic sequence of local idempotents
PA=GA.scal(F(1,2),GA.add(ONE,lin((F(3,5),X1),(F(4,5),Z1)))); PB1=GA.scal(F(1,2),GA.add(ONE,X2)); PB2=GA.scal(F(1,2),GA.add(ONE,lin((F(5,13),X2),(F(12,13),Z2))))
seq=P2(PB1,PA,PB2,PA,PB1)
print("palindrome weights equal:",lam(F(-1))(seq)==lam(F(1))(seq), lam(F(-1))(seq))
nonpal=P2(PB1,PB2,PA)
print("non-palindrome PB1 PB2 PA: lambda_-1 =",lam(F(-1))(nonpal)," lambda_1 =",lam(F(1))(nonpal))
# (v) weights of lambda_1 on joint outcomes
print("lambda_1 joint outcomes:",[lam(F(1))(GA.scal(F(1,4),P2(GA.add(ONE,GA.scal(u,U)),GA.add(ONE,GA.scal(v,V))))) for u,v in ((1,1),(1,-1),(-1,1),(-1,-1))])
# (vi) instance
u=GA.scal(F(1,2),lin((1,ONE),(1,Z2),(1,X1),(-1,P2(X1,Z2))))
loc=GA.scal(F(1,4),P2(GA.add(ONE,Z1),GA.add(ONE,X2))); jo=GA.scal(F(1,4),P2(GA.add(ONE,U),GA.add(ONE,V)))
print("(vi):",GA.eq(dag2(u),u),GA.eq(P2(u,u),ONE),GA.eq(P2(u,loc,u),jo),[lam(c)(loc) for c in (F(1),F(-1))],[lam(c)(jo) for c in (F(1),F(-1))])
# ---------------- two copies, l=4, m=n=2
sq4=(1,-1)*4; P4,dag4=mk(sq4)
E=[GA.gen(2*j) for j in range(4)]; Fg=[GA.gen(2*j+1) for j in range(4)]
pp=[P4(Fg[j],E[j]) for j in range(4)]
Xs=[]
for j in range(4):
    x=E[j]
    for i in range(j): x=P4(x,pp[i])
    Xs.append(x)
Zs=pp; Ys=[P4(Xs[j],Zs[j]) for j in range(4)]
for a in range(4):
    for b in range(4):
        if a!=b: assert GA.commutes(Xs[a],Xs[b],sq4) and GA.commutes(Xs[a],Zs[b],sq4)
def Mc(a,b,c): return lin((1,GA.sc(F(1))),(-1,P4(Xs[a],Xs[b])),(-1,P4(Zs[a],Zs[b])),(-c,P4(Ys[a],Ys[b])))
for c in (F(1,2),F(3),F(-2)):
    dens=P4(Mc(0,2,c),Mc(1,3,c))
    for s,t,s2,t2 in product((1,-1),repeat=4):
        p1=GA.scal(F(1,4),P4(GA.add(ONE,GA.scal(s,P4(Xs[0],Xs[1]))),GA.add(ONE,GA.scal(t,P4(Zs[0],Zs[1])))))
        p2=GA.scal(F(1,4),P4(GA.add(ONE,GA.scal(s2,P4(Xs[2],Xs[3]))),GA.add(ONE,GA.scal(t2,P4(Zs[2],Zs[3])))))
        val=s0(P4(dens,p1,p2))
        assert val==F(1,16)*(1+s*s2+t*t2+s*s2*t*t2*c*c),(c,s,t,s2,t2,val)
print("two-copy weight formula verified at c=1/2,3,-2, all 16 signs")
# party-2 algebra check: X3,Z3,X4,Z4 in algebra generated by gamma e_j, gamma f_j (j=3,4), gamma=p1p2
gm=P4(pp[0],pp[1]); twg=[P4(gm,E[2]),P4(gm,Fg[2]),P4(gm,E[3]),P4(gm,Fg[3])]
span=[ONE]
for k in range(1,5):
    for comb in combinations(range(4),k): span.append(P4(*[twg[i] for i in comb]))
bl8=GA.all_blades(8)
def inspan(x):
    Mx=[[y.get(b,F(0)) for b in bl8] for y in span]
    return GA.mat_rank(Mx+[[x.get(b,F(0)) for b in bl8]])==GA.mat_rank(Mx)
print("X3,Z3,X4,Z4 in party-2 algebra:",[inspan(x) for x in (Xs[2],Zs[2],Xs[3],Zs[3])])
# ---------------- P2: CHSH element facts, independent
Cs=GA.add(P2(X1,X2),P2(X1,Z2),P2(Z1,X2),GA.neg(P2(Z1,Z2)))
A1s,A2s,B1s,B2s=e1,P2(f1,e1),P2(e2,f1,e1),P2(f2,e2)
Cp=GA.add(P2(A1s,B1s),P2(A1s,B2s),P2(A2s,B1s),GA.neg(P2(A2s,B2s)))
print("P2's C equals P3's C_0:",GA.eq(Cs,Cp))
C2=P2(Cp,Cp); print("C^2 = 4+4K:",GA.eq(C2,lin((4,ONE),(4,K))),"C^3=8C:",GA.eq(P2(C2,Cp),GA.scal(8,Cp)))
# C is not in the commutative span of any family of commuting projectors: equivalently its eigenvalues are not all rational.
# Independent route: matrix of left multiplication by C on the 16-dim algebra, characteristic poly via exact trace powers
Lc=[[P2(Cp,{b:F(1)}).get(bb,F(0)) for b in bl] for bb in bl]
tr=lambda A: sum(A[i][i] for i in range(len(A)))
A2=GA.mat_mul(Lc,Lc); print("tr L_C =",tr(Lc)," tr L_C^2 =",tr(A2)," (eigs 0 x8, +-2sqrt2 x4 each gives 0 and 64)")
