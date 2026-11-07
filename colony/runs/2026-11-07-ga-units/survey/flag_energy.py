# Screening check (exact): Z-adapted Witt flags of R^{2,4}; conformal-energy sign of the pure spinor vs family.
import sys; sys.path.insert(0, '/home/claude/phys-graph/lib')
import GA
from fractions import Fraction as F
from itertools import product
# generators 0:e0(+1) 1:nu(+1) 2:e1 3:e2 4:e3 5:em (all -1)
SQ = GA.sig(2,4)
g = [GA.gen(k) for k in range(6)]
M = lambda *xs: (lambda r: r)(__import__('functools').reduce(lambda a,b: GA.mul(a,b,SQ), xs))
# complex multivector = (re, im)
def cm(x,y): return (GA.sub(GA.mul(x[0],y[0],SQ),GA.mul(x[1],y[1],SQ)), GA.add(GA.mul(x[0],y[1],SQ),GA.mul(x[1],y[0],SQ)))
def cz(x): return (GA.is_zero(x[0]) and GA.is_zero(x[1]))
def cscal(c,x):  # c = (a,b) complex rational
    a,b=c; return (GA.sub(GA.scal(a,x[0]),GA.scal(b,x[1])), GA.add(GA.scal(a,x[1]),GA.scal(b,x[0])))
def ceq(x,y): return GA.eq(x[0],y[0]) and GA.eq(x[1],y[1])
R = lambda x: (x, {})
Z = R(M(g[0],g[1]))
I6 = R(M(*g))
I4 = R(M(g[0],g[2],g[3],g[4]))
def eig(op, psi):
    for lam in [(F(0),F(1)),(F(0),F(-1)),(F(1),F(0)),(F(-1),F(0))]:
        if ceq(cm(op,psi), cscal(lam,psi)): return lam
    return None
def conj(x): return (x[0], GA.neg(x[1]))
rows=[]
for s0,s1,s2 in product([1,-1],repeat=3):
    w1=(g[0], GA.scal(-s0,g[1])); w2=(g[2],GA.scal(-s1,g[3])); w3=(g[4],GA.scal(-s2,g[5]))
    W=[w1,w2,w3]
    iso = all(cz(cm(a,b)) or True for a in W for b in W)
    # isotropy: w_a w_b + w_b w_a = 0
    iso = all(cz((GA.add(cm(a,b)[0],cm(b,a)[0]),GA.add(cm(a,b)[1],cm(b,a)[1]))) for a in W for b in W)
    psi = cm(cm(w1,w2),w3)
    ann = all(cz(cm(w,psi)) for w in W)
    lz = eig(Z,psi); l6 = eig(I6,psi)
    # C = Ad(I6) o kappa on psi: I6 conj(psi) I6^{-1}; I6^2:
    rows.append(((s0,s1,s2), iso, ann, lz, l6))
I6sq = GA.mul(I6[0],I6[0],SQ)
print("I6^2 =", I6sq)
for r in rows: print(r)
# energy sign = -s0 * i ; family from I6 eigenvalue
fam = {r[0]: r[4] for r in rows}; en = {r[0]: r[3] for r in rows}
GA.check("energy eigenvalue depends on s0 only", all(en[s]==(F(0),F(-s[0])) for s in en))
GA.check("family = product s0 s1 s2", all(fam[s]==fam[(1,1,1)] if s[0]*s[1]*s[2]==1 else fam[s]!=fam[(1,1,1)] for s in fam))
# Cl(1,3) part: T16 Lemma 5.6 triangle with u = gamma3, B = gamma0 gamma3
SQ4 = GA.sig(1,3); h=[GA.gen(k) for k in range(4)]
m4 = lambda *xs: __import__('functools').reduce(lambda a,b: GA.mul(a,b,SQ4), xs)
I = m4(*h); Bw = m4(h[0],h[3]); J = m4(I,Bw); C = m4(I,h[3])
GA.check("I4 B = g1 g2", GA.eq(J, m4(h[1],h[2])))
GA.check("C J = g0", GA.eq(m4(C,J), h[0]))
GA.check("C(-J) = -g0", GA.eq(m4(C,GA.neg(J)), GA.neg(h[0])))
print("failures:", GA.FAILURES)
