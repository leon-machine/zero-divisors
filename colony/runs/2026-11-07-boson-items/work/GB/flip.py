import sys; sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
mul,add,sub,neg,scal,sc,gen,eq=GA.mul,GA.add,GA.sub,GA.neg,GA.scal,GA.sc,GA.gen,GA.eq
def build(N):
    sq=[-1,-1]; planes=[]
    for k in range(N):
        i=len(sq); sq+=[1,-1]; planes.append((i,i+1))
    return tuple(sq),planes
def dag(x,sq):
    out={}
    for b,c in x.items():
        g=len(b); s=(-1)**(g*(g-1)//2)*(-1)**sum(1 for i in b if sq[i]==-1)
        out[b]=c*s
    return {b:c for b,c in out.items() if c!=0}
def comm(x,y,sq): return sub(mul(x,y,sq),mul(y,x,sq))
for N in (1,2,3):
    sq,planes=build(N); n=len(sq)
    J=mul(gen(0),gen(1),sq)
    Gam=sc(1)
    for (p,m) in planes: Gam=mul(Gam,mul(gen(p),gen(m),sq),sq)
    u=mul(Gam,gen(0),sq); ud=dag(u,sq)
    I=sc(1)
    for i in range(n): I=mul(I,gen(i),sq)
    uinv=ud
    Ad=lambda x: mul(mul(u,x,sq),uinv,sq)
    print(N, "unitary", eq(mul(u,ud,sq),sc(1)), eq(mul(ud,u,sq),sc(1)),
      "fixes transport gens", all(eq(Ad(gen(i)),gen(i)) for i in range(2,n)),
      "J->-J", eq(Ad(J),neg(J)), "I->-I", eq(Ad(I),neg(I)), "g1 fixed", eq(Ad(gen(0)),gen(0)), "g2->-g2", eq(Ad(gen(1)),neg(gen(1))),
      "u^2", mul(u,u,sq))
    # elements of span{Gam g1, Gam g2} anticommute with J: rotation family
    u2=add(scal(F(3,5),mul(Gam,gen(0),sq)),scal(F(4,5),mul(Gam,gen(1),sq)))
    print("  3/5,4/5 combo unitary", eq(mul(u2,dag(u2,sq),sq),sc(1)), "J->-J", eq(mul(mul(u2,J,sq),dag(u2,sq),sq),neg(J)))
# classification: a non-homogeneous unit quaternion of the commutant rotates J out of span{1,J} (grading broken)
for N in (1,2):
    sq,planes=build(N); n=len(sq); J=mul(gen(0),gen(1),sq)
    Gam=sc(1)
    for (p,m) in planes: Gam=mul(Gam,mul(gen(p),gen(m),sq),sq)
    x=scal(F(1,2),add(sc(1),J,mul(Gam,gen(0),sq),mul(Gam,gen(1),sq)))
    xi=dag(x,sq)
    print(N,"x unitary",eq(mul(x,xi,sq),sc(1)),"x J x^-1 =",mul(mul(x,J,sq),xi,sq)=={},
          "image of g1 homogeneous?", len({len(b)%2 for b in mul(mul(x,gen(0),sq),xi,sq)})==1,
          "fixes transport", all(eq(mul(mul(x,gen(i),sq),xi,sq),gen(i)) for i in range(2,n)))
    print("   x J x^-1:", mul(mul(x,J,sq),xi,sq))
