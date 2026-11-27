from dev import *
from fractions import Fraction as F
globals().update({k: v for k, v in vars(ck).items() if not k.startswith("__")})
t0 = time.time()
coef = (F(1), F(-1), F(1), F(-1, 2))
t, x, y, z = X

def at_corner(f):
    """restriction to the corner t = z = 0: polynomial {(b, c)} in (x, y)."""
    return cut(on_N(f), 0)

h = sample_field(11)
w = sample_poly(Stream(5), 2, 4) + 1        # weight c(x), generic, a function on spacetime
xi = vscal(w, XIB)
K = potential(h, xi, coef)
trperp = ptrace(h) - vdot(NU, papply(h, NBU)) * F(1, 2) * 2 * F(1, 2)
# tr_par = 1/2 (nbar.h(n) + n.h(nbar)) = n.h(nbar)   (reciprocals of n, nbar are nbar/2, n/2)
trpar = vdot(NU, papply(h, NBU))
trperp = ptrace(h) - trpar
print("tr_perp = -(H11 + H22):", (trperp + h[1][1] + h[2][2]) == 0)
print("B.K + w tr_perp = 0 at corner:", at_corner(K[(0, 3)] + w * trperp) == {}, "nonzero:", at_corner(w * trperp) != {})
print("not the full trace:", at_corner(K[(0, 3)] + w * ptrace(h)) != {})
# other components of K at the corner are not all zero (K is not a multiple of B there)
print("other comps at corner:", {b: at_corner(K[b]) != {} for b in K})
# Y ambiguity: Y(h, k) = h(d_a) ^ k(a); at the corner with k = D_xi it vanishes because D_xi = 0 there
Dxi = displacement(xi)
print("D_xi at corner zero:", all(at_corner(c) == {} for r in Dxi for c in r), " D_xi nonzero elsewhere:", not pzero(Dxi))
# gauge behaviour
zeta = sample_vector(23)
Dz = displacement(zeta)
trp = lambda Hm: ptrace(Hm) - vdot(NU, papply(Hm, NBU))
print("tr_perp D_zeta = 2 div_perp zeta:", (trp(Dz) - (zeta[1].d(1) + zeta[2].d(2)) * 2) == 0)
# zeta fixing the corner: zeta = t u + z v
u, v = sample_vector(31), sample_vector(37)
zfix = vadd(vscal(t, u), vscal(z, v))
Kz = potential(displacement(zfix), xi, coef)
print("corner-fixing displacement: B.K at corner", at_corner(Kz[(0, 3)]) == {}, " D nonzero at corner:", any(at_corner(c) != {} for r in displacement(zfix) for c in r))
# zeta moving the corner off itself along n and nbar, transverse part zero on the corner
a_, b_ = sample_poly(Stream(41), 2, 4), sample_poly(Stream(43), 2, 4)
znorm = vadd(vadd(vscal(a_, NU), vscal(b_, NBU)), [ZJ, t * a_, z * b_, ZJ])
print("normal displacement:", at_corner(potential(displacement(znorm), xi, coef)[(0, 3)]) == {}, any(at_corner(c) != {} for c in znorm))
# tangential: change is 2 w div_perp zeta, integral over window = boundary flux for w = 1
ztan = [ZJ, zeta[1], zeta[2], ZJ]
Kt = potential(displacement(ztan), XIB, coef)
dens = at_corner(Kt[(0, 3)])
tot = integrate(dens, (-1, -1), (1, 1))
# boundary flux of -2 zeta_perp through the sides of the square
z1, z2 = at_corner(zeta[1]), at_corner(zeta[2])
def sidex(P, val):   # set x = val, integrate y
    out = {}
    for e, c in P.items():
        out[(e[1],)] = out.get((e[1],), F(0)) + c * F(val) ** e[0]
    return integrate(out, (-1,), (1,))
def sidey(P, val):
    out = {}
    for e, c in P.items():
        out[(e[0],)] = out.get((e[0],), F(0)) + c * F(val) ** e[1]
    return integrate(out, (-1,), (1,))
flux = sidex(z1, 1) - sidex(z1, -1) + sidey(z2, 1) - sidey(z2, -1)
print("tangential: total", tot, " = -2 flux", -2 * flux, tot == -2 * flux)
print(time.time() - t0)
print("dens", dens)
print(z1, z2)
tot = integrate(dens, (0, -1), (2, 2))
def sidex(P, val):
    out = {}
    for e, c in P.items():
        out[(e[1],)] = out.get((e[1],), F(0)) + c * F(val) ** e[0]
    return integrate(out, (-1,), (2,))
def sidey(P, val):
    out = {}
    for e, c in P.items():
        out[(e[0],)] = out.get((e[0],), F(0)) + c * F(val) ** e[1]
    return integrate(out, (0,), (2,))
flux = sidex(z1, 2) - sidex(z1, 0) + sidey(z2, 2) - sidey(z2, -1)
print(tot, -2 * flux)
