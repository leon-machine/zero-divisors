"""Null-surface data at any field strength, the focusing equation integrated: exact checks.

Cl(1,3), signature (+,-,-,-), frame e_0..e_3, n = e_0 + e_3, l = (e_0 - e_3)/2 (Q(n) = Q(l) = 0, n.l = 1),
transverse e_1, e_2. The labels of the flat background are (lam, nu, y^1, y^2) with
x = lam n + nu l + y^1 e_1 + y^2 e_2, so lam = l.x and nu = n.x; the physical frame is the constant frame e_a.

The exact family: the plane wave hb^{-1}(a) = a - H (a.l) l, H = 1/2 w_ij(lam) y^i y^j (W = 2H in the entity),
w a symmetric 2 x 2 profile given by its Taylor coefficients about the sample point. A null function of it is
phi = n.x - 1/2 S_ij(lam) y^i y^j with S' = w - S^2, and K = hb^T(grad phi). E is the map with E' = S E.
Fields are lib/gtg.py jets about a rational point that is not the origin; nothing is small. Omega is solved
from the torsion equation at jet order two; the series of order eight use the closed forms of hb and Omega,
which are tested there, as jets, against hb^{-1} and the torsion equation.

(vi)   the wave is a gravitational field with Omega(a) = (a.l) grad H ^ l, its curvature is the stored
       first-order curvature of 2w at the null momentum l with no correction, its Ricci map is (tr w)(a.l) l;
(vi)   K is a null gradient, affinely parametrised by lam; the screen frame m_i = e_i - (K.e_i) l is parallel
       and the map B(A) = A.D K of the first-order result's clause (iii) is S in it;
(i)    rho^4 = -(hb^{-1}(x_1 ^ x_2))^2 for two connecting vectors, d rho/d lam = theta rho/2, and the shape:
       the Gram matrix G of the two physical separations has 1/4 tr((G^{-1} G' - theta)^2) = <sigma, sigma>;
(ii)   rho'' = -1/2 (<sigma, sigma> - K.R(K)) rho, on waves that are not weak, vacuum and not;
(ii), (iii), (vi) on a null plane (S = 0 at the point) at orders one to four in the amplitude of the wave;
(iii)  the integrated forms in the parameter s (ds = d lam/rho) and in the area parameter (with rho itself as
       the variable), with matter;
(iii), (viii) exact waves with power-law profile: form (beta) and the area as a clock, in differential form at
       sample points, with the shape computed from the gauge field;
(iv), (vii)  the bound 2/|theta| and exact caustics, one of them of a null plane crossed by a vacuum wave.
"""
from fractions import Fraction as F

import GA
from GA import gen
from tp_premise import premise
import gtg

Jet = gtg.Jet
D = 4
S13 = GA.sig(1, 3)
ETA = [1, -1, -1, -1]
E = [gen(i) for i in range(D)]
ZJ = Jet.const(0, D)
NV = {(0,): F(1), (3,): F(1)}                       # n
LV = {(0,): F(1, 2), (3,): F(-1, 2)}                # l
LABELS = (NV, LV, E[1], E[2])                       # the background vectors e_mu of the labels lam, nu, y^1, y^2
RECIPROCAL = (LV, NV, GA.neg(E[1]), GA.neg(E[2]))   # their reciprocals: grad f = sum RECIPROCAL[mu] d_mu f
FRAME_OF_LABELS = [[v.get((a,), F(0)) for v in LABELS] for a in range(D)]
GRAM = ((0, 1, 0, 0), (1, 0, 0, 0), (0, 0, -1, 0), (0, 0, 0, -1))      # e_mu . e_nu
L_LABEL = (1, 0, 0, 0)                              # e_mu . l
L_FRAME = (F(1, 2), F(0), F(0), F(1, 2))            # gamma_a . l
TR = (1, 2)                                         # the transverse frame vectors e_1, e_2
PAIRS = ((0, 0), (0, 1), (1, 0), (1, 1))

# sample data (fixed, generic, none of it small): the point, the profiles w_ij as Taylor coefficients in
# d lam about the point, initial screen maps, amplitudes
X0 = (F(7, 20), F(3, 10), F(1, 3), F(-1, 4))                      # lam, nu, y^1, y^2
W_BOTH = ((3, 2, 1), (F(5, 2), -1), (-3, -2, -1))                 # w11, w12, w22: both polarisations, varying
W_PLUS = ((7,), (), (-7,))                                        # one polarisation, constant
W_CROSS = ((), (2, 3, F(-1, 2), F(1, 3)), ())                     # the other polarisation, varying
W_MATTER = ((1, 2, 1), (F(5, 2), -1), (-3, 1, -2))                # trace -2 at the point: not vacuum
W_ANTI = ((3, 1), (F(1, 2),), (1, -1))                            # trace +4 at the point: not vacuum
PROFILES = (W_BOTH, W_PLUS, W_CROSS, W_MATTER, W_ANTI)
S_ZERO = ((0, 0), (0, 0))
S_OUT = ((F(2, 3), F(-1, 5)), (F(-1, 5), F(3, 7)))                # expanding
S_IN = ((F(-5, 4), F(1, 3)), (F(1, 3), F(-2, 7)))                 # contracting
AMPLITUDES = (F(1), F(-2), F(3, 2), F(5), F(-1, 3), F(7, 4))
LOW, HIGH = 2, 8                                                  # jet orders of Omega
SERIES = HIGH - 1                                                 # order of the series of theta and the shear
POWER_LAW_A = (F(1), F(3), F(1, 2), F(-2), F(10), F(0))           # exponents a of the shapes diag(rho^a, rho^-a)
POWER_LAW_LAMS = (F(3), F(5, 2))                                  # the values of lam at which they are sampled
E_START = ((3, -1), (2, 1))                                       # a value of E at the point that is not the identity
DUST_POINTS = (F(1, 4), F(1, 2), F(3, 4), F(9, 10))               # points before the caustic of the wave with matter
SMOOTH_WAVES = (F(1, 2), F(4))                                    # the constant c of the smooth vacuum waves
SMOOTH_POINTS = (F(1, 2), F(1))                                   # a point before the caustic, and the caustic
S11_SAMPLE = F(1, 3)                                              # a screen-map entry in the other direction


def point(lam):
    """the sample point with l.x = lam (the other labels fixed, not zero)."""
    return (lam, F(2, 5), F(1, 3), F(-1, 4))


def sign(x):
    return (x > 0) - (x < 0)


def padded(a, n):
    """a series cut or filled with zeros to order n."""
    return [a[i] if i < len(a) else F(0) for i in range(n + 1)]


# ---------------------------------------------------------------------------------------------------------
# one-variable truncated series (lists of Fractions, index = power of d lam)
# ---------------------------------------------------------------------------------------------------------

def s_mul(a, b, n):
    out = [F(0)] * (n + 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if i + j > n:
                    break
                if y:
                    out[i + j] += x * y
    return out


def s_add(a, b, c=1):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else F(0)) + c * (b[i] if i < len(b) else F(0)) for i in range(n)]


def s_scal(c, a):
    return [c * x for x in a]


def s_inv(a, n):
    out = [F(1) / a[0]]
    for k in range(1, n + 1):
        acc = sum((a[i] * out[k - i] for i in range(1, min(k, len(a) - 1) + 1)), F(0))
        out.append(-acc / a[0])
    return out


def s_der(a):
    return [a[k] * k for k in range(1, len(a))]


def s_int(a):
    return [F(0)] + [a[k] / (k + 1) for k in range(len(a))]


def s_log(a, n):
    """log of a series with a[0] = 1, to order n."""
    return s_int(s_mul(s_der(a), s_inv(a, n), n - 1))[:n + 1]


def s_log_ratio(a, n):
    """log(a/a[0]) to order n, for a series with a[0] != 0."""
    return s_log(s_scal(1 / a[0], a), n)


def s_pow(a, r, n):
    """a^r, to order n, for a series with a[0] = 1 and rational r (from y' = r (a'/a) y)."""
    q = s_scal(F(r), s_mul(s_der(a), s_inv(a, n), n - 1))
    y = [F(1)]
    for k in range(n):
        y.append(sum((q[i] * y[k - i] for i in range(k + 1)), F(0)) / (k + 1))
    return y


def s_exp(a, n):
    """exp of a series with a[0] = 0, to order n (from y' = a' y)."""
    q = s_der(a)
    y = [F(1)]
    for k in range(n):
        y.append(sum((q[i] * y[k - i] for i in range(min(k, len(q) - 1) + 1)), F(0)) / (k + 1))
    return y


def s_compose(f, g, n):
    """f(g(x)) to order n, for a series g with g[0] = 0."""
    out = [F(0)] * (n + 1)
    for c in reversed(f[:n + 1]):
        out = s_mul(out, g, n)
        out[0] += c
    return out


def s_revert(a, n):
    """the series b with a(b(x)) = x, to order n, for a[0] = 0, a[1] != 0."""
    b = [F(0), 1 / a[1]] + [F(0)] * (n - 1)
    for _ in range(n):
        r = s_compose(a, b, n)
        r[1] -= 1
        b = s_add(b, s_scal(1 / a[1], r), -1)
    return b


def same(a, b, n):
    """equality of two series through order n (both must reach it)."""
    return len(a) > n and len(b) > n and all(a[i] == b[i] for i in range(n + 1))


def interpolate(xs, ys):
    """coefficients of the polynomial of degree < len(xs) through the points (xs[i], ys[i])."""
    n = len(xs)
    coef = [F(0)] * n
    for i in range(n):
        num, den = [F(1)], F(1)
        for j in range(n):
            if j != i:
                num = s_mul(num, [-xs[j], F(1)], n)
                den *= xs[i] - xs[j]
        for k in range(n):
            coef[k] += ys[i] * num[k] / den
    return coef


def det(M):
    """determinant of a square matrix of Fractions."""
    M = [[F(x) for x in row] for row in M]
    out = F(1)
    for c in range(len(M)):
        p = next((r for r in range(c, len(M)) if M[r][c]), None)
        if p is None:
            return F(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            out = -out
        out *= M[c][c]
        for r in range(c + 1, len(M)):
            f = M[r][c] / M[c][c]
            M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return out


def rational_series(num, den, n):
    """Taylor coefficients to order n of num/den (polynomials in the series variable)."""
    return s_mul([F(c) for c in num], s_inv([F(c) for c in den] + [F(0)], n), n)


def shifted(poly, a):
    """coefficients of poly(a + t) in t."""
    out = [F(0)] * len(poly)
    for k, c in enumerate(poly):
        term = [F(1)]
        for _ in range(k):
            term = s_mul(term, [F(a), F(1)], len(poly) - 1)
        for i, x in enumerate(term):
            out[i] += F(c) * x
    return out


# ---------------------------------------------------------------------------------------------------------
# the plane wave and a null hypersurface in it
# ---------------------------------------------------------------------------------------------------------

def profile(w, amp=1):
    """the symmetric 2 x 2 array of coefficient lists of amp * w."""
    w11, w12, w22 = ([F(amp) * F(c) for c in part] for part in w)
    return [[w11, w12], [w12, w22]]


def riccati(w, S0, n):
    """Taylor coefficients through order n of S with S' = w - S^2, S(0) = S0."""
    Sc = [[[F(S0[i][j])] for j in range(2)] for i in range(2)]
    for k in range(n):
        new = [[(w[i][j][k] if k < len(w[i][j]) else F(0))
                - sum((Sc[i][m][a] * Sc[m][j][k - a] for m in range(2) for a in range(k + 1)), F(0))
                for j in range(2)] for i in range(2)]
        for i, j in PAIRS:
            Sc[i][j].append(new[i][j] / (k + 1))
    return Sc


def jacobi(Sc, n, E0=None):
    """Taylor coefficients through order n of E with E' = S E, E(0) = E0 (the identity if not given)."""
    Ec = [[[F(E0[i][j]) if E0 else F(1 if i == j else 0)] for j in range(2)] for i in range(2)]
    for k in range(n):
        new = [[sum((Sc[i][m][a] * Ec[m][j][k - a] for m in range(2) for a in range(k + 1)), F(0))
                for j in range(2)] for i in range(2)]
        for i, j in PAIRS:
            Ec[i][j].append(new[i][j] / (k + 1))
    return Ec


def series_jet(coeffs, dlam):
    out, p = ZJ, Jet.const(1, D)
    for c in coeffs:
        if c:
            out = out + p * c
        p = p * dlam
    return out


def vdot(a, b):
    return ZJ + gtg.vdot(a, b, S13)


def jzero(j):
    return not (ZJ + j).c


def mzero(m):
    return all(jzero(c) for c in m.values())


class Wave(object):
    """The plane wave of profile w about the point x0 = (lam, nu, y^1, y^2) and the null function whose screen
    map at the point is S0; E0 is the value at the point of the map E of the separations (the identity if not given). Omega is solved from the torsion equation by lib/gtg.py and hb is inverted there;
    with closed=True the closed forms Omega(a) = (a.l) grad H ^ l and hb(a) = a + H (a.l) l are used instead (the
    high-order series), and closed_form_holds() then tests, as jets, that this hb inverts hb^{-1} and that this
    Omega satisfies the torsion equation, which fixes it."""

    def __init__(self, w, S0, x0, order, closed=False, E0=None):
        self.order, self.w = order, w
        X = [Jet.var(i, x0[i], D, order + 1) for i in range(D)]
        self.X, self.Y = X, (X[2], X[3])
        self.dlam = X[0] - x0[0]
        self.wj = [[series_jet(w[i][j], self.dlam) for j in range(2)] for i in range(2)]
        H = ZJ
        for i, j in PAIRS:
            H = H + F(1, 2) * self.wj[i][j] * self.Y[i] * self.Y[j]
        self.H = H
        # hb^{-1}(e_mu) = e_mu - H (e_mu . l) l on the physical frame: TH[a][mu]
        TH = [[LABELS[mu].get((a,), F(0)) - H * L_LABEL[mu] * LV.get((a,), F(0)) for mu in range(D)]
              for a in range(D)]
        gradH = gtg.m_add(*[gtg.m_scal(H.d(mu), RECIPROCAL[mu]) for mu in range(D) if H.d(mu)])
        form = gtg.wedge(gradH, LV, S13)
        self.om_closed = [gtg.m_scal(L_FRAME[c], form) if L_FRAME[c] else {} for c in range(D)]
        self.fld = gtg.Field(TH, self.om_closed if closed else None, S13)
        if closed:
            # hb(gamma_a) = gamma_a + H (gamma_a . l) l on the labels: HJ[mu][a]
            self.HJ = [[gtg.vdot(RECIPROCAL[mu], E[a], S13) + H * L_FRAME[a] * gtg.vdot(RECIPROCAL[mu], LV, S13)
                        for a in range(D)] for mu in range(D)]
        else:
            self.HJ = self.fld.hb_matrix_jet()
        n = order + 2
        self.Sc = riccati(w, S0, n)
        self.Ec = jacobi(self.Sc, n, E0)
        self.Sj = [[series_jet(self.Sc[i][j], self.dlam) for j in range(2)] for i in range(2)]
        self.Ej = [[series_jet(self.Ec[i][j], self.dlam) for j in range(2)] for i in range(2)]
        phi = X[1]                                                                     # n.x
        for i, j in PAIRS:
            phi = phi - F(1, 2) * self.Sj[i][j] * self.Y[i] * self.Y[j]
        self.phi = phi
        dphi = [phi.d(mu) for mu in range(D)]
        klow = [sum((self.HJ[mu][a] * dphi[mu] for mu in range(D)), ZJ) for a in range(D)]
        self.K = {(a,): klow[a] * ETA[a] for a in range(D) if klow[a]}                 # K = hb^T(grad phi)
        self.Kup = [self.K.get((a,), ZJ) for a in range(D)]
        self.k = [sum((self.HJ[mu][a] * self.Kup[a] for a in range(D)), ZJ) for mu in range(D)]   # hb(K)
        self.Bj = [self.cov(c, self.K) for c in range(D)]                              # B(gamma_c)

    # -- derivatives ------------------------------------------------------------------------------------
    def cov(self, c, V):
        """(gamma_c . D) V, as jets."""
        out = gtg.comm(self.fld.om[c], V, S13)
        for mu in range(D):
            if self.HJ[mu][c]:
                out = gtg.m_add(out, gtg.m_scal(self.HJ[mu][c], gtg.m_d(V, mu)))
        return out

    def cov_K(self, V):
        """(K . D) V, as jets."""
        return gtg.m_add(*[gtg.m_scal(self.Kup[c], self.cov(c, V)) for c in range(D) if self.Kup[c]])

    def along(self, f):
        """hb(K) . grad f = d f/d lambda for a scalar jet."""
        return sum((self.k[mu] * f.d(mu) for mu in range(D)), ZJ)

    def B(self, V):
        """B(V) = V . D K for a physical vector V (jets)."""
        return gtg.m_add(*[gtg.m_scal(c, self.Bj[b[0]]) for b, c in V.items()])

    def torsion_jets(self):
        """the torsion D_mu g_nu - D_nu g_mu vanishes as jets (to the order of Omega)."""
        f = self.fld
        return all(mzero(gtg.m_add(gtg.m_d(f.g[nu], mu), gtg.m_neg(gtg.m_d(f.g[mu], nu)),
                                   gtg.comm(f.Om[mu], f.g[nu], S13), gtg.m_neg(gtg.comm(f.Om[nu], f.g[mu], S13))))
                   for mu in range(D) for nu in range(mu + 1, D))

    def closed_form_holds(self):
        """as jets: HJ inverts the matrix of hb^{-1}, and Omega satisfies the torsion equation."""
        f = self.fld
        inverse = all(jzero(sum((f.TH[a][mu] * self.HJ[mu][c] for mu in range(D)), ZJ) - (1 if a == c else 0))
                      for a in range(D) for c in range(D))
        return inverse and self.torsion_jets()

    # -- the congruence ---------------------------------------------------------------------------------
    def theta(self):
        return sum((self.Bj[c].get((c,), ZJ) for c in range(D)), ZJ)

    def tr_B2(self):
        return sum((self.Bj[c].get((a,), ZJ) * self.Bj[a].get((c,), ZJ) for a in range(D) for c in range(D)), ZJ)

    def shear2(self):
        """<sigma, sigma> = tr B^2 - theta^2/2."""
        th = self.theta()
        return self.tr_B2() - F(1, 2) * th * th

    def screen(self):
        """m_i = e_i - (K . e_i) l, i = 1, 2 (jets)."""
        return [gtg.m_sub(E[i], gtg.m_scal(vdot(self.K, E[i]), LV)) for i in TR]

    def connecting(self):
        """background vectors x_i = E(e_i) + alpha_i l, alpha_i fixed by x_i . grad phi = 0 (components, jets)."""
        out = []
        for i in range(2):
            alpha = ZJ
            for j, m in PAIRS:
                alpha = alpha + self.Ej[j][i] * self.Sj[j][m] * self.Y[m]
            out.append([ZJ, alpha, self.Ej[0][i], self.Ej[1][i]])
        return out

    def lie(self, xb):
        """(k . grad) x - (x . grad) k, components (jets)."""
        return [sum((self.k[nu] * xb[mu].d(nu) - xb[nu] * self.k[mu].d(nu) for nu in range(D)), ZJ)
                for mu in range(D)]

    def phys(self, xb):
        """hb^{-1} of a background vector given by components."""
        return gtg.m_add(*[gtg.m_scal(xb[mu], self.fld.g[mu]) for mu in range(D) if xb[mu]])

    def rho4(self):
        """-(hb^{-1}(x_1 ^ x_2))^2 for the two connecting vectors, the Gram determinant, and det E."""
        X1, X2 = (self.phys(x) for x in self.connecting())
        blade = gtg.outer(X1, X2, S13)
        square = gtg.m_mul(blade, blade, S13)
        gram = vdot(X1, X1) * vdot(X2, X2) - vdot(X1, X2) * vdot(X1, X2)
        det = self.Ej[0][0] * self.Ej[1][1] - self.Ej[0][1] * self.Ej[1][0]
        return ZJ - square.get((), ZJ), all(len(b) == 0 for b in square), gram, det

    # -- curvature at the point -------------------------------------------------------------------------
    def curvature(self):
        return gtg.as_op(self.fld.curvature())

    def k_ric_k(self, Rop):
        Kv = gtg.m_val(self.K)
        return gtg.vdot(Kv, gtg.ricci(Rop, Kv, S13), S13)

    def lam_series(self, j, n):
        """coefficients in d lam, through order n, of a jet that depends on the point through lam only."""
        if any(e[1] or e[2] or e[3] for e in j.c):
            raise ValueError("the jet depends on more than lam")
        return [j.coeff((k, 0, 0, 0)) for k in range(n + 1)]


def shape_rate(wave):
    """G^{-1} G' at the point, and det G: G_ij = -X_i . X_j is the matrix, in the basis of the two physical
    separations X_i = hb^{-1}(x_i), of minus the product on the screen, computed from the gauge field, and G'
    its derivative along the generator."""
    Xs = [wave.phys(x) for x in wave.connecting()]
    G = [[ZJ - vdot(Xs[i], Xs[j]) for j in range(2)] for i in range(2)]
    Gv = [[G[i][j].v for j in range(2)] for i in range(2)]
    dG = [[wave.along(G[i][j]).v for j in range(2)] for i in range(2)]
    d = Gv[0][0] * Gv[1][1] - Gv[0][1] * Gv[1][0]
    inv = [[Gv[1][1] / d, -Gv[0][1] / d], [-Gv[1][0] / d, Gv[0][0] / d]]
    return [[sum((inv[i][k] * dG[k][j] for k in range(2)), F(0)) for j in range(2)] for i in range(2)], d


def tr_square(M):
    return sum((M[i][j] * M[j][i] for i, j in PAIRS), F(0))


def w_at(w, i, j):
    return w[i][j][0] if w[i][j] else F(0)


def congruence_series(wave, n):
    """theta, <sigma, sigma>, tr w and rho (rho(0) = 1) as series in d lam; theta, shear through n, rho through n + 1."""
    th = wave.lam_series(wave.theta(), n)
    sh = wave.lam_series(wave.shear2(), n)
    r4, scalar, gram, det = wave.rho4()
    if not (scalar and jzero(r4 - gram) and jzero(r4 - det * det)):
        raise ValueError("area density")
    rho = s_pow(wave.lam_series(r4, n + 1), F(1, 4), n + 1)
    trw = [(wave.w[0][0][k] if k < len(wave.w[0][0]) else F(0)) + (wave.w[1][1][k] if k < len(wave.w[1][1]) else F(0))
           for k in range(n + 1)]
    return th, sh, trw, rho


# ---------------------------------------------------------------------------------------------------------
# checks
# ---------------------------------------------------------------------------------------------------------

def check_plane_wave_is_an_exact_field_with_the_stored_first_order_curvature():
    premise("synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators")
    ok, vacuum, planes = True, 0, 0
    for w in PROFILES:
        wave = Wave(profile(w), S_ZERO, X0, LOW)
        fld = wave.fld
        ok = ok and fld.torsion_free()
        # Omega solved from the torsion equation is (a.l) grad H ^ l, as jets
        ok = ok and all(mzero(gtg.m_sub(fld.om[c], wave.om_closed[c])) for c in range(D))
        ok = ok and any(gtg.m_val(fld.om[c]) for c in range(D))
        # and hb, inverted as jets, is a + H (a.l) l: the closed forms that the series of order eight use
        twin = Wave(profile(w), S_ZERO, X0, LOW, closed=True)
        ok = ok and twin.closed_form_holds()
        ok = ok and all(jzero(wave.HJ[mu][c] - twin.HJ[mu][c]) for mu in range(D) for c in range(D))
        # hb is invertible with determinant one: hb^{-1}(l) = l, and hb^{-1}(a) . hb^{-1}(b) = a.b - 2H (a.l)(b.l)
        ok = ok and GA.eq(fld.hb_inv({(1,): F(1)}), LV)
        ok = ok and det([[g.get((a,), ZJ).v for g in fld.g] for a in range(D)]) == det(FRAME_OF_LABELS)
        metric = fld.metric()
        ok = ok and all(metric[m][k] == GRAM[m][k] - 2 * wave.H.v * L_LABEL[m] * L_LABEL[k]
                        for m in range(D) for k in range(D)) and wave.H.v != 0
        # the curvature is R(B) = -l ^ w(B.l): the stored first-order curvature -1/2 p ^ h(B.p) at p = l, h = 2w
        Rop = wave.curvature()
        for a in range(D):
            for b in range(a + 1, D):
                Bab = gtg.wedge(E[a], E[b], S13)
                v = gtg.bdot(Bab, LV, S13)                        # B . l
                hv = {}
                for i, ei in enumerate(TR):
                    for j, ej in enumerate(TR):
                        hv = gtg.m_add(hv, gtg.m_scal(-2 * w_at(wave.w, i, j) * gtg.vdot(v, E[ej], S13), E[ei]))
                want = gtg.m_scal(F(-1, 2), gtg.wedge(LV, hv, S13))
                ok = ok and GA.eq(Rop(Bab), want)
                planes += 0 if GA.is_zero(want) else 1
        # Ricci map (tr w)(a.l) l: the field is vacuum exactly when the profile is trace-free
        trw = w_at(wave.w, 0, 0) + w_at(wave.w, 1, 1)
        ok = ok and all(GA.eq(gtg.ricci(Rop, E[a], S13), gtg.m_scal(trw * L_FRAME[a], LV)) for a in range(D))
        ok = ok and gtg.ricci_flat(Rop, S13) == (trw == 0)
        vacuum += 1 if gtg.ricci_flat(Rop, S13) else 0
    ok = ok and vacuum == 3 and planes == 20
    GA.check("(vi) the plane wave hb^{-1}(a) = a - H (a.l) l with H = 1/2 w_ij(l.x) y^i y^j, at amplitudes that are "
             "not small: Omega solved from the torsion equation is (a.l) grad H ^ l; det hb = 1; the curvature "
             "operator is the stored first-order curvature of 2w at the null momentum l, exactly; the Ricci map is "
             "(tr w)(a.l) l, zero exactly for the three trace-free profiles of five", ok)
    return ok


def check_null_gradient_of_the_wave_and_its_parallel_screen():
    premise("synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators")
    ok, count = True, 0
    for w, S0 in ((W_BOTH, S_OUT), (W_CROSS, S_IN), (W_MATTER, S_OUT), (W_ANTI, S_IN)):
        wave = Wave(profile(w), S0, X0, LOW)
        Kv = gtg.m_val(wave.K)
        # K is null as a jet, is not n, and l.x is its affine parameter: l . hb(K) = 1
        ok = ok and jzero(vdot(wave.K, wave.K)) and not GA.eq(Kv, NV)
        ok = ok and jzero(wave.k[0] - 1)
        # clause (iii)(a) of the first-order result: B symmetric, B(K) = 0, K . B(A) = 0
        Bv = [gtg.m_val(b) for b in wave.Bj]
        ok = ok and all(gtg.vdot(E[a], Bv[b], S13) == gtg.vdot(E[b], Bv[a], S13) for a in range(D) for b in range(D))
        ok = ok and mzero(wave.B(wave.K)) and all(jzero(vdot(wave.K, b)) for b in wave.Bj)
        # the screen frame: orthonormal, orthogonal to K, parallel along the generators, and B is S in it
        m = wave.screen()
        ok = ok and all(jzero(vdot(wave.K, mi)) and jzero(vdot(mi, mi) + 1) for mi in m) and jzero(vdot(m[0], m[1]))
        ok = ok and all(mzero(wave.cov_K(mi)) for mi in m)
        for i in range(2):
            image = gtg.m_add(gtg.m_scal(wave.Sj[0][i], m[0]), gtg.m_scal(wave.Sj[1][i], m[1]))
            ok = ok and mzero(gtg.m_sub(wave.B(m[i]), image)) and bool(gtg.m_val(image))
        th, sh = wave.theta(), wave.shear2()
        S = [[wave.Sj[i][j] for j in range(2)] for i in range(2)]
        ok = ok and jzero(th - S[0][0] - S[1][1]) and th.v != 0
        ok = ok and jzero(sh - F(1, 2) * (S[0][0] - S[1][1]) * (S[0][0] - S[1][1]) - 2 * S[0][1] * S[1][0])
        ok = ok and sh.v > 0
        # the curvature form C(m_i, m_j) = (K ^ m_j) . R(K ^ m_i) is w_ij, and K . R(K) = tr w
        Rop = wave.curvature()
        mv = [gtg.m_val(mi) for mi in m]
        for i, j in PAIRS:
            form = gtg.bb_dot(gtg.wedge(Kv, mv[j], S13), Rop(gtg.wedge(Kv, mv[i], S13)), S13)
            ok = ok and form == w_at(wave.w, i, j)
        ok = ok and wave.k_ric_k(Rop) == w_at(wave.w, 0, 0) + w_at(wave.w, 1, 1)
        count += 1
    ok = ok and count == 4
    GA.check("(vi) phi = n.x - 1/2 S_ij y^i y^j with S' = w - S^2 has a null gradient K = hb^T(grad phi) with "
             "affine parameter l.x; B(A) = A.D K is symmetric and annihilates K; the frame m_i = e_i - (K.e_i) l "
             "is orthonormal, orthogonal to K and parallel along K, and B(m_i) = S_ji m_j; theta = tr S, "
             "<sigma, sigma> = tr S^2 - theta^2/2; (K^m_j).R(K^m_i) = w_ij and K.R(K) = tr w (four strong waves)", ok)
    return ok


def check_area_density_and_the_linear_focusing_equation_on_strong_waves():
    premise("synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators")
    premise("synthesis.field-equation-linear-in-the-curvature-with-a-conserved-source-is-einsteins")
    ok, count, vacuum, signs = True, 0, 0, []
    for w, S0 in ((W_BOTH, S_OUT), (W_PLUS, S_IN), (W_CROSS, S_OUT), (W_MATTER, S_IN), (W_ANTI, S_OUT)):
        wave = Wave(profile(w), S0, X0, LOW, E0=E_START)
        # the two connecting vectors are tangent to the hypersurface and commute with hb(K)
        xs = wave.connecting()
        ok = ok and all(jzero(sum((x[mu] * wave.phi.d(mu) for mu in range(D)), ZJ)) for x in xs)
        ok = ok and all(jzero(c) for x in xs for c in wave.lie(x))
        ok = ok and all(jzero(vdot(wave.phys(x), wave.K)) for x in xs)
        # rho^4 = -(hb^{-1}(x_1 ^ x_2))^2 is the Gram determinant, equals (det E)^2, and d rho^4/d lam = 2 theta rho^4
        r4, scalar, gram, det = wave.rho4()
        th = wave.theta()
        ok = ok and scalar and jzero(r4 - gram) and jzero(r4 - det * det) and r4.v == 25
        d1 = wave.along(r4)
        ok = ok and jzero(d1 - 2 * th * r4) and d1.v != 0
        # the shape: with G the Gram matrix of the two physical separations, from the gauge field (not the
        # identity at the point), G^{-1} G' = theta + 2 sigma, so qbar^{-1} qbar' = G^{-1} G' - theta and
        # <sigma, sigma> = 1/4 tr((qbar^{-1} qbar')^2)
        rate, detG = shape_rate(wave)
        ok = ok and detG == r4.v and rate[0][0] + rate[1][1] == 2 * th.v
        qrate = [[rate[i][j] - (th.v if i == j else 0) for j in range(2)] for i in range(2)]
        ok = ok and F(1, 4) * tr_square(qrate) == wave.shear2().v and qrate[0][1] != qrate[1][0]
        # rho''/rho from rho^4: 1/4 r''/r - 3/16 (r'/r)^2, against -1/2 (<sigma, sigma> - K.R(K))
        d2 = wave.along(d1)
        lhs = F(1, 4) * d2.v / r4.v - F(3, 16) * (d1.v / r4.v) ** 2
        Rop = wave.curvature()
        krk = wave.k_ric_k(Rop)
        ok = ok and lhs == F(-1, 2) * (wave.shear2().v - krk) and lhs != 0
        # for null K the Einstein map and the Ricci map agree on K: the term is the K-K part of the field equation
        Kv = gtg.m_val(wave.K)
        ok = ok and gtg.vdot(Kv, gtg.einstein(Rop, Kv, S13), S13) == krk
        vacuum += 1 if krk == 0 else 0
        signs.append(sign(krk))
        count += 1
    ok = ok and count == 5 and vacuum == 3 and signs == [0, 0, 0, -1, 1]
    GA.check("(i), (ii) on five waves that are not weak: the connecting vectors commute with hb(K); "
             "rho^4 = -(hb^{-1}(x_1 ^ x_2))^2 obeys d rho/d lam = theta rho/2; the Gram matrix G of the separations, "
             "from the gauge field and not the identity at the point, has tr G^{-1}G' = 2 theta and "
             "1/4 tr((G^{-1}G' - theta)^2) = <sigma, sigma>; and "
             "rho'' = -1/2 (<sigma, sigma> - K.R(K)) rho with K.R(K) = K.G(K) computed from the gauge fields, "
             "zero on the three vacuum waves, negative and positive on the other two", ok)
    return ok


def plane_data_series(w, n):
    """for each amplitude: the wave of profile amp * w with S = 0 at the point (a null plane to second order),
    the closed forms of hb and Omega tested as jets; returns {amp: (theta, shear2, tr w, rho)} as series in d lam, or None."""
    out = {}
    for amp in AMPLITUDES:
        wave = Wave(profile(w, amp), S_ZERO, X0, HIGH, closed=True)
        if not (wave.closed_form_holds() and jzero(vdot(wave.K, wave.K))):
            return None
        out[amp] = congruence_series(wave, n)
    return out


def orders(data, pick, power):
    """the coefficient of d lam^power of the series pick(data[amp]) as a polynomial in the amplitude."""
    xs = list(data)
    return interpolate(xs, [pick(data[x])[power] for x in xs])


def check_orders_one_to_four_in_the_amplitude_on_a_null_plane():
    premise("synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators")
    n = SERIES
    ok = True
    vac, mat = plane_data_series(W_BOTH, n), plane_data_series(W_MATTER, n)
    ok = ok and vac is not None and mat is not None
    for data in (vac, mat) if ok else ():
        for amp, (th, sh, trw, rho) in data.items():
            src = s_add(sh, trw, -1)                                               # <sigma, sigma> - K.R(K)
            # (i), (ii) as series: rho' = theta rho/2 and rho'' = -1/2 (<sigma, sigma> - K.R(K)) rho
            ok = ok and same(s_der(rho), s_scal(F(1, 2), s_mul(th, rho, n)), n)
            ok = ok and same(s_der(s_der(rho)), s_scal(F(-1, 2), s_mul(src, rho, n)), n - 1)
            # (iii): with ds = d lam/rho and e_0 = 0, ln rho^2 = -int (s - s') (<sigma, sigma> - K.R(K))_s ds'
            s = s_int(s_inv(rho, n))
            dens = s_mul(rho, src, n)
            rhs = s_add(s_mul(s, s_int(dens), n + 1), s_int(s_mul(s, dens, n)), -1)
            ok = ok and same(s_log(s_mul(rho, rho, n + 1), n + 1), s_scal(-1, rhs), n + 1)
    if ok:
        # vacuum: the area density does not respond at first order (the first-order result's trace is free of the
        # wave), its first response is at second order, and odd orders vanish
        r4 = orders(vac, lambda d: d[3], 4)
        r8 = orders(vac, lambda d: d[3], 8)
        ok = ok and r4 == [0, 0, F(-61, 48), 0, 0, 0]
        ok = ok and r8 == [0, 0, F(-1, 504), 0, F(-40931, 53760), 0]
        ok = ok and all(orders(vac, lambda d: d[3], j)[1] == 0 for j in range(n + 2))
        # theta = -int <sigma, sigma> at second order: -(tr w_0^2)/3 d lam^3 with tr w_0^2 = 61/2; fourth order at d lam^7
        ok = ok and orders(vac, lambda d: d[0], 3) == [0, 0, F(-61, 6), 0, 0, 0]
        ok = ok and orders(vac, lambda d: d[1], 2) == [0, 0, F(61, 2), 0, 0, 0]
        ok = ok and orders(vac, lambda d: d[0], 7) == [0, 0, F(-2, 63), 0, F(-63257, 2520), 0]
        # with matter every order from the first appears: theta = int K.R(K) at first order (tr w = -2 at the
        # point), rho = 1 - 1/2 d lam^2 at first order, and orders two, three and four of rho at d lam^8
        ok = ok and orders(mat, lambda d: d[0], 1) == [0, F(-2), 0, 0, 0, 0]
        ok = ok and orders(mat, lambda d: d[3], 2) == [0, F(-1, 2), 0, 0, 0, 0]
        ok = ok and orders(mat, lambda d: d[3], 8) == [0, 0, F(-11, 2688), F(-341, 8064), F(-1159, 2560), 0]
    GA.check("(ii), (iii), (vi) on a null plane crossed by the wave, by interpolation in six amplitudes with jets of "
             "order eight: rho'' = -1/2 (<sigma, sigma> - K.R(K)) rho and ln rho^2 = -int (s - s') (<sigma, sigma> "
             "- K.R(K))_s ds' hold as series; in vacuum rho has no first-order term, -61/48 d lam^4 at second order, "
             "-40931/53760 d lam^8 at fourth, and theta = -61/6 d lam^3 at second; with matter rho has the orders "
             "one (-1/2 d lam^2), two, three and four (-1159/2560 d lam^8)", ok)
    return ok


def check_integrated_forms_in_the_parameter_s_and_in_the_area_parameter():
    premise("synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators")
    n = SERIES
    ok, slopes, vacuum, in_rho = True, [], 0, 0
    for w, S0 in ((W_BOTH, S_OUT), (W_BOTH, S_IN), (W_MATTER, S_OUT), (W_ANTI, S_IN)):
        wave = Wave(profile(w), S0, X0, HIGH, closed=True)
        ok = ok and wave.closed_form_holds() and jzero(vdot(wave.K, wave.K))
        th, sh, trw, rho = congruence_series(wave, n)
        src = s_add(sh, trw, -1)
        p = s_der(rho)                                                            # d rho/d lam
        slopes.append(p[0])
        ok = ok and p[0] == F(1, 2) * th[0]
        # parameter s, ds = d lam/rho, e = 2 d rho/d lam: ln(rho^2) = e_0 s - int (s - s') (<s,s> - K.R(K))_s ds'
        s = s_int(s_inv(rho, n))
        dens = s_mul(rho, src, n)
        rhs = s_add(s_mul(s, s_int(dens), n + 1), s_int(s_mul(s, dens, n)), -1)
        ok = ok and same(s_log(s_mul(rho, rho, n + 1), n + 1), s_add(s_scal(2 * p[0], s), rhs, -1), n + 1)
        # and e(s) = e_0 - int (<s,s> - K.R(K))_s ds: 2 p = 2 p_0 - int rho (<s,s> - K.R(K)) d lam
        ok = ok and same(s_scal(2, p), s_add([2 * p[0]], s_int(dens), -1), n)
        # area parameter: d(p^2)/d rho = -rho <s,s>_rho p^2 + rho K.R(K); multiplied by p it is a series identity
        ok = ok and same(s_der(s_mul(p, p, n)), s_scal(-1, s_mul(dens, p, n)), n - 1)
        if all(c == 0 for c in trw):
            # vacuum: ln(p/p_0) = -Xi, Xi = 1/2 int rho <s,s>_rho d rho = 1/2 int rho <s,s> / p d lam, and
            # lam - lam_0 = (1/p_0) int e^Xi d rho, that is e^Xi p = p_0
            xi = s_scal(F(1, 2), s_int(s_mul(dens, s_inv(p, n), n - 1)))
            ok = ok and same(s_log_ratio(p, n), s_scal(-1, xi), n) and sign(xi[1] * p[0]) == 1
            vacuum += 1
        # the same in the variable x = rho - 1 itself (rho_0 = 1): lam as a series in x by reversion, then
        # d(p^2)/d rho = rho (K.R(K) - <s,s>), and in vacuum p = p_0 exp(-Xi), Xi = 1/2 int rho <s,s>/p^2 d rho,
        # lam - lam_0 = (1/p_0) int exp(Xi) d rho
        lam_x = s_revert(s_add(rho, [F(1)], -1), n + 1)
        p_x, src_x = s_compose(p, lam_x, n), s_compose(src, lam_x, n)
        rho_x = [F(1), F(1)]
        ok = ok and same(s_der(s_mul(p_x, p_x, n)), s_scal(-1, s_mul(rho_x, src_x, n)), n - 1)
        if all(c == 0 for c in trw):
            xi_x = s_scal(F(1, 2), s_int(s_mul(s_mul(rho_x, src_x, n), s_inv(s_mul(p_x, p_x, n), n), n)))
            ok = ok and same(s_log_ratio(p_x, n), s_scal(-1, xi_x), n)
            ok = ok and same(lam_x, s_scal(1 / p[0], s_int(s_exp(xi_x, n))), n + 1) and sign(xi_x[1]) == 1
            in_rho += 1
    ok = ok and slopes == [F(23, 42), F(-43, 56), F(23, 42), F(-43, 56)] and vacuum == 2 and in_rho == 2
    GA.check("(iii) with expansion at the point (d rho/d lam = 23/42 and -43/56), on strong waves with and without "
             "matter, as series to order eight: ln rho^2 = e_0 s - int (s - s')(<sigma, sigma> - K.R(K))_s ds' and "
             "e = e_0 - int (<sigma, sigma> - K.R(K))_s ds in the parameter s; with rho as the variable (lam reverted "
             "as a series in rho) d(p^2)/d rho = -rho <sigma, sigma>_rho p^2 + rho K.R(K), and in vacuum "
             "p = p_0 exp(-Xi), lam - lam_0 = (1/p_0) int exp(Xi) d rho", ok)
    return ok


def power_law_wave(a, lam1):
    """the vacuum wave w = diag(c, -c)/lam^2 that form (beta) gives for the shape diag(rho^a, rho^-a), at lam1."""
    den = 1 + a * a / 4
    p1, p2 = (1 + a / 2) / den, (1 - a / 2) / den
    inv2 = [F((-1) ** k * (k + 1)) / lam1 ** (k + 2) for k in range(LOW + 3)]      # 1/lam^2 about lam1
    w = [[s_scal(p1 * (p1 - 1), inv2), []], [[], s_scal(p2 * (p2 - 1), inv2)]]
    return Wave(w, ((p1 / lam1, 0), (0, p2 / lam1)), point(lam1), LOW), p1, p2


def check_exact_power_law_waves_and_the_area_as_a_clock():
    premise("synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators")
    ok, curved, flat = True, 0, 0
    for lam1 in POWER_LAW_LAMS:
        for a in POWER_LAW_A:
            wave, p1, p2 = power_law_wave(a, lam1)
            fld, Rop = wave.fld, wave.curvature()
            ok = ok and fld.torsion_free() and gtg.ricci_flat(Rop, S13) and jzero(vdot(wave.K, wave.K))
            ok = ok and p1 * p1 + p2 * p2 == p1 + p2                              # trace-free profile
            is_flat = all(not Rop(gtg.wedge(E[i], E[j], S13)) for i in range(D) for j in range(i + 1, D))
            ok = ok and is_flat == (a * a in (0, 4))
            flat += 1 if is_flat else 0
            curved += 0 if is_flat else 1
            th = wave.theta()
            t0, t1, sh = th.v, wave.along(th).v, wave.shear2().v
            ok = ok and t0 * lam1 == p1 + p2 and sign(t0) == 1
            # the shape, from the Gram matrix of the separations computed from the gauge field: with
            # qbar = diag(rho^a, rho^-a), qbar^{-1} qbar' = a (rho'/rho) diag(1, -1) = (a theta/2) diag(1, -1)
            rate, detG = shape_rate(wave)
            ok = ok and detG == 1 and rate[0][1] == 0 and rate[1][0] == 0
            ok = ok and rate[0][0] - t0 == a * t0 / 2 and rate[1][1] - t0 == -a * t0 / 2
            ok = ok and sh == a * a * t0 * t0 / 8
            # form (beta) at the point: d ln p/d ln rho = rho rho''/rho'^2 = -a^2/4
            ok = ok and (t1 / 2 + t0 * t0 / 4) / (t0 * t0 / 4) == -a * a / 4
            # the clock at the point: d ln lam/d ln rho = 2/(lam theta) = 1 + a^2/4
            ok = ok and 2 / (lam1 * t0) == 1 + a * a / 4
            # the bound, towards decreasing lam (expansion -theta there): rho = 0 at lam = 0, within 2/theta of
            # lam1; the slack 2/theta - lam1 is lam1 a^2/4, zero exactly when there is no shear
            slack = 2 / t0 - lam1
            ok = ok and slack == lam1 * a * a / 4 and (slack == 0) == (a == 0)
    ok = ok and curved == 8 and flat == 4
    GA.check("(iii), (iv), (viii) exact vacuum waves w = diag(c, -c)/lam^2 for six values of a (four with curvature, "
             "amplitudes of order one), each at two sample points: the Gram matrix of the separations, from the "
             "gauge field, has qbar^{-1} qbar' = (a theta/2) diag(1, -1), the rate of the shape diag(rho^a, rho^-a); "
             "<sigma, sigma> = a^2 theta^2/8; d ln p/d ln rho = -a^2/4 and d ln lam/d ln rho = 1 + a^2/4 at the "
             "sample point, as form (beta) gives; rho vanishes within 2/|theta|, with slack lam a^2/4", ok)
    return ok


def check_focusing_bound_and_exact_caustics():
    premise("synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators")
    premise("synthesis.field-equation-linear-in-the-curvature-with-a-conserved-source-is-einsteins")
    ok, count, reach, at_caustic = True, 0, [], 0
    # (1) a wave with matter of positive null energy: E = diag(1, b), b = 1 - 3/2 lam^2 + 1/2 lam^3, a null plane
    # at lam = 0 (b = 1, b' = 0); w = diag(0, b''/b) = diag(0, -6/(2 + 2 lam - lam^2)); b(1) = 0, b'(1) = -3/2
    b = [F(1), F(0), F(-3, 2), F(1, 2)]
    q = [F(2), F(2), F(-1)]
    ok = ok and sum(b) == 0 and sum(s_der(b)) == F(-3, 2) and s_der(b)[0] == 0
    for lam1 in DUST_POINTS:
        bl = shifted(b, lam1)                                                      # b about lam1
        w22 = s_scal(-6, rational_series([1], shifted(q, lam1), HIGH))
        wave = Wave([[[], []], [[], w22]], ((0, 0), (0, bl[1] / bl[0])), point(lam1), LOW)
        # the profile used is b''/b, and the second column of the Jacobi map of the wave is b
        ok = ok and padded(s_mul(w22, bl, HIGH), HIGH) == padded(s_der(s_der(bl)), HIGH)
        ok = ok and padded(wave.Ec[1][1], LOW) == padded(s_scal(1 / bl[0], bl), LOW)
        Rop = wave.curvature()
        krk = wave.k_ric_k(Rop)
        th = wave.theta()
        ok = ok and wave.fld.torsion_free() and jzero(vdot(wave.K, wave.K))
        ok = ok and krk == w22[0] and sign(krk) == -1 and th.v == bl[1] / bl[0] and sign(th.v) == -1
        ok = ok and gtg.vdot(gtg.m_val(wave.K), gtg.einstein(Rop, gtg.m_val(wave.K), S13), S13) == krk
        # rho^2 = b: rho is concave, and the caustic at lam = 1 lies within 2/|theta| of lam1
        r4, scalar, gram, det = wave.rho4()
        ok = ok and scalar and jzero(r4 - det * det) and sign(wave.shear2().v - krk) == 1
        reach.append(lam1 + 2 / -th.v)
        count += 1
    ok = ok and reach == [F(85, 28), F(31, 18), F(229, 180), F(3271, 2970)] and all(r >= 1 for r in reach)
    # (2) vacuum waves smooth for every lam with a caustic where they are smooth: w = diag(-g, g),
    # g = 6c/(1 + c t^2), t = 1 - lam; the second column of E is b = t + c t^3, zero at lam = 1 with b' = -1
    for c in SMOOTH_WAVES:
        bt = [F(0), F(-1), F(0), -c]                                               # b in the variable lam - 1
        for lam1 in SMOOTH_POINTS:
            t1 = 1 - lam1
            bl = shifted(bt, -t1)                                                  # b about lam1
            g = s_scal(6 * c, rational_series([1], [1 + c * t1 * t1, -2 * c * t1, c], HIGH))
            ok = ok and padded(s_mul(g, bl, HIGH), HIGH) == padded(s_der(s_der(bl)), HIGH)
            if t1:
                wave = Wave([[s_scal(-1, g), []], [[], g]], ((S11_SAMPLE, 0), (0, bl[1] / bl[0])), point(lam1), LOW)
                ok = ok and jzero(vdot(wave.K, wave.K)) and sign(wave.theta().v - S11_SAMPLE) == -1
                ok = ok and padded(wave.Ec[1][1], LOW) == padded(s_scal(1 / bl[0], bl), LOW)
            else:
                # at the caustic itself the field is smooth and vacuum, with curvature (n ^ e_2) . R(n ^ e_2) = 6c
                wave = Wave([[s_scal(-1, g), []], [[], g]], S_ZERO, point(lam1), LOW)
                ok = ok and bl[0] == 0 and bl[1] == -1
                at_caustic += 1
                ok = ok and gtg.bb_dot(gtg.wedge(NV, E[2], S13), wave.curvature()(gtg.wedge(NV, E[2], S13)), S13) == 6 * c
            ok = ok and wave.fld.torsion_free() and gtg.ricci_flat(wave.curvature(), S13)
            count += 1
    # (3) a vacuum wave taking a null plane to a caustic: w = diag(6/q, -6/q), q = 2 + 2 lam - lam^2, smooth and
    # positive on [0, 1]; S = 0 at lam = 0. The second column of E is the same b (b'' = -(6/q) b, b(0) = 1,
    # b'(0) = 0, b(1) = 0); the first is f with f'' = (6/q) f, f(0) = 1, f'(0) = 0, which is at least 1 on [0, 1]
    # (the proof), so det E = f b first vanishes at lam = 1 exactly
    g0 = s_scal(6, rational_series([1], q, HIGH))
    Ec = jacobi(riccati([[g0, []], [[], s_scal(-1, g0)]], S_ZERO, HIGH), HIGH)
    ok = ok and Ec[1][1] == padded(b, HIGH) and not any(Ec[0][1]) and not any(Ec[1][0])
    ok = ok and Ec[0][0][:5] == [F(1), F(0), F(3, 2), F(-1, 2), F(3, 4)]
    wave = Wave([[g0, []], [[], s_scal(-1, g0)]], S_ZERO, point(0), LOW)
    Rop = wave.curvature()
    ok = ok and wave.fld.torsion_free() and gtg.ricci_flat(Rop, S13) and jzero(vdot(wave.K, wave.K))
    ok = ok and GA.eq(gtg.m_val(wave.K), NV) and wave.theta().v == 0 and wave.shear2().v == 0
    ok = ok and gtg.bb_dot(gtg.wedge(NV, E[2], S13), Rop(gtg.wedge(NV, E[2], S13)), S13) == -3
    r4, scalar, gram, det = wave.rho4()
    ok = ok and scalar and jzero(r4 - det * det) and wave.lam_series(r4, LOW) == [F(1), F(0), F(0)]
    # and at lam = 1, where b vanishes, the field is smooth and vacuum, with (n ^ e_2) . R(n ^ e_2) = -6/q(1) = -2
    g1 = s_scal(6, rational_series([1], shifted(q, 1), HIGH))
    end = Wave([[g1, []], [[], s_scal(-1, g1)]], S_ZERO, point(1), LOW)
    ok = ok and end.fld.torsion_free() and gtg.ricci_flat(end.curvature(), S13)
    ok = ok and gtg.bb_dot(gtg.wedge(NV, E[2], S13), end.curvature()(gtg.wedge(NV, E[2], S13)), S13) == -2
    ok = ok and count == 8 and at_caustic == 2
    GA.check("(iv), (vii) a wave with matter of positive null energy (K.R(K) = -6/(2 + 2 lam - lam^2) < 0) crossing a "
             "null plane: rho^2 = 1 - 3/2 lam^2 + 1/2 lam^3 exactly, zero at lam = 1, within 2/|theta| of each of "
             "four points; vacuum waves w = diag(-g, g), g = 6c/(1 + c(1 - lam)^2), smooth for every lam, with "
             "the Jacobi field (1 - lam) + c (1 - lam)^3 vanishing at lam = 1, where the field is smooth and vacuum; "
             "and a vacuum wave w = diag(6, -6)/(2 + 2 lam - lam^2) crossing a null plane (S = 0 at lam = 0) whose "
             "Jacobi map has the column 1 - 3/2 lam^2 + 1/2 lam^3, zero at lam = 1, where the field is smooth", ok)
    return ok
