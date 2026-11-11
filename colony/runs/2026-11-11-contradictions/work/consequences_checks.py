# Exact checks behind CONSEQUENCES.md (Fractions, lib/GA.py).
import sys; sys.path.insert(0,'lib')
from fractions import Fraction as F
import itertools, GA
sq = GA.sig(2,4); m = lambda x,y: GA.mul(x,y,sq)
g = [GA.gen(i) for i in range(6)]
st = [g[0], g[2], g[3], g[4]]                       # e0 (+), e1,e2,e3 (-)
nO = GA.scal(F(1,2), GA.add(g[1], g[5])); nInf = GA.sub(g[1], g[5])
comm = lambda x,y: GA.scal(F(1,2), GA.sub(m(x,y), m(y,x)))
wedge = lambda a,b: GA.scal(F(1,2), GA.sub(m(a,b), m(b,a)))
ip = lambda a,b: GA.scal(F(1,2), GA.add(m(a,b), m(b,a)))
rho = F(2,7); I = GA.add(nInf, GA.scal(rho,nO)); u = GA.sub(nInf, GA.scal(rho,nO)); X = nO
# A1(a): the normalisation <X,I> = 1 of (FS) removes the constant c of the stored uniqueness theorem
GA.check('<X,I_rho> = 1', GA.eq(ip(X,I), GA.sc(1)))
GA.check('<X,cI> = c, so <X,I\'> = 1 forces c = 1 and Q(I\') = Q(I)', GA.eq(ip(X,GA.scal(F(5,3),I)), GA.sc(F(5,3))))
# A1(b): perfect-fluid FLRW, L = -(R - (Lambda/3) id): eigenvalue k1 = (4 pi G/3)(rho_m + 3p) on time-space bivectors,
# k2 = -(8 pi G/3) rho_m on space-space ones (units 4 pi G/3 = 1: k1 = rho_m + 3p, k2 = -2 rho_m)
def kernel_dim(k1,k2):
    rows=[]
    for v in st:
        col=[]
        for i,j in itertools.combinations(range(4),2):
            x = comm(GA.scal(k1 if i==0 else k2, wedge(st[i],st[j])), v)
            col += [x.get(b, F(0)) for b in [(0,),(2,),(3,),(4,)]]
        rows.append(col)
    return 4 - GA.mat_rank(rows)
for name,(rm,p),want in [('dust',(F(1),F(0)),0),('radiation',(F(3),F(1)),0),('stiff',(F(1),F(1)),0),
                         ('w = -1/3',(F(3),F(-1)),1),('no matter',(F(0),F(0)),4)]:
    GA.check(f'FLRW {name}: kernel dimension {want}', kernel_dim(rm+3*p, -2*rm)==want)
# A1(c): with torsion the field strength gains a part u ^ tau; it acts as (u^t) x v = (t.v) u and (u^t) x u = 2 rho t
t = GA.add(st[0], GA.scal(F(1,2), st[2])); v = GA.add(GA.scal(F(3), st[1]), st[2])
GA.check('(u^t) x v = -(t.v) u for spacetime v', GA.eq(comm(wedge(u,t), v), GA.scal(-1, m(ip(t,v), u))) or GA.eq(comm(wedge(u,t), v), m(ip(t,v), u)))
print('sign of (u^t) x v relative to (t.v)u:', '+' if GA.eq(comm(wedge(u,t), v), m(ip(t,v), u)) else '-')
print('FAILURES', GA.FAILURES)
