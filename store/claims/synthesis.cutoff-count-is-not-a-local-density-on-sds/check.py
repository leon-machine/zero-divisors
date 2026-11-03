"""synthesis.cutoff-count-is-not-a-local-density-on-sds: exact checks.

Schwarzschild-de Sitter, f(r) = 1 - 2M/r - Lambda r^2/3, Planck units, pi kept formal.
check_cutoff_volume_rates: the exceptional-set measure mu_E = lim V(tau)/tau = 12 pi M per unit Killing
time for every Lambda (exact power series of tau and V in rho = sqrt(r), with 2M a square), and the
(C1) slice r_c^3 = 2M has V'^2 = (8 pi M)^2 (1 - r_c/2M + Lambda/3) exactly.
check_count_over_hole_period: with nu' fixed by the Schwarzschild calibration, the count over the hole's
modular period 2 pi/kappa_b against A_b/4 is M/(3M - r_b) = u/(3u - 2) = 1/(1 - 2 Lambda/(3 w_h)),
w_h = 2M/r_b^3; equal to 1 at Lambda = 0, larger for Lambda > 0, unbounded towards Nariai.
check_no_horizon_period_gives_area_law: the area law needs the epoch 2 pi r_b^2/M; on rational SdS
families with both horizons rational, kappa_c < kappa_b < M/r_b^2, so both horizon periods overcount.
check_mean_entropy_forced_down: under the area-law hypothesis, <s>_SdS/<s>_0 = (3u - 2)/u < 1.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise


def setup_count():
    premise("synthesis.exceptional-boundary-measure-one-calibration")
    premise("interior.schwarzschild-de-sitter-weighted-limit")
    premise("singularity.stretched-singularity-count")


def setup_epoch():
    premise("scrambling.epoch-modular-period-two-unknowns-become")
    premise("synthesis.exceptional-boundary-measure-one-calibration")
    premise("synthesis.sds-clausius-fixes-area-constant")


def mu_E_over_pi(M, Lam, N=14):
    """lim V/tau in units of pi, from exact series in rho (r = rho^2); needs 2M a perfect square q^2."""
    q = next(F(a, b) for b in range(1, 50) for a in range(1, 400) if F(a, b) ** 2 == 2 * M)
    u = [F(0)] * (N + 1)
    u[0], u[2] = F(1), -F(1) / (2 * M)
    u[6] = Lam / (6 * M)           # A = (2M/r)(1 - r/2M + Lam r^3/(6M))
    inv_sqrt = GA.ps_pow_rat(u, F(-1, 2), N)
    sq = GA.ps_pow_rat(u, F(1, 2), N)
    integrand = [F(0)] * (N + 1)
    for i in range(N - 1):
        integrand[i + 2] += 2 * inv_sqrt[i] / q        # dtau/drho = 2 rho^2 u^{-1/2}/sqrt(2M)
    tau = GA.ps_int(integrand)
    V = [F(0)] * (N + 1)
    for i in range(N - 2):
        V[i + 3] += 4 * q * sq[i]                     # V/pi = 4 sqrt(2M) rho^3 u^{1/2}
    first = next(i for i in range(N + 1) if tau[i] != 0)
    return V[first] / tau[first], first, V, tau


def check_cutoff_volume_rates():
    setup_count()
    vals = []
    for M in (F(2), F(8), F(9, 2), F(25, 2)):
        for Lam in (F(0), F(1, 100), F(3, 7), F(-1, 5)):
            r, first, V, tau = mu_E_over_pi(M, Lam)
            vals.append(r == 12 * M and first == 3)
    GA.check("mu_E = 12 pi M per unit Killing time for every Lambda (16 cases)", all(vals))
    # the Lambda-dependence of V/tau first appears at relative order rho^6 = r^3, i.e. Lambda r^3/M
    r, first, V, tau = mu_E_over_pi(F(2), F(3, 7))
    r0, _, V0, tau0 = mu_E_over_pi(F(2), F(0))
    GA.check("Lambda enters V and tau only from relative order r^3",
             V[3:9] == V0[3:9] and tau[3:9] == tau0[3:9] and V[9] != V0[9])
    # (C1) slice r_c^3 = 2M: V'^2 = (4 pi r_c^2)^2 A(r_c) = (8 pi M)^2 (1 - r_c/2M + Lambda/3)
    ok = []
    for rc in (F(2), F(3), F(5, 2)):
        M = rc ** 3 / 2
        for Lam in (F(0), F(1, 10), F(2, 9)):
            A = 2 * M / rc - 1 + Lam * rc ** 2 / 3
            ok.append(16 * rc ** 4 * A == 64 * M ** 2 * (1 - rc / (2 * M) + Lam / 3))
    GA.check("(C1) slice volume rate 8 pi M sqrt(1 - r_c/2M + Lambda/3), exact", all(ok))


def sds(M, rb):
    Lam = 3 * (1 - 2 * M / rb) / rb ** 2
    kb = (2 * M / rb ** 2 - 2 * Lam * rb / 3) / 2
    return Lam, kb


def check_count_over_hole_period():
    setup_count()
    premise("scrambling.epoch-modular-period-two-unknowns-become")
    premise("synthesis.sds-clausius-fixes-area-constant")
    # Schwarzschild calibration, 1-nat convention: nu' (12 pi M)(8 pi M) = 4 pi M^2 -> nu' = 1/(24 pi)
    nu_pi = F(1, 24)                       # nu' times pi
    M = F(1)
    rows = []
    for rb in (F(2), F(21, 10), F(5, 2), F(29, 10), F(299, 100)):
        Lam, kb = sds(M, rb)
        f = 1 - 2 * M / rb - Lam * rb ** 2 / 3
        N_over_pi = nu_pi * 12 * M * 2 / kb          # N = nu' mu_E 2 pi/kappa_b, the pi's: (1/pi) pi pi
        ratio = N_over_pi / rb ** 2                  # A_b/4 = pi r_b^2
        u = 2 * M / rb
        w = 2 * M / rb ** 3
        rows.append((rb, Lam, ratio))
        GA.check("r_b = %s: horizon, kappa_b = (3M - r_b)/r_b^2, ratio %s = u/(3u-2) = 1/(1 - 2 Lambda/3 w_h)"
                 % (rb, ratio),
                 f == 0 and kb == (3 * M - rb) / rb ** 2 and ratio == M / (3 * M - rb) == u / (3 * u - 2)
                 == 1 / (1 - 2 * Lam / (3 * w)))
    GA.check("ratio 1 at Lambda = 0 and strictly increasing with Lambda: 1, 10/9, 2, 10, 100",
             [r for _, _, r in rows] == [F(1), F(10, 9), F(2), F(10), F(100)]
             and all(rows[i][1] < rows[i + 1][1] for i in range(len(rows) - 1)))
    # Nariai: r_b -> 3M with 9 Lambda M^2 -> 1; the ratio exceeds every bound
    big = []
    for j in range(1, 6):
        rb = 3 * M - M / 10 ** j
        Lam, kb = sds(M, rb)
        big.append(nu_pi * 24 * M / kb / rb ** 2 > F(10 ** j, 3) and 9 * Lam * M ** 2 < 1)
    GA.check("towards Nariai the count exceeds A_b/4 by more than 10^j/3", all(big))


def check_no_horizon_period_gives_area_law():
    setup_epoch()
    nu_pi = F(1, 24)
    for rb, rc in ((F(1), F(3, 2)), (F(1), F(2)), (F(2), F(7)), (F(1), F(100)), (F(3), F(4))):
        L3 = 1 / (rb ** 2 + rb * rc + rc ** 2)          # Lambda/3 from Vieta, roots rb, rc, -(rb+rc)
        M = L3 * rb * rc * (rb + rc) / 2
        f = lambda r: 1 - 2 * M / r - L3 * r ** 2
        kb = (2 * M / rb ** 2 - 2 * L3 * rb) / 2
        kc = -(2 * M / rc ** 2 - 2 * L3 * rc) / 2
        # epoch needed for N = A_b/4: nu' 12 pi M dt = pi rb^2 -> dt = rb^2/(12 M nu') = 2 pi rb^2/M
        dt_needed_over_pi = rb ** 2 / (12 * M * nu_pi)
        GA.check("rb=%s rc=%s: both horizons, needed epoch 2 pi r_b^2/M" % (rb, rc),
                 f(rb) == 0 and f(rc) == 0 and dt_needed_over_pi == 2 * rb ** 2 / M)
        GA.check("  kappa_c < kappa_b < M/r_b^2, so 2 pi/kappa_c > 2 pi/kappa_b > 2 pi r_b^2/M",
                 0 < kc < kb < M / rb ** 2)
    # kappa_c < M/r_b^2 in general: with x = rc/rb > 1, it is x^3 - x^2 + x + 1 > 0 (scaled by r_b)
    xs = [F(n, 7) for n in range(8, 200)]
    GA.check("kappa_c r_b^2/M < 1 for 192 ratios x = r_c/r_b, via x^3 - x^2 + x + 1 > 0",
             all(x ** 3 - x ** 2 + x + 1 > 0 and
                 ((2 * x * x - x - 1) / (2 * x * (1 + x + x * x))) < x * (1 + x) / (2 * (1 + x + x * x))
                 for x in xs))


def check_mean_entropy_forced_down():
    premise("synthesis.residue-from-mode-entropy")
    premise("synthesis.boundary-mode-thermal-entropy")
    premise("synthesis.exceptional-boundary-measure-one-calibration")
    premise("synthesis.q-splits-maximum-entropy-affine-weights")
    # area-law hypothesis: N <s> = A_b/4 with N from the count; at Lambda = 0, N_0 <s>_0 = A/4.
    M = F(1)
    out = []
    for rb in (F(2), F(21, 10), F(5, 2), F(29, 10)):
        Lam, kb = sds(M, rb)
        ratio = M / (3 * M - rb)
        u = 2 * M / rb
        s_rel = 1 / ratio                     # <s>_SdS/<s>_0
        out.append(s_rel)
        GA.check("r_b = %s: <s>_SdS/<s>_0 = (3u - 2)/u = %s" % (rb, s_rel), s_rel == (3 * u - 2) / u)
    # under (Q-w) the slope is c = kappa_b: x_k = 2 pi k (pi formal: x_k/(2 pi) = k) on every member,
    # so <s> is the same on the family and cannot equal <s>_0 (3u-2)/u unless u = 1
    xs = []
    for rb in (F(2), F(21, 10), F(5, 2)):
        Lam, kb = sds(M, rb)
        xs.append([kb * k / kb for k in range(-3, 4)])
    GA.check("(Q-w): x_k/2pi = k on every member, independent of Lambda", all(x == xs[0] for x in xs)
             and xs[0] == [F(k) for k in range(-3, 4)])
    GA.check("mean entropy per counted mode forced below the Schwarzschild value: 1, 9/10, 1/2, 1/10",
             out == [F(1), F(9, 10), F(1, 2), F(1, 10)])
