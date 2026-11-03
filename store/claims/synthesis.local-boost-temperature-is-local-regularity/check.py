"""synthesis.local-boost-temperature-is-local-regularity: exact checks.

check_local_boost_period: in Riemann normal coordinates at p, g_ab(x) = eta_ab - (1/3) R_acbd x^c x^d
with signature (-,+,+,+) and R an algebraic curvature tensor (a sum of Kulkarni-Nomizu products of
rational symmetric matrices, so the pair symmetries and the first Bianchi identity hold by
construction, verified). Along the boost orbit x = rho (sinh l, cosh l, 0, 0) of the plane through p
(cosh, sinh given rationally by s), the metric on the (rho, l) plane is exactly
g_rr = 1, g_rl = 0, g_ll = -(rho^2 + k rho^4), k = R_0101/3, the same at every rapidity: so
F^2 = rho^2 + k rho^4, F'(0) = 1 for every curvature tensor, and the regular Euclidean period is
2 pi in rapidity. Negative control: off the plane (transverse offset y) g_ll depends on the rapidity.
check_acceleration_temperature: for -F^2 dl^2 + d rho^2 the static observer at rho has proper
acceleration a = F'/F and proper inverse temperature 2 pi F at rapidity period 2 pi, so
(T/(a/2 pi))^(-2) = F'^2 = (1 + 2 k rho^2)^2/(1 + k rho^2) = 1 + 3 k rho^2 + O(rho^4), an identity of
rational functions in rho (GA.RF), equal to 1 at rho = 0 for every k, and exactly 1 for every rho
only at k = 0.
check_diamond_flow_unit_boost: the field zeta = ((L^2 - t^2 - r^2) d_t - 2 t x^i d_i)/(2L) of the
diamond of radius L is conformal Killing (d_a zeta_b + d_b zeta_a = (1/2)(div zeta) eta_ab, checked at
rational points, the derivatives of a quadratic field being exact central differences), vanishes on
the edge t = 0, r = L, and its derivative there is the unit boost of the plane (t, n), n the edge
normal: surface gravity 1, the normalisation of the wedge.
check_window_kms_iff_modular: on a window of n = 3 CAR modes in Cl(3,3) with boost weights w_k and
rational Boltzmann factors q_k standing for e^(-2 pi w_k), the Gibbs element G = prod (1 + (q_k - 1) N_k)
implements the imaginary-time flow on the generators, G v_k G^-1 = q_k^-1 v_k and
G v_k^* G^-1 = q_k v_k^* (tau_{i beta}), with Fermi-Dirac occupations q_k/(1 + q_k);
the centre of the window algebra is the scalars (rank 63 commutator map), so Ad(rho) = Ad(G) forces
rho = c G; a faithful non-Gibbs rho (one Boltzmann factor changed, or a hop term added) fails both
the KMS identity omega_rho(xy) = omega_rho(y G x G^-1) on the 64 x 64 blade pairs and Ad(rho) = Ad(G);
a correlated state with the same single-mode marginals (G + sigma_0 sigma_1/20) passes the single-mode
test and fails the joint one: the joint condition is stronger than its single-mode form.
"""
from fractions import Fraction as F
import GA
from GA import RF
from tp_premise import premise

ETA = [-1, 1, 1, 1]


def setup_geometry():
    premise("singularity.euclidean-section-period")
    premise("angle.imported-theorems-deliver-their-hypotheses")


def setup_algebra():
    premise("singularity.kms-uniqueness-factor")
    premise("hawking.gibbs-states-are-kms-conversely-finite")
    premise("singularity.modular-theory-matrix-factor-proved-outright")
    premise("hawking.kms-restricts-invariant-subalgebras")
    premise("hawking.imported-kms-passes-inductive-limits")
    premise("singularity.rate-rigidity-temperature-not-algebra-intrinsic")
    premise("hawking.full-uniqueness-given-dynamics")


# ---------------------------------------------------------------- geometry

def kn(A, B):
    """Kulkarni-Nomizu product of symmetric 4x4 matrices, all indices down."""
    R = {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    R[(a, b, c, d)] = (A[a][c] * B[b][d] + A[b][d] * B[a][c]
                                       - A[a][d] * B[b][c] - A[b][c] * B[a][d])
    return R


def sym(entries):
    M = [[F(0)] * 4 for _ in range(4)]
    k = 0
    for i in range(4):
        for j in range(i, 4):
            M[i][j] = M[j][i] = F(entries[k])
            k += 1
    return M


def curvature(seed):
    A = sym([seed + i * 3 - 5 for i in range(10)])
    B = sym([F(7 - i * seed, 3 + i) for i in range(10)])
    C = sym([F(i * i - 4, 5) for i in range(10)])
    R1, R2 = kn(A, B), kn(C, C)
    return {key: R1[key] + F(seed, 2) * R2[key] for key in R1}


def is_algebraic_curvature(R):
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    v = R[(a, b, c, d)]
                    if v != -R[(b, a, c, d)] or v != R[(c, d, a, b)]:
                        return False
                    if v + R[(a, c, d, b)] + R[(a, d, b, c)] != 0:
                        return False
    return True


def metric(R, x, V, W):
    """g(V, W) at x for g_ab = eta_ab - (1/3) R_acbd x^c x^d."""
    tot = F(0)
    for a in range(4):
        tot += ETA[a] * V[a] * W[a]
    corr = F(0)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    corr += R[(a, c, b, d)] * V[a] * x[c] * W[b] * x[d]
    return tot - corr / 3


def boost_point(rho, s, y=(0, 0)):
    ch = (1 + s * s) / (1 - s * s)
    sh = 2 * s / (1 - s * s)
    x = [rho * sh, rho * ch, F(y[0]), F(y[1])]
    u = [rho * ch, rho * sh, F(0), F(0)]          # d x / d(rapidity)
    er = [sh, ch, F(0), F(0)]                       # d x / d rho
    return x, u, er


def check_local_boost_period():
    setup_geometry()
    SS = [F(0), F(1, 3), F(1, 2), F(-2, 5), F(3, 7)]
    RHOS = [F(1, 2), F(1, 3), F(2, 7)]
    KS = {1: F(9278, 1575), 2: F(984, 175), 5: F(68, 15)}
    for seed in (1, 2, 5):
        R = curvature(seed)
        GA.check("R is an algebraic curvature tensor (seed %d)" % seed, is_algebraic_curvature(R))
        k = R[(0, 1, 0, 1)] / 3
        GA.check("boost-plane coefficient k = R_0101/3 as computed (seed %d)" % seed, k == KS[seed])
        x, u, er = boost_point(F(1, 2), F(1, 3))
        GA.check("g_ll at rho = 1/2 equals -(1/4 + k/16)", metric(R, x, u, u) == -(F(1, 4) + KS[seed] / 16))
        GA.check("boost-plane curvature nonzero (seed %d)" % seed, k != 0)
        for rho in RHOS:
            for s in SS:
                x, u, er = boost_point(rho, s)
                GA.check("g_rr = 1", metric(R, x, er, er) == 1)
                GA.check("g_rl = 0", metric(R, x, er, u) == 0)
                GA.check("g_ll = -(rho^2 + k rho^4), rapidity independent",
                         metric(R, x, u, u) == -(rho * rho + k * rho ** 4))
        # F^2 = rho^2 + k rho^4: F'(0) = lim F^2/rho^2 = 1 whatever k
        r = RF.var()
        F2 = r * r + RF.const(k) * r * r * r * r
        GA.check("F^2/rho^2 -> 1 at rho = 0", (F2 / (r * r)).eval(F(0)) == 1)
        # negative control: off the plane the boost is not stationary at this order
        x0, u0, _ = boost_point(F(1, 2), F(0), (1, 2))
        x1, u1, _ = boost_point(F(1, 2), F(1, 2), (1, 2))
        GA.check("off-plane g_ll depends on rapidity (control)",
                 metric(R, x0, u0, u0) != metric(R, x1, u1, u1))
    return True


def check_acceleration_temperature():
    setup_geometry()
    r = RF.var()
    for k in (F(1, 3), F(-2, 5), F(7)):
        F2 = r * r + RF.const(k) * r * r * r * r
        dF2 = F2.deriv()
        # a = F'/F, proper inverse temperature 2 pi F; T/(a/2pi) = 1/F', and F'^2 = (F^2)'^2/(4 F^2)
        Fp2 = dF2 * dF2 / (RF.const(4) * F2)
        GA.check("F'^2 = (1 + 2 k rho^2)^2/(1 + k rho^2)",
                 Fp2.eqrf((RF.const(1) + RF.const(2 * k) * r * r) * (RF.const(1) + RF.const(2 * k) * r * r)
                          / (RF.const(1) + RF.const(k) * r * r)))
        GA.check("T = a/2pi at rho = 0", Fp2.eval(F(0)) == 1)
        # second-order coefficient 3k: (F'^2 - 1)/rho^2 -> 3k
        GA.check("first correction 3 k rho^2", ((Fp2 - RF.const(1)) / (r * r)).eval(F(0)) == 3 * k)
        GA.check("correction nonzero when curvature is", not (Fp2 - RF.const(1)).is_zero())
    # flat control: k = 0 gives T = a/2pi exactly at every rho
    F2 = r * r
    Fp2 = F2.deriv() * F2.deriv() / (RF.const(4) * F2)
    GA.check("flat: T = a/2pi exactly", Fp2.eqrf(RF.const(1)))
    return True


def zeta(L, p):
    t, x1, x2, x3 = p
    rr = x1 * x1 + x2 * x2 + x3 * x3
    c = 1 / (2 * L)
    return [c * (L * L - t * t - rr), -c * 2 * t * x1, -c * 2 * t * x2, -c * 2 * t * x3]


def jac(L, p):
    """J[a][b] = d_a zeta^b, exact for a quadratic field by central differences."""
    h = F(1)
    J = []
    for a in range(4):
        pp = list(p)
        pm = list(p)
        pp[a] += h
        pm[a] -= h
        zp, zm = zeta(L, pp), zeta(L, pm)
        J.append([(zp[b] - zm[b]) / (2 * h) for b in range(4)])
    return J


def check_diamond_flow_unit_boost():
    setup_geometry()
    for L in (F(1), F(3, 2), F(5, 7)):
        for p in ([F(1, 3), F(1, 2), F(-1, 4), F(2, 5)], [F(0), F(1, 7), F(3), F(-2)],
                  [F(-5, 6), F(0), F(1, 9), F(4, 3)]):
            J = jac(L, p)
            div = sum(J[a][a] for a in range(4))
            ok = True
            for a in range(4):
                for b in range(4):
                    lhs = J[a][b] * ETA[b] + J[b][a] * ETA[a]      # d_a zeta_b + d_b zeta_a
                    rhs = (div / 2) * (ETA[a] if a == b else 0)
                    ok = ok and lhs == rhs
            GA.check("conformal Killing at a point", ok)
        for n in ([F(1), F(0), F(0)], [F(3, 5), F(4, 5), F(0)], [F(2, 7), F(3, 7), F(6, 7)]):
            edge = [F(0)] + [L * c for c in n]
            GA.check("zeta vanishes on the edge", zeta(L, edge) == [0, 0, 0, 0])
            J = jac(L, edge)
            # unit boost of the plane (t, n): d_t zeta = -n, d_n zeta^t = -1, zero on the edge sphere
            GA.check("d_t zeta = -n", J[0] == [F(0)] + [-c for c in n])
            dn_t = sum(n[i] * J[1 + i][0] for i in range(3))
            GA.check("d_n zeta^t = -1 (surface gravity 1)", dn_t == -1)
            GA.check("div zeta = 0 on the edge", sum(J[a][a] for a in range(4)) == 0)
    # control: a diamond field with the wrong normalisation has surface gravity 2, not 1
    edge = [F(0), F(1), F(0), F(0)]
    Jw = jac(F(1, 2), [F(0), F(1, 2), F(0), F(0)])
    GA.check("the 1/(2L) normalisation gives surface gravity 1 at every radius", Jw[1][0] == -1)
    GA.check("edge point is off the half-size edge", zeta(F(1, 2), edge) != [0, 0, 0, 0])
    return True


# ---------------------------------------------------------------- algebra

NM = 3
SQ = GA.sig(NM, NM)


def m(*xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out


def v(k):
    return GA.scal(F(1, 2), GA.add(GA.gen(k), GA.gen(NM + k)))


def vs(k):
    return GA.scal(F(1, 2), GA.sub(GA.gen(k), GA.gen(NM + k)))


def Nk(k):
    return m(vs(k), v(k))


def gibbs(qs):
    out = GA.sc(1)
    for k, q in enumerate(qs):
        out = m(out, GA.add(GA.sc(1), GA.scal(q - 1, Nk(k))))
    return out


def tr(x):
    return x.get((), F(0))     # proportional to the matrix trace


def state(rho):
    z = tr(rho)
    return lambda x: tr(m(rho, x)) / z


def blades():
    return [{b: F(1)} for b in GA.all_blades(2 * NM)]


def kms_holds(rho, G, Ginv, basis):
    w = state(rho)
    for x in basis:
        gx = m(G, x, Ginv)
        for y in basis:
            if w(m(x, y)) != w(m(y, gx)):
                return False
    return True


def ad_equal(rho, rhoinv, G, Ginv, basis):
    return all(GA.eq(m(rho, x, rhoinv), m(G, x, Ginv)) for x in basis)


def check_window_kms_iff_modular():
    setup_algebra()
    basis = blades()
    GA.check("window algebra has 64 blades", len(basis) == 64)
    qs = [F(1, 3), F(2, 7), F(5, 11)]
    G = gibbs(qs)
    Ginv = gibbs([1 / q for q in qs])
    GA.check("G G^-1 = 1", GA.eq(m(G, Ginv), GA.sc(1)))
    # Ad(G) is the imaginary-time flow tau_{i beta} on the generators: G v_k = q_k^-1 v_k G and
    # G v_k^* = q_k v_k^* G (the KMS identity with Ad(G) itself holds for any invertible G by
    # cyclicity of the trace, so it is not tested positively; the controls below test it on other states)
    for k, q in enumerate(qs):
        GA.check("G v_k G^-1 = q_k^-1 v_k", GA.eq(m(G, v(k)), GA.scal(1 / q, m(v(k), G))))
        GA.check("G v_k^* G^-1 = q_k v_k^*", GA.eq(m(G, vs(k)), GA.scal(q, m(vs(k), G))))
    # Fermi-Dirac occupations q/(1 + q) = (e^(2 pi w) + 1)^(-1), the I-state symbol, mode by mode
    w = state(G)
    GA.check("occupations are Fermi-Dirac", [w(Nk(k)) for k in range(NM)] == [F(1, 4), F(2, 9), F(5, 16)])
    GA.check("modes uncorrelated in the Gibbs state", w(m(Nk(0), Nk(1))) == F(1, 4) * F(2, 9))
    # centre = scalars: commutators with the 6 generators have joint kernel of dimension 1
    rows = []
    for x in basis:
        row = []
        for i in range(2 * NM):
            c = GA.sub(m(x, GA.gen(i)), m(GA.gen(i), x))
            row.extend(GA.basis_vector_of(c, GA.all_blades(2 * NM)))
        rows.append(row)
    GA.check("centre of the window is the scalars (rank 63)", GA.mat_rank(rows) == 63)
    # faithful non-Gibbs controls
    bad_q = gibbs([F(1, 3), F(2, 7), F(4, 11)])
    bad_q_inv = gibbs([F(3), F(7, 2), F(11, 4)])
    GA.check("other Boltzmann factor: not KMS", not kms_holds(bad_q, G, Ginv, basis))
    GA.check("other Boltzmann factor: modular group differs", not ad_equal(bad_q, bad_q_inv, G, Ginv, basis))
    hop = GA.add(m(vs(0), v(1)), m(vs(1), v(0)))
    rho_h = GA.add(G, GA.scal(F(1, 50), hop))
    GA.check("hop-perturbed state: not KMS", not kms_holds(rho_h, G, Ginv, basis))
    GA.check("hop-perturbed state: Ad(rho) differs from Ad(G) on N_0",
             not GA.eq(m(rho_h, Nk(0)), m(G, Nk(0), Ginv, rho_h)))
    for k, q in ((0, qs[0]), (1, qs[1])):
        GA.check("hop-perturbed state does not implement tau_{i beta} on the hopping modes",
                 not GA.eq(m(rho_h, v(k)), GA.scal(1 / q, m(v(k), rho_h))))
    # same single-mode marginals, correlated modes: satisfies the local form of (R) mode by mode,
    # fails the joint condition (R_loc)
    s01 = m(GA.sub(GA.scal(2, Nk(0)), GA.sc(1)), GA.sub(GA.scal(2, Nk(1)), GA.sc(1)))
    rho_c = GA.add(G, GA.scal(F(1, 20), s01))
    wc = state(rho_c)
    for k in range(NM):
        for x in (Nk(k), v(k), vs(k), m(vs(k), v(k), Nk(k))):
            GA.check("correlated state: single-mode marginals unchanged", wc(x) == w(x))
    GA.check("correlated state: modes 0 and 1 correlated", wc(m(Nk(0), Nk(1))) != F(1, 4) * F(2, 9))
    GA.check("correlated state: not jointly KMS", not kms_holds(rho_c, G, Ginv, basis))
    GA.check("correlated state: Ad(rho) is not tau_{i beta} on v_0",
             not GA.eq(m(rho_c, v(0)), GA.scal(3, m(v(0), rho_c))))
    # scale freedom only: c G gives the same state and the same modular group
    cG = GA.scal(F(7, 3), G)
    GA.check("c G: same state", all(state(cG)(x) == w(x) for x in basis))
    GA.check("c G implements tau_{i beta}", all(GA.eq(m(cG, v(k)), GA.scal(1 / q, m(v(k), cG)))
                                                for k, q in enumerate(qs)))
    GA.check("c G: same modular group", ad_equal(cG, GA.scal(F(3, 7), Ginv), G, Ginv, basis))
    return True
