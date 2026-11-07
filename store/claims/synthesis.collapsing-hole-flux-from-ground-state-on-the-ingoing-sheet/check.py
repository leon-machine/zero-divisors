"""The collapse hole's thermal condition on the ingoing sheet: exact checks.

(1) Reparametrisation: for a polynomial xi with rational coefficients and a base point U0, the squared
    ratio of the weight-1/2 ground-state kernels in xi and in U, xi'(U0+x) xi'(U0) x^2/(xi(U0+x)-xi(U0))^2,
    is an exact rational function of x whose Taylor coefficients at 0 are 1, 0, S_xi(U0)/6 (Schwarzian);
    tabulated at three xi and three U0. The same coefficient S/6 is the diagonal value of the difference of
    the weight-1 field's own kernels (U - U')^{-2}: continuous for that weight too. Covariance-weight
    controls: the kernel 1/(U - U') carried with weight 0 or 1 gives a constant term != 1 or a linear term
    != 0; xi = U^3 at U0 = 0 gives ratio 0.
(2) Scaling: with eps a formal variable, eps/(eps U - eps U') = 1/(U - U') exactly (weight 1/2), while
    weights 0 and 1 are not invariant; eps R(eps U, eps U') for a polynomial R has no eps^0 term; a
    remainder homogeneous of degree -1 is unchanged.
(3) The Kruskal functions in the Painleve-Gullstrand gauge: kappa * 4M = 1 so that kappa int dr/(1 -+ beta)
    = s^2/2 +- s + ln|s -+ 1| (partial fractions, exact in RF); the prefactors and exponents of U V multiply
    to -(s^2 - 1) e^{s^2}; d/ds[(s-1)e^{s^2/2+s}] = s^2 e^{s^2/2+s}; U changes sign at s = 1; the exponent
    of t in U is -kappa and in V is +kappa (the dilation rates).
(4) The ingoing generator: in the chart (v, r) with g = f dv^2 - 2 dv dr, g(d_r, d_r) = 0, Gamma^r_rr = 0
    (r affine), Gamma^v_vv = f'/2 = kappa on the horizon (tabulated at two masses); dU/d rho along
    v = const has prefactor rho e^rho, equal to 1 at the horizon.
(5) The exterior half: the Mellin symbol m(w) = (1 + e^{-2 pi w})^{-1} written with q = e^{pi w} rational
    satisfies 1 - m = e^{beta h} m with h = -kappa w exactly when beta kappa = 2 pi, at kappa = 1/(4M),
    beta = 8 pi M, and at no other tested multiple; m(w) + m(-w) = 1.
Exact arithmetic only (Fractions, rational functions); pi and e are never evaluated.
"""
from fractions import Fraction as F
import GA
from GA import RF
from tp_premise import premise


def _shift(p, U0):
    """p(U0 + x) as a polynomial in x (coefficient lists over Fraction)."""
    out = []
    for i, c in enumerate(p):
        term = [F(1)]
        for _ in range(i):
            term = GA.pmul(term, [F(U0), F(1)])
        out = GA.padd(out, [c * t for t in term])
    return out


def _ratio_sq(xi, U0, twice_weight):
    """(xi'(U0+x) xi'(U0))^{2w} x^2 / (xi(U0+x) - xi(U0))^2 as an RF in x; 2w = twice_weight."""
    xs = _shift(xi, U0)
    d = GA.pderiv(xi)
    ds = _shift(d, U0)
    d0 = GA.peval(d, U0)
    diff = GA.padd(xs, GA.pneg([GA.peval(xi, U0)]))
    q, r = GA.pdivmod(diff, [F(0), F(1)])
    GA.check("xi(U0 + x) - xi(U0) is divisible by x", not r)
    num = [F(1)]
    for _ in range(twice_weight):
        num = GA.pmul(num, GA.pmul(ds, [d0]))
    return RF(num, GA.pmul(q, q))


def _taylor(rf, n):
    num = GA.ps_trunc(rf.num, n)
    den = GA.ps_trunc(rf.den, n)
    return GA.ps_mul(num, GA.ps_inv(den, n), n)


def check_regular_reparametrisation_keeps_the_ground_state_singularity():
    premise("synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation")
    premise("synthesis.positive-null-energy-gives-r-premises")
    xis = ([F(0), F(1), F(1, 3)],
           [F(2), F(3), F(-1, 2), F(1, 5)],
           [F(0), F(1), F(0), F(1, 7)])
    base = (F(0), F(1, 2), F(-3, 4))
    # tabulated S_xi(U0)/6 for the nine cases, row by xi
    want = ((F(-1, 9), F(-1, 16), F(-4, 9)),
            (F(7, 180), F(196, 2809), F(-544, 106929)),
            (F(1, 7), F(88, 961), F(928, 19321)))
    for i, xi in enumerate(xis):
        d1, d2, d3 = GA.pderiv(xi), GA.pderiv(GA.pderiv(xi)), GA.pderiv(GA.pderiv(GA.pderiv(xi)))
        for j, U0 in enumerate(base):
            a, b2, c6 = GA.peval(d1, U0), GA.peval(d2, U0), GA.peval(d3, U0)
            GA.check("xi' > 0 at the base point", a > 0)
            S6 = (c6 / a - F(3, 2) * (b2 / a) ** 2) / 6
            co = _taylor(_ratio_sq(xi, U0, 1), 3)
            GA.check("weight 1/2: squared ratio = 1 + 0 x + (S/6) x^2", co[0] == 1 and co[1] == 0 and co[2] == S6)
            GA.check("tabulated S/6", S6 == want[i][j])
            # the weight-1 field's own kernels (U - U')^{-2}: their difference is (squared ratio - 1)/x^2,
            # whose value on the diagonal is the x^2 coefficient S/6: continuous, nonzero
            GA.check("weight-1 own-kernel difference on the diagonal is S/6", co[2] == want[i][j] and (co[2] != 0))
            c0 = _taylor(_ratio_sq(xi, U0, 0), 1)
            c1 = _taylor(_ratio_sq(xi, U0, 2), 1)
            GA.check("covariance-weight control 0 on the kernel 1/(U - U'): constant term 1/xi'^2", c0[0] == 1 / (a * a))
            GA.check("covariance-weight control 1 on the kernel 1/(U - U'): constant xi'^2, linear xi' xi''", c1[0] == a * a and c1[1] == a * b2)
            if not (a == 1 and b2 == 0):
                GA.check("the kernel 1/(U - U') is not covariant with weight 0 or 1 off xi' = 1, xi'' = 0",
                         not (c0[0] == 1 and c0[1] == 0) or not (c1[0] == 1 and c1[1] == 0))
    # the Schwarzian of a Moebius-type polynomial truncation is not zero: a generic nonzero value
    GA.check("S/6 of xi = U + U^2/3 at 0 is -1/9", want[0][0] == F(-1, 9))
    # singular reparametrisation: xi'(0) = 0 kills the ratio
    GA.check("xi = U^3 at U0 = 0: ratio vanishes", _ratio_sq([F(0), F(0), F(0), F(1)], F(0), 1).eval(F(0)) == 0)


def check_scaling_limit_is_the_ground_state():
    premise("synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation")
    premise("synthesis.positive-null-energy-gives-r-premises")
    premise("hawking.imported-quasi-free-kms-reduces-two")
    e = RF.var()
    # polynomial remainder R = 3 - 2U + (5/2)U' + 7UU' - (1/3)U^2; tabulated: 1/(U - U'), the eps^2
    # coefficient of eps R(eps U, eps U') (= -2U + (5/2)U'), and the degree -1 kernel 1/(U + 2U')
    R = {(0, 0): F(3), (1, 0): F(-2), (0, 1): F(5, 2), (1, 1): F(7), (2, 0): F(-1, 3)}
    pts = ((F(2, 3), F(-5, 7), F(21, 29), F(-131, 42), F(-21, 16)),
           (F(-1), F(3, 2), F(-2, 5), F(23, 4), F(1, 2)),
           (F(1, 4), F(-1, 3), F(12, 7), F(-4, 3), F(-12, 5)))
    for U, Up, inv, c2, hom in pts:
        sing = RF.const(1) / (e * RF.const(U) - e * RF.const(Up))
        GA.check("tabulated 1/(U - U')", 1 / (U - Up) == inv)
        GA.check("weight 1/2: eps/(eps U - eps U') = 1/(U - U')", (e * sing).eqrf(RF.const(inv)))
        GA.check("control weight 0: not invariant", not sing.eqrf(RF.const(inv)))
        GA.check("control weight 1: not invariant", not (e * e * sing).eqrf(RF.const(inv)))
        scaled = RF.const(0)
        for (j, k), c in R.items():
            scaled = scaled + RF.const(c * U ** j * Up ** k) * RF([F(0)] * (j + k) + [F(1)])
        scaled = e * scaled
        co = _taylor(scaled, 2)
        GA.check("eps R(eps U, eps U') has no eps^0 term", co[0] == 0)
        GA.check("its eps^1 coefficient is R(0,0) = 3", co[1] == 3)
        GA.check("tabulated eps^2 coefficient -2U + (5/2)U'", co[2] == c2)
        GA.check("control: without the half-density factor the eps^0 term is R(0,0)",
                 (scaled / e).eval(F(0)) == 3)
        Rh = RF.const(1) / (e * RF.const(U) + RF.const(2) * e * RF.const(Up))
        GA.check("tabulated 1/(U + 2U')", 1 / (U + 2 * Up) == hom)
        GA.check("degree -1 remainder: eps R_h(eps U, eps U') = R_h(U, U')", (e * Rh).eqrf(RF.const(hom)))


def _dexp(P, E):
    """derivative prefactor of P(s) e^{E(s)}: P' + P E'."""
    return GA.padd(GA.pderiv(P), GA.pmul(P, GA.pderiv(E)))


def check_kruskal_functions_in_the_painleve_gullstrand_gauge():
    premise("sheaf.gauge-field-cometric")
    premise("synthesis.imported-gtg-dictionary")
    premise("singularity.euclidean-section-period")
    s = RF.var()
    one = RF.const(1)
    for M in (F(1), F(3, 2), F(7)):
        kap = 1 / (4 * M)
        GA.check("kappa * 4M = 1 (the exponent normalisation)", kap * 4 * M == 1)
        GA.check("tabulated kappa", kap == F(1, 4) / M)
    # kappa int dr/(1 - beta) = int s^2/(s-1) ds: partial fractions, exact
    GA.check("s^2/(s-1) = s + 1 + 1/(s-1)", ((s * s) / (s - one)).eqrf(s + one + one / (s - one)))
    GA.check("s^2/(s+1) = s - 1 + 1/(s+1)", ((s * s) / (s + one)).eqrf(s - one + one / (s + one)))
    GA.check("control: s^2/(s-1) != s + 1", not ((s * s) / (s - one)).eqrf(s + one))
    # the integrand itself: kappa * 4M s ds / ((s-1)/s) = s^2/(s-1) ds
    GA.check("kappa dr/(1 - beta) = s^2/(s - 1) ds", (RF.const(F(1, 4)) * RF.const(4) * s * s / (s - one)).eqrf((s * s) / (s - one)))
    # exponents and prefactors of U V
    EU, EV = [F(0), F(1), F(1, 2)], [F(0), F(-1), F(1, 2)]
    PU, PV = [F(-1), F(1)], [F(1), F(1)]
    GA.check("exponents add to s^2", GA.padd(EU, EV) == [F(0), F(0), F(1)])
    GA.check("prefactors multiply to s^2 - 1", GA.pmul(PU, PV) == [F(-1), F(0), F(1)])
    # d/ds of (s - 1) e^{s^2/2 + s}
    GA.check("d/ds[(s-1) e^{s^2/2+s}] = s^2 e^{s^2/2+s}", _dexp(PU, EU) == [F(0), F(0), F(1)])
    GA.check("d/ds[(s+1) e^{s^2/2-s}] = s^2 e^{s^2/2-s}", _dexp(PV, EV) == [F(0), F(0), F(1)])
    # sign change of U = -(s-1) e^{...} e^{-kappa t}: prefactor -(s-1)
    for sv, sign in ((F(2), -1), (F(3, 2), -1), (F(1), 0), (F(1, 2), 1), (F(1, 10), 1)):
        val = -GA.peval(PU, sv)
        GA.check("sign of U at s = %s" % sv, (val > 0) - (val < 0) == sign)
        GA.check("V's prefactor positive", GA.peval(PV, sv) > 0)
    # the t-dependence: U carries e^{-kappa t}, V carries e^{+kappa t}; d/dt of e^{a t} is a e^{a t}
    for M in (F(1), F(5, 2)):
        kap = 1 / (4 * M)
        GA.check("d_t U = -kappa U", _dexp([F(1)], [F(0), -kap]) == [-kap])
        GA.check("d_t V = +kappa V", _dexp([F(1)], [F(0), kap]) == [kap])
        GA.check("U V is t-independent", GA.padd([F(0), -kap], [F(0), kap]) == [])


def check_ingoing_generator_crosses_the_horizon_regularly():
    premise("synthesis.imported-gtg-dictionary")
    premise("singularity.euclidean-section-period")
    premise("synthesis.r-loc-needs-sheet-labelled-modes")
    r = RF.var()
    for M, want in ((F(1), F(1, 4)), (F(3, 2), F(1, 6))):
        f = RF.const(1) - RF.const(2 * M) / r
        g = [[f, RF.const(-1)], [RF.const(-1), RF.const(0)]]       # coordinates (v, r)
        gi = GA.rf_mat_inverse(g)
        GA.check("g^{vv} = 0, g^{vr} = -1", gi[0][0].is_zero() and gi[0][1].eqrf(RF.const(-1)))
        dg = [[f.deriv(), RF.const(0)], [RF.const(0), RF.const(0)]]  # d_r g; d_v g = 0

        def gamma(a, b, c):
            out = RF.const(0)
            for d in range(2):
                term = RF.const(0)
                if b == 1:
                    term = term + dg[d][c]
                if c == 1:
                    term = term + dg[d][b]
                if d == 1:
                    term = term - dg[b][c]
                out = out + gi[a][d] * term
            return out * RF.const(F(1, 2))
        GA.check("g(d_r, d_r) = 0: v = const is null", g[1][1].is_zero())
        GA.check("Gamma^r_rr = 0: r is affine along v = const", gamma(1, 1, 1).is_zero())
        GA.check("Gamma^v_vv = f'/2", gamma(0, 0, 0).eqrf(f.deriv() * RF.const(F(1, 2))))
        GA.check("Gamma^v_vv on the horizon is kappa = 1/(4M)", gamma(0, 0, 0).eval(2 * M) == 1 / (4 * M))
        GA.check("tabulated kappa", gamma(0, 0, 0).eval(2 * M) == want)
        GA.check("control: Gamma^v_vv off the horizon is not kappa", gamma(0, 0, 0).eval(3 * M) != want)
    # 2 kappa r* = rho + ln|rho - 1| with r* = r + 2M ln|r/2M - 1|: 2 kappa * 2M = 1 and 2 kappa * r = rho
    for M in (F(1), F(3, 2)):
        kap = 1 / (4 * M)
        GA.check("2 kappa 2M = 1", 2 * kap * 2 * M == 1)
    # U = -e^{-kappa v} (rho - 1) e^rho along v = const: dU/d rho prefactor rho e^rho
    P, E = [F(-1), F(1)], [F(0), F(1)]
    GA.check("d/d rho[(rho - 1) e^rho] = rho e^rho", _dexp(P, E) == [F(0), F(1)])
    GA.check("nonzero at the horizon rho = 1: value 1", GA.peval(_dexp(P, E), F(1)) == 1)
    GA.check("control: the prefactor vanishes only at rho = 0", GA.peval(_dexp(P, E), F(0)) == 0)


def check_exterior_half_is_the_i_state_at_the_hawking_temperature():
    premise("synthesis.positive-null-energy-gives-r-premises")
    premise("hawking.i-state-continuum")
    premise("hawking.imported-quasi-free-kms-reduces-two")
    premise("singularity.euclidean-section-period")
    # q = e^{pi w} rational; the future-half symbol m(w) = (1 + e^{-2 pi w})^{-1} = q^2/(q^2 + 1) and the
    # past-half symbol (1 + e^{2 pi w})^{-1} = 1/(q^2 + 1), tabulated; h = -+ kappa w; e^{beta h} at
    # beta kappa = 2 pi is q^{-+2}
    for q, m_want, mm_want in ((F(2), F(4, 5), F(1, 5)), (F(1, 3), F(1, 10), F(9, 10)), (F(7, 5), F(49, 74), F(25, 74))):
        m = q * q / (q * q + 1)
        mm = 1 / (1 + q * q)
        GA.check("tabulated future-half symbol", m == m_want)
        GA.check("tabulated past-half symbol", mm == mm_want)
        GA.check("0 < m < 1", 0 < m < 1)
        GA.check("future half: 1 - m = e^{beta h} m at beta kappa = 2 pi", 1 - m == m / (q * q))
        GA.check("fails at beta kappa = pi", 1 - m != m / q)
        GA.check("fails at beta kappa = 4 pi", 1 - m != m / (q ** 4))
        GA.check("past half: 1 - m = e^{beta h} m at beta kappa = 2 pi", 1 - mm == mm * q * q)
        GA.check("past half fails at beta kappa = pi", 1 - mm != mm * q)
        GA.check("m(w) + m(-w) = 1", m + mm == 1)
    for M, bpi in ((F(1), F(8)), (F(3, 2), F(12)), (F(7), F(56))):
        kap = 1 / (4 * M)
        GA.check("beta = 2 pi / kappa is 8 pi M: beta/pi tabulated", 2 / kap == bpi)
        GA.check("the temperature kappa/2 pi is 1/(8 pi M)", kap / 2 == 1 / bpi)
    # the exterior half U < 0 with flow -kappa U d_U: dU/dtau > 0 (towards the horizon), tabulated
    for kap, U, want in ((F(1, 4), F(-1), F(1, 4)), (F(1, 6), F(-3, 2), F(1, 4)), (F(1, 4), F(-6), F(3, 2))):
        GA.check("tabulated dU/dtau = -kappa U on U < 0", -kap * U == want and want > 0)
        GA.check("control: on U > 0 the flow moves away from the horizon", -kap * (-U) == -want)


# ---------------------------------------------------------------------------
# GTG proof of (ii) (2026-11-07): in the Painleve-Gullstrand gauge field on flat spacetime, the ingoing
# radial null worldline parametrised by r has physical velocity k = hb^{-1}(x') = (gamma_1 - gamma_0)/(1 + beta)
# and D_{x'} k = 0 (r affine); the horizon generator K = hb^{-1}(e_t) has (K . D) K = K/(4M) at r = 2M.
# The rotation-gauge field is the engine's torsion-free PG field (checked torsion-free here).
# ---------------------------------------------------------------------------
import gtg  # noqa: E402

PG_CASES = [(F(1), [F(2), F(8), F(1, 2)]), (F(3, 2), [F(3), F(12), F(3, 4)])]   # beta = sqrt(2M/r) rational
PG_ANGLE = (F(3, 5), F(4, 5))


def check_gtg_ingoing_generator_is_affine_and_horizon_rate():
    premise("synthesis.imported-gtg-dictionary")
    premise("singularity.euclidean-section-period")
    ok = True
    horizons = 0
    for M, radii in PG_CASES:
        for r0 in radii:
            fld = gtg.schwarzschild_pg(M, r0, PG_ANGLE[0], PG_ANGLE[1])
            ok = ok and fld.torsion_free()
            r = gtg.Jet.var(1, r0, 4, 2)
            beta = (2 * M / r).pw(F(1, 2))
            b0, db0 = beta.v, beta.d(1).v
            ok = ok and db0 == -b0 / (2 * r0)
            sig_r = gtg.biv(1, 0)                                   # sigma_r = e_r e_t
            ok = ok and gtg.m_sub(fld.Omega(0), gtg.m_scal(M / (r0 * r0), sig_r)) == {}
            ok = ok and gtg.m_sub(gtg.grade({bl: c for bl, c in fld.Omega(1).items() if bl == (0, 1)}, 2),
                                  gtg.m_scal(-db0, sig_r)) == {}
            k = {(0,): -1 / (1 + beta), (1,): 1 / (1 + beta)}
            ok = ok and gtg.vdot(gtg.m_val(k), gtg.m_val(k)) == 0
            xp = [-1 / (1 + b0), F(1), F(0), F(0)]                 # x' = e_r - e_t/(1 + beta)
            ok = ok and gtg.m_sub(fld.hb_inv(gtg.vec(xp)), gtg.m_val(k)) == {}
            Dk = gtg.m_add(*[gtg.m_scal(xp[mu], fld.cov(mu, k)) for mu in range(2)])
            ok = ok and Dk == {}                                    # r is affine
            # control: the same worldline parametrised by t is not affinely parametrised
            kt = {(0,): gtg.Jet.const(1, 4), (1,): -1 - beta}
            xt = [F(1), -1 - b0, F(0), F(0)]
            Dkt = gtg.m_add(*[gtg.m_scal(xt[mu], fld.cov(mu, kt)) for mu in range(2)])
            ok = ok and Dkt != {}
            K = {(0,): gtg.Jet.const(1, 4), (1,): beta}
            DK = fld.cov(0, K)
            if r0 == 2 * M:
                ok = ok and gtg.m_sub(DK, gtg.m_scal(1 / (4 * M), gtg.m_val(K))) == {}
                horizons += 1
            else:
                ok = ok and gtg.m_sub(DK, gtg.m_scal(M / (r0 * r0), gtg.vec([b0, 1, 0, 0]))) == {}
    ok = ok and horizons == 2
    GA.check("GTG: D_{x'} k = 0 along the ingoing generator; (K . D) K = K/(4M) on the horizon", ok)
    assert ok
