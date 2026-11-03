"""singularity.matching-steps-4b-4c-join-equation: exact checks (GA, Cl(1,3), (+,-,-,-)).

Local background frame e_t = e0, e_r = e1, e_theta = e2, e_phi = e3; PG field hb^{-1}(a) = a + beta (a.e_t) e_r.
(1) The atom on the radial plane: v = (e0 + e1)/2, v* = (e0 - e1)/2 satisfy the CAR (v^2 = v*^2 = 0,
    v v* + v* v = 1) and sigma = v* v - v v* = e0 e1, sigma^2 = +1. At every sampled r > 0 (beta = 1/3, 1, 2,
    5, horizon included) the physical radial plane span(hb^{-1}(e_t), hb^{-1}(e_r)) has Gram determinant -1,
    signature (1,1), and its physical null directions e_t + (-beta +- 1) e_r map to e0 +- e1: the CAR pair is
    available inside Cl(1,3) with no ascent.
(2) The pair of equations: among the 12 signed unit frame bivectors, S(B) = -2B and B^2 = +1 hold exactly for
    B = +-sigma_r; in the whole eigenspace span(sigma_r, I sigma_r), (a sigma_r + b I sigma_r)^2 =
    (a^2 - b^2) + 2ab I, so B^2 = 1 iff (a, b) = (+-1, 0) (rational grid); the dual has (I sigma_r)^2 = -1.
(3) The flow and the sign: R = ch + sh sigma (ch^2 - sh^2 = 1, Pythagorean-hyperbolic samples) gives
    R v R~ = (ch - sh)^2 v and R v* R~ = (ch + sh)^2 v*, opposite weights with product 1; exchanging
    v <-> v* sends sigma to -sigma (the Z_2 orientation).
(4) At r = 0 the plane degenerates: the weighted limit of beta^{-2} g on the radial plane is
    diag(-1, 0) (computed as the limit of the exact polynomial in 1/beta), rank one with radical R e_r; its
    null cone is the line R e_r, on which the form vanishes identically, so no pair with
    v w + w v = 2 B(v, w) = 1 exists there. The shared direction: k-sharp = hb^T(k) = -sqrt(r) e_r lies in the
    radial plane, is spacelike (Q = -r < 0) at every r > 0 while the atom's legs are null, and tends to 0.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = GA.sig(1, 3)
E0, E1 = GA.gen(0), GA.gen(1)
SIG = GA.mul(E0, E1, S)
I4 = {(0, 1, 2, 3): F(1)}
ISIG = GA.mul(I4, SIG, S)
BIV = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
BETAS = [F(1, 3), F(1), F(2), F(5)]
HYP = [(F(5, 4), F(3, 4)), (F(13, 12), F(5, 12)), (F(17, 15), F(-8, 15))]


def dot(a, b):
    return GA.dot(a, b, S)


def hbinv(a, beta):
    return GA.add(a, GA.scal(beta * dot(a, E0), E1))


def shape(B):
    return GA.scal(F(-1, 2), GA.add(B, GA.scal(3, GA.mul(GA.mul(SIG, B, S), SIG, S))))


def check_atom_on_the_physical_radial_plane():
    premise("singularity.pseudo-inverse-identities-hyperbolic-atom")
    premise("singularity.modular-structure-completed-pair")
    v = GA.scal(F(1, 2), GA.add(E0, E1))
    vs = GA.scal(F(1, 2), GA.sub(E0, E1))
    ok = GA.is_zero(GA.mul(v, v, S)) and GA.is_zero(GA.mul(vs, vs, S))
    ok = ok and GA.eq(GA.add(GA.mul(v, vs, S), GA.mul(vs, v, S)), GA.sc(1))
    ok = ok and GA.eq(GA.sub(GA.mul(vs, v, S), GA.mul(v, vs, S)), SIG) and GA.eq(GA.mul(SIG, SIG, S), GA.sc(1))
    for beta in BETAS:
        pt, pr = hbinv(E0, beta), hbinv(E1, beta)
        G = [[dot(pt, pt), dot(pt, pr)], [dot(pr, pt), dot(pr, pr)]]
        ok = ok and G[0][0] * G[1][1] - G[0][1] * G[1][0] == -1
        ok = ok and GA.congruence_signature(G) == (1, 1, 0)
        for sgn in (1, -1):
            a = GA.add(E0, GA.scal(-beta + sgn, E1))
            img = hbinv(a, beta)
            ok = ok and GA.eq(img, GA.add(E0, GA.scal(sgn, E1))) and dot(img, img) == 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_atom_on_the_physical_radial_plane"; return _tp_rv


def check_eigen_and_square_characterise_sigma():
    premise("singularity.curvature-gauge-field-exact-shape-decoupling")
    sols = []
    for b in BIV:
        for sg in (1, -1):
            B = {b: F(sg)}
            if GA.eq(shape(B), GA.scal(-2, B)) and GA.eq(GA.mul(B, B, S), GA.sc(1)):
                sols.append(B)
    ok = len(sols) == 2 and GA.eq(sols[0], GA.neg(sols[1])) and any(GA.eq(x, SIG) for x in sols)
    ok = ok and GA.eq(GA.mul(ISIG, ISIG, S), GA.sc(-1)) and GA.eq(shape(ISIG), GA.scal(-2, ISIG))
    grid = [F(n, d) for n in range(-3, 4) for d in (1, 2)]
    found = set()
    for a in grid:
        for b in grid:
            B = GA.add(GA.scal(a, SIG), GA.scal(b, ISIG))
            sq = GA.mul(B, B, S)
            ok = ok and GA.eq(sq, GA.add(GA.sc(a * a - b * b), GA.scal(2 * a * b, I4)))
            if GA.eq(sq, GA.sc(1)):
                found.add((a, b))
    _tp_rv = (ok and found == {(F(1), F(0)), (F(-1), F(0))}); assert _tp_rv is not False, "check_eigen_and_square_characterise_sigma"; return _tp_rv


def check_boost_flow_weights_and_orientation():
    premise("singularity.modular-structure-completed-pair")
    v = GA.scal(F(1, 2), GA.add(E0, E1))
    vs = GA.scal(F(1, 2), GA.sub(E0, E1))
    ok = True
    for ch, sh in HYP:
        ok = ok and ch * ch - sh * sh == 1
        R = GA.add(GA.sc(ch), GA.scal(sh, SIG))
        Rt = GA.reverse(R)
        ok = ok and GA.eq(GA.mul(R, Rt, S), GA.sc(1))
        wv, wvs = (ch - sh) ** 2, (ch + sh) ** 2
        ok = ok and GA.eq(GA.mul(GA.mul(R, v, S), Rt, S), GA.scal(wv, v))
        ok = ok and GA.eq(GA.mul(GA.mul(R, vs, S), Rt, S), GA.scal(wvs, vs))
        ok = ok and wv * wvs == 1 and wv != 1
    swapped = GA.sub(GA.mul(v, vs, S), GA.mul(vs, v, S))
    _tp_rv = (ok and GA.eq(swapped, GA.neg(SIG))); assert _tp_rv is not False, "check_boost_flow_weights_and_orientation"; return _tp_rv


def check_degenerate_plane_at_r_zero_and_shared_direction():
    premise("singularity.degeneration-exactly")
    ok = True
    # beta^{-2} g(a, b) on the radial plane, a polynomial in u = 1/beta:
    # g(a,b) = hb^{-1}(a) . hb^{-1}(b); entries for (e_t, e_r)
    def weighted(u):
        beta = 1 / u
        pt, pr = hbinv(E0, beta), hbinv(E1, beta)
        return [[dot(x, y) * u * u for y in (pt, pr)] for x in (pt, pr)]
    # exact polynomial in u: check degree <= 2 by four-point agreement, then evaluate the limit u -> 0
    us = [F(1, 2), F(1, 3), F(1, 5), F(1, 7)]
    vals = [weighted(u) for u in us]
    lim = [[None, None], [None, None]]
    for i in range(2):
        for j in range(2):
            # quadratic through the first three points, confirmed at the fourth, value at u = 0
            (u1, u2, u3), (y1, y2, y3) = us[:3], [vals[t][i][j] for t in range(3)]
            def q(u):
                return (y1 * (u - u2) * (u - u3) / ((u1 - u2) * (u1 - u3)) + y2 * (u - u1) * (u - u3) / ((u2 - u1) * (u2 - u3))
                        + y3 * (u - u1) * (u - u2) / ((u3 - u1) * (u3 - u2)))
            ok = ok and q(us[3]) == vals[3][i][j]
            lim[i][j] = q(F(0))
    ok = ok and lim == [[-1, 0], [0, 0]]
    ok = ok and GA.congruence_signature(lim) == (0, 1, 1)
    # null cone of diag(-1, 0): a^2 (-1) = 0 forces a = 0, the line R e_r, on which the form is zero
    for a, b in [(F(0), F(1)), (F(0), F(-3)), (F(1), F(1)), (F(2), F(1, 2))]:
        Qab = lim[0][0] * a * a + 2 * lim[0][1] * a * b + lim[1][1] * b * b
        ok = ok and ((Qab == 0) == (a == 0))
    ok = ok and all(lim[1][1] * b1 * b2 == 0 for b1 in (F(1), F(-2)) for b2 in (F(3), F(1, 5)))
    # k-sharp = -sqrt(r) e_r: spacelike in the radial plane, tends to 0
    for u in (F(2), F(1), F(1, 3), F(1, 10)):
        r = u * u
        ks = GA.scal(-u, E1)
        ok = ok and dot(ks, ks) == -r and dot(ks, ks) < 0
        ok = ok and not GA.eq(GA.mul(ks, ks, S), GA.sc(0))
    _tp_rv = (ok); assert _tp_rv is not False, "check_degenerate_plane_at_r_zero_and_shared_direction"; return _tp_rv
