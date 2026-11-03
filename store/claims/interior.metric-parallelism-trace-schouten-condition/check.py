"""interior.metric-parallelism-trace-schouten-condition: exact checks in Gauge Theory Gravity.

Gravitational fields (hb, Omega) on flat spacetime (GTG sign, jet engine below): Schwarzschild in the
static and Painleve-Gullstrand gauges, Schwarzschild-de Sitter, Schwarzschild-anti-de Sitter,
Reissner-Nordstrom (not Einstein) and flat-sliced de Sitter. For each, the store-sign curvature
calR(B) = -R(hb(B)) is computed from the fields, then Ricci calR(b) = sum_a gamma^a . calR(gamma_a ^ b),
R = sum_a gamma^a . calR(gamma_a) and the Schouten map P(A) = (calR(A) - A R/6)/2. Tractors are vectors
sigma ninf + mu + rho n0 of Cl(2,4) (generators 0..3 the physical frame, e+ and e- the added plane,
n0 = (e+ + e-)/2, ninf = e+ - e-), and the tractor gauge field along hb(gamma_c) is
Omega_T = Omega(hb(gamma_c)) - ninf ^ gamma_c + n0 ^ P(gamma_c), acting by the commutator product.
(i) For constant tractors V: V . (Omega_T x V) = 0 for every field, frame direction and sample V,
    the slots of Omega_T x V are (-mu.A, rho A - sigma P(A) + Omega x mu, P(A).mu) (the stored
    connection), the same holds for a non-symmetric P, and for a tractor field with jet slots the
    background derivative of Q(V) equals 2 V . D^T V. Control: flipping the sign of one Schouten slot
    (no longer a bivector action) breaks it.
(ii) The map Ric -> P on the ten-dimensional space of symmetric component matrices is injective (rank
    10) with inverse Ric = 2P + tr(P) eta; P = c eta forces c = R/24 and Ric = (R/4) eta; on the
    Einstein fields P = (Lambda/6) id with R = 4 Lambda; P = 0 exactly on the vacuum fields; the
    Reissner-Nordstrom field has R = 0 but P not a multiple of the identity.
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise

# ---- GTG engine: lib/gtg.py (L12 names; jets, fields (hb, Omega), store-sign curvature, Ricci and Schouten
# ---- maps, Cl(2,4) tractors with generators 0..3 spacetime, 4 = e+, 5 = e-) ----
S24, S13, ETA, J = gtg.S24, gtg.S13, gtg.ETA, gtg.J
m_add, m_d, m_val, static_field = gtg.m_add, gtg.m_d, gtg.m_val, gtg.static_field
ds_flat_field, fv, ricci, ricci_scalar = gtg.de_sitter_flat, GA.gen, gtg.ricci, gtg.ricci_scalar
schouten, tractor, slots, omega_T = gtg.schouten, gtg.tractor, gtg.slots, gtg.omega_T
dT_const = gtg.dT_const


def pg_field(r0, s0, c0, M):
    """Schwarzschild in the Painleve-Gullstrand gauge hb = 1 - beta P, beta = sqrt(2M/r)."""
    return gtg.schwarzschild_pg(M, r0, s0, c0)


def comm6(X, Y):
    return gtg.comm(X, Y, S24)


def dot6(a, b):
    return gtg.vdot(a, b, S24)


def fields():
    """(name, field, Lambda or None) at rational sample points."""
    out = []
    M = F(1)
    r0 = 2 * M / (1 - F(9, 25))
    out.append(("schw", static_field(r0, F(3, 5), F(4, 5), lambda r: 1 - 2 * M / r), F(0)))
    out.append(("pg", pg_field(F(1, 2), F(3, 5), F(4, 5), F(1)), F(0)))
    for lam, r0, F0 in ((F(3, 4), F(1), F(1, 2)), (F(-3, 2), F(2), F(1))):
        Ms = r0 * (1 - F0 * F0 - lam * r0 * r0 / 3) / 2
        out.append(("sds", static_field(r0, F(5, 13), F(12, 13),
                                        lambda r, Ms=Ms, lam=lam: 1 - 2 * Ms / r - lam * r * r / 3), lam))
    M, r0, F0 = F(1), F(3), F(1, 2)
    Q2 = r0 * r0 * (F0 * F0 - 1 + 2 * M / r0)
    out.append(("rn", static_field(r0, F(4, 5), F(3, 5),
                                   lambda r: 1 - 2 * M / r + Q2 / (r * r)),
                None))
    out.append(("ds", ds_flat_field(F(1, 2), F(3)), F(3, 4)))
    return out


TRACTORS = [(F(2), [1, 0, 3, -1], F(-7)), (F(-1, 3), [0, 4, 1, 1], F(5, 2)), (F(5), [2, -1, 0, 3], F(1, 7))]
NONSYM = [[2, 1, 0, -3], [5, -1, 4, 0], [0, -2, 5, 2], [1, 0, 7, 7]]


vec4 = gtg.vec                                       # sum c_i gamma_i


def smap(Mx):
    """A -> sum_n (sum_m Mx[m][n] A.e_m) e^n."""
    return lambda A: GA.add(*[GA.scal(sum(F(Mx[m][n]) * GA.dot(A, fv(m), S13) for m in range(4)) * ETA[n], fv(n))
                              for n in range(4)])


def check_tractor_gauge_field_preserves_tractor_metric():
    premise("interior.imported-tractor-connection")
    ok = True
    for name, fld, lam in fields():
        ok = ok and fld.torsion_free()
        P = schouten(fld.curvature())
        for Pm in (P, smap(NONSYM)):
            for c in range(4):
                A = fv(c)
                for sig, m, rho in TRACTORS:
                    mu = vec4(m)
                    V = tractor(sig, mu, rho)
                    dV = dT_const(fld, c, Pm, V)
                    ok = ok and dot6(V, dV) == 0
                    s1, m1, r1 = slots(dV)
                    om_mu = comm6(m_val(fld.om[c]), mu)
                    ok = ok and s1 == -GA.dot(mu, A, S13)
                    ok = ok and GA.eq(m1, GA.add(GA.scal(rho, A), GA.scal(-sig, Pm(A)), om_mu))
                    ok = ok and r1 == GA.dot(Pm(A), mu, S13)
                    ok = ok and GA.eq(dV, tractor(s1, m1, r1))
    # first tractor against the de Sitter Schouten (Lambda/6 = 1/8) along gamma_0 by hand: P(A).mu = 1/8
    name, fld, lam = fields()[-1]
    s1, m1, r1 = slots(dT_const(fld, 0, schouten(fld.curvature()), tractor(F(2), vec4([1, 0, 3, -1]), F(-7))))
    ok = ok and s1 == -1 and r1 == F(1, 8)
    _tp_rv = (ok); assert _tp_rv is not False, "check_tractor_gauge_field_preserves_tractor_metric"; return _tp_rv


def check_derivative_of_q_along_a_tractor_field():
    """d_a Q(V) = 2 V . D^T_a V for a tractor field with jet slots on the de Sitter and RN fields."""
    premise("interior.imported-tractor-connection")
    ok = True
    for name, fld, lam in [fs for fs in fields() if fs[0] in ("ds", "rn")]:
        P = schouten(fld.curvature())
        sig = J(F(3, 2), (1, -2, 0, 5))
        rho = J(F(-1, 4), (3, 0, 1, -1))
        mu = [J(F(1), (0, 2, -1, 1)), J(F(2), (1, 1, 0, 0)), J(F(-1, 3), (0, 0, 4, 1)), J(F(1, 2), (-2, 0, 0, 3))]
        Vj = m_add({(4,): sig + rho / 2, (5,): -sig + rho / 2}, {(a,): mu[a] for a in range(4)})
        V = m_val(Vj)
        Qj = sig * rho * 2 + sum(mu[a] * mu[a] * ETA[a] for a in range(4))
        for c in range(4):
            dV = comm6(omega_T(fld, c, P), V)
            dQ = F(0)
            for nu in range(4):
                h = fld.Hi[nu][c]
                if h:
                    dV = GA.add(dV, GA.scal(h, m_val(m_d(Vj, nu))))
                    dQ += h * Qj.g[nu]
            ok = ok and dQ == 2 * dot6(V, dV)
        ok = ok and Qj.v == F(-3, 4) + 1 - 4 - F(1, 9) - F(1, 4)
    _tp_rv = (ok); assert _tp_rv is not False, "check_derivative_of_q_along_a_tractor_field"; return _tp_rv


def check_opposite_schouten_sign_breaks_metric_preservation():
    """Control. Every Cl(2,4) bivector preserves Q under the commutator, so the control flips the sign of
    one Schouten slot only (the rho slot), leaving a slot map that is not a bivector action:
    then V . dV = -2 sigma P(A).mu, nonzero on the samples."""
    name, fld, lam = fields()[2]                                  # Schwarzschild-de Sitter, P = (Lambda/6) id
    P = schouten(fld.curvature())
    ok = True
    for c in range(4):
        A = fv(c)
        for sig, m, rho in TRACTORS:
            mu = vec4(m)
            V = tractor(sig, mu, rho)
            s1, m1, r1 = slots(dT_const(fld, c, P, V))
            bad = tractor(s1, m1, -r1)
            ok = ok and dot6(V, bad) == -2 * sig * GA.dot(P(A), mu, S13)
            ok = ok and (dot6(V, bad) != 0) == (GA.dot(A, mu, S13) != 0)
    # gamma_0 with the first tractor: P(A).mu = 1/8, sigma = 2, so V . bad = -1/2
    s1, m1, r1 = slots(dT_const(fld, 0, P, tractor(F(2), vec4([1, 0, 3, -1]), F(-7))))
    ok = ok and dot6(tractor(F(2), vec4([1, 0, 3, -1]), F(-7)), tractor(s1, m1, -r1)) == F(-1, 2)
    _tp_rv = (ok); assert _tp_rv is not False, "check_opposite_schouten_sign_breaks_metric_preservation"; return _tp_rv


def ricci_matrix(Rc):
    return [[GA.dot(fv(a), ricci(Rc, fv(b)), S13) for b in range(4)] for a in range(4)]


def sch_of(Ric):
    R = sum(ETA[a] * Ric[a][a] for a in range(4))
    return [[(Ric[a][b] - (R / 6 if a == b else 0) * ETA[a]) / 2 for b in range(4)] for a in range(4)]


SYM = [(a, b) for a in range(4) for b in range(a, 4)]


def check_trace_of_schouten_condition():
    premise("interior.imported-tractor-connection")
    ok = True
    # the map Ric -> P on symmetric component matrices: rank 10, and Ric = 2 P + tr(P) eta
    cols = []
    for (a, b) in SYM:
        Ric = [[F(1) if {i, j} == {a, b} else F(0) for j in range(4)] for i in range(4)]
        Pm = sch_of(Ric)
        cols.append([Pm[i][j] for (i, j) in SYM])
        trP = sum(ETA[i] * Pm[i][i] for i in range(4))
        ok = ok and Ric == [[2 * Pm[i][j] + (trP * ETA[i] if i == j else 0) for j in range(4)] for i in range(4)]
    ok = ok and GA.field_rank([list(r) for r in zip(*cols)]) == 10
    for name, fld, lam in fields():
        Rc = fld.curvature()
        Ric = ricci_matrix(Rc)
        R = ricci_scalar(Rc)
        Pm = sch_of(Ric)
        P = schouten(Rc)
        ok = ok and all(GA.eq(P(fv(b)), GA.add(*[GA.scal(Pm[a][b] * ETA[a], fv(a)) for a in range(4)]))
                        for b in range(4))
        c = Pm[0][0]
        is_mult = Pm == [[c * ETA[i] if i == j else F(0) for j in range(4)] for i in range(4)]
        if lam is not None:
            ok = ok and is_mult and c == lam / 6 and R == 4 * lam and c == R / 24
            ok = ok and Ric == [[R / 4 * ETA[i] if i == j else F(0) for j in range(4)] for i in range(4)]
            ok = ok and ((c == 0) == (lam == 0)) and ((c == 0) == all(v == 0 for row in Ric for v in row))
        else:
            ok = ok and not is_mult and R == 0 and any(v != 0 for row in Ric for v in row)
    _tp_rv = (ok); assert _tp_rv is not False, "check_trace_of_schouten_condition"; return _tp_rv
