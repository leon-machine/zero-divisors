"""singularity.transport-schwarzschild-fibre: exact checks in Gauge Theory Gravity (GA).

Background: Cl(1,3) local unit frame e_t, e_r, e_theta, e_phi (gens 0..3); completion Cl(2,4) with e+ (gen 4,
square +1), e- (gen 5, square -1), n0 = (e- - e+)/2, ninf = e- + e+ (n0 . ninf = -1). Points of the quadric are
N = s n0 + X + t ninf; the transported reciprocal is iota[N] = [e+ N e+] (computed in GA), and
dsc(N) = X/s (undefined at s = 0). The lift of a background vector x at p uses its physical vector:
X_p(x) = n0 + hb^{-1}(x) + Q_p(x) ninf/2 with Q_p(x) = Q(hb^{-1}(x)).
Static gauge (r > 2M): hb^{-1}(e_t) = sqrt(f) e_t, hb^{-1}(e_r) = e_r/sqrt(f), hb^{-1}(e_theta) = r e_theta,
hb^{-1}(e_phi) = r sin e_phi, symmetric, so hb^T = hb. Rational points: f = w^2, r = 2M/(1 - w^2), with 2M a
square and w Pythagorean so that sqrt(r) is rational too. PG gauge: hb(a) = a - beta (a . e_t) e_r,
hb^T(a) = a - beta (a . e_r) e_t (horizon and interior included). A covector xi = xi_t dt + xi_r dr is the
background vector xi_t e_t - xi_r e_r (reciprocal frame), with Q*_p(xi) = Q(hb^T(xi)).
(1) Static Gram of Q_p is diag(f, -1/f, -r^2, -r^2 sin^2); X_p(x)^2 = 0 for sample x; iota preserves
    the quadric value of every sample N (incident or not) and is an involution, e+ N e+ = -(2t n0 + X + (s/2) ninf).
(2) Q_p(x) != 0: dsc(iota(X_p(x))) = hb^{-1}(x)/Q_p(x), the physical vector of x/Q_p(x).
(3) x = e_t + f e_r: physical vector sqrt(f)(e_t + e_r) is null, iota(X_p(x)) has s = 0 and equals, up to the
    scale, hb^{-1}(x) + ninf/2: an ideal point, dsc undefined (division raises). Q(e_t + f e_r) = 0 also as
    an identity in Q(r).
(4) k = sqrt(r) dr + sqrt(2M) dt_PG: in the PG gauge hb^T(k) = -sqrt(r) e_r and Q*(k) = -r at r inside, at and
    outside the horizon; in the static chart k = sqrt(2M) dt_s + (sqrt(r)/f) dr gives hb^T(k) with Q = -r too
    (the two coordinate forms agree: dt_PG = dt_s + (beta/f) dr). Q*(k) = 2M/f - r/f = -r and the PG Gram
    k^T G k = -r, det G = -r, as identities in Q(r). The lift of k descends to dsc = -k/r (as a physical
    covector, -hb^T(k)/r) at every sample r > 0; its iota image has slots (-r, hb^T k, 1/2) up to sign, a
    polynomial in u = sqrt(r) whose value at u = 0 is the ideal point [ninf/2] (s = 0): the read-out fails
    only where -r = 0, i.e. on E.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S6 = (1, -1, -1, -1, 1, -1)
ET, ER, ETH, EPH, EP, EM = (GA.gen(i) for i in range(6))
N0 = GA.scal(F(1, 2), GA.sub(EM, EP))
NINF = GA.add(EM, EP)
# (M, w, sin theta): 2M a square, 1 - w^2 a square, so sqrt(f) = w and sqrt(r) are rational
STATIC = [(F(1, 2), F(3, 5), F(4, 5)), (F(2), F(5, 13), F(3, 5)), (F(9, 2), F(8, 17), F(1))]


def dot(a, b):
    return GA.dot(a, b, S6)


def slots(N):
    s = -dot(N, NINF)
    t = -dot(N, N0)
    X = GA.sub(N, GA.add(GA.scal(s, N0), GA.scal(t, NINF)))
    return s, X, t


def iota(N):
    return GA.mul(GA.mul(EP, N, S6), EP, S6)


def lift(X):
    Q = dot(X, X)
    return GA.add(N0, X, GA.scal(Q / 2, NINF)), Q


def static_hbinv(x, M, w, sn):
    """x = coefficients (a_t, a_r, a_th, a_ph) on the coordinate directions; returns hb^{-1}(x)."""
    r = 2 * M / (1 - w * w)
    a_t, a_r, a_th, a_ph = x
    return GA.add(GA.scal(a_t * w, ET), GA.scal(a_r / w, ER), GA.scal(a_th * r, ETH), GA.scal(a_ph * r * sn, EPH))


def isqrt_frac(q):
    for d in range(1, 200):
        n2 = q * d * d
        if n2.denominator == 1:
            n = int(n2)
            lo, hi = 0, n + 1
            while lo < hi:
                mid = (lo + hi) // 2
                if mid * mid < n:
                    lo = mid + 1
                else:
                    hi = mid
            if lo * lo == n:
                return F(lo, d)
    return None


def check_static_fibre_lift_incidence_involution():
    premise("transport.totality")
    premise("transport.swap-rescale-normal-form")
    ok = True
    for M, w, sn in STATIC:
        r = 2 * M / (1 - w * w)
        f = w * w
        frame = [static_hbinv(tuple(F(1) if i == j else F(0) for i in range(4)), M, w, sn) for j in range(4)]
        G = [[dot(a, b) for b in frame] for a in frame]
        ok = ok and G == [[f, 0, 0, 0], [0, -1 / f, 0, 0], [0, 0, -r * r, 0], [0, 0, 0, -r * r * sn * sn]]
        for x in [(F(1), F(2), F(0), F(1, 3)), (F(-3, 2), F(1, 7), F(2), F(0))]:
            X, Q = lift(static_hbinv(x, M, w, sn))
            ok = ok and GA.is_zero(GA.mul(X, X, S6)) and Q != 0
            Y = iota(X)
            ok = ok and GA.is_zero(GA.mul(Y, Y, S6))
            s, Xv, t = slots(X)
            s2, X2, t2 = slots(Y)
            ok = ok and (s2, t2) == (-2 * t, -s / 2) and GA.eq(X2, GA.neg(Xv))
            ok = ok and GA.eq(iota(Y), X)
        Ngen = GA.add(GA.scal(F(3, 4), N0), static_hbinv((F(1), F(1), F(0), F(0)), M, w, sn), GA.scal(F(-2, 7), NINF))
        ok = ok and not GA.is_zero(GA.mul(Ngen, Ngen, S6))
        ok = ok and GA.eq(GA.mul(iota(Ngen), iota(Ngen), S6), GA.mul(Ngen, Ngen, S6))
    _tp_rv = (ok); assert _tp_rv is not False, "check_static_fibre_lift_incidence_involution"; return _tp_rv


# Background vectors x with Q_p(x) != 0 at the static sample points.
X_INVERTIBLE = [(F(1), F(2), F(0), F(1, 3)), (F(-3, 2), F(1, 7), F(2), F(0)), (F(0), F(1), F(0), F(0))]


def check_invertible_directions_return_reciprocal():
    premise("transport.descent-read-out-map")
    ok = True
    for M, w, sn in STATIC:
        for x in X_INVERTIBLE:
            Xph = static_hbinv(x, M, w, sn)
            Xl, Q = lift(Xph)
            s, Xv, t = slots(iota(Xl))
            # by (1), e+ N e+ = -(2t n0 + X + (s/2) ninf); the lift has s = 1, t = Q/2, so iota has s = -Q, t = -1/2
            ok = ok and bool(Q) and s == -Q and t == F(-1, 2)
            want = static_hbinv(tuple(c / Q for c in x), M, w, sn)
            ok = ok and GA.eq(GA.scal(1 / s, Xv), want)
    _tp_rv = (ok); assert _tp_rv is not False, "check_invertible_directions_return_reciprocal"; return _tp_rv


def check_null_directions_go_ideal():
    premise("transport.totality")
    premise("transport.descent-read-out-map")
    ok = True
    for M, w, sn in STATIC:
        f = w * w
        x = (F(1), f, F(0), F(0))
        Xph = static_hbinv(x, M, w, sn)
        ok = ok and GA.eq(Xph, GA.scal(w, GA.add(ET, ER)))
        Xl, Q = lift(Xph)
        ok = ok and Q == 0
        Y = iota(Xl)
        s, Xv, t = slots(Y)
        ok = ok and s == 0 and t != 0
        ok = ok and t == F(-1, 2) and GA.eq(Y, GA.neg(GA.add(Xph, GA.scal(F(1, 2), NINF))))
        undefined = False
        try:
            GA.scal(1 / s, Xv)
        except ZeroDivisionError:
            undefined = True
        ok = ok and undefined
    r = GA.RF.var()
    for M in (F(1), F(3, 2)):
        f = (r - GA.RF.const(2 * M)) / r
        ok = ok and (f - (f * f) / f).is_zero()
    _tp_rv = (ok); assert _tp_rv is not False, "check_null_directions_go_ideal"; return _tp_rv


def check_dying_direction_dual_norm_and_read_out():
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    premise("singularity.degeneration-exactly")
    premise("transport.descent-read-out-map")
    ok = True
    # PG gauge, inside, at and outside the horizon: r and 2M squares
    for M in (F(1, 2), F(2), F(9, 2)):
        a = isqrt_frac(2 * M)
        for r in (F(1, 4), 2 * M, F(9), F(25, 16)):
            u = isqrt_frac(r)
            beta = a / u
            xi = GA.sub(GA.scal(a, ET), GA.scal(u, ER))          # sqrt(2M) dt + sqrt(r) dr
            hbT = GA.sub(xi, GA.scal(beta * dot(xi, ER), ET))
            ok = ok and GA.eq(hbT, GA.scal(-u, ER)) and dot(hbT, hbT) == -r
            # lift and read-out of the physical covector
            Xl, Q = lift(hbT)
            s, Xv, t = slots(iota(Xl))
            ok = ok and Q == -r and s == r and GA.eq(GA.scal(1 / s, Xv), GA.scal(-1 / r, hbT))
    # static chart form at the STATIC samples: k = sqrt(2M) dt_s + (sqrt(r)/f) dr
    for M, w, sn in STATIC:
        f = w * w
        r = 2 * M / (1 - f)
        a, u = isqrt_frac(2 * M), isqrt_frac(r)
        beta = a / u
        ok = ok and u + a * beta / f == u / f                  # dt_PG = dt_s + (beta/f) dr
        xi = GA.sub(GA.scal(a, ET), GA.scal(u / f, ER))
        # static hb^T = hb: e_t -> e_t/w, e_r -> w e_r
        hbT = GA.add(GA.scal(dot(xi, ET) / w, ET), GA.scal(w, GA.sub(xi, GA.scal(dot(xi, ET), ET))))
        ok = ok and GA.eq(hbT, GA.sub(GA.scal(a / w, ET), GA.scal(u / w, ER)))
        ok = ok and dot(hbT, hbT) == -r
    # identities in Q(r)
    rr = GA.RF.var()
    for M in (F(1), F(3, 2)):
        twoM = GA.RF.const(2 * M)
        f = (rr - twoM) / rr
        Qk = twoM / f + (rr / (f * f)) * (GA.RF.const(0) - f)
        ok = ok and Qk.eqrf(GA.RF.const(0) - rr)
        for m in (F(1), F(2)):
            mc = GA.RF.const(m)
            z = GA.RF.const(0)
            G = [[GA.RF.const(m * m) - rr, z - mc, z, z], [z - mc, GA.RF.const(1), z, z],
                 [z, z, GA.RF.const(-1), z], [z, z, z, GA.RF.const(-1)]]
            k = [GA.RF.const(1), mc, z, z]
            quad = z
            for i in range(4):
                for j in range(4):
                    quad = quad + k[i] * G[i][j] * k[j]
            ok = ok and quad.eqrf(z - rr) and GA.rf_mat_det(G).eqrf(z - rr)
    # the iota image of the lift of k, as a polynomial in u = sqrt(r): slots (s, vector, t) up to sign
    # s = Q = -u^2, vector -u e_r, t = 1/2; at u = 0 it is (0, 0, 1/2): the ideal point [ninf/2]
    def image(u):
        X, Q = lift(GA.scal(-u, ER))
        return iota(X)
    s0, X0, t0 = slots(image(F(0)))
    ok = ok and s0 == 0 and GA.is_zero(X0) and t0 == F(-1, 2)
    for uu in (F(1, 10), F(1, 100), F(3)):
        s1, X1, t1 = slots(image(uu))
        ok = ok and s1 == uu * uu and t1 == F(-1, 2) and GA.eq(X1, GA.scal(uu, ER))
    _tp_rv = (ok); assert _tp_rv is not False, "check_dying_direction_dual_norm_and_read_out"; return _tp_rv


# ---- GTG derivation (maintainer pass 2026-11-07, GTG proofs) ----
# The dual norm read off the shared GTG engine (lib/gtg.py): the PG and static gauge fields of the stored
# Schwarzschild field, hb^T(xi) = sum_a (hb(gamma_a) . xi) gamma^a for a background gradient xi (labels
# t, r, theta, phi; grad t = e^t = e_t, grad r = e^r = -e_r), and Q*(xi) = Q(hb^T(xi)).
import gtg  # noqa: E402


def hb_adjoint(fld, xi):
    """hb^T(xi) for a background vector xi (dict on e_mu): sum_a (hb(gamma_a) . xi) gamma^a."""
    out = {}
    for a in range(4):
        c = gtg.vdot(fld.hb(GA.gen(a)), xi)
        if c:
            out = GA.add(out, GA.scal(c * F(1, gtg.S13[a]), GA.gen(a)))
    return out


def check_gtg_dual_norm_of_the_dying_direction_from_the_engine():
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    premise("transport.descent-read-out-map")
    ok = True
    grad_t, grad_r = GA.gen(0), GA.scal(-1, GA.gen(1))
    for M in (F(1, 2), F(2), F(9, 2)):
        a = isqrt_frac(2 * M)
        for r in (F(1, 4), 2 * M, F(9), F(25, 16)):
            u = isqrt_frac(r)
            fld = gtg.schwarzschild_pg(M, r, F(3, 5), F(4, 5))
            xi = GA.add(GA.scal(a, grad_t), GA.scal(u, grad_r))
            k = hb_adjoint(fld, xi)
            ok = ok and GA.eq(k, GA.scal(-u, GA.gen(1))) and gtg.vdot(k, k) == -r
            s, Xv, t = slots(iota(lift(GA.scal(-u, ER))[0]))
            ok = ok and s == r and GA.eq(GA.scal(1 / s, Xv), GA.scal(-1 / r, k))
    for M, w, sn in STATIC:
        f = w * w
        r = 2 * M / (1 - f)
        a, u = isqrt_frac(2 * M), isqrt_frac(r)
        fld = gtg.schwarzschild_static(M, r, sn, isqrt_frac(1 - sn * sn))
        xi = GA.add(GA.scal(a, grad_t), GA.scal(u / f, grad_r))
        k = hb_adjoint(fld, xi)
        ok = ok and gtg.vdot(k, k) == -r
        kt = hb_adjoint(fld, grad_t)
        ok = ok and gtg.vdot(kt, kt) == 1 / f
    assert ok
    return ok
