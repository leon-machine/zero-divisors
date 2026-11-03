"""transport.swap-rescale-normal-form: exact checks.

Setting as in transport.totality: Cl(p+1, q+1) with nO = (e_- - e_+)/2, nInf = e_- + e_+ (nO . nInf = -1),
N = s nO + x + t nInf, coordinates read back by s = -N.nInf, t = -N.nO and x the V-part.
(a) Incidence: N^2 = Q(x) - 2 s t, so N is null exactly when Q(x) = 2 s t; ordinary points (s != 0) have the
    normal form (1, x/s, Q(x/s)/2) = X(x/s).
(b) iota[N] = [e_+ N e_+] (Theorem transport.totality) is, in coordinates, (s, x, t) -> (2t, x, s/2) up to the
    projectively immaterial factor -1, on a grid of (s, x, t); it preserves Q(x) - 2 s t, is an involution, and
    reading out the first slot recovers the reciprocal X(x/Q(x)) when Q(x) != 0 and an ideal point otherwise.
(c) Strata of the ideal points (s = 0, so Q(x) = 0): for t != 0, x != 0 the representative (0, x/(2t), 1/2) is
    unique (the last slot fixes the scale), distinct null vectors give distinct classes, and the class is
    iota[X(x')]; x = 0 forces t != 0, giving [nInf] = iota[X(0)]. Projective classes computed on a grid (every
    nonzero null (0, x, t) with x in {-1, 0, 1}^n, t in {0, 1/2, -1, 2}; one class iff proportional coordinates):
    classes never mix strata (disjoint), stratum (i) classes coincide exactly when the labels x/(2t) do, stratum
    (ii) classes (t = 0) coincide exactly when the x are proportional, so they keep only the null ray, and
    stratum (iii) is one class; the class counts are 1, the number of null rays, and the number of null-vector
    labels on the grid. Exhaustiveness beyond the grid and bijectivity onto all null vectors are not computed.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

BASES = [(1, 1), (2, 1), (1, 3)]
XS = [(1, 2, -1, 3), (3, 0, 1, -2), (2, -1, 0, 5), (1, 1, 0, 0)]
STS = [(F(1), F(2)), (F(-3), F(1, 2)), (F(0), F(5)), (F(4), F(0)), (F(2, 3), F(-7))]


def setting(p, q):
    n = p + q
    sq = GA.sig(p, q) + (1, -1)
    ep, em = GA.gen(n), GA.gen(n + 1)
    return n, sq, ep, GA.scal(F(1, 2), GA.sub(em, ep)), GA.add(em, ep)


def vec(c, n):
    return {(i,): F(v) for i, v in enumerate(c[:n]) if v != 0}


def quad(x, sq):
    return GA.mul(x, x, sq).get((), F(0))


def build(s, x, t, no, ninf):
    return GA.add(GA.scal(s, no), x, GA.scal(t, ninf))


def coords(N, n, sq, no, ninf):
    s = -GA.dot(N, ninf, sq)
    t = -GA.dot(N, no, sq)
    x = {b: c for b, c in N.items() if b[0] < n}
    return s, x, t


def null_vectors(p, q):
    """Null vectors of V for the strata (mixed signatures only)."""
    n = p + q
    e = [GA.gen(i) for i in range(n)]
    return [GA.add(e[0], e[p]), GA.sub(GA.scal(2, e[0]), GA.scal(2, e[n - 1])),
            GA.add(GA.scal(3, e[0]), GA.scal(3, e[p]))]


def check_incidence_and_ordinary_normal_form():
    ok = True
    for p, q in BASES:
        n, sq, ep, no, ninf = setting(p, q)
        for c in XS:
            x = vec(c, n)
            for s, t in STS:
                N = build(s, x, t, no, ninf)
                ok = ok and quad(N, sq) == quad(x, sq) - 2 * s * t
                s2, x2, t2 = coords(N, n, sq, no, ninf)
                ok = ok and (s2, t2) == (s, t) and GA.eq(x2, x)
            for s in (F(1), F(-2), F(1, 3)):
                # the null class with first slot s, normalised by 1/s, is X(x/s)
                xs = GA.scal(s, x)
                t = quad(xs, sq) / (2 * s)
                N = build(s, xs, t, no, ninf)
                Xn = GA.add(no, x, GA.scal(quad(x, sq) / 2, ninf))
                ok = ok and quad(N, sq) == 0 and GA.eq(GA.scal(1 / s, N), Xn) and quad(Xn, sq) == 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_incidence_and_ordinary_normal_form"; return _tp_rv


def check_iota_is_the_swap_rescale_involution():
    premise("transport.totality")
    ok = True
    for p, q in BASES:
        n, sq, ep, no, ninf = setting(p, q)
        for c in XS:
            x = vec(c, n)
            for s, t in STS:
                N = build(s, x, t, no, ninf)
                M = GA.neg(GA.mul(GA.mul(ep, N, sq), ep, sq))      # overall -1 dropped
                s2, x2, t2 = coords(M, n, sq, no, ninf)
                ok = ok and s2 == 2 * t and t2 == s / 2 and GA.eq(x2, x)
                ok = ok and quad(x2, sq) - 2 * s2 * t2 == quad(x, sq) - 2 * s * t
                # involution in coordinates
                ok = ok and (2 * t2, x2, s2 / 2) == (s, x2, t)
            # read-out on the lifted point (1, x, Q/2) -> (Q, x, 1/2)
            Q = quad(x, sq)
            s2, x2, t2 = coords(build(2 * (Q / 2), x, F(1, 2), no, ninf), n, sq, no, ninf)
            ok = ok and s2 == Q and t2 == F(1, 2)
            if Q != 0:
                xr = GA.scal(1 / Q, x)
                ok = ok and t2 / s2 == quad(xr, sq) / 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_iota_is_the_swap_rescale_involution"; return _tp_rv


def check_three_strata_of_ideal_points():
    premise("transport.totality")
    ok = True
    # class counts on the grid x in {-1, 0, 1}^n, t in {0, 1/2, -1, 2}, derived by hand:
    # (1,1): (+-1, +-1), 4 null vectors, 2 rays; (2,1): one of x0, x1 and x2 nonzero, 8 vectors, 4 rays;
    # (1,3): x0 and one of x1..x3 nonzero, 12 vectors, 6 rays; stratum (i) labels x/(2t), t in {1/2, -1, 2}: 3 each
    stratum2_rays = {(1, 1): 2, (2, 1): 4, (1, 3): 6}
    stratum1_vectors = {(1, 1): 12, (2, 1): 24, (1, 3): 36}
    for p, q in BASES:
        n, sq, ep, no, ninf = setting(p, q)
        nulls = null_vectors(p, q)
        reps = []
        for x in nulls:
            ok = ok and quad(x, sq) == 0 and x != {}
            for t in (F(1), F(-3), F(1, 4)):
                N = build(0, x, t, no, ninf)
                ok = ok and quad(N, sq) == 0
                rep = GA.scal(1 / (2 * t), N)                        # last slot 1/2
                s2, xp, t2 = coords(rep, n, sq, no, ninf)
                ok = ok and s2 == 0 and t2 == F(1, 2) and quad(xp, sq) == 0
                # the class is iota[X(x')] for the null vector x' = x/(2t)
                img = GA.mul(GA.mul(ep, GA.add(no, xp), sq), ep, sq)  # X(x') = nO + x'
                ok = ok and GA.eq(GA.scal(-2, img), GA.scal(2, rep))
                reps.append(rep)
            # stratum (ii): (0, x, 0) and (0, lam x, 0) are one class; no representative with last slot 1/2
            for lam in (F(2), F(-1, 3)):
                N2 = build(0, GA.scal(lam, x), 0, no, ninf)
                ok = ok and quad(N2, sq) == 0 and coords(N2, n, sq, no, ninf)[2] == 0
        # stratum (i): distinct null vectors x' give distinct representatives
        distinct = []
        for r in reps:
            if not any(GA.eq(r, d) for d in distinct):
                distinct.append(r)
        ok = ok and len(distinct) == 9
        # stratum (iii): x = 0, s = 0 forces t != 0; it is [nInf] = iota[X(0)]
        ok = ok and build(0, {}, 0, no, ninf) == {}
        ok = ok and GA.eq(GA.mul(GA.mul(ep, no, sq), ep, sq), GA.scal(F(-1, 2), ninf))
        # projective classes on a grid: every nonzero null N = (0, x, t) with x in {-1, 0, 1}^n and t in TS.
        # Two elements are one class iff their coordinate vectors are proportional (computed, not assumed).
        def cvec(N):
            s2, x2, t2 = coords(N, n, sq, no, ninf)
            return [s2] + [x2.get((i,), F(0)) for i in range(n)] + [t2]

        def proportional(u, v):
            return all(u[i] * v[j] == u[j] * v[i] for i in range(len(u)) for j in range(len(u)))

        def stratum(c):
            xpart, t = c[1:-1], c[-1]
            if any(xpart):
                return 1 if t != 0 else 2
            return 3
        pts = []
        for code in range(3 ** n):
            xc = [(code // 3 ** i) % 3 - 1 for i in range(n)]
            x = vec(xc, n)
            if quad(x, sq) != 0:
                continue
            for t in (F(0), F(1, 2), F(-1), F(2)):
                N = build(0, x, t, no, ninf)
                if N:
                    ok = ok and quad(N, sq) == 0
                    pts.append(cvec(N))
        n_classes = []
        for i, u in enumerate(pts):
            for v in pts[:i]:
                same = proportional(u, v)
                if same:
                    ok = ok and stratum(u) == stratum(v)                  # strata disjoint
                if stratum(u) == 1 and stratum(v) == 1:
                    # labelled bijectively by the null vector x/(2t)
                    lab_u = [a / (2 * u[-1]) for a in u[1:-1]]
                    lab_v = [a / (2 * v[-1]) for a in v[1:-1]]
                    ok = ok and same == (lab_u == lab_v)
                if stratum(u) == 2 and stratum(v) == 2:
                    ok = ok and same == proportional(u[1:-1], v[1:-1])    # labelled by the null ray
                if stratum(u) == 3 and stratum(v) == 3:
                    ok = ok and same                                       # the single point [nInf]
            if not any(proportional(u, v) for v in pts[:i]):
                n_classes.append(stratum(u))
        ok = ok and n_classes.count(3) == 1
        ok = ok and n_classes.count(2) == stratum2_rays[(p, q)] and n_classes.count(1) == stratum1_vectors[(p, q)]
    _tp_rv = (ok); assert _tp_rv is not False, "check_three_strata_of_ideal_points"; return _tp_rv
