"""synthesis.massless-composites-de-sitter-conformal-boundary: exact checks.

Gaussian rationals (GA.QI) stand for the chart's I6-complex components; Z = (omega^1, omega^2, pi^1, pi^2).
The squared grip is computed from its definition, <P,U> = M_{U ^ I_Lambda} with the chart matrices
A(U ^ V), the moment M_A = i sum_i bar Z^i . A Z^i and an exact inverse of the ambient Gram matrix
(route A, independent of the join formula). On it:
  (1) lines omega = mu pi: h = pi^dag (mu + mu^dag) pi, B_Lambda = (1 + lambda det mu) <pi pi>,
      [omega omega] = det mu <pi pi>; on mu + mu^dag = 0, m^2 = 2 sigma^2 |<pi pi>|^2 with sigma = 1 + lambda det mu;
  (2a) samples with det mu = -1/lambda are massless, and moving det mu makes them massive;
  (2b) the planes {(omega,0),(0,pi)} with bar omega . pi = 0 are massless; the plane pi = 0 is not;
  (3) the source term (2 Lambda/3) Re(bar b Omega) is -4 |b|^2 on (2a) and 0 on (2b);
  (4) a third constituent in the plane keeps the composite massless.
"""
import GA
from GA import QI
import gtg
from tp_premise import premise
from fractions import Fraction as F


def C(re=0, im=0):
    return QI(re, im)


def cc(x):
    return x if isinstance(x, QI) else QI(x)


def abs2(z):
    return z.re * z.re + z.im * z.im



I = C(0, 1)
EPS = [[0, 1], [-1, 0]]          # eps_12 = 1: eps^T eps = 1, eps^2 = -1, det = 1


# bar Z . W = conj(pi_Z).omega_W + conj(omega_Z).pi_W (Sigma pairs e1<->e3, e2<->e4): gtg.tw_herm;
# the moment M_A = i sum_i bar Z^i . A Z^i and the Gram matrix h_il = bar Z^i . Z^l
moment, gram_h = gtg.tw_moment, gtg.tw_gram_h


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


def trace(M):
    return sum((M[k][k] for k in range(len(M))), C())


def mm(X, Y):
    n = len(X)
    return [[sum((X[r][k] * Y[k][c] for k in range(n)), C()) for c in range(n)] for r in range(n)]


def C_N(h):
    t1 = trace(mm(h, h)); t0 = trace(h)
    return t1 * F(1, 2) - t0 * t0 * F(1, 4)



def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def adj(M):
    return [[M[c][r].conj() for c in range(2)] for r in range(2)]


def line(mu, p):
    """The conformal spinor mu pi + pi of the plane omega = mu pi."""
    return [mu[0][0] * p[0] + mu[0][1] * p[1], mu[1][0] * p[0] + mu[1][1] * p[1], p[0], p[1]]


def mu_of_x(x):
    """mu_x of the exact join (4): (mu_x pi)^a = x^{aa'} eps_{b'a'} pi^{b'}."""
    return [[sum((cc(x[a][ap]) * EPS[bp][ap] for ap in range(2)), C()) for bp in range(2)] for a in range(2)]


def Q_of_x(x):
    G = gram()
    v = [cc(x[a][ap]) for (a, ap) in XS]
    return sum((G[2 + r][2 + s] * v[r] * v[s] for r in range(4) for s in range(4)), C())


def source(b, Om, lam):
    """(2 Lambda / 3) Re(conj(b) Omega) with Lambda = 6 lam."""
    return 4 * lam * (b.conj() * Om).re


def check_massless_composites():
    premise("mass.exact-join")
    premise("mass.de-sitter-scale-frozen-point")
    premise("families.source-term-linear-tilt-mass-functional")
    premise("synthesis.many-twistor-join")
    pis = [([C(1), C(2, 1)], [C(0, 1), C(-1, 3)]), ([C(1, 2), C(0)], [C(2), C(1, -1)])]
    # (1) generic lines omega = mu pi (mu not anti-Hermitian): Gram, brackets, join from the definition
    for lam in (F(1, 6), F(2, 3)):
        for mu in ([[C(1, 1), C(2)], [C(0, -1), C(3, 1)]], [[C(0, 2), C(1, -1)], [C(2, 1), C(-1)]]):
            for (p1, p2) in pis:
                Zs = [line(mu, p1), line(mu, p2)]
                b = br(p1, p2)
                h = gram_h(Zs)
                S = [[mu[r][c] + adj(mu)[r][c] for c in range(2)] for r in range(2)]
                for i, pi in enumerate((p1, p2)):
                    for l, pl in enumerate((p1, p2)):
                        Sp = [S[0][0] * pl[0] + S[0][1] * pl[1], S[1][0] * pl[0] + S[1][1] * pl[1]]
                        assert h[i][l] == pi[0].conj() * Sp[0] + pi[1].conj() * Sp[1]
                assert br(Zs[0][:2], Zs[1][:2]) == det2(mu) * b
                assert B(Zs[0], Zs[1], lam) == (1 + lam * det2(mu)) * b == B_eps(Zs[0], Zs[1], lam)
                assert PP_routeA(Zs, lam) == C(2 * abs2(B(Zs[0], Zs[1], lam)) + 2 * lam * C_N(h).re)
    # mu_x is the chart's line of x and 1 + lam det mu_x = sigma(x) = 1 - lam Q(x) / 2
    for x in ([[1, 2], [3, 5]], [[F(1, 2), 0], [1, -3]]):
        mux = mu_of_x(x)
        assert det2(mux) == Q_of_x(x) * F(-1, 2)
        for (p1, p2) in pis:
            Zs = [line(mux, p1), line(mux, p2)]
            assert B_eps(Zs[0], Zs[1], F(1, 6)) == (1 - F(1, 6) * Q_of_x(x) * F(1, 2)) * br(p1, p2)
    # (1)-(2a) real points: mu = i Y, Y Hermitian; h = 0 and m^2 = 2 sigma^2 |<pi pi>|^2;
    # massless exactly at det Y = 1/lam, i.e. sigma = 0
    for lam, Y in ((F(1, 2), [[C(2), C(1, 1)], [C(1, -1), C(2)]]),
                   (F(1, 6), [[C(3), C(1, 1)], [C(1, -1), C(F(8, 3))]]),
                   (F(3), [[C(1), C(F(1, 3), F(1, 3))], [C(F(1, 3), F(-1, 3)), C(F(5, 9))]])):
        assert det2(Y) == C(1 / lam)
        for shift in (0, 1, -2):
            Ys = [[Y[0][0] + shift, Y[0][1]], [Y[1][0], Y[1][1]]]
            mu = [[I * Ys[r][c] for c in range(2)] for r in range(2)]
            assert all(mu[r][c] + adj(mu)[r][c] == 0 for r in range(2) for c in range(2))
            sig = 1 + lam * det2(mu)
            assert sig.im == 0
            for (p1, p2) in pis:
                Zs = [line(mu, p1), line(mu, p2)]
                b = br(p1, p2)
                Om = br(Zs[0][:2], Zs[1][:2])
                assert all(v == 0 for row in gram_h(Zs) for v in row)
                m2 = PP_routeA(Zs, lam)
                assert m2 == C(2 * sig.re * sig.re * abs2(b))
                if shift == 0:
                    # massless, and (3): Omega = -b / lam, source derivative -4 b, source term -4 |b|^2
                    assert sig == 0 and m2 == 0 and B(Zs[0], Zs[1], lam) == 0
                    assert Om == b * (-1 / lam)
                    assert Om * (4 * lam) == b * (-4)
                    assert source(b, Om, lam) == -4 * abs2(b)
                    # (4) a third constituent in the plane keeps it massless
                    Z3 = [Zs[0][q] * C(2, -1) + Zs[1][q] * C(F(1, 3)) for q in range(4)]
                    assert PP_routeA(Zs + [Z3], lam) == 0
                else:
                    assert m2 != 0
    # (2b) the sphere at infinity: span{(omega, 0), (0, pi)} with conj(omega) . pi = 0
    for lam in (F(1, 6), F(2)):
        for w0 in ([C(1), C(2, -1)], [C(0, 1), C(3)], [C(1), C(0)]):
            p = [w0[1].conj(), -w0[0].conj()]
            Zs = [[w0[0], w0[1], C(), C()], [C(), C(), p[0], p[1]]]
            assert all(v == 0 for row in gram_h(Zs) for v in row)
            b, Om = br(Zs[0][2:], Zs[1][2:]), br(Zs[0][:2], Zs[1][:2])
            assert b == 0 and Om == 0 and source(b, Om, lam) == 0
            # on the boundary at the chart's infinity: <n_inf, X> = <n_0, X> = 0, so <I_Lambda, X> = 0 for every lambda
            assert B_eps(Zs[0], Zs[1], F(0)) == 0 and B_eps(Zs[0], Zs[1], F(1)) == 0
            assert PP_routeA(Zs, lam) == 0
            # tilting pi off the orthogonal line leaves the locus
            Zt = [Zs[0], [C(), C(), p[0] + w0[0], p[1] + w0[1]]]
            assert PP_routeA(Zt, lam) != 0
        # the plane pi = 0 itself is massive: m^2 = 2 lam^2 |[omega omega]|^2
        Zs = [[C(1), C(2), C(), C()], [C(0, 1), C(-1), C(), C()]]
        Om = br(Zs[0][:2], Zs[1][:2])
        assert PP_routeA(Zs, lam) == C(2 * lam * lam * abs2(Om)) and Om != 0
    return True
