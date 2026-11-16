"""synthesis.quasi-free-deposit-has-white-energy-noise-unless-pure-and-stationary: exact checks.

One Weyl field on a slice: at momentum p the one-particle space is a minimal left ideal of Cl(3,0), the
one-particle Hamiltonian is left multiplication by the vector p (eigenvalues +-|p|, spectral idempotents
(1 +- p/|p|)/2), a homogeneous gauge-invariant quasi-free state has one-particle density E_p = (nu + mu)/2 with a
scalar nu and a vector mu, and the trace on the ideal of a real element is twice its scalar part.

(1) Zero-momentum noise in Cl(3,0): tr[p E p (1 - E)] = (1/2) p^2 (nu (2 - nu) - mu^2) + |p ^ mu|^2 and
    tr[E (1 - E)] = (1/2)(nu (2 - nu) - mu^2); the three classes (mixed stationary, pure pair, pure stationary).
(2) Overlaps of the filled ball: tr[eps P_+(p) eps P_+(p')] = (r + r')^2 (1 + cos)/8 and
    tr[eps P_-(p) eps P_+(p')] = (r' - r)^2 (1 - cos)/8 with eps = (p + p')/2; then the exact bipolar integrals
    over the lune and over the blocked region: number 3k/4 - k^3/16 (trivial overlap), energy excess
    (k_F^4 k/(8 pi^2)) (1 - kappa^3/30 + kappa^4/96), contrast spectrum (4/g) kappa^4 (1 - kappa^3/30 + kappa^4/96).
(3) Under the conversion zeta = gamma (a_d H_d/k)^2 delta: index 0, the miss in standard deviations, the
    amplitude gamma^2 H_d^2/(6 pi^2 M_P^2) and its values; the thermal crossover relations.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S3 = GA.sig(3, 0)


def vec(x, y, z):
    return {(0,): F(x), (1,): F(y), (2,): F(z)}


def prod(*xs):
    out = GA.sc(F(1))
    for x in xs:
        out = GA.mul(out, x, S3)
    return out


def scalar_part(x):
    return x.get((), F(0))


def tr(x):
    """trace of left multiplication on a minimal left ideal of Cl(3,0), for an element with no pseudoscalar part"""
    assert not x.get((0, 1, 2), F(0))
    return 2 * scalar_part(x)


def dot(a, b):
    return scalar_part(prod(a, b))


def wedge_sq(a, b):
    """|a ^ b|^2 = a^2 b^2 - (a.b)^2, minus the square of the bivector a ^ b"""
    w = GA.scal(F(1, 2), GA.sub(prod(a, b), prod(b, a)))
    return -scalar_part(prod(w, w))


def density(nu, mu):
    return GA.add(GA.sc(F(nu, 2)), GA.scal(F(1, 2), mu))


def complement(E):
    return GA.sub(GA.sc(F(1)), E)


# ---------------------------------------------------------------- exact bipolar integration (units k_F = 1)
def padd(p, q):
    n = max(len(p), len(q))
    out = [F(0)] * n
    for i, c in enumerate(p):
        out[i] += c
    for i, c in enumerate(q):
        out[i] += c
    return out


def pmul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def ppow(p, n):
    out = [F(1)]
    for _ in range(n):
        out = pmul(out, p)
    return out


def pint(p, lo, hi):
    return sum(c * (hi ** (i + 1) - lo ** (i + 1)) / (i + 1) for i, c in enumerate(p))


def inner(poly2, lo, hi):
    """integrate sum c r^i s^j over s from lo(r) to hi(r) (polynomials in r): a polynomial in r"""
    out = [F(0)]
    for (i, j), c in poly2.items():
        t = padd(ppow(hi, j + 1), [-x for x in ppow(lo, j + 1)])
        out = padd(out, [F(0)] * i + [x * c / (j + 1) for x in t])
    return out


def lune(weight, k):
    """int over |p| <= 1 < |p + k| of weight d^3p/(2 pi), 0 < k <= 2; weight is a polynomial in (r1, r2) = (|p|, |p + k|)
    that already contains the factor r1 r2 of d^3p = (2 pi/k) r1 r2 dr1 dr2"""
    k = F(k)
    if k <= 1:
        return pint(inner(weight, [F(1)], [k, F(1)]), 1 - k, F(1)) / k
    return (pint(inner(weight, [k, F(-1)], [k, F(1)]), F(0), k - 1)
            + pint(inner(weight, [F(1)], [k, F(1)]), k - 1, F(1))) / k


def blocked(weight, k):
    """int over |p + k| <= 1 of weight d^3p/(2 pi), 0 < k <= 1; weight a polynomial in (r2, r1) = (|p + k|, |p|)"""
    k = F(k)
    return (pint(inner(weight, [k, F(-1)], [k, F(1)]), F(0), k)
            + pint(inner(weight, [-k, F(1)], [k, F(1)]), k, F(1))) / k


def poly_mul2(p, q):
    out = {}
    for (a, b), c in p.items():
        for (d, e), f in q.items():
            out[(a + d, b + e)] = out.get((a + d, b + e), 0) + c * f
    return out


# ------------------------------------------------------------------------------------------------ the checks
def check_zero_momentum_noise_of_a_weyl_state_in_cl30():
    premise("synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise")
    premise("hawking.imported-quasi-free-states-car-algebra")
    samples = ((vec(2, 3, 6), F(1), vec(F(1, 3), F(-1, 5), F(2, 7))),
               (vec(1, -2, 2), F(4, 5), vec(F(1, 4), F(1, 4), F(-1, 3))),
               (vec(4, 4, 7), F(3, 2), vec(F(-2, 9), F(1, 9), F(1, 3))))
    for p, nu, mu in samples:
        E = density(nu, mu)
        p2, mu2 = dot(p, p), dot(mu, mu)
        mixed = nu * (2 - nu) - mu2
        GA.check("0 <= E <= 1 on the sample: mu^2 <= min(nu, 2 - nu)^2", mu2 <= min(nu, 2 - nu) ** 2)
        GA.check("tr[p E p (1 - E)] = p^2 (nu(2 - nu) - mu^2)/2 + |p ^ mu|^2",
                 tr(prod(p, E, p, complement(E))) == p2 * mixed + wedge_sq(p, mu))
        GA.check("tr[E (1 - E)] = (nu(2 - nu) - mu^2)/2", tr(prod(E, complement(E))) == mixed / 2)
        GA.check("|p ^ mu|^2 = p^2 mu^2 - (p.mu)^2 and both terms are positive on the sample",
                 wedge_sq(p, mu) == p2 * mu2 - dot(p, mu) ** 2 and wedge_sq(p, mu) > 0 and mixed > 0)
    # the three classes at p = (2, 3, 6), |p| = 7
    p = vec(2, 3, 6)
    phat = GA.scal(F(1, 7), p)
    GA.check("|p| = 7", dot(p, p) == 49)
    sea = density(1, phat)                                    # the spectral idempotent (1 + p/|p|)/2
    GA.check("pure and stationary: E idempotent, commutes with p, no energy noise, no momentum noise",
             GA.eq(prod(sea, sea), sea) and GA.commutes(sea, p, S3)
             and tr(prod(p, sea, p, complement(sea))) == 0 and tr(prod(sea, complement(sea))) == 0)
    GA.check("p E = +|p| E on it", GA.eq(prod(p, sea), GA.scal(F(7), sea)))
    for t in (F(1, 2), F(-3, 5)):
        th = density(1, GA.scal(t, phat))                     # stationary, mixed: occupations (1 +- t)/2
        n = (1 + t) / 2
        GA.check("mixed stationary: energy noise p^2 (1 - t^2)/2 = 2 p^2 n (1 - n), momentum weight 2 n (1 - n)",
                 tr(prod(p, th, p, complement(th))) == 2 * 49 * n * (1 - n)
                 and tr(prod(th, complement(th))) == 2 * n * (1 - n) and GA.commutes(th, p, S3))
    for m in (vec(F(3, 7), F(-6, 7), F(2, 7)), vec(F(6, 7), F(2, 7), F(3, 7))):
        pair = density(1, m)                                  # pure, not stationary: a state of pairs
        cos = dot(m, phat)
        n = (1 - cos) / 2                                     # occupation of the negative-energy idempotent's complement
        GA.check("pure pair state: idempotent, energy noise |p ^ m|^2 = 4 p^2 n (1 - n) > 0, no momentum noise",
                 GA.eq(prod(pair, pair), pair) and not GA.commutes(pair, p, S3)
                 and tr(prod(p, pair, p, complement(pair))) == wedge_sq(p, m) == 4 * 49 * n * (1 - n)
                 and wedge_sq(p, m) > 0 and tr(prod(pair, complement(pair))) == 0)
    return True


def check_fermi_ball_overlaps_and_structure_factors():
    premise("synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise")
    # overlaps in Cl(3,0): rational vectors of rational length
    pairs = ((vec(1, 2, 2), 3, vec(2, 3, 6), 7), (vec(4, 4, 7), 9, vec(2, 6, 9), 11), (vec(-1, 4, 8), 9, vec(6, -6, 7), 11))
    for p, r, q, s in pairs:
        up = lambda v, n: density(1, GA.scal(F(1, n), v))
        down = lambda v, n: density(1, GA.scal(F(-1, n), v))
        eps = GA.scal(F(1, 2), GA.add(p, q))
        cos = dot(p, q) / (r * s)
        GA.check("lengths", dot(p, p) == r ** 2 and dot(q, q) == s ** 2)
        GA.check("tr[P_+(p) P_+(q)] = (1 + cos)/2", tr(prod(up(p, r), up(q, s))) == (1 + cos) / 2)
        GA.check("particle to particle: tr[eps P_+(p) eps P_+(q)] = (r + s)^2 (1 + cos)/8",
                 tr(prod(eps, up(p, r), eps, up(q, s))) == F(r + s) ** 2 * (1 + cos) / 8)
        GA.check("sea to particle: tr[eps P_-(p) eps P_+(q)] = (s - r)^2 (1 - cos)/8",
                 tr(prod(eps, down(p, r), eps, up(q, s))) == F(s - r) ** 2 * (1 - cos) / 8)
        GA.check("r s cos = (r^2 + s^2 - k^2)/2 with k = q - p", 2 * dot(p, q) == r ** 2 + s ** 2 - dot(GA.sub(q, p), GA.sub(q, p)))
    # bipolar integrals, k_F = 1; weights as polynomials {(i, j): c} in r1^i r2^j
    ball = F(2, 3)                                            # volume of the unit ball over 2 pi
    for k in (F(1, 10), F(1, 2), F(1), F(3, 2), F(2)):
        GA.check("number structure factor with trivial overlap: 3k/4 - k^3/16 up to k = 2 k_F",
                 lune({(1, 1): F(1)}, k) / ball == F(3, 4) * k - k ** 3 / 16)
    for k in (F(1, 12), F(1, 3), F(2, 3), F(1)):
        # r1 r2 (1 + cos)/2 = (r1 r2 + (r1^2 + r2^2 - k^2)/2)/2 ;  r1 r2 (1 - cos)/2 = (k^2 - (r1 - r2)^2)/4
        half_plus = {(1, 1): F(1, 2), (2, 0): F(1, 4), (0, 2): F(1, 4), (0, 0): -k * k / 4}
        half_minus = {(0, 0): k * k / 4, (2, 0): F(-1, 4), (0, 2): F(-1, 4), (1, 1): F(1, 2)}
        mean_sq = {(2, 0): F(1, 4), (1, 1): F(1, 2), (0, 2): F(1, 4)}       # ((r1 + r2)/2)^2
        diff_sq = {(2, 0): F(1, 4), (1, 1): F(-1, 2), (0, 2): F(1, 4)}      # ((r2 - r1)/2)^2
        ph = lune(poly_mul2(mean_sq, half_plus), k)
        bl = blocked(poly_mul2(diff_sq, half_minus), k)
        GA.check("Weyl number structure factor of the lune: 3k/4 - 5k^3/32",
                 lune(half_plus, k) / ball == F(3, 4) * k - 5 * k ** 3 / 32)
        GA.check("energy, particle-hole part: k/2 - k^5/320", ph == k / 2 - k ** 5 / 320)
        GA.check("energy, blocked pair part: k^4/60 - k^5/120", bl == k ** 4 / 60 - k ** 5 / 120)
        L = ph - bl
        GA.check("energy excess over the vacuum: (k/2)(1 - k^3/30 + k^4/96)", L == k / 2 * (1 - k ** 3 / 30 + k ** 4 / 96))
        # units: S_E = (2 pi k_F^5/(2 pi)^3) L, mean density rho = (2 pi k_F^4/(2 pi)^3)/2 per Weyl field, so
        # P_delta = S_E/rho^2 = 4 (2 pi)^2 L/k_F^3 and Delta^2 = k^3 P/(2 pi^2) = 8 k^3 L
        GA.check("Delta_delta^2 = 4 kappa^4 (1 - kappa^3/30 + kappa^4/96) for one field", 8 * k ** 3 * L == 4 * k ** 4 * (1 - k ** 3 / 30 + k ** 4 / 96))
    GA.check("mean energy density: int_0^1 r^3 dr = 1/4, so 4 pi (1/4)/(2 pi) = 1/2", pint([F(0), F(0), F(0), F(1)], F(0), F(1)) * 2 == F(1, 2))
    GA.check("control: the lune's energy integral does not vanish faster than k", lune(poly_mul2({(2, 0): F(1, 4), (1, 1): F(1, 2), (0, 2): F(1, 4)}, {(1, 1): F(1, 2), (2, 0): F(1, 4), (0, 2): F(1, 4), (0, 0): F(-1, 400)}), F(1, 10)) > F(1, 21))
    return True


def check_index_amplitude_and_thermal_crossover_under_the_conversion():
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    premise("synthesis.imported-string-gas-thermal-spectrum-and-conversion")
    premise("synthesis.imported-large-scale-potential-and-sachs-wolfe-relations")
    premise("synthesis.quadratic-flows-cannot-thermalise-descent")
    premise("synthesis.finite-range-descent-deposit-cannot-seed-cmb")
    # index: Delta_zeta^2 = gamma^2 (aH/k)^4 Delta_delta^2 with Delta_delta^2 ~ k^(3 + s): n_s - 1 = s - 1
    GA.check("linear structure factor (s = 1): index 0; white (s = 0): index -1", (1 - 1, 0 - 1) == (0, -1))
    ns1, sig = F(-351, 10000), F(42, 10000)                  # measured n_s - 1 and its standard deviation
    GA.check("n_s = 1 misses the measured index by between 8.3 and 8.4 standard deviations", F(83, 10) < -ns1 / sig < F(84, 10))
    # amplitude: Delta_zeta^2 = gamma^2 (4/g)(H/k_F)^4, rho = g k_F^4/(8 pi^2) = 3 H^2 M_P^2:
    # (4/g) H^4/k_F^4 = (4/g) H^2 (rho/(3 M_P^2)) (g/(8 pi^2 rho)) = H^2/(6 pi^2 M_P^2) = rho/(18 pi^2 M_P^4)
    GA.check("4/(3 * 8) = 1/6 and gamma = 3/2 gives 3/8, gamma = 9/4 gives 27/32",
             F(4, 3 * 8) == F(1, 6) and F(3, 2) ** 2 / 6 == F(3, 8) and F(9, 4) ** 2 / 6 == F(27, 32))
    # in terms of a temperature label, rho = (pi^2/30) g T^4: Delta^2 = (9/4) g T^4/(540 M_P^4) = (g/240)(T/M_P)^4
    GA.check("(9/4)/(18 * 30) = 1/240", F(9, 4) / (18 * 30) == F(1, 240))
    MP, g, ten = F("2.435e18"), F(10675, 100), F(10)
    AS = F("2.1e-9")
    amp = lambda T: g / 240 * (T / MP) ** 4
    GA.check("at the energy density of the window's ceiling (7.3e8 GeV): between 3.5e-39 and 3.7e-39",
             F(35, 10) * ten ** -39 < amp(F(73, 10) * ten ** 8) < F(37, 10) * ten ** -39)
    GA.check("at 1e12 GeV: between 1.2e-26 and 1.3e-26, more than 1e17 below A_s",
             F(12, 10) * ten ** -26 < amp(ten ** 12) < F(13, 10) * ten ** -26 and amp(ten ** 12) * ten ** 17 < AS)
    GA.check("at the ceiling: more than 5e29 below A_s", amp(F(73, 10) * ten ** 8) * 5 * ten ** 29 < AS)
    # A_s needs rho/M_P^4 = 8 pi^2 A_s: rho^(1/4) between 4.9e16 and 5.0e16 GeV (333/106 < pi < 355/113)
    lo, hi = 8 * F(333, 106) ** 2 * AS, 8 * F(355, 113) ** 2 * AS
    GA.check("rho^(1/4) at A_s between 4.9e16 and 5.0e16 GeV",
             (F(49, 10) * ten ** 16 / MP) ** 4 < lo and hi < (F(50, 10) * ten ** 16 / MP) ** 4)
    # H_d^2 = rho/(3 M_P^2): H_d between 5.6e14 and 5.8e14 GeV
    GA.check("H_d at A_s between 5.6e14 and 5.8e14 GeV",
             (F(56, 10) * ten ** 14 / MP) ** 2 < lo / 3 and hi / 3 < (F(58, 10) * ten ** 14 / MP) ** 2)
    # the ceiling's energy scale rho^(1/4) = (pi^2 g/30)^(1/4) 7.3e8 GeV is below 1.8e9 GeV: a factor above 2.7e7
    GA.check("ceiling energy scale below 1.8e9 GeV", F(355, 113) ** 2 * g / 30 * (F(73, 10) * ten ** 8) ** 4 < (F(18, 10) * ten ** 9) ** 4)
    GA.check("4.9e16/1.8e9 > 2.7e7", F(49, 10) * ten ** 16 > F(27, 10) * ten ** 7 * F(18, 10) * ten ** 9)
    # thermal sea, T << k << k_F: S = c k (1 + e), e = 2 pi^2 T^2/(3 k^2); index = -2e/(1 + e), running = 4e/(1 + e)^2
    t = -ns1
    e = t / (2 - t)
    GA.check("the measured tilt needs e = t/(2 - t)", -2 * e / (1 + e) == ns1)
    GA.check("running at the measured tilt: t (2 - t) = 0.06896799", 4 * e / (1 + e) ** 2 == t * (2 - t) == F(6896799, 10 ** 8))
    # k/T there: (k/T)^2 = 2 pi^2/(3 e), between 19.1 and 19.3
    GA.check("the tilt is reached at k/T between 19.1 and 19.3",
             F(191, 10) ** 2 < 2 * F(333, 106) ** 2 / (3 * e) and 2 * F(355, 113) ** 2 / (3 * e) < F(193, 10) ** 2)
    # n(e)(1 - n(e + D)) = [n(e) - n(e + D)]/(1 - exp(-D/T)): with y = exp(e/T), d = exp(D/T) rational samples
    y = GA.RF.var()
    one = GA.RF.const(1)
    for d in (F(2), F(3, 5), F(7, 4)):
        n1, n2 = one / (y + one), one / (GA.RF.const(d) * y + one)
        GA.check("pair-occupation identity", (n1 * (one - n2)).eqrf((n1 - n2) * GA.RF.const(1 / (1 - 1 / d))))
    # the two-term model S = S(0) + c k (white plus linear): index -f, running f (1 - f)
    GA.check("two-term model: running 0.03386799 at the measured tilt", t * (1 - t) == F(3386799, 10 ** 8))
    # white end: S(0)/slope = 4 T for a degenerate sea (Var = 4 rho T, slope rho): white below k = 4 T
    GA.check("zeta(2) coefficient: 2 * (1/4) * (pi^2/6) = pi^2/12, and 2 * 4 * (1/12) = 2/3", 2 * F(1, 4) * F(1, 6) == F(1, 12) and 2 * 4 * F(1, 12) == F(2, 3))
    return True
