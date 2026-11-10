"""synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional: exact checks.

The Schwarzschild field in the static gauge of Gauge Theory Gravity (gtg.static_field, the stored connection forms),
perturbed to first order in the gauge field: hb^{-1}(e_mu) = g_mu + eps k_mu, Omega = Omega_0 + eps Omega_1 with
Omega_1 solved exactly from the linearised torsion-free condition, and the first-order Ricci vector
calR_1(gamma_b) read from the linearised field strength. Jets at rational points where f = 1 - 2M/r is a square.
The angular functions are generic solutions of their defining equations with a generic rational separation constant
L (L = l(l+1) is not used), so each identity holds for every l at the sample points. Checks:
  (1) odd parity (Regge-Wheeler gauge): calR_1(gamma_3) has the closed-form components E_t, E_r, E_theta;
  (2) the Regge-Wheeler reduction: the 2D operator on Q = f h1/r is an explicit combination of E_r, E_theta; the
      time derivative of E_t is a combination of E_r, E_theta; a reconstruction instance;
  (3) the superpotential: W^2 -+ dW/dr_* - c^2 are the Regge-Wheeler and Zerilli potentials, and d/dr_* + W
      intertwines the two channel operators;
  (4) even parity: the Zerilli equation of the Zerilli-Moncrief function lies in the span of the linearised vacuum
      equations and their first derivatives at the jet point (and fails to with a wrong potential);
  (5) horizon values of V/f for both parities.
"""
from fractions import Fraction as F
import GA
import gtg
from gtg import Jet, m_add, m_scal, m_neg, m_d, comm, S13
from GA import RF
from tp_premise import premise

SCHW = "pairing.imported-schwarzschild-connection-curvature"
LOWER = "synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional"
POINTS = [(F(3), F(1, 2), F(3, 5), F(4, 5)), (F(5), F(2, 3), F(5, 13), F(12, 13))]   # r0, sqrt f, sin, cos
H_COEF = [((1, 2, 3, -1, 5, 7, 2, -3, 1, 4), (2, -1, 1, 3, -2, 5, 1, 1, -2, 3)),
          ((0, 1, -2, 4, 1, -3, 5, 2, 2, -1), (3, 2, -5, 1, 4, 1, -2, 3, 1, 1))]
SEPARATION = [F(6), F(12), F(7, 2)]                 # L: two harmonic values and a generic one


def lin_ricci(fld, TH1):
    """Jets of the first-order Ricci vectors calR_1(gamma_b) of the field TH0 + eps TH1 (torsion-free)."""
    d, sq = fld.d, fld.sq
    g1 = [{(a,): TH1[a][mu] for a in range(d) if TH1[a][mu]} for mu in range(d)]
    bl = gtg.bivector_blades(d)
    nb = len(bl)
    rhs = []
    for p in range(d):
        for q in range(p + 1, d):
            t = m_add(m_d(g1[q], p), m_neg(m_d(g1[p], q)),
                      comm(fld.Om[p], g1[q], sq), m_neg(comm(fld.Om[q], g1[p], sq)))
            for a in range(d):
                rhs.append(-t.get((a,), F(0)))
    sol = gtg.ring_solve(gtg._torsion_matrix(fld.g, sq), rhs)
    Om1 = [{bl[j]: sol[mu * nb + j] for j in range(nb) if sol[mu * nb + j]} for mu in range(d)]
    H0 = fld.hb_matrix_jet()
    H1 = [[-sum((H0[mu][a] * TH1[a][nu] * H0[nu][b] for a in range(d) for nu in range(d)), F(0))
           for b in range(d)] for mu in range(d)]
    Rc1 = {}
    for a in range(d):
        for b in range(a + 1, d):
            acc = {}
            for mu in range(d):
                for nu in range(mu + 1, d):
                    R0 = fld.strength_jet(mu, nu)
                    R1 = m_add(m_d(Om1[nu], mu), m_neg(m_d(Om1[mu], nu)),
                               comm(fld.Om[mu], Om1[nu], sq), comm(Om1[mu], fld.Om[nu], sq))
                    c0 = H0[mu][a] * H0[nu][b] - H0[nu][a] * H0[mu][b]
                    c1 = (H1[mu][a] * H0[nu][b] + H0[mu][a] * H1[nu][b]
                          - H1[nu][a] * H0[mu][b] - H0[nu][a] * H1[mu][b])
                    if R1:
                        acc = m_add(acc, m_scal(c0, R1))
                    if R0:
                        acc = m_add(acc, m_scal(c1, R0))
            Rc1[(a, b)] = m_scal(gtg.STORE_SIGN, acc)
    return [gtg.ricci(Rc1, GA.gen(b), sq) for b in range(d)]


def integrate(j, i):
    """Termwise integral of a jet along label i from the base point (order kept)."""
    cc = {}
    for e, x in j.c.items():
        if j.order is not None and sum(e) + 1 > j.order:
            continue
        g = list(e)
        g[i] += 1
        cc[tuple(g)] = x / g[i]
    return Jet(c=cc, nv=j.nv, order=j.order)


def angular(sn, cs, L, a, b, sign, K):
    """Jet in theta of the solution of Y'' = sign cot(theta) Y' - L Y with Y = a, Y' = b at the point
    (sign = -1: the Legendre equation of P; sign = +1: S = sin(theta) dP/dtheta)."""
    th = Jet.var(2, F(0), 4, K)
    Y = a + b * th
    cot = cs / sn
    for _ in range(K):
        d1 = b + integrate((sign * cot * Y.d(2) - L * Y).trunc(K - 1), 2)
        d1 = Jet(c=d1.c, nv=4, order=K)
        Y = a + integrate(d1, 2)
    return Y


def setup(r0, w, s0, c0, K=3):
    M = gtg.mass_for_root(r0, w)                      # f(r0) = w^2
    f = gtg.f_static(M)
    fld = gtg.static_field(r0, s0, c0, f, order=K - 1)
    t = Jet.var(0, F(0), 4, K)
    r = Jet.var(1, r0, 4, K)
    sn, cs = gtg.sincos(2, s0, c0, 4, K)
    return M, f, fld, t, r, sn, cs


def generic(c, t, R):
    return (c[0] + c[1] * t + c[2] * R + c[3] * t * t + c[4] * t * R + c[5] * R * R
            + c[6] * t * t * R + c[7] * t * R * R + c[8] * R * R * R + c[9] * t * t * t)


def odd_equations(h0, h1, fj, r, M, L):
    Eth = h0.d(0) / fj - (fj * h1).d(1)
    Er = h1.d(0).d(0) - h0.d(0).d(1) + 2 * h0.d(0) / r + (L - 2) * fj * h1 / (r * r)
    Et = fj * (h0.d(1).d(1) - h1.d(0).d(1) - 2 * h1.d(0) / r) - (L / (r * r) - 4 * M / (r * r * r)) * h0
    return Et, Er, Eth


class K(object):
    """An element of the field Q(z) of rational functions (GA.RF) with mixed arithmetic, so that jets can carry
    coefficients that are rational functions of z = sqrt f (or of z = tan(theta/2))."""
    __slots__ = ("x",)

    def __init__(self, x):
        self.x = x if isinstance(x, RF) else RF.const(F(x))

    @staticmethod
    def _c(o):
        return o if isinstance(o, K) else K(o)

    def __add__(self, o):
        return K(self.x + K._c(o).x)
    __radd__ = __add__

    def __sub__(self, o):
        return K(self.x - K._c(o).x)

    def __rsub__(self, o):
        return K(K._c(o).x - self.x)

    def __mul__(self, o):
        if isinstance(o, Jet):
            return NotImplemented
        return K(self.x * K._c(o).x)
    __rmul__ = __mul__

    def __truediv__(self, o):
        return K(self.x / K._c(o).x)

    def __rtruediv__(self, o):
        return K(K._c(o).x / self.x)

    def __neg__(self):
        return K(-self.x)

    def __pow__(self, n):
        out = K(1)
        for _ in range(n):
            out = out * self
        return out

    def __bool__(self):
        return not self.x.is_zero()

    def __eq__(self, o):
        return (self.x - K._c(o).x).is_zero()

    def __ne__(self, o):
        return not self.__eq__(o)
    __hash__ = None


def odd_case(M, r0, w, s0, c0, L, ca, cb, a, b):
    """First-order Ricci vectors of the odd-parity field at the point (r0, theta0), sqrt f = w, against the closed
    forms; r0, w, s0, c0 may be rational numbers or elements of Q(z)."""
    f = gtg.f_static(M)
    fld = gtg.static_field(r0, s0, c0, f, order=1, sqrt_f=w)
    t = Jet.var(0, F(0), 4, 2)
    r = Jet.var(1, r0, 4, 2)
    sn, cs = gtg.sincos(2, s0, c0, 4, 2)
    fj = f(r)
    sf = fj.pw(F(1, 2), w)
    h0, h1 = generic(ca, t, r - r0), generic(cb, t, r - r0)
    S = angular(sn, cs, L, a, b, 1, 2)
    Z = Jet.const(0, 4)
    TH1 = [[Z] * 4 for _ in range(4)]
    TH1[0][3] = h0 * S / sf                  # hb^{-1}(e_phi) gains (h0 S / sqrt f) gamma_0
    TH1[1][3] = -h1 * S * sf                 # and -(sqrt f h1 S) gamma_1
    ric = [{k: gtg._val(v) for k, v in x.items() if gtg._val(v)} for x in lin_ricci(fld, TH1)]
    Et, Er, Eth = [x.v for x in odd_equations(h0, h1, fj, r, M, L)]
    pre = -a / (2 * r0 * s0 * w)
    ang = (b - 2 * (c0 / s0) * a) / (2 * r0 * r0 * s0)
    want = {(0,): pre * Et, (1,): pre * Er, (2,): ang * Eth}
    assert sorted(ric[3]) == [(0,), (1,), (2,)] and all(ric[3][k] == want[k] for k in want)
    assert sorted(ric[0]) == [(3,)] and ric[0][(3,)] == -want[(0,)]          # symmetric Ricci tensor
    assert sorted(ric[1]) == [(3,)] and ric[1][(3,)] == want[(1,)]
    assert sorted(ric[2]) == [(3,)] and ric[2][(3,)] == want[(2,)]
    assert ric[3][(1,)] != 2 * want[(1,)]
    return fld


def check_odd_parity_linearised_ricci():
    premise(SCHW)
    data = ((F(2), F(-1)), (F(1), F(3)))
    # (a) rational sample points
    seen = 0
    for (r0, w, s0, c0) in POINTS:
        M = gtg.mass_for_root(r0, w)
        for L in SEPARATION:
            for (ca, cb), (a, b) in zip(H_COEF, data):
                fld = odd_case(M, r0, w, s0, c0, L, ca, cb, a, b)
                assert fld.torsion_free()
                assert all(gtg.ricci(fld.curvature(), GA.gen(i)) == {} for i in range(4))   # vacuum background
                seen += 1
    assert seen == 12
    # (b) identities of rational functions of z = sqrt f, with r = 2M/(1 - z^2): every radius of the exterior
    z = K(RF.var())
    for M, (s0, c0), L, k in ((F(1), (F(3, 5), F(4, 5)), F(7, 2), 0), (F(9, 8), (F(5, 13), F(12, 13)), F(6), 1),
                              (F(1), (F(15, 17), F(-8, 17)), F(12), 1)):
        odd_case(M, 2 * M / (1 - z * z), z, s0, c0, L, H_COEF[k][0], H_COEF[k][1], data[k][0], data[k][1])
    # (c) identities of rational functions of z = tan(theta/2) at fixed radius: every polar angle
    s0, c0 = 2 * z / (1 + z * z), (1 - z * z) / (1 + z * z)
    for (r0, w, _, _), L, k in ((POINTS[0], F(7, 2), 1), (POINTS[1], F(6), 0)):
        odd_case(gtg.mass_for_root(r0, w), r0, w, s0, c0, L, H_COEF[k][0], H_COEF[k][1], data[k][0], data[k][1])


def check_regge_wheeler_reduction():
    premise(SCHW)
    for (r0, w, s0, c0) in POINTS:
        M, f, fld, t, r, sn, cs = setup(r0, w, s0, c0)
        fj = f(r)
        for L in SEPARATION:
            for ca, cb in H_COEF:
                h0, h1 = generic(ca, t, r - r0), generic(cb, t, r - r0)
                Et, Er, Eth = odd_equations(h0, h1, fj, r, M, L)
                Q = fj * h1 / r
                V = fj * (L / (r * r) - 6 * M / (r * r * r))
                RW = Q.d(0).d(0) - fj * (fj * Q.d(1)).d(1) + V * Q
                comb = (fj / r) * (Er + (fj * Eth).d(1) - 2 * fj * Eth / r)
                assert RW == comb and bool(RW)
                assert RW != comb + fj * Q / (r * r)                 # a potential with 5M or 7M fails
                bian = -fj * Er.d(1) - 2 * fj * Er / r - (L - 2) * fj * Eth / (r * r)
                assert Et.d(0) == bian and bool(bian)
                # reconstruction: h1 = r Q / f, d_t h0 = f d_r(r Q), no static part
                q = generic(cb, t, r - r0)
                k1 = r * q / fj
                k0 = integrate(fj * (r * q).d(1), 0)
                Gt, Gr, Gth = odd_equations(k0, k1, fj, r, M, L)
                assert not bool(Gth.trunc(1))
                rw = q.d(0).d(0) - fj * (fj * q.d(1)).d(1) + V * q
                assert (Gr.trunc(0) - (r * rw / fj).trunc(0)) == 0 and bool(rw)


def potentials(M, L):
    lam = (L - 2) / 2
    r = RF.var()
    k = RF.const
    f = k(F(1)) - k(2 * M) / r
    VRW = f * (k(L) / (r * r) - k(6 * M) / (r * r * r))
    den = k(lam) * r + k(3 * M)
    VZ = f * (k(2 * lam * lam * (lam + 1)) * r * r * r + k(6 * lam * lam * M) * r * r
              + k(18 * lam * M * M) * r + k(18 * M ** 3)) / (r * r * r * den * den)
    c = lam * (lam + 1) / (3 * M)
    W = k(3 * M) * f / (r * den) + k(c)
    return f, VRW, VZ, W, c, lam


def check_superpotential_and_intertwiner():
    premise(SCHW)
    for M in (F(1), F(9, 8), F(2, 3)):
        for L in (F(6), F(12), F(20), F(7, 2)):
            f, VRW, VZ, W, c, lam = potentials(M, L)
            dW = f * W.deriv()
            cc = RF.const(c * c)
            assert (W * W - dW - cc).eqrf(VRW) and (W * W + dW - cc).eqrf(VZ)
            assert not (W * W + dW - cc).eqrf(VRW)
            assert W.eval(2 * M) == c                                  # W is bounded at the horizon
    # operator form at a jet point: (D + W)(d_t^2 - D^2 + V_RW) = (d_t^2 - D^2 + V_Z)(D + W), D = f d_r
    r0, w, s0, c0 = POINTS[0]
    M, fs, fld, t, r, sn, cs = setup(r0, w, s0, c0, K=4)
    fj = fs(r)
    for L in (F(6), F(7, 2)):
        lam = (L - 2) / 2
        c = lam * (lam + 1) / (3 * M)
        Wj = 3 * M * fj / (r * (lam * r + 3 * M)) + c
        VRW = fj * (L / (r * r) - 6 * M / (r * r * r))
        VZ = fj * (2 * lam * lam * (lam + 1) * r ** 3 + 6 * lam * lam * M * r * r + 18 * lam * M * M * r
                   + 18 * M ** 3) / (r ** 3 * (lam * r + 3 * M) ** 2)
        R = r - r0
        Q = generic(H_COEF[0][0], t, R) + 2 * R * R * R * R - t * t * R * R + 3 * t * R * R * R

        def D(u):
            return fj * u.d(1)

        def box(u, V):
            return u.d(0).d(0) - D(D(u)) + V * u
        Zf = D(Q) + Wj * Q
        left = D(box(Q, VRW)) + Wj * box(Q, VRW)
        right = box(Zf, VZ)
        assert left == right and bool(right)
        assert left != box(Zf, VRW)
        # the kernel of D + W: (D - W)(D + W) = -(H_RW + c^2)
        assert D(Zf) - Wj * Zf == -(-D(D(Q)) + VRW * Q + c * c * Q)


def even_functionals(pt, L, fn, mono, ab):
    r0, w, s0, c0 = pt
    M, f, fld, t, r, sn, cs = setup(r0, w, s0, c0)
    fj = f(r)
    sf = fj.pw(F(1, 2))
    P = angular(sn, cs, L, ab[0], ab[1], -1, 3)
    Z = Jet.const(0, 4)
    H = [Z, Z, Z, Z]
    H[fn] = Jet(1, None, 4, 3) * (t ** mono[0]) * ((r - r0) ** mono[1])
    H0, H1, H2, K = H
    TH1 = [[Z] * 4 for _ in range(4)]
    TH1[0][0] = -sf * H0 * P / 2                     # f(1 - H0 P) dt^2
    TH1[1][0] = sf * H1 * P                          # -2 H1 P dt dr
    TH1[1][1] = H2 * P / (2 * sf)                    # -(1 + H2 P) dr^2 / f
    TH1[2][2] = r * K * P                        # -r^2 (1 + K P) dOmega^2
    TH1[3][3] = r * sn * K * P / 2
    ric = lin_ricci(fld, TH1)
    rows = []
    for b in range(4):
        for a in range(4):
            x = ric[b].get((a,), Z)
            x = x if isinstance(x, Jet) else Jet.const(x, 4)
            if x.order is None:
                rows += [x.v, F(0), F(0)]
            else:
                rows += [x.v, x.d(0).v, x.d(1).v]
    lam = (L - 2) / 2
    Psi = r * (K + (fj * r / (lam * r + 3 * M)) * (H2 - r * K.d(1)))

    def zer(l2):
        VZ = fj * (2 * l2 * l2 * (l2 + 1) * r ** 3 + 6 * l2 * l2 * M * r * r + 18 * l2 * M * M * r
                   + 18 * M ** 3) / (r ** 3 * (l2 * r + 3 * M) ** 2)
        return (Psi.d(0).d(0) - fj * (fj * Psi.d(1)).d(1) + VZ * Psi).v
    return rows, zer(lam), zer(lam + 1)


def check_even_parity_zerilli_in_span():
    premise(SCHW)
    for pt, L, ab in ((POINTS[0], F(6), (F(2), F(-1))), (POINTS[1], F(7, 2), (F(1), F(3)))):
        cols, good, bad = [], [], []
        for fn in range(4):
            for i in range(4):
                for j in range(4 - i):
                    rows, zg, zb = even_functionals(pt, L, fn, (i, j), ab)
                    cols.append(rows)
                    good.append(zg)
                    bad.append(zb)
        n = len(cols)
        assert n == 40
        mat = [[cols[c][k] for c in range(n)] for k in range(len(cols[0]))]
        mat = [row for row in mat if any(row)]
        rk = GA.field_rank(mat)
        assert rk == 18 and any(good)
        assert GA.field_rank(mat + [good]) == rk          # Zerilli's equation follows from the vacuum equations
        assert GA.field_rank(mat + [bad]) == rk + 1       # with a wrong potential it does not


def check_horizon_values():
    premise(SCHW)
    premise(LOWER)
    for M in (F(1), F(9, 8), F(2, 3)):
        kappa = 1 / (4 * M)
        for L in (F(6), F(12), F(20), F(30)):
            f, VRW, VZ, W, c, lam = potentials(M, L)
            assert f.eval(2 * M) == 0 and f.deriv().eval(2 * M) == 2 * kappa
            a = (VRW / f).eval(2 * M)
            b = (VZ / f).eval(2 * M)
            assert a == (L - 3) / (4 * M * M) and a > 0
            assert b == (4 * lam * lam + 4 * lam + 3) / (4 * M * M * (2 * lam + 3)) and b > 0
            assert VRW.eval(2 * M) == 0 and VZ.eval(2 * M) == 0
