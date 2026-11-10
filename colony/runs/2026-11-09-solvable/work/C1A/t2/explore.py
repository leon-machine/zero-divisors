import sys; sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, gtg
from gtg import Jet, m_add, m_scal, m_mul, m_d, m_val, er, S13
r0, w = F(3), F(1, 2)
M = gtg.mass_for_root(r0, w*w)          # f(r0) = w^4
f = gtg.f_static(M)
print('M', M, 'f(r0)', 1-2*M/r0)
fld = gtg.static_field(r0, F(3,5), F(4,5), f, order=2)
print('torsion free', fld.torsion_free())
NV=4; K=3
t = Jet.var(0, F(0), NV, K); r = Jet.var(1, r0, NV, K); th = Jet.var(2, F(0), NV, K); ph = Jet.var(3, F(0), NV, K)
fj = f(r); q = fj.pw(F(1,4), w)
# generic even multivector Phi with polynomial jet coefficients
import itertools
evens=[(),(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(0,1,2,3)]
T=t; R=r-r0; A=th; P=ph
coef=[1,2,-1,3,5,-2,4,1]
Phi={}
for k,b in enumerate(evens):
    c=coef[k]
    Phi[b]= c + (k+1)*T + (2*k-3)*R + (k-2)*A + (3-k)*P + (k%3)*T*R + (k-1)*R*A + 2*A*P - k*R*R
psi={b: c*(1/(r*q)) for b,c in Phi.items()}
Hi=fld.hb_matrix()
def Dirac(psi):
    out={}
    for c in range(4):
        der={}
        for mu in range(4):
            if Hi[mu][c]:
                der=m_add(der, m_scal(Hi[mu][c], m_d(psi,mu)))
        term=m_add(der, m_scal(F(1,2), m_mul(fld.om[c], psi)))
        out=m_add(out, m_mul(er(c), term))
    return out
Dpsi=m_val(Dirac(psi))
lhs={b: c*r0*w**3 for b,c in Dpsi.items()}
lhs={b:c for b,c in lhs.items() if c}
s0,c0=F(3,5),F(4,5)
f0=w**4
dt=m_val(m_d(Phi,0)); dr=m_val(m_d(Phi,1)); dth=m_val(m_d(Phi,2)); dph=m_val(m_d(Phi,3)); P0=m_val(Phi)
Kphi=m_add(GA.mul(er(2), m_add(dth, m_scal(c0/s0/2, P0)), S13), GA.mul(er(3), m_scal(1/s0, dph), S13))
rhs=m_add(GA.mul(er(0), dt, S13), GA.mul(er(1), m_scal(f0, dr), S13), m_scal(w*w/r0, Kphi))
print('reduction holds:', GA.sub(lhs, rhs)=={})
print(GA.sub(lhs,rhs))
for c in range(4): print(c, fld.omega(c))
