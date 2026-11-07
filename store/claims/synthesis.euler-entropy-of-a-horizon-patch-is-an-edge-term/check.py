"""The Euler part of the series' Wald density on a horizon cut is an edge transport angle: exact checks.

Units G = 1. alpha = -3/(4 Lambda) is the Euler coefficient of the series' Lagrangian; the Jacobson-Myers
density of a cut is 1/4 + (alpha/2) R_Sigma = 1/4 + alpha K, K the Gauss curvature of the cut.
(1) Cut geometry. Cuts with the rotationally symmetric induced metric ds^2 + rho(s)^2 dphi^2, rho a
    polynomial (four profiles). K is computed from the metric through its Christoffel symbols (GA.RF in s);
    the rotation-gauge field of the cut in the tangent frame (d_s, d_phi/rho) is read off the structure
    equations de^A = -omega^A_B ^ e^B; then d omega^{23} = K e^2 ^ e^3 identically (the two-dimensional
    transgression), so the Euler entropy alpha int_P K dA of a patch is the edge integral alpha oint omega^{23}
    whenever the frame is smooth on P (rectangles away from the poles); on a polar cap the edge integral
    falls short by exactly 2 pi (index 1 of the frame at the pole); on closed cuts int K dA = 4 pi = 2 pi chi
    for every profile.
(1b) Edge term. The geodesic curvature k_g of the circles s = const, computed from the Christoffel symbols
    (meridians are geodesics), gives int_P K dA + oint k_g ds + sum of corner turns = 2 pi chi(P) on rectangles
    (chi = 1, four right corners), polar caps (chi = 1) and annuli (chi = 0): with the edge term the Euler
    part of every patch is 2 pi alpha chi(P). On closed profiles the frames smooth on the two caps,
    omega_N = (1 - rho') dphi and omega_S = (-1 - rho') dphi, differ on every separating circle by winding
    2 = chi(S^2) (clutching), and the two cap integrals of K are their edge integrals.
(2) Gauge. Under a rotation of the tangent frame by theta (rational: cos = (1 - t^2)/(1 + t^2),
    sin = 2t/(1 + t^2), t a polynomial in s), omega'^{23} = omega^{23} - d theta with d theta = 2 t'/(1 + t^2) ds:
    the edge term is unchanged for theta smooth on P and shifts by -2 pi w for winding w around the edge.
(3) Schwarzschild-de Sitter radial generators: K = (1 - f)/r^2 = 2M/r^3 + Lambda/3; the Jacobson-Myers
    density -3M/(2 Lambda r^3) varies along the generator, the density with the edge counterterm subtracted is
    1/4 at every point, so Delta S = 0 = delta Q there; the unsubtracted change is the stored
    -(3M/2 Lambda)(r0^-3 - r1^-3).
(4) Closed cuts: the edge counterterm leaves 2 pi alpha chi = -3 pi chi/(2 Lambda), the stored closed-cut
    shift (-3 pi/Lambda on spheres), which is -chi/2 times the de Sitter entropy 3 pi/Lambda.
(5) The wall counterterm one dimension up: Q(omega) of dark-energy.wall-counterterm has first-order gauge
    variation delta_lambda Q = d<lambda, d omega> (<X, Y> = eps_abcd X^ab ^ Y^cd, delta omega = D lambda) on a
    generic polynomial so(1,3) connection; for lambda the binormal n = e0 ^ e1 of a cut, <n, d omega> =
    4 d omega^{23}; and in a frame adapted to the cut x0 = x1 = 0, R^{23} - d omega^{23} pulled back is
    -(b_2 ^ a_3 + a_2 ^ b_3), a_A = omega^{A0} - omega^{A1} the k-extrinsic and b_A = (omega^{A0} + omega^{A1})/2
    the l-extrinsic forms, so it vanishes on admissible cuts (a = 0) and not otherwise.
Exact arithmetic only (Fractions, GA.RF); no randomness: the samples are fixed tables.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

LAMBDAS = [F(3), F(1, 2), F(-3, 7)]


# ---------------------------------------------------------------- one-variable helpers (GA.RF in s)
S = GA.RF.var()


def rc(x):
    return GA.RF.const(F(x))


def poly_rf(coeffs):
    out = GA.RF0
    p = GA.RF1
    for c in coeffs:
        out = out + rc(c) * p
        p = p * S
    return out


def poly_int(coeffs, a, b):
    """int_a^b of sum c_i s^i, exact."""
    return sum(F(c) * (F(b) ** (i + 1) - F(a) ** (i + 1)) / (i + 1) for i, c in enumerate(coeffs))


def poly_d(coeffs):
    return [i * F(c) for i, c in enumerate(coeffs)][1:] or [F(0)]


def poly_mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += F(x) * F(y)
    return out


def poly_val(coeffs, x):
    return sum(F(c) * F(x) ** i for i, c in enumerate(coeffs))


# profiles rho(s): open profiles (rho(0) = 0, rho'(0) = 1) and closed ones on [0, L] (rho(L) = 0, rho'(L) = -1)
def closed_profile(L, c):
    base = poly_mul([0, 1], [F(L), -1])                     # s (L - s)
    base = [x / F(L) for x in base]
    return poly_mul(base, poly_mul([1], [1, F(c) * F(L), -F(c)]))   # times 1 + c s (L - s)


OPEN = [[0, 1, F(1, 3), F(-1, 5)], [0, 1, 0, F(-1, 6), 0, F(1, 120)]]
CLOSED = [(F(2), F(0)), (F(7, 3), F(1, 4)), (F(5), F(-1, 40))]

RECTS = [(F(1, 4), F(1, 2)), (F(1, 3), F(9, 10))]
CAPS = [F(1, 5), F(2, 3)]
INTERIOR = [F(k, 7) for k in range(1, 7)]
ROTATIONS = [[F(1, 3), 1], [0, F(1, 2), F(-1, 7)], [2, 0, 0, F(1, 9)]]
WINDINGS = [1, -2, 3]
HOLES = [(F(1, 10), F(1, 2), F(1)), (F(1, 20), F(3, 10), F(3, 2)), (F(1, 7), F(1, 9), F(2))]
SIGNS = (1, -1)
LAMS0 = [F(-1, 10), F(-1, 50)]


def gauss_curvature_from_metric(rho):
    """K of ds^2 + rho^2 dphi^2 from the Christoffel symbols and the Riemann tensor (coordinates s, phi)."""
    r = poly_rf(rho)
    g = [[GA.RF1, GA.RF0], [GA.RF0, r * r]]
    gi = [[GA.RF1, GA.RF0], [GA.RF0, GA.RF1 / (r * r)]]
    dg = lambda i, j, k: g[i][j].deriv() if k == 0 else GA.RF0      # d_k g_ij (nothing depends on phi)
    Gam = [[[GA.RF0] * 2 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                acc = GA.RF0
                for l in range(2):
                    acc = acc + gi[i][l] * (dg(l, k, j) + dg(l, j, k) - dg(j, k, l))
                Gam[i][j][k] = acc / rc(2)
    d = lambda f, k: f.deriv() if k == 0 else GA.RF0
    # R^i_{jkl} = d_k Gam^i_{lj} - d_l Gam^i_{kj} + Gam^i_{km} Gam^m_{lj} - Gam^i_{lm} Gam^m_{kj}
    i, j, k, l = 0, 1, 0, 1
    Rup = d(Gam[i][l][j], k) - d(Gam[i][k][j], l)
    for m in range(2):
        Rup = Rup + Gam[i][k][m] * Gam[m][l][j] - Gam[i][l][m] * Gam[m][k][j]
    R_sphisphi = g[0][0] * Rup
    return R_sphisphi / (g[0][0] * g[1][1])


def cut_connection(rho):
    """omega^{23} = A ds + B dphi from de^A = -omega^A_B ^ e^B with e^2 = ds, e^3 = rho dphi.
    de^2 = 0 = -omega^{23} ^ rho dphi gives A = 0; de^3 = rho' ds^dphi = omega^{23} ^ ds = -B ds^dphi gives B."""
    r = poly_rf(rho)
    A = GA.RF0
    B = GA.RF0 - r.deriv()
    # verify the structure equations componentwise (coefficient of ds^dphi)
    de2, de3 = GA.RF0, r.deriv()
    rhs2 = GA.RF0 - A * r          # -(A ds + B dphi) ^ (rho dphi) = -A rho ds^dphi
    rhs3 = GA.RF0 - B              # (A ds + B dphi) ^ ds = -B ds^dphi
    assert de2.eqrf(rhs2) and de3.eqrf(rhs3)
    return A, B


def check_euler_density_is_the_cut_transgression():
    premise("synthesis.euler-term-horizon-entropy-shift")
    premise("synthesis.imported-wald-noether-charge-entropy")
    premise("synthesis.imported-gtg-dictionary")
    for rho in OPEN + [closed_profile(L, c) for (L, c) in CLOSED]:
        K = gauss_curvature_from_metric(rho)
        A, B = cut_connection(rho)
        r = poly_rf(rho)
        # d omega^{23} = (dB/ds) ds^dphi (A = 0, nothing depends on phi); K e^2^e^3 = K rho ds^dphi
        assert B.deriv().eqrf(K * r)
        assert not K.is_zero()
        # patch [s1, s2] x [0, phi0] with the frame smooth on it: area integral = edge integral (units 2 pi phi0)
        drho = poly_d(rho)
        for (s1, s2) in RECTS:
            area = poly_int([-x for x in poly_d(drho)], s1, s2)          # int K rho ds = int -rho'' ds
            edge = -poly_val(drho, s2) + poly_val(drho, s1)              # oint omega^{23} / phi0
            assert area == edge
        # polar cap s < s0: the edge integral falls short by exactly one turn (index 1 at the pole)
        for s0 in CAPS:
            cap = poly_int([-x for x in poly_d(drho)], 0, s0)            # per unit phi; times 2 pi
            edge = -poly_val(drho, s0)
            assert cap - edge == 1 == poly_val(drho, 0)
    for (L, c) in CLOSED:
        rho = closed_profile(L, c)
        assert poly_val(rho, 0) == 0 == poly_val(rho, L)
        assert all(poly_val(rho, x * L) > 0 for x in INTERIOR)
        total = poly_int([-x for x in poly_d(poly_d(rho))], 0, L)        # int K dA / (2 pi)
        assert total == 2                                                 # = chi(S^2): 4 pi in all


def geodesic_curvature_of_circle(rho, inward_sign):
    """k_g of the circle s = const, w.r.t. the unit normal inward_sign * d_s, from the Christoffel symbols:
    T = d_phi/rho, nabla_T T = Gamma^s_{phi phi}/rho^2 d_s (+ a d_phi part that vanishes), k_g = g(nabla_T T, N).
    Also returns Gamma^s_{ss}, Gamma^phi_{ss} (meridians are geodesics)."""
    r = poly_rf(rho)
    g_pp = r * r
    Gs_pp = GA.RF0 - g_pp.deriv() / rc(2)                 # Gamma^s_{phi phi} = -1/2 d_s g_{phi phi}
    Gp_ss = GA.RF0                                        # Gamma^phi_{ss} = 0 (g_{ss} = 1 is constant)
    Gs_ss = GA.RF0                                        # Gamma^s_{ss} = 1/2 d_s g_{ss} = 0
    Gp_pp = GA.RF0                                        # Gamma^phi_{phi phi} = 1/2 g^{phi phi} d_phi g_{phi phi} = 0
    assert Gp_pp.is_zero()
    return rc(inward_sign) * Gs_pp / g_pp, Gs_ss, Gp_ss


def check_edge_term_makes_patch_euler_entropy_topological():
    premise("synthesis.euler-term-horizon-entropy-shift")
    premise("synthesis.euler-entropy-first-order-rate-on-local-patches")
    for rho in OPEN + [closed_profile(L, c) for (L, c) in CLOSED]:
        drho = poly_d(rho)
        r = poly_rf(rho)
        for s in [F(1, 7), F(2, 5)]:
            kg, Gss, Gpss = geodesic_curvature_of_circle(rho, 1)
            assert Gss.is_zero() and Gpss.is_zero()
            assert kg.eval(s) == -poly_val(drho, s) / poly_val(rho, s)
        # in units of 2 pi (angles) and per unit 2 pi of phi-extent where the edge runs along a circle
        k_in = lambda s, sg: geodesic_curvature_of_circle(rho, sg)[0].eval(s) * poly_val(rho, s)   # k_g x length / phi
        area = lambda a, b: poly_int([-x for x in poly_d(drho)], a, b)                            # int K dA / phi
        # rectangle [s1, s2] x [0, phi0]: meridian edges geodesic, four right corners (total turn 1)
        for (s1, s2) in [(F(1, 4), F(1, 2)), (F(1, 3), F(9, 10))]:
            assert area(s1, s2) + k_in(s1, 1) + k_in(s2, -1) == 0      # coefficient of phi0
            corners = 4 * F(1, 4)
            assert corners == 1                                          # chi(disk) = 1 turn
        # polar cap s < s0 (no corners): K-integral + edge = 1 turn = chi(disk)
        for s0 in [F(1, 5), F(2, 3)]:
            assert area(0, s0) + k_in(s0, -1) == 1
        # annulus s1 < s < s2 (chi = 0)
        assert area(F(1, 5), F(3, 5)) + k_in(F(1, 5), 1) + k_in(F(3, 5), -1) == 0
    # so with the edge term the Euler part of every patch is alpha 2 pi chi(P): its coefficient of pi
    for Lam in LAMBDAS:
        alpha = F(-3) / (4 * Lam)
        assert 2 * alpha * 1 == F(-3, 2) / Lam          # disk patch: -3 pi/(2 Lambda), independent of the patch
        assert 2 * alpha * 0 == 0                       # annular patch


def check_clutching_winding_is_the_euler_number():
    premise("dark-energy.wall-counterterm")
    premise("synthesis.euler-term-horizon-entropy-shift")
    for (L, c) in CLOSED:
        rho = closed_profile(L, c)
        drho = poly_d(rho)
        assert poly_val(drho, 0) == 1 and poly_val(drho, L) == -1
        # smooth frames on the two caps: rotate the polar frame by -phi near s = 0 and by +phi near s = L;
        # omega_N = (1 - rho') dphi and omega_S = (-1 - rho') dphi vanish at their poles (smooth there)
        oN = lambda s: 1 - poly_val(drho, s)
        oS = lambda s: -1 - poly_val(drho, s)
        assert oN(0) == 0 and oS(L) == 0
        for eq in [L / 3, L / 2, 3 * L / 4]:
            north = poly_int([-x for x in poly_d(drho)], 0, eq)          # int K dA / 2 pi over the north cap
            south = poly_int([-x for x in poly_d(drho)], eq, L)
            assert north == oN(eq) and south == -oS(eq)                   # Stokes with frames smooth on each cap
            assert oN(eq) - oS(eq) == 2                                   # clutching winding = chi(S^2)
            assert north + south == 2


def rot_shift(t_coeffs):
    """Rotate the tangent frame by theta, cos = (1 - t^2)/(1 + t^2), sin = 2t/(1 + t^2); return
    (omega'^{23} - omega^{23}) and 2 t'/(1 + t^2), the ds-components."""
    t = poly_rf(t_coeffs)
    den = GA.RF1 + t * t
    c = (GA.RF1 - t * t) / den
    s = rc(2) * t / den
    assert (c * c + s * s).eqrf(GA.RF1)
    # e'^2 = c e^2 + s e^3, e'^3 = -s e^2 + c e^3; omega' = R omega R^T + R dR^T in the 2 x 2 rotation block;
    # for so(2) the conjugation is trivial and the shift of omega'^{23} is (R dR^T)^{23}
    Rm = [[c, s], [GA.RF0 - s, c]]
    dRT = [[c.deriv(), GA.RF0 - s.deriv()], [s.deriv(), c.deriv()]]
    shift = Rm[0][0] * dRT[0][1] + Rm[0][1] * dRT[1][1]
    return shift, rc(2) * t.deriv() / den


def check_edge_term_gauge_and_winding():
    premise("dark-energy.wall-counterterm")
    for tc in ROTATIONS:
        shift, dtheta = rot_shift(tc)
        assert shift.eqrf(GA.RF0 - dtheta) and not dtheta.is_zero()
    # a frame rotation theta = w phi along the edge circle shifts oint omega^{23} by -2 pi w; in units of the
    # Euler entropy quantum 2 pi alpha = -3 pi/(2 Lambda) the patch entropy shifts by -w quanta
    for Lam in LAMBDAS:
        alpha = F(-3) / (4 * Lam)
        for w in WINDINGS:
            assert alpha * (-w) * 2 == F(3 * w, 2) / Lam * 1      # coefficient of pi: 2 alpha (-w) = 3w/(2 Lambda)
        assert 2 * alpha == F(-3, 2) / Lam


def sds_K(M, Lam, r):
    f = 1 - 2 * M / r - Lam * r * r / 3
    return (1 - f) / (r * r)


def check_counterterm_restores_area_density_on_sds_generators():
    premise("synthesis.series-wald-entropy-changes-without-flux-on-local-horizons")
    premise("synthesis.einstein-equations-from-c-loc-and-clausius")
    for (M, Lam, r0) in HOLES:
        f0 = 1 - 2 * M / r0 - Lam * r0 * r0 / 3
        assert f0 > 0
        alpha = F(-3) / (4 * Lam)
        for sign in SIGNS:
            for lam0 in LAMS0:
                pts = [r0 + sign * lam0 * F(k, 4) for k in range(5)]
                for r in pts:
                    K = sds_K(M, Lam, r)
                    assert K == 2 * M / r ** 3 + Lam / 3
                    s_jm = F(1, 4) + alpha * K
                    assert s_jm == -3 * M / (2 * Lam * r ** 3)
                    assert s_jm - alpha * K == F(1, 4)
                r1 = r0 + sign * lam0
                dS_jm = -3 * M / (2 * Lam) * (1 / r0 ** 3 - 1 / r1 ** 3)
                assert (dS_jm > 0) == (sign > 0)
                # first-order change: the stored rate +-9M/(2 Lambda r0^4) times |lambda0|
                lin = -3 * M / (2 * Lam) * (3 * sign * lam0 / r0 ** 4)
                assert lin == sign * 9 * M / (2 * Lam * r0 ** 4) * abs(lam0)
                assert abs(dS_jm - lin) * 2 < abs(lin)          # the linear term dominates at these lengths
                sub = lambda r: -3 * M / (2 * Lam * r ** 3) - alpha * sds_K(M, Lam, r)
                assert sub(r0) - sub(r1) == 0 and sub(r1) == F(1, 4)


def check_closed_cut_residual_is_the_stored_shift():
    premise("synthesis.euler-term-horizon-entropy-shift")
    premise("synthesis.sds-clausius-fixes-area-constant")
    for Lam in LAMBDAS:
        alpha = F(-3) / (4 * Lam)
        for chi in (2, 0, -2):
            residual = 2 * alpha * chi                 # coefficient of pi: 2 pi alpha chi
            assert residual == F(-3 * chi, 2) / Lam
        assert 2 * alpha * 2 == -3 / Lam               # spheres: -3 pi/Lambda, minus the de Sitter entropy
        assert 2 * alpha == -(3 / Lam) / 2             # one quantum: half the de Sitter entropy, negative


AREA_FRACTIONS = [F(1, 3), F(1, 2), F(2, 3), F(1), F(3, 2)]


def check_disk_patch_entropy_sign_and_non_additivity():
    premise("synthesis.euler-term-horizon-entropy-shift")
    premise("synthesis.sds-clausius-fixes-area-constant")
    for Lam in LAMBDAS:
        alpha = F(-3) / (4 * Lam)
        # S'[disk] = A/4 + 2 pi alpha; work in units of pi: A = a pi, S'/pi = a/4 + 2 alpha
        dS_area = 4 * 3 / Lam                       # de Sitter horizon area / pi = 12/Lambda
        threshold = dS_area / 2                     # 6/Lambda
        assert threshold == F(6) / Lam and threshold / 4 + 2 * alpha == 0
        assert dS_area / 4 == 3 / Lam               # the de Sitter entropy 3 pi/Lambda
        for x in AREA_FRACTIONS:
            a = x * abs(threshold)
            s_disk = a / 4 + 2 * alpha
            if Lam > 0:
                assert (s_disk < 0) == (a < threshold) and (s_disk == 0) == (a == threshold)
            else:
                assert s_disk > 0
        # two disks of areas a1, a2 glued to one disk: the sum exceeds the union's value by 2 pi alpha
        a1, a2 = F(1, 7) / abs(Lam), F(5, 3) / abs(Lam)
        union = (a1 + a2) / 4 + 2 * alpha
        parts = (a1 / 4 + 2 * alpha) + (a2 / 4 + 2 * alpha)
        assert parts - union == 2 * alpha == F(-3, 2) / Lam


# ---------------------------------------------------------------- four-dimensional forms (polynomial coefficients)
NV = 4


def p_add(a, b, c=1):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + c * v
    return {k: v for k, v in out.items() if v}


def p_mul(a, b):
    out = {}
    for ka, u in a.items():
        for kb, v in b.items():
            k = tuple(x + y for x, y in zip(ka, kb))
            out[k] = out.get(k, F(0)) + u * v
    return {k: v for k, v in out.items() if v}


def p_d(a, i):
    out = {}
    for k, u in a.items():
        if k[i]:
            kk = list(k)
            kk[i] -= 1
            out[tuple(kk)] = out.get(tuple(kk), F(0)) + k[i] * u
    return {k: v for k, v in out.items() if v}


def sort_sign(arr):
    arr = list(arr)
    sg = 1
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sg = -sg
    return sg, tuple(arr)


def f_wedge(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            if set(ka) & set(kb):
                continue
            sg, key = sort_sign(list(ka) + list(kb))
            out[key] = p_add(out.get(key, {}), p_mul(va, vb), sg)
    return {k: v for k, v in out.items() if v}


def f_add(a, b, c=1):
    out = {k: p_add(a.get(k, {}), b.get(k, {}), c) for k in set(a) | set(b)}
    return {k: v for k, v in out.items() if v}


def f_scal(a, c):
    out = {k: {kk: vv * c for kk, vv in v.items()} for k, v in a.items()}
    return {k: v for k, v in out.items() if v}


def f_d(a):
    out = {}
    for k, v in a.items():
        for i in range(NV):
            if i in k:
                continue
            dv = p_d(v, i)
            if dv:
                sg, key = sort_sign([i] + list(k))
                out[key] = p_add(out.get(key, {}), dv, sg)
    return {k: v for k, v in out.items() if v}


def f_zero(a):
    return all(not v for v in a.values())


def pullback_to_cut(a):
    """Restrict to the cut x0 = x1 = 0 (coordinates x2, x3)."""
    out = {}
    for k, v in a.items():
        if not set(k) <= {2, 3}:
            continue
        vv = {kk: u for kk, u in v.items() if kk[0] == 0 and kk[1] == 0}
        if vv:
            out[k] = vv
    return out


ETA4 = [1, -1, -1, -1]
PAIRS4 = [(a, b) for a in range(4) for b in range(a + 1, 4)]


def eps4(a, b, c, d):
    p = [a, b, c, d]
    if len(set(p)) < 4:
        return 0
    return sort_sign(p)[0]


def eps_from_GA(a, b, c, d):
    """eps_abcd read off e_a e_b e_c e_d = eps_abcd I in Cl(1,3) for distinct indices."""
    SQ = (1, -1, -1, -1)
    x = GA.gen(a)
    for i in (b, c, d):
        x = GA.mul(x, GA.gen(i), SQ)
    return x.get((0, 1, 2, 3), F(0))


def mono(c, e):
    return {tuple(e): F(c)} if c else {}


def lin(c0, c):
    out = {}
    if c0:
        out[(0, 0, 0, 0)] = F(c0)
    for i, ci in enumerate(c):
        if ci:
            e = [0] * 4
            e[i] = 1
            out[tuple(e)] = F(ci)
    return out


def antisym(comp):
    om = {}
    for (a, b), v in comp.items():
        om[(a, b)] = v
        om[(b, a)] = f_scal(v, -1)
    return om


TABLE = [(1, (0, 1, 0, -1)), (-1, (1, 0, 2, 0)), (2, (0, -1, 0, 1)), (0, (1, 1, 0, 0)),
         (1, (0, 0, -1, 2)), (-2, (1, 0, 0, 1)), (1, (2, 0, 1, 0)), (0, (0, 1, 1, -1))]


def generic_connection():
    comp = {}
    for idx, (a, b) in enumerate(PAIRS4):
        comp[(a, b)] = {(mu,): lin(*TABLE[(idx + 2 * mu) % 8]) for mu in ((idx) % 4, (idx + 1) % 4)}
    return antisym(comp)


def generic_parameter():
    comp = {}
    for idx, (a, b) in enumerate(PAIRS4):
        comp[(a, b)] = {(): lin(*TABLE[(3 * idx + 1) % 8])}
    return antisym(comp)


def W(om, a, b):
    return om.get((a, b), {})


def pair(X, Y):
    out = {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    sg = eps4(a, b, c, d)
                    if sg:
                        out = f_add(out, f_wedge(X.get((a, b), {}), Y.get((c, d), {})), sg)
    return out


def cubic(X, Y, Z):
    """eps_abcd X^ab ^ Y^c_e ^ Z^ed."""
    out = {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    sg = eps4(a, b, c, d)
                    if not sg:
                        continue
                    for e in range(4):
                        out = f_add(out, f_wedge(f_wedge(X.get((a, b), {}), f_scal(Y.get((c, e), {}), ETA4[e])),
                                                 Z.get((e, d), {})), sg)
    return out


def Dlam(om, lam):
    out = {}
    for a in range(4):
        for b in range(4):
            if a == b:
                continue
            cur = f_d(lam.get((a, b), {}))
            for c in range(4):
                cur = f_add(cur, f_wedge(f_scal(W(om, a, c), ETA4[c]), lam.get((c, b), {})))
                cur = f_add(cur, f_wedge(f_scal(W(om, b, c), ETA4[c]), lam.get((a, c), {})))
            out[(a, b)] = cur
    return out


def dQ_linear(om, dom_):
    """First-order change of Q = <om, d om> + 2/3 eps om ^ om ^ om under om -> om + dom_."""
    d_om = {k: f_d(v) for k, v in om.items()}
    d_dom = {k: f_d(v) for k, v in dom_.items()}
    out = f_add(pair(dom_, d_om), pair(om, d_dom))
    cub = f_add(f_add(cubic(dom_, om, om), cubic(om, dom_, om)), cubic(om, om, dom_))
    return f_add(out, f_scal(cub, F(2, 3)))


def check_wall_counterterm_anomaly_is_the_edge_transgression():
    premise("dark-energy.wall-counterterm")
    for (a, b, c, d) in [(0, 1, 2, 3), (1, 0, 2, 3), (2, 3, 0, 1), (3, 1, 0, 2)]:
        assert eps_from_GA(a, b, c, d) == eps4(a, b, c, d)
    om = generic_connection()
    lam = generic_parameter()
    var = dQ_linear(om, Dlam(om, lam))
    anom = f_d(pair(lam, {k: f_d(v) for k, v in om.items()}))
    assert not f_zero(anom) and f_zero(f_add(var, anom, -1))
    # lambda = the binormal n = e0 ^ e1 of the cut: <n, d om> = 4 d om^{23}
    n = antisym({(0, 1): {(): {(0, 0, 0, 0): F(1)}}})
    d_om = {k: f_d(v) for k, v in om.items()}
    assert f_zero(f_add(pair(n, d_om), f_scal(d_om[(2, 3)], 4), -1))
    # Gauss in an adapted frame: R^{23} - d om^{23} on the cut = -(b2 ^ a3 + a2 ^ b3)
    for admissible in (True, False):
        comp = {}
        for idx, (p, q) in enumerate(PAIRS4):
            comp[(p, q)] = {(mu,): lin(*TABLE[(5 * idx + mu) % 8]) for mu in range(4)}
        if admissible:      # k-extrinsic part omega^{A0} - omega^{A1} vanishes on the cut: omega^{A1} := omega^{A0}
            for A in (2, 3):
                comp[(1, A)] = {k: dict(v) for k, v in comp[(0, A)].items()}
        cn = antisym(comp)
        R23 = f_d(W(cn, 2, 3))
        for e in range(4):
            R23 = f_add(R23, f_wedge(f_scal(W(cn, 2, e), ETA4[e]), W(cn, e, 3)))
        defect = pullback_to_cut(f_add(R23, f_d(W(cn, 2, 3)), -1))
        aA = {A: pullback_to_cut(f_add(W(cn, A, 0), W(cn, A, 1), -1)) for A in (2, 3)}
        bA = {A: pullback_to_cut(f_scal(f_add(W(cn, A, 0), W(cn, A, 1)), F(1, 2))) for A in (2, 3)}
        pred = f_scal(f_add(f_wedge(bA[2], aA[3]), f_wedge(aA[2], bA[3])), -1)
        assert f_zero(f_add(defect, pred, -1))
        assert f_zero(defect) == admissible


# ---- GTG derivation (maintainer pass 2026-11-07, GTG proofs) ----
# The cut as a two-dimensional gauge field on its flat Riemannian background (lib/gtg.py, sq = (-1, -1): the
# tangent physical frame e2, e3 is generator 0, 1 here, J = e2 e3 the cut's unit bivector): hb^{-1}(e_s) = e2,
# hb^{-1}(e_phi) = rho(s) e3; the rotation-gauge field is SOLVED from the torsion equation. It is J times a scalar
# one-form, Omega_S(a) = -omega_S(a) J (the Cartan value omega_S = -rho' dphi of the statement, C10), so the field
# strength has no commutator term, R(e_s ^ e_phi) = d_s Omega_S(e_phi), and calR(J) = K J with K = -rho''/rho.
import gtg  # noqa: E402

S2 = (-1, -1)
CUT_POINTS = [F(1, 2), F(1, 3), F(3, 4)]


def cut_field(rho, s0, tpoly=None):
    """The cut's gauge field at s = s0; with tpoly, the gauge transformation hb^{-1} -> R hb^{-1} R~ with
    R = exp(-J theta/2), cos = (1 - t^2)/(1 + t^2), sin = 2t/(1 + t^2), which rotates the frame map
    E_A = hb(e_A) by +theta: E_2' = cos E_2 + sin E_3."""
    s = gtg.J.var(0, s0, 2, 2)
    z = gtg.J.const(0, 2)
    r = z
    for k, c in enumerate(rho):
        r = r + c * s ** k
    if tpoly is None:
        return gtg.Field([[gtg.J.const(1, 2), z], [z, r]], sq=S2)
    t = z
    for k, c in enumerate(tpoly):
        t = t + c * s ** k
    cth, sth = (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)
    return gtg.Field([[cth, sth * r], [-sth, cth * r]], sq=S2)


def check_gtg_cut_gauge_field_transgression_gauge_law_and_edge_curvature():
    premise("synthesis.imported-gtg-dictionary")
    premise("synthesis.imported-gauss-bonnet-with-corners-poincare-hopf-and-edge-term")
    ok = True
    Jb = {(0, 1): F(1)}
    for rho in OPEN + [closed_profile(L, c) for (L, c) in CLOSED]:
        d1, d2 = poly_d(rho), poly_d(poly_d(rho))
        for s0 in CUT_POINTS:
            r0, rp, rpp = poly_val(rho, s0), poly_val(d1, s0), poly_val(d2, s0)
            if r0 <= 0:
                continue
            fld = cut_field(rho, s0)
            ok = ok and fld.torsion_free() and fld.Omega(0) == {} and GA.eq(fld.Omega(1), GA.scal(rp, Jb))
            # abelian field strength: no commutator term, so R = d Omega (the transgression d omega_S = K e^2 ^ e^3)
            ok = ok and gtg.comm(fld.Omega(0), fld.Omega(1), S2) == {}
            ok = ok and GA.eq(fld.strength(0, 1), GA.scal(rpp, Jb))
            K = -rpp / r0
            ok = ok and GA.eq(fld.curvature()[(0, 1)], GA.scal(K, Jb))
            # edge curvature of the circle s = s0 for N = +e2: k_g = -((T . D) T) . N = -rho'/rho
            TDT = fld.cov_phys([F(0), F(1)], gtg.vec([gtg.J(0, None, 2), gtg.J(1, None, 2)]))
            ok = ok and -gtg.vdot(TDT, GA.gen(0), S2) == -rp / r0
            # gauge law: rotating the tangent frame by theta(s) adds d theta: Omega'(e_s) = theta' J, i.e.
            # omega_S -> omega_S - d theta
            for tp in ([F(1, 3), F(1, 2)], [F(0), F(-2), F(1)], [F(2), F(0), F(0), F(-1, 5)]):
                rot = cut_field(rho, s0, tp)
                t0, t1 = poly_val(tp, s0), poly_val(poly_d(tp), s0)
                ok = ok and GA.eq(rot.Omega(0), GA.scal(2 * t1 / (1 + t0 * t0), Jb))
                ok = ok and GA.eq(rot.Omega(1), fld.Omega(1))
    assert ok
    return ok


BIV_SAMPLES = ((1, 2, -3, 5, F(1, 2), 7), (0, 0, 0, 0, 0, 1), (F(2, 3), -1, 4, 0, 3, F(-5, 4)))


def biv_from(coeffs):
    """sum of coeffs times e_a ^ e_b over the blades (0,1), (0,2), (0,3), (1,2), (1,3), (2,3) of Cl(1,3)."""
    Y = {}
    for (a, b), c in zip(gtg.bivector_blades(4), coeffs):
        Y = GA.add(Y, GA.scal(F(c), gtg.wedge(GA.gen(a), GA.gen(b), gtg.S13)))
    return Y


def check_gtg_binormal_contraction_is_four_times_the_cut_component():
    premise("dark-energy.wall-counterterm")
    S13 = gtg.S13
    Iinv = GA.scal(F(-1), gtg.pseudoscalar(S13))
    lam = gtg.wedge(GA.gen(0), GA.gen(1), S13)
    ok = True
    for coeffs in BIV_SAMPLES:
        Y = biv_from(coeffs)
        y23 = Y.get((2, 3), F(0))
        ok = ok and y23 != 0 and 4 * gtg.sp(GA.mul(GA.mul(lam, Iinv, S13), Y, S13)) == 4 * y23
    assert ok
    return ok
