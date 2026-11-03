"""interior.covariant-form-vacuum-equations: exact checks in Gauge Theory Gravity.

Gravitational fields (hb, Omega) on flat spacetime (GTG sign, jet engine below), the store-sign curvature
calR(B) = -R(hb(B)) computed from them, the Schouten map P(A) = (calR(A) - A R/6)/2, and the tractor
gauge field Omega_T(hb(gamma_c)) = Omega(hb(gamma_c)) - ninf ^ gamma_c + n0 ^ P(gamma_c) in Cl(2,4)
(generators 0..3 the physical frame, e+, e-; n0 = (e+ + e-)/2, ninf = e+ - e-). The pure-scale section
I_g = ninf is constant on the background, so D^T_a I_g = Omega_T(a) x ninf.
(1) D^T ninf = -P(gamma_c) along every frame direction (slots (0, -P, 0)), on Schwarzschild (static and
    Painleve-Gullstrand gauges, the latter also inside the horizon), Schwarzschild-de Sitter,
    Reissner-Nordstrom and flat-sliced de Sitter; Q(ninf) = 0.
(2) The equivalence: ninf is parallel exactly on the fields whose Ricci contraction vanishes (the two
    Schwarzschild gauges); on SdS and de Sitter D^T ninf = -(Lambda/6) gamma_c; on RN (R = 0, Ricci
    nonzero) it is not parallel.
(3) The weaker statement: on flat-sliced de Sitter (not Ricci-flat), the tractor field
    V = s ninf + H s gamma_0 - (Lambda/6) s n0 with s = e^{Ht} (jets with exact derivatives) is
    parallel, D^T V = a.grad V + Omega_T x V = 0 along all four directions, and null, Q(V) = 0: a parallel
    null tractor exists without the field equations.
(4) The structure algebra: the 15 bivectors of Cl(2,4) close under the commutator and their commutators
    span all 15 (so(2,4) is perfect), and each preserves Q. Covariance itself (the bundle and connection
    are scale-independent) is the content of the imported tractor Fact and is not recomputed.
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise

# ---- GTG engine: lib/gtg.py (L12 names; jets, fields (hb, Omega), store-sign curvature, Ricci and Schouten
# ---- maps, Cl(2,4) tractors with generators 0..3 spacetime, 4 = e+, 5 = e-) ----
S24, N0, NI, J = gtg.S24, gtg.N0, gtg.NI, gtg.J
m_add, m_d, m_val, static_field = gtg.m_add, gtg.m_d, gtg.m_val, gtg.static_field
ds_flat_field, fv, ricci, schouten = gtg.de_sitter_flat, GA.gen, gtg.ricci, gtg.schouten
tractor, slots, omega_T, dT_const = gtg.tractor, gtg.slots, gtg.omega_T, gtg.dT_const


def pg_field(r0, s0, c0, M):
    """Schwarzschild in the Painleve-Gullstrand gauge hb = 1 - beta P, beta = sqrt(2M/r)."""
    return gtg.schwarzschild_pg(M, r0, s0, c0)


def comm6(X, Y):
    return gtg.comm(X, Y, S24)


def dot6(a, b):
    return gtg.vdot(a, b, S24)


def fields():
    out = []
    M = F(1)
    r0 = 2 * M / (1 - F(9, 25))
    out.append(("schw", static_field(r0, F(3, 5), F(4, 5), lambda r: 1 - 2 * M / r), F(0)))
    out.append(("pg", pg_field(F(1, 2), F(3, 5), F(4, 5), F(1)), F(0)))
    out.append(("pg", pg_field(F(9, 2), F(5, 13), F(12, 13), F(1)), F(0)))
    lam, r0, F0 = F(3, 4), F(1), F(1, 2)
    Ms = r0 * (1 - F0 * F0 - lam * r0 * r0 / 3) / 2
    out.append(("sds", static_field(r0, F(5, 13), F(12, 13),
                                    lambda r: 1 - 2 * Ms / r - lam * r * r / 3),
                lam))
    M, r0, F0 = F(1), F(3), F(1, 2)
    Q2 = r0 * r0 * (F0 * F0 - 1 + 2 * M / r0)
    out.append(("rn", static_field(r0, F(4, 5), F(3, 5),
                                   lambda r: 1 - 2 * M / r + Q2 / (r * r)),
                None))
    out.append(("ds", ds_flat_field(F(1, 2), F(3)), F(3, 4)))
    return out


def check_derivative_of_the_scale_tractor_is_minus_schouten():
    premise("interior.imported-tractor-connection")
    ok = dot6(NI, NI) == 0 and dot6(NI, N0) == 1
    for name, fld, lam in fields():
        ok = ok and fld.torsion_free()
        P = schouten(fld.curvature())
        for c in range(4):
            dI = dT_const(fld, c, P, NI)
            s1, m1, r1 = slots(dI)
            ok = ok and s1 == 0 and r1 == 0 and GA.eq(m1, GA.neg(P(fv(c))))
            ok = ok and GA.eq(dI, GA.neg(P(fv(c))))
    _tp_rv = (ok); assert _tp_rv is not False, "check_derivative_of_the_scale_tractor_is_minus_schouten"; return _tp_rv


def check_parallel_iff_vacuum():
    premise("interior.metric-parallelism-trace-schouten-condition")
    premise("interior.imported-equivalence-einstein-equations")
    ok = True
    seen = {}
    for name, fld, lam in fields():
        Rc = fld.curvature()
        P = schouten(Rc)
        parallel = all(GA.is_zero(dT_const(fld, c, P, NI)) for c in range(4))
        vacuum = all(GA.is_zero(ricci(Rc, fv(a))) for a in range(4))
        ok = ok and parallel == vacuum
        seen[name] = parallel
        if name in ("sds", "ds"):
            ok = ok and all(GA.eq(dT_const(fld, c, P, NI), GA.scal(-lam / 6, fv(c))) for c in range(4))
    ok = ok and seen == {"schw": True, "pg": True, "sds": False, "rn": False, "ds": False}
    # de Sitter with Lambda = 3/4 by hand: D^T ninf along gamma_1 is -(1/8) gamma_1
    name, fld, lam = fields()[-1]
    ok = ok and dT_const(fld, 1, schouten(fld.curvature()), NI) == {(1,): F(-1, 8)}
    _tp_rv = (ok); assert _tp_rv is not False, "check_parallel_iff_vacuum"; return _tp_rv


def check_parallel_null_tractor_without_field_equations():
    """Flat-sliced de Sitter with H = 1/2 at e^{Ht} = 3: s = e^{Ht} has d_t s = H s, d_t^2 s = H^2 s."""
    premise("interior.imported-tractor-connection")
    H, E = F(1, 2), F(3)
    fld = ds_flat_field(H, E)
    lam = 3 * H * H
    Rc = fld.curvature()
    P = schouten(Rc)
    s = J(E, (H * E, 0, 0, 0))
    mu0 = J(H * E, (H * H * E, 0, 0, 0))
    rho = J(-lam / 6 * E, (-lam / 6 * H * E, 0, 0, 0))
    Vj = m_add({(4,): s + rho / 2, (5,): -s + rho / 2}, {(0,): mu0})
    V = m_val(Vj)
    ok = dot6(V, V) == 0 and not all(GA.is_zero(ricci(Rc, fv(a))) for a in range(4))
    for c in range(4):
        dV = comm6(omega_T(fld, c, P), V)
        for nu in range(4):
            h = fld.Hi[nu][c]
            if h:
                dV = GA.add(dV, GA.scal(h, m_val(m_d(Vj, nu))))
        ok = ok and GA.is_zero(dV)
    ok = ok and slots(V) == (F(3), {(0,): F(3, 2)}, F(-3, 8))
    # with the wrong rho slot (sign flipped) the field is not parallel
    Vbad = m_add({(4,): s - rho / 2, (5,): -s - rho / 2}, {(0,): mu0})
    dV = comm6(omega_T(fld, 0, P), m_val(Vbad))
    dV = GA.add(dV, GA.scal(fld.Hi[0][0], m_val(m_d(Vbad, 0))))
    ok = ok and not GA.is_zero(dV)
    _tp_rv = (ok); assert _tp_rv is not False, "check_parallel_null_tractor_without_field_equations"; return _tp_rv


def check_structure_algebra_so24():
    biv = [GA.mul(GA.gen(i), GA.gen(j), S24) for i in range(6) for j in range(i + 1, 6)]
    bl = [b for b in GA.all_blades(6) if len(b) == 2]
    ok = len(biv) == 15
    rows = []
    for X in biv:
        for Y in biv:
            Z = comm6(X, Y)
            ok = ok and all(len(b) == 2 for b in Z)
            rows.append([Z.get(b, F(0)) for b in bl])
    ok = ok and GA.rank_of_vectors(rows) == 15
    V = tractor(F(2), GA.add(GA.gen(0), GA.scal(3, GA.gen(2))), F(-1, 3))
    ok = ok and all(dot6(V, comm6(X, V)) == 0 for X in biv)
    _tp_rv = (ok); assert _tp_rv is not False, "check_structure_algebra_so24"; return _tp_rv
