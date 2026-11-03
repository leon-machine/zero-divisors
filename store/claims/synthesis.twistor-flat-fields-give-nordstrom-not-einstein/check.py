"""Exact checks: on the fields where twistor transport is path independent (the domain of the twistor
attachment) Einstein's equations hold only for matter of uniform rest density, while Nordstrom's trace
equation is solvable for every trace.

Conventions of lib/gtg.py: background Cl(1,3), signature (+,-,-,-); a field is given by its coframe,
hb^{-1}(e_mu) = sum_a TH[a][mu] gamma_a; store curvature calR(B) = -R(hb(B)); Schouten
P(a) = (calR(a) - a calR/6)/2; Weyl W(a ^ b) = calR(a ^ b) - P(a) ^ b - a ^ P(b); the tractor gauge field
Omega_T(a) = Omega(a) - ninf ^ hb^{-1}(a) + n0 ^ P(hb^{-1}(a)) in Cl(2,4) (gtg.tractor_curvature: the
covariant tractor field strength on the frame planes; Lorentz block -W, soldering block the torsion,
n0 block the Cotton term).

(1) Conformally flat fields hb^{-1}(a) = phi a, phi a rational polynomial, at rational points: every block of
    the tractor field strength vanishes (so local twistor transport, the tractor connection on the conformal
    spinor space, is flat); on a field that is not conformally flat the tractor field strength is nonzero
    and its spacetime block is -W.
(2) The curl identity behind clause (ii): with S_bc = w u_b u_c - (rho/3) g_bc (the Einstein Schouten
    tensor of a perfect fluid up to the factor -4 pi G and the Lambda term, which has zero curl), for
    arbitrary polynomial jets rho, p and a unit u (rational parametrisation), at a point of the flat field,
    u^b u^c (d_a S_bc - d_b S_ac) = d_a f - u_a (u.d f) - w (u.d u)_a with f = 2 rho/3 + p, w = rho + p.
    Static dust of nonuniform density (u = e_t, p = 0) has nonzero curl.
(3) Nordstrom's trace equation: calR = 6 box(phi)/phi^3 on hb^{-1}(a) = phi a (box = d_t^2 - laplacian),
    and for a nonuniform, time-dependent polynomial trace tau the Cauchy-Kovalevskaya recursion gives phi to
    order 4 with calR + 6 kappa tau = 0 to curvature-jet order 2 (kappa = 4 pi G carried as a rational
    formal value); the tractor field strength of that field vanishes.
(4) Einstein vacuum on the attachment domain: the conformally flat de Sitter field phi = 1/(1 - Lambda Q(x)/12)
    has calR(B) = (Lambda/3) B on every frame plane (constant curvature), as Weyl = 0 with P = (Lambda/6) id
    forces.
"""
from fractions import Fraction as F

import GA
import gtg
from gtg import Jet
from tp_premise import premise

SQ = GA.sig(1, 3)
ETA = [1, -1, -1, -1]


def _zero():
    return Jet.const(0)


def _conf_flat(phi_fn):
    def hbinv(X):
        p = phi_fn(X)
        return [[p if a == mu else _zero() for a in range(4)] for mu in range(4)]
    return hbinv


def phi_a(X):
    t, x, y, z = X
    return 1 + x * F(1, 3) + t * y * F(1, 5) + z * z * F(1, 7) - t * t * F(1, 11) + x * y * z * F(1, 13)


def phi_b(X):
    t, x, y, z = X
    return 2 - y * F(1, 4) + t * x * F(2, 9) + x * x * z * F(1, 6)


def not_conf_flat(X):
    t, x, y, z = X
    p = phi_a(X)
    q = 1 + y * y * F(1, 4) + x * t * F(1, 6)
    rows = []
    for mu in range(4):
        rows.append([(p * q if mu == 1 else p) if a == mu else _zero() for a in range(4)])
    return rows


def _all_zero(op):
    return all(v == {} for v in op.values())


def _spacetime_part(x):
    return {b: c for b, c in x.items() if all(i < 4 for i in b)}


def check_attachment_domain_is_tractor_flat():
    """(1) conformally flat fields: tractor field strength zero in every block; control: not zero, block -W."""
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    premise("correspondence.imported-tractor-connection-local-twistor-transport")
    premise("correspondence.imported-weyls-theorem")
    pts = [[F(1, 2), F(1, 3), F(-1, 4), F(1, 5)], [F(-2, 7), F(3, 5), F(1, 9), F(-1, 3)]]
    n_flat = 0
    for fn in (phi_a, phi_b):
        for x0 in pts:
            fld = gtg.field_from_hbinv(_conf_flat(fn), x0, order=2)
            R = fld.curvature()
            assert _all_zero(gtg.weyl_op(R))
            assert gtg.ricci_scalar(R) != 0          # a nonvanishing gravitational field
            TC = gtg.tractor_curvature(fld)
            assert _all_zero(TC)
            if n_flat == 0:                                  # pinned anchor
                assert gtg.ricci_scalar(R) == F(-16409024888256000000, 7122117076515531271)
            n_flat += 1
    assert n_flat == 4
    # control: a field that is not conformally flat
    fld = gtg.field_from_hbinv(not_conf_flat, pts[0], order=2)
    R = fld.curvature()
    W = gtg.weyl_op(R)
    TC = gtg.tractor_curvature(fld)
    assert not _all_zero(W) and not _all_zero(TC)
    assert sum(1 for v in TC.values() if v) == 6
    assert W[(0, 1)] == {(0, 1): F(155831195520000, 2224746562216681)}   # pinned anchor
    for k in W:
        assert _spacetime_part(TC[k]) == gtg.m_neg(W[k])
    return True


def _unit_u(n):
    """u = ((1 + N), 2 n) / (1 - N), N = |n|^2: Q(u) = 1 exactly."""
    N = n[0] * n[0] + n[1] * n[1] + n[2] * n[2]
    den = 1 - N
    return [(1 + N) / den] + [2 * n[i] / den for i in range(3)]


def _curl_contraction(rho, p, u):
    """u^b u^c (d_a S_bc - d_b S_ac) for S_bc = w u_b u_c - (rho/3) g_bc, flat field, index form."""
    w = rho + p
    ul = [ETA[i] * u[i] for i in range(4)]                  # lowered components
    S = [[w * ul[b] * ul[c] - (rho * F(1, 3)) * ETA[b] * (1 if b == c else 0) for c in range(4)]
         for b in range(4)]
    out = []
    for a in range(4):
        acc = Jet.const(0)
        for b in range(4):
            for c in range(4):
                acc = acc + u[b] * u[c] * (S[b][c].d(a) - S[a][c].d(b))
        out.append(acc)
    return out


def _predicted(rho, p, u):
    f = rho * F(2, 3) + p
    w = rho + p
    ul = [ETA[i] * u[i] for i in range(4)]
    udf = sum((u[b] * f.d(b) for b in range(4)), Jet.const(0))
    acc = [sum((u[b] * ul[a].d(b) for b in range(4)), Jet.const(0)) for a in range(4)]
    return [f.d(a) - ul[a] * udf - w * acc[a] for a in range(4)]


def check_curl_identity_forces_uniform_rest_density():
    """(2) the contracted curl identity for a perfect fluid, and nonzero curl for nonuniform static dust."""
    premise("synthesis.imported-gtg-dictionary")
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    x0 = [F(1, 3), F(-1, 2), F(1, 4), F(2, 5)]
    X = [Jet.var(i, x0[i], 4, 2) for i in range(4)]
    t, x, y, z = X
    cases = [
        (1 + x * F(1, 2) + t * y * F(1, 3), x * z * F(1, 7) + t * F(1, 5),
         [t * F(1, 9) + x * F(1, 11), y * F(1, 6), z * x * F(1, 8)]),
        (3 - y * y * F(1, 5) + t * x, F(1, 4) + z * F(1, 3),
         [x * F(1, 7), t * z * F(1, 5) + y * F(1, 10), x * F(-1, 6)]),
    ]
    for rho, p, n in cases:
        u = _unit_u(n)
        q = sum((ETA[i] * u[i] * u[i] for i in range(4)), Jet.const(0))
        assert (q - 1).trunc(1) == Jet.const(0).trunc(1)
        lhs = _curl_contraction(rho, p, u)
        rhs = _predicted(rho, p, u)
        for a in range(4):
            assert (lhs[a] - rhs[a]).v == 0
        assert any(lhs[a].v != 0 for a in range(4))
        # with the projected conservation law E_a = w (u.d u)_a - (d_a p - u_a (u.d p)) added, the
        # contraction is (2/3) times the rest-space gradient of rho
        w = rho + p
        ul = [ETA[i] * u[i] for i in range(4)]
        for a in range(4):
            acc = sum((u[b] * ul[a].d(b) for b in range(4)), Jet.const(0))
            udp = sum((u[b] * p.d(b) for b in range(4)), Jet.const(0))
            udr = sum((u[b] * rho.d(b) for b in range(4)), Jet.const(0))
            euler = w * acc - (p.d(a) - ul[a] * udp)
            assert (lhs[a] + euler).v == (F(2, 3) * (rho.d(a) - ul[a] * udr)).v
    # static dust of nonuniform density: u = e_t, p = 0; the curl's x component is (2/3) d_x rho
    rho = 1 + x * F(1, 2) + y * y * F(1, 3)
    u = [Jet.const(1), Jet.const(0), Jet.const(0), Jet.const(0)]
    cur = _curl_contraction(rho, Jet.const(0), u)
    assert cur[1].v == F(2, 3) * rho.d(1).v and cur[1].v != 0
    assert cur[2].v == F(2, 3) * rho.d(2).v and cur[2].v != 0
    assert cur[0].v == 0
    return True


def _poly_eval(coeffs, X):
    acc = Jet.const(0)
    for e, c in coeffs.items():
        term = Jet.const(c)
        for i in range(4):
            for _ in range(e[i]):
                term = term * X[i]
        acc = acc + term
    return acc


def _pmul(a, b, N):
    out = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = tuple(i + j for i, j in zip(e1, e2))
            if sum(e) <= N:
                out[e] = out.get(e, F(0)) + c1 * c2
    return {e: c for e, c in out.items() if c != 0}


def _solve_trace_equation(tau, data0, data1, kappa, N):
    """Polynomial phi (about 0, total order N) with box(phi) = -kappa tau phi^3 to order N - 2, from Cauchy
    data phi(0, x) = data0, d_t phi(0, x) = data1 (box = d_t^2 - d_x^2 - d_y^2 - d_z^2)."""
    phi = dict(data0)
    for e, c in data1.items():
        phi[(1,) + e[1:]] = c
    for et in range(0, N - 1):
        cube = _pmul(_pmul(phi, phi, N), phi, N)
        src = _pmul(tau, cube, N)
        for e in [k for k in _monomials(N - 2) if k[0] == et]:
            lap = F(0)
            for i in (1, 2, 3):
                f = list(e)
                f[i] += 2
                lap += (e[i] + 2) * (e[i] + 1) * phi.get(tuple(f), F(0))
            val = lap - kappa * src.get(e, F(0))
            f = list(e)
            f[0] += 2
            phi[tuple(f)] = val / ((e[0] + 2) * (e[0] + 1))
    return {e: c for e, c in phi.items() if c != 0}


def _monomials(N):
    out = []
    for a in range(N + 1):
        for b in range(N + 1 - a):
            for c in range(N + 1 - a - b):
                for d in range(N + 1 - a - b - c):
                    out.append((a, b, c, d))
    return out


def check_nordstrom_trace_equation_solvable_for_any_trace():
    """(3) calR = 6 box(phi)/phi^3, and the trace equation solved order by order for a nonuniform trace."""
    premise("synthesis.imported-gtg-dictionary")
    premise("correspondence.imported-weyls-theorem")
    # calR = 6 box(phi)/phi^3 at two points of two conformally flat fields
    for fn, x0 in ((phi_a, [F(1, 2), F(1, 3), F(-1, 4), F(1, 5)]), (phi_b, [F(1, 5), F(-1, 3), F(1, 2), F(1, 7)])):
        fld = gtg.field_from_hbinv(_conf_flat(fn), x0, order=1)
        X = [Jet.var(i, x0[i], 4, 3) for i in range(4)]
        p = fn(X)
        box = p.d(0).d(0) - p.d(1).d(1) - p.d(2).d(2) - p.d(3).d(3)
        assert gtg.ricci_scalar(fld.curvature()) == 6 * box.v / p.v ** 3
    kappa = F(1, 2)
    N = 4
    tau = {(0, 0, 0, 0): F(1), (0, 1, 0, 0): F(1, 3), (0, 0, 1, 1): F(-1, 4), (1, 0, 0, 0): F(1, 5),
           (0, 2, 0, 0): F(1, 6)}
    data0 = {(0, 0, 0, 0): F(1), (0, 1, 0, 0): F(1, 7), (0, 0, 0, 2): F(-1, 9)}
    data1 = {(0, 0, 1, 0): F(1, 8)}
    phi = _solve_trace_equation(tau, data0, data1, kappa, N)
    assert phi[(2, 0, 0, 0)] == F(-13, 36) and phi[(3, 0, 0, 0)] == F(-1, 60)   # pinned anchors
    x0 = [F(0), F(0), F(0), F(0)]
    fld = gtg.field_from_hbinv(_conf_flat(lambda X: _poly_eval(phi, X)), x0, order=3)
    Rj = fld.curvature_jet()
    scal = gtg.ricci_scalar(Rj)
    X = [Jet.var(i, x0[i], 4, 2) for i in range(4)]
    resid = scal + 6 * kappa * _poly_eval(tau, X)
    for e in _monomials(2):
        assert resid.coeff(e) == 0
    assert scal.v == -3 and scal.coeff((0, 1, 0, 0)) == -1   # the field follows a nonuniform trace
    # control: the same phi does not solve the equation for a different trace
    tau2 = dict(tau)
    tau2[(0, 1, 0, 0)] = F(1, 2)
    resid2 = scal + 6 * kappa * _poly_eval(tau2, X)
    assert any(resid2.coeff(e) != 0 for e in _monomials(2))
    # the Nordstrom field is in the attachment domain: tractor field strength zero
    fld2 = gtg.field_from_hbinv(_conf_flat(lambda X: _poly_eval(phi, X)), [F(1, 10), F(1, 9), F(0), F(-1, 8)], order=2)
    assert _all_zero(gtg.tractor_curvature(fld2))
    return True


def check_einstein_vacuum_on_attachment_domain_is_constant_curvature():
    """(4) conformally flat de Sitter: calR(B) = (Lambda/3) B on every frame plane."""
    premise("synthesis.imported-gtg-dictionary")
    premise("correspondence.imported-weyls-theorem")
    pinned = [F(14400, 14981), F(19600, 20921), F(36000, 35419), F(49000, 47679)]
    k = 0
    for lam in (F(3), F(-6, 5)):
        def phi(X, lam=lam):
            Qx = X[0] * X[0] - X[1] * X[1] - X[2] * X[2] - X[3] * X[3]
            return 1 / (1 - lam * Qx * F(1, 12))
        for x0 in ([F(1, 5), F(1, 3), F(-1, 4), F(1, 6)], [F(-1, 7), F(1, 2), F(1, 5), F(0)]):
            fld = gtg.field_from_hbinv(_conf_flat(phi), x0, order=1)
            R = fld.curvature()
            assert _all_zero(gtg.weyl_op(R))
            for (a, b), v in R.items():
                assert v == {(a, b): lam * F(1, 3)}
            assert gtg.ricci_scalar(R) == 4 * lam
            assert fld.TH[0][0].v == pinned[k]
            k += 1
    assert k == 4
    return True
