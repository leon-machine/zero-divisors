"""Fix round, lead 1: the chain's bath in both places it enters. c* = A/(2 M_3^4) with A = 3 kappa_s M_P^3 (...),
kappa_s = sqrt(pi^2 g/90)(2 pi^2/45) g at g_* = g_s = g, so c*(g) = c*(100) (g/100)^(3/2). Display only."""
from fractions import Fraction as F
def r(CD, tauD, Ns, Nw, Nv, tauB):
    return (F(CD*(Ns + 12*Nv) + 5*tauD*tauB, 225) + F(49*CD*Nw, 4800))/17280
PI = 3.14159265358979
CS100 = 13.4949
for Ns in (188, 64, 68):
    g = Ns + F(7, 8)*2*48 + 2*21
    cs = CS100*(float(g)/100)**1.5
    bath = (Ns, 48, 21)
    rv = float(r(12, 0, *bath, 0))*PI**3
    sm = float(r(283, 4, *bath, Ns))*PI**3
    C = Ns + 396
    own0 = float(r(C, Ns, *bath, Ns))*PI**3; ownc = float(r(C, 0, *bath, 0))*PI**3
    print('N_s=%d g=%s c*=%.3f ratio %.4f' % (Ns, g, cs, cs/CS100))
    print('  per vector %.6f; 22 vectors c=%.4f margin %.4f; c*/vector = %.1f' % (rv, 22*rv, (cs/(22*rv))**.25, cs/rv))
    print('  four SM c=%.4f margin %.4f; c*/SM = %.2f' % (4*sm, (cs/(4*sm))**.25, cs/sm))
    print('  four chain copies xi=0 c=%.4f margin %.4f; conformal c=%.4f margin %.4f; c*/copy %.2f, %.2f' % (4*own0, (cs/(4*own0))**.25, 4*ownc, (cs/(4*ownc))**.25, cs/own0, cs/ownc))
    base = float(r(C, 0, *bath, 0))
    t2 = (cs/4/PI**3 - base)/(5*Ns*Ns/225/17280)
    m = t2**.25
    print('  crossing: tau^2=%.4f |1-6xi|=%.4f xi in (%.4f, %.4f)' % (t2, m, (1-m)/6, (1+m)/6))
    # floor scaling (c g^-1/2)^(1/4) for vectors
    print('  vector floor ratio (c ratio * (100/g)^(1/2))^(1/4) = %.4f' % ((rv/0.0240547)*(100/float(g))**.5)**.25)
# working branch (8,45,12): g = 100 + 4 (stored round value 100 for (4,45,12))
for bath, dg in (((8,45,12), 4), ((8,48,12), 4 + 5.25)):
    g = 100 + dg; cs = CS100*(g/100)**1.5
    c4 = 4*float(r(8 + 3*bath[1] + 144, 8, *bath, 8))*PI**3; v22 = 22*float(r(12, 0, *bath, 0))*PI**3
    print(bath, 'c* %.3f; four copies c %.4f margin %.4f; 22 vectors %.4f margin %.4f' % (cs, c4, (cs/c4)**.25, v22, (cs/v22)**.25))
