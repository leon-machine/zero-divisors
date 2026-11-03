"""synthesis.de-sitter-field-fixes-the-observer-tube-point: exact checks.

Model: Cl(2,4) with the labels of synthesis.wick-rotated-boost-selects-observer-tube-point:
e1 (square +1, time), e2, e3, e4 (square -1), e+ (+1), e- (-1); nO = (e+ + e-)/2, ninf = e+ - e-,
X(x) = nO + x - Q(x) ninf / 2.  The chart boost is K = e1 e2 (twice the stored generator), its
bifurcation plane span(e3, e4).  The de Sitter field of
synthesis.de-sitter-horizon-translation-is-conformal-null-rotation: I = ninf + (L/6) nO,
sigma(x) = <X(x), I> = 1 - L Q(x)/12, hb(a) = sigma a, Omega(a) = -(a ^ grad sigma)/sigma;
W = ninf - (L/6) nO.  A compatible tube point is m = x_perp + i rho u, u = cosh(eta) e1 + sinh(eta) e2,
with Re X(m) = nO + x_perp + (|x_perp|^2 + rho^2) ninf / 2 and Im X(m) = rho u.
Exact rationals throughout (rational boosts by the half-rapidity parameter s:
cosh = (1 + s^2)/(1 - s^2), sinh = 2s/(1 - s^2)).
"""
from fractions import Fraction as F
from itertools import combinations

import GA as g
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)


def vec(*c):
    return {(i,): F(x) for i, x in enumerate(c) if x != 0}


E = [vec(*[1 if j == i else 0 for j in range(6)]) for i in range(6)]
e1, e2, e3, e4, ep, em = E
NO = g.scal(F(1, 2), g.add(ep, em))
NINF = g.sub(ep, em)
K = g.mul(e1, e2, SQ)
BL = list(combinations(range(6), 2))
BIV = [g.mul(E[i], E[j], SQ) for i, j in BL]


def mul(a, b):
    return g.mul(a, b, SQ)


def comm(a, b):
    return g.sub(mul(a, b), mul(b, a))


def ip(a, b):
    return g.dot(a, b, SQ)


def wedge(a, b):
    return g.scal(F(1, 2), comm(a, b))


def dotbv(B, a):
    """Bivector-vector inner product B . a = (Ba - aB)/2."""
    return g.scal(F(1, 2), comm(B, a))


def I_of(L):
    return g.add(NINF, g.scal(F(L) / 6, NO))


def W_of(L):
    return g.sub(NINF, g.scal(F(L) / 6, NO))


def X_of(x):
    return g.add(NO, x, g.scal(-ip(x, x) / 2, NINF))


def sigma(x, L):
    return ip(X_of(x), I_of(L))


def boost_pair(s):
    s = F(s)
    ch = (1 + s * s) / (1 - s * s)
    sh = 2 * s / (1 - s * s)
    u = g.add(g.scal(ch, e1), g.scal(sh, e2))
    w = g.add(g.scal(sh, e1), g.scal(ch, e2))
    return u, w


def tube_parts(x3, x4, rho, s):
    u, _ = boost_pair(s)
    xp = vec(0, 0, x3, x4, 0, 0)
    rho = F(rho)
    re = g.add(NO, xp, g.scal((F(x3) ** 2 + F(x4) ** 2 + rho * rho) / 2, NINF))
    im = g.scal(rho, u)
    return re, im


def cv(x):
    return [x.get((i,), F(0)) for i in range(6)]


def in_span(x, basis):
    return g.rank_of_vectors([cv(b) for b in basis] + [cv(x)]) == g.rank_of_vectors([cv(b) for b in basis])


def fixes(B, re, im):
    """The real Lie algebra element B fixes the complex null line of X = re + i im iff
    [B, X] = c X for a complex c; here [B, im] = 0 for every B used, so this is [B, re] = 0."""
    dre, dim_ = comm(B, re), comm(B, im)
    if not g.is_zero(dim_):
        return False
    return g.is_zero(dre)


def moves(B, re, im):
    """[B, X] is not a complex multiple of X: [B, re] or [B, im] leaves span(re, im)."""
    return not (in_span(comm(B, re), [re, im]) and in_span(comm(B, im), [re, im]))


def symmetry_kernel_dim(I):
    rows = []
    for B in BIV:
        cb = comm(B, K)
        rows.append(cv(comm(B, I)) + [cb.get(t, F(0)) for t in BL])
    return len(BIV) - g.mat_rank(g.frac_matrix(rows))


POS = [12, 3, 48, F(4, 3)]          # rho_L^2 = 12 / L = 1, 4, 1/4, 9
RHO = {12: F(1), 3: F(2), 48: F(1, 2), F(4, 3): F(3)}
RHOS = [F(1, 3), F(1, 2), F(1), F(2), F(3)]
FEET = [(0, 0), (1, 0), (F(1, 2), F(-1, 3))]
BOOSTS = [0, F(1, 3), F(-1, 2)]


def transverse_symmetries(L):
    if L == 0:
        return [mul(e3, e4), mul(e3, NINF), mul(e4, NINF)]
    W = W_of(L)
    return [mul(e3, e4), wedge(e3, W), wedge(e4, W)]


def check_field_symmetries_commuting_with_the_boost():
    """(i): the bivectors commuting with I_L and K are K plus three transverse ones, compact so(3)
    exactly for L > 0 (so(1,2) for L < 0, the transverse Euclidean algebra for L = 0)."""
    premise("synthesis.de-sitter-horizon-translation-is-conformal-null-rotation")
    premise("synthesis.de-sitter-static-boost-frozen-point")
    ok = True
    for L in POS + [0, -12, F(-3, 4)]:
        I = I_of(L)
        ok &= symmetry_kernel_dim(I) == 4
        gens = transverse_symmetries(L)
        for B in gens + [K]:
            ok &= g.is_zero(comm(B, I)) and g.is_zero(comm(B, K))
        ok &= g.rank_of_vectors([[B.get(t, F(0)) for t in BL] for B in gens + [K]]) == 4
        ok &= ip(I, I) == F(L) / 3
        if L != 0:
            W = W_of(L)
            ok &= ip(W, I) == 0 and ip(W, W) == -F(L) / 3
            # closure: [e3W, e4W] is a multiple of e3e4, with sign set by Q(W)
            c = comm(gens[1], gens[2])
            ok &= g.eq(c, g.scal(-2 * ip(W, W), gens[0]))
            # compact (all three transverse directions negative) exactly when L > 0
            ok &= (ip(W, W) < 0) == (L > 0)
    g.check("symmetries of the de Sitter field commuting with the chart boost", ok)
    return ok


def check_fixed_tube_point_is_the_frozen_point():
    """(ii): among compatible tube points, those fixed by the transverse symmetries form the one boost
    orbit x_perp = 0, rho^2 = 12/L, and there Re X(m) is a multiple of I_L."""
    premise("one-relation.spacetime-manifold-vacuum-lines")
    premise("synthesis.wick-rotated-boost-selects-observer-tube-point")
    premise("synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale")
    ok = True
    for L in POS:
        gens = transverse_symmetries(L)
        I = I_of(L)
        for (x3, x4) in FEET:
            for rho in RHOS + [RHO[L]]:
                for s in BOOSTS:
                    re, im = tube_parts(x3, x4, rho, s)
                    fixed = all(fixes(B, re, im) for B in gens)
                    expect = (x3 == 0 and x4 == 0 and rho * rho * F(L) == 12)
                    ok &= fixed == expect
                    if not expect:
                        ok &= any(moves(B, re, im) for B in gens)
                    else:
                        ok &= g.eq(g.scal(F(2) / (rho * rho), re), g.add(NINF, g.scal(F(2) / (rho * rho), NO)))
                        ok &= g.eq(g.scal(F(2) / (rho * rho), re), I)
                    # the boost K never fixes a compatible tube point; it moves it along its orbit
                    ok &= moves(K, re, im)
    g.check("transverse symmetries fix exactly the frozen-point tube orbit", ok)
    return ok


def check_no_fixed_tube_point_for_nonpositive_lambda():
    """(v): for L = 0 and L < 0 no compatible tube point is fixed by the symmetries commuting with K."""
    premise("synthesis.wick-rotated-boost-selects-observer-tube-point")
    premise("synthesis.de-sitter-horizon-translation-is-conformal-null-rotation")
    ok = True
    for L in [0, -12, F(-3, 4)]:
        gens = transverse_symmetries(L)
        for (x3, x4) in FEET:
            for rho in RHOS:
                for s in BOOSTS:
                    re, im = tube_parts(x3, x4, rho, s)
                    ok &= any(moves(B, re, im) for B in gens)
        # Re X(m) is never a multiple of I_L for L <= 0: its wedge with I_L is nonzero
        for (x3, x4) in FEET:
            for rho in RHOS:
                re, _ = tube_parts(x3, x4, rho, 0)
                ok &= not g.is_zero(wedge(re, I_of(L)))
        # at L = 0 the transverse translation alone moves every tube point
        if L == 0:
            for rho in RHOS:
                re, im = tube_parts(0, 0, rho, 0)
                ok &= moves(gens[1], re, im)
    TAB = {0: ({(2,): F(2), (4,): F(1), (5,): F(-1)}, F(1)),
           -12: ({(2,): F(193, 18), (4,): F(2)}, F(-121, 36)),
           F(-3, 4): ({(2,): F(733, 288), (4,): F(17, 16), (5,): F(-15, 16)}, F(419, 576))}
    for L, (vexp, sexp) in TAB.items():
        re, im = tube_parts(F(1, 2), F(-1, 3), 2, F(1, 3))
        ok &= g.eq(comm(transverse_symmetries(L)[1], re), vexp) and ip(re, I_of(L)) == sexp
    g.check("no symmetry-fixed tube point when L <= 0", ok)
    return ok


def norm_N(rho, L):
    """Physical norm of the boost velocity field at the observer x(m) = rho e2: the background
    velocity is x . K-type vector rho e1 with Q = rho^2, physical norm rho / sigma."""
    x = g.scal(rho, e2)
    xi = dotbv(K, x)                      # (e1 e2) . (rho e2) = rho e1 up to sign
    q = ip(xi, xi)
    s = sigma(x, L)
    return q, s


def check_boost_norm_is_maximal_and_equal_to_inverse_surface_gravity_at_the_frozen_point():
    """(iii): N(rho) = rho / sigma(rho e2) satisfies 1 - H N = (1 - H rho/2)^2 / sigma, so N <= 1/H = 1/kappa
    with equality only at rho = 2/H, i.e. rho^2 = 12/L; at rho = 1/H (chart length) N = 4/(5H)."""
    premise("synthesis.de-sitter-static-boost-frozen-point")
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    for H in [F(1), F(2), F(1, 2), F(1, 3)]:
        L = 3 * H * H
        for rho in RHOS + [2 / H, 1 / H]:
            q, s = norm_N(rho, L)
            ok &= q == rho * rho
            ok &= s == 1 + L * rho * rho / 12
            N = rho / s
            ok &= 1 - H * N == (1 - H * rho / 2) ** 2 / s
            ok &= (N == 1 / H) == (rho == 2 / H)
            ok &= N <= 1 / H
        ok &= norm_N(2 / H, L)[1] == 2
        ok &= (1 / H) / norm_N(1 / H, L)[1] == F(4, 5) / H
        ok &= (2 / H) ** 2 * L == 12
    # L = 0: N = rho, unbounded, no extremum
    for rho in RHOS:
        q, s = norm_N(rho, 0)
        ok &= s == 1 and q == rho * rho
    g.check("boost norm maximal, equal to 1/kappa, exactly at rho^2 = 12/L", ok)
    return ok


def check_frozen_point_orbit_is_the_free_fall_orbit():
    """(iv): along x(lam) = rho w(lam) the GTG acceleration dv/dtau + Omega(x').v of the unit physical
    velocity v = u(lam) is (1 - L rho^2/12)/rho w: zero exactly at rho^2 = 12/L, never for L <= 0."""
    premise("synthesis.imported-gtg-dictionary")
    premise("synthesis.de-sitter-horizon-translation-is-conformal-null-rotation")
    ok = True
    for L in POS + [0, -12]:
        for rho in RHOS + ([RHO[L]] if L in RHO else []):
            for s in BOOSTS:
                u, w = boost_pair(s)
                x = g.scal(rho, w)
                sig = sigma(x, L)
                if sig <= 0:
                    continue
                grad_sigma = g.scal(-F(L) / 6, x)      # grad of 1 - L Q(x)/12
                v = u
                ok &= ip(v, v) == 1
                N = rho / sig                            # dtau/dlam
                dv_dtau = g.scal(1 / N, w)               # du/dlam = w
                xdot = g.scal(sig, v)                    # x' = hb(v) = sigma v
                Omega_xdot = g.scal(-1 / sig, wedge(xdot, grad_sigma))
                acc = g.add(dv_dtau, dotbv(Omega_xdot, v))
                expect = g.scal((1 - F(L) * rho * rho / 12) / rho, w)
                ok &= g.eq(acc, expect)
                ok &= g.is_zero(acc) == (F(L) * rho * rho == 12)
    g.check("the frozen-point orbit is the free-fall boost orbit", ok)
    return ok


def check_bifurcation_plane_is_a_round_sphere_with_equator_at_the_frozen_scale():
    """(v): on span(e3, e4) the physical metric sigma^-2 (dy^2 + dz^2), sigma = 1 + L r^2/12, has Gauss
    curvature sigma Lap(sigma) - |grad sigma|^2 = L/3 (central differences are exact on quadratics),
    and the circle of chart radius r has physical radius r/sigma, maximal (the equator) at r^2 = 12/L."""
    premise("synthesis.de-sitter-horizon-translation-is-conformal-null-rotation")
    ok = True
    TAB = {12: [F(1), F(2), F(61, 36), F(59, 25)], 3: [F(1), F(5, 4), F(169, 144), F(67, 50)],
           48: [F(1), F(5), F(34, 9), F(161, 25)], F(4, 3): [F(1), F(10, 9), F(349, 324), F(259, 225)],
           -12: [F(1), F(0), F(11, 36), F(-9, 25)]}
    PTS = [(0, 0), (1, 0), (F(1, 2), F(-2, 3)), (F(3, 5), 1)]
    for L in POS + [-12]:
        ok &= [sigma(vec(0, 0, y, z, 0, 0), L) for (y, z) in PTS] == TAB[L]
        def sg(y, z):
            return sigma(vec(0, 0, y, z, 0, 0), L)
        h = F(1, 7)
        for (y, z) in [(0, 0), (1, 0), (F(1, 2), F(-2, 3)), (F(3, 5), 1)]:
            s0 = sg(y, z)
            dy = (sg(y + h, z) - sg(y - h, z)) / (2 * h)
            dz = (sg(y, z + h) - sg(y, z - h)) / (2 * h)
            lap = (sg(y + h, z) + sg(y - h, z) + sg(y, z + h) + sg(y, z - h) - 4 * s0) / (h * h)
            ok &= s0 == 1 + F(L) * (F(y) ** 2 + F(z) ** 2) / 12
            ok &= s0 * lap - dy * dy - dz * dz == F(L) / 3
        if L > 0:
            r0 = RHO[L]
            for r in RHOS:
                if r != r0:
                    ok &= r / sg(r, 0) < r0 / sg(r0, 0)
            ok &= r0 / sg(r0, 0) * r0 / sg(r0, 0) * L == 3       # physical equator radius = ell = (3/L)^(1/2)
    g.check("bifurcation plane round of curvature L/3, equator at the frozen tube scale", ok)
    return ok


def check_frozen_orbit_is_the_stored_static_observer():
    """(vi): at L = 3 (H = 1) the rotor R = 1 + e2 W fixes I, carries K to e1 W (the stored static boost
    B_L = e1 ^ W of the observer at the origin), and carries the origin worldline t e1 onto the
    K-orbit Q(x) = -12/L = -4, i.e. rho = 2 = rho_L (in the left wedge for this orientation of R)."""
    premise("synthesis.de-sitter-static-boost-frozen-point")
    ok = True
    L = 3
    I, W = I_of(L), W_of(L)
    R = g.add(g.sc(1), mul(e2, W))
    Rr = g.reverse(R)
    ok &= g.eq(mul(R, Rr), g.sc(2))
    ok &= g.eq(mul(mul(R, I), Rr), g.scal(2, I))
    ok &= g.eq(mul(mul(R, K), Rr), g.scal(2, mul(e1, W)))
    ok &= g.eq(mul(mul(e1, W), mul(e1, W)), g.sc(ip(I, I)))
    for t in [0, F(1, 2), 1, F(-3, 2)]:
        X0 = X_of(g.scal(t, e1))
        Y = mul(mul(Rr, X0), R)                  # R^-1 X R up to the factor 2
        lam = ip(Y, NINF)
        P = g.scal(1 / lam, Y)                   # normalised so that <P, ninf> = 1
        x = g.add(*[g.scal(P.get((i,), F(0)), E[i]) for i in range(4)])
        ok &= g.eq(P, X_of(x))
        ok &= x.get((2,), F(0)) == 0 and x.get((3,), F(0)) == 0
        ok &= ip(x, x) == -F(12) / L
    g.check("frozen-point orbit is the stored static observer carried by a field symmetry", ok)
    return ok


def check_stelle_west_vector_at_the_tube_point():
    """(vii): for every compatible m, V(m) = X(m)/sigma(m) - (3/L) I_L with sigma(m) = <X(m), I_L> (real)
    lies in I_L^perp, has Q(V) = -3/L, Re V orthogonal to Im V = Im X(m)/sigma(m); for L > 0, Q(Re V) <= 0,
    so |Im V|^2 = Q(Im V) <= 3/L = l^2, with equality iff Re V = 0 iff m is the fixed tube point, where
    V(m) = i l u.  The conjugate point (rho -> -rho) is fixed by the same symmetries."""
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    premise("synthesis.wick-rotated-boost-selects-observer-tube-point")
    ok = True
    for L in POS:
        I = I_of(L)
        gens = transverse_symmetries(L)
        for (x3, x4) in FEET:
            for rho in RHOS + [RHO[L]]:
                for s in BOOSTS:
                    re, im = tube_parts(x3, x4, rho, s)
                    sg = ip(re, I)
                    ok &= ip(im, I) == 0
                    ok &= sg == 1 + F(L) * (F(x3) ** 2 + F(x4) ** 2 + rho * rho) / 12
                    reV = g.sub(g.scal(1 / sg, re), g.scal(F(3) / L, I))
                    imV = g.scal(1 / sg, im)
                    ok &= ip(reV, I) == 0 and ip(imV, I) == 0 and ip(reV, imV) == 0
                    ok &= ip(reV, reV) - ip(imV, imV) == -F(3) / L
                    ok &= ip(imV, imV) == (rho / sg) ** 2
                    ok &= ip(reV, reV) <= 0
                    at_fixed = (x3 == 0 and x4 == 0 and rho * rho * F(L) == 12)
                    ok &= g.is_zero(reV) == at_fixed
                    ok &= (ip(imV, imV) == F(3) / L) == at_fixed
                    re2, im2 = tube_parts(x3, x4, -rho, s)
                    ok &= all(fixes(B, re2, im2) for B in gens) == at_fixed
                    if at_fixed:
                        u, _ = boost_pair(s)
                        ok &= g.eq(g.scal(L, imV), g.scal(L * rho / 2, u)) and (rho / 2) ** 2 * L == 3
    g.check("Stelle-West vector at the tube point is i l u exactly at the fixed point", ok)
    return ok


def check_scale_of_the_null_pair_moves_rho_and_lambda_together():
    """(viii): the boost R = 1 + t e+e- of the ascent plane (a rescaling of the null pair, the conformal
    dilation) maps I_L to a multiple of I_{s^2 L} and X(m) to a multiple of X(m/s), s = (1+t)/(1-t) up to
    inversion, so rho^2 L is invariant and the fixed tube point goes to the fixed tube point; in the frame
    where I_L is a multiple of e+ (L = 12), the fixed tube point is i e1, the stored structure h_{i e1}."""
    premise("synthesis.positive-structure-is-twistor-form-at-imaginary-time")
    ok = True
    Ed = mul(ep, em)
    for t in [F(1, 3), F(-1, 2), F(2, 5)]:
        R = g.add(g.sc(1), g.scal(t, Ed))
        Rr = g.reverse(R)
        nrm = mul(R, Rr).get((), F(0))
        def act(x):
            return g.scal(1 / nrm, mul(mul(R, x), Rr))
        a0 = act(NO)
        s = ip(a0, NINF)                      # nO -> s nO
        ok &= g.eq(a0, g.scal(s, NO)) and g.eq(act(NINF), g.scal(1 / s, NINF))
        for L in POS:
            ok &= g.eq(act(I_of(L)), g.scal(1 / s, I_of(L * s * s)))
            rho = RHO[L]
            re, im = tube_parts(0, 0, rho, 0)
            re2, im2 = act(re), act(im)
            ok &= g.eq(g.scal(1 / s, re2), tube_parts(0, 0, rho / s, 0)[0])
            ok &= g.eq(g.scal(1 / s, im2), tube_parts(0, 0, rho / s, 0)[1])
            ok &= (rho / s) ** 2 * (L * s * s) == 12
    ok &= g.eq(I_of(12), g.scal(2, ep))
    re, im = tube_parts(0, 0, 1, 0)
    ok &= g.eq(re, ep) and g.eq(im, e1)       # X(i e1) = e+ + i e1
    g.check("rescaling the null pair moves (rho, L) with rho^2 L fixed; balanced frame gives i e1", ok)
    return ok


def check_two_horizon_field_separates_the_candidates():
    """(scope): for the Schwarzschild-de Sitter lapse f(r) = 1 - 2M/r - (L/3) r^2 at L = M = 3/7 the
    horizons are r = 1, 2 and the surface gravities |f'(r_h)|/2 are 2/7 and 5/28, ratio 8/5; at M = 0 the
    single horizon r = (3/L)^(1/2) has kappa^2 = L/3 (the de Sitter value of (iii))."""
    premise("synthesis.de-sitter-static-boost-frozen-point")
    ok = True
    L, M = F(3, 7), F(3, 7)

    def f(r):
        return 1 - 2 * M / r - L * r * r / 3

    def fp(r):
        return 2 * M / (r * r) - 2 * L * r / 3

    ok &= f(F(1)) == 0 and f(F(2)) == 0 and f(F(-3)) == 0
    for r in [F(1, 2), F(3, 2), F(5, 2)]:
        ok &= r * f(r) == -(r - 1) * (r - 2) * (r + 3) / 7
    kb, kc = abs(fp(F(1))) / 2, abs(fp(F(2))) / 2
    ok &= kb == F(2, 7) and kc == F(5, 28) and kb / kc == F(8, 5)
    # de Sitter limit: M = 0, L = 3: horizon r = 1, kappa = 1 = H
    ok &= abs(-2 * F(3) * 1 / 3) / 2 == 1
    g.check("Schwarzschild-de Sitter: two horizons, surface gravities in ratio 8/5", ok)
    return ok
