"""scratch: linearised constraints on a slice of a perturbed flat RW h-field (conformal time), via lib/gtg.py"""
import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, gtg
from gtg import Jet
from pert0 import Dual, EPS, tay

NV = 4
def D(x):  # embed
    return x if isinstance(x, Dual) else Dual(x, 0)

def field(a_c, phi_c, psi_c, b_c, k, s0, c0, order=3):
    """conformal time eta = label 0. a_c etc: Taylor coefficient lists at the point.
    hb^-1(e0) = a (1 + eps phi cos) g0 ; hb^-1(e1) = a (1 - eps psi cos) g1 + eps a b sin g0 ; hb^-1(e2,3) = a(1 - eps psi cos) g2,3"""
    a = tay(0, a_c)
    phi = tay(0, phi_c); psi = tay(0, psi_c); b = tay(0, b_c)
    x = Jet.var(1, F(0), NV, order)
    sn, cs = gtg.jsincos(x * k, s0, c0)
    one = Jet.const(1, NV)
    e = Jet.const(EPS, NV)
    TH = [[F(0)] * 4 for _ in range(4)]
    TH[0][0] = a * (one + e * phi * cs)
    TH[0][1] = e * a * b * sn
    for i in range(1, 4):
        TH[i][i] = a * (one - e * psi * cs)
    return gtg.Field(TH), dict(a=a, phi=phi, psi=psi, b=b, sn=sn, cs=cs)

def normal(fld):
    """unit normal n (physical vector, jet coefficients) to the slices eta = const, and unit tangent m1"""
    HJ = fld.hb_matrix_jet()          # HJ[mu][a]: hb(gamma_a) = sum_mu HJ[mu][a] e_mu ; g^mu = sum_a HJ[mu][a] gamma^a
    sq = fld.sq
    # g^0 as a vector: components on gamma_a are HJ[0][a] * sq[a] (gamma^a = gamma_a / sq[a])
    g0 = {(a_,): HJ[0][a_] * sq[a_] for a_ in range(4) if HJ[0][a_]}
    return g0

if __name__ == "__main__":
    k = F(3, 2); s0, c0 = F(3, 5), F(4, 5)
    a_c = [F(2), F(3), F(5, 7), F(1, 3), F(2, 9)]
    Hc = a_c[1] / a_c[0]                      # conformal Hubble rate at the point
    import itertools
    def run(phi_c, psi_c, b_c):
        fld, J = field(a_c, phi_c, psi_c, b_c, k, s0, c0)
        Rc = fld.curvature()
        # normal to first order: n = g0 + eps (b sin) g1   (check orthogonality to g_1)
        bs = J['b'].v * s0
        n = {(0,): Dual(1, 0), (1,): Dual(0, bs)}
        m1 = {(1,): Dual(1, 0), (0,): Dual(0, bs)}
        g1 = gtg.m_val(fld.g[1])
        assert gtg.vdot(n, g1) == Dual(0, 0) * 0 or (gtg.vdot(n, g1).a == 0 and gtg.vdot(n, g1).b == 0), gtg.vdot(n, g1)
        Gn = gtg.einstein(Rc, n)
        Gnn = gtg.vdot(n, Gn)
        Gn1 = gtg.vdot(m1, Gn)
        G11 = gtg.vdot(m1, gtg.einstein(Rc, m1))
        G22 = gtg.vdot(GA.gen(2), gtg.einstein(Rc, GA.gen(2)))
        return Gnn, Gn1, G11, G22
    z = [F(0)] * 5
    for name, (p, q, r) in {'phi': ([F(7, 3), F(1, 2), F(-2, 5), F(1, 7), F(0)], z, z),
                            'psi': (z, [F(5, 2), F(-1, 3), F(3, 4), F(2, 7), F(0)], z),
                            'b': (z, z, [F(1, 4), F(2, 3), F(-3, 5), F(1, 9), F(0)])}.items():
        print(name, run(p, q, r))
    a0, a1, a2 = a_c[0], a_c[1], a_c[2]
    print("bg: -3 Hc^2/a^2 =", -3 * Hc ** 2 / a0 ** 2)
    # predictions (store sign: n.G(n) = -8 pi rho)
    phi_c = [F(7, 3), F(1, 2), F(-2, 5)]
    psi_c = [F(5, 2), F(-1, 3), F(3, 4)]
    b_c = [F(1, 4), F(2, 3), F(-3, 5)]
    # expected first-order n.G(n): -(2/a^2)[ -k^2 psi - 3 Hc (psi' + Hc phi) ... ] etc: print candidate pieces
    print("k^2 psi c/a^2 =", k * k * psi_c[0] * c0 / a0 ** 2)
    print("Hc(psi'+Hc phi) c /a^2 =", Hc * (psi_c[1]) * c0 / a0 ** 2, Hc * Hc * phi_c[0] * c0 / a0 ** 2)
    print("Hc k b c/a^2 =", Hc * k * b_c[0] * c0 / a0 ** 2)
    print("k (psi') s /a^2, k Hc phi s/a^2 =", k * psi_c[1] * s0 / a0 ** 2, k * Hc * phi_c[0] * s0 / a0 ** 2)
