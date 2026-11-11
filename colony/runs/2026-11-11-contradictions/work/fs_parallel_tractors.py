# Exact check (Fractions, lib/GA.py): parallel tractors of the (FS) gauge field
# A_rho(a) = Omega(a) - (nInf - rho nO) ^ hb^{-1}(a), in a gauge hb = 1, Omega = 0 at the point.
import sys; sys.path.insert(0,'lib')
from fractions import Fraction as F
import itertools, GA
sq = GA.sig(2,4)   # gens 0,1 square +1 ; 2..5 square -1
m = lambda x,y: GA.mul(x,y,sq)
g = [GA.gen(i) for i in range(6)]
# spacetime: time = g0 (+), space = g2,g3,g4 (-); added plane: e4 := g1 (+), e5 := g5 (-)
st = [g[0], g[2], g[3], g[4]]
nO  = GA.scal(F(1,2), GA.add(g[1], g[5]))
nInf = GA.sub(g[1], g[5])
comm = lambda x,y: GA.scal(F(1,2), GA.sub(m(x,y), m(y,x)))     # commutator product
wedge = lambda a,b: GA.scal(F(1,2), GA.sub(m(a,b), m(b,a)))    # for vectors
GA.check('nO.nInf = 1', GA.eq(GA.scal(F(1,2), GA.add(m(nO,nInf), m(nInf,nO))), GA.sc(1)))
for rho in (F(1,3), F(-2,5), F(7,4)):
    I = GA.add(nInf, GA.scal(rho, nO)); u = GA.sub(nInf, GA.scal(rho, nO))
    GA.check(f'rho={rho}: Q(I) = 2 rho', GA.eq(m(I,I), GA.sc(2*rho)))
    GA.check(f'rho={rho}: u.I = 0', GA.is_zero(GA.add(m(u,I), m(I,u))))
    ok1 = all(GA.is_zero(comm(wedge(u,a), I)) for a in st)
    GA.check(f'rho={rho}: solder bivectors u^a stabilise I', ok1)
    ok2 = all(GA.eq(comm(wedge(u,a), wedge(u,b)), GA.scal(2*rho, wedge(a,b))) for a in st for b in st)
    GA.check(f'rho={rho}: (u^a)x(u^b) = 2 rho a^b  (so F = Lorentz block L = R + 2 rho E^E, torsion-free)', ok2)
    ok3 = all(GA.eq(comm(wedge(u,a), u), GA.scal(2*rho, a)) for a in st)
    GA.check(f'rho={rho}: (u^a) x u = 2 rho a  (u is moved into spacetime by the soldering)', ok3)
    ok4 = all(GA.is_zero(comm(wedge(a,b), I)) and GA.is_zero(comm(wedge(a,b), u)) for a in st for b in st)
    GA.check(f'rho={rho}: Lorentz bivectors kill I and u, so F x T = L x v for T = alpha I + beta u + v', ok4)
# de Sitter-subtracted curvature of an FLRW-type field: L(a^b) = k1 a^b on time-space, k2 a^b on space-space.
# kernel vector v: (L(a^b)) x v = 0 for all a,b.  Exact rank of the linear map v -> (L(a^b) x v)_{a<b}.
def kernel_dim(k1,k2):
    rows=[]
    for vi in st:
        col=[]
        for i,j in itertools.combinations(range(4),2):
            k = k1 if i==0 else k2
            x = comm(GA.scal(k, wedge(st[i],st[j])), vi)
            for b in [(0,),(2,),(3,),(4,)]:
                col.append(x.get(b, F(0)))
        rows.append(col)
    return 4 - GA.mat_rank(rows)
GA.check('conformally flat matter region (k1,k2 both nonzero): no kernel vector', kernel_dim(F(1,2),F(-3,7))==0)
GA.check('exact de Sitter at the same Lambda (L = 0): kernel is everything', kernel_dim(F(0),F(0))==4)
print('FAILURES', GA.FAILURES)
