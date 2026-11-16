"""scratch: expansion of the slice normal, slice curvature, and the constraint identities"""
import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, gtg
from gtg import Jet
from pert2 import NV, ORD, Z, E1, tay, build, split, vd, components

def cov_frame(fld, c, V):
    """(gamma_c . D) V as jets"""
    HJ = fld.hb_matrix_jet()
    out = gtg.comm(fld.om[c], V, fld.sq)
    for mu in range(fld.d):
        if HJ[mu][c]:
            out = gtg.m_add(out, gtg.m_scal(HJ[mu][c], gtg.m_d(V, mu)))
    return out

def unit_normal(fld):
    HJ = fld.hb_matrix_jet()
    sq = fld.sq
    g0 = {(a_,): HJ[0][a_] * sq[a_] for a_ in range(4) if HJ[0][a_]}
    q = gtg.vdot(g0, g0, sq)
    inv = q.pw(F(-1, 2))
    return {b: c * inv for b, c in g0.items()}

def expansion(fld):
    n = unit_normal(fld)
    th = None
    for c in range(4):
        dn = cov_frame(fld, c, n)
        t = gtg.vdot(gtg.er(c, fld.sq), dn, fld.sq)
        th = t if th is None else th + t
    return n, th

def slice_curv(a0, psi0, k, s0, c0, order=ORD):
    """scalar curvature (store sign) of the 3-field TH = a0 (1 - eps psi0 cos kx) on Cl(0,3)"""
    nv = 4  # labels x1,x2,x3 -> 0,1,2 ; eps -> 3
    x = Jet.var(0, F(0), nv, order)
    sn, cs = gtg.jsincos(x * k, s0, c0)
    eps = Jet.var(3, F(0), nv, order)
    one = Jet(1, None, nv, order)
    sc = (one - eps * cs * psi0) * a0
    TH = [[F(0)] * 3 for _ in range(3)]
    for i in range(3):
        TH[i][i] = sc
    sq3 = GA.sig(0, 3)
    fld = gtg.Field(TH, sq=sq3)
    Rc = fld.curvature_jet()
    Rs = gtg.ricci_scalar(Rc, sq3)
    return Rs.coeff((0, 0, 0, 0)), Rs.coeff((0, 0, 0, 1))

if __name__ == "__main__":
    k = F(3, 2); s0, c0 = F(3, 5), F(4, 5)
    a_c = [F(2), F(3), F(5, 7), F(1, 3)]
    a0 = a_c[0]; Hc = a_c[1] / a_c[0]
    z = [F(0)] * 4
    P = [F(7, 3), F(1, 2), F(-2, 5), F(1, 7)]
    S = [F(5, 2), F(-1, 3), F(3, 4), F(2, 7)]
    B = [F(1, 4), F(2, 3), F(-3, 5), F(1, 9)]
    for name, (p, q, r) in {'phi': (P, z, z), 'psi': (z, S, z), 'b': (z, z, B), 'all': (P, S, B)}.items():
        fld = build(a_c, p, q, r, k, s0, c0)
        n, th = expansion(fld)
        print(name, 'n =', {b: split(c) for b, c in n.items()}, 'theta =', split(th))
    A = a0
    print("bg theta = 3 Hc/a =", 3 * Hc / A)
    print("phi pred -3 Hc phi c/a:", -3 * Hc * P[0] * c0 / A)
    print("psi pred -3 psi' c/a:", -3 * S[1] * c0 / A)
    print("b pred  k b c /a:", k * B[0] * c0 / A)
    print("3-curv:", slice_curv(a0, S[0], k, s0, c0), " 4 k^2 psi c/a^2 =", 4 * k * k * S[0] * c0 / A ** 2)
