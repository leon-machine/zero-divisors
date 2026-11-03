"""The generator field of the Dirac field on a null hypersurface: flux contraction, thin layers, regulator
independence. Exact checks.

(1) The Dirac current J = psi e0 psi~ is future causal (J.J = alpha^2 + beta^2 with psi psi~ = alpha + I beta,
    J.e0 > 0, J.N >= 0 on sampled future causal N), and its flux along a null k (any null direction, not only
    e0 + e3) is 2 (k.e0) <(Lam psi)^dag Lam psi>, depending on Lam psi only, Lam = e0 k / (2 k.e0) the
    Hermitian projector: the integrand of the flux contraction.
(2) Generator scaling is conjugation by a unitary dilation: for polynomial kernels and test functions the
    scaled pairing lambda <phi, w(u0 + lambda ., u0 + lambda .) chi> equals <phi_l, w chi_l> with
    phi_l(u) = lambda^(-1/2) phi((u - u0)/lambda), and |phi_l| = |phi| (lambda a rational square); so a
    bounded restricted kernel stays bounded under scaling (scaling degree at most one).
(3) Thin layers on the flat null plane: the compressed anticommutator smeared with layers rho_n(v) F has
    symbol (1/2)|rho_n^(p_-)|^2 |F^|^2 on both shells, any mass (shell density 1/2 from the exact Jacobian
    d^3p/(2 p0) = dp_+ d^2p_perp/(2 |p_+|) and Lam (p +- m) e0 Lam = (p.k) Lam), with
    rho_n^(q) = n^2/(n^2 + q^2) <= 1 (the transform of the two-sided exponential, an example of the only properties
    used: |rho_n^| <= 1 and rho_n^ -> 1 pointwise, true for every positive approximate identity); the defect
    1 - rho_n^(p_-)^2 tends to zero at every shell point, below 2 p_-^2/n^2: the layer limit is the generator CAR.
(4) The projector identity: for the Hermitian projector of any null k, Lam p e0 Lam (k.e0) = (p.k) Lam for every
    vector p (at k.e0 = 1 the stored flat-plane identity), so for a complex time-function regulator the coefficient of
    the null singularity does not depend on the regulator direction. The comparison with a real thin-layer
    displacement is argued in the proof, not checked.
Exact arithmetic only (Fractions; GA).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S4 = (1, -1, -1, -1)
E = [GA.gen(i) for i in range(4)]
I4 = GA.mul(GA.mul(E[0], E[1], S4), GA.mul(E[2], E[3], S4), S4)


def mul(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, S4)
    return out


def vec(c):
    return GA.add(*[GA.scal(F(ci), E[i]) for i, ci in enumerate(c)])


def dag(x):
    return mul(E[0], GA.reverse(x), E[0])


def lam_of(k):
    return GA.scal(1 / (2 * GA.dot(k, E[0], S4)), mul(E[0], k))


def spinor(c):
    """even multivector from 8 rational coefficients"""
    blades = [(), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2, 3)]
    return GA.add(*[{b: F(ci)} for b, ci in zip(blades, c) if ci != 0])


SPINORS = ((2, F(1, 3), 0, F(5, 7), 3, 0, -1, F(1, 2)),
           (-1, 4, F(2, 5), -3, 0, F(7, 3), 1, 2),
           (F(1, 4), 0, -2, 1, F(-3, 2), 5, F(2, 9), -1))
# future null directions e0 + rhat with rational unit rhat (Pythagorean quadruples)
NULLS = ((1, 0, 0, 1), (1, F(2, 3), F(2, 3), F(1, 3)), (1, F(3, 5), F(4, 5), 0), (1, F(-2, 7), F(3, 7), F(-6, 7)),
         (3, 2, 2, 1))
TIMELIKE = ((1, 0, 0, 0), (2, 1, -1, F(1, 2)), (5, 3, 0, -4), (F(3, 2), 0, F(1, 2), 1))


PINNED_SCALED = [F(3201, 10240), F(9025883, 70858800), F(85212776, 926485875)]
PINNED_REG = [F(1, 2), F(3, 4), F(1, 2), F(1), F(1, 2), F(1, 2), F(1, 2), F(11, 12), F(1, 3), F(-1), F(19, 18),
              F(1, 2), F(1, 2), F(11, 10), F(1, 4), F(-3, 2), F(8, 5), F(1, 2), F(1, 2), F(11, 7), F(1, 28),
              F(-19, 14), F(23, 6), F(1, 2), F(3, 2), F(11, 4), F(1), F(-3), F(19, 6), F(1, 2)]
# (k.e0) Lam p e0 Lam has scalar part (p.k)/2: one entry per regulator (five fixed, then the Hermitian partner n)


def check_dirac_current_is_future_causal_and_its_null_flux_is_canonical():
    premise("synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field")
    premise("synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces")
    ok = True
    fluxes = []
    for c in SPINORS:
        psi = spinor(c)
        pp = mul(psi, GA.reverse(psi))
        alpha, beta = pp.get((), F(0)), pp.get((0, 1, 2, 3), F(0))
        ok &= set(pp) <= {(), (0, 1, 2, 3)}
        J = mul(psi, E[0], GA.reverse(psi))
        ok &= set(len(b) for b in J) <= {1}
        ok &= GA.dot(J, J, S4) == alpha ** 2 + beta ** 2
        ok &= GA.dot(J, E[0], S4) == mul(dag(psi), psi).get((), F(0)) and GA.dot(J, E[0], S4) > 0
        for t in TIMELIKE:
            ok &= GA.dot(J, vec(t), S4) > 0
        for kc in NULLS:
            k = vec(kc)
            ok &= GA.dot(k, k, S4) == 0
            L = lam_of(k)
            ok &= GA.eq(mul(L, L), L) and GA.eq(dag(L), L) and GA.is_zero(mul(L, k))
            lp = mul(L, psi)
            fl = GA.dot(J, k, S4)
            ok &= fl >= 0
            ok &= fl == 2 * GA.dot(k, E[0], S4) * mul(dag(lp), lp).get((), F(0))
            ok &= fl == GA.dot(mul(lp, E[0], GA.reverse(lp)), k, S4)
            fluxes.append(fl)
    # the canonical frame of the stored results: k = e0 + e3, flux = 2 |Lam psi|^2 (pinned value)
    ok &= fluxes[0] == F(36565, 1764)
    GA.check("Dirac current future causal (J.J = alpha^2 + beta^2, J.N > 0 on timelike N); null flux = 2 (k.e0) |Lam psi|^2, depends on Lam psi only", ok)
    return ok


def binom(n, r):
    out = 1
    for t in range(r):
        out = out * (n - t) // (t + 1)
    return out


def pint(p, a, b):
    """integral of polynomial p (coefficient list) over [a, b]"""
    return sum(c * (b ** (i + 1) - a ** (i + 1)) / (i + 1) for i, c in enumerate(p))


def peval(p, x):
    return sum(c * x ** i for i, c in enumerate(p))


def check_generator_scaling_is_conjugation_by_a_unitary_dilation():
    premise("synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state")
    ok = True
    u0 = F(2, 5)
    phi = [F(1), F(-3), F(2)]          # test functions on [0, 1]
    chi = [F(2), F(1, 2), F(0), F(-1)]
    # polynomial kernel w(u, u') = sum c_ij u^i u'^j
    w = {(0, 0): F(3), (1, 0): F(-1), (0, 2): F(5), (2, 1): F(7, 3), (1, 1): F(-2)}
    vals = []
    for root in (F(1, 2), F(1, 3), F(2, 7)):
        lam = root ** 2
        # left side: lambda * int int phi(x) w(u0 + lam x, u0 + lam y) chi(y) dx dy over [0,1]^2
        lhs = F(0)
        rhs = F(0)
        for (i, j), c in w.items():
            # expand (u0 + lam x)^i as polynomial in x
            px = [F(0)] * (i + 1)
            for a in range(i + 1):
                px[a] = F(binom(i, a)) * u0 ** (i - a) * lam ** a
            py = [F(0)] * (j + 1)
            for a in range(j + 1):
                py[a] = F(binom(j, a)) * u0 ** (j - a) * lam ** a
            fx = [F(0)] * (len(px) + len(phi))
            for a, ca in enumerate(px):
                for b, cb in enumerate(phi):
                    fx[a + b] += ca * cb
            fy = [F(0)] * (len(py) + len(chi))
            for a, ca in enumerate(py):
                for b, cb in enumerate(chi):
                    fy[a + b] += ca * cb
            lhs += lam * c * pint(fx, F(0), F(1)) * pint(fy, F(0), F(1))
            # right side: int int phi_l(u) u^i u'^j chi_l(u') du du', phi_l(u) = lam^(-1/2) phi((u - u0)/lam),
            # on [u0, u0 + lam]; substitute u = u0 + lam x: du = lam dx, so each leg gives lam^(1/2) int ...
            legx = (1 / root) * lam * pint(fx, F(0), F(1))
            legy = (1 / root) * lam * pint(fy, F(0), F(1))
            rhs += c * legx * legy
        ok &= lhs == rhs
        vals.append(lhs)
        # the dilation is unitary: |phi_l|^2 = |phi|^2
        sq = [F(0)] * (2 * len(phi))
        for a, ca in enumerate(phi):
            for b, cb in enumerate(phi):
                sq[a + b] += ca * cb
        ok &= (1 / root) ** 2 * lam * pint(sq, F(0), F(1)) == pint(sq, F(0), F(1))
        # weight 1 per leg instead of 1/2 is not unitary
        ok &= (1 / lam) ** 2 * lam * pint(sq, F(0), F(1)) != pint(sq, F(0), F(1))
    ok &= pint([F(1), F(-3), F(2)], F(0), F(1)) == F(1, 6)
    ok &= vals == PINNED_SCALED
    GA.check("generator scaling is conjugation by the unitary dilation at weight 1/2: scaled kernels of a bounded restricted kernel stay bounded", ok)
    return ok


def shell_point(pp, p1, p2, m, sign):
    """on-shell momentum with p.k = pp (k = e0 + e3), transverse (p1, p2), mass m; sign = +1 positive energy"""
    s = p1 * p1 + p2 * p2 + m * m
    p0 = (pp + s / pp) / 2
    p3 = (s / pp - pp) / 2
    return vec((p0, p1, p2, p3)), s


def check_thin_layers_on_the_flat_null_plane_converge_to_the_generator_car():
    premise("synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes")
    premise("synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field")
    ok = True
    k = GA.add(E[0], E[3])
    L = lam_of(k)
    pts = ((F(3), F(1), F(-2), F(0)), (F(1, 2), F(2), F(1), F(1)), (F(-2), F(1, 3), F(0), F(2)), (F(-1, 4), F(-1), F(3), F(0)))
    defects = {}
    for (pp, p1, p2, m) in pts:
        p, s = shell_point(pp, p1, p2, m, 1)
        ok &= GA.dot(p, p, S4) == m * m
        ok &= GA.dot(p, k, S4) == pp
        p0 = p.get((0,), F(0))
        # Jacobian of the light-front parametrisation: d p3 / d pp = - p0 / pp, so d^3p/(2|p0|) = dpp d^2p/(2|pp|)
        h = F(1, 10 ** 6)
        pph = pp + h
        p3a = (s / pp - pp) / 2
        p3b = (s / pph - pph) / 2
        exact = -F(1, 2) * (1 + s / (pp * pph))  # difference quotient of p3, exact
        ok &= (p3b - p3a) / h == exact
        ok &= -F(1, 2) * (1 + s / (pp * pp)) == -p0 / pp     # its limit: d p3 / d pp = - p0 / pp
        # compressed numerator: Lam (p +- m) e0 Lam = (p.k) Lam, so density (1/(2|p0|)) |dp3/dpp| |p.k| = 1/2
        for sgn in (1, -1):
            num = mul(L, GA.add(p, GA.sc(sgn * m)), E[0], L)
            ok &= GA.eq(num, GA.scal(pp, L))
        dens = (1 / (2 * abs(p0))) * abs(p0 / pp) * abs(pp)
        ok &= dens == F(1, 2)
        # layer factor: rho_n^(q) = n^2/(n^2 + q^2) at q = p.nv, nv = (e0 - e3)/2 the layer direction
        q = GA.dot(p, GA.scal(F(1, 2), GA.sub(E[0], E[3])), S4)
        ok &= q == s / (2 * pp)
        dl = []
        for n in (10, 100, 1000):
            r = F(n * n, n * n + q * q)
            ok &= 0 < r <= 1
            d = 1 - r * r
            ok &= 0 <= d <= 2 * q * q / (n * n)
            dl.append(d)
        ok &= dl[0] > dl[1] > dl[2]
        defects[(pp, p1, p2, m)] = dl[0]
    ok &= defects[(F(3), F(1), F(-2), F(0))] == 1 - F(100, 100 + F(25, 36)) ** 2
    GA.check("thin layers on the flat null plane: shell density 1/2 on both shells, any mass; layer defect 1 - rho_n^2 -> 0 below 2 p_-^2/n^2", ok)
    return ok


def check_regulator_direction_drops_out_of_the_null_singularity_coefficient():
    premise("synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes")
    premise("synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces")
    premise("synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport")
    ok = True
    coeffs = []
    regs = ((1, 0, 0, 0), (2, 1, -1, F(1, 2)), (F(1, 2), 0, 0, F(-1, 2)), (0, 1, 3, -2), (5, F(1, 3), 2, 4))
    for kc in NULLS:
        k = vec(kc)
        L = lam_of(k)
        ke0 = GA.dot(k, E[0], S4)
        # the Hermitian partner n with n.k = 1: n = (2 (k.e0) e0 - k)/(2 (k.e0)^2); Lam = n k / 2
        n = GA.scal(1 / (2 * ke0 * ke0), GA.sub(GA.scal(2 * ke0, E[0]), k))
        ok &= GA.dot(n, n, S4) == 0 and GA.dot(n, k, S4) == 1
        ok &= GA.eq(GA.scal(F(1, 2), mul(n, k)), L)
        for rc in regs + ((n.get((0,), F(0)), n.get((1,), F(0)), n.get((2,), F(0)), n.get((3,), F(0))),):
            p = vec(rc)
            ok &= GA.eq(GA.scal(ke0, mul(L, p, E[0], L)), GA.scal(GA.dot(p, k, S4), L))
            coeffs.append(ke0 * mul(L, p, E[0], L).get((), F(0)))
        # e0 Lam = k / (2 k.e0): the right projector turns e0 into the null direction
        ok &= GA.eq(mul(E[0], L), GA.scal(1 / (2 * ke0), k))
    ok &= coeffs == PINNED_REG
    GA.check("projector identity: Lam p e0 Lam (k.e0) = (p.k) Lam for every vector p and every null k", ok)
    return ok
