"""Line 1 exploration, part 2: anomaly coefficients from the stored a_4, the anomalous stress map, conservation,
power-law origins, the branch bound and the window numbers. Exact."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../../../lib'))
from fractions import Fraction as F
import GA, gtg
S = gtg.S13

# ---- a_4 density of the stored Fact (i), dropping total derivatives: (1/360) tr(60 R E + 180 E^2 + 5 R^2 - 2 Ric^2
# + 2 Riem^2 + 30 Om.Om), as a triple (Riem^2, Ric^2, R^2) times 1/360; E = e_R R * id + e_Ric * Ric (vector case)
def a4_triple(dim, eR=F(0), eRic=F(0), om=F(0)):
    """dim: fibre dimension; E = eR R id (scalar, spinor) or eRic Ric (vector: tr E = eRic R, tr E^2 = eRic^2 Ric^2);
    om: tr(Om_ij Om_ij) as a multiple of Riem^2."""
    riem = 2 * dim + 30 * om
    ric = -2 * dim + 180 * eRic ** 2
    r2 = 5 * dim + 60 * (eR * dim + eRic) + 180 * eR ** 2 * dim
    return (riem, ric, r2)

def to_weyl_euler(t):
    """(Riem^2, Ric^2, R^2) -> (c, a, r): t = c W^2 - a E4 + r R^2 with W^2 = Riem^2 - 2 Ric^2 + R^2/3,
    E4 = Riem^2 - 4 Ric^2 + R^2."""
    riem, ric, r2 = t
    # riem = c - a ; ric = -2c + 4a ; r2 = c/3 - a + r
    a = (ric + 2 * riem) / 2
    c = riem + a
    r = r2 - c / 3 + a
    return (c, a, r)

def tscale(s, t): return tuple(s * x for x in t)
def tadd(*ts): return tuple(sum(x) for x in zip(*ts))

for xi in (F(1, 6), F(0)):
    t = tscale(1, a4_triple(1, eR=-xi))     # real scalar: sigma w * 2 = +1/2 * 2
    print('scalar xi', xi, t, to_weyl_euler(t))
tD = tscale(-1, a4_triple(4, eR=F(-1, 4), om=F(-1, 2)))    # Dirac: sigma = -1, w = 1/2, times 2
print('Dirac', tD, to_weyl_euler(tD), ' Weyl half', to_weyl_euler(tscale(F(1, 2), tD)))
tV = tadd(tscale(1, a4_triple(4, eRic=F(-1), om=F(-1))), tscale(-2, a4_triple(1)))
print('vector', tV, to_weyl_euler(tV))
aS = to_weyl_euler(a4_triple(1, eR=F(-1, 6)))[1]; aW = to_weyl_euler(tscale(F(1, 2), tD))[1]; aV = to_weyl_euler(tV)[1]
cS = to_weyl_euler(a4_triple(1, eR=F(-1, 6)))[0]; cW = to_weyl_euler(tscale(F(1, 2), tD))[0]; cV = to_weyl_euler(tV)[0]
print('a weights', aS, aW, aV, 'ratios', aW / aS, aV / aS, ' c ratios', cW / cS, cV / cS)
content = 48 * aW / aS + 12 * aV / aS
print('content a (units of one real scalar):', content, '+8 ->', content + 8, ' 28*36 =', 28 * 36)
print('c content', 48 * cW / cS + 12 * cV / cS, '+8', 48 * cW / cS + 12 * cV / cS + 8)

# ---- spin-curvature trace in the algebra: sum_ij <(1/2 R(e_i^e_j)) (1/2 R(e^i ^ e^j))> * 4 = -K/2
tau, fld0 = gtg.kasner_field((F(1, 2), F(1, 3), F(1, 5)), 2)
Rc = gtg.Field(fld0.TH).curvature()
R = gtg.as_op(Rc)
tot = F(0)
for i in range(4):
    for j in range(4):
        if i != j:
            A = R(gtg.wedge(GA.gen(i), GA.gen(j), S)); B = R(gtg.wedge(gtg.er(i, S), gtg.er(j, S), S))
            tot += gtg.sp(gtg.m_mul(gtg.m_scal(F(1, 2), A), gtg.m_scal(F(1, 2), B), S))
print('4*sum <Om Om> =', 4 * tot, '  -K/2 =', -gtg.kretschmann(Rc) / 2)

# ---- anomalous stress map on Weyl-flat fields: T_A(a) = 2 alpha [Ric(Ric(a)) - (2/3) R Ric(a) - (1/2) Ric2 a + (1/4) R^2 a]
def TA(Rc, a):
    r = gtg.ricci_scalar(Rc)
    Ra = gtg.ricci(Rc, a)
    return gtg.m_scal(2, gtg.m_add(gtg.ricci(Rc, Ra), gtg.m_scal(-F(2, 3) * r, Ra),
                                   gtg.m_scal(-gtg.ricci_sq(Rc) / 2 + r * r / 4, a)))
for (a, ad, add) in [(F(2), F(3), F(5)), (F(1), F(1, 2), F(-1, 4)), (F(7, 3), F(-2), F(11, 5))]:
    Rc = gtg.flrw_flat(a, ad, add).curvature()
    H = ad / a
    T0 = TA(Rc, GA.gen(0)); T1 = TA(Rc, GA.gen(1))
    tr = sum((gtg.vdot(gtg.er(m, S), TA(Rc, GA.gen(m)), S) for m in range(4)), F(0))
    print('T_A(g0) =', T0, ' 6H^4 =', 6 * H ** 4, '| T_A(g1) =', T1, ' -P_A = ', -(2 * H ** 4 - 8 * H * H * add / a),
          '| trace', tr, 'E', gtg.euler_density(Rc), '| Ric(g0)', gtg.ricci(Rc, GA.gen(0)), gtg.ricci(Rc, GA.gen(1)))
