"""one-relation.imported-condensate-derived-content: exact checks.

Computable part: the mass-weight dictionary at Klein-Gordon level, m^2 = -w(w+3) Lambda/3, on the de Sitter
field written on flat spacetime. Conventions of the cited dictionary and frozen-point results: eta =
diag(1, -1, -1, -1), Q(x) = eta(x, x), sigma = 1 - Lambda Q/12, g = sigma^-2 eta; tractors in the flat scale
are sigma n_inf + mu + rho n0 with <n_inf, n0> = 1, and I = (sigma, grad sigma, -(1/4) box sigma).
The Thomas D-operator on a density f of weight w in the flat scale (J = 0, n = 4) is
D f = ((2w + 2) w f, (2w + 2) grad f, -box f).
(1) I = (1 - Lambda Q/12, -(Lambda/6) x_a, Lambda/6) and <I, I> = Lambda/3 identically.
(2) For phi any monomial of degree <= 2 in (t, x1, x2, x3) (this determines a second-order operator), six
    integer weights w = -3..2 and two values of Lambda, the identity
        I . D(sigma^w phi) = -sigma^(w-1) (box_g phi + m^2 phi),   m^2 = -w(w+3) Lambda/3,
    holds exactly, with box_g phi = |g|^(-1/2) d_a(|g|^(1/2) g^ab d_b phi) computed from g = sigma^-2 eta. Both
    sides are polynomial of degree two in w after dividing by sigma^(w-1), so six weights give it for every w;
    hence I . D sigma = 0 is (box_g + m^2) phi = 0 in the scale of I. Controls: m^2 replaced by
    +w(w+3) Lambda/3 fails for w = -1, and m^2 = 0 at w = 0 and w = -3.
The observation-level readings (condensation, democracy of the alignment, minimal coupling) and the join
identity's interpretation have no finite content of their own and are not checked.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement

import GA  # noqa: F401
from tp_premise import premise

ETA = (1, -1, -1, -1)
LAMBDAS = [F(3, 5), F(-2)]
WEIGHTS = [-3, -2, -1, 0, 1, 2]


# polynomials in x0..x3: {exponent tuple: Fraction}; "sigma-polynomials": {k: poly} meaning sum poly * sigma^k
def padd(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c != 0}


def pscal(s, p):
    return {e: s * c for e, c in p.items() if s * c != 0}


def pmul(p, q):
    out = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            e = tuple(a + b for a, b in zip(e1, e2))
            out[e] = out.get(e, F(0)) + c1 * c2
    return {e: c for e, c in out.items() if c != 0}


def pder(a, p):
    out = {}
    for e, c in p.items():
        if e[a]:
            ne = tuple(x - (1 if i == a else 0) for i, x in enumerate(e))
            out[ne] = out.get(ne, F(0)) + c * e[a]
    return {e: c for e, c in out.items() if c != 0}


def mono(*e):
    return {tuple(e): F(1)}


ONE = mono(0, 0, 0, 0)
XS = [mono(*[1 if i == a else 0 for i in range(4)]) for a in range(4)]
QPOLY = padd(*[pscal(F(ETA[a]), pmul(XS[a], XS[a])) for a in range(4)])


def sigma_poly(L):
    return padd(ONE, pscal(-L / 12, QPOLY))


def s_add(*ss):
    out = {}
    for s in ss:
        for k, p in s.items():
            out[k] = padd(out.get(k, {}), p)
    return {k: p for k, p in out.items() if p}


def s_scal(c, s):
    return {k: pscal(c, p) for k, p in s.items() if pscal(c, p)}


def s_mulp(p, s):
    return {k: pmul(p, q) for k, q in s.items() if pmul(p, q)}


def s_shift(j, s):
    return {k + j: p for k, p in s.items()}


def s_der(a, s, L):
    dsig = pder(a, sigma_poly(L))
    out = {}
    for k, p in s.items():
        out = s_add(out, {k: pder(a, p)})
        if k:
            out = s_add(out, {k - 1: pscal(F(k), pmul(dsig, p))})
    return out


def s_expand(s, L):
    """Multiply by sigma^K (K large enough) and expand to a polynomial in x."""
    K = -min(s) if s and min(s) < 0 else 0
    sig = sigma_poly(L)
    out = {}
    for k, p in s.items():
        q = p
        for _ in range(k + K):
            q = pmul(q, sig)
        out = padd(out, q)
    return out


def box_flat(s, L):
    return s_add(*[s_scal(F(ETA[a]), s_der(a, s_der(a, s, L), L)) for a in range(4)])


def box_g(phi, L):
    """|g|^(-1/2) d_a(|g|^(1/2) g^aa d_a phi), g = sigma^-2 eta: |g|^(1/2) = sigma^-4, g^aa = sigma^2 eta^aa."""
    terms = []
    for a in range(4):
        inner = s_shift(-4 + 2, s_scal(F(ETA[a]), s_der(a, {0: phi}, L)))
        terms.append(s_der(a, inner, L))
    return s_shift(4, s_add(*terms))


def frozen_point(L):
    sig = sigma_poly(L)
    mu = [pder(a, sig) for a in range(4)]                       # grad_a sigma (lower index)
    rho = pscal(F(-1, 4), padd(*[pscal(F(ETA[a]), pder(a, pder(a, sig))) for a in range(4)]))
    return sig, mu, rho


def check_frozen_point_components_and_norm():
    premise("mass.de-sitter-scale-frozen-point")
    ok = True
    for L in LAMBDAS:
        sig, mu, rho = frozen_point(L)
        ok = ok and rho == {(0, 0, 0, 0): L / 6}
        ok = ok and all(mu[a] == pscal(-L / 6 * ETA[a], XS[a]) for a in range(4))
        # <I, I> = 2 sigma rho + eta^ab mu_a mu_b
        norm = padd(pscal(F(2), pmul(sig, rho)), *[pscal(F(ETA[a]), pmul(mu[a], mu[a])) for a in range(4)])
        ok = ok and norm == {(0, 0, 0, 0): L / 3}
    _tp_rv = (ok); assert _tp_rv is not False, "check_frozen_point_components_and_norm"; return _tp_rv


def i_dot_d(w, phi, L):
    """I . D f for f = sigma^w phi."""
    sig, mu, rho = frozen_point(L)
    f = {w: phi}
    top = s_scal(F((2 * w + 2) * w), f)
    mid = [s_scal(F(2 * w + 2), s_der(a, f, L)) for a in range(4)]
    bottom = s_scal(F(-1), box_flat(f, L))
    terms = [s_mulp(sig, bottom), s_mulp(rho, top)]
    terms += [s_mulp(pscal(F(ETA[a]), mu[a]), mid[a]) for a in range(4)]
    return s_add(*terms)


def test_functions():
    out = [ONE] + XS
    for a, b in combinations_with_replacement(range(4), 2):
        out.append(pmul(XS[a], XS[b]))
    return out


def check_klein_gordon_mass_is_minus_w_w_plus_3_lambda_over_3():
    premise("mass.mass-weight-dictionary")
    premise("mass.de-sitter-scale-frozen-point")
    ok = True
    tests = test_functions()
    ok = ok and len(tests) == 15
    for L in LAMBDAS:
        for w in WEIGHTS:
            m2 = -w * (w + 3) * L / 3
            for phi in tests:
                lhs = i_dot_d(w, phi, L)
                rhs = s_shift(w - 1, s_scal(F(-1), s_add(box_g(phi, L), {0: pscal(m2, phi)})))
                ok = ok and s_expand(s_add(lhs, s_scal(F(-1), rhs)), L) == {}
    # controls: the opposite sign fails at w = -1; the massless weights are 0 and -3
    L = LAMBDAS[0]
    phi = pmul(XS[0], XS[1])
    wrong = s_shift(-2, s_scal(F(-1), s_add(box_g(phi, L), {0: pscal(2 * L / 3 * -1, phi)})))
    ok = ok and s_expand(s_add(i_dot_d(-1, phi, L), s_scal(F(-1), wrong)), L) != {}
    ok = ok and [w for w in WEIGHTS if w * (w + 3) == 0] == [-3, 0]
    _tp_rv = (ok); assert _tp_rv is not False, "check_klein_gordon_mass_is_minus_w_w_plus_3_lambda_over_3"; return _tp_rv
