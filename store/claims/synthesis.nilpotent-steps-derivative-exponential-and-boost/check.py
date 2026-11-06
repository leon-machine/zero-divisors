"""synthesis.nilpotent-steps-derivative-exponential-and-boost: exact checks (nilpotent steps).

(1) Cl(0,0,1): f(x + rho) = f(x) + f'(x) rho for f = (x^3 + 3x)/(x^2 + 1), against hand-stated
    values.
(2) Through a generalised inverse: a radical vector rho of Cl(p,q,r) has rho x rho = 0 for every
    blade x (no generalised inverse); in Cl(1,1) the null vector a = (e+ + e-)/2 has the partner
    a' with a a' a = a, and for f = 2x^3 + 5x and (x^3 + 3x)/(x^2 + 1),
    g (f(x + a) - f(x)) = f'(x) g a with g a idempotent, for the partner and for another
    generalised inverse; only the partner's idempotent is self-adjoint for the adjoint exchanging
    a and a'.
(3) N commuting square-zero steps b_i: prod (1 + b_i) = exp(eps), eps^k = k! e_k(b),
    eps^(N+1) = 0; b_i = rho_{2i-1} rho_{2i} in Cl(0,0,2N) (N = 2..6), disjoint pairs of six
    orthogonal null vectors in Cl(6,6) (N = 3), and Jordan-Wigner steps
    b_i = v_i pi_1 ... pi_{i-1}, pi_j = v_j w_j - w_j v_j, in Cl(N,N) (N = 2, 3), with nonzero product.
(4) The boost over R[d]/(d^2): in Cl(1,1,2) with d = s rho1 rho2, B = e_t e_r, l_+/- = e_t +/- e_r,
    (1 + d B / 2) l_+/- (1 - d B / 2) = (1 -/+ d) l_+/-, while conjugation with the reversion of
    Cl(1,1,2) (which fixes the grade-4 element d B) fixes l_+; an even R = alpha + beta B with scalar
    alpha, beta gives R l_+ R~ = (alpha - beta)^2 l_+; R^2 = 5/4 + 3/4 B halves l_+ and doubles l_-.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

S11 = GA.sig(1, 1)
ONE = GA.sc(1)
A = GA.scal(F(1, 2), GA.add(GA.gen(0), GA.gen(1)))
AP = GA.scal(F(1, 2), GA.sub(GA.gen(0), GA.gen(1)))


def m11(x, y):
    return GA.mul(x, y, S11)


def poly_at(coeffs, x, n, S):
    """f(x + n) for f = sum coeffs[k] t^k, x a scalar, n in the algebra."""
    base = GA.add(GA.sc(x), n)
    out, pw = {}, GA.sc(1)
    for c in coeffs:
        out = GA.add(out, GA.scal(c, pw))
        pw = GA.mul(pw, base, S)
    return out


def ratfun_at(num, den, x, n, S):
    """num(x + n) / den(x + n) for a square-zero n commuting with scalars."""
    h = poly_at(den, x, n, S)
    h0 = h.get((), F(0))
    h1 = GA.sub(h, GA.sc(h0))                    # h'(x) n
    hinv = GA.sub(GA.sc(1 / h0), GA.scal(1 / (h0 * h0), h1))
    assert GA.eq(GA.mul(h, hinv, S), GA.sc(1))
    return GA.mul(poly_at(num, x, n, S), hinv, S)


def adjoint(x):
    """Reversion composed with e_- -> -e_- in Cl(1,1): exchanges a and a'."""
    return GA.reverse({b: (c if (1 not in b) else -c) for b, c in x.items()})


def check_dual_number_derivative():
    premise("std-algebra.radical-ideal-and-quotient")
    D = GA.sig(0, 0, 1)
    rho = GA.gen(0)
    # f = (x^3 + 3x)/(x^2 + 1); hand-stated (x, f(x), f'(x)), f' = (x^4 + 3)/(x^2 + 1)^2
    for x, fx, dfx in ((0, 0, 3), (1, 2, 1), (2, F(14, 5), F(19, 25)), (F(-1, 3), F(-14, 15), F(61, 25))):
        val = ratfun_at([0, 3, 0, 1], [1, 0, 1], F(x), rho, D)
        assert GA.eq(val, GA.add(GA.sc(fx), GA.scal(dfx, rho)))
    return True


def check_derivative_through_a_generalised_inverse():
    premise("std-algebra.radical-ideal-and-quotient")
    premise("conformal.minimal-nondegenerate-completion")
    premise("singularity.pseudo-inverse-identities-hyperbolic-atom")
    premise("std-algebra.witt-basis-car")
    premise("transport.regularity-localises-zero-divisors-idempotents")
    count = 0
    for p, q, r in ((0, 0, 1), (1, 1, 1), (1, 2, 1), (0, 0, 2), (1, 3, 1)):
        S = GA.sig(p, q, r)
        nn = p + q + r
        for k in range(p + q, nn):
            rho = GA.gen(k)
            for bl in GA.all_blades(nn):
                assert GA.is_zero(GA.mul(GA.mul(rho, {bl: F(1)}, S), rho, S))
            count += 1
    assert count == 6
    assert GA.is_zero(m11(A, A)) and GA.eq(GA.add(m11(A, AP), m11(AP, A)), ONE)
    other = GA.add(AP, GA.scal(3, A), GA.scal(2, m11(A, AP)))     # a second generalised inverse of a
    for g in (AP, other):
        assert GA.eq(m11(m11(A, g), A), A)
        P = m11(g, A)
        assert GA.eq(m11(P, P), P)
        # f = 2 x^3 + 5 x, hand-stated (x, f(x), f'(x)), f' = 6 x^2 + 5
        for x, fx, dfx in ((0, 0, 5), (1, 7, 11), (-2, -26, 29), (F(3, 7), F(789, 343), F(299, 49))):
            fxn = poly_at([0, 5, 0, 2], F(x), A, S11)
            assert GA.eq(m11(g, GA.sub(fxn, GA.sc(fx))), GA.scal(dfx, P))
        for x, gx, dgx in ((2, F(14, 5), F(19, 25)), (F(-1, 3), F(-14, 15), F(61, 25))):
            val = ratfun_at([0, 3, 0, 1], [1, 0, 1], F(x), A, S11)
            assert GA.eq(m11(g, GA.sub(val, GA.sc(gx))), GA.scal(dgx, P))
    P_partner, P_other = m11(AP, A), m11(other, A)
    assert GA.eq(adjoint(P_partner), P_partner)
    assert not GA.eq(adjoint(P_other), P_other)
    assert GA.eq(adjoint(A), AP)
    return True


def esym(bs, k, S):
    out = {}
    for c in combinations(bs, k):
        t = GA.sc(1)
        for b in c:
            t = GA.mul(t, b, S)
        out = GA.add(out, t)
    return out


def steps_identity(bs, S):
    N = len(bs)
    eps = GA.add(*bs)
    prod = GA.sc(1)
    for b in bs:
        assert GA.is_zero(GA.mul(b, b, S))
        prod = GA.mul(prod, GA.add(GA.sc(1), b), S)
    for b in bs:
        for c in bs:
            assert GA.commutes(b, c, S)
    expo, pw, fact = {}, GA.sc(1), 1
    for k in range(N + 1):
        if k > 0:
            pw = GA.mul(pw, eps, S)
            fact *= k
        assert GA.eq(pw, GA.scal(fact, esym(bs, k, S)))
        expo = GA.add(expo, GA.scal(F(1, fact), pw))
    assert GA.is_zero(GA.mul(pw, eps, S))
    assert not GA.is_zero(esym(bs, N, S))           # the product of all steps is nonzero
    assert GA.eq(prod, expo)
    return len(expo)


def check_product_of_null_steps_is_the_exponential():
    premise("std-algebra.radical-ideal-and-quotient")
    premise("std-algebra.witt-basis-car")
    sizes = []
    for N in range(2, 7):
        S = GA.sig(0, 0, 2 * N)
        bs = [GA.mul(GA.gen(2 * i), GA.gen(2 * i + 1), S) for i in range(N)]
        sizes.append(steps_identity(bs, S))
    assert sizes == [4, 8, 16, 32, 64]
    S = GA.sig(6, 6)
    nulls = [GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(6 + i))) for i in range(6)]
    for x in nulls:
        for y in nulls:
            assert GA.anticommutes(x, y, S)
    bs = [GA.mul(nulls[2 * i], nulls[2 * i + 1], S) for i in range(3)]
    assert steps_identity(bs, S) > 8
    # Jordan-Wigner steps already in Cl(N, N)
    for N in (2, 3):
        S = GA.sig(N, N)
        v = [GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(N + i))) for i in range(N)]
        w = [GA.scal(F(1, 2), GA.sub(GA.gen(i), GA.gen(N + i))) for i in range(N)]
        pis = [GA.sub(GA.mul(v[j], w[j], S), GA.mul(w[j], v[j], S)) for j in range(N)]
        bs = []
        for i in range(N):
            b = v[i]
            for j in range(i):
                b = GA.mul(b, pis[j], S)
            bs.append(b)
        assert steps_identity(bs, S) == 3 ** N
    return True


def check_boost_scales_the_null_vector():
    premise("std-algebra.witt-basis-car")
    S = GA.sig(1, 1, 2)
    et, er = GA.gen(0), GA.gen(1)
    B = GA.mul(et, er, S)
    lp, lm = GA.add(et, er), GA.sub(et, er)
    assert GA.eq(GA.mul(lp, lp, S), {}) and GA.eq(GA.add(GA.mul(lp, lm, S), GA.mul(lm, lp, S)), GA.sc(4))
    assert GA.eq(GA.mul(B, lp, S), GA.neg(lp)) and GA.eq(GA.mul(lp, B, S), lp)
    for s in (F(1), F(-3), F(2, 5)):
        d = GA.scal(s, GA.mul(GA.gen(2), GA.gen(3), S))
        assert GA.is_zero(GA.mul(d, d, S)) and GA.commutes(d, et, S) and GA.commutes(d, er, S)
        dB = GA.mul(d, B, S)
        R = GA.add(GA.sc(1), GA.scal(F(1, 2), dB))
        Rinv = GA.sub(GA.sc(1), GA.scal(F(1, 2), dB))
        assert GA.eq(GA.mul(R, Rinv, S), GA.sc(1))
        assert GA.eq(GA.mul(GA.mul(R, lp, S), Rinv, S), GA.sub(lp, GA.mul(d, lp, S)))
        assert GA.eq(GA.mul(GA.mul(R, lm, S), Rinv, S), GA.add(lm, GA.mul(d, lm, S)))
        # the reversion of Cl(1,1,2) fixes the grade-4 element d B, so it is not the inverse here
        assert GA.eq(GA.reverse(R), R) and not GA.eq(GA.mul(R, GA.reverse(R), S), GA.sc(1))
        assert GA.eq(GA.mul(GA.mul(R, lp, S), GA.reverse(R), S), lp)
    for al, be in ((F(3), F(1)), (F(5, 13), F(-2, 7))):
        R = GA.add(GA.sc(al), GA.scal(be, B))
        assert GA.eq(GA.mul(GA.mul(R, lp, S), GA.reverse(R), S), GA.scal((al - be) ** 2, lp))
        assert GA.eq(GA.mul(GA.mul(R, lm, S), GA.reverse(R), S), GA.scal((al + be) ** 2, lm))
    R2 = GA.add(GA.sc(F(5, 4)), GA.scal(F(3, 4), B))
    assert GA.eq(GA.mul(R2, GA.reverse(R2), S), GA.sc(1))
    assert GA.eq(GA.mul(R2, lp, S), GA.scal(F(1, 2), lp))
    assert GA.eq(GA.mul(R2, lm, S), GA.scal(2, lm))
    return True
