"""mass.imported-frozen-point-tractor-connection: exact checks in Gauge Theory Gravity.

Gravitational fields (hb, Omega) on flat spacetime (GTG sign, jet engine below); the store-sign curvature
calR(B) = -R(hb(B)) from the fields, Schouten P(A) = (calR(A) - A R/6)/2, J = tr P = sum_a gamma^a . P(gamma_a),
and the Cl(2,4) tractor gauge field Omega_T(hb(gamma_c)) = Omega(hb(gamma_c)) - ninf ^ gamma_c +
n0 ^ P(gamma_c) (n0 = (e+ + e-)/2, ninf = e+ - e-), acting by the commutator product.
(1) The displayed connection: Omega_T x (sigma ninf + mu + rho n0) has the slots
    (-mu.A, rho A - sigma P(A) + Omega x mu, P(A).mu) and preserves Q.
(2) On the vacuum Einstein fields (Schwarzschild-de Sitter, flat-sliced de Sitter, Schwarzschild-anti-de
    Sitter, and Schwarzschild with Lambda = 0): P = (Lambda/6) id, J = 2 Lambda/3, the frozen point
    I = ninf + rho_I n0 with rho_I = J/4 = Lambda/6 is parallel, Q(I) = 2J/4 = Lambda/3, null exactly at
    Lambda = 0; on Reissner-Nordstrom no (1, 0, rho) is parallel.
(3) For Lambda > 0 the stabiliser {B bivector : B x I = 0} has dimension 10 and I-perp has signature
    (1,4); the scalar-part form <XY> on the stabiliser is nondegenerate (reductive). At Lambda = 0 the
    stabiliser of ninf also has dimension 10 but the form has a 4-dimensional radical (the translations).
    With the opposite Schouten sign the parallel section would be ninf - (Lambda/6) n0, of norm -Lambda/3,
    with I-perp of signature (2,3): the anti-de Sitter group, so the sign carries the de Sitter stabiliser.
(4) General n: in Cl(1,n-1) plus the plane, n = 3..6, for the constant-curvature operator calR(B) = k B the
    n-dimensional Schouten map P(a) = (calR(a) - a R/(2(n-1)))/(n-2) is (k/2) id, J = n k/2, and
    I = ninf + (J/n) n0 is annihilated by -ninf ^ A + n0 ^ P(A) for every A, with Q(I) = 2J/n.
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise

# ---- GTG engine: lib/gtg.py (jets, fields (hb, Omega), store-sign curvature, Ricci and Schouten maps, and the
# ---- Cl(2,4) tractor gauge field Omega_T; generators 0..3 as Cl(1,3), 4 = e+, 5 = e-, n0 = (e+ + e-)/2, ninf = e+ - e-)
S13 = gtg.S13
ETA = gtg.ETA
J = gtg.J
m_val = gtg.m_val
fv = GA.gen
schouten = gtg.schouten                  # P(a) = (calR(a) - a calR/6)/2 (four dimensions), a callable
S24 = gtg.S24
NI = gtg.NINF                            # ninf = e+ - e-
tractor = gtg.tractor                    # sigma ninf + mu + rho n0
slots = gtg.slots                        # (sigma, mu, rho) of V
dT_const = gtg.dT_const                  # Omega_T(hb(gamma_c)) x V for a constant tractor V


def comm6(X, Y):
    return gtg.comm(X, Y, S24)


def dot6(a, b):
    return gtg.vdot(a, b, S24)


def static_field(r0, s0, c0, fdf):
    """Static spherically symmetric field, derived metric f dt^2 - dr^2/f - r^2 dOmega^2, labels
    (t, r, theta, phi), at the point r = r0, sin(theta) = s0, cos(theta) = c0; fdf(r) returns the jets
    (f, f'). sqrt(f(r0)) must be rational. Kept on gtg pieces rather than gtg.static_field because the
    callers supply f' explicitly (gtg.static_field differentiates f and would ignore it)."""
    r = J.var(1, r0)
    f, fp = fdf(r)
    sf = f.pw(F(1, 2))
    sn, cs = gtg.sincos(2, s0, c0)
    TH = [[F(0)] * 4 for _ in range(4)]
    TH[0][0], TH[1][1], TH[2][2], TH[3][3] = sf, 1 / sf, r, r * sn
    om = gtg.omega_forms([(0, 0, 1, fp / (2 * sf)), (2, 2, 1, sf / r), (3, 3, 1, sf / r), (3, 3, 2, (cs / sn) / r)])
    return gtg.Field(TH, om)


def pg_field(r0, s0, c0, M):
    """Schwarzschild in the Painleve-Gullstrand gauge hb = 1 - beta P, beta = sqrt(2M/r)."""
    return gtg.schwarzschild_pg(M, r0, s0, c0)


ds_flat_field = gtg.de_sitter_flat       # (H, E): de Sitter in the flat slicing at e^{Ht} = E
# ---- end of engine ----


def sds(lam, r0, F0, s0, c0):
    Ms = r0 * (1 - F0 * F0 - lam * r0 * r0 / 3) / 2
    return static_field(r0, s0, c0, lambda r: (1 - 2 * Ms / r - lam * r * r / 3, 2 * Ms / (r * r) - 2 * lam * r / 3))


def einstein_fields():
    return [(sds(F(3, 4), F(1), F(1, 2), F(5, 13), F(12, 13)), F(3, 4)),
            (ds_flat_field(F(1, 2), F(3)), F(3, 4)),
            (sds(F(-3, 2), F(2), F(1), F(4, 5), F(3, 5)), F(-3, 2)),
            (pg_field(F(1, 2), F(3, 5), F(4, 5), F(1)), F(0))]


TRACTORS = [(F(2), [1, 0, 3, -1], F(-7)), (F(-1, 3), [0, 4, 1, 1], F(5, 2))]


vec4 = gtg.vec


def trace_P(P):
    return sum(ETA[a] * GA.dot(fv(a), P(fv(a)), S13) for a in range(4))


def bivectors(n):
    sq = (1,) + (-1,) * (n - 1) + (1, -1)
    return [GA.mul(GA.gen(i), GA.gen(j), sq) for i in range(n + 2) for j in range(i + 1, n + 2)], sq


def stabiliser(I, sq):
    """Basis of {B : B x I = 0}."""
    return gtg.stabiliser(I, sq)


def perp_signature(I, sq):
    N = len(sq)
    vecs = [GA.gen(i) for i in range(N)]
    rows = [[GA.dot(I, v, sq) for v in vecs]]
    ker = GA.field_kernel(rows)
    basis = [GA.add(*[GA.scal(k[i], vecs[i]) for i in range(N) if k[i]]) for k in ker]
    return GA.congruence_signature([[GA.dot(u, v, sq) for v in basis] for u in basis])


def check_displayed_connection_slots():
    premise("interior.imported-tractor-connection")
    ok = True
    for fld, lam in einstein_fields()[:2]:
        P = schouten(fld.curvature())
        for c in range(4):
            A = fv(c)
            for sig, m, rho in TRACTORS:
                mu = vec4(m)
                V = tractor(sig, mu, rho)
                dV = dT_const(fld, c, P, V)
                s1, m1, r1 = slots(dV)
                ok = ok and s1 == -GA.dot(mu, A, S13) and r1 == GA.dot(P(A), mu, S13)
                ok = ok and GA.eq(m1, GA.add(GA.scal(rho, A), GA.scal(-sig, P(A)), comm6(m_val(fld.om[c]), mu)))
                ok = ok and dot6(V, dV) == 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_displayed_connection_slots"; return _tp_rv


def check_frozen_point_parallel_with_rho_j_over_n():
    premise("interior.scale-tractor-leaves-cone")
    premise("interior.covariant-form-vacuum-equations")
    ok = True
    for fld, lam in einstein_fields():
        ok = ok and fld.torsion_free()
        P = schouten(fld.curvature())
        ok = ok and all(GA.eq(P(fv(a)), GA.scal(lam / 6, fv(a))) for a in range(4))
        Jt = trace_P(P)
        ok = ok and Jt == 2 * lam / 3
        rho = Jt / 4
        I = tractor(F(1), {}, rho)
        ok = ok and rho == lam / 6 and all(GA.is_zero(dT_const(fld, c, P, I)) for c in range(4))
        ok = ok and dot6(I, I) == 2 * Jt / 4 == lam / 3 and ((dot6(I, I) == 0) == (lam == 0))
    # Reissner-Nordstrom: no constant rho works (P is not a multiple of the identity)
    M, r0, F0 = F(1), F(3), F(1, 2)
    Q2 = r0 * r0 * (F0 * F0 - 1 + 2 * M / r0)
    rn = static_field(r0, F(4, 5), F(3, 5), lambda r: (1 - 2 * M / r + Q2 / (r * r), 2 * M / (r * r) - 2 * Q2 / (r * r * r)))
    P = schouten(rn.curvature())
    p00 = GA.dot(fv(0), P(fv(0)), S13)
    ok = ok and not all(GA.eq(P(fv(a)), GA.scal(p00, fv(a))) for a in range(4))
    # by hand for Lambda = 3/4: J = 1/2, rho_I = 1/8, Q(I) = 1/4
    fld, lam = einstein_fields()[0]
    ok = ok and trace_P(schouten(fld.curvature())) == F(1, 2)
    _tp_rv = (ok); assert _tp_rv is not False, "check_frozen_point_parallel_with_rho_j_over_n"; return _tp_rv


def check_stabiliser_de_sitter_group_and_sign():
    premise("interior.non-null-stabilisers-section-they-act")
    premise("interior.stabiliser-rotates-parabolic-reductive")
    premise("interior.sign-fixed-internally")
    ok = True
    biv, sq = bivectors(4)
    for lam in (F(3, 4), F(6)):
        I = tractor(F(1), {}, lam / 6)
        st = stabiliser(I, sq)
        ok = ok and len(st) == 10 and perp_signature(I, sq) == (1, 4, 0)
        form = [[GA.mul(X, Y, sq).get((), F(0)) for Y in st] for X in st]
        ok = ok and GA.field_rank(form) == 10
        # the opposite Schouten sign: parallel section ninf - (Lambda/6) n0, norm -Lambda/3, I-perp (2,3)
        Ibad = tractor(F(1), {}, -lam / 6)
        ok = ok and dot6(Ibad, Ibad) == -lam / 3 and perp_signature(Ibad, sq) == (2, 3, 0)
    st0 = stabiliser(NI, sq)
    form0 = [[GA.mul(X, Y, sq).get((), F(0)) for Y in st0] for X in st0]
    ok = ok and len(st0) == 10 and GA.field_rank(form0) == 6
    _tp_rv = (ok); assert _tp_rv is not False, "check_stabiliser_de_sitter_group_and_sign"; return _tp_rv


def check_general_n_rho_is_j_over_n():
    premise("interior.imported-tractor-connection")
    ok = True
    k = F(2, 7)
    for n in range(3, 7):
        sq = (1,) + (-1,) * (n - 1) + (1, -1)
        e = [GA.gen(i) for i in range(n)]
        er = [GA.scal(F(1, sq[i]), e[i]) for i in range(n)]
        n0 = GA.scal(F(1, 2), GA.add(GA.gen(n), GA.gen(n + 1)))
        ni = GA.sub(GA.gen(n), GA.gen(n + 1))

        def cm(X, Y):
            return GA.scal(F(1, 2), GA.sub(GA.mul(X, Y, sq), GA.mul(Y, X, sq)))

        def calR(B):
            return GA.scal(k, B)

        def ric(b):
            return GA.add(*[{bb: c for bb, c in cm(er[a], calR(cm(e[a], b))).items() if len(bb) == 1}
                            for a in range(n)])
        R = sum(GA.dot(er[a], ric(e[a]), sq) for a in range(n))

        def P(a):
            return GA.scal(F(1, n - 2), GA.sub(ric(a), GA.scal(R / (2 * (n - 1)), a)))
        ok = ok and R == n * (n - 1) * k
        ok = ok and all(GA.eq(P(e[a]), GA.scal(k / 2, e[a])) for a in range(n))
        Jt = sum(GA.dot(er[a], P(e[a]), sq) for a in range(n))
        ok = ok and Jt == n * k / 2
        I = GA.add(ni, GA.scal(Jt / n, n0))
        for a in range(n):
            theta = GA.add(GA.neg(cm(ni, e[a])), cm(n0, P(e[a])))
            ok = ok and GA.is_zero(cm(theta, I))
        ok = ok and GA.dot(I, I, sq) == 2 * Jt / n
    _tp_rv = (ok); assert _tp_rv is not False, "check_general_n_rho_is_j_over_n"; return _tp_rv
