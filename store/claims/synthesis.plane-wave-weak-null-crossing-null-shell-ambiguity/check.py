"""synthesis.plane-wave-weak-null-crossing-impulsive-ambiguity: exact checks.

Metrics on coordinates (u, v, x, y) whose components depend on one coordinate only (index 0), written as
rational functions (GA.RF) of a parameter t with a known du/dt. Curvature with
    Gamma^a_bc = 1/2 g^ad (d_b g_dc + d_c g_db - d_d g_bc),
    R^a_bcd = d_c Gamma^a_db - d_d Gamma^a_cb + Gamma^a_ce Gamma^e_db - Gamma^a_de Gamma^e_cb,
    Ric_bd = R^a_bad.
The store's convention (Ric = Lambda g for de Sitter, Lambda > 0, signature (1,3)) is calibrated on de
Sitter space in conformal time: the formula above gives Ric = -3 H^2 g there, so Ric_store = -Ric_formula,
and the store's Schouten tensor is P = 1/2 (Ric_store - R_store g / 6).

  check_store_sign:       de Sitter calibration (formula Ric = -3H^2 g at H = 2).
  check_rosen_schouten:   for g = 2 du dv - a^2 (dx^2 + dy^2), with a = 1 + t, u = -t^2 (the model of
                          the left side), the only nonzero Schouten component is P_uu = a_uu / a, the
                          Christoffel symbols Gamma^u_bc vanish (du is parallel), every Christoffel symbol
                          is a multiple of a_u, and y = a solves the removal equation y_uu = P_uu y;
                          the same for a generic rational a(u) (t = u).
  check_flat_scales:      a^{-2} g (a = 1 + t, u = -t^2) and Omega^2 eta with Omega = 1/(1 + c w)
                          (eta = 2 dw dv - dx^2 - dy^2, c = 3) have vanishing Riemann tensor; for the
                          scale phi^{-2} eta the formula Ric_ww equals 2 phi_ww / phi, so P_store,ww = -phi_ww / phi (the impulsive
                          coefficient), checked for phi = 1 + 3w + 5w^2; the Wronskian identity
                          a (a w)_u - a_u (a w) = a^2 w_u for a sample rational w.
  check_model_integrability: in the model a = 1 + t, u = -t^2 near t = 0: |a_u| du and |u| |S| du are
                          bounded in t (finite integrals), a_u^2 du and |S| du have a pole at t = 0 (divergent).
"""
from fractions import Fraction as F
import GA
from GA import RF
from tp_premise import premise


def _metric_curvature(g, dudt):
    """g: 4x4 list of RF in t (components depend on coordinate 0 only); dudt: RF.
    Returns (ginv, Gamma, Riemann, Ricci) with derivatives along coordinate 0 only."""
    n = 4
    zero = RF.const(0)

    def d0(f):
        return f.deriv() / dudt

    M = [[g[i][j] for j in range(n)] for i in range(n)]
    ginv = GA.rf_mat_inverse(M)
    dg = [[[d0(g[i][j]) if k == 0 else zero for k in range(n)] for j in range(n)] for i in range(n)]
    Gam = [[[zero] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                s = zero
                for d in range(n):
                    if ginv[a][d].is_zero():
                        continue
                    term = dg[d][c][b] + dg[d][b][c] - dg[b][c][d]
                    s = s + ginv[a][d] * term
                Gam[a][b][c] = s * RF.const(F(1, 2))
    dGam = [[[[d0(Gam[a][b][c]) if k == 0 else zero for k in range(n)] for c in range(n)]
             for b in range(n)] for a in range(n)]
    Riem = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    s = dGam[a][d][b][c] - dGam[a][c][b][d]
                    for e in range(n):
                        s = s + Gam[a][c][e] * Gam[e][d][b] - Gam[a][d][e] * Gam[e][c][b]
                    Riem[(a, b, c, d)] = s
    Ric = [[zero] * n for _ in range(n)]
    for b in range(n):
        for d in range(n):
            s = zero
            for a in range(n):
                s = s + Riem[(a, b, a, d)]
            Ric[b][d] = s
    return ginv, Gam, Riem, Ric


def _store_schouten(g, dudt):
    ginv, Gam, Riem, Ric = _metric_curvature(g, dudt)
    n = 4
    Rs = [[-Ric[i][j] for j in range(n)] for i in range(n)]          # store sign
    R = RF.const(0)
    for i in range(n):
        for j in range(n):
            R = R + ginv[i][j] * Rs[i][j]
    P = [[(Rs[i][j] - R * g[i][j] * RF.const(F(1, 6))) * RF.const(F(1, 2)) for j in range(n)]
         for i in range(n)]
    return P, R, Gam, Riem


def _rosen(a):
    z = RF.const(0)
    one = RF.const(1)
    return [[z, one, z, z], [one, z, z, z], [z, z, -(a * a), z], [z, z, z, -(a * a)]]


def check_store_sign():
    premise("interior.imported-tractor-connection")
    H = RF.const(2)
    eta = RF.var()
    conf = RF.const(1) / (H * H * eta * eta)
    z = RF.const(0)
    g = [[conf, z, z, z], [z, -conf, z, z], [z, z, -conf, z], [z, z, z, -conf]]
    _, _, _, Ric = _metric_curvature(g, RF.const(1))
    for i in range(4):
        for j in range(4):
            assert Ric[i][j].eqrf(RF.const(-3) * H * H * g[i][j])
    return True


def check_rosen_schouten():
    premise("interior.imported-tractor-connection")
    premise("synthesis.tractor-transport-weak-null-crossing")
    t = RF.var()
    cases = [(RF.const(1) + t, RF.const(-2) * t),                          # a = 1 + t, u = -t^2
             (RF([F(2), F(1), F(0), F(3)], [F(1), F(1)]), RF.const(1))]   # generic rational a(u), t = u
    for a, dudt in cases:
        g = _rosen(a)
        P, R, Gam, _ = _store_schouten(g, dudt)
        a_u = a.deriv() / dudt
        a_uu = a_u.deriv() / dudt
        S = a_uu / a
        assert R.is_zero()
        for i in range(4):
            for j in range(4):
                if (i, j) == (0, 0):
                    assert P[i][j].eqrf(S)
                else:
                    assert P[i][j].is_zero()
        for b in range(4):
            for c in range(4):
                assert Gam[0][b][c].is_zero()
        # every nonzero Christoffel symbol is a_u / a or a a_u (up to index symmetry)
        for i in range(4):
            for b in range(4):
                for c in range(4):
                    G_ = Gam[i][b][c]
                    assert G_.is_zero() or G_.eqrf(a_u / a) or G_.eqrf(a * a_u)
        assert Gam[2][0][2].eqrf(a_u / a)
        assert Gam[1][2][2].eqrf(a * a_u)
        # removal equation y_uu = S y for y = a
        y = a
        assert ((y.deriv() / dudt).deriv() / dudt).eqrf(S * y)
    return True


PHI = RF([F(1), F(3), F(5)])
A_GEN = RF([F(2), F(1), F(0), F(3)], [F(1), F(1)])
W_GEN = RF([F(1), F(-4), F(7)], [F(3), F(0), F(1)])


def _conformal_null(phi):
    """phi^{-2} eta with eta = 2 dw dv - dx^2 - dy^2, phi a rational function of w."""
    z = RF.const(0)
    O2 = RF.const(1) / (phi * phi)
    return [[z, O2, z, z], [O2, z, z, z], [z, z, -O2, z], [z, z, z, -O2]]


def check_flat_scales():
    premise("synthesis.tractor-transport-weak-null-crossing")
    t = RF.var()
    a = RF.const(1) + t
    dudt = RF.const(-2) * t
    ainv2 = RF.const(1) / (a * a)
    g = _rosen(a)
    gh = [[g[i][j] * ainv2 for j in range(4)] for i in range(4)]
    _, _, Riem, _ = _metric_curvature(gh, dudt)
    assert all(v.is_zero() for v in Riem.values())
    _, _, Riem0, _ = _metric_curvature(g, dudt)          # g itself is not flat
    assert not all(v.is_zero() for v in Riem0.values())
    w = RF.var()
    one = RF.const(1)
    _, _, Riem2, _ = _metric_curvature(_conformal_null(one + RF.const(3) * w), one)
    assert all(v.is_zero() for v in Riem2.values())
    _, _, _, Ricp = _metric_curvature(_conformal_null(PHI), one)
    assert Ricp[0][0].eqrf(RF.const(2) * PHI.deriv().deriv() / PHI)
    assert Ricp[0][0].eqrf(RF.const(20) / PHI)
    for i in range(4):
        for j in range(4):
            if (i, j) != (0, 0):
                assert Ricp[i][j].is_zero()
    lhs = A_GEN * (A_GEN * W_GEN).deriv() - A_GEN.deriv() * (A_GEN * W_GEN)
    assert lhs.eqrf(A_GEN * A_GEN * W_GEN.deriv())
    return True


def _ord0(r):
    """order of a rational function at t = 0."""
    def low(p):
        return next(i for i, x in enumerate(p) if x != 0)
    return low(r.num) - low(r.den)


def check_model_integrability():
    premise("synthesis.tractor-transport-weak-null-crossing")
    t = RF.var()
    a = RF.const(1) + t
    dudt = RF.const(-2) * t
    u = RF.const(-1) * t * t
    a_u = a.deriv() / dudt
    S = (a_u.deriv() / dudt) / a
    assert _ord0(a_u * dudt) >= 0              # int |a_u| du finite
    assert _ord0(a_u * a_u * dudt) == -1       # int a_u^2 du diverges (log)
    assert _ord0(S * dudt) == -2               # int |S| du diverges
    assert _ord0(u * S * dudt) >= 0            # Tipler: int |u| |S| du finite
    # S has a fixed sign near t = 0: S = -1/(4 t^3 (1 + t))
    assert S.eqrf(RF.const(-1) / (RF.const(4) * t * t * t * a))
    return True


if __name__ == "__main__":
    for f in (check_store_sign, check_rosen_schouten, check_flat_scales, check_model_integrability):
        print(f.__name__, f())
