"""synthesis.many-twistor-join: exact checks.

Gaussian rationals (pairs of Fractions) stand for the chart's I6-complex components. The grip of
N conformal spinors is assembled three ways and compared exactly, for N = 2..5 and several lambda:
  route A: from the definition <P,U> = M_{U ^ I}, with the matrices A(U ^ V) of the chart lemma,
           the moment M_A = i sum_i bar Z^i . A Z^i, and a generic exact inverse of the ambient Gram
           matrix (no use of G^2 = 1);
  route B: 2 sum_{i<l} |B^{il}|^2 + 2 lambda C_N, with B^{il} = eps(I ^ Z^i ^ Z^l) as 4x4 determinants
           and C_N = tr h^2 / 2 - (tr h)^2 / 4 from the Gram matrix;
  route C: the component formulas p.p, k.k, p.k, d in closed form.
Then U(N) invariance (exact Cayley unitaries), the positivity bound, the antilinear map J of the
massless-locus argument, and the de Sitter Casimir corollary.
"""
import GA  # noqa: F401  (house rule; the computation below is in Gaussian rationals)
from tp_premise import premise


class _Rng:
    """Deterministic integer generator (Lehmer, modulus 2^31 - 1) giving a fixed, reproducible list
    of rational test points; no floats and no random module."""

    def __init__(self, seed):
        self.s = seed % 2147483647 or 1

    def _next(self):
        self.s = (self.s * 48271) % 2147483647
        return self.s

    def randint(self, a, b):
        return a + self._next() % (b - a + 1)

    def randrange(self, n):
        return self._next() % n
from fractions import Fraction as F


class C:
    """Gaussian rational a + i b, i the chart's complex unit (I6)."""
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re, self.im = F(re), F(im)

    def __add__(s, o):
        o = cc(o); return C(s.re + o.re, s.im + o.im)
    __radd__ = __add__

    def __sub__(s, o):
        o = cc(o); return C(s.re - o.re, s.im - o.im)

    def __rsub__(s, o):
        return cc(o) - s

    def __neg__(s):
        return C(-s.re, -s.im)

    def __mul__(s, o):
        o = cc(o); return C(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)
    __rmul__ = __mul__

    def __truediv__(s, o):
        o = cc(o); n = o.re * o.re + o.im * o.im
        return s * C(o.re / n, -o.im / n)

    def conj(s):
        return C(s.re, -s.im)

    def abs2(s):
        return s.re * s.re + s.im * s.im

    def __eq__(s, o):
        o = cc(o); return s.re == o.re and s.im == o.im

    def __repr__(s):
        return f"({s.re}+{s.im}i)"


def cc(x):
    return x if isinstance(x, C) else C(x)


I = C(0, 1)
EPS = [[0, 1], [-1, 0]]          # eps_12 = 1: eps^T eps = 1, eps^2 = -1, det = 1


def rnd(rng, k=3):
    return C(F(rng.randint(-k, k), rng.randint(1, 3)), F(rng.randint(-k, k), rng.randint(1, 3)))


def herm(Z, W):
    """bar Z . W = conj(pi_Z).omega_W + conj(omega_Z).pi_W  (Sigma pairs e1<->e3, e2<->e4)."""
    return sum((Z[2 + a].conj() * W[a] + Z[a].conj() * W[2 + a] for a in range(2)), C())


def matvec(A, Z):
    return [sum((cc(A[r][c]) * Z[c] for c in range(4)), C()) for r in range(4)]


def moment(A, Zs):
    """M_A = i sum_i bar Z^i . A Z^i."""
    return I * sum((herm(Z, matvec(A, Z)) for Z in Zs), C())


def A_grading():          # A(n_inf ^ n_0)
    h = F(1, 2)
    return [[-h, 0, 0, 0], [0, -h, 0, 0], [0, 0, h, 0], [0, 0, 0, h]]


def A_trans(x):           # A(x ^ n_inf): omega-block <- b_x pi, (b_x pi)^a = x^{aa'} eps_{a'b'} pi^{b'}
    A = [[0] * 4 for _ in range(4)]
    for a in range(2):
        for bp in range(2):
            A[a][2 + bp] = sum(x[a][ap] * EPS[ap][bp] for ap in range(2))
    return A


def A_spec(x):            # A(x ^ n_0): pi-block <- c_x omega, (c_x w)^{a'} = -x^{ba'} eps_{ba} w^a
    A = [[0] * 4 for _ in range(4)]
    for ap in range(2):
        for a in range(2):
            A[2 + ap][a] = -sum(x[b][ap] * EPS[b][a] for b in range(2))
    return A


def unit_x(a, ap):
    x = [[0, 0], [0, 0]]
    x[a][ap] = 1
    return x


# ambient basis: n_inf, n_0, E_{aa'} (a, a' in 0..1 standing for 1,2 and 3,4)
XS = [(a, ap) for a in range(2) for ap in range(2)]


def gram():
    G = [[F(0)] * 6 for _ in range(6)]
    G[0][1] = G[1][0] = F(1)
    for r, (a, ap) in enumerate(XS):
        for s, (b, bp) in enumerate(XS):
            G[2 + r][2 + s] = F(-EPS[a][b] * EPS[ap][bp])
    return G


def inverse(G):
    n = len(G)
    M = [[cc(G[r][c]) for c in range(n)] + [C(1 if r == c else 0) for c in range(n)] for r in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if not (M[r][col] == 0))
        M[col], M[piv] = M[piv], M[col]
        p = M[col][col]
        M[col] = [v / p for v in M[col]]
        for r in range(n):
            if r != col and not (M[r][col] == 0):
                f = M[r][col]
                M[r] = [M[r][c] - f * M[col][c] for c in range(2 * n)]
    return [row[n:] for row in M]


GI = inverse(gram())


def bil(u, v):
    return sum((GI[r][s] * u[r] * v[s] for r in range(6) for s in range(6)), C())


def grip_values(Zs, lam):
    """<P, U_j> = M_{U_j ^ I}, I = n_inf + lam n_0, by bilinearity of U ^ V -> A(U ^ V)."""
    d = moment(A_grading(), Zs)                     # M_{n_inf ^ n_0}
    v = [lam * d, -d]                               # M_{n_inf ^ I} = lam d ; M_{n_0 ^ I} = -d
    for (a, ap) in XS:
        x = unit_x(a, ap)
        v.append(moment(A_trans(x), Zs) + lam * moment(A_spec(x), Zs))
    return v


def PP_routeA(Zs, lam):
    v = grip_values(Zs, lam)
    return bil(v, v)


def br(u, w):            # eps_{ab} u^a w^b
    return u[0] * w[1] - u[1] * w[0]


def B(Zi, Zl, lam):      # B^{il} = <pi^i pi^l> + lam [omega^i omega^l]
    return br(Zi[2:], Zl[2:]) + lam * br(Zi[:2], Zl[:2])


def det4(M):
    if len(M) == 1:
        return M[0][0]
    return sum(((-1) ** c * M[0][c] * det4([row[:c] + row[c + 1:] for row in M[1:]]) for c in range(len(M))), C())


def B_eps(Zi, Zl, lam):
    """B^{il} = eps(I ^ Z^i ^ Z^l) with eps(e1 e2 e3 e4) = 1, n_inf = e1^e2, n_0 = e3^e4: a 4x4
    determinant route independent of the bracket formula."""
    def e(k):
        return [C(1 if j == k else 0) for j in range(4)]
    t1 = det4([e(0), e(1), Zi, Zl])          # eps(e1 ^ e2 ^ Zi ^ Zl), as columns (det of transpose)
    t2 = det4([e(2), e(3), Zi, Zl])
    return t1 + lam * t2


def gram_h(Zs):
    return [[herm(Zi, Zl) for Zl in Zs] for Zi in Zs]


def trace(M):
    return sum((M[k][k] for k in range(len(M))), C())


def mm(X, Y):
    n = len(X)
    return [[sum((X[r][k] * Y[k][c] for k in range(n)), C()) for c in range(n)] for r in range(n)]


def C_N(h):
    t1 = trace(mm(h, h)); t0 = trace(h)
    return t1 * F(1, 2) - t0 * t0 * F(1, 4)


def PP_routeB(Zs, lam):
    N = len(Zs)
    s = sum((B_eps(Zs[i], Zs[l], lam).abs2() for i in range(N) for l in range(i + 1, N)), F(0))
    return 2 * s + 2 * lam * C_N(gram_h(Zs)).re


def components(Zs):
    N = len(Zs)
    pp = 2 * sum((br(Zs[i][2:], Zs[l][2:]).abs2() for i in range(N) for l in range(i + 1, N)), F(0))
    kk = 2 * sum((br(Zs[i][:2], Zs[l][:2]).abs2() for i in range(N) for l in range(i + 1, N)), F(0))
    t = [[sum((Zs[i][2 + a].conj() * Zs[l][a] for a in range(2)), C()) for l in range(N)] for i in range(N)]
    pk = sum((t[i][l].abs2() for i in range(N) for l in range(N)), F(0))
    d = trace(t).im
    return pp, kk, pk, d, t


def PP_routeC(Zs, lam):
    pp, kk, pk, d, _ = components(Zs)
    return -2 * lam * d * d + pp + 2 * lam * pk + lam * lam * kk


def forms(Zs):
    """p, k as linear forms on the x-slot (components on E_{aa'}), d, all from the A-matrices."""
    p = [moment(A_trans(unit_x(a, ap)), Zs) for (a, ap) in XS]
    k = [moment(A_spec(unit_x(a, ap)), Zs) for (a, ap) in XS]
    d = moment(A_grading(), Zs)
    return p, k, d


def xdot(f, g):
    return sum((GI[2 + r][2 + s] * f[r] * g[s] for r in range(4) for s in range(4)), C())




# ---------------------------------------------------------------- further constructions

def cayley_unitary(rng, N):
    """U = (1 - K)(1 + K)^{-1} for an anti-Hermitian K with Gaussian-rational entries: exactly unitary."""
    K = [[C() for _ in range(N)] for _ in range(N)]
    for r in range(N):
        K[r][r] = C(0, F(rng.randint(-3, 3), 2))
        for c in range(r + 1, N):
            z = rnd(rng, 2)
            K[r][c] = z
            K[c][r] = -z.conj()
    one = [[C(1 if r == c else 0) for c in range(N)] for r in range(N)]
    Am = [[one[r][c] - K[r][c] for c in range(N)] for r in range(N)]
    Bm = [[one[r][c] + K[r][c] for c in range(N)] for r in range(N)]
    Binv = inverse(Bm)
    return mm(Am, Binv)


def apply_U(Zs, U):
    """Z^i -> sum_j Z^j U_{ji}."""
    N = len(Zs)
    return [[sum((Zs[j][a] * U[j][i] for j in range(N)), C()) for a in range(4)] for i in range(N)]


def J(Z, lam):
    """The antilinear map with bar(JZ).W = B_lam(Z, W): JZ = S Omega^T conj(Z), S the block swap."""
    cz = [z.conj() for z in Z]
    OT = [[0] * 4 for _ in range(4)]
    for a in range(2):
        for b in range(2):
            OT[a][b] = lam * EPS[b][a]
            OT[2 + a][2 + b] = EPS[b][a]
    y = matvec(OT, cz)
    return [y[2], y[3], y[0], y[1]]


def check_many_twistor_join():
    premise("mass.exact-join")
    premise("mass.chart-form-spin-isomorphism")
    premise("mass.de-sitter-scale-frozen-point")
    premise("mass.imported-flat-model-twistor-chart-infinity")
    premise("mass.casimir-form-join")
    rng = _Rng(20261022)
    # the ambient Gram matrix: <n_inf, n_0> = 1 (de-sitter-scale-frozen-point (3) uses it),
    # <x, x> = -2 det x on the mixed slot (imported chart fact)
    G = gram()
    for (a, ap), (b, bp) in [((0, 0), (1, 1)), ((0, 1), (1, 0))]:
        x = [[F(0)] * 2 for _ in range(2)]
        x[a][ap] += 1
        x[b][bp] += 1
        r, s = XS.index((a, ap)), XS.index((b, bp))
        quad = G[2 + r][2 + r] + G[2 + s][2 + s] + 2 * G[2 + r][2 + s]
        assert quad == -2 * (x[0][0] * x[1][1] - x[0][1] * x[1][0])
    for lam in (F(1, 6), F(1), F(-2, 3)):
        Iv = [C(1), C(lam), C(), C(), C(), C()]          # coordinates of I = n_inf + lam n_0
        Gc = [[cc(v) for v in row] for row in G]
        II = sum((Gc[r][s] * Iv[r] * Iv[s] for r in range(6) for s in range(6)), C())
        assert II == C(2 * lam)                          # <I,I> = 2 lambda = Lambda/3
    for N in range(2, 6):
        for trial in range(3):
            Zs = [[rnd(rng) for _ in range(4)] for _ in range(N)]
            h = gram_h(Zs)
            # (i) component formulas: forms built from the chart matrices, paired by the inverse Gram
            p, k, d = forms(Zs)
            pp, kk, pk, dd, t = components(Zs)
            assert xdot(p, p) == pp and xdot(k, k) == kk and xdot(p, k) == pk
            assert d == C(dd)
            for i in range(N):
                for l in range(N):
                    assert h[i][l] == t[i][l] + t[l][i].conj()     # h = t + t^dagger
            for lam in (F(0), F(1), F(-2, 3), F(5, 7)):
                # B by the bracket formula equals eps(I ^ Z^i ^ Z^l)
                for i in range(N):
                    for l in range(i + 1, N):
                        assert B(Zs[i], Zs[l], lam) == B_eps(Zs[i], Zs[l], lam)
                # (ii) three routes to <P,P>
                a, b, c = PP_routeA(Zs, lam), PP_routeB(Zs, lam), PP_routeC(Zs, lam)
                assert a.im == 0 and a.re == b == c
            # (ii) at N = 2 the remainder is T11's C = (h11 - h22)^2/4 + |h12|^2
            cN = C_N(h)
            assert cN.im == 0
            if N == 2:
                assert cN.re == (h[0][0].re - h[1][1].re) ** 2 / 4 + h[0][1].abs2()
            # C_N = (1/2) tr h0^2 - (N-2)/(4N) (tr h)^2
            th = trace(h)
            h0 = [[h[r][s] - (th * F(1, N) if r == s else C()) for s in range(N)] for r in range(N)]
            assert cN == trace(mm(h0, h0)) * F(1, 2) - th * th * F(N - 2, 4 * N)
            # (iii) U(N) invariance of <P,P>, of sum |B|^2 and of C_N, with h -> U^dag h U
            U = cayley_unitary(rng, N)
            Zu = apply_U(Zs, U)
            hu = gram_h(Zu)
            Ud = [[U[c][r].conj() for c in range(N)] for r in range(N)]
            assert hu == mm(mm(Ud, h), U)
            assert C_N(hu) == cN
            for lam in (F(1), F(-3, 4)):
                assert PP_routeA(Zu, lam) == PP_routeA(Zs, lam)
                sB = sum((B(Zs[i], Zs[l], lam).abs2() for i in range(N) for l in range(i + 1, N)), F(0))
                sBu = sum((B(Zu[i], Zu[l], lam).abs2() for i in range(N) for l in range(i + 1, N)), F(0))
                assert sB == sBu
            # (iv) C_N >= 0 on realised Gram matrices
            assert cN.re >= 0
            # (vi) de Sitter Casimir: C2(Lambda^2 CS) - <P,P>/<I,I> = (1/2) tr h^2 - sum|B|^2 / lambda
            for lam in (F(1, 6), F(2)):
                sB = sum((B(Zs[i], Zs[l], lam).abs2() for i in range(N) for l in range(i + 1, N)), F(0))
                conf = trace(mm(h, h)).re - th.re * th.re / 4
                assert conf - PP_routeB(Zs, lam) / (2 * lam) == trace(mm(h, h)).re / 2 - sB / lam
    # (iv) the bound uses the signature: an abstract Hermitian h = 1_N has C_N = N(2 - N)/4 < 0 for N >= 3,
    # so 1_N is not the Gram matrix of N >= 3 conformal spinors; and 4 C_N = (a1-a2)^2 + (b1-b2)^2 + 2AB
    for N in range(3, 7):
        one = [[C(1 if r == c else 0) for c in range(N)] for r in range(N)]
        assert C_N(one) == C(F(N * (2 - N), 4)) and F(N * (2 - N), 4) < 0
    for (a1, a2, b1, b2) in [(F(3), F(1), F(2), F(0)), (F(1, 2), F(1, 2), F(0), F(0)), (F(5), F(0), F(1), F(1))]:
        mus = [a1, a2, -b1, -b2, F(0)]
        h = [[C(mus[r] if r == c else 0) for c in range(5)] for r in range(5)]
        assert 4 * C_N(h).re == (a1 - a2) ** 2 + (b1 - b2) ** 2 + 2 * (a1 + a2) * (b1 + b2)
    # (v) the antilinear map J: bar(JZ).W = B_lam(Z,W), J^2 = -lam, bar(JZ).(JW) = lam conj(bar Z.W)
    for lam in (F(1, 6), F(1), F(-3, 5)):
        for _ in range(4):
            Z = [rnd(rng) for _ in range(4)]
            W = [rnd(rng) for _ in range(4)]
            assert herm(J(Z, lam), W) == B(Z, W, lam)
            JJ = J(J(Z, lam), lam)
            assert all(JJ[q] == -lam * Z[q] for q in range(4))
            assert herm(J(Z, lam), J(W, lam)) == lam * herm(Z, W).conj()
    # (v) massless examples: B = 0 and h = 0, for N = 2 (T11's) and N = 3, at Lambda > 0
    for lam in (F(1, 6), F(3)):
        for coeffs in ([(C(1), C(1)), (C(2), C(0, 1))], [(C(1), C(1)), (C(-1), C(2)), (C(0, 1), C(1, -1))]):
            Zs = [[a, C(), C(), b] for (a, b) in coeffs]      # Z = a e1 + b e4
            assert all(B(Zs[i], Zs[l], lam) == 0 for i in range(len(Zs)) for l in range(len(Zs)))
            assert all(v == 0 for row in gram_h(Zs) for v in row)
            assert PP_routeA(Zs, lam) == 0
    return True
