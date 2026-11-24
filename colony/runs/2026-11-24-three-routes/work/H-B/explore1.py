"""Line 1 exploration: Euler density of the Robertson-Walker gauge field, exact (lib/gtg.py)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../../../lib'))
from fractions import Fraction as F
import GA, gtg

S = gtg.S13
I4 = gtg.pseudoscalar(S)

def dual_trace(R):
    """-4 Tr((I R)^2) over the six frame planes, with reciprocal planes for the trace."""
    R = gtg.as_op(R)
    tot = F(0)
    for a in range(4):
        for b in range(a + 1, 4):
            B = gtg.wedge(GA.gen(a), GA.gen(b), S)
            X = gtg.m_mul(I4, R(gtg.grade(gtg.m_mul(I4, R(B), S), 2)), S)
            Brec = gtg.wedge(gtg.er(b, S), gtg.er(a, S), S)   # reciprocal plane: <Brec B> = 1
            tot += gtg.sp(gtg.m_mul(Brec, X, S))
    return -4 * tot

# generic FLRW instants
for (a, ad, add) in [(F(2), F(3), F(5)), (F(1), F(1, 2), F(-1, 4)), (F(7, 3), F(-2), F(11, 5))]:
    fld = gtg.flrw_flat(a, ad, add)
    Rc = fld.curvature()
    H = ad / a
    E = gtg.euler_density(Rc)
    print('FLRW', a, ad, add, 'E =', E, ' 24 H^2 addot/a =', 24 * H * H * add / a, ' -4Tr((IR)^2) =', dual_trace(Rc),
          ' R =', gtg.ricci_scalar(Rc), ' Weyl=0:', all(not v for v in gtg.weyl_op(Rc).values()))
    print('   calR planes:', {k: v for k, v in Rc.items()})
# radiation field
tau, fld0 = gtg.kasner_field((F(1, 2),) * 3, 2)
fld = gtg.Field(fld0.TH)
Rc = fld.curvature()
print('radiation t =', tau, 'E =', gtg.euler_density(Rc), ' -3/(2t^4) =', F(-3, 2) / tau ** 4, 'R =', gtg.ricci_scalar(Rc),
      'Ric2 =', gtg.ricci_sq(Rc), 'K =', gtg.kretschmann(Rc), 'dual', dual_trace(Rc))
# Kasner (Weyl-curved) to test the dual-trace formula off the symmetric case
tau, fld0 = gtg.kasner_field((F(2, 3), F(2, 3), F(-1, 3)), 2)
Rc = gtg.Field(fld0.TH).curvature()
print('Kasner E', gtg.euler_density(Rc), 'dual', dual_trace(Rc), 'K', gtg.kretschmann(Rc))
tau, fld0 = gtg.kasner_field((F(1, 2), F(1, 3), F(1, 5)), 2)
Rc = gtg.Field(fld0.TH).curvature()
print('non-vacuum Bianchi I E', gtg.euler_density(Rc), 'dual', dual_trace(Rc), 'K', gtg.kretschmann(Rc), 'Ric2', gtg.ricci_sq(Rc))
