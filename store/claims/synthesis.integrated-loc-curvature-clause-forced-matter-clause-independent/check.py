"""(Loc) on the integrated reading: the curvature clause on asymptotically calibrated fields, the matter clause independent.

Gauge Theory Gravity on flat spacetime, store sign (lib/gtg.py): signature (+,-,-,-), calR(B) the store curvature,
field equation G(b) + Lambda b = -kappa T(b), T(b) = (rho + p)(b.u)u - p b for a perfect fluid at rest (u = gamma_0).
(1) The flat Friedmann field hb^{-1}(e_i) = a(t) e_i at an instant with a = 1, da/dt = a1, d2a/dt2 = a2 has
    calR(gamma_i ^ gamma_j) = a1^2 gamma_i ^ gamma_j, calR(gamma_0 ^ gamma_i) = a2 gamma_0 ^ gamma_i (tabulated
    samples, linear in (a1^2, a2)); with a1^2 = a2 = Lambda/3 it is the de Sitter operator (Lambda/3) B.
(2) Friedmann: a perfect fluid (s = kappa rho, w = p/rho) with Lambda solves the field equation at the instant iff
    a1^2 = (s + Lambda)/3 and a2 = -s(1 + 3w)/6 + Lambda/3; then calR = (Lambda/3) Id + s K_w, affine in s with the
    de Sitter limit at s = 0 (samples).
(3) The Einstein static universe of radius A (stereographic jets about a point) has the curvature of the flat
    dust Friedmann-Lambda field at its inflection instant: a1 = 1/A, a2 = 0, Lambda = 1/A^2, kappa rho = 2/A^2;
    both Weyl-free.
(4) Reach: every isotropic Weyl-free value (beta, alpha) = (a1^2, a2) with beta > 0, -2 beta <= alpha < beta is
    the instant value of a flat Friedmann field with w in [0, 1], Lambda in [0, 3 beta), rho > 0 (tabulated grid).
(5) The narrowing fails for discontinuous densities: along flat dust Friedmann (Lambda = 0) the scalar curvature
    and S.S vary while S.S / calR^2 = 3/4 at every instant.
(6) Matter-dependent density: X(b) = calR0(b) + 4 t0(b) (t = 2 pi T, G = 1, 0 = trace-free part) vanishes on
    every Einstein-with-G pair; on the Einstein static universe of radius 2 with dust t = sigma, eta = 1/2,
    sigma = 1/4, Q = X.X = 3/16 and eta = 1/4 (1 + c Q) at c = 16/3; the Clausius defect t(k,k) + eta k.calR(k)
    vanishes for every sampled null k, and the field equation holds with G_e = 1/(4 eta) = 1/2; eta = 1/4 with
    sigma = 1/8 is the Einstein-with-G member (Q = 0).
"""
from fractions import Fraction as F
import GA
import gtg
from tp_premise import premise

J = gtg.Jet
E = [GA.gen(i) for i in range(4)]
ER = [gtg.er(i) for i in range(4)]
PLANES = [(a, b) for a in range(4) for b in range(a + 1, 4)]


def _frw(a1, a2):
    at = J.from_taylor(0, [F(1), F(a1), F(a2) / 2], 4)
    TH = [[J.const(0, 4) for _ in range(4)] for _ in range(4)]
    TH[0][0] = J.const(1, 4)
    for i in (1, 2, 3):
        TH[i][i] = at
    return gtg.Field(TH).curvature()


def _esu(A):
    X = [J.var(i, F(0), 4, 2) for i in range(4)]
    f = (2 * F(A)) * (1 + X[1] * X[1] + X[2] * X[2] + X[3] * X[3]).inv()
    TH = [[J.const(0, 4) for _ in range(4)] for _ in range(4)]
    TH[0][0] = J.const(1, 4)
    for i in (1, 2, 3):
        TH[i][i] = f
    return gtg.Field(TH).curvature()


def _iso(beta, alpha):
    """The isotropic Weyl-free operator with space-plane value beta and time-plane value alpha."""
    return {(a, b): {(a, b): (alpha if a == 0 else beta)} if (alpha if a == 0 else beta) else {} for (a, b) in PLANES}


def _same(R1, R2):
    return all(gtg.m_sub(R1[k], R2[k]) == {} for k in PLANES)


def _weyl_free(R):
    return all(v == {} for v in gtg.weyl_op(R).values())


def _fluid_T(s, w, b):
    """kappa T(b) for a perfect fluid at rest, kappa rho = s, p = w rho."""
    u = E[0]
    return gtg.m_sub(gtg.m_scal(s * (1 + w) * gtg.vdot(b, u), u), gtg.m_scal(s * w, b))


def _field_eq_holds(R, lam, s, w):
    return all(gtg.m_add(gtg.einstein_residual(R, E[b], lam), _fluid_T(s, w, E[b])) == {} for b in range(4))


def check_friedmann_instant_curvature():
    premise("synthesis.imported-gtg-dictionary")
    premise("synthesis.loc-independent-of-clausius-and-killing-data")
    ok = True
    # tabulated: (a1, a2) -> (space-plane value, time-plane value)
    table = [((F(1, 2), F(3, 5)), (F(1, 4), F(3, 5))), ((F(2), F(-1)), (F(4), F(-1))),
             ((F(1, 3), F(0)), (F(1, 9), F(0))), ((F(3), F(7, 2)), (F(9), F(7, 2)))]
    for (a1, a2), (beta, alpha) in table:
        R = _frw(a1, a2)
        ok = ok and _same(R, _iso(beta, alpha)) and _weyl_free(R)
    # de Sitter: a1^2 = a2 = Lambda/3 gives (Lambda/3) B on every plane
    R = _frw(F(1), F(1))
    ok = ok and all(R[k] == {k: F(1)} for k in PLANES)
    GA.check("Friedmann instant: calR = a1^2 on space planes, a2 on time planes, Weyl-free", ok)
    return ok


def check_friedmann_equations_and_affine_path():
    premise("synthesis.imported-gtg-dictionary")
    premise("synthesis.c-loc-entropy-clause-curvature-independent-density")
    ok = True
    # tabulated samples (a1, Lambda, w) -> (s, a2), s = 3 a1^2 - Lambda, a2 = -s(1+3w)/6 + Lambda/3
    table = [((F(1), F(1), F(0)), (F(2), F(0))), ((F(1), F(0), F(1, 3)), (F(3), F(-1))),
             ((F(2), F(3), F(1)), (F(9), F(-5))), ((F(1, 2), F(1, 4), F(1, 2)), (F(1, 2), F(-1, 8))),
             ((F(3, 2), F(0), F(0)), (F(27, 4), F(-9, 8)))]
    for (a1, lam, w), (s, a2) in table:
        ok = ok and s == 3 * a1 * a1 - lam and a2 == -s * (1 + 3 * w) / 6 + lam / 3
        R = _frw(a1, a2)
        ok = ok and s > 0 and _field_eq_holds(R, lam, s, w)
        # wrong a2 fails the field equation (control)
        ok = ok and not _field_eq_holds(_frw(a1, a2 + F(1, 7)), lam, s, w)
        # affine in s about the de Sitter operator: calR = (Lambda/3) Id + s K_w, K_w = (1/3) Ks - (1+3w)/6 Kt
        ok = ok and _same(R, _iso(lam / 3 + s / 3, lam / 3 - s * (1 + 3 * w) / 6))
    # s -> 0 limit: the de Sitter operator, calibrated (and Lambda = 0: the flat operator)
    for lam in (F(3), F(0)):
        ok = ok and _same(_iso(lam / 3, lam / 3), {k: ({k: lam / 3} if lam else {}) for k in PLANES})
    GA.check("Friedmann: field equation iff the two Friedmann relations; curvature affine in kappa rho, de Sitter at 0", ok)
    return ok


def check_einstein_static_universe_is_a_friedmann_inflection_instant():
    premise("synthesis.loc-independent-of-clausius-and-killing-data")
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    for A in (F(2), F(3), F(1, 2)):
        Re = _esu(A)
        lam, s = 1 / (A * A), 2 / (A * A)
        Rf = _frw(1 / A, F(0))
        ok = ok and _same(Re, Rf) and _weyl_free(Re)
        # both satisfy the dust field equation with Lambda = 1/A^2, kappa rho = 2/A^2
        ok = ok and _field_eq_holds(Re, lam, s, F(0)) and _field_eq_holds(Rf, lam, s, F(0))
        # the Friedmann relations at the instant: a1^2 = (s + Lambda)/3, a2 = -s/6 + Lambda/3 = 0
        ok = ok and (1 / A) ** 2 == (s + lam) / 3 and -s / 6 + lam / 3 == 0
        # control: a different radius does not match
        ok = ok and not _same(Re, _frw(1 / (A + 1), F(0)))
    GA.check("Einstein static universe curvature = flat dust Friedmann-Lambda at its inflection instant", ok)
    return ok


def _reach(beta, alpha):
    """(w, Lambda, s) of a flat Friedmann field through (beta, alpha), or None."""
    if not (beta > 0 and -2 * beta <= alpha < beta):
        return None
    if alpha >= -beta / 2:
        w, lam = F(0), 2 * alpha + beta
    else:
        w, lam = -(2 * alpha + beta) / (3 * beta), F(0)
    return w, lam, 3 * beta - lam


def check_flat_friedmann_reach():
    premise("synthesis.c-loc-entropy-clause-curvature-independent-density")
    ok = True
    for beta in (F(1), F(1, 4), F(9)):
        for alpha in (-2 * beta, -beta, -beta / 2, F(0), beta / 3, beta * F(99, 100)):
            w, lam, s = _reach(beta, alpha)
            ok = ok and 0 <= w <= 1 and 0 <= lam < 3 * beta and s > 0
            ok = ok and (s + lam) / 3 == beta and -s * (1 + 3 * w) / 6 + lam / 3 == alpha
    # the Einstein static value (beta, alpha) = (1/A^2, 0): dust with Lambda = 1/A^2
    ok = ok and _reach(F(1, 4), F(0)) == (F(0), F(1, 4), F(1, 2))
    # controls: alpha = beta is de Sitter (s = 0, not a fluid), alpha < -2 beta needs w > 1, beta <= 0 not reached
    ok = ok and _reach(F(1), F(1)) is None and _reach(F(1), F(-3)) is None and _reach(F(-1), F(0)) is None
    GA.check("flat Friedmann fields with w in [0,1], Lambda >= 0 reach every -2 beta <= alpha < beta, beta > 0", ok)
    return ok


def _ric_sq_scal(R):
    sc = gtg.ricci_scalar(R)
    rs = gtg.ricci_sq(R)
    return sc, rs - sc * sc / 4


def check_degree_zero_density_escapes_on_flat_dust():
    premise("synthesis.loc-independent-of-clausius-and-killing-data")
    ok = True
    vals = []
    for a1 in (F(1), F(1, 2), F(2, 3)):
        s = 3 * a1 * a1
        R = _frw(a1, -s / 6)
        ok = ok and _field_eq_holds(R, F(0), s, F(0))
        sc, ss = _ric_sq_scal(R)
        vals.append((sc, ss))
        ok = ok and ss == F(3, 4) * sc * sc and sc != 0
    ok = ok and len(set(v[0] for v in vals)) == 3
    # control: radiation (w = 1/3) is trace-free, so the same ratio is not available there
    R = _frw(F(1), -F(1))
    ok = ok and gtg.ricci_scalar(R) == 0
    GA.check("flat dust Friedmann: S.S / calR^2 = 3/4 at every instant while calR varies", ok)
    return ok


def _tracefree(Tmap):
    tr = sum((gtg.vdot(ER[m], Tmap(E[m])) for m in range(4)), F(0))
    return lambda b: gtg.m_sub(Tmap(b), gtg.m_scal(tr / 4, b))


def _Q(R, tmap):
    Rc0 = _tracefree(lambda b: gtg.ricci(R, b))
    t0 = _tracefree(tmap)
    X = lambda b: gtg.m_add(Rc0(b), gtg.m_scal(4, t0(b)))
    return sum((gtg.vdot(X(E[m]), X(ER[m])) for m in range(4)), F(0))


def _dust_t(sigma):
    return lambda b: gtg.m_scal(sigma * gtg.vdot(b, E[0]), E[0])


NULLS = [(1, 1, 0, 0), (1, 0, 1, 0), (5, 3, 4, 0), (3, -2, 2, 1), (9, 4, -4, 7)]


def check_matter_dependent_density_counter_model():
    premise("synthesis.einstein-equations-from-c-loc-and-clausius")
    premise("synthesis.loc-independent-of-clausius-and-killing-data")
    premise("synthesis.c-loc-entropy-clause-curvature-independent-density")
    ok = True
    # (a) Q = 0 on Einstein-with-G pairs: Friedmann fluids with t = kappa T / 4 (kappa = 8 pi, t = 2 pi T)
    for a1, lam, w in [(F(1), F(1), F(0)), (F(1), F(0), F(1, 3)), (F(2), F(3), F(1))]:
        s = 3 * a1 * a1 - lam
        R = _frw(a1, -s * (1 + 3 * w) / 6 + lam / 3)
        tmap = lambda b, s=s, w=w: gtg.m_scal(F(1, 4), _fluid_T(s, w, b))
        ok = ok and _Q(R, tmap) == 0
    # (b) the Einstein static universe of radius 2 with dust t = sigma u u
    Re = _esu(F(2))
    lam = F(1, 4)
    c = F(16, 3)
    for eta, sigma, q in [(F(1, 2), F(1, 4), F(3, 16)), (F(1, 4), F(1, 8), F(0))]:
        tmap = _dust_t(sigma)
        Q = _Q(Re, tmap)
        ok = ok and Q == q and eta == F(1, 4) * (1 + c * Q)
        # field equation with G_e = 1/(4 eta): G(b) + Lambda b = -t(b)/eta
        ok = ok and all(gtg.m_add(gtg.einstein_residual(Re, E[b], lam), gtg.m_scal(1 / eta, tmap(E[b]))) == {}
                        for b in range(4))
        # Clausius defect at leading order: t(k,k) + eta k.calR(k) = 0 for null k
        for kk in NULLS:
            k = gtg.vec([F(x) for x in kk])
            ok = ok and gtg.vdot(k, k) == 0
            ok = ok and gtg.vdot(k, tmap(k)) + eta * gtg.vdot(k, gtg.ricci(Re, k)) == 0
    # control: eta = 1/2 with the Einstein-with-G density 1/4 leaves a nonzero defect
    k = gtg.vec([F(1), F(1), F(0), F(0)])
    ok = ok and gtg.vdot(k, _dust_t(F(1, 4))(k)) + F(1, 4) * gtg.vdot(k, gtg.ricci(Re, k)) != 0
    GA.check("eta = 1/4(1 + c Q): 1/4 on Einstein-with-G pairs, 1/2 on an Einstein static universe where Clausius holds", ok)
    return ok
