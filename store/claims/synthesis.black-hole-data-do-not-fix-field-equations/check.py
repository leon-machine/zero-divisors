"""synthesis.black-hole-data-do-not-fix-field-equations: exact checks.

Curvature of g = diag(-f, 1/f, r^2/(1 - x^2), r^2 (1 - x^2)) in coordinates (t, r, x = cos theta, phi), with
f = 1 - 2M/r + Q^2/r^2 - Lambda r^2/3, from the Christoffel symbols, as exact rational functions of r times truncated Taylor series in x about 1/2:
Ricci = 0 for Schwarzschild, Ricci = Lambda g for Schwarzschild-de Sitter, Kretschmann = 48 M^2/r^6 (so the (C1)
surface 2M/r^3 = 1 is sqrt(K/12) = 1, and flat space, K = 0, has none), and for Reissner-Nordstrom the mixed
Ricci components R^t_t = R^r_r = -Q^2/r^4, so R^t_t + R^r_r != 0 on the horizon r_+, and the Wald term of
f = beta R_ab R^ab is 4 pi beta (R^t_t + R^r_r) A there ((iv), at one mass and one Q^2). (ii) under (W): the
Einstein part of the Wald functional gives A/4G (binormal contraction -2), and the Wald densities of the two
quadratic monomials R_ab R^ab and R^2 vanish on Schwarzschild, at one radius. Along the Schwarzschild family
(five masses), from f itself: the horizon is the sign change of the monotone f at r = 2M, kappa = f'(2M)/2 =
1/4M, 1/T = 2 pi/kappa is fitted by a cubic through four masses (it is 8 pi M) and confirmed at the fifth, and
its integral S = int dM/T equals A/4 = pi r_h^2 at every mass, with A from the sphere metric.
Not tested: that a vacuum field solves the field equations of every L_f, Ricci monomials of degree above two,
and (iii)'s statement that the matter field equations differ from Einstein's (no field equations are derived).
"""
from fractions import Fraction as F
from itertools import product
import GA
from tp_premise import premise


# Quantities are truncated Taylor series in e = x - x0 (x0 = 1/2), orders 0..2, with coefficients exact
# rational functions of r (GA.RF). Derivatives in x shift the series down, so the metric is carried to order 2,
# the Christoffel symbols are valid to order 1 and the curvature at order 0, which is all that is compared.
RF0, RF1 = GA.RF0, GA.RF1
X0 = F(1, 2)


def S(c0, c1=None, c2=None):
    return [c0, c1 or RF0, c2 or RF0]


Z = S(RF0)


def sadd(a, b, s=1):
    return [a[i] + b[i] if s == 1 else a[i] - b[i] for i in range(3)]


def smul(a, b):
    return [a[0] * b[0], a[0] * b[1] + a[1] * b[0], a[0] * b[2] + a[1] * b[1] + a[2] * b[0]]


def sinv(a):
    c0, c1, c2 = a
    i0 = RF1 / c0
    return [i0, -(c1 * i0 * i0), (c1 * c1 * i0 - c2) * i0 * i0]


def sconst(c):
    return S(GA.RF.const(c))


def sd(a, i):
    """derivative in coordinate i of (t, r, x, phi)."""
    if i == 1:
        return [c.deriv() for c in a]
    if i == 2:
        return [a[1], a[2] + a[2], RF0]
    return Z


def zero0(a):
    return a[0].is_zero()


def eq0(a, b):
    return (a[0] - b[0]).is_zero()


def curvature(gdiag):
    n = 4
    ginv = [sinv(gdiag[i]) for i in range(n)]
    half = sconst(F(1, 2))
    G = {}
    for a, b, c in product(range(n), repeat=3):
        t = Z
        if a == c:
            t = sadd(t, sd(gdiag[a], b))
        if a == b:
            t = sadd(t, sd(gdiag[a], c))
        if b == c:
            t = sadd(t, sd(gdiag[b], a), -1)
        G[(a, b, c)] = smul(smul(half, ginv[a]), t)
    Riem = {}
    for a, b, c, d in product(range(n), repeat=4):
        t = sadd(sd(G[(a, b, d)], c), sd(G[(a, b, c)], d), -1)
        for e in range(n):
            t = sadd(t, smul(G[(a, c, e)], G[(e, b, d)]))
            t = sadd(t, smul(G[(a, d, e)], G[(e, b, c)]), -1)
        Riem[(a, b, c, d)] = t
    Ric = {}
    for b, d in product(range(n), repeat=2):
        t = Z
        for a in range(n):
            t = sadd(t, Riem[(a, b, a, d)])
        Ric[(b, d)] = t
    return Riem, Ric, ginv


def metric(M, Q2, Lam):
    r = GA.RF.var()
    f = RF1 - GA.RF.const(2 * M) / r + GA.RF.const(Q2) / (r * r) - GA.RF.const(Lam / 3) * r * r
    sx = S(GA.RF.const(1 - X0 * X0), GA.RF.const(-2 * X0), GA.RF.const(-1))      # 1 - x^2
    r2 = S(r * r)
    return [S(-f), S(RF1 / f), smul(r2, sinv(sx)), smul(r2, sx)]


def kretschmann(Riem, gdiag, ginv):
    t = Z
    for a, b, c, d in product(range(4), repeat=4):
        x = Riem[(a, b, c, d)]
        if zero0(x):
            continue
        w = smul(smul(gdiag[a], ginv[b]), smul(ginv[c], ginv[d]))
        t = sadd(t, smul(smul(x, x), w))
    return t


def check_black_hole_data():
    premise("synthesis.imported-wald-noether-charge-entropy")
    premise("synthesis.quarter-from-temperature")
    premise("scrambling.mode-count")
    premise("singularity.rate-discharge-hypothesis-iii")
    M = F(3, 2)
    # Schwarzschild: Ricci flat; Kretschmann 48 M^2 / r^6
    g = metric(M, F(0), F(0))
    Riem, Ric, ginv = curvature(g)
    assert all(zero0(Ric[(b, d)]) for b, d in product(range(4), repeat=2))
    K = kretschmann(Riem, g, ginv)
    r = GA.RF.var()
    assert eq0(K, S(GA.RF.const(48 * M * M) / (r * r * r * r * r * r)))
    # (C1): Planck curvature 2M/r^3 = 1 is sqrt(K/12) = 1; flat space has K = 0 and no such surface
    gflat = metric(F(0), F(0), F(0))
    Rf, Ricf, gi = curvature(gflat)
    assert all(zero0(v) for v in Rf.values())
    # Schwarzschild-de Sitter: Ricci = Lambda g
    Lam = F(1, 5)
    g2 = metric(M, F(0), Lam)
    _, Ric2, _ = curvature(g2)
    for b, d in product(range(4), repeat=2):
        target = smul(sconst(Lam), g2[b]) if b == d else Z
        assert eq0(Ric2[(b, d)], target)
    # Reissner-Nordstrom: R^t_t = R^r_r = -Q^2/r^4, R^x_x = R^phi_phi = Q^2/r^4 (traceless), nonzero on the horizon
    Q2 = F(5, 4)
    g3 = metric(M, Q2, F(0))
    _, Ric3, gi3 = curvature(g3)
    mixed = [smul(gi3[a], Ric3[(a, a)]) for a in range(4)]
    q = S(GA.RF.const(Q2) / (r * r * r * r))
    mq = S(GA.RF.const(-Q2) / (r * r * r * r))
    assert eq0(mixed[0], mq) and eq0(mixed[1], mq)
    assert eq0(mixed[2], q) and eq0(mixed[3], q)
    assert all(zero0(Ric3[(b, d)]) for b, d in product(range(4), repeat=2) if b != d)
    rh = M + 1                                    # r_+ = M + sqrt(M^2 - Q^2) = 3/2 + 1
    assert rh * rh - 2 * M * rh + Q2 == 0
    assert -g3[0][0].eval(rh) == 0                # the RN horizon: f(r_+) = 0
    assert (mixed[0][0] + mixed[1][0]).eval(rh) == -2 * Q2 / rh ** 4 != 0
    # Wald contraction for f = beta R_ab R^ab: 2 R^{bd} eps_ab eps^a_d = -2 (R^t_t + R^r_r); pointwise algebraic, so
    # evaluated at r_+ + 1, where 1/f is finite (R^t_t + R^r_r is the rational function above, nonzero at r_+)
    gv = [g3[a][0].eval(rh + 1) for a in range(4)]
    eps = {(0, 1): F(1), (1, 0): F(-1)}
    ginvv = [1 / x for x in gv]
    Rmix = [mixed[a][0].eval(rh + 1) for a in range(4)]
    Rup = {(b, b): ginvv[b] * Rmix[b] for b in range(4)}         # R^{bb} = g^{bb} R^b_b
    con = sum(2 * Rup.get((b, d), F(0)) * eps.get((a, b), F(0)) * ginvv[a] * eps.get((a, d), F(0))
              for a in range(4) for b in range(4) for d in range(4))
    assert con == -2 * (Rmix[0] + Rmix[1])
    # entropy term -2 pi beta con A = 4 pi beta (R^t_t + R^r_r) A (units of pi beta A)
    assert -2 * con == 4 * (Rmix[0] + Rmix[1])
    nrm = sum(eps.get((a, b), F(0)) ** 2 * ginvv[a] * ginvv[b] for a in range(4) for b in range(4))
    assert gv[0] * gv[1] == -1 and nrm == -2
    # (ii) under (W): Einstein part E = (1/16 pi G) (g g - g g)/2 gives -2 pi (nrm / 16 pi G) A = A/4G (units A/G);
    # the Wald densities of R_ab R^ab and R^2 are linear in Ricci, zero on Schwarzschild (Ricci-flat in r above)
    assert -2 * nrm / 16 == F(1, 4)
    gs = metric(M, F(0), F(0))
    gsv = [gs[a][0].eval(4 * M) for a in range(4)]
    Rs = [(sinv(gs[a])[0] * Ric[(a, a)][0]).eval(4 * M) for a in range(4)]
    con_s = sum(2 * (1 / gsv[b]) * Rs[b] * eps.get((a, b), F(0)) * (1 / gsv[a]) * eps.get((a, b), F(0))
                for a in range(4) for b in range(4))
    ricci_scalar = sum(Rs)
    assert con_s == 0 and 2 * ricci_scalar * nrm == 0
    # surface gravity, horizon locus and Hawking's integral along the Schwarzschild family, from f itself
    masses = (F(1), F(3, 2), F(7, 3), F(10), F(5, 7))
    inv_T, quarter_area = [], []
    for m in masses:
        fm = -metric(m, F(0), F(0))[0][0]         # f = 1 - 2m/r as a rational function of r
        rh_m = 2 * m
        assert fm.eval(rh_m) == 0 and fm.eval(m) < 0 and fm.eval(3 * m) > 0
        assert fm.deriv().eval(m) > 0 and fm.deriv().eval(3 * m) > 0
        kappa = fm.deriv().eval(rh_m) / 2
        assert kappa == 1 / (4 * m)
        inv_T.append(2 / kappa)                   # 1/T = 2 pi / kappa, units of pi
        # A = int r^2 dx dphi over x in [-1, 1], phi in [0, 2 pi]; sqrt(g_xx g_phiphi) = r^2 at order 0
        rr = GA.RF.var()
        gh = metric(m, F(0), F(0))
        assert (smul(gh[2], gh[3])[0] - rr * rr * rr * rr).is_zero()
        quarter_area.append(2 * 2 * rh_m ** 2 / 4)    # units of pi
    # 1/T through the first four masses by cubic interpolation, confirmed at the fifth, then integrated in M
    V = [[m ** k for k in range(4)] for m in masses[:4]]
    poly = GA.field_solve(V, inv_T[:4])
    assert poly == [0, 8, 0, 0] and GA.peval(poly, masses[4]) == inv_T[4]
    entropy = GA.ps_int(poly)                     # S(M) = int dM / T with S(0) = 0
    assert (len(masses) == len(quarter_area) and all(GA.peval(entropy, m) == qa for m, qa in zip(masses, quarter_area)))
    return True


# ---------------------------------------------------------------------------
# GTG proof (2026-11-07): Schwarzschild and Reissner-Nordstrom as Painleve-Gullstrand gauge fields on flat
# spacetime (rotation-gauge field from the engine, checked torsion-free), their store-sign curvature operators,
# Ricci maps and Kretschmann scalars 2 <calR(a ^ b) calR(d_b ^ d_a)>, and the Wald contraction read as the
# derivative of the Lagrangian along the curvature operator S(B) = -<B sigma> sigma, sigma = gamma_1 gamma_0 the
# unit bivector of the horizon's normal plane: -1/(8 pi G) for the Einstein term (so A/4G), zero for Ricci
# monomials on a vacuum field, and -2 beta (R^t_t + R^r_r) for beta Ric^2 at the Reissner-Nordstrom horizon.
# ---------------------------------------------------------------------------
import gtg  # noqa: E402

SCHW = [(F(1), [F(2), F(8), F(1, 2)]), (F(3, 2), [F(3), F(12)])]        # beta = sqrt(2M/r) rational
RN_M, RN_Q2, RN_R = F(3, 2), F(5, 4), [F(5, 2), F(9, 2)]                 # beta = sqrt(3/r - 5/(4 r^2)) rational
ANGLE = (F(3, 5), F(4, 5))
SIGMA = gtg.biv(1, 0)                                                    # sigma = gamma_1 gamma_0, sigma^2 = 1


def _wald_op(B):
    return gtg.m_scal(-gtg.sp(gtg.m_mul(B, SIGMA)), SIGMA)


def _along(L, R):
    """d/ds L(R + s S) at s = 0 for L a polynomial of degree <= 2 in the curvature operator."""
    up = L(gtg.op_add(R, _wald_op))
    dn = L(gtg.op_add(R, lambda B: gtg.m_neg(_wald_op(B))))
    return (up - dn) / 2


def check_gtg_black_hole_data():
    premise("synthesis.imported-wald-noether-charge-entropy")
    premise("singularity.rate-discharge-hypothesis-iii")
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    # the Wald direction: Riem^o(u, v, w, z) = (w ^ z) . S(u ^ v) = -eps_uv eps_wz on the frame (eps_tr = 1), so S is
    # the curvature operator whose (-,+,+,+) Riemann tensor is eps_ab eps_cd, with constant 1
    eps = {(0, 1): 1, (1, 0): -1}
    ok = ok and all(gtg.riem_o(_wald_op, gtg.e(u), gtg.e(v), gtg.e(w), gtg.e(z)) == -eps.get((u, v), 0) * eps.get((w, z), 0)
                    for u in range(4) for v in range(4) for w in range(4) for z in range(4))
    ric2 = lambda R: gtg.ricci_sq(R)                                     # noqa: E731
    for M, radii in SCHW:
        for r0 in radii:
            fld = gtg.schwarzschild_pg(M, r0, *ANGLE)
            ok = ok and fld.torsion_free()
            Rc = fld.curvature()
            typ = gtg.op_planes(gtg.op_type_d(M / (2 * r0 ** 3), SIGMA))
            ok = ok and all(gtg.m_sub(Rc[pl], typ[pl]) == {} for pl in Rc)
            ok = ok and gtg.ricci_flat(Rc) and gtg.kretschmann(Rc) == 48 * M * M / r0 ** 6
            lam_r = gtg.sp(gtg.m_mul(gtg.apply_op(Rc, SIGMA), SIGMA))       # radial eigenvalue 2M/r^3
            ok = ok and lam_r == 2 * M / r0 ** 3 and lam_r * lam_r == gtg.kretschmann(Rc) / 12
            ok = ok and _along(ric2, Rc) == 0 and _along(lambda R: gtg.ricci_scalar(R) ** 2, Rc) == 0
            ok = ok and _along(gtg.ricci_scalar, Rc) == -2                 # Einstein: E.eps.eps = -2/(16 pi G)
            if r0 == 2 * M:                                                 # horizon: (K . D) K = K/(4M)
                r = gtg.Jet.var(1, r0, 4, 2)
                K = {(0,): gtg.Jet.const(1, 4), (1,): (2 * M / r).pw(F(1, 2))}
                ok = ok and gtg.m_sub(fld.cov(0, K), gtg.m_scal(1 / (4 * M), gtg.m_val(K))) == {}
    # the Wald direction S(B) = -<B sigma> sigma has Ricci map -P_sigma (minus the projector on the normal plane)
    ok = ok and all(gtg.m_sub(gtg.ricci(_wald_op, gtg.e(a)), gtg.m_scal(-1 if a < 2 else 0, gtg.e(a))) == {}
                    for a in range(4))
    beta_rn = lambda r: (2 * RN_M / r - RN_Q2 / (r * r)).pw(F(1, 2))      # noqa: E731
    for r0 in RN_R:
        fld = gtg.pg_field(r0, ANGLE[0], ANGLE[1], beta_rn)
        ok = ok and fld.torsion_free()
        Rc = fld.curvature()
        q = RN_Q2 / r0 ** 4
        for a, lam in enumerate([-q, -q, q, q]):
            ok = ok and gtg.m_sub(gtg.ricci(Rc, gtg.e(a)), gtg.m_scal(lam, gtg.e(a))) == {}
        wald = _along(lambda R: gtg.ricci_sq(R), Rc)                       # per unit beta
        ok = ok and wald == -2 * (-q - q) and _along(gtg.ricci_scalar, Rc) == -2
        if r0 == RN_M + 1:                                               # r_+ = M + sqrt(M^2 - Q^2) = 5/2
            ok = ok and 1 - 2 * RN_M / r0 + RN_Q2 / (r0 * r0) == 0
            ok = ok and -2 * wald == -8 * RN_Q2 / r0 ** 4                   # entropy shift / (pi beta A)
    GA.check("GTG: Schwarzschild and RN curvature, Kretschmann, and the Wald contraction along -<B sigma> sigma", ok)
    assert ok
