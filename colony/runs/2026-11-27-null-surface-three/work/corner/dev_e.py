from dev import *
from fractions import Fraction as F
globals().update({k: v for k, v in vars(ck).items() if not k.startswith("__")})
t0 = time.time()
t, x, y, z = X
# E: quadratic generator in the gauge
hg = sample_gauge_field(29, 2, 5)
L = boost_variation(hg)
print("gauge kept:", vzero(papply(L, NU)), " L nonzero:", not pzero(L))
dh = [[dn(hg[m][k]) for k in range(D)] for m in range(D)]
tau = ptrace(hg)
PL, CR = pconst(NPLUS, ONE), pconst(NCROSS, ONE)
hp, hc = ppair(hg, PL) * F(1, 2), ppair(hg, CR) * F(1, 2)
# <dh, dh> - (d tau)^2 = 2 (d h+)^2 + 2 (d hx)^2 - 1/2 (d tau)^2 = 4 <sigma, sigma> - 2 theta^2
sig2 = (dn(hp) * dn(hp) + dn(hc) * dn(hc)) * F(1, 2)          # <sigma, sigma>, sigma = 1/2 d_n h^TT: 1/4 * 2 (..)
theta = dn(tau) * F(1, 2)
print("pairing split:", (ppair(dh, dh) - dn(tau) * dn(tau) - (sig2 * 4 - theta * theta * 2)) == 0)
w = pomega(hg, L)
nw = w[0] - w[3]
want = t * (sig2 - theta * theta * F(1, 2)) * 4 - dn(t * (ppair(hg, dh) - tau * dn(tau))) * F(1, 2)
print("n.omega(h, L h) on N:", on_N(nw - want) == {}, " off N differs:", (nw - want) != 0)
# on N: L h transverse comps = lam d_n h ; trace L = xi.grad tau
print("tr L = lam d_n tau on N:", on_N(ptrace(L) - t * dn(tau)) == {})
Lam = 2; lo = (0, 0, -1); hi = (Lam, 2, 2)
flux = integrate(on_N(nw), lo, hi)
energy = integrate(on_N(t * (sig2 - theta * theta * F(1, 2))), lo, hi)
far = integrate(cut(on_N(t * (ppair(hg, dh) - tau * dn(tau))), Lam), lo[1:], hi[1:])
near = integrate(cut(on_N(t * (ppair(hg, dh) - tau * dn(tau))), 0), lo[1:], hi[1:])
print("flux", flux, "energy", energy, "far", far, "near", near, flux == 4 * energy - F(1, 2) * far)
# boost maps solutions to solutions: E[L h] = L E[h]
hgen = sample_field(31, 2, 4)
print("E[L h] = L E[h]:", pzero(padd(peinstein(boost_variation(hgen)), boost_variation(peinstein(hgen)), -1)), not pzero(peinstein(hgen)))
# and L of a displacement is a displacement: L D_zeta = D_{[xi, zeta]}
zeta = sample_vector(37)
br = [jsum(XIB[a] * zeta[k].d(a) - zeta[a] * XIB[k].d(a) for a in range(D)) for k in range(D)]
print("L D_zeta = D_[xi,zeta]:", pzero(padd(boost_variation(displacement(zeta)), displacement(br), -1)))
print(time.time() - t0)
