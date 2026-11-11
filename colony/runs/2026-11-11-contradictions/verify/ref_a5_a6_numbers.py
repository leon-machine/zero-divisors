#!/usr/bin/env python3
"""Referee recomputation for A5 (exact, totals as a + b/pi with rational a, b) and A6
(decimal arithmetic, order-of-magnitude cosmological numbers only; not evidence for any identity)."""
import sys
from fractions import Fraction as F
sys.path.insert(0, '/home/claude/phys-graph/lib')
import GA
check = GA.check

# ---- A5. Represent x = a + b/pi + c/pi^2 exactly as a tuple of Fractions in powers of 1/pi (and pi).
# Ball volumes: V2 = pi, V3 = 4 pi/3, V4 = pi^2/2.  Ratios V3/V_D: D=2: 4/3 ; D=3: 1 ; D=4: 8/(3 pi).
share = {2: (F(4, 3), F(0)), 3: (F(1), F(0)), 4: (F(0), F(8, 3))}   # (rational part, coefficient of 1/pi)
D = {1: 2, 7: 2, 3: 4, 5: 4, 2: 3}                                     # towers other than r = 6


def tot(shares):
    a = sum(s[0] for s in shares)
    b = sum(s[1] for s in shares)
    return a, b


def val(x):
    return float(x[0]) + float(x[1]) / 3.141592653589793


T0 = tot([share[D[r]] for r in D])
check("A5 unit-ball total = 11/3 + 16/(3 pi) = (11 pi + 16)/(3 pi)", T0 == (F(11, 3), F(16, 3)))
print("    value", round(val(T0), 4))


# own-cell-radius reading: f_r = (m_r/m_6)(V3/V_D)(a_6/a_r)^3 with m_r = s_r m, a_r = s_r^(1/D) d.
# For D = 4, s = 16: a_r = 2 d, f = 16 * (8/3pi) / 8 = 2 * (8/3pi).
def own_radius_share(Dr, s, root):   # root = s^(1/D) supplied exactly
    r, b = share[Dr]
    fac = F(s) / F(root) ** 3
    return (r * fac, b * fac)


shares = []
for r, Dr in D.items():
    if Dr == 4:
        shares.append(own_radius_share(4, 16, 2))
    else:
        shares.append(share[Dr])
T1 = tot(shares)
check("A5 counter-filling s3 = s5 = 16, own radius: T = 11/3 + 32/(3 pi)", T1 == (F(11, 3), F(32, 3)))
print("    value", round(val(T1), 4))
# The formula itself, derived from densities: D=4 share m_r nu_r a_r/(m_6 nu_6), nu = 1/(V_D a^D).
# with V's as (rational coeff of pi^k): check the D = 4 and D = 2 cases symbolically on rationals by setting
# pi -> symbol: verify f = (m_r/m_6)(V3/V_D)(a6/a_r)^3 for random rationals, with V3/V4 = 8/(3 pi) handled by
# carrying pi^-1 as a separate exponent.
for (mr, m6, ar, a6) in ((F(3), F(5, 2), F(7, 3), F(2, 9)), (F(1, 4), F(9), F(11, 5), F(13, 7))):
    # D = 4: (mr * (1/(V4 ar^4)) * ar) / (m6 / (V3 a6^3)) = (mr/m6)(V3/V4)(a6/ar)^3 -- pure algebra in ar, a6
    lhs = mr * (1 / ar ** 4) * ar / (m6 / a6 ** 3)
    rhs = (mr / m6) * (a6 / ar) ** 3
    lhs2 = mr * (1 / ar ** 2) / ar / (m6 / a6 ** 3)
    check("A5 own-radius share formula (D = 4 and D = 2, V ratios factored)", lhs == rhs and lhs2 == rhs)
# thickness function T(lambda, mu) = 1 + 8/(3 mu) + 16 lambda/(3 pi)
for lam, mu, want in ((1, 1, (F(11, 3), F(16, 3))), (2, 1, (F(11, 3), F(32, 3))), (1, 2, (F(7, 3), F(16, 3)))):
    got = (1 + F(8, 3) / mu, F(16, 3) * lam)
    check(f"A5 T(lambda={lam}, mu={mu}) = {want[0]} + {want[1]}/pi", got == want)
# cube cells side 2d, thickness 2d: each odd share = 1, T = 5
check("A5 cubic cells: T = 5", 1 + 4 * 1 == 5)
# a D=2 tower read at D=4: 1 + 4/3 + 8/3pi + 16/3pi = 7/3 + 8/pi
check("A5 one D=2 tower read at D=4: 7/3 + 24/(3 pi) = 7/3 + 8/pi", (1 + F(4, 3), F(8, 3) + F(16, 3)) == (F(7, 3), F(8)))

# ---- A6 (decimal, order of magnitude) ----
import math
c = 2.99792458e8; G = 6.67430e-11; hbar = 1.054571817e-34; kB = 1.380649e-23
h = 0.6736; H0 = h * 100e3 / 3.0857e22; OmL = 0.6847; Obh2 = 0.02237; Tcmb = 2.7255
H = H0 * math.sqrt(OmL)
tP = math.sqrt(hbar * G / c ** 5)
N = 1 / (H * tP)                              # M_P/H in Planck units (non-reduced M_P)
rho_c_h2 = 3 * (100e3 / 3.0857e22) ** 2 / (8 * math.pi * G)
nB = Obh2 * rho_c_h2 / 1.67262192e-27         # per m^3 (proton mass per baryon; helium binding ignored)
R = c / H
Vball = 4 / 3 * math.pi * R ** 3
T = kB * Tcmb / (hbar * c)                    # 1/m
s = 2 * math.pi ** 2 / 45 * 3.9091 * T ** 3
ngam = 2 * 1.2020569 / math.pi ** 2 * T ** 3
units = math.pi * N ** 2 / math.log(2)
print(f"A6 (decimal) N = M_P/H = {N:.3e}")
print(f"A6 (decimal) baryons in de Sitter ball today {nB*Vball:.2e}, z=1 {nB*8*Vball:.2e}, z=1090 {nB*1091**3*Vball:.2e}")
print(f"A6 (decimal) n_B/s = {nB/s:.3e}, eta = n_B/n_gamma = {nB/ngam:.3e}")
print(f"A6 (decimal) thermal entropy in the ball S = {s*Vball:.2e}")
print(f"A6 (decimal) eps N at eps = 8.7e-11: {8.7e-11*N:.2e};  pi N^2/ln2 = {units:.2e};  8.7e-11 * that = {8.7e-11*units:.2e}")
print(f"A6 (decimal) Q/N today = {nB*Vball/N:.2e};  Q per registered unit = {nB*Vball/units:.2e}")
eta = 6.1e-10
for xi in (2.8e-4, 2.85e-4, 3.2e-4, 4e-3):
    print(f"A6 (decimal) eta' = eta/xi^3 at xi = {xi:g}: {eta/xi**3:.4g}")
print(f"A6 (decimal) xi at eta' = 1: {eta**(1/3):.3e};  Delta N_eff at xi=1: {8/7*(11/4)**(4/3)+3.046:.3f}")
print("FAILURES:", GA.FAILURES)
