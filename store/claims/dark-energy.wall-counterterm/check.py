"""dark-energy.wall-counterterm: exact checks of the Chern-Simons counterterm.

Exact exterior calculus on coordinates (s, x, y, z) with coefficients rational functions of s (GA.RF);
Kasner exponents p_i = n_i/N with tau = s^N, so every power is integral; eta = diag(+, -, -, -),
epsilon_{0123} = 1. Q(omega) = eps_{abcd}(omega^{ab} ^ d omega^{cd} + 2/3 omega^{ab} ^ omega^c_e ^ omega^{ed}).
(i) dQ = eps_{abcd} R^{ab} ^ R^{cd} identically: on the Kasner connection omega^{i0} = (p_i/tau) e^i at
    p = (-1/3, 2/3, 2/3) and (-2/7, 3/7, 6/7), and for a generic so(1,3) connection with all six components
    nonzero, polynomial in s, legs in all four directions (eps R ^ R itself nonzero).
(ii) On the Kasner approach Q restricted to tau = const is 8 p1 p2 p3 tau^{-2} d^3x, and eps R ^ R is
    -16 p1 p2 p3 tau^{-3} dtau d^3x, so the curvature-squared term (3/Lambda) eps R ^ R integrated over
    eps < tau < tau_1 is (3/Lambda)(Q(tau_1) - Q(eps)), whose divergent part -(3/Lambda) Q(eps) =
    -(24/Lambda) p1 p2 p3 eps^{-2} (Lambda = 3, -1/2, 7); adding (3/Lambda) Q(eps) leaves (3/Lambda) Q(tau_1),
    independent of eps.
(iii) On Kasner the quadratic term omega ^ d omega contributes nothing to the slice component and the cubic
    term carries all of it. Q is not gauge invariant: under a local boost Lambda(s) in the (0, 1) plane
    (rational: cosh = (1 + t^2)/(1 - t^2), sinh = 2t/(1 - t^2), t = s/7), omega' = Lambda omega Lambda^{-1}
    + Lambda d Lambda^{-1} gives Q' != Q while dQ' = dQ.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

RFs = GA.RF.var()
RF1, RF0 = GA.RF1, GA.RF0
ETA = [1, -1, -1, -1]
KASNER = [(3, (-1, 2, 2)), (7, (-2, 3, 6))]
LAMBDAS = [F(3), F(-1, 2), F(7)]
EPSS = [F(1, 10), F(1, 1000)]
TAU1 = F(2)
PAIRS4 = [(m, n) for m in range(4) for n in range(m + 1, 4)]
GEN_SEED = 3


def rfk(x):
    return GA.RF.const(F(x))


def spow(n):
    r = RF1
    for _ in range(abs(n)):
        r = r * RFs
    return r if n >= 0 else RF1 / r


def eps4(a, b, c, d):
    p = [a, b, c, d]
    if len(set(p)) < 4:
        return 0
    s = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]:
                s = -s
    return s


def wedge(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            if set(ka) & set(kb):
                continue
            arr = list(ka) + list(kb)
            sg = 1
            for i in range(len(arr)):
                for j in range(len(arr) - 1 - i):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        sg = -sg
            key = tuple(arr)
            out[key] = out.get(key, RF0) + rfk(sg) * va * vb
    return out


def dform(a):
    out = {}
    for k, v in a.items():
        if 0 in k:
            continue
        key = (0,) + k
        out[key] = out.get(key, RF0) + v.deriv()
    return out


def add(a, b, sb=RF1):
    return {k: a.get(k, RF0) + sb * b.get(k, RF0) for k in set(a) | set(b)}


def scal(a, f):
    return {k: v * f for k, v in a.items()}


def is_zero_form(a):
    return all(v.is_zero() for v in a.values())


def curvature_and_Q(om, parts=False):
    W = lambda a, b: om.get((a, b), {})
    R = {}
    for a in range(4):
        for b in range(4):
            if a != b:
                cur = dform(W(a, b))
                for c in range(4):
                    cur = add(cur, wedge(scal(W(a, c), rfk(ETA[c])), W(c, b)))
                R[(a, b)] = cur
    GB, Q2, Q3 = {}, {}, {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    sg = eps4(a, b, c, d)
                    if not sg:
                        continue
                    GB = add(GB, wedge(R[(a, b)], R[(c, d)]), rfk(sg))
                    Q2 = add(Q2, wedge(W(a, b), dform(W(c, d))), rfk(sg))
                    t2 = {}
                    for e in range(4):
                        t2 = add(t2, wedge(wedge(W(a, b), scal(W(c, e), rfk(ETA[e]))), W(e, d)))
                    Q3 = add(Q3, t2, rfk(sg))
    Q = add(Q2, scal(Q3, rfk(F(2, 3))))
    return (GB, Q, Q2, Q3) if parts else (GB, Q)


def kasner_connection(N, ns):
    tau = spow(N)
    e = [{(0,): rfk(N) * spow(N - 1)}] + [{(i + 1,): spow(ns[i])} for i in range(3)]
    om = {}
    for i in range(1, 4):
        om[(i, 0)] = scal(e[i], rfk(F(ns[i - 1], N)) / tau)
        om[(0, i)] = scal(om[(i, 0)], -RF1)
    return om, tau


def generic_connection():
    seed = [GEN_SEED]

    def coef():
        seed[0] = (seed[0] * 7 + 5) % 11
        c0, c1 = seed[0] - 5, (seed[0] * 3) % 7 - 3
        return rfk(c0) + rfk(c1) * RFs + rfk(c1 * c0 % 5) * RFs * RFs
    om = {}
    for (a, b) in PAIRS4:
        om[(a, b)] = {(mu,): coef() for mu in range(4)}
        om[(b, a)] = scal(om[(a, b)], -RF1)
    return om


def check_transgression_identity():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    for (N, ns) in KASNER:
        om, tau = kasner_connection(N, ns)
        GB, Q = curvature_and_Q(om)
        assert is_zero_form(add(GB, dform(Q), -RF1)) and not is_zero_form(GB)
    GB, Q = curvature_and_Q(generic_connection())
    assert is_zero_form(add(GB, dform(Q), -RF1)) and not is_zero_form(GB)
    assert sum(1 for v in GB.values() if not v.is_zero()) >= 1


def check_slice_value_and_divergence_cancelled():
    premise("dark-energy.frozen-point-datum-kasner-wall")
    for (N, ns) in KASNER:
        om, tau = kasner_connection(N, ns)
        GB, Q = curvature_and_Q(om)
        p = [F(n, N) for n in ns]
        ppp = p[0] * p[1] * p[2]
        q_slice = Q.get((1, 2, 3), RF0)
        assert q_slice.eqrf(rfk(8 * ppp) / (tau * tau))
        dtau = rfk(N) * spow(N - 1)                    # dtau = N s^{N-1} ds
        assert GB.get((0, 1, 2, 3), RF0).eqrf(rfk(-16 * ppp) / (tau * tau * tau) * dtau)
        Qtau = lambda t: 8 * ppp / (t * t)
        for Lam in LAMBDAS:
            for eps in EPSS:
                bulk = 3 / Lam * (Qtau(TAU1) - Qtau(eps))
                assert -3 / Lam * Qtau(eps) == -24 / Lam * ppp / (eps * eps)
                assert bulk + 3 / Lam * Qtau(eps) == 3 / Lam * Qtau(TAU1)


# --- a second, two-variable calculus for the gauge check: Laurent polynomials in (s, x) as dicts
# {(i, j): coefficient}, forms on coordinates (s, x, y, z) = (0, 1, 2, 3) with such coefficients


def lp_add(a, b, c=1):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + c * v
    return {k: v for k, v in out.items() if v}


def lp_mul(a, b):
    out = {}
    for (i, j), u in a.items():
        for (k, l), v in b.items():
            out[(i + k, j + l)] = out.get((i + k, j + l), F(0)) + u * v
    return {k: v for k, v in out.items() if v}


def lp_d(a, var):
    out = {}
    for (i, j), u in a.items():
        e = (i, j)[var]
        if e:
            key = (i - 1, j) if var == 0 else (i, j - 1)
            out[key] = out.get(key, F(0)) + e * u
    return out


def f_wedge(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            if set(ka) & set(kb):
                continue
            arr = list(ka) + list(kb)
            sg = 1
            for i in range(len(arr)):
                for j in range(len(arr) - 1 - i):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        sg = -sg
            key = tuple(arr)
            out[key] = lp_add(out.get(key, {}), lp_mul(va, vb), sg)
    return {k: v for k, v in out.items() if v}


def f_add(a, b, c=1):
    out = {k: lp_add(a.get(k, {}), b.get(k, {}), c) for k in set(a) | set(b)}
    return {k: v for k, v in out.items() if v}


def f_scal(a, f):
    out = {k: lp_mul(v, f) for k, v in a.items()}
    return {k: v for k, v in out.items() if v}


def f_d(a):
    out = {}
    for k, v in a.items():
        for var in (0, 1):
            if var in k:
                continue
            dv = lp_d(v, var)
            if not dv:
                continue
            arr = [var] + list(k)
            sg = 1
            for i in range(len(arr)):
                for j in range(len(arr) - 1 - i):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        sg = -sg
            key = tuple(arr)
            out[key] = lp_add(out.get(key, {}), dv, sg)
    return {k: v for k, v in out.items() if v}


def lp_Q_and_GB(om):
    W = lambda a, b: om.get((a, b), {})
    eta = lambda c: {(0, 0): F(ETA[c])}
    R = {}
    for a in range(4):
        for b in range(4):
            if a != b:
                cur = f_d(W(a, b))
                for c in range(4):
                    cur = f_add(cur, f_wedge(f_scal(W(a, c), eta(c)), W(c, b)))
                R[(a, b)] = cur
    GB, Q = {}, {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    sg = eps4(a, b, c, d)
                    if not sg:
                        continue
                    GB = f_add(GB, f_wedge(R[(a, b)], R[(c, d)]), sg)
                    Q = f_add(Q, f_wedge(W(a, b), f_d(W(c, d))), sg)
                    for e in range(4):
                        Q = f_add(Q, f_wedge(f_wedge(W(a, b), f_scal(W(c, e), eta(e))), W(e, d)), F(2, 3) * sg)
    return GB, Q


def lp_kasner(N, ns):
    om = {}
    for i in range(1, 4):
        om[(i, 0)] = {(i,): {(ns[i - 1] - N, 0): F(ns[i - 1], N)}}
        om[(0, i)] = {(i,): {(ns[i - 1] - N, 0): F(-ns[i - 1], N)}}
    return om


def null_rotation_gauge(om):
    """omega' = L omega L^{-1} + L dL^{-1}, L = exp(x N) = 1 + x N + x^2 N^2/2, N the null rotation about
    e_0 + e_1 into e_2 (mixed indices), N^3 = 0; returns the new omega^{ab}."""
    l = [F(1), F(-1), F(0), F(0)]                      # (e_0 + e_1)_b lowered
    up = [F(1), F(1), F(0), F(0)]
    e2_low = [F(0), F(0), F(-1), F(0)]
    e2_up = [F(0), F(0), F(1), F(0)]
    Nm = [[up[a] * e2_low[b] - e2_up[a] * l[b] for b in range(4)] for a in range(4)]
    N2 = [[sum(Nm[a][k] * Nm[k][b] for k in range(4)) for b in range(4)] for a in range(4)]
    assert all(sum(N2[a][k] * Nm[k][b] for k in range(4)) == 0 for a in range(4) for b in range(4))
    Lm = [[{k: v for k, v in {(0, 0): F(int(a == b)), (0, 1): Nm[a][b], (0, 2): N2[a][b] / 2}.items() if v}
           for b in range(4)] for a in range(4)]
    Li = [[{k: v for k, v in {(0, 0): F(int(a == b)), (0, 1): -Nm[a][b], (0, 2): N2[a][b] / 2}.items() if v}
           for b in range(4)] for a in range(4)]
    for a in range(4):
        for b in range(4):
            prod = {}
            for k in range(4):
                prod = lp_add(prod, lp_mul(Lm[a][k], Li[k][b]))
            assert prod == ({(0, 0): F(1)} if a == b else {})
    mixed = {(a, b): f_scal(om.get((a, b), {}), {(0, 0): F(ETA[b])}) for a in range(4) for b in range(4)}
    new = {}
    for a in range(4):
        for b in range(4):
            acc = {}
            for c in range(4):
                for d in range(4):
                    if Lm[a][c] and Li[d][b]:
                        acc = f_add(acc, f_scal(mixed[(c, d)], lp_mul(Lm[a][c], Li[d][b])))
                dLi = lp_d(Li[c][b], 1)
                if Lm[a][c] and dLi:
                    acc = f_add(acc, {(1,): lp_mul(Lm[a][c], dLi)})
            new[(a, b)] = acc
    return {(a, b): f_scal(new[(a, b)], {(0, 0): F(ETA[b])}) for a in range(4) for b in range(4) if a != b}


def check_quadratic_term_vanishes_and_gauge_dependence():
    for (N, ns) in KASNER:
        om, tau = kasner_connection(N, ns)
        GB, Q, Q2, Q3 = curvature_and_Q(om, parts=True)
        assert Q2.get((1, 2, 3), RF0).is_zero()
        assert (Q3.get((1, 2, 3), RF0) * rfk(F(2, 3))).eqrf(Q.get((1, 2, 3), RF0))
        assert not Q3.get((1, 2, 3), RF0).is_zero()
    N, ns = KASNER[0]
    om = lp_kasner(N, ns)
    GB, Q = lp_Q_and_GB(om)
    p = [F(n, N) for n in ns]
    assert Q.get((1, 2, 3)) == {(-2 * N, 0): 8 * p[0] * p[1] * p[2]}
    om2 = null_rotation_gauge(om)
    for a in range(4):
        for b in range(a + 1, 4):
            assert not f_add(om2.get((a, b), {}), om2.get((b, a), {}))
    GB2, Q2 = lp_Q_and_GB(om2)
    assert not f_add(GB2, GB, -1)
    assert f_add(Q2, Q, -1)
    assert not f_add(f_d(Q2), f_d(Q), -1)
    assert not f_add(f_d(Q), GB, -1)
