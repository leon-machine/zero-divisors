"""R1: the four-form under the stored conjugation (both conventions), the mirror identification sign, duality."""
import sys; sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
from itertools import combinations
import GA
def g4(x): return {b:c for b,c in x.items() if len(b)==4}
def biv(cs, idx):
    out={}
    for (i,j),c in zip(combinations(idx,2),cs):
        if c: out[(i,j)]=F(c)
    return out
# --- Cl(2,4): e0,e1 square +1, e2..e5 square -1; spacetime (1,3) on e0,e2,e3,e4
S24=GA.sig(2,4); st=(0,2,3,4)
I4={st:F(1)}; I6={(0,1,2,3,4,5):F(1)}
Fa=biv([2,-1,3,5,1,-4],st); Fb=biv([1,4,-2,3,3,7],st)
Th=lambda X,Y: g4(GA.scal(F(1,2),GA.add(GA.mul(X,Y,S24),GA.mul(Y,X,S24))))
t=Th(Fa,Fb)
I6inv=GA.scal(-1,I6)
C=lambda x: GA.mul(GA.mul(I6,x,S24),I6inv,S24)   # Ad(I6); kappa fixes real Cl(2,4)
print("field-action convention: Theta(CF)=Theta(F):", Th(C(Fa),C(Fb))==t, " t=",t)
phi=lambda x: GA.reverse(C(x))                    # the stored anti-automorphism
# connection convention: A -> -phi(A), curvature by C; whole-integrand: apply phi to the product
whole=g4(phi(GA.scal(F(1,2),GA.add(GA.mul(Fa,Fb,S24),GA.mul(Fb,Fa,S24)))))
print("whole-integrand convention: phi(<FF>)_4 = <FF>_4:", whole==t)
# frozen-point type integrand for contrast: e(I,V,F,F) top grade under the two conventions
Iv={(1,):F(1)}; Vv={(5,):F(1)}
ff=GA.mul(GA.mul(GA.mul(Iv,Vv,S24),Fa,S24),Fb,S24)
top=lambda x: x.get((0,1,2,3,4,5),F(0))
print("frozen-point integrand top coefficient:", top(ff), " field-action:", top(GA.mul(GA.mul(GA.mul(C(Iv),C(Vv),S24),C(Fa),S24),C(Fb),S24)), " whole:", top(phi(ff)))
# real-linear flag conjugate: reflections in e1,e3,e5 (det -1 on R^{2,4}); on the spacetime 4-space it reflects e3 only
def outer_refl(x, flips):
    out={}
    for b,c in x.items():
        s=-1 if sum(1 for i in b if i in flips)%2 else 1
        out[b]=c*s
    return out
g=lambda x: outer_refl(x,(1,3,5))
print("real-linear flag conjugate reverses Theta:", Th(g(Fa),g(Fb))==GA.scal(-1,t))
# duality: F -> I4 F reverses Theta without any orientation reversal
S13=GA.sig(1,3); I4s={(0,1,2,3):F(1)}
Fa13=biv([2,-1,3,5,1,-4],(0,1,2,3)); Fb13=biv([1,4,-2,3,3,7],(0,1,2,3))
Th13=lambda X,Y,S: g4(GA.scal(F(1,2),GA.add(GA.mul(X,Y,S),GA.mul(Y,X,S))))
t13=Th13(Fa13,Fb13,S13)
d=lambda x: GA.mul(I4s,x,S13)
print("duality F->I4 F: Theta ->", Th13(d(Fa13),d(Fb13),S13)=={b:-c for b,c in t13.items()}, "(reversed)")
# mirror: two even-algebra isomorphisms Cl+(1,3)->Cl+(3,1), one sends I4->I4', the other I4->-I4'
S31=tuple(-s for s in S13)
basis=[GA.sc(1)]+[{p:F(1)} for p in combinations(range(4),2)]+[I4s]
sigma=lambda x: {b:(-c if len(b)==2 else c) for b,c in x.items()}
g0={(0,):F(1)}
ad0=lambda x: GA.mul(GA.mul(g0,x,S13),g0,S13)    # gamma0 x gamma0^{-1}, gamma0^2=1
sigma2=lambda x: sigma(ad0(x))
for name,s in (("sigma",sigma),("sigma o Ad(gamma0)",sigma2)):
    mult=all(GA.eq(s(GA.mul(x,y,S13)),GA.mul(s(x),s(y),S31)) for x in basis for y in basis)
    print(name,": multiplicative",mult," image of I4:",s(I4s), " Theta' coefficient:", Th13(s(Fa13),s(Fb13),S31), "vs", t13)
