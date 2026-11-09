import sys; sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, gtg
from gtg import Jet, m_add, m_scal, m_mul, m_d, m_val, er, S13
r0, w = F(3), F(1,2)
M = gtg.mass_for_root(r0, w*w); f = gtg.f_static(M)
s0,c0,sp,cp = F(3,5),F(4,5),F(5,13),F(12,13)
O=3
fld = gtg.static_field(r0, s0, c0, f, order=O)
t=Jet.var(0,F(0),4,O); r=Jet.var(1,r0,4,O)
sn,cs=gtg.sincos(2,s0,c0,4,O); sph,cph=gtg.sincos(3,sp,cp,4,O)
R=r-r0
def run(psi, Y, ll, label):
    dY_th = Y.d(2); dY_ph = Y.d(3)
    Acoord=[Jet.const(0,4)*0, Jet.const(0,4)*0, psi*dY_ph/sn, -psi*sn*dY_th]   # A_mu, odd parity
    Hi = fld.hb_matrix_jet()
    A={}
    for mu in (2,3):
        for a in range(4):
            if Hi[mu][a] != 0:
                A=m_add(A, m_scal(Acoord[mu]*Hi[mu][a], er(a)))
    # F = D ^ A
    Hv=fld.hb_matrix_jet()
    Fb={}
    for c in range(4):
        Ac=[F(int(k==c)) for k in range(4)]
        # D_{hb(gamma_c)} A as jet field: sum_mu Hi[mu][c] d_mu A + om[c] x A
        der={}
        for mu in range(4):
            if Hv[mu][c] != 0:
                der=m_add(der, m_scal(Hv[mu][c], m_d(A,mu)))
        der=m_add(der, gtg.comm(fld.om[c], A))
        Fb=m_add(Fb, gtg.grade(m_mul(er(c), der), 2))
    # D . F at the point
    out={}
    for c in range(4):
        Ac=[F(int(k==c)) for k in range(4)]
        DF=fld.cov_phys(Ac, Fb)
        out=GA.add(out, {k:v for k,v in GA.mul(er(c), DF, S13).items() if len(k)==1})
    fj=f(r)
    E = (psi.d(0).d(0) - fj*(fj*psi.d(1)).d(1) + fj*ll*psi/(r*r)).v
    print(label, 'DF=',out, 'E=',E)
    return out,E
for coeffs in [(1,2,3,-1,5,7),(2,0,1,3,-2,1)]:
    c=coeffs
    psi = c[0]+c[1]*t+c[2]*R+c[3]*t*t+c[4]*t*R+c[5]*R*R
    run(psi, cs, 2, 'l=1')
    run(psi, sn*cs*cph, 6, 'l=2,m=1')
