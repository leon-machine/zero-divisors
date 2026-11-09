import sys, time
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, gtg
from GA import RF
from sym import K, C, Jet
t0 = time.time()
tau = K(RF.var())                                   # inner field Q(tau)
s0 = 2 * tau / (1 + tau * tau); c0 = (1 - tau * tau) / (1 + tau * tau)
w = K(RF([tau * 0, tau * 0 + 1]))                   # outer variable w with coefficients in Q(tau)
M = F(1); L = F(7, 2); a, b = F(2), F(-1)
r0 = 2 * M / (1 - w * w)
f = gtg.f_static(M); KK = 2
fld = gtg.static_field(r0, s0 + 0 * w, c0 + 0 * w, f, order=KK - 1, sqrt_f=w)
print('field', time.time() - t0)
t = Jet.var(0, F(0), 4, KK); r = Jet.var(1, r0, 4, KK)
sn, cs = gtg.sincos(2, s0 + 0 * w, c0 + 0 * w, 4, KK)
fj = f(r); sf = fj.pw(F(1, 2), w)
ca, cb = C.H_COEF[0]
h0, h1 = C.generic(ca, t, r - r0), C.generic(cb, t, r - r0)
S = C.angular(sn, cs, L, a, b, 1, KK)
Z = Jet.const(0, 4)
TH1 = [[Z] * 4 for _ in range(4)]
TH1[0][3] = h0 * S / sf
TH1[1][3] = -h1 * S * sf
ric = [{k: gtg._val(v) for k, v in x.items() if gtg._val(v)} for x in C.lin_ricci(fld, TH1)]
Et, Er, Eth = [x.v for x in C.odd_equations(h0, h1, fj, r, M, L)]
pre = -a / (2 * r0 * s0 * w)
ang = (b - 2 * (c0 / s0) * a) / (2 * r0 * r0 * s0)
want = {(0,): pre * Et, (1,): pre * Er, (2,): ang * Eth}
print(time.time() - t0, sorted(ric[3].keys()), all(ric[3][k] == want[k] for k in want), len(ric[3]))
# sanity: a wrong prefactor must fail
print('control', ric[3][(1,)] == 2 * want[(1,)], ric[3][(2,)] == want[(2,)] + 1)
