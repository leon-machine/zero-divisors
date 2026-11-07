"""synthesis.series-wald-entropy-changes-without-flux-on-local-horizons: exact checks.

The Schwarzschild-de Sitter curvature is computed from the metric itself: the metric in coordinates
(t, r, z = cos theta, phi) is rational, its components are expanded as exact truncated Taylor jets
about rational points, and the Christoffel symbols and the Riemann tensor are formed from the jets.
(1) Lambda-vacuum, the orthonormal pair components, the vanishing of R(k, A, k, B) and of every
component that a tilt of the edge plane along k could bring in, the parallel transport of the static
transverse frame along both radial null generators, and K = 2M/r^3 + Lambda/3 with dK/dr = -6M/r^4,
at several points and at points displaced along the generators. (2) The Jacobson-Myers density of the
series' Lagrangian on an edge where the k-extrinsic curvature vanishes is (1 - 3K/Lambda)/4G, minus
3/(4 Lambda G) times the Cartan curvature of the edge plane; it vanishes for every plane of de Sitter
space (GA wedge products give the sectional curvatures of tilted and generic planes); integrated over
the bifurcation sphere of a Schwarzschild-de Sitter hole it reproduces A/4G - 3 pi/(Lambda G).
(3) Marching along each radial generator with the curvature read from the jets, the Sachs step keeps chi = 0,
the area and the vacuum heat stay zero, while the density
changes by an exact rational amount, positive outward and negative inward; the first-order rate is
the defect of the integrated reading, +-9M/(2 Lambda G r^4).
Units G = 1. pi is carried as a formal factor (coefficients of pi compared).
"""
from fractions import Fraction as F
from itertools import product
import GA
from tp_premise import premise

NV = 4
D = 3
SQ = [-1, 1, 1, 1]          # orthonormal frame (t, r, theta, phi), signature (-,+,+,+)


# ---- exact truncated Taylor jets in the four coordinate displacements --------------------------
def jconst(c):
    return {(0, 0, 0, 0): F(c)} if c != 0 else {}


def jvar(i):
    e = [0, 0, 0, 0]
    e[i] = 1
    return {tuple(e): F(1)}


def jadd(a, b, s=1):
    out = dict(a)
    for e, v in b.items():
        out[e] = out.get(e, F(0)) + s * v
    return {e: v for e, v in out.items() if v != 0}


def jscal(c, a):
    return {e: c * v for e, v in a.items() if c * v != 0}


def jmul(a, b, d):
    out = {}
    for e1, v1 in a.items():
        for e2, v2 in b.items():
            e = tuple(x + y for x, y in zip(e1, e2))
            if sum(e) <= d:
                out[e] = out.get(e, F(0)) + v1 * v2
    return {e: v for e, v in out.items() if v != 0}


def jinv(a, d):
    c0 = a.get((0, 0, 0, 0), F(0))
    assert c0 != 0
    x = jscal(-1 / c0, jadd(a, jconst(c0), -1))
    term, out = jconst(1), jconst(1)
    for _ in range(d):
        term = jmul(term, x, d)
        out = jadd(out, term)
    return jscal(1 / c0, out)


def jderiv(a, i):
    out = {}
    for e, v in a.items():
        if e[i] > 0:
            ee = list(e)
            ee[i] -= 1
            out[tuple(ee)] = out.get(tuple(ee), F(0)) + v * e[i]
    return out


def jval(a):
    return a.get((0, 0, 0, 0), F(0))


def jdr(a):
    return a.get((0, 1, 0, 0), F(0))


def christoffel(g):
    ginv = [jinv(g[a], D) for a in range(NV)]
    G = {}
    for a, b, c in product(range(NV), repeat=3):
        s = {}
        if a == c:
            s = jadd(s, jderiv(g[a], b))
        if a == b:
            s = jadd(s, jderiv(g[a], c))
        if b == c:
            s = jadd(s, jderiv(g[b], a), -1)
        if s:
            G[(a, b, c)] = jscal(F(1, 2), jmul(ginv[a], s, D - 1))
    return G


def riemann(g):
    """lowered R_{abcd} = g_aa (d_c G^a_db - d_d G^a_cb + G^a_ce G^e_db - G^a_de G^e_cb)"""
    G = christoffel(g)
    Rl = {}
    for a, b, c, d in product(range(NV), repeat=4):
        if c >= d:
            continue
        s = jadd(jderiv(G.get((a, d, b), {}), c), jderiv(G.get((a, c, b), {}), d), -1)
        for e in range(NV):
            s = jadd(s, jmul(G.get((a, c, e), {}), G.get((e, d, b), {}), D - 2))
            s = jadd(s, jmul(G.get((a, d, e), {}), G.get((e, c, b), {}), D - 2), -1)
        low = jmul(g[a], s, D - 2)
        if low:
            Rl[(a, b, c, d)] = low
            Rl[(a, b, d, c)] = jscal(-1, low)
    return Rl, G


def sds(M, Lam, r0):
    """metric jets of -f dt^2 + dr^2/f + r^2 dz^2/(1-z^2) + r^2 (1-z^2) dphi^2 about (0, r0, 0, 0)"""
    r = jadd(jconst(r0), jvar(1))
    r2 = jmul(r, r, D)
    f = jadd(jadd(jconst(1), jscal(-2 * M, jinv(r, D))), jscal(-Lam / 3, r2))
    z = jvar(2)
    omz = jadd(jconst(1), jmul(z, z, D), -1)
    g = [jscal(-1, f), jinv(f, D), jmul(r2, jinv(omz, D), D), jmul(r2, omz, D)]
    return g, f


def R4(Rl, a, b, c, d):
    return jval(Rl.get((a, b, c, d), {}))


def frame_data(M, Lam, r0):
    """orthonormal pair components, f, f', f'' at the point, plus raw data"""
    g, f = sds(M, Lam, r0)
    Rl, G = riemann(g)
    norm = [abs(jval(g[a])) for a in range(NV)]
    pairs = {(a, b): R4(Rl, a, b, a, b) / (norm[a] * norm[b]) for a in range(NV) for b in range(a + 1, NV)}
    f0, f1, f2 = jval(f), jdr(f), 2 * f.get((0, 2, 0, 0), F(0))
    return g, f, Rl, G, pairs, (f0, f1, f2)


# ---- sectional curvature of a plane from the pair components, with GA wedge products -------------
def vec(c):
    return {(i,): F(x) for i, x in enumerate(c) if x != 0}


def wedge(u, v):
    uv, vu = GA.mul(u, v, SQ), GA.mul(v, u, SQ)
    return {k: x for k, x in GA.scal(F(1, 2), GA.sub(uv, vu)).items() if len(k) == 2}


def sectional(pairs, u, v):
    """K(u, v) = R(u, v, u, v) / (Q(u) Q(v) - (u.v)^2) for a pair-diagonal curvature tensor"""
    B = wedge(u, v)
    num = sum(pairs[(a, b)] * B.get((a, b), F(0)) ** 2 for (a, b) in pairs)
    den = GA.dot(u, u, SQ) * GA.dot(v, v, SQ) - GA.dot(u, v, SQ) ** 2
    return num / den


POINTS = [(F(1), F(3, 100), F(3)), (F(1, 2), F(1, 10), F(7, 5)), (F(2), F(1, 50), F(9))]


def check_sds_radial_generator_data():
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("synthesis.euler-term-horizon-entropy-shift")
    premise("synthesis.imported-raychaudhuri-null-congruence")
    for (M, Lam, r0) in POINTS:
        g, f, Rl, G, pairs, (f0, f1, f2) = frame_data(M, Lam, r0)
        GA.check("static region f(r0) > 0", f0 > 0)
        # Lambda-vacuum: Ric_bd = g^ac R_abcd = Lambda g_bd (a solution of the series' field equations)
        ok = True
        for b, d in product(range(NV), repeat=2):
            ric = sum(R4(Rl, a, b, a, d) / jval(g[a]) for a in range(NV))
            ok = ok and ric == (Lam * jval(g[b]) if b == d else 0)
        GA.check("Ricci = Lambda g at r0 = %s" % r0, ok)
        GA.check("orthonormal pairs f''/2, f'/2r, -f'/2r, (1-f)/r^2",
                 pairs[(0, 1)] == f2 / 2 and pairs[(0, 2)] == f1 / (2 * r0) and pairs[(0, 3)] == f1 / (2 * r0)
                 and pairs[(1, 2)] == -f1 / (2 * r0) and pairs[(1, 3)] == -f1 / (2 * r0)
                 and pairs[(2, 3)] == (1 - f0) / r0 ** 2)
        GA.check("no off-pair components", all(R4(Rl, a, b, c, d) == 0 for a, b, c, d in product(range(NV), repeat=4)
                                                if sorted((a, b)) != sorted((c, d))))
        K0 = pairs[(2, 3)]
        GA.check("K = 2M/r^3 + Lambda/3", K0 == 2 * M / r0 ** 3 + Lam / 3)
        Kjet = jmul(Rl[(2, 3, 2, 3)], jinv(jmul(g[2], g[3], D), D), D - 2)
        GA.check("dK/dr = -6M/r^4", jdr(Kjet) == -6 * M / r0 ** 4)
        for sgn in (1, -1):
            k = [1 / f0, F(sgn), F(0), F(0)]
            GA.check("k null", sum(jval(g[a]) * k[a] ** 2 for a in range(NV)) == 0)
            RkAkB = [sum(k[m] * k[n] * R4(Rl, m, A, n, B) for m in range(NV) for n in range(NV))
                     for A in (2, 3) for B in (2, 3)]
            GA.check("R(k,A,k,B) = 0 (no focusing, no shear source)", all(x == 0 for x in RkAkB))
            tilt = [sum(k[m] * R4(Rl, m, A, B, C) for m in range(NV)) for A, B, C in product((2, 3), repeat=3)]
            GA.check("R(k,A,B,C) = 0 (edge-plane tilts along k invisible)", all(x == 0 for x in tilt))
            # geodesic: k^a d_a k^b + Gamma^b_ac k^a k^c = 0, with k^t = 1/f(r), k^r = sgn
            dkt = -f1 / f0 ** 2           # d(1/f)/dr
            acc = [sgn * (dkt if b == 0 else 0) + sum(jval(G.get((b, a, c), {})) * k[a] * k[c]
                                                      for a in range(NV) for c in range(NV)) for b in range(NV)]
            GA.check("radial null field is affinely geodesic", all(x == 0 for x in acc))
            # static transverse frame E_z = d_z / r, E_phi = d_phi / r is parallel along k (at z = 0)
            for A in (2, 3):
                par = [sgn * (-1 / r0 ** 2 if b == A else 0) + sum(jval(G.get((b, a, A), {})) * k[a] / r0
                                                                for a in range(NV)) for b in range(NV)]
                GA.check("E_%d parallel along k" % A, all(x == 0 for x in par))
        # the same along the generator: displaced points r0 + lam carry the same vanishing data
        for lam in (F(1, 3), F(-1, 4)):
            g2, f2j, Rl2, G2, pairs2, (fa, fb, fc) = frame_data(M, Lam, r0 + lam)
            for sgn in (1, -1):
                k = [1 / fa, F(sgn), F(0), F(0)]
                GA.check("R(k,A,k,B) = 0 at r0 + %s" % lam,
                         all(sum(k[m] * k[n] * R4(Rl2, m, A, n, B) for m in range(NV) for n in range(NV)) == 0
                             for A in (2, 3) for B in (2, 3)))
            GA.check("K along the generator", pairs2[(2, 3)] == 2 * M / (r0 + lam) ** 3 + Lam / 3)


def jm_density(K, Lam):
    """Jacobson-Myers density (1 + 2 alpha R_Sigma)/4G with R_Sigma = 2K, alpha = -3/(4 Lambda), G = 1"""
    alpha = -3 / (4 * Lam)
    return (1 + 2 * alpha * 2 * K) / 4


def check_density_is_cartan_curvature():
    premise("synthesis.imported-wald-noether-charge-entropy")
    premise("synthesis.euler-term-horizon-entropy-shift")
    premise("synthesis.sds-clausius-fixes-area-constant")
    # sectional curvature from GA wedges; tilts u -> u + a k leave the edge-plane curvature unchanged
    for (M, Lam, r0) in POINTS:
        g, f, Rl, G, pairs, (f0, f1, f2) = frame_data(M, Lam, r0)
        e2, e3 = vec([0, 0, 1, 0]), vec([0, 0, 0, 1])
        K0 = sectional(pairs, e2, e3)
        GA.check("GA sectional curvature of the edge plane", K0 == pairs[(2, 3)])
        for sgn in (1, -1):
            kk = vec([1, sgn, 0, 0])
            for a, b in ((F(2), F(-3)), (F(1, 7), F(5)), (F(-4, 3), F(0))):
                u = GA.add(e2, GA.scal(a, kk))
                v = GA.add(e3, GA.scal(b, kk))
                GA.check("tilted edge plane has the same K", sectional(pairs, u, v) == K0)
        s = jm_density(K0, Lam)
        GA.check("JM density = -(3/(4 Lambda)) (K - Lambda/3)", s == -3 / (4 * Lam) * (K0 - Lam / 3))
        GA.check("JM density = -3M/(2 Lambda r^3) < 0", s == -3 * M / (2 * Lam * r0 ** 3) and s < 0)
    # anchors: at (M, Lambda, r0) = (1, 3/100, 3) the edge curvature is 227/2700 and the density -50/27
    g, f, Rl, G, pairs, _ = frame_data(F(1), F(3, 100), F(3))
    K = sectional(pairs, vec([0, 0, 1, 0]), vec([0, 0, 0, 1]))
    GA.check("anchor K = 227/2700, s = -50/27", K == F(227, 2700) and jm_density(K, F(3, 100)) == F(-50, 27))
    # de Sitter (M = 0): every plane has K = Lambda/3 and the density vanishes
    for Lam in (F(3, 100), F(1, 10)):
        g, f, Rl, G, pairs, _ = frame_data(F(0), Lam, F(2))
        planes = [([0, 0, 1, 0], [0, 0, 0, 1]), ([0, 1, 0, 0], [0, 0, 0, 1]),
                  ([F(1, 2), 1, 2, 0], [0, 3, -1, F(5, 2)]), ([1, 0, 0, 2], [0, 1, 7, -1])]
        for u, v in planes:
            u, v = vec(u), vec(v)
            if GA.dot(u, u, SQ) * GA.dot(v, v, SQ) - GA.dot(u, v, SQ) ** 2 > 0:
                K = sectional(pairs, u, v)
                GA.check("de Sitter K = Lambda/3, density 0", K == Lam / 3 and jm_density(K, Lam) == 0)
    # bifurcation sphere of a Schwarzschild-de Sitter hole: s(r_b) * 4 pi r_b^2 = pi r_b^2 - 3 pi/Lambda
    for rb, Lam in ((F(2), F(1, 10)), (F(3, 2), F(1, 5)), (F(5), F(3, 100))):
        M = rb * (1 - Lam * rb ** 2 / 3) / 2
        GA.check("f(r_b) = 0 with M > 0", M > 0 and 1 - 2 * M / rb - Lam * rb ** 2 / 3 == 0)
        g, f, Rl, G, pairs, _ = frame_data(M, Lam, rb + 1)      # curvature formula, checked off the horizon
        K_b = 2 * M / rb ** 3 + Lam / 3
        total = jm_density(K_b, Lam) * 4 * rb ** 2              # coefficient of pi
        GA.check("integral over the sphere = A/4 - 3 pi chi/(2 Lambda), chi = 2",
                 total == rb ** 2 - 3 / Lam and pairs[(2, 3)] == 2 * M / (rb + 1) ** 3 + Lam / 3)
        anchors = {F(2): F(-26), F(3, 2): F(-51, 4), F(5): F(-75)}
        GA.check("anchor: coefficient of pi", total == anchors[rb])


def check_entropy_change_without_flux():
    premise("synthesis.einstein-equations-from-c-loc-and-clausius")
    premise("synthesis.imported-raychaudhuri-null-congruence")
    for (M, Lam, r0) in POINTS:
        for lam0 in (F(-1, 2), F(-1, 10)):
            dS = {}
            for sgn in (1, -1):
                r1 = r0 + sgn * lam0                               # r(lambda_0), lambda_0 < 0
                # march along the generator from lambda_0 to 0 in steps h, reading the curvature from the
                # metric jets at each point: Sachs/Raychaudhuri step for chi, heat 8 pi T(k,k) = Ric(k,k) - Lambda g(k,k)
                nsteps = 4
                h = -lam0 / nsteps
                chi = [[F(0), F(0)], [F(0), F(0)]]
                dA, dQ8pi = F(0), F(0)
                for j in range(nsteps + 1):
                    lam = lam0 + j * h
                    rr = r0 + sgn * lam
                    gj, fj, Rj, Gj, pj, (fa, fb, fc) = frame_data(M, Lam, rr)
                    k = [1 / fa, F(sgn), F(0), F(0)]
                    RkAkB = [[sum(k[m] * k[n] * R4(Rj, m, A, n, B) for m in range(NV) for n in range(NV))
                              / rr ** 2 for B in (2, 3)] for A in (2, 3)]
                    ric_kk = sum(k[m] * k[n] * sum(R4(Rj, a, m, a, n) / jval(gj[a]) for a in range(NV))
                                 for m in range(NV) for n in range(NV))
                    gkk = sum(jval(gj[a]) * k[a] ** 2 for a in range(NV))
                    dQ8pi += (-lam) * (ric_kk - Lam * gkk) * h       # boost weight -lambda, vacuum heat
                    theta = chi[0][0] + chi[1][1]
                    dA += theta * h
                    chi = [[chi[A][B] - h * (sum(chi[A][C] * chi[C][B] for C in (0, 1)) + RkAkB[A][B])
                            for B in (0, 1)] for A in (0, 1)]
                    if j == 0:
                        K_start = pj[(2, 3)]
                    if j == nsteps:
                        K_end = pj[(2, 3)]
                GA.check("no focusing, no shear, no heat along the generator",
                         all(x == 0 for row in chi for x in row) and dA == 0 and dQ8pi == 0)
                dS[sgn] = jm_density(K_end, Lam) - jm_density(K_start, Lam)   # per unit cross-section area
                closed = -3 * M / (2 * Lam) * (1 / r0 ** 3 - 1 / r1 ** 3)
                GA.check("Delta S from the jets = closed form", dS[sgn] == closed)
                GA.check("Clausius defect on the open patch: dQ = 0, dA = 0, Delta S != 0", dS[sgn] != 0)
            GA.check("outward increase, inward decrease", dS[1] > 0 and dS[-1] < 0)
        # first-order rate: d s/d lambda = (1/4)(4 alpha) dK/dlambda = +-9M/(2 Lambda r^4)
        g, f, Rl, G, pairs, _ = frame_data(M, Lam, r0)
        Kjet = jmul(Rl[(2, 3, 2, 3)], jinv(jmul(g[2], g[3], D), D), D - 2)
        alpha = -3 / (4 * Lam)
        for sgn in (1, -1):
            rate = alpha * sgn * jdr(Kjet)
            GA.check("rate = +-9M/(2 Lambda r^4)", rate == sgn * 9 * M / (2 * Lam * r0 ** 4))


EXPORTS = {}


# ---- GTG derivation (maintainer pass 2026-11-07, GTG proofs) ----
# The Schwarzschild-de Sitter field as a gauge field on flat spacetime (lib/gtg.py), store signature (+,-,-,-),
# Painleve-Gullstrand chart hb = 1 - beta P, beta^2 = 2M/r + Lambda r^2/3 = 1 - f; the store curvature
# calR(B) = -R(hb(B)) from the field strength. The sectional curvature of a spacelike plane with unit bivector
# B (B^2 = -1) is K = <calR(B) B^{-1}> (de Sitter: Lambda/3, sign-free); the Cartan curvature of the edge plane
# is K - Lambda/3 = <(calR(B) - (Lambda/3) B) B^{-1}>; R(k, A, k, B) = (k ^ B) . calR(k ^ A) (dictionary C11).
import gtg  # noqa: E402

S13 = gtg.S13
# (r, Lambda, beta) in the static region (beta < 1), M = r (beta^2 - Lambda r^2/3)/2 > 0
SDS_POINTS = [(F(1), F(3, 4), F(4, 5)), (F(2), F(3, 8), F(4, 5)), (F(1, 2), F(3), F(3, 5))]


def sds_gauge_field(r0, lam, b0):
    M = r0 * (b0 * b0 - lam * r0 * r0 / 3) / 2
    return gtg.pg_field(r0, F(3, 5), F(4, 5), gtg.beta_kottler(M, lam)), M


def sect(Rc, B):
    """<calR(B) B^{-1}> for a bivector B (B^{-1} = B/<BB>)."""
    BB = gtg.sp(GA.mul(B, B, S13))
    return gtg.sp(GA.mul(gtg.apply_op(Rc, B), B, S13)) / BB


def check_gtg_sds_field_strength_on_radial_generators():
    premise("synthesis.imported-raychaudhuri-null-congruence")
    premise("synthesis.euler-term-horizon-entropy-shift")
    ok = True
    e = [GA.gen(i) for i in range(4)]
    for r0, lam, b0 in SDS_POINTS:
        fld, M = sds_gauge_field(r0, lam, b0)
        ok = ok and M > 0 and fld.torsion_free()
        Rc = fld.curvature()
        ok = ok and all(GA.eq(gtg.ricci(Rc, e[c]), GA.scal(lam, e[c])) for c in range(4))
        K = 2 * M / r0 ** 3 + lam / 3
        ok = ok and GA.eq(gtg.apply_op(Rc, gtg.wedge(e[2], e[3])), GA.scal(K, gtg.wedge(e[2], e[3])))
        for sgn in (1, -1):
            k = GA.add(e[0], GA.scal(sgn, e[1]))
            for A in (e[2], e[3]):
                for Bv in (e[2], e[3]):
                    ok = ok and gtg.riem_o(Rc, k, A, k, Bv) == 0
                    ok = ok and gtg.riem_o(Rc, k, A, e[2], e[3]) == 0
            for a, b in ((F(0), F(0)), (F(2), F(-1, 3)), (F(-5, 7), F(4))):
                tilt = gtg.wedge(GA.add(e[2], GA.scal(a, k)), GA.add(e[3], GA.scal(b, k)))
                ok = ok and sect(Rc, tilt) == K
            # the transverse physical frame is D-parallel along both radial null directions
            kc = [F(1), F(sgn), F(0), F(0)]
            ok = ok and all(fld.cov_phys(kc, gtg.vec([gtg.J(1 if j == i else 0) for j in range(4)])) == {}
                            for i in (2, 3))
        s_density = -F(3, 4) / lam * (K - lam / 3)
        ok = ok and s_density == -3 * M / (2 * lam * r0 ** 3)
    # de Sitter (flat slicing): every spacelike plane has K = Lambda/3, so the density vanishes
    Rds = gtg.de_sitter_flat(F(1, 2), F(3)).curvature()
    for B in (gtg.wedge(e[2], e[3]), gtg.wedge(GA.add(e[1], GA.scal(F(2), e[3])), GA.add(e[2], GA.scal(F(1, 3), e[0])))):
        ok = ok and sect(Rds, B) == F(1, 4)
    assert ok
    return ok


def check_gtg_horizon_cross_section_surface_gravity_and_value():
    premise("synthesis.euler-term-horizon-entropy-shift")
    premise("synthesis.sds-clausius-fixes-area-constant")
    ok = True
    for rb, lam in ((F(1), F(3, 4)), (F(2), F(3, 16)), (F(1, 2), F(3, 2))):
        M = rb * (1 - lam * rb * rb / 3) / 2
        fld = gtg.pg_field(rb, F(3, 5), F(4, 5), gtg.beta_kottler(M, lam))
        beta = fld.TH[1][0]
        ok = ok and M > 0 and beta.v == 1
        xi = gtg.vec([gtg.J(1), beta, gtg.J(0), gtg.J(0)])
        ok = ok and gtg.vdot(gtg.m_val(xi), gtg.m_val(xi)) == 0
        kappa = (2 * M / rb ** 2 - 2 * lam * rb / 3) / 2
        ok = ok and GA.eq(fld.cov_phys([F(1), F(1), F(0), F(0)], xi), GA.scal(kappa, gtg.m_val(xi)))
        # the cut's second fundamental form along xi vanishes (the condition of (i)); the other null normal's does not
        tang = ([F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)])
        ok = ok and all(gtg.vdot(GA.gen(b), fld.cov_phys(a, xi)) == 0 for a in tang for b in (2, 3))
        n = gtg.vec([gtg.J(1), gtg.J(-1), gtg.J(0), gtg.J(0)])
        ok = ok and -sum(gtg.vdot(GA.gen(2 + i), fld.cov_phys(a, n)) for i, a in enumerate(tang)) == -4 / rb
        K = sect(fld.curvature(), gtg.wedge(GA.gen(2), GA.gen(3)))
        # coefficients of pi: 4 rb^2 * s = A/4 - 3/Lambda (pi factored out), s = -(3/4 Lambda)(K - Lambda/3)
        ok = ok and 4 * rb * rb * (-F(3, 4) / lam * (K - lam / 3)) == rb * rb - 3 / lam
    assert ok
    return ok
