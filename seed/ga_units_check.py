# Which pseudoscalar can serve as a complex unit on which real space, inside Cl(2,4).
# Written 21 October 2026 for the GA conversion (seed/GA_DICTIONARY.md); exact arithmetic.
import sys; import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lib'))
from fractions import Fraction as F
import GA as g
SQ = g.sig(2,4)      # e0,e1 square +1 ; e2..e5 square -1
# spacetime R^{1,3}: e0 (+), e2,e3,e4 (-); extra plane H: e1 (+), e5 (-)
st=[0,2,3,4]; H=[1,5]
def blade(ix):
    r=g.sc(1)
    for i in ix: r=g.mul(r,g.gen(i),SQ)
    return r
I4=blade(st); I6=blade(range(6))
M=lambda a,b:g.mul(a,b,SQ)
def vec(c): return g.add(*[g.scal(F(x),g.gen(i)) for i,x in c.items()])
def Q(v): return M(v,v)
def dot(a,b): return g.scal(F(1,2),g.add(M(a,b),M(b,a)))
def cplx_ok(J,h,k):
    z=g.add(h,M(J,k)); lhs=M(z,z)
    rhs=g.add(Q(h),g.neg(Q(k)),g.scal(2,M(J,dot(h,k))))
    return g.eq(lhs,rhs)
print("I4^2=-1:",g.eq(M(I4,I4),g.sc(-1)),"I6^2=-1:",g.eq(M(I6,I6),g.sc(-1)))
for name,J in (("I4",I4),("I6",I6)):
    for e in range(6):
        c=g.eq(M(J,g.gen(e)),M(g.gen(e),J))
        print(name,"commutes with e%d:"%e,c)
h,k=vec({1:2,5:1}),vec({1:1,5:3})
print("H plane, J=I4 complex-bilinear:",cplx_ok(I4,h,k))
print("H plane, J=I6 complex-bilinear:",cplx_ok(I6,h,k))
h2,k2=vec({0:1,2:2,1:1}),vec({3:1,4:2,5:1})
print("full V, J=I4:",cplx_ok(I4,h2,k2),"J=I6:",cplx_ok(I6,h2,k2))
