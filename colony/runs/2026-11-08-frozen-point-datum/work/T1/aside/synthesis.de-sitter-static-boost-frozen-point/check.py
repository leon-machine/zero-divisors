"""synthesis.de-sitter-static-boost-frozen-point: exact checks in Cl(2,4) (GA.py).

Generators: 0 = e_0 (square +1), 1..3 = e_1..e_3 (square -1), 4 = e_+ (+1), 5 = e_- (-1);
n_inf = e_+ + e_-, n_O = (e_+ - e_-)/2, so <n_O, n_inf> = 1. For x = sum x_mu e_mu,
X(x) = n_O + x - Q(x)/2 n_inf, I = n_inf + (Lam/6) n_O, W = n_inf - (Lam/6) n_O, B = e_0 W, and
xi = X . B = (X B - B X)/2. The chart velocity dx is read off xi = dX + a X with
dX = dx - <x, dx> n_inf: a is the n_O coefficient of xi and dx = (vector part of xi) - a x.
  (i)   For eight Lam of both signs and zero: Q(I) = Lam/3, <W, I> = 0, Q(W) = -Lam/3, W = V/Q(V) at
        x = 0 with V = X - (3/Lam) I (Lam != 0), B commutes with I and B^2 = Lam/3.
  (ii)  On the grid of three Lam and five values of each of x_0..x_3: xi is a vector with <X, xi> = 0,
        Q(xi) = (1 + Lam Q(x)/12)^2 - (Lam/3) x_0^2 = Q(dx), the n_inf coefficient matches dX, and
        dx = -(1 + Lam Q(x)/12) e_0 + (Lam/6) x_0 x. (Q(xi) has degree <= 2 in Lam and <= 4 in each
        coordinate, so the grid determines the identity.) On x = r e_1 (six radii, four Lam):
        sigma = <X, I> = 1 + Lam r^2/12, R = r/sigma and Q(xi)/sigma^2 = 1 - (Lam/3) R^2.
  (iii) At Lam = 3H^2, H = 1, 2, 1/3: f(R) = 1 - Lam R^2/3 vanishes at R_h = 1/H, kappa = |f'(R_h)|/2 = H
        (Fact singularity.imported-surface-gravity-redshifted-acceleration), kappa^2 = B^2 = Q(I);
        u = e_0 W/H has u^2 = +1 and B = H u. On the bifurcation sphere x_0 = 0, Q(x) = -12/Lam
        (r = 2/H, three directions): dx = 0, sigma = 2, R = R_h; the Jacobian of dx (central
        differences, exact for a quadratic) is [[0, H], [H, 0]] on the (x_0, r) plane and zero on
        the sphere directions. The other zeros x = +-(2/H) e_0 have sigma = 0.
  (iv)  Lam = 0: B = e_0 n_inf != 0, B^2 = 0, dx = -e_0 everywhere (no zero), and the flow of xi, the rotor
        e^{-tB/2} = 1 - (t/2) B, sends X(x) to X(x - t e_0) (the time translation). Lam < 0: B^2 = Lam/3 < 0 and B/H' squares to
        -1 at Lam = -3H'^2 (a rotation); f(R) = 1 + |Lam| R^2/3 >= 1 and dx has no zero on the grid.
  (v)   In the reversed form (squares negated, signature (4,2)): Q(I) = -Lam/3, Q(e_0) = -1,
        Q(W) = +Lam/3, while B^2 = Lam/3 is unchanged.
The Euclidean-period clause is the premise's analytic argument and is not checked here.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)                 # signature (2,4) in the generator order above
SQ_REV = tuple(-s for s in SQ)
E0 = GA.gen(0)
EP, EM = GA.gen(4), GA.gen(5)
NINF = GA.add(EP, EM)
NO = GA.scal(F(1, 2), GA.sub(EP, EM))
LAMS = [F(3), F(-3), F(12), F(6, 5), F(-1, 3), F(0), F(27), F(-12)]
GRID_LAM = [F(3), F(-6, 5), F(1, 2)]
GRID_X = [F(-2), F(-1), F(0), F(1, 2), F(3)]
RADII = [F(0), F(1, 3), F(1), F(2), F(5, 2), F(7)]
HS = [F(1), F(2), F(1, 3)]
DIRS = [[1, 0, 0], [F(3, 5), F(4, 5), 0], [0, F(5, 13), F(12, 13)]]
# (iv) samples. Lam = 0: flow times t and two points for the time translation, and the 3^4 = 81 grid
# points where dx = -e_0. Lam = -3 H'^2 < 0 at two H', with dx tested on points (a, b, 0, 0) and
# (a, 0, b, b) for a, b on the grid.
FLOW_TIMES = [F(1), F(-2), F(1, 3)]
FLOW_POINTS = [[F(1), F(2), F(0), F(-1)], [F(0), F(0), F(3), F(1, 2)]]
LAMBDA0_POINTS = [list(x) for x in product(GRID_X[:3], repeat=4)]
NEG_HS = [F(1), F(2, 3)]
NEG_POINTS = ([[a, b, F(0), F(0)] for a, b in product(GRID_X, repeat=2)]
              + [[a, F(0), b, b] for a, b in product(GRID_X, repeat=2)])


def vec4(x):
    return GA.add(*[GA.scal(x[i], GA.gen(i)) for i in range(4) if x[i]]) if any(x) else {}


def Q4(x):
    return x[0] * x[0] - x[1] * x[1] - x[2] * x[2] - x[3] * x[3]


def Xof(x):
    return GA.add(NO, vec4(x), GA.scal(-Q4(x) / 2, NINF))


def frozen(lam):
    return GA.add(NINF, GA.scal(lam / 6, NO)), GA.sub(NINF, GA.scal(lam / 6, NO))


def dotv(a, b, sq=SQ):
    return GA.dot(a, b, sq)


def xi_of(x, lam):
    I, W = frozen(lam)
    B = GA.mul(E0, W, SQ)
    X = Xof(x)
    return GA.scal(F(1, 2), GA.sub(GA.mul(X, B, SQ), GA.mul(B, X, SQ))), X, B


def velocity(x, lam):
    xi, X, B = xi_of(x, lam)
    a = dotv(xi, NINF)                      # n_O coefficient, since <n_O, n_inf> = 1
    dx = [xi.get((i,), F(0)) - a * x[i] for i in range(4)]
    return dx, xi, a


def check_stabiliser_and_square():
    premise("mass.de-sitter-scale-frozen-point")
    premise("dark-energy.stelle-west-vector-frozen-point")
    ok = dotv(NO, NINF) == 1 and dotv(NO, NO) == 0 and dotv(NINF, NINF) == 0
    for lam in LAMS:
        I, W = frozen(lam)
        ok = ok and dotv(I, I) == lam / 3 and dotv(W, I) == 0 and dotv(W, W) == -lam / 3
        B = GA.mul(E0, W, SQ)
        ok = ok and GA.commutes(B, I, SQ) and GA.eq(GA.mul(B, B, SQ), GA.sc(lam / 3))
        if lam != 0:
            V = GA.sub(Xof([0, 0, 0, 0]), GA.scal(3 / lam, I))
            ok = ok and dotv(V, V) == -3 / lam and GA.eq(GA.scal(1 / dotv(V, V), V), W)
    GA.check("I = n_inf + (Lam/6) n_O, W = V/Q(V): B = e_0 W commutes with I and B^2 = Q(I) = Lam/3", ok)
    return ok


def check_killing_field_norm_and_chart_velocity():
    premise("mass.de-sitter-scale-frozen-point")
    ok = True
    for lam in GRID_LAM:
        for x in product(GRID_X, repeat=4):
            x = list(x)
            dx, xi, a = velocity(x, lam)
            X = Xof(x)
            ok = ok and all(len(b) == 1 for b in xi) and dotv(X, xi) == 0
            Qx = Q4(x)
            want = (1 + lam * Qx / 12) ** 2 - lam / 3 * x[0] * x[0]
            ok = ok and dotv(xi, xi) == want and Q4(dx) == want
            # the n_inf coefficient of xi equals that of dX + a X: -<x, dx> - a Q(x)/2
            xdx = x[0] * dx[0] - x[1] * dx[1] - x[2] * dx[2] - x[3] * dx[3]
            ok = ok and dotv(xi, NO) == -xdx - a * Qx / 2
            formula = [-(1 + lam * Qx / 12) * (1 if i == 0 else 0) + lam / 6 * x[0] * x[i] for i in range(4)]
            ok = ok and dx == formula
    GA.check("Q(xi) = (1 + Lam Q(x)/12)^2 - (Lam/3) x_0^2 = Q(dx) on the 3 x 5^4 grid; dx as stated", ok)
    return ok


def check_static_slice_norm():
    premise("mass.de-sitter-scale-frozen-point")
    ok = True
    skipped = 0
    for lam in LAMS[:4]:
        I, W = frozen(lam)
        for r in RADII:
            x = [F(0), r, F(0), F(0)]
            xi, X, B = xi_of(x, lam)
            sigma = dotv(X, I)
            ok = ok and sigma == 1 + lam * r * r / 12
            if sigma == 0:
                skipped += 1
                continue
            R = r / sigma
            ok = ok and dotv(xi, xi) / (sigma * sigma) == 1 - lam / 3 * R * R
    ok = ok and skipped == 1                       # Lam = -3, r = 2: sigma = 0, outside the chart
    GA.check("on x = r e_1: sigma = 1 + Lam r^2/12 and g(xi, xi) = 1 - (Lam/3) R^2 with R = r/sigma", ok)
    return ok


def check_horizon_surface_gravity_and_bifurcation_sphere():
    premise("singularity.imported-surface-gravity-redshifted-acceleration")
    ok = True
    for H in HS:
        lam = 3 * H * H
        I, W = frozen(lam)
        Rh = 1 / H
        ok = ok and 1 - lam * Rh * Rh / 3 == 0
        kappa = abs(-2 * lam * Rh / 3) / 2
        ok = ok and kappa == H and kappa * kappa == dotv(I, I)
        B = GA.mul(E0, W, SQ)
        ok = ok and GA.eq(GA.mul(B, B, SQ), GA.sc(kappa * kappa))
        u = GA.scal(1 / H, B)
        ok = ok and GA.eq(GA.mul(u, u, SQ), GA.sc(1)) and dotv(GA.scal(1 / H, W), GA.scal(1 / H, W)) == -1
        r = 2 / H
        for d in DIRS:
            x = [F(0)] + [r * F(c) for c in d]
            ok = ok and Q4(x) == -12 / lam
            dx, xi, a = velocity(x, lam)
            ok = ok and dx == [0, 0, 0, 0]
            sigma = dotv(Xof(x), I)
            ok = ok and sigma == 2 and r / sigma == Rh
        # Jacobian at x = r e_1 on (x_0, x_1) and the sphere directions x_2, x_3
        x = [F(0), r, F(0), F(0)]
        J = []
        for j in range(4):
            xp, xm = list(x), list(x)
            xp[j] += 1
            xm[j] -= 1
            vp, vm = velocity(xp, lam)[0], velocity(xm, lam)[0]
            J.append([(vp[i] - vm[i]) / 2 for i in range(4)])
        ok = ok and [[J[0][0], J[1][0]], [J[0][1], J[1][1]]] == [[0, H], [H, 0]]
        ok = ok and all(J[j][i] == 0 for j in (2, 3) for i in range(4))
        ok = ok and all(J[j][i] == 0 for j in (0, 1) for i in (2, 3))
        for s in (1, -1):
            x = [s * 2 / H, F(0), F(0), F(0)]
            ok = ok and velocity(x, lam)[0] == [0, 0, 0, 0] and dotv(Xof(x), I) == 0
    GA.check("Lam = 3H^2: kappa = H, kappa^2 = B^2; dx = 0 on Q(x) = -12/Lam with Jacobian [[0,H],[H,0]]", ok)
    return ok


def check_zero_and_negative_lambda():
    ok = True
    I, W = frozen(F(0))
    B0 = GA.mul(E0, W, SQ)
    ok = ok and GA.eq(B0, GA.mul(E0, NINF, SQ)) and not GA.is_zero(B0) and GA.is_zero(GA.mul(B0, B0, SQ))
    for t in FLOW_TIMES:
        R = GA.sub(GA.sc(1), GA.scal(t / 2, B0))          # e^{-tB/2}, the flow of xi = X . B
        Rt = GA.reverse(R)
        ok = ok and GA.eq(GA.mul(R, Rt, SQ), GA.sc(1))
        for x in FLOW_POINTS:
            moved = GA.mul(GA.mul(R, Xof(x), SQ), Rt, SQ)
            ok = ok and GA.eq(moved, Xof([x[0] - t, x[1], x[2], x[3]]))
    ok = ok and len(LAMBDA0_POINTS) == 81
    for x in LAMBDA0_POINTS:
        ok = ok and velocity(x, F(0))[0] == [-1, 0, 0, 0]
    for Hp in NEG_HS:
        lam = -3 * Hp * Hp
        I, W = frozen(lam)
        B = GA.mul(E0, W, SQ)
        # B^2 = Lam/3 = -H'^2 < 0, and f(R) = 1 - Lam R^2/3 = 1 + H'^2 R^2 >= 1 (exact, by hand)
        ok = ok and GA.eq(GA.mul(B, B, SQ), GA.sc(lam / 3)) and GA.eq(GA.mul(B, B, SQ), GA.sc(-Hp * Hp))
        u = GA.scal(1 / Hp, B)
        ok = ok and GA.eq(GA.mul(u, u, SQ), GA.sc(-1))
        ok = ok and all(1 - lam * R * R / 3 == 1 + Hp * Hp * R * R for R in RADII)
        for xx in NEG_POINTS:
            dx, _xi, _a = velocity(xx, lam)
            ok = ok and any(dx)                              # dx has a nonzero component
    GA.check("Lam = 0: B nilpotent, the time translation X(x) -> X(x - t e_0); Lam < 0: a rotation, no horizon", ok)
    return ok


def check_reversal_of_the_ambient_form():
    ok = True
    for lam in LAMS:
        I, W = frozen(lam)
        ok = ok and dotv(I, I, SQ_REV) == -lam / 3 and dotv(E0, E0, SQ_REV) == -1
        ok = ok and dotv(W, W, SQ_REV) == lam / 3
        B = GA.mul(E0, W, SQ_REV)
        ok = ok and GA.eq(GA.mul(B, B, SQ_REV), GA.sc(lam / 3))
    GA.check("under Q -> -Q, Q(I) changes sign and B^2 = Lam/3 does not", ok)
    return ok
