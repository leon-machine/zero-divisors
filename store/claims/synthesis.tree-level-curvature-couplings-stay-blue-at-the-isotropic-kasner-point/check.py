"""synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point: exact checks of the tree-level curvature couplings the series fixes for its scalars, where on a Kasner approach they
act, and the tilt each gives.

(1) Dictionary off the Einstein region. Tractors in GA as in the dictionary's own check: generators 0..n-1 of
    signature (1, n-1) and e+, e-; n0 = (e+ + e-)/2, ninf = e+ - e-, ninf . n0 = 1. The Thomas operator
    D sigma = (w(n+2w-2) sigma, (n+2w-2) grad sigma, -(Box sigma - w J sigma)) is paired by GA.dot with a tractor
    I = ninf + rho n0 whose rho is independent of J; I . D sigma = -Box sigma - (w J + rho w(n+2w-2)) sigma, so the
    Klein-Gordon form (Box + m^2) sigma = 0 has m^2 = -w J - rho w(n+2w-2), J = R/(2(n-1)). Three extensions
    (labels here: (b) is the entity's first extension, (a) its second, (c) its third):
      (b) the frozen point of the field-space premise, rho = Lambda/6 constant, Thomas operator of the derived metric:
          m^2 = xi R + mu, xi = -w/(2(n-1)) (n = 4: -w/6), mu = -w(w+1) Lambda/3 (n = 4);
      (a) rho = J/n, the derived metric's own scale tractor: xi = -w(w+n-1)/(n(n-1)) (n = 4: -w(w+3)/12), mu = 0;
      (c) the Thomas operator of the connection preserving I (Schouten slot rho id, so J -> n rho): xi = 0,
          mu = -w(w+3) Lambda/3.
    All three equal the dictionary -w(w+3) Lambda/3 at R = 4 Lambda. The conformal weight w = 1 - n/2 gives the
    Yamabe coefficient (n-2)/(4(n-1)) in (b) and (a) with mu = 0 in (b), for n = 3..6.
(2) Ricci scalar at the store's Kasner points, by an exact monomial engine on -dT^2 + sum T^(2P)(dx)^2 (mostly plus,
    R > 0 for an accelerating power law, the de Sitter sign): R T^2 = 0 on the four-dimensional circle (Schwarzschild
    interior and BKL points) and at the five-dimensional vacuum ends (0,0,0,1), (1/2,1/2,1/2,-1/2); the induced
    four-metrics (0,0,0) and (1/2,1/2,1/2) at those ends have R = 0; the isotropic disk point (1/3,1/3,1/3) has
    R T^2 = -2/3 = -c^2. So a curvature coupling acts at that point only.
(3) Index of each listed coupling there, with c^2 = -R T^2 taken from the engine of (2) and no hidden-scale weight
    in the Einstein frame: nu^2 = 3 xi/2, n - 1 = 3 - 2 nu; the listed values (twelve: 0, 1/8, 3/20, 1/6, 3/16, 1/5,
    1/4, 1/3, 3/8, 1/2, -1/6, -1/3) are all at most 1/2, index above 63/50; the three-sigma window needs
    xi in [xi_lo, xi_hi] (exact), none listed.
(3') Hidden-scale weight: a scalar whose four-dimensional action carries b^lambda has Einstein-frame weight
    b^(lambda - 1); at both five-dimensional ends the Einstein-frame reduction has b ~ tau_E^(+-2/3), so the stored
    order formula with pump w = (lambda - 1)(+-2/3) gives nu^2 = (lambda - 1)^2/4 + 3 xi/2 (curvature term taken
    with the same power of b as the kinetic term); for |lambda - 1| <= 2 and xi <= 1/2, 4 nu^2 <= 7 and the index
    exceeds 7/20 (3 - sqrt 7). The Wilson-line weight lambda = -1 would meet the window for an unfixed coupling
    xi in [2/3 (nu_lo^2 - 1), 2/3 (nu_hi^2 - 1)] (exact; recorded, not a candidate).
(4) The window read back through the extensions: (b) w = -6 xi in [-6 xi_hi, -6 xi_lo], below -3, where
    -w(w+3) < 0 (outside both unitary series); on the principal series (b) gives Im xi = -/+ nu/6 != 0; (c) xi = 0;
    (a) needs the principal series with 12 xi - 9/4 = nu^2 in an exact interval, real weights giving xi <= 3/16.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

NS1, SIG = F("-0.0351"), F("0.0042")
WS = [F(0), F(-1), F(-2), F(-3), F(-3, 2), F(1), F(-1, 2), F(7, 3), F(-5, 4)]
LISTED = [F(0), F(1, 8), F(3, 20), F(1, 6), F(3, 16), F(1, 5), F(1, 4), F(1, 3), F(3, 8), F(1, 2), F(-1, 6), F(-1, 3)]
_ALG = {}


def algebra(n):
    if n not in _ALG:
        S = tuple([1] + [-1] * (n - 1) + [1, -1])
        E = [GA.gen(i) for i in range(n + 2)]
        n0 = GA.scal(F(1, 2), GA.add(E[n], E[n + 1]))
        ninf = GA.sub(E[n], E[n + 1])
        grad = GA.add(*[GA.scal(F(k + 2), E[k]) for k in range(n)])
        _ALG[n] = (S, ninf, n0, grad)
    return _ALG[n]


def mass_term(w, n, J, rho):
    """m^2 read off I . D sigma = 0 with I = ninf + rho n0 (rho independent of J); also returns the gradient pairing."""
    S, ninf, n0, grad = algebra(n)
    I = GA.add(ninf, GA.scal(rho, n0))
    d_sigma = GA.add(GA.scal(w * (n + 2 * w - 2), ninf), GA.scal(w * J, n0))
    a = GA.dot(I, GA.scal(-1, n0), S)
    b = GA.dot(I, d_sigma, S)
    c = GA.dot(I, GA.scal(n + 2 * w - 2, grad), S)
    return b / a, a, c


def check_dictionary_extensions_off_the_einstein_region():
    premise("mass.imported-thomas-operator")
    premise("mass.mass-weight-dictionary")
    premise("synthesis.parallel-frozen-point-on-matter-regions-is-the-field-space-premise")
    ok = True
    count = 0
    for n in (3, 4, 5, 6):
        for w in WS:
            for R in (F(1), F(-2, 3), F(12), F(5, 7)):
                for lam in (F(3), F(1, 7), F(-6, 5)):
                    J = R / (2 * (n - 1))
                    rho = lam / 6
                    m2b, a, c = mass_term(w, n, J, rho)
                    ok = ok and a == -1 and c == 0
                    # (b): xi R + mu with xi = -w/(2(n-1)), mu = -rho w (n + 2w - 2)
                    ok = ok and m2b == F(-w, 2 * (n - 1)) * R - rho * w * (n + 2 * w - 2)
                    # (a): rho = J/n
                    m2a, _, _ = mass_term(w, n, J, J / n)
                    ok = ok and m2a == -w * (w + n - 1) * R / (n * (n - 1))
                    # (c): J replaced by n rho
                    m2c, _, _ = mass_term(w, n, n * rho, rho)
                    ok = ok and m2c == -w * (w + n - 1) * 2 * rho
                    if n == 4:
                        ok = ok and m2b == -w * R / 6 - w * (w + 1) * lam / 3
                        ok = ok and m2a == -w * (w + 3) * R / 12
                        ok = ok and m2c == -w * (w + 3) * lam / 3
                        if R == 4 * lam:
                            ok = ok and m2a == m2b == m2c == -w * (w + 3) * lam / 3
                    count += 1
    GA.check("three extensions of I . D sigma = 0 on %d sample points, agreeing on Einstein regions" % count,
             ok and count == 432)
    # control: at R = 1, Lambda = 3 (not Einstein), w = -2, the frozen point (rho = 1/2) and the own-scale
    # tractor (rho = J/4 = 1/24) give different mass terms: 1/3 - 2 = -5/3 against -(-2)(1)/12 = 1/6
    m2_fp, _, _ = mass_term(F(-2), 4, F(1, 6), F(1, 2))
    m2_own, _, _ = mass_term(F(-2), 4, F(1, 6), F(1, 24))
    GA.check("control: off the Einstein region (b) and (a) differ (-5/3 against 1/6)",
             m2_fp == F(-5, 3) and m2_own == F(1, 6))
    # conformal weight w = 1 - n/2: Yamabe coefficient (n-2)/(4(n-1)) in (b) and (a); no mass term in (b)
    yam = True
    for n in (3, 4, 5, 6):
        w = 1 - F(n, 2)
        xi_b = F(-1, 2 * (n - 1)) * w
        xi_a = -w * (w + n - 1) / (n * (n - 1))
        mu_b = -w * (n + 2 * w - 2)
        yam = yam and xi_b == xi_a == F(n - 2, 4 * (n - 1)) and mu_b == 0
    GA.check("conformal weight gives (n-2)/(4(n-1)) in (a) and (b), no mass in (b), n = 3..6", yam)
    GA.check("values: 1/6 (n=4), 3/16 (n=5), 1/5 (n=6)",
             (F(2, 12), F(3, 16), F(4, 20)) == (F(1, 6), F(3, 16), F(1, 5)))
    # four-dimensional values of (b) and (a) at the real dictionary weights
    xb = {w: -w / 6 for w in (F(0), F(-1), F(-3, 2), F(-2), F(-3))}
    xa = {w: -w * (w + 3) / 12 for w in (F(0), F(-1), F(-3, 2), F(-2), F(-3))}
    GA.check("(b) on w = 0, -1, -3/2, -2, -3: 0, 1/6, 1/4, 1/3, 1/2",
             [xb[w] for w in (F(0), F(-1), F(-3, 2), F(-2), F(-3))] == [0, F(1, 6), F(1, 4), F(1, 3), F(1, 2)])
    GA.check("(a) on w = 0, -1, -3/2, -2, -3: 0, 1/6, 3/16, 1/6, 0",
             [xa[w] for w in (F(0), F(-1), F(-3, 2), F(-2), F(-3))] == [0, F(1, 6), F(3, 16), F(1, 6), 0])
    # real weights of the unitary range [-3, 0]: (b) in [0, 1/2], (a) in [0, 3/16]
    grid = [F(-3) + F(k, 40) * 3 for k in range(41)]
    GA.check("(b) maps [-3, 0] into [0, 1/2], (a) into [0, 3/16]",
             all(0 <= -w / 6 <= F(1, 2) for w in grid) and all(0 <= -w * (w + 3) / 12 <= F(3, 16) for w in grid))
    return ok and yam


# ---------------------------------------------------------------- Ricci scalar of a diagonal power-law metric
def m_add(*xs):
    out = {}
    for x in xs:
        for e, v in x.items():
            out[e] = out.get(e, 0) + v
            if out[e] == 0:
                del out[e]
    return out


def m_mul(x, y):
    out = {}
    for e1, v1 in x.items():
        for e2, v2 in y.items():
            out[e1 + e2] = out.get(e1 + e2, 0) + v1 * v2
            if out[e1 + e2] == 0:
                del out[e1 + e2]
    return out


def m_d(x, coord):
    if coord != 0:
        return {}
    return {e - 1: v * e for e, v in x.items() if e != 0}


def m_sc(c, x):
    return {e: c * v for e, v in x.items() if c * v != 0}


def ricci_scalar(P):
    """metric -dT^2 + sum_i T^(2 P_i) (dx^i)^2, mostly plus; returns R as {exponent: coefficient}."""
    D = len(P) + 1
    g = [{F(0): F(-1)}] + [{2 * F(p): F(1)} for p in P]
    gi = [{F(0): F(-1)}] + [{-2 * F(p): F(1)} for p in P]
    Gam = [[[{} for _ in range(D)] for _ in range(D)] for _ in range(D)]
    for s in range(D):
        for x in range(D):
            for y in range(D):
                t = {}
                if s == y:
                    t = m_add(t, m_d(g[s], x))
                if s == x:
                    t = m_add(t, m_d(g[s], y))
                if x == y:
                    t = m_add(t, m_sc(-1, m_d(g[x], s)))
                Gam[s][x][y] = m_sc(F(1, 2), m_mul(gi[s], t))
    R = {}
    for x in range(D):
        acc = {}
        for s in range(D):
            acc = m_add(acc, m_d(Gam[s][x][x], s), m_sc(-1, m_d(Gam[s][x][s], x)))
            for l in range(D):
                acc = m_add(acc, m_mul(Gam[s][s][l], Gam[l][x][x]), m_sc(-1, m_mul(Gam[s][x][l], Gam[l][x][s])))
        R = m_add(R, m_mul(gi[x], acc))
    return R


def bkl(u):
    d = 1 + u + u * u
    return (-u / d, (1 + u) / d, u * (1 + u) / d)


def check_curvature_coupling_acts_only_at_the_isotropic_disk_point():
    premise("interior.kasner-form-interior")
    premise("synthesis.bkl-bounce-invariant-holonomy-and-bound")
    premise("synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall")
    premise("synthesis.kasner-hidden-scale-coupled-scalars-stay-blue")
    ok = True
    circle = [(F(-1, 3), F(2, 3), F(2, 3))] + [bkl(u) for u in (F(2), F(3), F(7, 2), F(5))]
    for P in circle:
        ok = ok and sum(P) == 1 and sum(p * p for p in P) == 1 and ricci_scalar(P) == {}
    GA.check("R = 0 on the four-dimensional circle (Schwarzschild interior and BKL points)", ok)
    ends = [(F(0), F(0), F(0), F(1)), (F(1, 2), F(1, 2), F(1, 2), F(-1, 2))]
    ok5 = all(ricci_scalar(P) == {} for P in ends)
    GA.check("R_5 = 0 at both five-dimensional vacuum ends: a bulk coupling to R_5 is inert there", ok5)
    ind = all(ricci_scalar(P[:3]) == {} for P in ends)
    GA.check("induced four-metrics (0,0,0) and (1/2,1/2,1/2) at the ends have R_4 = 0", ind)
    iso = ricci_scalar((F(1, 3), F(1, 3), F(1, 3)))
    GA.check("isotropic disk point (1/3,1/3,1/3): R T^2 = -2/3 = -c^2", iso == {F(-2): F(-2, 3)})
    # general disk point and the closed form R T^2 = sum P^2 - 2 sum P + (sum P)^2
    gen = True
    for P in [(F(1, 2), F(1, 4), F(1, 4)), (F(3, 5), F(1, 5), F(1, 5)), (F(1, 5), F(2, 5), F(3, 10), F(1, 10))]:
        s1, s2 = sum(P), sum(p * p for p in P)
        gen = gen and ricci_scalar(P) == ({F(-2): s2 - 2 * s1 + s1 * s1} if s2 - 2 * s1 + s1 * s1 != 0 else {})
    GA.check("R T^2 = sum P^2 - 2 sum P + (sum P)^2 at sampled points", gen)
    # sign: an accelerating power law T^q (q = 2) has R > 0, the de Sitter sign of the dictionary
    acc = ricci_scalar((F(2), F(2), F(2)))
    GA.check("sign control: power law q = 2 has R T^2 = 6 q (2q - 1) = 36 > 0", acc == {F(-2): F(36)})
    GA.check("control: a stiff point is not Ricci-flat", ricci_scalar((F(1, 3), F(1, 3), F(1, 3))) != {})
    return ok and ok5 and ind


def window():
    lo, hi = NS1 - 3 * SIG, NS1 + 3 * SIG
    nu_lo, nu_hi = (3 - hi) / 2, (3 - lo) / 2
    return lo, hi, F(2, 3) * nu_lo * nu_lo, F(2, 3) * nu_hi * nu_hi


def check_listed_couplings_are_blue_at_the_isotropic_point():
    premise("synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    premise("synthesis.imported-einstein-cartan-matter-coupling")
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("mass.weight-polynomial-two-series")
    lo, hi, xlo, xhi = window()
    GA.check("three-sigma window of n - 1: [-0.0477, -0.0225]", (lo, hi) == (F("-0.0477"), F("-0.0225")))
    GA.check("xi window exact: [2/3 ((3.0225)/2)^2, 2/3 ((3.0477)/2)^2] inside the stored [1.5225, 1.5481]",
             F("1.5225") <= xlo < xhi <= F("1.5481") and xlo == F(2, 3) * F(30225, 20000) ** 2)
    # order at the isotropic point: nu^2 = (w^2 + 4 xi c^2)/(4 (1 - p)^2) with w = 0, c^2 = 2/3, p = 1/3
    iso = ricci_scalar((F(1, 3), F(1, 3), F(1, 3)))
    c2 = -iso[F(-2)]
    GA.check("c^2 at the isotropic point from the Ricci engine: 2/3", c2 == F(2, 3))
    ok = True
    for xi in LISTED:
        nu2 = (0 + 4 * xi * c2) / (4 * (1 - F(1, 3)) ** 2)
        ok = ok and nu2 == F(3, 2) * xi
        ok = ok and not (xlo <= xi <= xhi)
        # index 3 - 2 nu >= 63/50: 2 nu <= 87/50 iff 4 nu^2 <= (87/50)^2
        ok = ok and 4 * nu2 < F(87, 50) ** 2
        # and far from the window: 3 - 2 nu > hi + 1
        ok = ok and 4 * nu2 < (3 - hi - 1) ** 2
    GA.check("each listed coupling: nu^2 = 3 xi/2, outside the window, index above 63/50", ok)
    GA.check("largest listed xi = 1/2: nu^2 = 3/4, index 3 - sqrt(3)", max(LISTED) == F(1, 2) and F(3, 2) * F(1, 2) == F(3, 4))
    GA.check("conformal 1/6: nu = 1/2, index 2", F(3, 2) * F(1, 6) == F(1, 4))
    GA.check("minimal 0: nu = 0 (the stored logarithm)", F(3, 2) * F(0) == 0)
    GA.check("look-elsewhere: twelve listed values, largest 1/2", len(set(LISTED)) == 12 and max(LISTED) == F(1, 2))
    GA.check("control: xi = 3/2 gives nu = 3/2, index 0, still outside", F(3, 2) * F(3, 2) == F(9, 4) and not (xlo <= F(3, 2) <= xhi))
    return ok


def check_window_needs_weight_outside_unitary_range():
    premise("mass.weight-polynomial-two-series")
    premise("mass.imported-unitary-representations-de-sitter-group")
    premise("synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    lo, hi, xlo, xhi = window()
    # (b): xi = -w/6, so w in [-6 xhi, -6 xlo]
    wl, wh = -6 * xhi, -6 * xlo
    GA.check("exact xi window [487227/320000, 309615843/200000000]",
             (xlo, xhi) == (F(487227, 320000), F(309615843, 200000000)))
    GA.check("(b): window weights exactly [-928847529/100000000, -1461681/160000]",
             (wl, wh) == (F(-928847529, 100000000), F(-1461681, 160000)))
    GA.check("(b): window weights lie in [-9.2886, -9.1350]", F("-9.2886") <= wl < wh <= F("-9.1350"))
    m2 = [-w * (w + 3) for w in (wl, wh)]
    GA.check("(b): m^2/H^2 = -w(w+3) between -58.5 and -56.0, negative", all(F("-58.5") < v < F("-56.0") for v in m2))
    GA.check("(b): end value at the weak end exactly -1434904465761/25600000000",
             m2[1] == F(-1434904465761, 25600000000))
    GA.check("(b): -w(w+3) < 0 for every w < -3", all(-w * (w + 3) < 0 for w in [wl + F(k, 10) * (wh - wl) for k in range(11)]))
    # (b) on the principal series w = -3/2 + i nu: xi = (3/2 - i nu)/6, imaginary part -nu/6
    ok_c = True
    for nu in (F(1, 2), F(4), F(10 ** 6)):
        re, im = F(3, 2) / 6, -nu / 6
        ok_c = ok_c and re == F(1, 4) and im != 0 and 6 * im == -nu
        # on Einstein regions the dictionary is still real: -w(w+3) = 9/4 + nu^2
        a_re, a_im = F(-3, 2), nu
        prod_re = -(a_re * (a_re + 3) - a_im * a_im)
        prod_im = -(a_re * a_im + a_im * (a_re + 3))
        ok_c = ok_c and prod_re == F(9, 4) + nu * nu and prod_im == 0
    GA.check("(b) on the principal series: xi complex (real part 1/4), dictionary real on Einstein regions", ok_c)
    # (c): xi = 0 for every weight
    GA.check("(c): xi = 0 is outside the window", not (xlo <= 0 <= xhi))
    # (a): real weights give xi <= 3/16; the window needs 12 xi - 9/4 = nu^2 in [12 xlo - 9/4, 12 xhi - 9/4]
    nl, nh = 12 * xlo - F(9, 4), 12 * xhi - F(9, 4)
    GA.check("(a): nu^2 interval exactly [1281681/80000, 816347529/50000000]",
             (nl, nh) == (F(1281681, 80000), F(816347529, 50000000)))
    GA.check("(a): window needs principal series nu^2 in [16.02, 16.33], m^2/H^2 = 12 xi in [18.27, 18.58]",
             F("16.02") < nl < nh < F("16.33") and F("18.27") < 12 * xlo < 12 * xhi < F("18.58"))
    GA.check("(a): real weights stay at xi <= 3/16 < window", F(3, 16) < xlo)
    return ok_c


def check_hidden_scale_weight_bound():
    premise("synthesis.kasner-hidden-scale-coupled-scalars-stay-blue")
    premise("synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall")
    premise("synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    c2 = -ricci_scalar((F(1, 3), F(1, 3), F(1, 3)))[F(-2)]
    ok = True
    qbs = []
    for P in [(F(0), F(0), F(0), F(1)), (F(1, 2), F(1, 2), F(1, 2), F(-1, 2))]:
        k = 1 + P[3] / 2                      # Einstein-frame time tau_E ~ T^k (d tau_E = b^(1/2) dT, b = T^P4)
        p = [(x + P[3] / 2) / k for x in P[:3]]
        qb = P[3] / k                         # b ~ tau_E^qb
        qbs.append(qb)
        ok = ok and p == [F(1, 3)] * 3 and sum(p) == 1
        for lam in (F(-1), F(0), F(1), F(3), F(-2)):
            for xi in LISTED:
                w = (lam - 1) * qb
                nu2 = (w * w + 4 * xi * c2) / (4 * (1 - p[0]) ** 2)
                ok = ok and nu2 == (lam - 1) ** 2 / 4 + F(3, 2) * xi
                if abs(lam - 1) <= 2 and xi <= F(1, 2):
                    ok = ok and 4 * nu2 <= 7 and 4 * nu2 < (3 - F(7, 20)) ** 2
    GA.check("Einstein-frame reduction of both ends: (1/3,1/3,1/3) with b ~ tau_E^(2/3), tau_E^(-2/3)",
             ok and qbs == [F(2, 3), F(-2, 3)])
    GA.check("bound attained: lambda = -1, xi = 1/2 gives 4 nu^2 = 7", 4 * (F(4, 4) + F(3, 2) * F(1, 2)) == 7)
    GA.check("control: lambda = 3 (|lambda - 1| = 2) at xi = 1/2 also 4 nu^2 = 7; lambda = -2 exceeds it",
             4 * (F(4, 4) + F(3, 4)) == 7 and 4 * (F(9, 4) + F(3, 4)) == 12)
    lo, hi, xlo, xhi = window()
    nlo, nhi = (3 - hi) / 2, (3 - lo) / 2
    wl, wh = F(2, 3) * (nlo * nlo - 1), F(2, 3) * (nhi * nhi - 1)
    GA.check("Wilson-line weight: window needs xi in [0.8559, 0.8815], exactly [2/3 (nu_lo^2 - 1), 2/3 (nu_hi^2 - 1)]",
             F("0.8559") < wl < wh < F("0.8815") and wl == F(2, 3) * (F(30225, 20000) ** 2 - 1))
    GA.check("Wilson-line window lies above every listed value", wl > max(LISTED))
    return ok
