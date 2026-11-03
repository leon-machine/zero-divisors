"""Theorem (HS): the Hadamard scaling limit on the generators of local Rindler horizons. Exact checks of the
identities the assembled chain rests on.

(1) The canonical projector of a null k (Lam = e0 k / (2 k.e0) = n k / 2 with the Hermitian partner n, n.k = 1):
    Lam^2 = Lam, Lam k = 0, k Lam = k, Lam p k = 2 (p.k) Lam and (k.e0) Lam p e0 Lam = (p.k) Lam for every vector p
    (the projector identity behind the coefficient of the null singularity, the flux trace and the step
    coefficient), and the null flux of the Dirac current J = psi e0 psi~ is 2 (k.e0) |Lam psi|^2 (the integrand of
    the flux contraction).
(2) The null-hypersurface identity Delta^(1/2)/sqrt(det M) = (a(u) a(u'))^(-1/2) on one exact model: the future
    light cone of a point of the flat field (Delta = 1), with expansion theta = 2/u, generators labelled by a
    rational stereographic chart. M is the Hessian of -sigma in the label offset, computed exactly from the
    Synge function sigma = Q(x - x')/2 by truncated power series; a^2 is the determinant of the induced metric of
    the cut. Checked: sigma has no constant or linear term in the offset (the generators are null and lie in the
    hypersurface), (det M)^2 = det G(u) det G(u') at several (u, u', y'), and a(u) = u^2 a(1), so theta = 2/u and the
    step and log coefficient (d_u + theta/2)(a(u) a(u'))^(-1/2) vanishes.
(3) The time-function dependence of the epsilon-regularised restriction and generator scaling: on the flat null
    plane with t(u) = u + c u^2, t_u/(t(u) - t(u')) - 1/(u - u') = c/(1 + c(u + u')) = d_u log phi_t,
    phi_t = (t(u) - t(u'))/(u - u'), a bounded smooth kernel; lambda times it at (u0 + lambda x, u0 + lambda x')
    tends to zero (scaling degree at most 0), while lambda W0(u0 + lambda x, u0 + lambda x') = W0(x, x') (the null
    vacuum is dilation invariant).
Exact arithmetic only (Fractions; GA). The analytic content (the bounds, the limits, the flux contraction, the
Morse reduction) is in the premises' proofs.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S4 = (1, -1, -1, -1)
E = [GA.gen(i) for i in range(4)]

BOUND = "synthesis.restricted-dirac-hadamard-parametrix-on-a-null-hypersurface-is-the-null-vacuum-plus-a-bounded-kernel"
FLUX = "synthesis.dirac-states-restrict-to-null-hypersurfaces-through-the-flux-contraction-and-are-thin-layer-limits-under-the-generator-car"
GCAR = "synthesis.dirac-causal-propagator-between-nearby-null-leaves-tends-to-the-generator-car-on-every-geodesic-null-hypersurface"
NULLSING = "synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces"
BULK = "synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field"
FLATPLANE = "synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes"
DIMOCK = "synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field"
MICRO = "synthesis.imported-microlocal-hadamard-condition"
HFORM = "synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard"
PARAM = "synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport"


def mul(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, S4)
    return out


def vec(c):
    return GA.add(*[GA.scal(F(ci), E[i]) for i, ci in enumerate(c)])


def dag(x):
    return mul(E[0], GA.reverse(x), E[0])


def spinor(c):
    blades = [(), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2, 3)]
    return GA.add(*[{b: F(ci)} for b, ci in zip(blades, c) if ci != 0])


# future null directions e0 + rhat, rhat a rational unit vector
NULLS = ((1, 0, 0, 1), (1, F(2, 3), F(2, 3), F(1, 3)), (1, F(-3, 5), 0, F(4, 5)), (3, 2, -2, 1))
REGS = ((1, 0, 0, 0), (2, 1, -1, F(1, 2)), (0, 1, 3, -2), (F(5, 2), F(1, 3), 2, 4))
SPINORS = ((2, F(1, 3), 0, F(5, 7), 3, 0, -1, F(1, 2)), (-1, 4, F(2, 5), -3, 0, F(7, 3), 1, 2))
PINNED_PROJ = [F(1, 2), F(3, 4), F(1), F(-3, 4), F(36565, 1764), F(13966, 225), F(1, 2), F(11, 12), F(-1), F(-7, 36),
               F(3789, 196), F(11026, 225), F(1, 2), F(11, 10), F(11, 10), F(-1, 4), F(170729, 8820), F(2294, 45),
               F(3, 2), F(3, 4), F(3), F(41, 12), F(8679, 196), F(12266, 75)]
# per null k: (k.e0) <Lam p e0 Lam>_0 = (p.k)/2 for the four regulators, then the null flux of the two spinors
PINNED_DETM = [F(6718464, 5764801), F(576480100, 7890481), F(51380224, 635796225)]
PINNED_TKERNEL = [F(6, 43), F(5, 46), F(2, 15), F(3, 227), F(3, 2297), F(3, 22997)]


def check_projector_identity_and_null_flux_of_the_dirac_current():
    premise(GCAR)
    premise(FLUX)
    premise(NULLSING)
    premise(FLATPLANE)
    premise(DIMOCK)
    ok = True
    vals = []
    for kc in NULLS:
        k = vec(kc)
        ke0 = GA.dot(k, E[0], S4)
        ok &= GA.dot(k, k, S4) == 0
        # Hermitian partner n with n.k = 1, and the projector Lam = n k / 2 = e0 k / (2 k.e0)
        n = GA.scal(F(1) / (2 * ke0 * ke0), GA.sub(GA.scal(2 * ke0, E[0]), k))
        L = GA.scal(F(1, 2), mul(n, k))
        ok &= GA.dot(n, n, S4) == 0 and GA.dot(n, k, S4) == 1
        ok &= GA.eq(L, GA.scal(F(1) / (2 * ke0), mul(E[0], k)))
        ok &= GA.eq(mul(L, L), L) and GA.eq(dag(L), L)
        ok &= GA.is_zero(mul(L, k)) and GA.eq(mul(k, L), k)
        for rc in REGS:
            p = vec(rc)
            pk = GA.dot(p, k, S4)
            ok &= GA.eq(mul(L, p, k), GA.scal(2 * pk, L))
            ok &= GA.eq(GA.scal(ke0, mul(L, p, E[0], L)), GA.scal(pk, L))
            vals.append(ke0 * mul(L, p, E[0], L).get((), F(0)))
        for c in SPINORS:
            psi = spinor(c)
            J = mul(psi, E[0], GA.reverse(psi))
            lp = mul(L, psi)
            ok &= GA.dot(J, k, S4) == 2 * ke0 * mul(dag(lp), lp).get((), F(0))
            vals.append(GA.dot(J, k, S4))
    ok &= vals == PINNED_PROJ
    GA.check("canonical projector: Lam^2 = Lam, Lam k = 0, k Lam = k, Lam p k = 2 (p.k) Lam, "
             "(k.e0) Lam p e0 Lam = (p.k) Lam; null flux of the Dirac current = 2 (k.e0) |Lam psi|^2", ok)
    return ok


# --- truncated power series in the label offset (eta1, eta2), total degree <= 2 ---------------------------

DEG = 2


def s_const(c):
    return {(0, 0): F(c)}


def s_add(*xs):
    out = {}
    for x in xs:
        for m, c in x.items():
            out[m] = out.get(m, F(0)) + c
    return {m: c for m, c in out.items() if c != 0}


def s_scal(c, x):
    return {m: c * v for m, v in x.items() if c * v != 0}


def s_mul(x, y):
    out = {}
    for (a, b), c in x.items():
        for (d, e), f in y.items():
            if a + b + d + e <= DEG:
                out[(a + d, b + e)] = out.get((a + d, b + e), F(0)) + c * f
    return {m: c for m, c in out.items() if c != 0}


def s_inv(x):
    """1/x for x with nonzero constant term, truncated at degree DEG"""
    c0 = x[(0, 0)]
    rest = s_scal(F(-1) / c0, {m: c for m, c in x.items() if m != (0, 0)})
    out, term = s_const(1), s_const(1)
    for _ in range(DEG):
        term = s_mul(term, rest)
        out = s_add(out, term)
    return s_scal(F(1) / c0, out)


def cone_point(u, yp):
    """X(u, y' + eta) = u (e0 + nhat(y)), nhat the inverse stereographic chart, as four series"""
    y1 = s_add(s_const(yp[0]), {(1, 0): F(1)})
    y2 = s_add(s_const(yp[1]), {(0, 1): F(1)})
    r2 = s_add(s_mul(y1, y1), s_mul(y2, y2))
    inv = s_inv(s_add(s_const(1), r2))
    nh = [s_mul(s_add(s_const(1), s_scal(F(-1), r2)), inv), s_scal(F(2), s_mul(y1, inv)), s_scal(F(2), s_mul(y2, inv))]
    return [s_const(u)] + [s_scal(F(u), c) for c in nh]


def light_cone_data(u, up, yp):
    X = cone_point(u, yp)
    Xp = [x.get((0, 0), F(0)) for x in cone_point(up, yp)]
    d = [s_add(X[i], s_const(-Xp[i])) for i in range(4)]
    sig = s_scal(F(1, 2), s_add(*[s_scal(F(S4[i]), s_mul(d[i], d[i])) for i in range(4)]))
    low = [sig.get(m, F(0)) for m in ((0, 0), (1, 0), (0, 1))]
    M = [[-2 * sig.get((2, 0), F(0)), -sig.get((1, 1), F(0))],
         [-sig.get((1, 1), F(0)), -2 * sig.get((0, 2), F(0))]]
    return low, M


def induced_det(u, yp):
    X = cone_point(u, yp)
    dX = [[X[mu].get(m, F(0)) for mu in range(4)] for m in ((1, 0), (0, 1))]
    G = [[-sum(S4[mu] * dX[i][mu] * dX[j][mu] for mu in range(4)) for j in range(2)] for i in range(2)]
    return G[0][0] * G[1][1] - G[0][1] * G[1][0]


def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def check_null_hypersurface_identity_on_the_light_cone():
    premise(NULLSING)
    premise(BOUND)
    premise(GCAR)
    ok = True
    dets = []
    samples = ((F(3, 2), F(1, 3), (F(1, 2), F(-1, 3))), (F(2), F(5, 4), (F(0), F(2, 7))),
               (F(1, 5), F(7, 3), (F(-3, 4), F(1))))
    for u, up, yp in samples:
        low, M = light_cone_data(u, up, yp)
        ok &= low == [0, 0, 0]
        dM = det2(M)
        ok &= dM > 0
        # Delta = 1 on the flat field: Delta / det M = 1/(a a')  <=>  (det M)^2 = det G(u) det G(u')
        ok &= dM * dM == induced_det(u, yp) * induced_det(up, yp)
        # area density a(u) = u^2 a(1): theta = a'/a = 2/u, so (d_u + theta/2)(a(u) a(u'))^(-1/2) = 0
        ok &= induced_det(u, yp) == u ** 4 * induced_det(F(1), yp)
        dets.append(dM)
    ok &= dets == PINNED_DETM
    GA.check("light cone of a point: sigma = -(1/2) M(eta, eta) + O(eta^3), (det M)^2 = a(u)^2 a(u')^2 "
             "(Delta^(1/2)/sqrt(det M) = (a a')^(-1/2)), a(u) = u^2 a(1) so the step coefficient vanishes", ok)
    return ok


def check_time_function_kernel_is_bounded_and_scales_away():
    premise(BOUND)
    premise(GCAR)
    premise(BULK)
    premise(MICRO)
    premise(HFORM)
    premise(PARAM)
    ok = True
    c = F(1, 7)
    vals = []
    pairs = ((F(1, 2), F(-1, 3)), (F(2), F(1, 5)), (F(-1, 4), F(3, 4)))
    for u, up in pairs:
        t, tp, tu = u + c * u * u, up + c * up * up, 1 + 2 * c * u
        lhs = tu / (t - tp) - 1 / (u - up)
        phi_u = 1 + c * (u + up)          # phi_t = (t(u) - t(u'))/(u - u'), and d_u log phi_t = c / phi_t
        ok &= (t - tp) == (u - up) * phi_u
        ok &= lhs == c / phi_u
        # bounded on |u|, |u'| <= 2: |c / phi| <= c / (1 - 4 c)
        ok &= abs(lhs) <= c / (1 - 4 * c)
        vals.append(lhs)
    # generator scaling at u0: lambda W0(u0 + lambda x, u0 + lambda x') = W0(x, x'); lambda k -> 0 for the kernel k
    u0, x, xp = F(1, 3), F(1), F(-2)
    prev = None
    for lam in (F(1, 10), F(1, 100), F(1, 1000)):
        w = lam / ((u0 + lam * x) - (u0 + lam * xp))
        ok &= w == 1 / (x - xp)
        sk = lam * c / (1 + c * (2 * u0 + lam * (x + xp)))
        ok &= sk <= lam * c / (1 - 4 * c)
        if prev is not None:
            ok &= sk < prev
        prev = sk
        vals.append(sk)
    ok &= vals == PINNED_TKERNEL
    GA.check("epsilon-regularised restriction on the flat null plane with t = u + c u^2: the time-function kernel "
             "t_u/(t(u) - t(u')) - 1/(u - u') = c/(1 + c(u + u')) is bounded and scales away; W0 is dilation invariant", ok)
    return ok
