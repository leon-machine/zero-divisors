import sys; sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
import itertools, GA
mul,add,sub,neg,scal,sc,gen,eq,rev=GA.mul,GA.add,GA.sub,GA.neg,GA.scal,GA.sc,GA.gen,GA.eq,GA.reverse
ok_all=True
def chk(label,ok):
    global ok_all; ok_all&=bool(ok); print(("PASS " if ok else "FAIL ")+label)

def build(N, kernel=True):
    # generators: [kernel g1,g2 (square -1)] + N hyperbolic planes (e+, e-) squares (+1,-1)
    sq=[]; K=[]
    if kernel: K=[0,1]; sq+=[-1,-1]
    planes=[]
    for k in range(N):
        i=len(sq); sq+=[1,-1]; planes.append((i,i+1))
    return tuple(sq),K,planes
def dag(x,sq):
    out={}
    for b,c in x.items():
        g=len(b); s=(-1)**(g*(g-1)//2) * (-1)**sum(1 for i in b if sq[i]==-1)
        out[b]=c*s
    return {b:c for b,c in out.items() if c!=0}
def comm(x,y,sq): return sub(mul(x,y,sq),mul(y,x,sq))

# --- 1. hyperbolic tower alone: commutant of the even part is span{1, Gamma}, Gamma^2 = +1: no unit
print("1. hyperbolic tower Cl(N,N): no central element of the even part squares to -1")
for N in (1,2,3):
    sq,K,planes=build(N,kernel=False); n=len(sq)
    evengens=[mul(gen(i),gen(j),sq) for i in range(n) for j in range(i+1,n)]
    blades=[b for k in range(n+1) for b in itertools.combinations(range(n),k)]
    commut=[b for b in blades if all(GA.commutes({b:F(1)},g,sq) for g in evengens)]
    Gam=sc(1)
    for (p,m) in planes: Gam=mul(Gam,mul(gen(p),gen(m),sq),sq)
    chk(f"N={N}: commutant of even part = blades {commut} (empty and full), Gamma^2 = {mul(Gam,Gam,sq)}",
        commut==[(),tuple(range(n))] and eq(mul(Gam,Gam,sq),sc(1)))
    # alpha + beta Gamma squares to alpha^2+beta^2 + 2 alpha beta Gamma, never -1 over Q: check the scalar part is a sum of squares
# --- 2. the kernel supplies the unit
print("\n2. tower level Cl(N, N+2) = kernel (0,2) x N hyperbolic planes")
for N in (1,2,3):
    sq,K,planes=build(N); n=len(sq)
    J=mul(gen(0),gen(1),sq)
    a=[scal(F(1,2),add(gen(p),gen(m))) for (p,m) in planes]; ad=[dag(x,sq) for x in a]
    car=all(eq(add(mul(a[j],ad[k],sq),mul(ad[k],a[j],sq)), sc(1 if j==k else 0)) and GA.is_zero(add(mul(a[j],a[k],sq),mul(a[k],a[j],sq))) for j in range(N) for k in range(N))
    Jc=all(GA.commutes(J,gen(i),sq) for i in range(2,n))
    Gam=sc(1)
    for (p,m) in planes: Gam=mul(Gam,mul(gen(p),gen(m),sq),sq)
    I=sc(1)
    for i in range(n): I=mul(I,gen(i),sq)
    chk(f"N={N}: CAR from Witt pairs; J^2=-1: {eq(mul(J,J,sq),sc(-1))}; J^dag=-J: {eq(dag(J,sq),neg(J))}; J commutes with every hyperbolic generator: {Jc}",
        car and eq(mul(J,J,sq),sc(-1)) and eq(dag(J,sq),neg(J)) and Jc)
    In_eq = eq(I,mul(J,Gam,sq)) or eq(I,neg(mul(J,Gam,sq)))
    chk(f"   level pseudoscalar I_n = +-J Gamma: {In_eq}; I_n^2 = -1: {eq(mul(I,I,sq),sc(-1))}; I_n^dag = -I_n: {eq(dag(I,sq),neg(I))}; Gamma^dag = Gamma: {eq(dag(Gam,sq),Gam)}",
        In_eq and eq(mul(I,I,sq),sc(-1)) and eq(dag(I,sq),neg(I)) and eq(dag(Gam,sq),Gam))
    # Gamma = (-1)^F on the hyperbolic modes: Gamma anticommutes with each a_k, commutes with pairs
    chk(f"   Gamma anticommutes with every mode, commutes with every pair: "
        f"{all(GA.anticommutes(Gam,x,sq) for x in a) and all(GA.commutes(Gam,mul(ad[j],a[k],sq),sq) for j in range(N) for k in range(N))}",
        all(GA.anticommutes(Gam,x,sq) for x in a) and all(GA.commutes(Gam,mul(ad[j],a[k],sq),sq) for j in range(N) for k in range(N)))
# --- 3. Hermitian canonical pair with unit J from collective hopping pairs (blocks of two modes)
print("\n3. Hermitian fields from collective pairs: [phi, pi] = 2 J [S, S^dag], S = sum of block pairs")
for M in (1,2):
    N=2*M; sq,K,planes=build(N); n=len(sq); J=mul(gen(0),gen(1),sq)
    a=[scal(F(1,2),add(gen(p),gen(m))) for (p,m) in planes]; ad=[dag(x,sq) for x in a]
    nop=[mul(ad[k],a[k],sq) for k in range(N)]
    S={}
    for k in range(M): S=add(S,mul(ad[2*k],a[2*k+1],sq))
    Sd=dag(S,sq)
    phi=add(S,Sd); pi=mul(J,sub(Sd,S),sq)
    herm = eq(dag(phi,sq),phi) and eq(dag(pi,sq),pi)
    lhs=comm(phi,pi,sq)
    edge={}
    for k in range(M): edge=add(edge,sub(nop[2*k],nop[2*k+1]))
    rhs=scal(2,mul(J,edge,sq))
    chk(f"M={M} blocks: phi, pi self-adjoint: {herm}; [phi,pi] = 2 J sum_k (n_lower - n_upper) exactly: {eq(lhs,rhs)}", herm and eq(lhs,rhs))
    # with the level pseudoscalar instead: pi' = I (S^dag - S)
    I=sc(1)
    for i in range(n): I=mul(I,gen(i),sq)
    pi2=mul(I,sub(Sd,S),sq)
    chk(f"   with I_n as the unit: pi' self-adjoint: {eq(dag(pi2,sq),pi2)}; I_n commutes with phi: {GA.commutes(I,phi,sq)}",
        eq(dag(pi2,sq),pi2) and GA.commutes(I,phi,sq))
print("\nALL:", ok_all)
