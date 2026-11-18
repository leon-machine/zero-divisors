"""The eigenbundle class of a tame wall: a twisted wall on the cylinder and the transfer bookkeeping, exact.

The wall. On the cylinder S^1 x R, with l(a) = (cos a/2, sin a/2) spanning the twisted line L at the angle a,
    G(a, s) = P_perp + s P_L = 1 + (s - 1) l l^T        on the trivial plane bundle:
signature (2,0) for s > 0, (1,1) for s < 0, corank one at s = 0 with radical L. All entries are quadratic in
(C, S) = (cos a/2, sin a/2), so they are functions of the point; (C, S) and (-C, -S) give the same point.

(1) Eigenbundles: for s > 0 the positive eigenbundle is the whole plane (L_perp + L); for s < 0 it is L_perp and the
    negative one is L. The difference across the wall is L, a line whose unit section reverses after one turn.
(2) A two-sided completion with two rungs, nondegenerate everywhere: on R^2 + R^4,
    h = 1 - 2 (n n^T + b b^T),  n = (C, S) in a fixed plane Pi of R^4,  b = cos(t) n_perp + sin(t) l,
    t from 0 (physical end) to a quarter turn (far end). Signature (4,2) throughout. On the physical side it is
    G + K_ph with K_ph = 1 - 2 P_Pi, a constant form of signature (2,2) (two hyperbolic planes); on the far side
    G + K_far with K_far = 1 - 2 n n^T of signature (3,1), whose negative line N is twisted like L.
(3) Bookkeeping of transfer for k rungs: ranks, the Whitney consequence x^k = 0 from w(N) = 1/(1 + x), and the
    lambda consequence (1 - xi)^k = 2^(k-1) (1 - xi) for xi^2 = 1 (coefficient of t^k in (1 + t)^k / (1 + xi t)).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

# half-angle points (C, S) from tau = tan(a/4); the angle a runs over (-2 pi, 2 pi) as tau runs over the line
HALF_TAUS = [F(-5), F(-2), F(-1), F(-1, 2), F(-1, 5), F(0), F(1, 5), F(1, 2), F(1), F(2), F(5)]
S_VALUES = [F(-4), F(-2), F(-7, 4), F(-3, 2), F(-1), F(-1, 2), F(-1, 4), F(0), F(1, 4), F(1, 2), F(1),
            F(3, 2), F(7, 4), F(2), F(4)]
S_OUT, S_IN = F(2), F(1)
SIGNATURES = [(1, 1), (1, 3), (2, 2), (4, 0), (3, 1), (1, 5), (6, 0)]
RUNGS = [1, 2, 3, 4, 5, 6, 7, 8]
TRUNCATION = 12


def circ(tau):
    tau = F(tau)
    d = 1 + tau * tau
    return (1 - tau * tau) / d, 2 * tau / d


def outer(u, v):
    return [[a * b for b in v] for a in u]


def ident(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def lin(*terms):
    """Sum of c * M over (c, M)."""
    n, m = len(terms[0][1]), len(terms[0][1][0])
    return [[sum(c * mat[i][j] for (c, mat) in terms) for j in range(m)] for i in range(n)]


def dsum(a, b):
    n, m = len(a), len(b)
    return [list(a[i]) + [F(0)] * m for i in range(n)] + [[F(0)] * n + list(b[i]) for i in range(m)]


def wall_form(ch, sh, s):
    """G = 1 + (s - 1) l l^T with l = (C, S)."""
    return lin((F(1), ident(2)), (F(s) - 1, outer([ch, sh], [ch, sh])))


K_PH = [[(F(-1) if i < 2 else F(1)) if i == j else F(0) for j in range(4)] for i in range(4)]


def k_far(ch, sh):
    n = [ch, sh, F(0), F(0)]
    return lin((F(1), ident(4)), (F(-2), outer(n, n)))


def completion(ch, sh, s):
    s = F(s)
    ell = [ch, sh]
    if s >= S_OUT:
        return dsum(wall_form(ch, sh, s), K_PH)
    if s >= S_IN:
        lam = S_OUT - s
        return dsum(lin((1 - lam, wall_form(ch, sh, s)), (lam, ident(2))), K_PH)
    if s >= -S_IN:
        ct, st = circ((S_IN - s) / 2)                     # tan(t/2) from 0 (s = 1) to 1 (s = -1)
        n = [F(0), F(0), ch, sh, F(0), F(0)]
        b = [st * ch, st * sh, -ct * sh, ct * ch, F(0), F(0)]
        return lin((F(1), ident(6)), (F(-2), outer(n, n)), (F(-2), outer(b, b)))
    sign_far = lin((F(1), ident(2)), (F(-2), outer(ell, ell)))
    if s >= -S_OUT:
        lam = -s - S_IN
        return dsum(lin((1 - lam, sign_far), (lam, wall_form(ch, sh, s))), k_far(ch, sh))
    return dsum(wall_form(ch, sh, s), k_far(ch, sh))


def check_twisted_wall_and_its_eigenbundles():
    premise("synthesis.wall-class-one-rung-obstruction")
    premise("sheaf.imported-real-line-bundles")
    ok = True
    for tau in HALF_TAUS:
        ch, sh = circ(tau)
        ok = ok and ch * ch + sh * sh == 1
        for s in S_VALUES:
            g = wall_form(ch, sh, s)
            # the same form at the antipodal half-angle point: a function of the point of the circle
            ok = ok and g == wall_form(-ch, -sh, s)
            want = (2, 0, 0) if s > 0 else ((1, 1, 0) if s < 0 else (1, 0, 1))
            ok = ok and GA.congruence_signature(g) == want
            # l is an eigenvector of value s, l_perp of value 1
            ok = ok and GA.mat_mul(g, [[ch], [sh]]) == [[s * ch], [s * sh]]
            ok = ok and GA.mat_mul(g, [[-sh], [ch]]) == [[-sh], [ch]]
    # the unit section of L reverses after one turn: tau from 0 to infinity is a = 0 to 2 pi
    start, end = circ(F(0)), (F(-1), F(0))
    ok = ok and start == (1, 0) and wall_form(*start, F(0)) == wall_form(*end, F(0))
    ok = ok and [end[0], end[1]] == [-start[0], -start[1]]
    GA.check("G = 1 + (s-1) l l^T on the cylinder: signature (2,0), corank one with radical l, (1,1) for s > 0, "
             "= 0, < 0 at eleven half-angle points; the form is a function of the point and the unit section of "
             "the radical line reverses after one turn", ok)
    return ok


def check_two_rung_completion_moves_the_twist_into_the_far_form():
    premise("synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump")
    premise("synthesis.wall-rung-count-is-height-of-dying-line-class")
    ok = True
    ok = ok and GA.congruence_signature(K_PH) == (2, 2, 0)
    for tau in HALF_TAUS:
        ch, sh = circ(tau)
        kf = k_far(ch, sh)
        ok = ok and GA.congruence_signature(kf) == (3, 1, 0) and kf == k_far(-ch, -sh)
        ok = ok and GA.mat_mul(kf, [[ch], [sh], [F(0)], [F(0)]]) == [[-ch], [-sh], [F(0)], [F(0)]]
        for s in S_VALUES:
            h = completion(ch, sh, s)
            ok = ok and h == completion(-ch, -sh, s)
            ok = ok and GA.mat_eq(h, [list(r) for r in zip(*h)])
            ok = ok and GA.congruence_signature(h) == (4, 2, 0)
            if s >= S_OUT:
                ok = ok and h == dsum(wall_form(ch, sh, s), K_PH)
            if s <= -S_OUT:
                ok = ok and h == dsum(wall_form(ch, sh, s), kf)
        # seams at s = 1 and s = -1
        ok = ok and completion(ch, sh, S_IN) == dsum(ident(2), K_PH)
        ell = [ch, sh]
        ok = ok and completion(ch, sh, -S_IN) == dsum(lin((F(1), ident(2)), (F(-2), outer(ell, ell))), kf)
        # the undeformed sums are degenerate on the wall
        ok = ok and GA.congruence_signature(dsum(wall_form(ch, sh, F(0)), K_PH))[2] == 1
    GA.check("the form 1 - 2(n n^T + b b^T) on R^6 has signature (4,2) at eleven half-angle points and fifteen "
             "values of s, is G + K_ph (constant, signature (2,2)) for s >= 2 and G + K_far for s <= -2, with "
             "K_far = 1 - 2 n n^T of signature (3,1) and negative line n twisted like the radical line", ok)
    return ok


def pmul_mod2(a, b, trunc):
    out = [0] * trunc
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j < trunc:
                out[i + j] = (out[i + j] + x * y) % 2
    return out


def xi_mul(a, b):
    """(a0 + a1 xi)(b0 + b1 xi) with xi^2 = 1."""
    return (a[0] * b[0] + a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def binom(n, k):
    out = 1
    for i in range(k):
        out = out * (n - i) // (i + 1)
    return out


def check_transfer_bookkeeping_for_k_rungs():
    premise("synthesis.imported-whitney-product-formula-and-projective-space")
    premise("synthesis.wall-rung-count-is-height-of-dying-line-class")
    ok = True
    for (p, q) in SIGNATURES:
        for k in RUNGS:
            # exterior totals: physical (p, q) + (k, k); far (p-1, q+1) + sig K_far; equal iff sig K_far = (k+1, k-1)
            far = [(a, 2 * k - a) for a in range(2 * k + 1) if (p - 1 + a, q + 1 + 2 * k - a) == (p + k, q + k)]
            ok = ok and far == [(k + 1, k - 1)]
            # negative eigenbundles on the wall: q + k = q + 1 + rank N, with rank N the negative index of K_far
            ok = ok and all(q + k == q + 1 + neg for (pos, neg) in far)
    # Whitney: w(N) (1 + x) = 1 gives w(N) = 1 + x + x^2 + ... ; rank N = k - 1 forces x^j = 0 for j >= k
    inv = [1] * TRUNCATION
    ok = ok and pmul_mod2(inv, [1, 1], TRUNCATION) == [1] + [0] * (TRUNCATION - 1)
    for k in RUNGS:
        ok = ok and all(inv[j] == 1 for j in range(k, TRUNCATION))
    # lambda: coefficient of t^k in (1 + t)^k (1 + xi t)^(-1) is sum_j C(k, j) (-xi)^(k-j) = (1 - xi)^k,
    # and (1 - xi)^k = 2^(k-1) (1 - xi) when xi^2 = 1
    for k in RUNGS:
        coeff = (0, 0)
        for j in range(k + 1):
            sgn = (-1) ** (k - j)
            term = (sgn * binom(k, j), 0) if (k - j) % 2 == 0 else (0, sgn * binom(k, j))
            coeff = (coeff[0] + term[0], coeff[1] + term[1])
        power = (1, 0)
        for _ in range(k):
            power = xi_mul(power, (1, -1))
        ok = ok and coeff == power == (2 ** (k - 1), -(2 ** (k - 1)))
    GA.check("for seven signatures and k = 1..8 rungs the far exterior form must have signature (k+1, k-1), so "
             "its negative bundle N has rank k-1; w(N) = 1/(1+x) has every coefficient 1; the coefficient of "
             "t^k in (1+t)^k/(1+xi t) is (1-xi)^k = 2^(k-1)(1-xi)", ok)
    return ok
