from dev import *
from fractions import Fraction as F
globals().update({k: v for k, v in vars(ck).items() if not k.startswith("__")})
t0 = time.time()
coef = (F(1), F(-1), F(1), F(-1, 2))
t, x, y, z = X
h = sample_field(17, 2, 5)
Eh = peinstein(h)
print("source nonzero:", not pzero(Eh), " D_boost = 0:", pzero(displacement(XIB)))
K = potential(h, XIB, coef)
dK = bdiv(K)
src = papply(Eh, XIB)
print("div K = -2 E[h](xi):", vzero(vadd(dK, vscal(2, src))))
Kn, Knb = bdotv(K, NU), bdotv(K, NBU)
# K.n = -(B.K) n + perp ; K.nbar = (B.K) nbar + perp
print("K.n:", (Kn[0] + K[(0, 3)]) == 0, (Kn[3] + K[(0, 3)]) == 0, " K.nbar:", (Knb[0] - K[(0, 3)]) == 0, (Knb[3] + K[(0, 3)]) == 0)
lawN = (dK[0] - dK[3]) - (dn(K[(0, 3)] * (-1)) + Kn[1].d(1) + Kn[2].d(2))
lawNb = (dK[0] + dK[3]) - (dnb(K[(0, 3)]) + Knb[1].d(1) + Knb[2].d(2))
print("n.(div K) = d_lam(-B.K) + div_perp(K.n):", lawN == 0, " nbar.(div K) = d_mu(B.K) + div_perp(K.nbar):", lawNb == 0)
# xi = lam n on N, = -mu nbar on Nbar
print("xi on N = lam n:", on_N(XIB[0] - t) == {} and on_N(XIB[3] - t) == {}, " on Nbar = -mu nbar:", on_Nbar(XIB[0] + t) == {} and on_Nbar(XIB[3] - t) == {})
# window
Lam = 2; lo = (0, 0, -1); hi = (Lam, 2, 2)
charge = on_N(K[(0, 3)] * (-1))                      # -B.K on N
top = integrate(cut(charge, Lam), lo[1:], hi[1:])
bot = integrate(cut(charge, 0), lo[1:], hi[1:])
J1, J2 = on_N(Kn[1]), on_N(Kn[2])
sides = (integrate(side(J1, 1, hi[1]), (lo[0], lo[2]), (hi[0], hi[2])) - integrate(side(J1, 1, lo[1]), (lo[0], lo[2]), (hi[0], hi[2]))
         + integrate(side(J2, 2, hi[2]), (lo[0], lo[1]), (hi[0], hi[1])) - integrate(side(J2, 2, lo[2]), (lo[0], lo[1]), (hi[0], hi[1])))
En = papply(Eh, NU)
nEn = En[0] - En[3]
bulk = integrate(on_N(t * nEn * (-2)), lo, hi)       # -2 int lam n.E[h](n)
trperp = ptrace(h) - vdot(NU, papply(h, NBU))
print("top", top, "bot", bot, "sides", sides, "bulk", bulk, top - bot + sides == bulk)
print("bot = int tr_perp h at corner:", bot == integrate(cut(on_N(trperp), 0), lo[1:], hi[1:]))
# light-cone gauge: second route
hg = sample_gauge_field(19, 2, 5)
print("h(n) = 0:", vzero(papply(hg, NU)))
Kg = potential(hg, XIB, coef)
tau = ptrace(hg)
print("-B.K = tau - lam d_n tau on N:", on_N(Kg[(0, 3)] * (-1) - (tau - t * dn(tau))) == {})
Eg = papply(peinstein(hg), NU)
print("n.E[h](n) = 1/2 d_n^2 tau:", ((Eg[0] - Eg[3]) - dn(dn(tau)) * F(1, 2)) == 0, " everywhere")
Kgn = bdotv(Kg, NU)
print("transverse flux has no divergence on N in the gauge:", on_N(Kgn[1].d(1) + Kgn[2].d(2)) == {})
# the two routes: route 1 = [(-B.K)]_0^Lam ; route 2 = [lam theta*2 - tau]... = -int lam d_n^2 tau
r1 = integrate(cut(on_N(Kg[(0, 3)] * (-1)), Lam), lo[1:], hi[1:]) - integrate(cut(on_N(Kg[(0, 3)] * (-1)), 0), lo[1:], hi[1:])
r2 = integrate(on_N(t * dn(dn(tau)) * (-1)), lo, hi)
r3 = integrate(on_N(t * (Eg[0] - Eg[3]) * (-2)), lo, hi)
print("routes:", r1, r2, r3)
# in terms of delta a = 1/2 tau: (da - lam da')(Lam) - da(0) = -int lam n.E(n) => with E = -8 pi G T: = 8 pi G int lam T
da = tau * F(1, 2)
lhs = integrate(cut(on_N(da - t * dn(da)), Lam), lo[1:], hi[1:]) - integrate(cut(on_N(da), 0), lo[1:], hi[1:])
rhs = integrate(on_N(t * (Eg[0] - Eg[3]) * (-1)), lo, hi)
print("first law:", lhs, rhs, lhs == rhs)
print(time.time() - t0)
