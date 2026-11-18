"""Lead 1, second part: the bath's content on the chain between M_I and M_U (stored: 21 vectors, 48 Weyl fields,
64, 68 or 188 real scalars), and central inputs for c*. Exact rationals; floats only for display."""
from fractions import Fraction as F
def r(CD, tauD, Ns, Nw, Nv, tauB):
    return (F(CD*(Ns + 12*Nv) + 5*tauD*tauB, 225) + F(49*CD*Nw, 4800))/17280
PI = F(314159265358979, 10**14)
v = lambda x: float(x*PI**3)
CSTAR = F(134949, 10**4)
r_v0 = r(12, 0, 4, 45, 12, 4); r_sm0 = r(283, 4, 4, 45, 12, 4)
print('stored bath (4,45,12): per vector %.6f, 22 vectors %.5f, SM copy %.5f' % (v(r_v0), v(22*r_v0), v(r_sm0)))
for Ns in (64, 68, 188):
    print('\nbath (N_s, N_w, N_v) = (%d, 48, 21):' % Ns)
    rv = r(12, 0, Ns, 48, 21, 0)
    print('  per vector %.6f (ratio %.4f, floor ratio %.4f); 9 vectors %.5f; 22 vectors c = %.5f; margin (c*/c)^(1/4) = %.4f; 41-vector count for c<=1: %.2f'
          % (v(rv), float(rv/r_v0), float(rv/r_v0)**.25, v(9*rv), v(22*rv), (float(CSTAR)/v(22*rv))**.25, 1/v(rv)))
    for name, tB in (('bath scalars xi=0', Ns), ('bath scalars conformal', 0)):
        sm = r(283, 4, Ns, 48, 21, tB)
        print('  SM copy (its 4 scalars at 0), %-24s c = %.5f (ratio %.4f); four copies %.4f, margin %.4f' % (name, v(sm), float(sm/r_sm0), v(4*sm), (float(CSTAR)/v(4*sm))**.25))
    CPS = Ns + 3*48 + 12*21
    for name, t in (('all scalars xi=0', Ns), ('all conformal', 0)):
        ps = r(CPS, t, Ns, 48, 21, t)
        print('  copy of this content, %-18s c = %.5f (ratio to stored mirror %.3f, floor ratio %.4f); four copies %.4f against c* = 13.4949: margin %.4f'
              % (name, v(ps), float(ps/r_sm0), float(ps/r_sm0)**.25, v(4*ps), (float(CSTAR)/v(4*ps))**.25))
    # common |1 - 6 xi| at which four copies of this content reach c*
    base = r(CPS, 0, Ns, 48, 21, 0)
    t2 = (CSTAR/4/PI**3 - base)/(F(5*Ns*Ns, 225)/17280)      # tau^2 with tauD = tauB = Ns*tau
    if t2 > 0:
        m = float(t2)**.25
        print('  four copies reach c* at common tau^2 = %.4f, |1-6xi| = %.4f, xi = %.4f or %.4f' % (float(t2), m, (1+m)/6, (1-m)/6))
    else:
        print('  four copies exceed c* already with conformal scalars')
# central inputs for c*: remainder 4.364, baryons 8.7e-11, kappa 145.26, v_R = 4.2e10, pi exact
E = F(10)
def cstar(rem, eta, kappa, vR, pi):
    A = 3*kappa*(F(2435, 1000)*E**18)**3*rem*F(938272, 10**6)*eta
    return A/(2*(4*pi*vR)**4)
weak = cstar(F(4364, 1000) - F(65, 1000), F(865, 100)/E**11, F(1453, 10), F(425, 100)*E**10, F(355, 113))
cent = cstar(F(4364, 1000), F(87, 10)/E**11, F(14526, 100), F(42, 10)*E**10, PI)
print('\nc* at the stored (weakening) ends %.4f; at central inputs %.4f' % (float(weak), float(cent)))
XLO, XHI = F(1522584375, 10**9), F(1548079215, 10**9)
tau = lambda x: (1 - 6*x)**2
for x in (XLO, XHI):
    cc = 4*r(283, 4*tau(x), 4, 45, 12, 4*tau(x))
    print('four SM copies, doublets of bath and copies at xi = %.6f: c = %.4f; margin at stored c* %.4f, at central c* %.4f' % (float(x), v(cc), (float(weak)/v(cc))**.25, (float(cent)/v(cc))**.25))
