"""The trace anomaly against a radiation-type descent: exact checks.

The Robertson-Walker gauge field hb^{-1}(gamma_i) = a(t) gamma_i on flat spacetime, in the store's sign
(lib/gtg.py): field strength, Euler density as -4 Tr((I_4 R)^2), the radiation field a = t^(1/2); the anomaly
weights of the three spins from the stored heat-kernel coefficient; the anomalous stress map of Weyl-flat fields,
its trace and its conservation; power-law origins; the bound on the branch joined to late radiation and the
numbers for the stored content. Exact arithmetic only (Fractions); pi enters only through stated rational
combinations and the bracket 314/100 < pi < 315/100.
"""
from fractions import Fraction as F
import GA
import gtg
from tp_premise import premise, quantity

S = gtg.S13
WALL = "synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state"
HEAT = "synthesis.imported-heat-kernel-coefficients-and-background-field-gauge"
SAKH = "synthesis.imported-sakharov-induced-gravity-coefficients"
ATTM = "synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations"
CONT = "synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike"
STRS = "synthesis.imported-renormalised-stress-tensor-of-hadamard-dirac-states"
EINS = "synthesis.imported-einstein-cartan-matter-coupling"
CEIL = "dark-matter.ceiling-valued-inherited-success"

INSTANTS = ((F(2), F(3), F(5)), (F(1), F(1, 2), F(-1, 4)), (F(7, 3), F(-2), F(11, 5)), (F(3), F(1), F(0)))


def _planes():
    return [(a, b) for a in range(4) for b in range(a + 1, 4)]


def dual_trace(Rc):
    """-4 Tr((I_4 R)^2): the trace over the six frame planes of B -> I_4 R(I_4 R(B)), times -4."""
    R = gtg.as_op(Rc)
    I4 = gtg.pseudoscalar(S)
    tot = F(0)
    for (a, b) in _planes():
        B = gtg.wedge(GA.gen(a), GA.gen(b), S)
        X = gtg.m_mul(I4, R(gtg.grade(gtg.m_mul(I4, R(B), S), 2)), S)
        Brec = gtg.wedge(gtg.er(b, S), gtg.er(a, S), S)       # reciprocal plane, <Brec B> = 1
        tot += gtg.sp(gtg.m_mul(Brec, X, S))
    return -4 * tot


def radiation_field(base=2):
    tau, fld0 = gtg.kasner_field((F(1, 2), F(1, 2), F(1, 2)), base)
    return tau, gtg.Field(fld0.TH).curvature()


# ---------------------------------------------------------------- check 1
def check_euler_density_of_the_robertson_walker_gauge_field():
    """(i): R(g0 ^ gi) = (addot/a) g0 gi, R(gi ^ gj) = H^2 gi gj (store sign), Weyl part zero, scalar
    6(addot/a + H^2), Euler density 24 H^2 addot/a = -4 Tr((I_4 R)^2); on the radiation field the scalar is 0 and
    the Euler density is -3/(2 t^4) = -2 Ric.Ric; the dual-trace form also on Weyl-curved fields."""
    premise(WALL)
    ok = True
    for (a, ad, add) in INSTANTS:
        Rc = gtg.flrw_flat(a, ad, add).curvature()
        H2, q = (ad / a) ** 2, add / a
        for i in range(1, 4):
            ok = ok and GA.eq(Rc[(0, i)], GA.scal(q, gtg.biv(0, i))) if q != 0 else ok and Rc[(0, i)] == {}
            for j in range(i + 1, 4):
                ok = ok and GA.eq(Rc[(i, j)], GA.scal(H2, gtg.biv(i, j)))
        ok = ok and all(not v for v in gtg.weyl_op(Rc).values())
        ok = ok and gtg.ricci_scalar(Rc) == 6 * (q + H2)
        E = gtg.euler_density(Rc)
        ok = ok and E == 24 * H2 * q and dual_trace(Rc) == E
    for base in (2, 3):
        t, Rc = radiation_field(base)
        E = gtg.euler_density(Rc)
        ok = ok and gtg.ricci_scalar(Rc) == 0 and all(not v for v in gtg.weyl_op(Rc).values())
        ok = ok and gtg.ricci_sq(Rc) == F(3, 4) / t ** 4
        ok = ok and E == F(-3, 2) / t ** 4 and E == -2 * gtg.ricci_sq(Rc) and dual_trace(Rc) == E
    # off the Weyl-flat class: a vacuum Kasner field and a Bianchi field with matter
    for p in ((F(2, 3), F(2, 3), F(-1, 3)), (F(1, 2), F(1, 3), F(1, 5))):
        tau, fld0 = gtg.kasner_field(p, 2)
        Rc = gtg.Field(fld0.TH).curvature()
        ok = ok and dual_trace(Rc) == gtg.euler_density(Rc) and gtg.euler_density(Rc) != 0
        Wc = gtg.weyl_op(Rc)
        ok = ok and any(v for v in Wc.values())
        # the three parts: W and S = (R/12) id commute with the duality, Z = R - W - S anticommutes with it
        I4 = gtg.pseudoscalar(S)
        Rop, Wop, s12 = gtg.as_op(Rc), gtg.as_op(Wc), gtg.ricci_scalar(Rc) / 12

        def Zop(B):
            return gtg.m_sub(Rop(B), gtg.m_add(Wop(B), gtg.m_scal(s12, B)))
        trW = trZ = F(0)
        for (a, b) in _planes():
            B = gtg.wedge(GA.gen(a), GA.gen(b), S)
            sB = gtg.grade(gtg.m_mul(I4, B, S), 2)
            ok = ok and GA.eq(Wop(sB), gtg.grade(gtg.m_mul(I4, Wop(B), S), 2))
            ok = ok and GA.eq(Zop(sB), gtg.m_neg(gtg.grade(gtg.m_mul(I4, Zop(B), S), 2)))
            Brec = gtg.wedge(gtg.er(b, S), gtg.er(a, S), S)
            trW += gtg.sp(gtg.m_mul(Brec, Wop(Wop(B)), S))
            trZ += gtg.sp(gtg.m_mul(Brec, Zop(Zop(B)), S))
        ok = ok and 4 * trW == gtg.kretschmann(Wc)
        ok = ok and 4 * trZ == 2 * gtg.ricci_sq(Rc) - gtg.ricci_scalar(Rc) ** 2 / 2
    GA.check("Robertson-Walker gauge field: field strength, Euler density 24 H^2 addot/a = -4 Tr((I_4 R)^2); "
             "radiation field: scalar 0, Euler density -3/(2 t^4) = -2 Ric.Ric", ok)
    return ok


# ---------------------------------------------------------------- check 2
def a4_triple(dim, eR=F(0), eRic=F(0), om=F(0)):
    """360 times the local a_4 density of the stored Fact (i) without total derivatives,
    tr(60 R E + 180 E^2 + 5 R^2 - 2 Ric^2 + 2 Riem^2 + 30 Om.Om), as coefficients of (Riem^2, Ric^2, R^2).
    dim: fibre dimension; E = eR R id (scalar, spinor) or E = eRic Ric on the vector index (tr E = eRic R,
    tr E^2 = eRic^2 Ric^2); om: tr(Om_ij Om_ij) as a multiple of Riem^2."""
    return (2 * dim + 30 * om,
            -2 * dim + 180 * eRic ** 2,
            5 * dim + 60 * (eR * dim + eRic) + 180 * eR ** 2 * dim)


def weyl_euler(t):
    """(Riem^2, Ric^2, R^2) -> (c, a, r) with t = c W^2 - a E + r R^2, W^2 = Riem^2 - 2 Ric^2 + R^2/3,
    E = Riem^2 - 4 Ric^2 + R^2."""
    riem, ric, r2 = t
    a = (ric + 2 * riem) / 2
    c = riem + a
    return (c, a, r2 - c / 3 + a)


def _tscale(s, t):
    return tuple(s * x for x in t)


def _tadd(*ts):
    return tuple(sum(x) for x in zip(*ts))


def check_anomaly_weights_from_the_stored_heat_kernel_coefficient():
    """(ii): spin-curvature traces computed in the algebra (spinor -K/2, vector -K); weights (c, a) = (3, 1),
    (9, 11/2), (36, 62) for a real scalar, a Weyl field and a gauge vector with its ghosts, in units of
    1/(360 (4 pi)^2); no R^2 remainder for the conformal fields, 5 for the minimal scalar; the stored content
    48 Weyl + 12 vectors has a = 1008 = 28 x 36 (1016 with eight scalars); with n_{1/2} = 4 n_1 and
    n'_0 = 3 n_1 both coefficients cancel exactly for dimension-zero weights (-28, -8)."""
    premise(HEAT)
    premise(SAKH)
    premise(ATTM)
    premise(CONT)
    ok = True
    # connection-curvature traces on a field with Weyl and Ricci parts both nonzero
    tau, fld0 = gtg.kasner_field((F(1, 2), F(1, 3), F(1, 5)), 2)
    Rc = gtg.Field(fld0.TH).curvature()
    R = gtg.as_op(Rc)
    K = gtg.kretschmann(Rc)
    spin = F(0)
    vect = F(0)
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            A = R(gtg.wedge(GA.gen(i), GA.gen(j), S))
            B = R(gtg.wedge(gtg.er(i, S), gtg.er(j, S), S))
            # spinors: Om_ij = (1/2) R(e_i ^ e_j) by left multiplication; the trace over the four-dimensional
            # module of a product of two bivectors is four times its scalar part
            spin += 4 * gtg.sp(gtg.m_mul(gtg.m_scal(F(1, 2), A), gtg.m_scal(F(1, 2), B), S))
            # vectors: Om_ij v = R(e_i ^ e_j) . v; trace of the composite over the frame
            for m in range(4):
                v = gtg.bdot(A, gtg.bdot(B, GA.gen(m), S), S)
                vect += gtg.vdot(gtg.er(m, S), v, S)
    ok = ok and K != 0 and spin == -K / 2 and vect == -K
    scal = a4_triple(1, eR=F(-1, 6))                               # real scalar, weight 2 w = 1
    scal0 = a4_triple(1)                                           # minimal coupling
    dirac = _tscale(-1, a4_triple(4, eR=F(-1, 4), om=F(-1, 2)))    # sigma = -1, 2 w = 1
    weyl_f = _tscale(F(1, 2), dirac)
    vec = _tadd(a4_triple(4, eRic=F(-1), om=F(-1)), _tscale(-2, a4_triple(1)))   # less two ghost scalars
    ok = ok and scal == (2, -2, 0) and dirac == (7, 8, -5) and vec == (-26, 176, -50)
    ok = ok and weyl_euler(scal) == (3, 1, 0) and weyl_euler(scal0) == (3, 1, 5)
    ok = ok and weyl_euler(weyl_f) == (9, F(11, 2), 0) and weyl_euler(vec) == (36, 62, 0)
    aS, aW, aV = weyl_euler(scal)[1], weyl_euler(weyl_f)[1], weyl_euler(vec)[1]
    cS, cW, cV = weyl_euler(scal)[0], weyl_euler(weyl_f)[0], weyl_euler(vec)[0]
    ok = ok and aS > 0 and aW > 0 and aV > 0
    n_weyl, n_vec, n_scal = 48, 12, 8
    a_content = n_weyl * aW + n_vec * aV
    ok = ok and a_content == 1008 and a_content == 28 * 36 and a_content + n_scal * aS == 1016
    ok = ok and (n_weyl * cW + n_vec * cV) / cS == 288
    # the stored Fact (c): n_{1/2} = 4 n_1 and n'_0 = 3 n_1 cancel both coefficients for one pair of weights
    a0 = -(4 * aW + aV) / 3
    c0 = -(4 * cW + cV) / (3 * cS)
    ok = ok and a0 == -28 and c0 == -8
    GA.check("anomaly weights from the stored a_4: (c, a) = (3, 1), (9, 11/2), (36, 62); content 1008 = 28 x 36, "
             "1016 with the eight scalars", ok)
    return ok


# ---------------------------------------------------------------- check 3
def anomalous_stress(Rc, a):
    """T_A(a)/alpha = 2 [Ric(Ric(a)) - (2/3) R Ric(a) - (1/2)(Ric.Ric) a + (1/4) R^2 a]."""
    r = gtg.ricci_scalar(Rc)
    Ra = gtg.ricci(Rc, a)
    return gtg.m_scal(2, gtg.m_add(gtg.ricci(Rc, Ra), gtg.m_scal(-F(2, 3) * r, Ra),
                                   gtg.m_scal(-gtg.ricci_sq(Rc) / 2 + r * r / 4, a)))


N = 6


def _d(x):
    return [x[k + 1] * (k + 1) for k in range(len(x) - 1)] + [F(0)]


def _m(x, y):
    return GA.ps_mul(x, y, N)


def _sub(x, y):
    return [u - v for u, v in zip(x, y)]


def _addl(*xs):
    return [sum(c) for c in zip(*xs)]


def _sc(s, x):
    return [s * u for u in x]


def _hubble_data(a):
    """Truncated series in t - t0: H, addot/a and the scalar R = 6(addot/a + H^2)."""
    ainv = GA.ps_inv(a, N)
    H = _m(_d(a), ainv)
    q = _m(_d(_d(a)), ainv)
    return H, q, _sc(6, _addl(q, _m(H, H)))


def check_anomalous_stress_map_its_trace_and_conservation():
    """(iii): on the Robertson-Walker field T_A(g0) = 6 alpha H^4 g0, T_A(gi) = -alpha (2 H^4 - 8 H^2 addot/a) gi,
    trace alpha E; rho_A' + 3H(rho_A + P_A) = 0 and rho_b' + 4 H rho_b = H box R for the free term
    rho_b = H R' - R^2/12 + H^2 R, as identities in the Taylor coefficients of a; radiation field:
    rho_A = 3/(8 t^4), P_A = 5/(8 t^4), and the free term vanishes."""
    premise(STRS)
    premise(SAKH)
    ok = True
    for (a, ad, add) in INSTANTS:
        Rc = gtg.flrw_flat(a, ad, add).curvature()
        H2, q = (ad / a) ** 2, add / a
        rho, P = 6 * H2 * H2, 2 * H2 * H2 - 8 * H2 * q
        ok = ok and GA.eq(anomalous_stress(Rc, GA.gen(0)), GA.scal(rho, GA.gen(0)))
        for i in range(1, 4):
            Ti = anomalous_stress(Rc, GA.gen(i))
            ok = ok and (GA.eq(Ti, GA.scal(-P, GA.gen(i))) if P != 0 else Ti == {})
        tr = sum((gtg.vdot(gtg.er(m, S), anomalous_stress(Rc, GA.gen(m)), S) for m in range(4)), F(0))
        ok = ok and tr == gtg.euler_density(Rc) and tr == rho - 3 * P
    # conservation as identities in the Taylor coefficients of the scale factor
    for a in ([F(2), F(3), F(5, 2), F(-1, 3), F(7, 4), F(1, 5), F(-2, 7)],
              [F(1), F(-1, 2), F(2, 3), F(4), F(-3, 5), F(1, 7), F(5, 11)]):
        H, q, R = _hubble_data(a)
        H2 = _m(H, H)
        rhoA = _sc(6, _m(H2, H2))
        PA = _sub(_sc(2, _m(H2, H2)), _sc(8, _m(H2, q)))
        resA = _addl(_d(rhoA), _sc(3, _m(H, _addl(rhoA, PA))))
        ok = ok and all(c == 0 for c in resA[:N - 2]) and any(c != 0 for c in rhoA[:2])
        traceA = _sub(rhoA, _sc(3, PA))
        ok = ok and traceA[:N - 2] == _sc(24, _m(H2, q))[:N - 2]
        rhob = _addl(_m(H, _d(R)), _sc(F(-1, 12), _m(R, R)), _m(H2, R))
        boxR = _addl(_d(_d(R)), _sc(3, _m(H, _d(R))))
        resb = _sub(_addl(_d(rhob), _sc(4, _m(H, rhob))), _m(H, boxR))
        ok = ok and all(c == 0 for c in resb[:N - 4]) and any(c != 0 for c in rhob[:1])
    # the radiation field about t0 = 4: a = 2 (1 + s/4)^(1/2)
    t0 = F(4)
    a = _sc(2, GA.ps_pow_rat([F(1), F(1, 4)] + [F(0)] * (N - 1), F(1, 2), N))
    H, q, R = _hubble_data(a)
    H2 = _m(H, H)
    ok = ok and all(c == 0 for c in R[:N - 2])
    ok = ok and 6 * H2[0] ** 2 == F(3, 8) / t0 ** 4
    ok = ok and 2 * H2[0] ** 2 - 8 * H2[0] * q[0] == F(5, 8) / t0 ** 4
    GA.check("anomalous stress map on Weyl-flat fields: rho_A = 6 alpha H^4, trace alpha E, conserved; free term "
             "conserved and zero on the radiation field, where rho_A = 3/(8 t^4), P_A = 5/(8 t^4)", ok)
    return ok


# ---------------------------------------------------------------- check 4
def check_no_power_law_origin_is_tame_unless_the_anomaly_vanishes():
    """(iv): for a = t^p the order t^-4 of the density is 6 alpha p^4 - 9 b p^2 (2p - 1) and of the trace
    12 p (p - 1)[2 alpha p^2 - 3 b (2p - 1)]; at p = 1/2 both are nonzero for every b unless alpha = 0
    (3 alpha/8 and -3 alpha/2); a power law p != 1/2 solves at leading order exactly for b = 2 alpha p^2/(3(2p-1));
    on the exact radiation field the scalar is zero, so the trace of the field equation fails by alpha E."""
    premise(WALL)
    premise(EINS)
    ok = True
    half = F(1, 2)
    for alpha in (F(0), F(1), F(127, 720), F(7, 40)):
        for p in (F(1, 2), F(1, 3), F(2, 3), F(2, 5), F(3, 4), F(49, 100)):
            Hc = p                                  # H = p/t
            Rc_ = 6 * p * (2 * p - 1)               # R = Rc_/t^2
            dR = -2 * Rc_                           # R' = dR/t^3
            ddR = 6 * Rc_                           # R'' = ddR/t^4
            rb = Hc * dR - Rc_ * Rc_ / 12 + Hc * Hc * Rc_
            ok = ok and rb == -9 * p * p * (2 * p - 1)
            box = ddR + 3 * Hc * dR
            ok = ok and box == 36 * p * (2 * p - 1) * (1 - p)
            E4 = 24 * p ** 3 * (p - 1)
            for b in (F(0), F(1), F(-1), F(5, 3), F(-7, 2), F(1000)):
                rho4 = 6 * alpha * p ** 4 + b * rb
                T4 = alpha * E4 + b * box
                ok = ok and 4 * (p - 1) * rho4 == p * T4               # conservation at leading order
                ok = ok and T4 == 12 * p * (p - 1) * (2 * alpha * p * p - 3 * b * (2 * p - 1))
                if p == half:
                    ok = ok and rho4 == F(3, 8) * alpha and T4 == F(-3, 2) * alpha
                    ok = ok and ((rho4 == 0) == (alpha == 0))
            if p != half:
                bstar = 2 * alpha * p * p / (3 * (2 * p - 1))
                ok = ok and 6 * alpha * p ** 4 + bstar * rb == 0
    # the quadratic 2 alpha p^2 - 6 b p + 3 b = 0 has the root p = 1/2 only at alpha = 0
    for b in (F(1), F(-1), F(5, 3), F(-7, 2)):
        ok = ok and 2 * F(0) * half * half - 6 * b * half + 3 * b == 0
        ok = ok and 2 * F(1) * half * half - 6 * b * half + 3 * b == half
    # exact radiation field: scalar 0, Euler density nonzero
    t, Rc = radiation_field(2)
    ok = ok and gtg.ricci_scalar(Rc) == 0 and gtg.euler_density(Rc) == F(-3, 2) / t ** 4
    # tameness in cosmic time holds only at 2p = 1 (the stored clause (iv)): the bracket's cometric is -t^(2p)
    ok = ok and [p for p in (F(1, 3), F(2, 5), F(1, 2), F(49, 100), F(2, 3)) if 2 * p == 1] == [half]
    GA.check("power-law origins: order t^-4 balance 2 alpha p^2 = 3 b (2p - 1); p = 1/2 only at alpha = 0", ok)
    return ok


# ---------------------------------------------------------------- check 5
def check_branch_bound_and_the_numbers_for_the_stored_content():
    """(v), (vi): with b = 0, 3 H^2 (1 - x) = rho_r/Mbar^2, x = 2 alpha H^2/Mbar^2; x(1 - x) <= 1/4, so
    rho_r <= 3 Mbar^4/(8 alpha) and H^2 <= Mbar^2/(4 alpha) on the branch joined to late radiation; with no
    radiation x = 0 or 1. Stored content: alpha pi^2 = 127/720, g = 116, T_max^4 = (2025/3683) Mbar^4,
    2.09e18 < T_max < 2.12e18 GeV; at the ceiling 6e14 GeV, rho_r/rho_max in (6.6, 6.8)e-15 and the anomalous
    share of the density in (1.6, 1.7)e-15; t_eq^2 Mbar^2 pi^2 = 127/360, 0.94 < t_eq/t_P < 0.95."""
    premise(CONT)
    premise(CEIL)
    ok = True
    for x in (F(0), F(1, 7), F(1, 2), F(3, 4), F(1), F(9, 8)):
        ok = ok and F(1, 4) - x * (1 - x) == (x - F(1, 2)) ** 2
    ok = ok and [x for x in (F(0), F(1, 2), F(1), F(2)) if x * (1 - x) == 0] == [F(0), F(1)]
    a_units = 48 * F(11, 2) + 12 * 62 + 8                 # in units of one real scalar
    alpha_pi2 = a_units / 5760                            # alpha = a_units/(360 (4 pi)^2)
    ok = ok and a_units == 1016 and alpha_pi2 == F(127, 720)
    g = 8 + 2 * 12 + F(7, 8) * 2 * 48
    ok = ok and g == 116
    # rho_max = 3/(8 alpha) and rho_r = (pi^2/30) g T^4 (units Mbar = 1): T_max^4 = 90/(8 alpha pi^2 g)
    Tmax4 = 90 / (8 * alpha_pi2 * g)
    ok = ok and Tmax4 == F(2025, 3683)
    ok = ok and F(86, 100) ** 4 < Tmax4 < F(87, 100) ** 4
    Mbar = quantity("quantity.reduced-planck-mass")       # GeV
    ok = ok and F(209, 100) * 10 ** 18 < F(86, 100) * Mbar and F(87, 100) * Mbar < F(212, 100) * 10 ** 18
    Tc = F(6) * 10 ** 15                                  # the stored ceiling on the rung scale, GeV
    r = (Tc / Mbar) ** 4 / Tmax4                          # rho_r/rho_max at the ceiling
    ok = ok and F(66, 10) / 10 ** 15 < r < F(68, 10) / 10 ** 15
    x0 = r / 4 * (1 + r)                                  # x(1 - x) = r/4 has its small root below x0
    ok = ok and x0 * (1 - x0) > r / 4 and (r / 4) * (1 - r / 4) < r / 4
    ok = ok and F(16, 10) / 10 ** 15 < (r / 4) / (1 - r / 4) and x0 / (1 - x0) < F(17, 10) / 10 ** 15
    # |trace| = rho on the radiation field: (3 alpha/2) t^-4 = 3 Mbar^2/(4 t^2), t^2 = 2 alpha/Mbar^2
    teq2_pi2 = 2 * alpha_pi2
    ok = ok and teq2_pi2 == F(127, 360)
    # in Planck times, t_P = 1/(sqrt(8 pi) Mbar): (t_eq/t_P)^2 = 8 pi * 2 alpha = 127/(45 pi)
    lo, hi = F(127, 45) / F(315, 100), F(127, 45) / F(314, 100)
    ok = ok and 8 * teq2_pi2 == F(127, 45) and F(94, 100) ** 2 < lo and hi < F(95, 100) ** 2
    GA.check("branch bound rho_r <= 3 Mbar^4/(8 alpha); stored content: T_max^4 = 2025/3683 Mbar^4, share of the "
             "anomalous density at 6e14 GeV below 1.7e-15, t_eq between 0.94 and 0.95 Planck times", ok)
    return ok
