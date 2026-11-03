"""interior.scale-tractor-leaves-cone: exact checks in Gauge Theory Gravity.

Gravitational fields (hb, Omega) on flat spacetime (GTG sign, jet engine below); the store-sign curvature
calR(B) = -R(hb(B)) from the fields, Schouten P(A) = (calR(A) - A R/6)/2, and the Cl(2,4) tractor gauge
field Omega_T(hb(gamma_c)) = Omega(hb(gamma_c)) - ninf ^ gamma_c + n0 ^ P(gamma_c) (n0 = (e+ + e-)/2,
ninf = e+ - e-). For a constant tractor (1, 0, rho) = ninf + rho n0, D^T = Omega_T x.
(1) Einstein fields: Schwarzschild-de Sitter (Lambda = 3/4 and 3/7), Schwarzschild-anti-de Sitter
    (Lambda = -3/2), flat-sliced de Sitter, Schwarzschild (Lambda = 0): calR(a) = Lambda a is computed,
    and I_g = ninf + (Lambda/6) n0 is parallel along every frame direction.
(2) Only that rho: the set of constant rho with (1, 0, rho) parallel is solved for (the linear condition
    rho gamma_c = P(gamma_c) for all c) and is exactly {Lambda/6}; on the Reissner-Nordstrom field
    (not Einstein) it is empty. A non-constant rho (jet with nonzero gradient) is never parallel: the
    n0 slot of D^T is the derivative of rho.
(3) Q(I_g) = 2 rho = Lambda/3: zero exactly at Lambda = 0, positive for de Sitter, negative for anti-de
    Sitter.
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise

# ---- GTG engine: lib/gtg.py (L12 names; jets, fields (hb, Omega), store-sign curvature, Ricci and Schouten
# ---- maps, Cl(2,4) tractors with generators 0..3 spacetime, 4 = e+, 5 = e-) ----
S24, N0, NI, J = gtg.S24, gtg.N0, gtg.NI, gtg.J
m_d, m_val, static_field, ds_flat_field = gtg.m_d, gtg.m_val, gtg.static_field, gtg.de_sitter_flat
fv, ricci, ricci_scalar, schouten = GA.gen, gtg.ricci, gtg.ricci_scalar, gtg.schouten
tractor, slots, omega_T, dT_const = gtg.tractor, gtg.slots, gtg.omega_T, gtg.dT_const


def pg_field(r0, s0, c0, M):
    """Schwarzschild in the Painleve-Gullstrand gauge hb = 1 - beta P, beta = sqrt(2M/r)."""
    return gtg.schwarzschild_pg(M, r0, s0, c0)


def comm6(X, Y):
    return gtg.comm(X, Y, S24)


def dot6(a, b):
    return gtg.vdot(a, b, S24)


def sds(lam, r0, F0, s0, c0):
    Ms = r0 * (1 - F0 * F0 - lam * r0 * r0 / 3) / 2
    return static_field(r0, s0, c0, lambda r: 1 - 2 * Ms / r - lam * r * r / 3)


def einstein_fields():
    """(field, Lambda) with Lambda the declared cosmological constant of the sample."""
    return [(sds(F(3, 4), F(1), F(1, 2), F(5, 13), F(12, 13)), F(3, 4)),
            (sds(F(3, 7), F(1, 2), F(4, 5), F(3, 5), F(4, 5)), F(3, 7)),
            (sds(F(-3, 2), F(2), F(1), F(4, 5), F(3, 5)), F(-3, 2)),
            (ds_flat_field(F(2, 3), F(5)), F(4, 3)),
            (pg_field(F(9, 2), F(5, 13), F(12, 13), F(1)), F(0))]


def rn_field():
    M, r0, F0 = F(1), F(3), F(1, 2)
    Q2 = r0 * r0 * (F0 * F0 - 1 + 2 * M / r0)
    return static_field(r0, F(4, 5), F(3, 5),
                        lambda r: 1 - 2 * M / r + Q2 / (r * r))


def parallel_rhos(fld, P):
    """All constant rho with Omega_T x (ninf + rho n0) = 0 for every c: solve rho gamma_c - P(gamma_c) = 0,
    linear in rho; returns a list (empty, one value, or ['all'])."""
    rows, rhs = [], []
    for c in range(4):
        x = dT_const(fld, c, P, NI)                      # the rho-independent part
        y = dT_const(fld, c, P, N0)                      # the coefficient of rho
        for b in set(x) | set(y):
            rows.append(y.get(b, F(0)))
            rhs.append(-x.get(b, F(0)))
    nz = [(a, b) for a, b in zip(rows, rhs) if a != 0]
    if any(a == 0 and b != 0 for a, b in zip(rows, rhs)):
        return []
    if not nz:
        return ["all"]
    cand = nz[0][1] / nz[0][0]
    return [cand] if all(a * cand == b for a, b in nz) else []


def check_einstein_scale_tractor_is_parallel():
    premise("interior.imported-tractor-connection")
    premise("interior.metric-parallelism-trace-schouten-condition")
    ok = True
    for fld, lam in einstein_fields():
        ok = ok and fld.torsion_free()
        Rc = fld.curvature()
        ok = ok and all(GA.eq(ricci(Rc, fv(a)), GA.scal(lam, fv(a))) for a in range(4))
        P = schouten(Rc)
        I = tractor(F(1), {}, lam / 6)
        ok = ok and all(GA.is_zero(dT_const(fld, c, P, I)) for c in range(4))
    _tp_rv = (ok); assert _tp_rv is not False, "check_einstein_scale_tractor_is_parallel"; return _tp_rv


def check_only_rho_lambda_over_six_and_only_einstein():
    premise("interior.imported-tractor-connection")
    premise("interior.metric-parallelism-trace-schouten-condition")
    ok = True
    for fld, lam in einstein_fields():
        P = schouten(fld.curvature())
        ok = ok and parallel_rhos(fld, P) == [lam / 6]
        ok = ok and not all(GA.is_zero(dT_const(fld, c, P, tractor(F(1), {}, lam / 6 + F(1, 10)))) for c in range(4))
    fld = rn_field()
    Rc = fld.curvature()
    ok = ok and parallel_rhos(fld, schouten(Rc)) == [] and ricci_scalar(Rc) == 0
    # a non-constant rho: (1, 0, rho(x)) with d rho != 0 along gamma_0 on de Sitter
    fld, lam = einstein_fields()[3]
    P = schouten(fld.curvature())
    rho = J(lam / 6, (F(1, 3), 0, 0, 0))
    Vj = {(4,): J(1) + rho / 2, (5,): J(-1) + rho / 2}
    dV = comm6(omega_T(fld, 0, P), m_val(Vj))
    dV = GA.add(dV, GA.scal(fld.Hi[0][0], m_val(m_d(Vj, 0))))
    s1, m1, r1 = slots(dV)
    ok = ok and s1 == 0 and GA.is_zero(m1) and r1 == F(1, 3)
    # by hand: de Sitter with H = 2/3 has Lambda = 3 H^2 = 4/3 and rho = 2/9
    ok = ok and parallel_rhos(fld, P) == [F(2, 9)]
    _tp_rv = (ok); assert _tp_rv is not False, "check_only_rho_lambda_over_six_and_only_einstein"; return _tp_rv


def check_norm_is_lambda_over_three():
    ok = True
    signs = []
    for fld, lam in einstein_fields():
        I = tractor(F(1), {}, lam / 6)
        q = dot6(I, I)
        ok = ok and q == lam / 3
        signs.append((q > 0) - (q < 0))
    ok = ok and signs == [1, 1, -1, 1, 0]
    ok = ok and dot6(tractor(F(1), {}, F(1, 8)), tractor(F(1), {}, F(1, 8))) == F(1, 4)
    _tp_rv = (ok); assert _tp_rv is not False, "check_norm_is_lambda_over_three"; return _tp_rv
