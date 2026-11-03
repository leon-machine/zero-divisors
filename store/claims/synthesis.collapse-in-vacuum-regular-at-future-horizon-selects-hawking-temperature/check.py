"""The late-time state of a collapsing hole's outgoing modes is the scaling limit at the horizon crossing:
exact checks.

Carrier: the series' continuum mode space on one light ray (complex chiral CAR field of weight 1/2),
null vacuum two-point kernel K0(l1, l2) = 1/(l1 - l2) (times i/2pi, with the +i0 of the store's convention).
A map f of the ray's parameter pulls the kernel back as (f'(l1) f'(l2))^{1/2} / (f(l1) - f(l2)).
Schwarzian {f, x} = f'''/f' - (3/2)(f''/f')^2 = L' - L^2/2 with L = (log f')'.
(1) GTG, Painleve-Gullstrand field hb = 1 - beta P on flat spacetime, beta^2 = 2M/r (the stored rotation-gauge
    field Omega(e_t) = -beta beta' sigma_r, Omega(e_r) = -beta' sigma_r): radial null directions in background
    labels are e_t + w e_r with w = 1 - beta (outgoing) and w = -(1 + beta) (ingoing); along the ingoing radial
    null worldline with background tangent a = e_t/(1 + beta) - e_r the physical tangent k = (gamma0 - gamma1)/(1+beta)
    is parallel, a.grad k + Omega(a) x k = 0, so r is an affine parameter there (exact in Q(beta) at samples).
(2) The background time translation (Killing flow) moves the outgoing worldlines' label u; on a fixed ingoing
    worldline the crossing radius obeys dr/du = -(r - 2M)/(2r); the function U = -rho e^{rho/2M}, rho = r - 2M,
    obeys dU/du = -kappa U with kappa = 1/4M exactly (the exponential factor cancels), so the Killing translation by s
    is the dilation U -> e^{-kappa s} U about the horizon crossing, and dU/dr = -1 at r = 2M (U is an analytic affine
    coordinate there).
(3) Kernel identities: the weight-1/2 null vacuum kernel is exactly invariant under dilations and Moebius maps, and
    for U = -e^{-kappa u}/kappa it equals the thermal kernel kappa/(2 sinh(kappa(u1 - u2)/2)), written in
    x = e^{kappa u/2}; continuation by -i beta, beta = 2 pi/kappa, sends x to -x and the kernel to minus itself
    (antiperiodic, the fermionic KMS boundary value) with no pole at -i beta/2.
(4) Short-distance condition: for the analytic map f(l) = l e^l (both the ray's Kruskal coordinate in (2) and the
    Vaidya ray-tracing map in (5), after an affine change) the pulled-back kernel is K0 + R with R vanishing at the
    origin along every line l = (p e, q e); the dilated remainder mu R(mu l1, mu l2) is O(mu^2): exact series.
(5) Vaidya null shell (flat inside, Schwarzschild field outside, shell at v = v0): u(s) = v0 - 2s - 2m ln(s/m - 1),
    v = v0 - 2s, m = 2M, s the radius at which the ray leaves the shell. Exactly {v, u} = -m(4s - 3m)/(8 s^4) at
    sample radii, and at the horizon ray s = m it is -1/(8 m^2) = -kappa^2/2; {U, u} = -kappa^2/2 for Kruskal U;
    {U, v} is finite at the horizon ray (-3/(4 m^2)), so the in-vacuum is regular across the future horizon.
(6) Dichotomy: with flux T_uu = -(1/24pi) S, a late-time temperature theta T_H needs the U-frame Schwarzian
    t(U) = (1 - theta^2) kappa^2 / (2 (kappa U)^2) relative to the U-vacuum, bounded at U = 0 only for theta = 1;
    the Boulware state (u-vacuum) has {u, U} = 1/(2 U^2).
Controls: a mistuned surface gravity, a shifted shell exponent, a mutated remainder, theta != 1.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SUM_DRDU = F(359, 70)
SUM_THERMAL = F(508390, 47481)
SUM_MOB = F(1138237745, 310050468)
SUM_REM = F(24303316863918829379, 5598720000000000000000)
S13 = GA.sig(1, 3)
G0, G1 = GA.gen(0), GA.gen(1)
SIG_R = GA.mul(G1, G0, S13)          # sigma_r = gamma1 gamma0


def _comm(A, B):
    return GA.scal(F(1, 2), GA.sub(GA.mul(A, B, S13), GA.mul(B, A, S13)))


def _schw(d1, d2, d3):
    """Schwarzian from the first three derivatives."""
    return d3 / d1 - F(3, 2) * (d2 / d1) ** 2


def _derivs_of_rational(num, den, s0, n=2):
    """Taylor coefficients of num(s)/den(s) at s0 (num, den coefficient lists in s): returns
    [g(s0), g'(s0), g''(s0)]."""
    def shift(p):
        # p(s0 + e) as series in e
        out = [F(0)] * len(p)
        for k, c in enumerate(p):
            # (s0 + e)^k
            binom = [F(1)]
            for _ in range(k):
                binom = [a + b for a, b in zip(binom + [F(0)], [F(0)] + binom)]
            for j, b in enumerate(binom):
                out[j] += c * b * F(s0) ** (k - j)
        return out
    a = GA.ps_trunc(shift(num), n)
    b = GA.ps_trunc(shift(den), n)
    g = GA.ps_mul(a, GA.ps_inv(b, n), n)
    return [g[0], g[1], 2 * g[2]]


# ---------------------------------------------------------------- (1)
def check_ingoing_radius_is_affine_in_pg_gauge():
    premise("singularity.connection-bivector-computed")
    premise("synthesis.imported-gtg-dictionary")
    tab = []
    for M, beta in ((F(1), F(1, 2)), (F(3, 2), F(2, 3)), (F(1, 3), F(1)), (F(5), F(7, 5))):
        # physical image of e_t + w e_r is gamma0 + (beta + w) gamma1 (coframe theta^1 = beta dt + dr)
        for w, tag in ((1 - beta, "out"), (-(1 + beta), "in")):
            img = GA.add(G0, GA.scal(beta + w, G1))
            GA.check("radial %s direction is null (M=%s, beta=%s)" % (tag, M, beta),
                     GA.dot(img, img, S13) == 0)
        r = 2 * M / beta ** 2
        bp = -beta / (2 * r)                         # beta' = d beta / dr
        tab.append((r, bp))
        k_coef = 1 / (1 + beta)
        k = GA.scal(k_coef, GA.sub(G0, G1))
        # a = e_t/(1+beta) - e_r: dr/dlambda = -1, so a.grad f(r) = -f'(r); d/dr (1+beta)^-1 = -beta'/(1+beta)^2
        a_grad_k = GA.scal(bp / (1 + beta) ** 2, GA.sub(G0, G1))
        Om_t = GA.scal(-beta * bp, SIG_R)
        Om_r = GA.scal(-bp, SIG_R)
        Om_a = GA.sub(GA.scal(k_coef, Om_t), Om_r)
        img_a = GA.add(GA.scal(k_coef, G0), GA.scal(k_coef * beta - 1, G1))
        GA.check("tangent image is the stated k", GA.eq(img_a, k))
        GA.check("ingoing tangent is parallel: r affine (M=%s, beta=%s)" % (M, beta),
                 GA.is_zero(GA.add(a_grad_k, _comm(Om_a, k))))
        # control: with the rotation gauge field reversed the tangent is not parallel
        bad = GA.add(a_grad_k, _comm(GA.scal(-1, Om_a), k))
        GA.check("control: flipped rotation gauge field breaks parallelism", not GA.is_zero(bad))
    GA.check("tabulated (r, beta') at the samples", tab == [
        (F(8), F(-1, 32)), (F(27, 4), F(-4, 81)), (F(2, 3), F(-3, 4)), (F(250, 49), F(-343, 2500))])
    return True


# ---------------------------------------------------------------- (2)
def check_killing_translation_dilates_the_crossing():
    premise("singularity.connection-bivector-computed")
    premise("angle.imported-theorems-deliver-their-hypotheses")
    tab = []
    for M in (F(1), F(1, 4), F(7, 3)):
        kappa = 1 / (4 * M)
        for r in (3 * M, F(5, 2) * M, F(21, 10) * M, M, F(1, 2) * M):
            beta2 = 2 * M / r
            # along the ingoing worldline dt/dr = -1/(1+beta); u = t - r*_PG, dr*/dr = 1/(1-beta)
            # du/dr = -1/(1+beta) - 1/(1-beta) = -2/(1 - beta^2)
            du_dr = -2 / (1 - beta2)
            dr_du = 1 / du_dr
            tab.append(dr_du)
            rho = r - 2 * M
            GA.check("dr/du = -(r - 2M)/(2r) at r=%s" % r, dr_du == -rho / (2 * r))
            # U = -rho e^{rho/2M}: dU/du = -(1 + rho/2M) e^{rho/2M} dr/du; in units of e^{rho/2M}:
            dU_du_over_exp = -(1 + rho / (2 * M)) * dr_du
            U_over_exp = -rho
            GA.check("dU/du = -kappa U exactly (r=%s, M=%s)" % (r, M),
                     dU_du_over_exp == -kappa * U_over_exp)
            GA.check("control: kappa' = 1/(2M) fails", dU_du_over_exp != -U_over_exp / (2 * M))
        # dU/dr = -(1 + rho/2M) e^{rho/2M}: at rho = 0 it is -1 (nonzero): analytic affine coordinate
        GA.check("dU/dr = -1 at the horizon", -(1 + F(0) / (2 * M)) == -1)
    GA.check("tabulated dr/du (sum over samples)", sum(tab) == SUM_DRDU)
    return True


# ---------------------------------------------------------------- (3)
def check_vacuum_kernel_pulls_back_to_the_thermal_kernel():
    premise("hawking.i-state-continuum")
    premise("hawking.imported-ideal-fermi-gas-uniqueness")
    premise("angle.imported-theorems-deliver-their-hypotheses")
    tab, mob = [], []
    pts = [(F(1, 3), F(-2, 5)), (F(3), F(1, 7)), (F(-4, 9), F(5, 2))]
    # Moebius maps (a l + b)/(c l + d), ad - bc = 1: f' = 1/(c l + d)^2, sqrt = 1/(c l + d) for c l + d > 0
    for (a, b, c, d) in ((F(2), F(0), F(0), F(1, 2)), (F(1), F(1), F(0), F(1)), (F(1), F(0), F(1, 10), F(1))):
        assert a * d - b * c == 1
        for l1, l2 in pts:
            s1, s2 = c * l1 + d, c * l2 + d
            assert s1 > 0 and s2 > 0
            f1, f2 = (a * l1 + b) / s1, (a * l2 + b) / s2
            GA.check("Moebius covariance of the weight-1/2 kernel",
                     (1 / (s1 * s2)) / (f1 - f2) == 1 / (l1 - l2))
            mob.append(f1 - f2)
    # thermal pull-back: U = -1/(kappa x^2), x = e^{kappa u/2}; U' = 1/x^2; sqrt(U1'U2') = 1/(x1 x2)
    for kappa in (F(1, 4), F(2), F(3, 7)):
        for x1, x2 in ((F(2), F(1, 3)), (F(5, 4), F(7, 2)), (F(9), F(8))):
            U1, U2 = -1 / (kappa * x1 ** 2), -1 / (kappa * x2 ** 2)
            pulled = (1 / (x1 * x2)) / (U1 - U2)
            rr = x1 / x2                                # e^{kappa (u1 - u2)/2}
            thermal = kappa / (rr - 1 / rr)             # kappa / (2 sinh(kappa (u1-u2)/2))
            GA.check("pull-back is the thermal kernel (kappa=%s)" % kappa, pulled == thermal)
            tab.append(thermal)
            # continuation u1 -> u1 - i beta, beta = 2pi/kappa: x1 -> -x1, rr -> -rr
            GA.check("antiperiodic under -i beta", kappa / (-rr + 1 / rr) == -thermal)
            # midpoint -i beta/2: x1 -> -i x1, denominator -i(rr + 1/rr) has no zero for real rr
            GA.check("no pole at -i beta/2", rr + 1 / rr != 0)
    GA.check("tabulated thermal kernel values (sum)", sum(tab) == SUM_THERMAL)
    GA.check("tabulated Moebius image differences (sum)", sum(mob) == SUM_MOB)
    return True


# ---------------------------------------------------------------- (4)
def _exp_series(N):
    out, fact = [], F(1)
    for n in range(N + 1):
        out.append(1 / fact)
        fact *= n + 1
    return out


def _kernel_remainder_series(p, q, N, shift_exp=0):
    """eps * R(p eps, q eps) as a series in eps for f(l) = l e^{(1+shift) l}; R = pulled kernel - 1/(l1-l2)."""
    c = 1 + shift_exp
    E = _exp_series(N + 2)
    # f(l) = l e^{c l} = sum c^n l^{n+1}/n!; f'(l) = e^{c l}(1 + c l)
    def f_coeffs(t):              # series in eps of f(t eps)/eps
        return [E[n] * c ** n * t ** (n + 1) for n in range(N + 1)]
    def fp_coeffs(t):             # series in eps of f'(t eps)
        e = [E[n] * (c * t) ** n for n in range(N + 1)]
        return GA.ps_mul(e, [F(1), c * t], N)
    num = GA.ps_pow_rat(GA.ps_mul(fp_coeffs(p), fp_coeffs(q), N), F(1, 2), N)
    diff = [a - b for a, b in zip(f_coeffs(p), f_coeffs(q))]       # (f(p e) - f(q e))/e
    kern_eps = GA.ps_mul(num, GA.ps_inv(diff, N), N)                # eps * pulled kernel
    rem = list(kern_eps)
    rem[0] -= 1 / (p - q)
    return rem


def check_short_distance_condition_and_scaling_limit():
    premise("hawking.i-state-continuum")
    premise("angle.imported-theorems-deliver-their-hypotheses")
    N = 6
    tab = []
    for p, q in ((F(1), F(-1)), (F(2, 3), F(1, 5)), (F(-3), F(1, 2))):
        rem = _kernel_remainder_series(p, q, N)
        GA.check("leading term is the null vacuum (p=%s, q=%s)" % (p, q), rem[0] == 0)
        GA.check("remainder vanishes at the origin: eps R = O(eps^2)", rem[1] == 0)
        # the eps^2 coefficient is (1/12){f,l}(0) (p - q) with {f,l}(0) = -3 for l e^l
        GA.check("second coefficient is {f,l}(0)(p-q)/12 with {f,l}(0) = -3",
                 rem[2] == F(-3, 12) * (p - q))
        # dilation mu: mu R(mu l1, mu l2) at l = (p, q) is sum_n rem[n] mu^{n} ... starts at mu^2
        for mu in (F(1, 10), F(1, 100)):
            val = sum(rem[n] * mu ** n for n in range(N + 1))           # eps R at eps = mu, i.e. mu R(mu p, mu q)
            GA.check("dilated remainder is O(mu^2) (mu=%s)" % mu, abs(val) < 2 * abs(rem[2]) * mu ** 2)
            tab.append(val)
        bad = _kernel_remainder_series(p, q, N, shift_exp=1)
        GA.check("control: l e^{2l} has another second coefficient", bad[2] != rem[2])
    # {f,l}(0) for f = l e^l from L = (log f')' = 1 + 1/(1 + l): L(0) = 2, L'(0) = -1, S = -1 - 2 = -3
    GA.check("Schwarzian of l e^l at 0 is -3", F(-1) - F(2) ** 2 / 2 == -3)
    GA.check("tabulated dilated remainders (sum)", sum(tab) == SUM_REM)
    return True


# ---------------------------------------------------------------- (5)
def check_vaidya_shell_flux_tends_to_hawking_value():
    premise("synthesis.imported-gtg-dictionary")
    premise("hawking.i-state-continuum")
    for m in (F(2), F(1, 2), F(7, 3)):              # m = 2M
        kappa = 1 / (2 * m)                          # 1/(4M)
        for s in (F(3) * m, F(5, 4) * m, F(101, 100) * m, F(17, 3) * m):
            # u'(s) = -2s/(s - m)
            g = _derivs_of_rational([F(0), F(-2)], [-m, F(1)], s)   # g = u', g' = u'', g'' = u'''
            S_us = _schw(g[0], g[1], g[2])
            S_vu = -S_us / g[0] ** 2                    # {v,u} = -{u,s}/u'^2  (v = v0 - 2s)
            GA.check("{v,u} = -m(4s-3m)/(8 s^4) (m=%s, s=%s)" % (m, s),
                     S_vu == -m * (4 * s - 3 * m) / (8 * s ** 4))
        closed_at_h = -m * (4 * m - 3 * m) / (8 * m ** 4)
        GA.check("at the horizon ray {v,u} = -kappa^2/2 (m=%s)" % m, closed_at_h == -kappa ** 2 / 2)
        GA.check("control: not -kappa^2", closed_at_h != -kappa ** 2)
        # flux T_uu = -(1/24 pi){v,u} -> kappa^2/(48 pi) = (pi/12) T_H^2 with T_H = kappa/2pi: in units of
        # kappa^2/pi the two sides are 1/48 and (1/12)(1/4)
        GA.check("Hawking value is the chiral fermion flux at T_H", F(1, 2) / 24 == F(1, 12) * F(1, 4))
        # Kruskal U = -e^{-kappa u}/kappa: L = (log U')' = -kappa, L' = 0: {U,u} = -kappa^2/2
        GA.check("{U,u} = -kappa^2/2", F(0) - (-kappa) ** 2 / 2 == -kappa ** 2 / 2)
        # {U, v} at the horizon ray: U ~ e^y (y - 1) with y = s/m; L_y = 1 + 1/y, {U,y} = -1/y^2 - (1+1/y)^2/2 ...
        y = F(1)
        Ly, dLy = 1 + 1 / y, -1 / y ** 2
        S_Uy = dLy - Ly ** 2 / 2
        # check against derivatives (y+2)/y - (3/2)((y+1)/y)^2
        GA.check("{U,y} closed form", S_Uy == (y + 2) / y - F(3, 2) * ((y + 1) / y) ** 2)
        S_Uv = S_Uy * (1 / (2 * m)) ** 2              # y = (v0 - v)/(2m): dy/dv = -1/(2m)
        GA.check("{U,v} finite at the horizon ray: -3/(4 m^2)", S_Uv == F(-3, 4) / m ** 2)
        # approach: {v,u} + kappa^2/2 vanishes at s = m to first order (s - m ~ e^{-kappa u})
        for e in (F(1, 10), F(1, 1000)):
            s = m * (1 + e)
            dev = -m * (4 * s - 3 * m) / (8 * s ** 4) + kappa ** 2 / 2
            GA.check("deviation is O(s - m)", abs(dev) < 4 * e * kappa ** 2)
    return True


# ---------------------------------------------------------------- (6)
def check_regularity_across_future_horizon_selects_t_h():
    premise("hawking.i-state-continuum")
    premise("hawking.imported-ideal-fermi-gas-uniqueness")
    for kappa in (F(1, 4), F(3, 2)):
        for theta in (F(0), F(1, 2), F(1), F(3)):
            # late-time u-Schwarzian of a theta T_H state: S_u = -theta^2 kappa^2/2; S_u = t(U) U_u^2 - kappa^2/2
            # with U_u = -kappa U: t(U) = (1 - theta^2) kappa^2 / (2 kappa^2 U^2)
            for U in (F(-1, 10), F(-1, 1000), F(-1, 10 ** 6)):
                Uu = -kappa * U
                t = (1 - theta ** 2) * kappa ** 2 / (2 * (kappa * U) ** 2)
                GA.check("chain rule closes", t * Uu ** 2 - kappa ** 2 / 2 == -theta ** 2 * kappa ** 2 / 2)
            t_far = (1 - theta ** 2) * kappa ** 2 / (2 * (kappa * F(-1, 10 ** 6)) ** 2)
            GA.check("bounded at U -> 0 iff theta = 1 (theta=%s)" % theta,
                     (abs(t_far) < 1) == (theta == 1))
        # Boulware: u = -(1/kappa) ln(-kappa U): u' = -1/(kappa U), L = (log|u'|)' = -1/U, L' = 1/U^2
        for U in (F(-1, 3), F(-2, 7)):
            L, dL = -1 / U, 1 / U ** 2
            GA.check("{u,U} = 1/(2U^2) (Boulware singular on the future horizon)", dL - L ** 2 / 2 == 1 / (2 * U ** 2))
    return True
