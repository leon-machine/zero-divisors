"""Bridge-hunter light exact checks (run 2026-11-10-phase3). Fractions only; no store access."""
from fractions import Fraction as F
import itertools

# ---- Lead 1: constant-w stage, index against equation of state --------------------------------
# a ~ t^p, 1 + w = 2/(3p); expanding branch p > 1: nu = 3/2 + 1/(p-1), n_s - 1 = 3 - 2 nu = -2/(p-1).
def tilt_from_w(w):
    p = F(2) / (3 * (1 + w))
    return -F(2) / (p - 1)
def closed(w):            # claimed closed form
    return 6 * (1 + w) / (1 + 3 * w)
for w in (F(-20117, 20351), F(-9, 10), F(-99, 100), F(-11, 10), F(-3, 2)):
    assert tilt_from_w(w) == closed(w), w
w_pl = F(-20117, 20351)
print("L1 tilt at w = -20117/20351:", closed(w_pl), float(closed(w_pl)), " 1+w =", 1 + w_pl)
assert closed(w_pl) == F(-351, 10000)
print("L1 sign: w=-9/10 ->", closed(F(-9, 10)), "(red); w=-11/10 ->", closed(F(-11, 10)), "(blue); w -> -1 gives 0")
# de Sitter stage in the one equation (f, kappa, P) = (-3, kappa, 0): red iff f^2 + 4 kappa > 9 (1-P)^2 iff kappa > 0
for kap in (F(-1), F(0), F(1, 100)):
    print("L1 de Sitter kappa =", kap, "red:", 9 + 4 * kap > 9)
# DESI/DES-type best fit w(a) = w0 + wa (1 - a): sign of 1 + w at a = 1 and a -> 0
w0, wa = F(-82, 100), F(-63, 100)
print("L1 w0wa best fit (all data, DES 2026): 1+w(a=1) =", 1 + w0, " 1+w(a->0) =", 1 + w0 + wa, " crossing at a =", 1 - (-1 - w0) / wa)

# ---- Lead 4: released-norm equation against the stored clock density ---------------------------
# Reduced Lagrangian on the isotropic family: L = 24 (u y' - n s)(y^2 - s^2/u)   [= 24 n s^3 u (al - 1/u)(be - 1/u)]
# with al = y'/(n s), be = y^2/s^2.  Partial derivatives at rational sample points, by exact difference quotients
# of a polynomial/rational function (L is affine in n, quadratic in s, affine in y').
def L(n, s, y, yp, u):
    return 24 * (u * yp - n * s) * (y * y - s * s / u)
def dn(n, s, y, yp, u):  return L(n + 1, s, y, yp, u) - L(n, s, y, yp, u)              # affine in n: exact
def ds(n, s, y, yp, u):  # quadratic... L is cubic in s; exact derivative by formula checked against symmetric quotient limit
    return 24 * (-n * (y * y - s * s / u) + (u * yp - n * s) * (-2 * s / u))
def du(n, s, y, yp, u):
    return 24 * (yp * (y * y - s * s / u) + (u * yp - n * s) * (s * s / (u * u)))
samples = [(F(2), F(3), F(5, 7), F(11, 13), F(17, 19)), (F(1), F(1, 2), F(-3), F(2, 5), F(7)), (F(3, 4), F(5), F(2), F(-1, 3), F(1, 9))]
for (n, s, y, yp, u) in samples:
    al, be = yp / (n * s), y * y / (s * s)
    assert L(n, s, y, yp, u) == 24 * n * s**3 * u * (al - 1 / u) * (be - 1 / u)
    assert dn(n, s, y, yp, u) == -24 * s**3 * (be - 1 / u)
    assert ds(n, s, y, yp, u) == 24 * n * s * s * (3 / u - 2 * al - be)
    assert du(n, s, y, yp, u) == 24 * n * s**3 * (al * be - 1 / (u * u))
    # cubic in s: check ds against the exact third-order finite-difference derivative of a cubic
    h = F(1)
    fd = (-L(n, s + 2*h, y, yp, u) + 8 * L(n, s + h, y, yp, u) - 8 * L(n, s - h, y, yp, u) + L(n, s - 2*h, y, yp, u)) / (12 * h)
    assert fd == ds(n, s, y, yp, u)
print("L4 reduced Lagrangian: dL/dn, dL/ds, dL/du reproduce the three algebraic equations (3 samples, exact)")
# frame equations with a fluid: be = Lam/3 + rho/3, 2 al + be = Lam - p (Lam = 3/u, rho,p in units 8 pi G)
def al_be(Lam, rho, p):
    be = (Lam + rho) / 3
    al = (Lam - p - be) / 2
    return al, be
for Lam, rho, p in itertools.product((F(1), F(3, 2), F(7, 5)), (F(0), F(1), F(5, 3)), (F(0), F(1, 3), F(-2, 7))):
    al, be = al_be(Lam, rho, p)
    u = 3 / Lam
    released = 24 * (al * be - 1 / (u * u))                       # dL/du / (n s^3): the released norm's equation
    stored_v = F(4, 3) * (Lam * (rho - 3 * p) - rho * (rho + 3 * p))   # stored clause (v): E - (8/3) Lam^2
    E = 24 * al * be
    assert E - F(8, 3) * Lam**2 == stored_v == released
print("L4 on the frame equations: 24(al be - 1/u^2) == E - (8/3)Lam^2 == (4/3)[Lam(rho-3p) - rho(rho+3p)] (27 samples, exact)")
print("L4 dust zero at rho = Lam:", F(4, 3) * (F(5) * F(5) - F(5) * F(5)), "; radiation (p=rho/3):", F(4,3)*(0 - 2), "x rho^2")

# ---- Lead 5: the Milne wall at Bessel order 0 --------------------------------------------------
# Solutions a J0 + b Y0.  Physical (Klein-Gordon) form Om = |tau| (f g' - f' g); in the basis (J, Y) written in the
# variable k|tau| on each side, Om(J, Y) = +c for tau > 0 and -c for tau < 0 (c = 2/pi).  A matching M (2x2, acting on
# coefficient columns, in-basis -> out-basis) is canonical iff det M = -1.
# Monodromy of the logarithm: Y0(z e^{+-i pi}) = Y0(z) +- 2i J0(z), J0 even.  Gaussian rationals as (re, im).
class G:
    def __init__(s, re, im=0): s.re, s.im = F(re), F(im)
    def __add__(s, o): return G(s.re + o.re, s.im + o.im)
    def __sub__(s, o): return G(s.re - o.re, s.im - o.im)
    def __mul__(s, o): return G(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)
    def conj(s): return G(s.re, -s.im)
    def __eq__(s, o): return s.re == o.re and s.im == o.im
    def __repr__(s): return "%s%s%si" % (s.re, "+" if s.im >= 0 else "-", abs(s.im))
half = G(F(1, 2)); I = G(0, 1)
def mono(sig):                       # columns: images of J and Y, as (coef of J, coef of Y)
    return {"J": (G(1), G(0)), "Y": (G(0, 2 * sig), G(1))}
def apply(M, v):                     # v = (a, b) meaning a J + b Y
    return (M["J"][0] * v[0] + M["Y"][0] * v[1], M["J"][1] * v[0] + M["Y"][1] * v[1])
H1, H2 = (G(1), I), (G(1), G(0, -1))          # H1 = J + iY, H2 = J - iY
def rule(sig_pos):                   # positive-norm in-mode H1 continued with sign sig_pos, its conjugate with the opposite
    a = apply(mono(sig_pos), H1); b = apply(mono(-sig_pos), H2)
    Jimg = ((a[0] + b[0]) * half, (a[1] + b[1]) * half)
    # Y = (H1 - H2)/(2i) = -i/2 (H1 - H2)
    mi2 = G(0, F(-1, 2))
    Yimg = ((a[0] - b[0]) * mi2, (a[1] - b[1]) * mi2)
    return Jimg, Yimg
def det(Jimg, Yimg): return Jimg[0] * Yimg[1] - Yimg[0] * Jimg[1]
for sig in (+1, -1):
    Jimg, Yimg = rule(sig)
    print("L5 frequency-paired continuation, sign", sig, ": J ->", Jimg, " Y ->", Yimg, " det =", det(Jimg, Yimg),
          " image of H1 =", apply(mono(sig), H1))
avgJ = tuple((x + y) * half for x, y in zip(mono(1)["J"], mono(-1)["J"]))
avgY = tuple((x + y) * half for x, y in zip(mono(1)["Y"], mono(-1)["Y"]))
print("L5 equal-weight average of the two continuations: J ->", avgJ, " Y ->", avgY, " det =", det(avgJ, avgY))
for sig in (+1, -1):
    M = mono(sig); print("L5 single branch", sig, "for both frequencies: det =", det(M["J"], M["Y"]), " real:", M["Y"][0].im == 0)
# real canonical alternatives: J -> -J, Y -> Y + c J, any rational c (det -1): Bogoliubov beta = c/2 up to phase
for c in (F(0), F(1), F(-3, 2)):
    Jimg, Yimg = (G(-1), G(0)), (G(c), G(1))
    a = (Jimg[0] + I * Yimg[0], Jimg[1] + I * Yimg[1])           # image of H1 = J + iY in (J, Y)
    # decompose on out basis H2 (positive norm for tau>0) and H1: a = al H2 + be H1 ; J coef = al+be, Y coef = -i al + i be
    al = (a[0] + I * a[1]) * half; be = (a[0] - I * a[1]) * half
    n2 = lambda z: z.re * z.re + z.im * z.im
    print("L5 real canonical rule c =", c, ": det =", det(Jimg, Yimg), " |alpha|^2 - |beta|^2 =", n2(al) - n2(be), " |beta|^2 =", n2(be))

# ---- Extra: dimmed-burst ratio with no graviton term; boundary amplitude against the entropy ---
D = lambda g, o: (2 + g + o) / (1 + g)
print("X1 D(g=0, o) = 2 + o:", all(D(F(0), o) == 2 + o for o in (F(0), F(1, 3), F(5))), "; D(g, 0) < 2 for g > 0:", D(F(1, 10), F(0)))
# P = 2 lam H^2/(pi M^2), S = pi N^2, N^2 = M^2/H^2  =>  P S = 2 lam (coefficient of pi cancels): rational check of the pi-free part
lam, H2_, M2 = F(3, 7), F(5), F(11)
P_over_invpi = 2 * lam * H2_ / M2; S_over_pi = M2 / H2_
print("X2 P * S = 2 lam:", P_over_invpi * S_over_pi == 2 * lam)

# ---- Extra X3: the stored w = -1/4 branch (standing R3, static hidden direction) read as "dark energy" --------
# Stored: five-dimensional towers hold a fraction between 0.316 and 0.317 of the dark matter, density ~ a^(-9/4).
# Inputs from memory (not stored Facts here): Omega_dm = 0.265, Omega_Lambda = 0.685.  X = Lambda + that component.
# w_X(a) = -1 + (3/4) r/(1+r), r = Om5 a^(-9/4)/OmL;  w0 = w_X(1), wa = -dw/da at a = 1 = (27/16) r/(1+r)^2.
for share in (F(316, 1000), F(317, 1000)):
    Om5 = share * F(265, 1000); OmL = F(685, 1000); r = Om5 / OmL
    w0 = -1 + F(3, 4) * r / (1 + r); wa = F(27, 16) * r / (1 + r) ** 2
    print("X3 share", share, ": Om5 =", float(Om5), " w0 =", float(w0), " wa =", float(wa), " (wa > 0:", wa > 0, "; never below -1:", w0 > -1, ")")
# growth of the share relative to dust from 1+z = 1090: (1090)^(3/4) between 189 and 190  <=> 189^4 < 1090^3 < 190^4
print("X3 189^4 < 1090^3 < 190^4:", 189**4 < 1090**3 < 190**4)
