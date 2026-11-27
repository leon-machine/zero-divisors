"""Plane-wave toolkit for the experiments (exact; jets from lib/gtg.py)."""
import sys
sys.path.insert(0, 'lib')
from fractions import Fraction as F
import GA, gtg
from GA import add, gen, mul, scal, sub
Jet = gtg.Jet
D = 4; S = GA.sig(1, 3); ETA = [1, -1, -1, -1]
E = [gen(i) for i in range(D)]
NUP = [1, 0, 0, 1]; NLOW = [1, 0, 0, -1]          # n = e0 + e3; n.e_mu
ZJ = Jet.const(0, D)

def polymul(a, b, n):
    out = [F(0)] * (n + 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if i + j <= n and y:
                    out[i + j] += x * y
    return out

def riccati(w, S0, n):
    """Taylor coefficients (in du) of the symmetric 2x2 S with S' = w - S^2, S(0) = S0; w[i][j] = list of coeffs."""
    Sc = [[[F(S0[i][j])] for j in range(2)] for i in range(2)]
    for k in range(n):
        # coefficient k of w - S^2
        for i in range(2):
            for j in range(2):
                pass
        new = [[None, None], [None, None]]
        for i in range(2):
            for j in range(2):
                s2 = F(0)
                for m in range(2):
                    for a in range(k + 1):
                        s2 += Sc[i][m][a] * Sc[m][j][k - a]
                wk = w[i][j][k] if k < len(w[i][j]) else F(0)
                new[i][j] = (F(wk) - s2) / (k + 1)
        for i in range(2):
            for j in range(2):
                Sc[i][j].append(new[i][j])
    return Sc

def jacobi(Sc, n):
    """E with E' = S E, E(0) = 1 (Taylor coefficients)."""
    Ec = [[[F(1 if i == j else 0)] for j in range(2)] for i in range(2)]
    for k in range(n):
        new = [[None, None], [None, None]]
        for i in range(2):
            for j in range(2):
                acc = F(0)
                for m in range(2):
                    for a in range(k + 1):
                        acc += Sc[i][m][a] * Ec[m][j][k - a]
                new[i][j] = acc / (k + 1)
        for i in range(2):
            for j in range(2):
                Ec[i][j].append(new[i][j])
    return Ec

def series_jet(coeffs, du):
    out = Jet.const(0, D)
    p = Jet.const(1, D)
    for c in coeffs:
        if c:
            out = out + p * c
        p = p * du
    return out

class Wave(object):
    def __init__(self, w, S0, x0, order, analytic=False):
        """w[i][j]: Taylor coefficient lists in du = u - u0 (u0 = n.x0); order = jet order of Omega."""
        self.order = order
        self.x0 = x0
        u0 = x0[0] - x0[3]
        self.u0 = u0
        n = order + 3
        self.w = w
        self.Sc = riccati(w, S0, n)
        self.Ec = jacobi(self.Sc, n)

        def hbinv(X):
            t, x, y, z = X
            du = t - z - u0
            wj = [[series_jet(w[i][j], du) for j in range(2)] for i in range(2)]
            H = F(1, 2) * (wj[0][0] * x * x + 2 * wj[0][1] * x * y + wj[1][1] * y * y)
            self.X = X
            self.du = du
            return [[(1 if mu == a else 0) - H * NLOW[mu] * NUP[a] for a in range(D)] for mu in range(D)]
        if analytic:
            X = [Jet.var(i, x0[i], D, order + 1) for i in range(D)]
            rows = hbinv(X)
            TH = [[rows[mu][a] for mu in range(D)] for a in range(D)]
            t, x, y, z = X
            wj = [[series_jet(w[i][j], self.du) for j in range(2)] for i in range(2)]
            H = F(1, 2) * (wj[0][0] * x * x + 2 * wj[0][1] * x * y + wj[1][1] * y * y)
            gradH = {(mu,): H.d(mu) * ETA[mu] for mu in range(D) if H.d(mu)}
            Bv = gtg.wedge(gradH, {(0,): F(1), (3,): F(1)}, S)
            om = [gtg.m_scal(NLOW[c], Bv) if NLOW[c] else {} for c in range(D)]
            self.fld = gtg.Field(TH, om, S)
        else:
            self.fld = gtg.field_from_hbinv(hbinv, x0, S, order=order)
        X = self.X
        t, x, y, z = X
        Y = [x, y]
        du = self.du
        self.Sj = [[series_jet(self.Sc[i][j], du) for j in range(2)] for i in range(2)]
        self.Ej = [[series_jet(self.Ec[i][j], du) for j in range(2)] for i in range(2)]
        phi = F(1, 2) * (t + z)
        for i in range(2):
            for j in range(2):
                phi = phi - F(1, 2) * self.Sj[i][j] * Y[i] * Y[j]
        self.phi = phi
        HJ = self.fld.hb_matrix_jet()
        self.HJ = HJ
        dphi = [phi.d(mu) for mu in range(D)]
        # K . gamma_a = grad phi . hb(gamma_a)
        Klow = [sum((HJ[mu][a] * dphi[mu] for mu in range(D)), ZJ) for a in range(D)]
        self.K = {(a,): Klow[a] * ETA[a] for a in range(D) if Klow[a]}
        self.Kup = [self.K.get((a,), ZJ) for a in range(D)]
        # background generator k = hb(K): k^mu
        self.k = [sum((HJ[mu][a] * self.Kup[a] for a in range(D)), ZJ) for mu in range(D)]
        self.Bj = [self.cov(c, self.K) for c in range(D)]

    def cov(self, c, V):
        """(gamma_c . D) V as jets."""
        out = gtg.comm(self.fld.om[c], V, S)
        for mu in range(D):
            if self.HJ[mu][c]:
                out = gtg.m_add(out, gtg.m_scal(self.HJ[mu][c], gtg.m_d(V, mu)))
        return out

    def along(self, f):
        """k . grad f for a scalar jet f (d/d lambda)."""
        return sum((self.k[mu] * f.d(mu) for mu in range(D)), ZJ)

    def QK(self):
        return ZJ + gtg.vdot(self.K, self.K, S)

    def theta(self):
        return sum((self.Bj[c].get((c,), ZJ) for c in range(D)), ZJ)

    def Bmat(self):
        """M[a][c] = gamma^a . B(gamma_c) (jets)."""
        return [[self.Bj[c].get((a,), ZJ) for c in range(D)] for a in range(D)]

    def trB2(self):
        M = self.Bmat()
        return sum((M[a][c] * M[c][a] for a in range(D) for c in range(D)), ZJ)

    def connecting(self):
        """background connecting vectors x_i^mu (jets) and physical X_i = hb^{-1}(x_i)."""
        t, x, y, z = self.X
        Y = [x, y]
        out = []
        for i in range(2):
            alpha = ZJ
            for j in range(2):
                for m in range(2):
                    alpha = alpha + self.Ej[j][i] * self.Sj[j][m] * Y[m]
            xi = [alpha * NUP[0], self.Ej[0][i], self.Ej[1][i], alpha * NUP[3]]
            out.append(xi)
        return out

    def phys(self, xb):
        return gtg.m_add(*[gtg.m_scal(xb[mu], self.fld.g[mu]) for mu in range(D) if xb[mu]])

    def lie(self, xb):
        """[k, x]^mu as jets."""
        return [sum((self.k[nu] * xb[mu].d(nu) - xb[nu] * self.k[mu].d(nu) for nu in range(D)), ZJ) for mu in range(D)]

    def rho4(self):
        x1, x2 = self.connecting()
        X1, X2 = self.phys(x1), self.phys(x2)
        return ZJ + gtg.vdot(X1, X1, S) * gtg.vdot(X2, X2, S) - gtg.vdot(X1, X2, S) * gtg.vdot(X1, X2, S)

def jet_zero(j, order):
    return all(v == 0 for e, v in j.c.items() if sum(e) <= order)

def maxdeg(j):
    return max([sum(e) for e in j.c] or [0])


# ---- one-variable truncated series (lists of Fractions) ----
def s_add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0)) for i in range(n)]

def s_scal(c, a):
    return [c * x for x in a]

def s_mul(a, b, n):
    return polymul(a, b, n)

def s_inv(a, n):
    out = [F(0)] * (n + 1)
    out[0] = 1 / a[0]
    for k in range(1, n + 1):
        acc = F(0)
        for i in range(1, k + 1):
            if i < len(a):
                acc += a[i] * out[k - i]
        out[k] = -acc / a[0]
    return out

def s_der(a):
    return [a[k] * k for k in range(1, len(a))]

def s_int(a):
    return [F(0)] + [a[k] / (k + 1) for k in range(len(a))]

def s_log(a, n):
    """log of a series with a[0] = 1."""
    assert a[0] == 1
    q = s_mul(s_der(a), s_inv(a, n), n - 1)
    return s_int(q)[:n + 1]

def s_pow(a, r, n):
    """a^r for a[0] = 1, r rational: y' = r a' y / a."""
    assert a[0] == 1
    q = s_scal(F(r), s_mul(s_der(a), s_inv(a, n), n - 1))
    y = [F(1)]
    for k in range(n):
        acc = F(0)
        for i in range(k + 1):
            if i < len(q):
                acc += q[i] * y[k - i]
        y.append(acc / (k + 1))
    return y

def u_series(j, n):
    """coefficients in du of a jet that depends on t, z only through t - z."""
    return [j.coeff((k, 0, 0, 0)) for k in range(n + 1)]
