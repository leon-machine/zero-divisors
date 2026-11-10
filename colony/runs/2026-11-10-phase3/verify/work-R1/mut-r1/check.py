"""synthesis.red-tilt-criterion-on-power-law-stages-and-the-index-ledger-of-the-stored-sources: exact checks.

Mode equation (E): chi'' + (1 + f) chi'/T + (k^2 T^(-2P) - kappa T^(-2)) chi = 0, with q = 1 - P nonzero and
s = k T^q / q.  The stored Bessel reduction gives chi = T^(-f/2) Z_nu(s) with nu^2 = (f^2 + 4 kappa)/(4 q^2); the
exited spectrum has index n - 1 = 3 - 2 nu (stored), so it is red exactly when f^2 + 4 kappa > 9 q^2.

(1) The order, by exact Frobenius series: chi = T^(-f/2) sum_m c_m s^(sigma nu + 2m), c_m = -c_(m-1)/(4m(m + sigma nu)),
    sigma = +1 or -1, inserted in (E) with monomials T^e carried as exact exponents; every coefficient below the
    truncation order cancels; a wrong order leaves a nonzero lowest coefficient.  The branch sigma = -1 carries
    k^(-nu), which is the index 3 - 2 nu of k^3 |chi|^2.
(2) Isotropic power laws a = T^p in d observed directions, massless and minimally coupled: f = d p - 1, P = p.
    (d p - 1)^2 - 9 (1 - p)^2 = ((d + 3) p - 4)((d - 3) p + 2); for d = 3 this is 12 p - 8, so red exactly for
    p > 2/3; the Kasner trace sum P = 1 forces p = 1/d, f = 0, order 0.  The measured window in p on both branches;
    the fluid reading p = 2/(3(1 + w_f)) gives n - 1 = 12 w_f/(1 + 3 w_f); invariance of nu^2 under Wands' map.
(3) Ledger on the Kasner side.  The exponents are read off the residue bivector B = sum_a P_a e_0 e_a of Cl(1,4) as
    weights (1/2)(e_a B - B e_a) = P_a e_0; the trace is 1 on the equal-exponent segment (p, p, p, 1 - 3p) and the
    scalar part of B B is the sum of squares.  Rows: cross modes (f = 0), the Kaluza-Klein vector (f = 2(P_h - p)),
    the hidden-direction component (lambda = -1), a confined field (lambda = 0), a bulk zero mode (lambda = 1),
    each with f = (lambda - 1) P_h; margins 9 q^2 - f^2 in closed form; the tree-level couplings at the isotropic
    point, 4 nu^2 = (lambda - 1)^2 + 6 xi <= 7 < 9; the fitted window of xi recomputed from the measured index.
(4) De Sitter row: (E) in conformal time has f = -3, P = 0, kappa = -m^2/H^2; with m^2/H^2 = -w(w + 3),
    nu^2 = (w + 3/2)^2, never above 9/4 on [-3, 0], equal to 9/4 only at the ends; the measured index needs
    w = 351/20000 and m^2/H^2 = -21183201/400000000.
(5) Dust with a cosmological constant: H^2 = A a^(-3) + Lambda/3.  Monomials A^r Lambda^t k^u invariant under
    (a, k, A) -> (c a, c k, c^3 A) and of zero time dimension form a line spanned by (2, 1, -6); at exit of the dust
    stage (k = a H) the ratio of the constant's density to the dust's is Lambda A^2/(3 k^6); for a spectrum ratio
    G(x) = 1 + g1 x + g2 x^2, x proportional to k^(-6), the running and the index obey alpha + 6 (n - 1) = O(x^2).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

NS1, SIG = F("-0.0351"), F("0.0042")
SAMPLES_E = [  # (f, kappa, P) with rational order
    (F(0), F(0), F(1, 3)), (F(2), F(0), F(0)), (F(-3), F(-2), F(0)), (F(1), F(2), F(1, 2)),
    (F(-4, 3), F(0), F(1, 3)), (F(1), F(3, 4), F(-1, 3)), (F(3), F(4), F(5, 2)), (F(-3), F(0), F(0)),
]
P_GRID = [F(i, 40) for i in range(0, 21)]
P_WIDE = [F(i, 24) for i in range(-24, 97) if i != 24]
LISTED_XI = [F(0), F(1, 8), F(3, 20), F(1, 6), F(3, 16), F(1, 5), F(1, 4), F(1, 3), F(3, 8), F(1, 2), F(-1, 6), F(-1, 3)]
W_GRID = [F(-i, 16) for i in range(0, 49)]
S14 = (1, -1, -1, -1, -1)


def int_sqrt(n):
    """Integer square root by Newton's iteration on integers; None unless n is a perfect square."""
    if n < 0:
        return None
    r = n
    while r * r > n:
        r = (r + n // r) // 2 if r else 0
    return r if r * r == n else None


def frac_sqrt(x):
    """Exact square root of a rational that is a square of a rational, else None."""
    rn, rd = int_sqrt(x.numerator), int_sqrt(x.denominator)
    return None if rn is None or rd is None else F(rn, rd)


def residual(f, kappa, P, nu, sigma, terms):
    """Coefficients (dict exponent of T -> coefficient) of (E) applied to the truncated Frobenius series, k = 1."""
    q = 1 - P
    out = {}
    c = F(1)
    for m in range(terms):
        if m:
            c = -c / (4 * m * (m + sigma * nu))
        r = sigma * nu + 2 * m
        e = -f / 2 + q * r
        coef = c * (1 / q) ** (2 * m)  # s = T^q/q; the common factor q^(-sigma nu) is dropped
        out[e - 2] = out.get(e - 2, 0) + coef * (e * (e - 1) + (1 + f) * e - kappa)
        out[e - 2 * P] = out.get(e - 2 * P, 0) + coef
    return out, -f / 2 + q * sigma * nu - 2, e - 2 * P


def check_order_of_the_mode_equation_by_exact_frobenius_series():
    premise("synthesis.imported-bessel-reduction-and-small-argument-hankel-forms")
    premise("synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling")
    ok = True
    for f, kappa, P in SAMPLES_E:
        q = 1 - P
        nu = frac_sqrt((f * f + 4 * kappa) / (4 * q * q))
        ok = ok and nu is not None
        for sigma in (1, -1):
            if sigma == -1 and nu == int(nu):
                continue  # the second solution is logarithmic at integer order
            res, lowest, top = residual(f, kappa, P, nu, sigma, 7)
            ok = ok and all(v == 0 for e, v in res.items() if e != top) and res[top] != 0
            bad, low_bad, _ = residual(f, kappa, P, nu + F(1, 7), sigma, 7)
            ok = ok and bad[low_bad] != 0
        # index: the exited branch carries k^(-nu), so k^3 |chi|^2 has index 3 - 2 nu; red iff f^2 + 4 kappa > 9 q^2
        index = 3 - 2 * nu
        ok = ok and ((index < 0) == (f * f + 4 * kappa > 9 * q * q)) and ((index == 0) == (4 * nu * nu == 9))
    # the stored cases: order 0 for (0, 0, P); conformal coupling at the isotropic point (kappa = xi c^2 = 1/9) gives 1/2
    ok = ok and frac_sqrt((F(0) + 4 * F(1, 9)) / (4 * F(2, 3) ** 2)) == F(1, 2)
    assert ok
    return True


def nu2_power_law(p, d):
    return (d * p - 1) ** 2 / (4 * (1 - p) ** 2)


def check_power_law_threshold_two_thirds_and_the_kasner_trace():
    premise("synthesis.imported-wands-duality-of-perturbation-spectra")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    premise("synthesis.kasner-approach-gives-horizon-exit-and-index-three")
    premise("synthesis.finite-range-descent-deposit-cannot-seed-cmb")
    ok = True
    for p in P_WIDE:
        for d in (3, 4, 5):
            lhs = (d * p - 1) ** 2 - 9 * (1 - p) ** 2
            ok = ok and lhs == ((d + 3) * p - 4) * ((d - 3) * p + 2)
        red = 4 * nu2_power_law(p, 3) > 9
        ok = ok and (red == (p > F(3, 5))) and ((3 * p - 1) ** 2 - 9 * (1 - p) ** 2 == 12 * p - 8)
        # Wands' form of the order and his map
        ok = ok and nu2_power_law(p, 3) == (F(3, 2) + 1 / (p - 1)) ** 2
        if p != F(2, 3):
            pd = (1 - 2 * p) / (2 - 3 * p)
            ok = ok and (pd == 1 or nu2_power_law(pd, 3) == nu2_power_law(p, 3))
    # Kasner trace: equal exponents with sum 1 give p = 1/d, friction excess 0, order 0
    for d in (3, 4, 5):
        ok = ok and nu2_power_law(F(1, d), d) == 0 and F(1, d) < F(2, 3)
    # stored stages: stiff 1/3 (order 0), radiation 1/2 (order 1/2, index 2), dust 2/3 (order 3/2, index 0)
    ok = ok and [nu2_power_law(p, 3) for p in (F(1, 3), F(1, 2), F(2, 3))] == [0, F(1, 4), F(9, 4)]
    # measured window, contracting branch p < 1: n - 1 = (4 - 6p)/(1 - p); expanding branch p > 1: n - 1 = -2/(p - 1)
    for N in (NS1 - 3 * SIG, NS1, NS1 + 3 * SIG):
        pc, pe = (4 - N) / (6 - N), 1 - 2 / N
        ok = ok and F(2, 3) < pc < 1 and pe > 1
        ok = ok and 3 - (3 * pc - 1) / (1 - pc) == N and 3 - (3 * pe - 1) / (pe - 1) == N
        wf = 2 / (3 * pc) - 1
        ok = ok and N == 12 * wf / (1 + 3 * wf) and F(-41, 10000) < wf < F(-18, 10000)
    wf0 = 2 / (3 * ((4 - NS1) / (6 - NS1))) - 1
    ok = ok and F(-30, 10000) < wf0 < F(-28, 10000)  # the stored -0.0029
    pc0 = (4 - NS1) / (6 - NS1)
    ok = ok and pc0 == F(40351, 60351) and 1 - 2 / NS1 == F(20351, 351)
    assert ok
    return True


def residue_weights(P):
    """Exponents read from B = sum_a P_a e_0 e_a in Cl(1,4): (1/2)(e_a B - B e_a) = P_a e_0; also the scalar of B B."""
    e = [GA.gen(i) for i in range(5)]
    B = GA.add(*[GA.scal(P[a - 1], GA.mul(e[0], e[a], S14)) for a in range(1, 5)])
    out = []
    for a in range(1, 5):
        c = GA.scal(F(1, 2), GA.sub(GA.mul(e[a], B, S14), GA.mul(B, e[a], S14)))
        w = GA.dot(c, e[0], S14)
        if not GA.eq(c, GA.scal(w, e[0])):
            return None, None
        out.append(w)
    BB = GA.mul(B, B, S14)
    return out, BB.get((), F(0))


def check_ledger_of_kasner_rows_from_residue_weights():
    premise("synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling")
    premise("synthesis.kasner-hidden-scale-coupled-scalars-stay-blue")
    premise("synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    ok = True
    for p in P_GRID:
        P, BB = residue_weights([p, p, p, 1 - 3 * p])
        ok = ok and P is not None and sum(P) == 1 and BB == sum(x * x for x in P) and BB <= 1
        ok = ok and ((BB == 1) == (p in (F(0), F(1, 2))))
        q, ph = 1 - P[0], P[3]
        red = lambda f: f * f > 9 * q * q
        # cross modes of observed pairs: f = 2(P_b - P_a) = 0
        ok = ok and 2 * (P[1] - P[0]) == 0 and not red(F(0))
        # hidden-scale weights lambda = -1, 0, 1: f = (lambda - 1) P_h, never red on the segment
        for lam in (-1, 0, 1):
            f = (lam - 1) * ph
            ok = ok and not red(f) and 9 * q * q - 4 * ph * ph == (1 + 3 * p) * (5 - 9 * p)
        # Kaluza-Klein vector potential: f = 2(P_h - p); red exactly for p > 5/11; its field strength has index
        # 5 - 2 nu >= 1 exactly when f^2 <= 16 q^2, which holds on the whole segment
        f = 2 * (ph - P[0])
        ok = ok and (red(f) == (p > F(5, 11))) and f * f - 9 * q * q == (1 + 5 * p) * (11 * p - 5)
        ok = ok and f * f <= 16 * q * q
    # the isotropic point in the Einstein frame: 4 nu^2 = (lambda - 1)^2 + 6 xi for the twelve tree-level couplings
    worst = max((lam - 1) ** 2 + 6 * xi for lam in (-1, 0, 1) for xi in LISTED_XI)
    ok = ok and worst == 7 and worst < 9
    # the fitted window of xi (lambda = 1), recomputed from the measured index at three standard deviations
    lo, hi = (3 - (NS1 + 3 * SIG)) ** 2 / 6, (3 - (NS1 - 3 * SIG)) ** 2 / 6
    ok = ok and lo == F("1.522584375") and hi == F("1.548079215")
    ok = ok and all(not (lo <= xi <= hi) for xi in LISTED_XI) and lo < F(3, 2) + F(1, 40) < hi
    assert ok
    return True


def check_de_sitter_row_in_the_same_equation():
    premise("synthesis.frozen-phase-spectrum-not-red")
    premise("mass.weight-polynomial-two-series")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    premise("synthesis.frozen-point-geometry-reads-descent-as-vacuum")
    ok = True
    f, P = F(-3), F(0)
    for w in W_GRID:
        m2 = -w * (w + 3)
        nu2 = (f * f + 4 * (-m2)) / (4 * (1 - P) ** 2)
        ok = ok and nu2 == (w + F(3, 2)) ** 2 and 4 * nu2 <= 9
        ok = ok and ((4 * nu2 == 9) == (w in (F(0), F(-3))))
        if w >= F(-3, 2):
            ok = ok and 3 - 2 * (w + F(3, 2)) == -2 * w  # the stored n - 1 = -2 w of the leading weight
    # red needs a negative mass term; the measured index needs w = 351/20000
    w = -NS1 / 2
    m2 = -w * (w + 3)
    ok = ok and w == F(351, 20000) and m2 == F(-21183201, 400000000) and m2 < 0
    ok = ok and 3 - 2 * (w + F(3, 2)) == NS1
    assert ok
    return True


def check_dust_with_cosmological_constant_scaling_and_running():
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    ok = True
    # invariant monomials A^r Lambda^t k^u: scaling weight 3r + u = 0, time dimension 2r + 2t + u = 0
    M = [[F(3), F(0), F(1)], [F(2), F(2), F(1)]]
    ok = ok and GA.mat_rank(M) == 2
    v = [F(2), F(1), F(-6)]
    ok = ok and all(sum(r[i] * v[i] for i in range(3)) == 0 for r in M)
    for A, Lam, k, a, c in ((F(5), F(2, 7), F(3), F(4), F(11, 3)), (F(1, 9), F(6), F(7, 2), F(1, 5), F(2))):
        H2 = lambda A_, a_: A_ / a_ ** 3 + Lam / 3
        ok = ok and H2(c ** 3 * A, c * a) == H2(A, a) and (c * k) / (c * a) == k / a
        ok = ok and Lam * (c ** 3 * A) ** 2 / (c * k) ** 6 == Lam * A ** 2 / k ** 6
        # exit of the dust stage: k^2 = a^2 A a^(-3) gives a = A/k^2, and the density ratio (Lambda/3)/(A a^(-3))
        a_exit = A / k ** 2
        ok = ok and k ** 2 == a_exit ** 2 * (A / a_exit ** 3)
        ok = ok and (Lam / 3) / (A / a_exit ** 3) == Lam * A ** 2 / (3 * k ** 6)
    # index and running of k^0 G(x), x proportional to k^(-6): N = -6 x G'/G, alpha = -6 x dN/dx
    for g1, g2 in ((F(4), F(7)), (F(12), F(0)), (F(3, 2), F(-5))):
        for j in (3, 6, 9):
            x = F(1, 10 ** j)
            G, G1, G2 = 1 + g1 * x + g2 * x * x, g1 + 2 * g2 * x, 2 * g2
            N = -6 * x * G1 / G
            dN = -6 * (G1 / G + x * (G2 * G - G1 * G1) / (G * G))
            alpha = -6 * x * dN
            ok = ok and alpha + 6 * N == -36 * x * x * (G1 * G1 - G2 * G) / (G * G)
            ok = ok and abs(alpha / N + 6) < 100 * x and N < 0 and alpha > 0
    # at the measured index the leading relation gives the running 6 * 0.0351 = 0.2106
    ok = ok and -6 * NS1 == F(2106, 10000)
    assert ok
    return True
