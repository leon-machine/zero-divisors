from dev import *
from fractions import Fraction as F
globals().update({k: v for k, v in vars(ck).items() if not k.startswith("__")})
t0 = time.time()
coef = (F(1), F(-1), F(1), F(-1, 2))
t, x, y, z = X
for pc, H, power in wave_maps():
    p = vec(pc)
    print(pc, "null:", dot(p, p) == 0, "in kernel:", einstein(H, p) == ZERO, "n.p:", dot(N, p), "H(n) nonzero:", not GA.is_zero(apply(H, N)),
          "TT part nonzero:", riem(H, p, wedge(E[0], E[1])) != {})
h = vacuum_field(7)
print("E[h] = 0:", pzero(peinstein(h)), " h(n) != 0:", not vzero(papply(h, NU)), time.time() - t0)
# curvature nonzero: h is not a pure displacement: check via R1's shear datum? use E of a perturbed... simply: riem nonzero above
Lam = 2
f = (ONE - (t + z) * F(1, 2 * Lam)) ** 2
g = (x * (ONE * 2 - x)) ** 2 * ((ONE + y) * (ONE * 2 - y)) ** 2 * F(1, 4)
xi = vscal(f * g, XIB)
Dxi = displacement(xi)
print("built", time.time() - t0)
w = pomega(h, Dxi)
print("omega", time.time() - t0)
flux = integrate(on_N(w[0] - w[3]), (0, 0, -1), (Lam, 2, 2))
trperp = ptrace(h) - vdot(NU, papply(h, NBU))
corner = integrate(cut(on_N(g * trperp), 0), (0, -1), (2, 2))
print("flux", flux, "corner", corner, flux == -corner, time.time() - t0)
# off shell
k = sample_field(13)
h2 = padd(h, k)
w2 = pomega(h2, Dxi)
flux2 = integrate(on_N(w2[0] - w2[3]), (0, 0, -1), (Lam, 2, 2))
Exi = papply(peinstein(h2), xi)
bulk = integrate(on_N((Exi[0] - Exi[3]) * 2), (0, 0, -1), (Lam, 2, 2))
tr2 = ptrace(h2) - vdot(NU, papply(h2, NBU))
corner2 = integrate(cut(on_N(g * tr2), 0), (0, -1), (2, 2))
print("off shell:", flux2, bulk, corner2, flux2 == bulk - corner2, time.time() - t0)
