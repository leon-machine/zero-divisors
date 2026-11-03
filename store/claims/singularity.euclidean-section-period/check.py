"""singularity.euclidean-section-period: exact checks in Gauge Theory Gravity, Wick-rotated.

The Wick-rotated static gauge lives on the flat Euclidean background Cl(4,0) (labels tau, r, theta, phi at
indices 0..3). Rational sample points use w = F = sqrt(f) as the parameter: f = w^2, r = 2M/(1 - w^2).
(1) Derived metric: with hb^{-1}(e_tau) = w e_tau, hb^{-1}(e_r) = e_r/w, hb^{-1}(e_theta) = r e_theta,
    hb^{-1}(e_phi) = r s e_phi (s = sin theta rational), the Gram of the physical frame computed in GA is
    diag(f, 1/f, r^2, r^2 s^2); in the labels (rho, tau) with d rho = dr/sqrt(f) the physical vector over e_rho
    is the unit e_r, so the (rho, tau) block is diag(1, F^2).
(2) dF/d rho = f'(r)/2 = M/r^2 as an identity of rational functions in w (F = w, d rho = dr/F), F = 0 at the
    horizon and dF/d rho = 1/(4M) = kappa there, for four masses; f(2M) = 0 and f'(2M)/2 = 1/(4M).
(3) Near the tip, by exact power series (masses with 2M a rational square, so sqrt(2M) is rational):
    rho(w) = 2 int_0^w sqrt(2M + t^2) dt and F(w) = w/sqrt(2M + w^2), u = r - 2M = w^2; reverting rho(w) gives
    F(rho) = kappa rho + c3 rho^3 + O(rho^5) with the even coefficients zero, so F^2 = kappa^2 rho^2 + O(rho^4).
(4) The rotation-gauge field of the (rho, tau) block, solved from the torsion-free condition
    D_rho hb^{-1}(e_tau) - D_tau hb^{-1}(e_rho) = 0 (D_a M = a.nabla M + Omega(a) x M, unknown
    Omega(e_rho) = a B, Omega(e_tau) = c B, B = e_r e_tau), is a = 0, c = -F'(rho) at sample values; at the
    tip c = -kappa. The flat polar field (F = rho, angle phi) has c = -1. With tau of period p and the
    angle phi = 2 pi tau/p, the field in the angle label is -(kappa p/(2 pi)) B: it is the flat polar field,
    so the tip is a smooth point, iff kappa p = 2 pi, i.e. p = 8 pi M (p/pi = 8M exactly); for any other
    period the tip is a cone of total angle kappa p (checked: p/pi = 8M +- 1, 4M, 16M give angle ratios
    kappa p/(2 pi) != 1).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SE = GA.sig(4, 0)
MASSES = [F(1), F(1, 2), F(2), F(9, 2)]
SQRT2M = {F(1, 2): F(1), F(2): F(2), F(9, 2): F(3)}
NS = 9


def check_wick_rotated_derived_metric():
    premise("singularity.computed")
    ok = True
    for M in MASSES:
        for w, s in [(F(1, 2), F(3, 5)), (F(2, 3), F(5, 13)), (F(1, 5), F(1))]:
            f = w * w
            r = 2 * M / (1 - f)
            ok = ok and f == 1 - 2 * M / r
            frame = [GA.scal(w, GA.gen(0)), GA.scal(1 / w, GA.gen(1)), GA.scal(r, GA.gen(2)),
                     GA.scal(r * s, GA.gen(3))]
            G = [[GA.dot(a, b, SE) for b in frame] for a in frame]
            want = [[f, 0, 0, 0], [0, 1 / f, 0, 0], [0, 0, r * r, 0], [0, 0, 0, r * r * s * s]]
            ok = ok and G == [[F(x) for x in row] for row in want]
            # (rho, tau) labels: e_rho = (dr/drho) e_r with dr/drho = sqrt(f) = w
            g_rho = GA.scal(w, frame[1])
            ok = ok and GA.eq(g_rho, GA.gen(1)) and GA.dot(g_rho, g_rho, SE) == 1
            ok = ok and GA.dot(frame[0], frame[0], SE) == w * w and GA.dot(g_rho, frame[0], SE) == 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_wick_rotated_derived_metric"; return _tp_rv


def check_slope_is_half_f_prime():
    premise("singularity.computed")
    ok = True
    one = GA.RF.const(1)
    w = GA.RF.var()
    for M in MASSES:
        r_w = GA.RF.const(2 * M) / (one - w * w)
        dF_drho = w / r_w.deriv()                       # dF/drho = F / (dr/dF)
        half_fp = GA.RF.const(M) / (r_w * r_w)
        ok = ok and dF_drho.eqrf(half_fp) and dF_drho.eval(F(0)) == 1 / (4 * M)
        r = GA.RF.var()
        f = one - GA.RF.const(2 * M) / r
        ok = ok and f.eval(2 * M) == 0 and f.deriv().eval(2 * M) / 2 == 1 / (4 * M)
    _tp_rv = (ok); assert _tp_rv is not False, "check_slope_is_half_f_prime"; return _tp_rv


def revert(a, N):
    """Series inverse g of a (a[0] = 0, a[1] != 0): a(g(x)) = x, to order N."""
    g = [F(0), 1 / a[1]] + [F(0)] * (N - 1)
    for k in range(2, N + 1):
        comp = GA.ps_compose(a, g, N)
        g[k] = -comp[k] / a[1]
    return g


def check_tip_expansion():
    premise("singularity.computed")
    ok = True
    for M, a in SQRT2M.items():
        kappa = 1 / (4 * M)
        # sqrt(2M + t^2) = a (1 + t^2/a^2)^(1/2)
        base = [F(1), F(0), 1 / (a * a)] + [F(0)] * (NS - 2)
        root = [a * c for c in GA.ps_pow_rat(base, F(1, 2), NS)]
        rho_w = [2 * c for c in GA.ps_int(root)][:NS + 1]
        Fw = [F(0)] + [c / a for c in GA.ps_pow_rat(base, F(-1, 2), NS - 1)]
        w_rho = revert(rho_w, NS)
        F_rho = GA.ps_compose(Fw, w_rho, NS)
        ok = ok and F_rho[0] == 0 and F_rho[1] == kappa and F_rho[2] == 0 and F_rho[4] == 0
        ok = ok and F_rho[3] != 0 and F_rho[6] == 0
        F2 = GA.ps_mul(F_rho, F_rho, NS)
        ok = ok and F2[2] == kappa * kappa and F2[3] == 0 and F2[1] == 0
        # consistency: rho(w(rho)) = rho
        back = GA.ps_compose(rho_w, w_rho, NS)
        ok = ok and back[1] == 1 and all(back[k] == 0 for k in range(2, NS + 1))
    _tp_rv = (ok); assert _tp_rv is not False, "check_tip_expansion"; return _tp_rv


def omega_coefficients(Fv, Fp):
    """Solve the torsion equation for Omega(e_rho) = a B, Omega(e_tau) = c B in the (rho, tau) block."""
    S2 = GA.sig(2, 0)
    er, et = GA.gen(0), GA.gen(1)
    B = GA.mul(er, et, S2)

    def cx(A, X):
        return GA.scal(F(1, 2), GA.sub(GA.mul(A, X, S2), GA.mul(X, A, S2)))
    # D_rho (F e_tau) - D_tau (e_rho) = F' e_tau + a F (B x e_tau) - c (B x e_rho) = 0: linear in (a, c)
    col_a = cx(GA.scal(Fv, B), et)
    col_c = GA.neg(cx(B, er))
    rhs = GA.neg(GA.scal(Fp, et))
    rows = [[col_a.get(k, F(0)), col_c.get(k, F(0))] for k in ((0,), (1,))]
    return GA.field_solve(rows, [rhs.get(k, F(0)) for k in ((0,), (1,))])


# Sample (F, F'(rho)) values for the torsion-free solve.
FV_FP = [(F(1, 3), F(2, 7)), (F(5, 2), F(-1, 4)), (F(1, 10), F(3))]
# A small F at which the near-tip fields are solved (the solution depends only on F').
NEAR_TIP_F = F(1, 1000)


def period_samples(M):
    """Sample periods p = q pi: the claimed q = 8M and the controls 8M +- 1, 4M, 16M."""
    return (8 * M, 8 * M + 1, 8 * M - 1, 4 * M, 16 * M)


def check_regular_tip_iff_period_eight_pi_m():
    premise("singularity.computed")
    ok = True
    for Fv, Fp in FV_FP:
        a, c = omega_coefficients(Fv, Fp)
        ok = ok and a == 0 and c == -Fp
    a0, c0 = omega_coefficients(NEAR_TIP_F, F(1))      # flat polar field: F = rho, F' = 1
    ok = ok and a0 == 0 and c0 == -1
    for M in MASSES:
        kappa = 1 / (4 * M)
        a1, c1 = omega_coefficients(NEAR_TIP_F, kappa)   # near the tip F' -> kappa
        ok = ok and c1 == -kappa
        regular = []
        for q in period_samples(M):                       # p = q pi
            angle_field = c1 * q / 2                     # Omega in the angle label: (p/(2 pi)) c
            ratio = kappa * q / 2                        # cone angle kappa p over 2 pi
            ok = ok and angle_field == -ratio and ((angle_field == c0) == (ratio == 1))
            if ratio == 1:
                regular.append(q)
        ok = ok and regular == [8 * M]                   # the smooth tip is exactly p = 8 pi M
    _tp_rv = (ok); assert _tp_rv is not False, "check_regular_tip_iff_period_eight_pi_m"; return _tp_rv
