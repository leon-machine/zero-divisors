"""synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching: exact checks.

Diagonal Kasner approach d tau^2 - sum tau^(2p_j)(dx^j)^2, sum p = 1, momentum along a principal axis with p < 1,
q = 1 - p, s = k tau^q / q; a mode of Bessel order nu (stored order formula) is Z(s) with
Z'' + Z'/s + (1 - nu^2/s^2) Z = 0.
(1) check_exit_direction: s is strictly increasing in tau (ds/dtau = k tau^(-p) > 0), sampled exactly at
    tau = t^d with d the denominator of q, so tau^q is rational: the ratio of the axis' wavelength to the Hubble
    length 1/theta = tau (theta = sum p / tau) is 1/(q s) and falls only as tau falls; control: sum p != 1 changes
    the expansion rate.
(2) check_liouville_and_adiabaticity: Z = s^(-1/2) u maps the order-nu equation to
    u'' + (1 + (1/4 - nu^2)/s^2) u = 0 (monomial identity with exponents in Q); with a = 1/4 - nu^2,
    omega^2 = 1 + a/s^2 and the adiabatic parameter eps^2 = (omega'/omega^2)^2 = a^2/(s^2 + a)^3, which is
    1/a >= 4 at the wall for 0 < a <= 1/4 and decreasing in s, with eps^2 = 1 exactly at s^2 = a^(2/3) - a
    (sampled at cubes a); for nu^2 > 1/4, omega^2 < 0 for s^2 < nu^2 - 1/4; nu = 1/2 gives omega^2 = 1.
(3) check_wall_curvature: the curvature two-forms recomputed from the coframe (Cartan); Kretschmann K tau^4 = 4 sum (p_i(p_i - 1))^2 + 4 sum_{i<j} (p_i p_j)^2 from the
    stored frame components R^{i0} = p_i(p_i - 1)/tau^2, R^{ij} = -p_i p_j/tau^2; equals the stored
    -16 p1 p2 p3 on the 4D vacuum circle (64/27 at the Schwarzschild exponents); K > 0 at every sampled
    stored Kasner point (BKL, Schwarzschild, the isotropic disk point, the 5D end (1/2,1/2,1/2,-1/2), generic
    5D vacuum points) and K = 0 exactly at the flat Milne points (1,0,0) and (0,0,0,1); at the latter the hidden
    scale b = tau collapses at the wall.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def check_exit_direction():
    premise("synthesis.kasner-approach-gives-horizon-exit-and-index-three")
    ok, n = True, 0
    k = F(3)
    for p in (F(-1, 3), F(2, 3), F(1, 3), F(0), F(1, 2), F(-2, 7), F(6, 7)):
        q = 1 - p
        d = q.denominator
        prev = None
        for r in (F(1, 4), F(1, 2), F(1), F(3, 2), F(5)):
            tau = r ** d                                   # tau^q = r^(q.numerator)
            tq = r ** q.numerator
            s = k * tq / q
            ratio = 1 / (q * s)                            # wavelength / Hubble length, theta = 1/tau
            ok = ok and ratio * k * tq == 1 and tq ** d == tau ** q.numerator   # (tau^p/k)/tau = 1/(k tau^q)
            if prev is not None:
                ok = ok and s > prev[0] and ratio < prev[1]
            prev = (s, ratio)
            n += 1
    # expansion rate theta = (sum p)/tau = 1/tau for sum p = 1; control: sum p = 3/2 gives 3/(2 tau)
    ok = ok and sum((F(1, 3),) * 3) == 1 and sum((F(1, 2),) * 3) != 1
    GA.check("s increases with tau; wavelength/Hubble falls only toward the wall (%d samples)" % n, ok and n == 35)
    assert ok and n == 35


def mono_add(*xs):
    out = {}
    for x in xs:
        for e, c in x.items():
            out[e] = out.get(e, 0) + c
            if out[e] == 0:
                del out[e]
    return out


def mono_d(x):
    return {e - 1: c * e for e, c in x.items() if e != 0}


def mono_shift(x, de, c=1):
    return {e + de: v * c for e, v in x.items() if v * c != 0}


def check_liouville_and_adiabaticity():
    premise("synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling")
    premise("synthesis.imported-bessel-reduction-and-small-argument-hankel-forms")
    ok = True
    for nu2 in (F(0), F(1, 4), F(9, 16), F(2), F(1, 9)):
        for m in (F(0), F(1), F(5, 2), F(-3, 4), F(7)):
            u = {m: F(1)}
            Z = mono_shift(u, F(-1, 2))
            lhs = mono_add(mono_d(mono_d(Z)), mono_shift(mono_d(Z), -1), Z, mono_shift(Z, -2, -nu2))
            rhs_in = mono_add(mono_d(mono_d(u)), u, mono_shift(u, -2, F(1, 4) - nu2))
            ok = ok and lhs == mono_shift(rhs_in, F(-1, 2))
    # control: the wrong Liouville weight s^(+1/2) fails
    u = {F(2): F(1)}
    Zb = mono_shift(u, F(1, 2))
    lhsb = mono_add(mono_d(mono_d(Zb)), mono_shift(mono_d(Zb), -1), Zb)
    ctrl = lhsb != mono_shift(mono_add(mono_d(mono_d(u)), u, mono_shift(u, -2, F(1, 4))), F(1, 2))
    GA.check("Liouville form u'' + (1 + (1/4 - nu^2)/s^2) u = 0", ok)
    GA.check("control: wrong Liouville weight fails", ctrl)
    ok2 = True
    for a in (F(1, 4), F(1, 8), F(1, 27), F(8, 125)):
        eps2_wall = a * a / a ** 3
        ok2 = ok2 and eps2_wall == 1 / a and eps2_wall >= 4
        cube = {F(1, 8): F(1, 2), F(1, 27): F(1, 3), F(8, 125): F(2, 5)}
        if a in cube:
            s2 = cube[a] ** 2 - a                           # a^(2/3) - a
            ok2 = ok2 and s2 > 0 and a * a / (s2 + a) ** 3 == 1
        last = None
        for s2 in (F(0), F(1, 100), F(1, 10), F(1, 2), F(2)):
            e2 = a * a / (s2 + a) ** 3
            if last is not None:
                ok2 = ok2 and e2 < last
            last = e2
    for nu2 in (F(9, 16), F(1), F(4)):
        a = F(1, 4) - nu2
        ok2 = ok2 and all(1 + a / s2 < 0 for s2 in (F(1, 100), (nu2 - F(1, 4)) / 2))
    ok2 = ok2 and 1 + (F(1, 4) - F(1, 4)) / F(1, 3) == 1
    # hand values: wall values 1/a, crossing points s^2 = a^(2/3) - a, a non-oscillating omega^2
    walls = {a: a * a / a ** 3 for a in (F(1, 4), F(1, 8), F(1, 27), F(8, 125))}
    ok2 = ok2 and walls == {F(1, 4): 4, F(1, 8): 8, F(1, 27): 27, F(8, 125): F(125, 8)}
    ok2 = ok2 and [r * r - a for a, r in ((F(1, 8), F(1, 2)), (F(1, 27), F(1, 3)), (F(8, 125), F(2, 5)))] \
        == [F(1, 8), F(2, 27), F(12, 125)]
    ok2 = ok2 and 1 + (F(1, 4) - F(9, 16)) / F(1, 100) == F(-121, 4)
    # hand values of the Liouville form: coefficient of s^(m - 5/2) is m(m - 1) + 1/4 - nu^2
    for nu2, m, want in ((F(0), F(2), F(9, 4)), (F(2), F(5, 2), F(2)), (F(9, 16), F(1), F(-5, 16))):
        u = {m: F(1)}
        Z = mono_shift(u, F(-1, 2))
        lhs = mono_add(mono_d(mono_d(Z)), mono_shift(mono_d(Z), -1), Z, mono_shift(Z, -2, -nu2))
        ok2 = ok2 and lhs.get(m - F(5, 2), 0) == want and lhs.get(m - F(1, 2), 0) == 1
    GA.check("adiabatic parameter at the wall 1/a >= 4; non-oscillatory for nu > 1/2; exact at nu = 1/2", ok2)
    assert ok and ctrl and ok2


def curvature_from_coframe(p):
    """Recompute the frame curvature of e^0 = d tau, e^i = tau^(p_i) dx^i from Cartan's equations.
    Coefficients are kept as (c, n) meaning c tau^n. omega^i_0 = p_i tau^(p_i - 1) dx^i; with eta = diag(1, -1, ...)
    omega^0_j = -eta_00 eta^jj ... = omega^j_0. R^i_0 = d omega^i_0 (no omega^i_k omega^k_0 term, omega^i_k = 0);
    R^i_j = omega^i_0 ^ omega^0_j. Returns ({i: coefficient of e^0 ^ e^i}, {(i, j): coefficient of e^i ^ e^j}) for
    R^{i0} and R^{ij} (indices raised with eta), each times tau^2."""
    eta0, etas = 1, -1
    r0, rij = {}, {}
    for i, pi in enumerate(p):
        c, n = pi, pi - 1                       # omega^i_0 = c tau^n dx^i
        dc, dn = c * n, n - 1                   # d omega^i_0 = dc tau^dn d tau ^ dx^i
        # e^0 ^ e^i = tau^(p_i) d tau ^ dx^i ; R^i_0 coefficient, then R^{i0} = R^i_0 eta^00
        coef, expo = dc, dn - pi
        assert expo == -2
        r0[i] = coef * eta0
    for i, pi in enumerate(p):
        for j, pj in enumerate(p):
            if i < j:
                c = pi * pj * (-eta0 * etas)       # omega^i_0 ^ omega^0_j with omega^0_j = -eta^00 eta_jj omega^j_0
                expo = (pi - 1) + (pj - 1) - (pi + pj)
                assert expo == -2
                rij[(i, j)] = c * etas             # raise j with eta^jj
    return r0, rij


def kretschmann_tau4(p):
    t = sum((x * (x - 1)) ** 2 for x in p)
    t2 = sum((p[i] * p[j]) ** 2 for i in range(len(p)) for j in range(i + 1, len(p)))
    return 4 * t + 4 * t2


def bkl(u):
    d = 1 + u + u * u
    return (-u / d, (1 + u) / d, u * (1 + u) / d)


def check_wall_curvature():
    premise("dark-energy.frozen-point-datum-kasner-wall")
    premise("synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall")
    ok = True
    for u in (F(1), F(2), F(7, 3), F(11, 2)):
        p = bkl(u)
        ok = ok and kretschmann_tau4(p) == -16 * p[0] * p[1] * p[2] and kretschmann_tau4(p) > 0
    ok = ok and kretschmann_tau4((F(-1, 3), F(2, 3), F(2, 3))) == F(64, 27)
    # the curvature two-forms recomputed from the coframe agree with the stored forms, and give K
    for P in ((F(-1, 3), F(2, 3), F(2, 3)), (F(1, 3),) * 3, (F(1, 5), F(2, 5), F(4, 5), F(-2, 5)), bkl(F(7, 3))):
        r0, rij = curvature_from_coframe(P)
        ok = ok and all(r0[i] == P[i] * (P[i] - 1) for i in range(len(P)))
        ok = ok and all(v == -P[i] * P[j] for (i, j), v in rij.items())
        ok = ok and 4 * sum(v * v for v in r0.values()) + 4 * sum(v * v for v in rij.values()) == kretschmann_tau4(P)
    r0, rij = curvature_from_coframe((F(-1, 3), F(2, 3), F(2, 3)))
    ok = ok and r0 == {0: F(4, 9), 1: F(-2, 9), 2: F(-2, 9)} and rij[(1, 2)] == F(-4, 9)
    sing = [(F(1, 3),) * 3, (F(1, 2), F(1, 2), F(1, 2), F(-1, 2)), (F(1, 5), F(2, 5), F(4, 5), F(-2, 5)),
            (F(-2, 7), F(3, 7), F(6, 7), F(0))]
    for P in sing:
        ok = ok and sum(P) == 1 and kretschmann_tau4(P) > 0
    flat = [(F(1), F(0), F(0)), (F(0), F(0), F(0), F(1))]
    for P in flat:
        ok = ok and sum(P) == 1 and sum(x * x for x in P) == 1 and kretschmann_tau4(P) == 0
    # at (0,0,0,1) the hidden scale is b = tau^1: it collapses at the wall; the 4D reduction is (1/3,1/3,1/3)
    P = flat[1]
    ph, k = P[3], 1 + P[3] / 2
    pe = tuple((x + ph / 2) / k for x in P[:3])
    ok = ok and ph == 1 and pe == (F(1, 3),) * 3
    GA.check("Kretschmann > 0 at stored Kasner points; = 0 only at the flat Milne points", ok)
    # control: a sign slip in the pair term breaks agreement with -16 p1 p2 p3
    p = bkl(F(2))
    ctrl = 4 * sum((x * (x - 1)) ** 2 for x in p) - 4 * sum((p[i] * p[j]) ** 2 for i in range(3)
                                                           for j in range(i + 1, 3)) != -16 * p[0] * p[1] * p[2]
    GA.check("control: wrong pair sign fails", ctrl)
    assert ok and ctrl
