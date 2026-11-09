"""synthesis.horizon-channels-of-scalar-and-dirac-fields-are-two-dimensional: exact checks.

The Schwarzschild field in the static gauge of Gauge Theory Gravity (coframe sqrt f dt, dr/sqrt f, r dtheta,
r sin theta dphi; rotation-gauge field from the stored connection forms; gtg.static_field), evaluated with jets at
rational points where f = 1 - 2M/r is a fourth power. Checks:
  (1) the Dirac channel reduction: for a generic even multivector field Phi,
      r f^{3/4} D(r^{-1} f^{-1/4} Phi) = (gamma^0 d_t + gamma^1 d_{r*}) Phi + (sqrt f / r) K Phi,
      K = gamma^2 (d_theta + cot theta / 2) + gamma^3 (1/sin theta) d_phi, D the GTG spinor derivative, at two
      points; the field is torsion-free and its Omega has the stored values;
  (2) T = gamma^0 gamma^1 K commutes with A = gamma^0 d_t + gamma^1 d_{r*} (second-order jets), gamma^0 gamma^1
      squares to 1; the squared channel operator is d_t^2 - d_{r*}^2 + lambda^2 W^2 + lambda (d_{r*} W) gamma^0,
      W = sqrt f / r; the free two-dimensional equation is solved by chiral movers;
  (3) the scalar channel: for phi = u(t,r) Y(theta,phi) / r with Y a spherical harmonic (l = 1, 2), the GTG
      divergence of the gradient gives r f (box + mu^2) phi / Y = d_t^2 u - d_{r*}^2 u + V u with
      V = f (l(l+1)/r^2 + 2M/r^3 + mu^2), at the jet point;
  (4) the horizon orders: V/f and l(l+1)/r^2 + 2M/r^3 + mu^2 regular and nonzero at r = 2M; the Dirac
      potentials' sqrt f part (d_{r*} W)/sqrt f = (3M - r)/r^3 is 1/(8M^2) at r = 2M, so V_+- is of exact order
      sqrt f there; and (f' - 2 kappa)/f is regular at r = 2M with kappa = 1/(4M), so f = C e^{2 kappa r*} with C
      regular: sqrt f decays as e^{kappa r*}, f as e^{2 kappa r*};
  (5) the Maxwell channels: for the odd-parity potential A = psi(t,r) (dY/dphi / sin theta dtheta
      - sin theta dY/dtheta dphi) (l = 1, 2), F = D ^ A satisfies D ^ F = 0, D . A = 0 and
      D . F = (1/f) (d_t^2 psi - d_{r*}^2 psi + f l(l+1) psi / r^2) A / psi at the jet point, and the dual
      I F (the even parity) has D(IF) = -I DF.
"""
from fractions import Fraction as F
import GA
import gtg
from gtg import Jet, m_add, m_scal, m_mul, m_d, m_val, er, S13
from GA import RF
from tp_premise import premise

EVENS = [(), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2, 3)]
COEF = [1, 2, -1, 3, 5, -2, 4, 1]
POINTS = [(F(3), F(1, 2), F(3, 5), F(4, 5), F(5, 13), F(12, 13)),
          (F(5), F(2, 3), F(4, 5), F(3, 5), F(8, 17), F(15, 17))]
U_COEF = (1, 2, 3, -1, 5, 7)            # u = c0 + c1 T + c2 R + c3 T^2 + c4 T R + c5 R^2
MU2 = F(1, 9)


def setup(r0, w, s0, c0, order=3):
    M = gtg.mass_for_root(r0, w * w)                  # f(r0) = w^4
    f = gtg.f_static(M)
    fld = gtg.static_field(r0, s0, c0, f, order=order)
    t = Jet.var(0, F(0), 4, order)
    r = Jet.var(1, r0, 4, order)
    th = Jet.var(2, F(0), 4, order)
    ph = Jet.var(3, F(0), 4, order)
    return M, f, fld, t, r, th, ph


def generic_phi(t, r, th, ph, r0):
    R = r - r0
    out = {}
    for k, b in enumerate(EVENS):
        c = COEF[k]
        out[b] = (c + (k + 1) * t + (2 * k - 3) * R + (k - 2) * th + (3 - k) * ph + (k % 3) * t * R
                  + (k - 1) * R * th + 2 * th * ph - k * R * R + (k - 4) * t * t + (2 - k) * th * th)
    return out


def dirac(fld, psi):
    Hi = fld.hb_matrix()
    out = {}
    for c in range(4):
        der = {}
        for mu in range(4):
            if Hi[mu][c]:
                der = m_add(der, m_scal(Hi[mu][c], m_d(psi, mu)))
        out = m_add(out, m_mul(er(c), m_add(der, m_scal(F(1, 2), m_mul(fld.om[c], psi)))))
    return out


def K_op(Phi, cot, isin):
    """gamma^2 (d_theta + cot/2) + gamma^3 (1/sin) d_phi, coefficients as jets."""
    a = m_add(m_d(Phi, 2), m_scal(cot * F(1, 2), Phi))
    b = m_scal(isin, m_d(Phi, 3))
    return m_add(m_mul(er(2), a), m_mul(er(3), b))


def A_op(Phi, fj):
    return m_add(m_mul(er(0), m_d(Phi, 0)), m_mul(er(1), m_scal(fj, m_d(Phi, 1))))


def check_dirac_channel_reduction():
    premise("pairing.imported-schwarzschild-connection-curvature")
    expected_M = [F(45, 32), F(325, 162)]
    expected_om = [
        [{(0, 1): F(-5, 8)}, {}, {(1, 2): F(1, 12)}, {(1, 3): F(1, 12), (2, 3): F(4, 9)}],
        [{(0, 1): F(-13, 72)}, {}, {(1, 2): F(4, 45)}, {(1, 3): F(4, 45), (2, 3): F(3, 20)}],
    ]
    for n, (r0, w, s0, c0, sp, cp) in enumerate(POINTS):
        M, f, fld, t, r, th, ph = setup(r0, w, s0, c0, order=2)
        assert M == expected_M[n]
        assert fld.torsion_free()
        assert [fld.omega(c) for c in range(4)] == expected_om[n]
        fj = f(r)
        q = fj.pw(F(1, 4), w)                         # f^{1/4}
        Phi = generic_phi(t, r, th, ph, r0)
        psi = m_scal(1 / (r * q), Phi)
        lhs = m_val(m_scal(r0 * w ** 3, dirac(fld, psi)))
        sn, cs = gtg.sincos(2, s0, c0, 4, 2)
        Kp = m_val(K_op(Phi, cs / sn, 1 / sn))
        rhs = m_add(m_val(A_op(Phi, fj)), m_scal(w * w / r0, Kp))
        assert GA.sub(lhs, rhs) == {}
        # a wrong measure factor (r^{-1} f^{+1/4}) fails
        bad = m_val(m_scal(r0 * w ** 3, dirac(fld, m_scal(q / r, Phi))))
        assert GA.sub(m_scal(w ** 2, bad), rhs) != {}


def check_angular_operator_and_squared_channel():
    premise("pairing.imported-schwarzschild-connection-curvature")
    r0, w, s0, c0, sp, cp = POINTS[0]
    M, f, fld, t, r, th, ph = setup(r0, w, s0, c0, order=3)
    g01 = GA.mul(er(0), er(1), S13)
    assert GA.mul(g01, g01, S13) == {(): F(1)}
    for a in (0, 1):
        assert GA.anticommutes(g01, er(a), S13)
    for a in (2, 3):
        assert GA.commutes(g01, er(a), S13)
    fj = f(r)
    sn, cs = gtg.sincos(2, s0, c0, 4, 3)
    Phi = generic_phi(t, r, th, ph, r0)
    T = lambda X: m_mul(g01, K_op(X, cs / sn, 1 / sn))
    assert GA.sub(m_val(T(A_op(Phi, fj))), m_val(A_op(T(Phi), fj))) == {}
    W = fj.pw(F(1, 2), w * w) / r
    dW = (fj * W.d(1))                                 # d_{r*} W = f d_r W
    assert W.v == F(1, 12) and dW.v == F(13, 1152)
    for lam in (1, -2):
        C = lambda X: m_add(A_op(X, fj), m_scal(lam * W, m_mul(g01, X)))
        lhs = m_val(C(C(Phi)))
        box = m_add(m_d(m_d(Phi, 0), 0), m_scal(-1, m_scal(fj, m_d(m_scal(fj, m_d(Phi, 1)), 1))))
        rhs = m_val(m_add(box, m_scal(lam * lam * W * W, Phi), m_scal(lam * dW, m_mul(er(0), Phi))))
        assert GA.sub(lhs, rhs) == {}
    # free 2D equation: (gamma^0 - gamma^1) P_+ = 0 with P_+ = (1 + gamma^0 gamma^1)/2: right movers
    Pp = m_scal(F(1, 2), m_add({(): F(1)}, g01))
    assert GA.mul(GA.sub(er(0), er(1)), Pp, S13) == {}
    assert GA.mul(Pp, Pp, S13) == Pp


def check_scalar_channel_potential():
    premise("pairing.imported-schwarzschild-connection-curvature")
    r0, w, s0, c0, sp, cp = POINTS[0]
    M, f, fld, t, r, th, ph = setup(r0, w, s0, c0, order=2)
    fd = gtg.static_field(r0, s0, c0, f, order=2)
    sn, cs = gtg.sincos(2, s0, c0, 4, 2)
    sph, cph = gtg.sincos(3, sp, cp, 4, 2)
    T, R = t, r - r0
    c = U_COEF
    u = c[0] + c[1] * T + c[2] * R + c[3] * T * T + c[4] * T * R + c[5] * R * R
    f0, fp0 = w ** 4, 2 * M / (r0 * r0)
    expect_u = 2 * c[3] - f0 * (fp0 * c[2] + f0 * 2 * c[5])   # d_t^2 u - f d_r (f d_r u) at the point
    for Y, ll, y0 in ((cs, 2, c0), (sn * cs * cph, 6, s0 * c0 * cp)):
        phi = u * Y / r
        Hi = fd.hb_matrix_jet()
        V = {}
        for a in range(4):
            comp = None
            for mu in range(4):
                term = Hi[mu][a] * phi.d(mu)
                comp = term if comp is None else comp + term
            V = m_add(V, m_scal(comp, er(a)))
        div = F(0)
        for cc in range(4):
            A = [F(int(k == cc)) for k in range(4)]
            DV = fd.cov_phys(A, V)
            div += GA.dot(er(cc), {k: v for k, v in DV.items() if len(k) == 1}, S13)
        lhs = r0 * f0 * (div + MU2 * phi.v) / y0
        Vpot = f0 * (F(ll) / (r0 * r0) + 2 * M / r0 ** 3 + MU2)
        assert lhs == expect_u + Vpot * c[0]
    assert expect_u == F(-541, 256)


def check_horizon_decay_orders():
    premise("pairing.imported-schwarzschild-connection-curvature")
    M = F(1)
    r = RF.var()
    f = RF.const(1) - RF.const(2 * M) / r
    fp = f.deriv()
    kappa = F(1, 4)                                    # f'(2M)/2 = 1/(4M)
    assert fp.eval(2 * M) == 2 * kappa
    for ll in (0, 2, 6, 12):
        Vf = RF.const(ll) / (r * r) + RF.const(2 * M) / (r * r * r) + RF.const(MU2)
        assert Vf.eval(2 * M) == F(ll, 4) + F(1, 4) + MU2   # V = f * (regular, nonzero) at the horizon
    # Dirac: (d_{r*} W)/sqrt f = f'/(2r) - f/r^2 = (3M - r)/r^3
    g = fp / (RF.const(2) * r) - f / (r * r)
    assert g.eqrf((RF.const(3 * M) - r) / (r * r * r))
    assert g.eval(2 * M) == F(1, 8)                    # 1/(8 M^2): V_+- of exact order sqrt f
    # f = C e^{2 kappa r*}: d/dr log C = (f' - 2 kappa)/f is regular at r = 2M
    h = (fp - RF.const(2 * kappa)) / f
    assert h.eqrf(-(r + RF.const(2)) / (RF.const(2) * r))
    assert h.eval(2 * M) == F(-1)


PSI_COEF = [(1, 2, 3, -1, 5, 7), (2, 0, 1, 3, -2, 1)]


def maxwell_odd(fld, f, r, r0, psi, Y):
    """Odd-parity potential A = psi (dY/dphi / sin dtheta - sin dY/dtheta dphi), F = D ^ A, and DF, D(IF)."""
    sn = Y[1]
    Yj = Y[0]
    Acoord = {2: psi * Yj.d(3) / sn, 3: -psi * sn * Yj.d(2)}
    Hi = fld.hb_matrix_jet()
    A = {}
    for mu, am in Acoord.items():
        for a in range(4):
            if Hi[mu][a] != 0:
                A = m_add(A, m_scal(am * Hi[mu][a], er(a)))
    Fb = {}
    for c in range(4):
        der = {}
        for mu in range(4):
            if Hi[mu][c] != 0:
                der = m_add(der, m_scal(Hi[mu][c], m_d(A, mu)))
        der = m_add(der, gtg.comm(fld.om[c], A))
        Fb = m_add(Fb, m_mul(er(c), der))
    assert gtg.grade(m_val(Fb), 0) == {}                # D . A = 0: the odd potential is in Lorenz gauge
    Fb = gtg.grade(Fb, 2)
    I = gtg.pseudoscalar()
    IF = m_mul(I, Fb)
    DF, DIF = {}, {}
    for c in range(4):
        Ac = [F(int(k == c)) for k in range(4)]
        DF = GA.add(DF, GA.mul(er(c), fld.cov_phys(Ac, Fb), S13))
        DIF = GA.add(DIF, GA.mul(er(c), fld.cov_phys(Ac, IF), S13))
    X = {k: v / psi.v for k, v in m_val(A).items()}
    return DF, DIF, X, I


def check_maxwell_channels_both_parities():
    premise("pairing.imported-schwarzschild-connection-curvature")
    r0, w, s0, c0, sp, cp = POINTS[0]
    M, f, fld, t, r, th, ph = setup(r0, w, s0, c0, order=3)
    sn, cs = gtg.sincos(2, s0, c0, 4, 3)
    sph, cph = gtg.sincos(3, sp, cp, 4, 3)
    fj = f(r)
    R = r - r0
    f0 = w ** 4
    seen = []
    for c in PSI_COEF:
        psi = c[0] + c[1] * t + c[2] * R + c[3] * t * t + c[4] * t * R + c[5] * R * R
        for Y, ll in (((cs, sn), 2), ((sn * cs * cph, sn), 6)):
            DF, DIF, X, I = maxwell_odd(fld, f, r, r0, psi, Y)
            E = (psi.d(0).d(0) - fj * (fj * psi.d(1)).d(1) + fj * (ll + 2) * psi / (r * r)).v
            assert {k: v for k, v in DF.items() if len(k) == 3} == {}      # D ^ F = 0
            vec = {k: v for k, v in DF.items() if len(k) == 1}
            assert vec == {k: E * v / f0 for k, v in X.items()}             # D . F = (1/f) E X
            assert GA.add(DIF, GA.mul(I, DF, S13)) == {}                    # D(IF) = -I DF: duality
            seen.append(vec)
    assert seen[0] == {(3,): F(4837, 720)}
