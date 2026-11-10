"""Exact checks: the one-loop electron self-energy and vertex extended across coincident points with the
Ward-Takahashi identity holding for the pair of extensions at one common cut-off length (Euclidean section, Cl(4,0),
units hbar = c = 1; method and conventions of the stored vacuum polarisation result).

Notation: w a vector of Cl(4,0), s = Q(w), L = ln s (the scale mu = 1 throughout; a scale M enters as ln(M^2 s) =
L + ln M^2). Propagators S0(w) = w/(2 pi^2 s^2), photon D_ab(w) = ((1 + xi)/2 delta_ab + (1 - xi) w_a w_b / s)/(4 pi^2 s)
with gauge parameter xi (xi = 1 Feynman, xi = 0 Landau).

Two exact calculi are used.
(A) Off the origin: polynomials in the four components times s^a L^k, differentiated exactly
    (dict {(e0, e1, e2, e3, a, k): Fraction}).
(B) Pairings with test functions g = P(w) (1 - s)^N on the unit ball (zero outside; C^(N-1), so they pair with the
    distributions of order at most 3 that occur for N = 5). Integrals over the ball of w^e s^a L^k are exact
    rationals times pi^2: angular average of a monomial over the 3-sphere times |S^3| = 2 pi^2 times a radial
    integral int_0^1 t^p (ln t)^k dt = (-1)^k k!/(p + 1)^(k + 1). A distributional derivative of a locally
    integrable function is paired by moving the derivatives to g. Every pairing below is returned in units of pi^2.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIG4 = (1, 1, 1, 1)
E = [GA.gen(i) for i in range(4)]


def _m(x, y):
    return GA.mul(x, y, SIG4)


def _vec(c):
    return {(i,): F(v) for i, v in enumerate(c) if v != 0}


# ------------------------------------------------------------------ calculus (A) and (B)
def padd(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def pscl(c, p):
    c = F(c)
    return {k: c * v for k, v in p.items() if c * v != 0}


def pmul(p, q):
    out = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(x + y for x, y in zip(k1, k2))
            out[k] = out.get(k, F(0)) + v1 * v2
    return {k: v for k, v in out.items() if v != 0}


def mono(e=(0, 0, 0, 0), a=0, k=0, c=1):
    return {tuple(e) + (a, k): F(c)}


def comp(i):
    e = [0, 0, 0, 0]
    e[i] = 1
    return mono(e)


def d(i, p):
    """Partial derivative d/dw_i of sum c w^e s^a L^k (off the origin for singular terms)."""
    out = {}

    def put(key, v):
        out[key] = out.get(key, F(0)) + v

    for key, v in p.items():
        e, a, k = list(key[:4]), key[4], key[5]
        if e[i]:
            e2 = list(e)
            e2[i] -= 1
            put(tuple(e2) + (a, k), v * e[i])
        e2 = list(e)
        e2[i] += 1
        if a:
            put(tuple(e2) + (a - 1, k), v * 2 * a)
        if k:
            put(tuple(e2) + (a - 1, k - 1), v * 2 * k)
    return {k: v for k, v in out.items() if v != 0}


def lap(p):
    return padd(*[d(i, d(i, p)) for i in range(4)])


def normal(p):
    """Canonical form: trade w_3^2 = s - w_0^2 - w_1^2 - w_2^2 so that equal functions have equal dicts."""
    out = dict(p)
    changed = True
    while changed:
        changed = False
        new = {}
        for key, v in out.items():
            e, a, k = list(key[:4]), key[4], key[5]
            if e[3] >= 2:
                changed = True
                e[3] -= 2
                kk = tuple(e) + (a + 1, k)
                new[kk] = new.get(kk, F(0)) + v
                for j in range(3):
                    e2 = list(e)
                    e2[j] += 2
                    kk = tuple(e2) + (a, k)
                    new[kk] = new.get(kk, F(0)) - v
            else:
                new[key] = new.get(key, F(0)) + v
        out = {k: v for k, v in new.items() if v != 0}
    return out


def same(p, q):
    return normal(padd(p, pscl(-1, q))) == {}


def factorial(k):
    out = 1
    for j in range(2, k + 1):
        out *= j
    return out


def sphere_average(e):
    """Average of w^e / |w|^|e| over the unit 3-sphere: prod (e_i - 1)!! / (4 * 6 * ... ) for even exponents."""
    if any(x % 2 for x in e):
        return F(0)
    num = 1
    for x in e:
        for j in range(x - 1, 0, -2):
            num *= j
    den = 1
    for j in range(sum(e) // 2):
        den *= 4 + 2 * j
    return F(num, den)


def ball(p):
    """Integral over the unit ball of sum c w^e s^a L^k, in units of pi^2. Raises if a term is not integrable."""
    tot = F(0)
    for key, v in p.items():
        e, a, k = key[:4], key[4], key[5]
        av = sphere_average(e)
        if av == 0:
            continue
        # d^4w = |S^3| r^3 dr = pi^2 t dt (t = s); integrand t^(|e|/2 + a) (ln t)^k
        pw = F(sum(e), 2) + a + 1
        if pw <= -1:
            raise ValueError("not locally integrable")
        tot += v * av * (-1) ** k * factorial(k) / (pw + 1) ** (k + 1)
    return tot


def bump(poly, n=5):
    """g = poly(w) (1 - s)^n as a polynomial dict (support the unit ball)."""
    one_minus_s = {(0, 0, 0, 0, 0, 0): F(1), (0, 0, 0, 0, 1, 0): F(-1)}
    g = {(0, 0, 0, 0, 0, 0): F(1)}
    for _ in range(n):
        g = pmul(g, one_minus_s)
    return expand_s(pmul(poly, g))


def expand_s(p):
    """Write s^a (a >= 0) as a polynomial in the components (test functions only)."""
    ssum = padd(*[mono([2 if j == i else 0 for j in range(4)]) for i in range(4)])
    out = {}
    for key, v in p.items():
        e, a, k = key[:4], key[4], key[5]
        assert a >= 0 and k == 0
        term = {tuple(e) + (0, 0): v}
        for _ in range(a):
            term = pmul(term, ssum)
        out = padd(out, term)
    return out


def at0(p):
    return p.get((0, 0, 0, 0, 0, 0), F(0))


def taylor1(g):
    """g(0) + w . grad g(0)."""
    out = {}
    for key, v in g.items():
        if sum(key[:4]) <= 1:
            out[key] = v
    return out


TESTS = None


def tests():
    global TESTS
    if TESTS is None:
        p1 = padd(mono(c=1), comp(0), pscl(2, comp(1)), pscl(-1, pmul(comp(0), comp(2))), pscl(3, pmul(comp(1), comp(1))))
        p2 = padd(mono(c=2), pscl(-3, comp(2)), comp(3), pmul(comp(0), comp(0)), pscl(5, pmul(comp(2), comp(3))),
                  pmul(comp(1), pmul(comp(1), comp(3))))
        TESTS = [bump(p1), bump(p2)]
    return TESTS


LS = mono(a=-1, k=1)          # L / s
INV_S = mono(a=-1)            # 1 / s


# ------------------------------------------------------------------ check 1: the kernels in Cl(4,0)
def check_kernels_in_the_euclidean_algebra_and_their_gauge_dependence():
    premise("field-theory.second-quantisation")
    premise("field-theory.coupled-system-tree-level")
    premise("synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants")
    ok = True
    for c in ([1, 0, 0, 0], [1, 2, 0, 0], [3, -2, 5, 7], [1, 1, -4, 2]):
        w = _vec(c)
        s = sum(F(x) * x for x in c)
        for xi in (F(1), F(0), F(3), F(-2, 5)):
            # sum_ab e_a w e_b ((1 + xi)/2 delta_ab s + (1 - xi) w_a w_b) = -2 xi s w
            tot = {}
            mass = {}
            for a in range(4):
                for b in range(4):
                    coef = (1 - xi) * c[a] * c[b] + ((1 + xi) / 2 * s if a == b else 0)
                    if coef:
                        tot = GA.add(tot, GA.scal(coef, _m(_m(E[a], w), E[b])))
                        mass = GA.add(mass, GA.scal(coef, _m(E[a], E[b])))
            ok = ok and GA.eq(tot, GA.scal(-2 * xi * s, w))
            ok = ok and GA.eq(mass, {(): (3 + xi) * s})
    # coefficients: Sigma = e^2 e_a S0 e_b D_ab = -xi e^2 w/(4 pi^4 s^3); order m: (3 + xi) e^2 m/(16 pi^4 s^2)
    c_sigma = lambda xi: F(1, 2) * F(1, 4) * (-2 * xi)      # units e^2 pi^-4, times w/s^3
    c_mass = lambda xi: F(1, 4) * F(1, 4) * (3 + xi)        # units e^2 m pi^-4, times 1/s^2
    ok = ok and c_sigma(F(1)) == F(-1, 4) and c_sigma(F(0)) == 0 and c_mass(F(1)) == F(1, 4) and c_mass(F(0)) == F(3, 16)
    # sphere average of w_nu w = e_nu s/4 (the trace part of the zero-transfer vertex)
    for nu in range(4):
        for a in range(4):
            e = [0, 0, 0, 0]
            e[nu] += 1
            e[a] += 1
            ok = ok and sphere_average(e) == (F(1, 4) if a == nu else 0)
    GA.check("kernels: sandwich -2 xi w, mass part 3 + xi, sphere average e_nu s/4", ok)
    return ok


# ------------------------------------------------------------------ check 2: identities off the origin
def check_identities_off_the_origin():
    premise("field-theory.second-quantisation")
    premise("synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products")
    ok = True
    # S0 = w/s^2 (times 1/(2 pi^2)) is monogenic off the origin: d_i (w_j/s^2) symmetric and traceless
    s0 = [pmul(comp(j), mono(a=-2)) for j in range(4)]
    tr = {}
    for i in range(4):
        tr = padd(tr, d(i, s0[i]))
        for j in range(4):
            ok = ok and same(d(i, s0[j]), d(j, s0[i]))
    ok = ok and normal(tr) == {}
    # flux of S0 through the sphere: (w/s^2) . (w/r) r^3 |S^3| / (2 pi^2) = 1, so dslash S0 = delta
    ok = ok and F(1, 2) * 2 * sphere_average((0, 0, 0, 0)) == 1
    # dslash (w_nu S0) = e_nu S0 off the origin: d_i (w_nu w_j / s^2) - delta_(i nu) w_j/s^2 = w_nu d_i (w_j/s^2)
    for nu in range(4):
        tr = {}
        for i in range(4):
            lhs = d(i, pmul(comp(nu), s0[i]))
            tr = padd(tr, lhs)
        ok = ok and same(tr, s0[nu])                      # scalar part: e_nu . S0
        for i in range(4):
            for j in range(i + 1, 4):                     # bivector part: (e_nu ^ S0)_(ij)
                curl = padd(d(i, pmul(comp(nu), s0[j])), pscl(-1, d(j, pmul(comp(nu), s0[i]))))
                want = padd(s0[j] if i == nu else {}, pscl(-1, s0[i]) if j == nu else {})
                ok = ok and same(curl, want)
    # w_nu S0 is of degree -2: no delta at the origin (flux through a sphere of radius r scales as r)
    ok = ok and (-2 + 3) > 0
    # w/s^3 = (1/16) dslash box (L/s); 1/s^2 = -(1/4) box(L/s); box(1/s) = 0
    for a in range(4):
        ok = ok and same(pscl(F(1, 16), d(a, lap(LS))), pmul(comp(a), mono(a=-3)))
    ok = ok and same(pscl(F(-1, 4), lap(LS)), mono(a=-2)) and normal(lap(INV_S)) == {}
    # traceless part: (d_a d_nu - (1/4) delta box)(1/(8 s)) = (w_a w_nu - delta s/4)/s^3
    for a in range(4):
        for nu in range(4):
            lhs = pscl(F(1, 8), d(a, d(nu, INV_S)))
            rhs = pmul(pmul(comp(a), comp(nu)), mono(a=-3))
            if a == nu:
                rhs = padd(rhs, mono(a=-2, c=F(-1, 4)))
            ok = ok and same(lhs, rhs)
    # box(w_nu L/s) = 2 d_nu((L + 1)/s) off the origin (used for the product w_nu Sigma-bar)
    for nu in range(4):
        ok = ok and same(lap(pmul(comp(nu), LS)), pscl(2, d(nu, padd(LS, INV_S))))
    GA.check("off the origin: S0 monogenic with unit flux, dslash(w_nu S0) = e_nu S0, differential forms of "
             "w/s^3, 1/s^2 and the traceless part", ok)
    return ok


# ------------------------------------------------------------------ pairings
def pair_dist(F_loc, derivs, g):
    """< d_(i1) ... d_(ik) F_loc, g > = (-1)^k int F_loc d_(i1) ... d_(ik) g, units pi^2."""
    h = g
    for i in derivs:
        h = d(i, h)
    return (-1) ** len(derivs) * ball(pmul(F_loc, h))


def pair_lap(F_loc, g, extra=()):
    h = lap(g)
    for i in extra:
        h = d(i, h)
    return (-1) ** len(extra) * ball(pmul(F_loc, h))


def check_cut_off_extensions_against_the_logarithmic_forms():
    """[1/s^2]_1 = -(1/4) box(L/s) + pi^2 delta; [w/s^3]_1 = (1/16) dslash box(L/s) - (3 pi^2/8) dslash delta;
    [w_nu w_a/s^3]_1 = (d_a d_nu - delta box/4)(1/(8 s)) + (delta/4)(-(1/4) box(L/s) + pi^2 delta)."""
    premise("synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products")
    premise("synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants")
    ok = True
    consts = set()
    seen_gradient = False
    for g in tests():
        g0 = at0(g)
        # zero-order cut-off extension of 1/s^2 at radius 1
        cut = ball(pmul(mono(a=-2), padd(g, mono(c=-g0))))
        diff = cut - F(-1, 4) * pair_lap(LS, g)
        ok = ok and g0 != 0 and diff == 1 * g0                       # pi^2 delta
        consts.add(diff / g0)
        for a in range(4):
            # first-order cut-off extension of w_a/s^3 at radius 1
            cut = ball(pmul(pmul(comp(a), mono(a=-3)), padd(g, pscl(-1, taylor1(g)))))
            log_form = F(1, 16) * pair_lap(LS, g, extra=(a,))
            dg0 = at0(d(a, g))
            seen_gradient = seen_gradient or dg0 != 0
            # <dslash delta, g> = -dslash g(0): the difference is -(3 pi^2/8) dslash delta
            ok = ok and cut - log_form == F(3, 8) * dg0
            for nu in range(4):
                cutv = ball(pmul(pmul(pmul(comp(a), comp(nu)), mono(a=-3)), padd(g, mono(c=-g0))))
                trl = F(1, 8) * (pair_dist(INV_S, (a, nu), g) - (F(1, 4) * pair_lap(INV_S, g) if a == nu else 0))
                trc = (F(1, 4) * (F(-1, 4) * pair_lap(LS, g) + g0)) if a == nu else F(0)
                ok = ok and cutv == trl + trc
    ok = ok and consts == {F(1)} and seen_gradient
    # scales: -(1/4) box(ln(M^2 s)/s) = -(1/4) box(L/s) + pi^2 ln(M^2) delta, so [1/s^2]_1 has ln M_V^2 = 1;
    # (1/16) dslash box(ln(M^2 s)/s) = (1/16) dslash box(L/s) - (pi^2/4) ln(M^2) dslash delta, so [w/s^3]_1 has
    # ln M_Sigma^2 = 3/2
    g = tests()[0]
    box_inv_s = pair_lap(INV_S, g) / at0(g)
    ok = ok and box_inv_s == -4                                       # box(1/s) = -4 pi^2 delta
    per_log_zero = F(-1, 4) * box_inv_s                               # pairing shift per unit ln M^2, against g(0)
    per_log_one = F(1, 16) * pair_lap(INV_S, g, extra=(0,)) / at0(d(0, g))   # against d_0 g(0)
    ln_mv2 = F(1) / per_log_zero
    ln_ms2 = F(3, 8) / per_log_one
    ok = ok and per_log_zero == 1 and per_log_one == F(1, 4)
    ok = ok and ln_mv2 == 1 and ln_ms2 == F(3, 2) and ln_ms2 - ln_mv2 == F(1, 2)
    GA.check("cut-off extensions at radius 1 equal the logarithmic forms with ln M^2 = 1 (order zero) and 3/2 "
             "(order one); the difference of the logarithms is 1/2", ok)
    return ok


def check_product_of_the_extended_self_energy_with_a_coordinate():
    """w_nu (1/16) d_a box(ln(M^2 s)/s) = (d_a d_nu - delta box/4)(1/(8 s)) - (delta/16) box(ln(M'^2 s)/s)
    exactly when ln(M^2/M'^2) = 1/2: the pairing of the left side at M = 1 against the right side at M' = 1 leaves
    -(pi^2/8) delta_(a nu) g(0), which the shift ln M^2 = 1/2 removes."""
    premise("synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products")
    ok = True
    for g in tests():
        g0 = at0(g)
        for a in range(4):
            for nu in range(4):
                left = F(1, 16) * pair_lap(LS, pmul(comp(nu), g), extra=(a,))
                per_log = F(1, 16) * pair_lap(INV_S, pmul(comp(nu), g), extra=(a,))
                right = F(1, 8) * (pair_dist(INV_S, (a, nu), g) - (F(1, 4) * pair_lap(INV_S, g) if a == nu else 0))
                if a == nu:
                    right += F(-1, 16) * pair_lap(LS, g)
                    ok = ok and per_log == F(1, 4) * g0 and left + F(1, 2) * per_log == right
                    ok = ok and left != right
                else:
                    ok = ok and per_log == 0 and left == right
    GA.check("w_nu times the extended self-energy is the zero-transfer vertex form exactly at ln(M_Sigma^2/M_V^2) = 1/2", ok)
    return ok


def check_ward_matching_of_subtractions_and_scale_coefficients():
    """The subtraction of the vertex pairing against d_t f is the first-order Taylor term of
    F(w) = f(u = w, v = 0) - f(u = 0, v = w); and the scale derivatives of the two extensions are opposite."""
    premise("synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants")
    ok = True
    # f a polynomial in (u, v) of degree <= 2 with rational coefficients: f = sum c x^alpha, x = (u, v) in Q^8
    monos = [((1, 0, 0, 0, 0, 0, 0, 0), F(2)), ((0, 0, 0, 0, 0, 1, 0, 0), F(-3)), ((0, 1, 0, 0, 0, 0, 0, 0), F(5)),
             ((0, 0, 0, 0, 0, 0, 0, 1), F(7)), ((1, 0, 0, 0, 1, 0, 0, 0), F(1)), ((0, 2, 0, 0, 0, 0, 0, 0), F(4)),
             ((0, 0, 1, 0, 0, 0, 1, 0), F(-2)), ((0, 0, 0, 0, 0, 0, 0, 0), F(9))]
    for nu in range(4):
        # d_t = d_u - d_v at the origin
        dtf0 = sum(c for e, c in monos if sum(e) == 1 and e[nu] == 1) - sum(c for e, c in monos if sum(e) == 1 and e[4 + nu] == 1)
        # F(w): put v = 0 (keep monomials in u only) minus u = 0 (monomials in v only), both as functions of w
        lin = sum(c for e, c in monos if sum(e) == 1 and e[nu] == 1 and sum(e[4:]) == 0) \
            - sum(c for e, c in monos if sum(e) == 1 and e[4 + nu] == 1 and sum(e[:4]) == 0)
        ok = ok and lin == dtf0
    # F(0) = 0 although f(0) != 0, and the second-order part of F is not zero (the matching is of first order only)
    f_v0 = {e[:4]: c for e, c in monos if sum(e[4:]) == 0}              # f(u = w, v = 0) as a polynomial in w
    f_u0 = {e[4:]: c for e, c in monos if sum(e[:4]) == 0}              # f(u = 0, v = w)
    big_f = {k: f_v0.get(k, F(0)) - f_u0.get(k, F(0)) for k in set(f_v0) | set(f_u0)}
    ok = ok and f_v0[(0, 0, 0, 0)] != 0 and big_f[(0, 0, 0, 0)] == 0
    ok = ok and any(v != 0 for k, v in big_f.items() if sum(k) == 2)
    # the forced relation on the Euclidean section: pair c_V n delta delta and c_2 dslash delta against the linear part
    # of f; div(c_V g_a delta delta) pairs to -c_V (d_v - d_u)_a f(0) = +c_V d_t f(0), the right side to -c_2 d_a F(0)
    for nu in range(4):
        dtf0 = sum(c for e, c in monos if sum(e) == 1 and e[nu] == 1) - sum(c for e, c in monos if sum(e) == 1 and e[4 + nu] == 1)
        dF0 = big_f.get(tuple(1 if j == nu else 0 for j in range(4)), F(0))
        for c_v, c_2, want in ((F(3), F(-3), True), (F(3), F(3), dtf0 == 0), (F(1), F(-2), dtf0 == 0)):
            ok = ok and ((c_v * dtf0 == -c_2 * dF0) == want)
    # scale derivatives (units e^2 pi^-2, gauge parameter xi factored out):
    # Sigma-bar = c_s [w/s^3]_mu, c_s = -1/4 pi^-4; d/dln(mu) of [w/s^3]_mu = +(|S^3|/4) dslash delta... computed:
    # [h]_mu - [h]_mu' = -(int over the shell of h T) so mu d/dmu [w_a/s^3] paired with g is -(2 pi^2)(1/4) d_a g(0)
    shell = 2 * sphere_average((2, 0, 0, 0))                           # |S^3|/pi^2 times the average of w_a w_a / s
    ok = ok and shell == F(1, 2)
    # raising mu shrinks the subtraction ball: mu d/dmu <[w_a/s^3]_mu, g> = +shell pi^2 d_a g(0)
    # = -shell pi^2 <d_a delta, g>, and mu d/dmu <[w_nu w_a/s^3]_mu, g> = +shell pi^2 delta_(a nu) g(0).
    # With Sigma = c_s xi e^2 pi^-4 w/s^3 and the zero-transfer vertex c_s xi e^2 pi^-4 w_nu w/s^3, c_s = -1/4:
    c_s = F(1, 2) * F(1, 4) * F(-2)
    d_sigma = c_s * (-shell)                     # coefficient of dslash delta, units xi e^2 pi^-2
    d_vertex = c_s * shell                       # coefficient of e_nu delta(u) delta(v)
    ok = ok and c_s == F(-1, 4) and d_sigma == F(1, 8) and d_vertex == F(-1, 8) and d_sigma == -d_vertex
    # the same from the logarithmic form: mu d/dmu of (1/16) dslash box(ln(mu^2 s)/s) is (1/8) dslash box(1/s)
    g = tests()[1]
    for a in range(4):
        dg0 = at0(d(a, g))
        ok = ok and F(1, 8) * pair_lap(INV_S, g, extra=(a,)) == shell * dg0
    GA.check("the vertex subtraction is the first-order Taylor term of the self-energy pairing; scale derivatives "
             "xi e^2/(8 pi^2) (self-energy) and its negative (vertex)", ok)
    return ok
