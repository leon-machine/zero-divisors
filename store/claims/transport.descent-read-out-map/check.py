"""transport.descent-read-out-map: exact checks.

Conformal model in Cl(p+1, q+1): n0 = (e- - e+)/2, ninf = e- + e+, X(x) = n0 + x + Q(x)/2 ninf,
iota[N] = [e+ N e+] (Theorem transport.totality). Coordinates of N = s n0 + x + t ninf are read
off as s = -N.ninf, t = -N.n0, x = the V-part; dsc[N] = x/s.
(1) dsc is well defined: rescaling N by lambda (five values, negative included) leaves x/s
    unchanged; dsc[X(x)] = x; for a non-ideal null N, X(dsc[N]) = N/s, a member of [N].
    (Continuity: x/s is a rational map regular on {s != 0}; not tested further.)
(2) For Q(x) != 0: iota X(x) = -(Q(x) n0 + x + ninf/2), so dsc(iota[X(x)]) = x / Q(x), the
    classical reciprocal, which satisfies rho(x) x = 1.
(3) The composite is defined exactly on {Q != 0}: the n0-coefficient of iota X(x) is -Q(x), so for
    null x0 (and x0 = 0) iota[X(x0)] is ideal (s = 0), equal to [x0 + ninf/2], outside the domain.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = [(1, 1), (2, 1), (1, 2), (1, 3), (3, 1), (2, 2), (3, 0), (0, 2)]
XS = [[1, 2, -1, 3], [F(1, 2), -3, 2, 0], [2, 0, 1, 1], [0, 1, 0, 0]]
LAMBDAS = [F(2), F(-1), F(1, 3), F(-7, 2), F(11)]


def _model(p, q):
    n = p + q
    sq = GA.sig(p, q) + (1, -1)
    ep, em = GA.gen(n), GA.gen(n + 1)
    n0 = GA.scal(F(1, 2), GA.sub(em, ep))
    ninf = GA.add(em, ep)
    return n, sq, ep, n0, ninf


def _vec(cs):
    return {(i,): F(c) for i, c in enumerate(cs) if c != 0}


def _Q(x, sq):
    return GA.mul(x, x, sq).get((), F(0))


def _coords(N, n, sq, n0, ninf):
    s = -GA.dot(N, ninf, sq)
    t = -GA.dot(N, n0, sq)
    x = {b: c for b, c in N.items() if b[0] < n}
    return s, x, t


def check_descent_inverts_the_lift():
    ok = True
    count = 0
    for (p, q) in SIGS:
        n, sq, ep, n0, ninf = _model(p, q)
        for cs in XS:
            x = _vec(cs[:n])
            X = GA.add(n0, x, GA.scal(_Q(x, sq) / 2, ninf))
            s, xx, t = _coords(X, n, sq, n0, ninf)
            ok = ok and s == 1 and GA.eq(xx, x) and t == _Q(x, sq) / 2
            for lam in LAMBDAS:
                N = GA.scal(lam, X)
                sN, xN, tN = _coords(N, n, sq, n0, ninf)
                ok = ok and sN == lam                                   # s scales with N
                d = GA.scal(1 / sN, xN)
                ok = ok and GA.eq(d, x)                                  # dsc[N] = x, well defined
                Xd = GA.add(n0, d, GA.scal(_Q(d, sq) / 2, ninf))
                ok = ok and GA.eq(Xd, GA.scal(1 / sN, N))                # X(dsc N) in [N]
                count += 1
    ok = ok and count == 160
    GA.check("dsc well defined on rays, dsc[X(x)] = x and X(dsc[N]) = N/s, 8 signatures", ok)
    return ok


def check_descent_of_transported_point_is_reciprocal():
    premise("transport.totality")
    ok = True
    for (p, q) in SIGS:
        n, sq, ep, n0, ninf = _model(p, q)
        for cs in XS:
            x = _vec(cs[:n])
            Qx = _Q(x, sq)
            if Qx == 0:
                continue
            X = GA.add(n0, x, GA.scal(Qx / 2, ninf))
            I = GA.mul(GA.mul(ep, X, sq), ep, sq)
            ok = ok and GA.eq(I, GA.scal(-1, GA.add(GA.scal(Qx, n0), x, GA.scal(F(1, 2), ninf))))
            s, xx, t = _coords(I, n, sq, n0, ninf)
            rho = GA.scal(1 / s, xx)
            ok = ok and GA.eq(rho, GA.scal(1 / Qx, x))
            ok = ok and GA.eq(GA.mul(rho, x, sq), GA.sc(1))
    GA.check("dsc(iota[X(x)]) = x/Q(x), the classical reciprocal, on the invertible samples", ok)
    return ok


def check_composite_defined_exactly_off_the_null_cone():
    premise("transport.totality")
    ok = True
    nulls = 0
    for (p, q) in SIGS:
        n, sq, ep, n0, ninf = _model(p, q)
        samples = [_vec(cs[:n]) for cs in XS] + [{}]
        if p >= 1 and q >= 1:
            samples.append(_vec([1 if i in (0, p) else 0 for i in range(n)]))
            samples.append(_vec([3 if i == 0 else (-3 if i == p else 0) for i in range(n)]))
        for x in samples:
            Qx = _Q(x, sq)
            X = GA.add(n0, x, GA.scal(Qx / 2, ninf))
            I = GA.mul(GA.mul(ep, X, sq), ep, sq)
            s, xx, t = _coords(I, n, sq, n0, ninf)
            ok = ok and s == -Qx                       # n0-coefficient of iota X(x)
            ok = ok and ((s == 0) == (Qx == 0))
            if Qx == 0:
                nulls += 1
                ok = ok and GA.eq(I, GA.scal(-1, GA.add(x, GA.scal(F(1, 2), ninf))))
                ok = ok and GA.is_zero(GA.mul(I, I, sq)) and not GA.is_zero(I)
    # the origin in each of 8 signatures and two null vectors in each of the 6 mixed ones (none of
    # the XS samples is null in any of the 8 signatures)
    ok = ok and nulls == 8 + 2 * 6
    GA.check("iota[X(x0)] is ideal exactly when Q(x0) = 0 (20 null samples), equal to [x0 + ninf/2]", ok)
    return ok
