"""transport.density: exact checks of the finite core of the density lemma.

Conformal model in Cl(p+1, q+1): n0 = (e- - e+)/2, ninf = e- + e+, X(x) = n0 + x + Q(x)/2 ninf.
The topological statement (closure in the quadric) is checked through the explicit paths of the
proof, with exact convergence certificates: a representative r(s) whose difference from the
limit is (1/s) g(1/s) with g a polynomial of degree <= 2 (verified at four values of s, one
beyond the interpolation nodes), so the difference tends to zero.
(1) Non-ideal null rays are lifts: for N = s n0 + y + t ninf with s != 0, nullity forces
    t = Q(y)/(2s) (solved from N^2, which is affine in t), and N / s = X(y/s).
(2) Invertible points are dense in V: Q(x + t a) = Q(x) + 2t x.a + t^2 Q(a) at five values of t,
    a nonconstant polynomial when Q(a) != 0, so among t = 1, 1/2, ..., 1/30 at most two zeros;
    the null samples have exactly the predicted zeros.
(3) Ideal points [x + t ninf] (x null, nonzero): u with x.u = 1, y_s = s x + (t + 1/s) u;
    Q(y_s) = 2ts + 2 + (t + 1/s)^2 Q(u); Q(y_s) != 0 at s = 10, 100, 1000, 10^4; and
    X(y_s)/s - (x + t ninf) = (1/s) g(1/s) with g(0) = n0 + t u + (1 + t^2 Q(u)/2) ninf.
(4) The point [ninf]: 2 X(s a)/(s^2 Q(a)) - ninf = (1/s) g(1/s) with g(0) = 2 a / Q(a).
No premises (the lemma has none in the store).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise  # noqa: F401  (no store premises)

SIGS = [(1, 1), (2, 1), (1, 2), (1, 3), (3, 1), (2, 2)]
YS = [[1, 2, -1, 3], [F(1, 2), -3, 2, 0], [2, 2, 2, 2]]
SS = [F(1), F(-2), F(1, 3), F(5)]
T_VALUES = [F(0), F(3), F(-2), F(1, 2)]


def _model(p, q):
    n = p + q
    sq = GA.sig(p, q) + (1, -1)
    ep, em = GA.gen(n), GA.gen(n + 1)
    n0 = GA.scal(F(1, 2), GA.sub(em, ep))
    ninf = GA.add(em, ep)
    return n, sq, n0, ninf


def _vec(cs):
    return {(i,): F(c) for i, c in enumerate(cs) if c != 0}


def _Q(x, sq):
    return GA.mul(x, x, sq).get((), F(0))


def _X(x, sq, n0, ninf):
    return GA.add(n0, x, GA.scal(_Q(x, sq) / 2, ninf))


def _null_and_partner(p, q):
    """The nonzero null x = e_0 + e_p and u = e_0, with x.u = 1 and Q(u) = 1."""
    n = p + q
    x = _vec([1 if i in (0, p) else 0 for i in range(n)])
    u = _vec([1 if i == 0 else 0 for i in range(n)])   # x.u = e_0^2 = 1
    return x, u


def _lagrange0(hs, vals):
    """Value at h = 0 of the quadratic through (h_i, vals_i), vals multivectors."""
    out = {}
    for i, hi in enumerate(hs):
        w = F(1)
        for j, hj in enumerate(hs):
            if j != i:
                w *= (0 - hj) / (hi - hj)
        out = GA.add(out, GA.scal(w, vals[i]))
    return out


def _lagrange_at(hs, vals, h):
    out = {}
    for i, hi in enumerate(hs):
        w = F(1)
        for j, hj in enumerate(hs):
            if j != i:
                w *= (h - hj) / (hi - hj)
        out = GA.add(out, GA.scal(w, vals[i]))
    return out


def check_non_ideal_null_rays_are_lifts():
    ok = True
    count = 0
    for (p, q) in SIGS:
        n, sq, n0, ninf = _model(p, q)
        for ys in YS:
            y = _vec(ys[:n])
            for s in SS:
                base = GA.add(GA.scal(s, n0), y)
                N0 = GA.mul(base, base, sq).get((), F(0))                       # N^2 at t = 0
                N1v = GA.add(base, ninf)
                slope = GA.mul(N1v, N1v, sq).get((), F(0)) - N0                # N^2 affine in t
                ok = ok and slope == -2 * s
                t = -N0 / slope
                ok = ok and t == _Q(y, sq) / (2 * s)
                N = GA.add(base, GA.scal(t, ninf))
                ok = ok and GA.is_zero(GA.mul(N, N, sq))
                ok = ok and GA.eq(GA.scal(1 / s, N), _X(GA.scal(1 / s, y), sq, n0, ninf))
                count += 1
    ok = ok and count == 72
    GA.check("every non-ideal null ray is the lift [X(y/s)]; nullity forces t = Q(y)/(2s)", ok)
    return ok


def check_invertible_points_dense_in_v():
    ok = True
    for (p, q) in SIGS:
        n, sq, n0, ninf = _model(p, q)
        x, a = _null_and_partner(p, q)          # Q(x) = 0, Q(a) = 1, x.a = 1
        for t in (F(0), F(1), F(-1), F(2, 3), F(5)):
            lhs = _Q(GA.add(x, GA.scal(t, a)), sq)
            ok = ok and lhs == _Q(x, sq) + 2 * t * GA.dot(x, a, sq) + t * t * _Q(a, sq)
        # zeros of Q(x + t a) = 2t + t^2 are t = 0 and t = -2 only: none among 1/k, k = 1..30
        zeros = [k for k in range(1, 31) if _Q(GA.add(x, GA.scal(F(1, k), a)), sq) == 0]
        ok = ok and zeros == []
        # xb = x - a/4: Q(xb + t a) = t^2 + 3t/2 - 7/16, roots t = 1/4 and t = -7/4
        xb = GA.sub(x, GA.scal(F(1, 4), a))
        zb = [k for k in range(1, 31) if _Q(GA.add(xb, GA.scal(F(1, k), a)), sq) == 0]
        ok = ok and zb == [4] and _Q(GA.add(xb, GA.scal(F(-7, 4), a)), sq) == 0
    GA.check("Q(x + t a) is the stated nonconstant quadratic; invertible points accumulate at x", ok)
    return ok


def check_ideal_points_are_limits_of_lifted_invertible_points():
    ok = True
    for (p, q) in SIGS:
        n, sq, n0, ninf = _model(p, q)
        x, u = _null_and_partner(p, q)
        ok = ok and _Q(x, sq) == 0 and GA.dot(x, u, sq) == 1 and _Q(u, sq) == 1
        for t in T_VALUES:
            limit = GA.add(x, GA.scal(t, ninf))
            ok = ok and not GA.is_zero(limit) and GA.is_zero(GA.mul(limit, limit, sq))
            hs, vals = [], []
            for s in (F(10), F(100), F(1000), F(10000)):
                ys = GA.add(GA.scal(s, x), GA.scal(t + 1 / s, u))
                Qy = _Q(ys, sq)
                ok = ok and Qy == 2 * t * s + 2 + (t + 1 / s) ** 2 * _Q(u, sq)
                ok = ok and Qy != 0
                rep = GA.scal(1 / s, _X(ys, sq, n0, ninf))
                hs.append(1 / s)
                vals.append(GA.scal(s, GA.sub(rep, limit)))          # g(1/s)
            g0 = _lagrange0(hs[:3], vals[:3])
            ok = ok and GA.eq(_lagrange_at(hs[:3], vals[:3], hs[3]), vals[3])   # degree <= 2 in 1/s
            expect = GA.add(n0, GA.scal(t, u), GA.scal(1 + t * t / 2, ninf))
            ok = ok and GA.eq(g0, expect)
    GA.check("ideal points [x + t ninf] are limits of X(y_s)/s with an O(1/s) remainder", ok)
    return ok


# Sample directions a (e_0 and 2 e_p, of either sign of Q(a)) and sample path parameters s.
def _directions(p, q):
    n = p + q
    return (_vec([1] + [0] * (n - 1)), _vec([0] * p + [2] + [0] * (q - 1)))


S_PATH = (F(3), F(30), F(300), F(7))


def check_point_at_infinity_is_limit():
    ok = True
    for (p, q) in SIGS:
        n, sq, n0, ninf = _model(p, q)
        for a in _directions(p, q):
            Qa = _Q(a, sq)
            hs, vals = [], []
            for s in S_PATH:
                rep = GA.scal(F(2) / (s * s * Qa), _X(GA.scal(s, a), sq, n0, ninf))
                h = 1 / s
                hs.append(h)
                vals.append(GA.scal(s, GA.sub(rep, ninf)))
                # by hand: X(s a) = n0 + s a + (s^2 Q(a)/2) ninf, so s (rep - ninf) = (2/Q(a)) (a + n0/s),
                # the remainder rep - ninf being exactly (2/(s Q(a))) a + (2/(s^2 Q(a))) n0 = O(1/s)
                ok = ok and GA.eq(vals[-1], GA.scal(F(2) / Qa, GA.add(a, GA.scal(h, n0))))
            ok = ok and GA.eq(_lagrange_at(hs[:-1], vals[:-1], hs[-1]), vals[-1])
            ok = ok and GA.eq(_lagrange0(hs[:-1], vals[:-1]), GA.scal(F(2) / Qa, a))
    GA.check("[ninf] is the limit of [X(s a)] with an O(1/s) remainder", ok)
    return ok
