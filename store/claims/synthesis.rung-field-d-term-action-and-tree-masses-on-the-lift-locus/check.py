"""synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus: exact checks.

Coordinates of the stored rung field (synthesis.rung-field-on-the-lift-locus): c = sum_a alpha_a v_a + beta_a w_a,
alpha, beta in C^2 as Gaussian rationals (GA.QI); Q(c) = alpha^T beta; N(c) = (|alpha|^2 + |beta|^2)/2;
G(c, d) = Re(c* . d) = Re(alpha^dag alpha' + beta^dag beta')/2; U(2): alpha -> X alpha, beta -> conj(X) beta,
generators T_j = (i/2) sigma_j, Y = (i/2) 1; the hypercharge moment map m(c) = (|alpha|^2 - |beta|^2)/2.
Moment maps mu_a(c) = G(c, (-i T_a) c), a = 1, 2, 3, Y. Lift locus L: Q(c) = -Lambda/3 = -H^2; lift family
c_lambda: alpha = (H^2/lambda, 0), beta = (-lambda, 0).
Potential V = (1/2)[g^2 sum_j mu_j^2 + g'^2 (mu_Y - zeta)^2] + kappa (N - N_0)^2, xi := 2 zeta.
Masses from the Hessian of V restricted to L (curves c + eps d + eps^2 e on L) divided by the kinetic
coefficient 2 N(d) of the stored Hermitian kinetic term, against M_W^2 = g^2 N/2, M_Z^2 = (g^2 + g'^2) N/2.
Exact throughout (Fractions, Gaussian rationals).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI
I = GA.QI_I


def q(re, im=0):
    return QI(F(re), F(im))


def conj(z):
    return z.conj()


def absq(v):
    return sum((z.re * z.re + z.im * z.im for z in v), F(0))


def hdot(u, v):
    return sum((conj(a) * b for a, b in zip(u, v)), QI(0))


def N(c):
    return (absq(c[0]) + absq(c[1])) / 2


def G(c, d):
    return (hdot(c[0], d[0]) + hdot(c[1], d[1])).re / 2


def Q(c):
    return sum((a * b for a, b in zip(c[0], c[1])), QI(0))


def Qb(c, d):
    return (sum((a * b for a, b in zip(c[0], d[1])), QI(0))
            + sum((a * b for a, b in zip(d[0], c[1])), QI(0)))


def m(c):
    return (absq(c[0]) - absq(c[1])) / 2


S1 = [[q(0), q(1)], [q(1), q(0)]]
S2 = [[q(0), q(0, -1)], [q(0, 1), q(0)]]
S3 = [[q(1), q(0)], [q(0), q(-1)]]
ONE2 = [[q(1), q(0)], [q(0), q(1)]]


def mv(M, v):
    return [M[i][0] * v[0] + M[i][1] * v[1] for i in range(2)]


def mconj(M):
    return [[conj(M[i][j]) for j in range(2)] for i in range(2)]


def msc(s, M):
    return [[s * M[i][j] for j in range(2)] for i in range(2)]


def mm2(A, B):
    return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)] for i in range(2)]


def gen(sig):
    A = msc(I * F(1, 2), sig)
    return lambda c: (mv(A, c[0]), mv(mconj(A), c[1]))


T = [gen(S1), gen(S2), gen(S3)]
Y = gen(ONE2)


def herm(g):
    return lambda c: ([z * (-I) for z in g(c)[0]], [z * (-I) for z in g(c)[1]])


HT = [herm(t) for t in T]
HY = herm(Y)


def mu(c):
    return [G(c, h(c)) for h in HT] + [G(c, HY(c))]


def cadd(c, d, s=F(1)):
    return ([a + s * b for a, b in zip(c[0], d[0])], [a + s * b for a, b in zip(c[1], d[1])])


def u2(X):
    return lambda c: (mv(X, c[0]), mv(mconj(X), c[1]))


R35 = [[q(F(3, 5)), q(F(4, 5))], [q(F(-4, 5)), q(F(3, 5))]]
PH = [[q(F(3, 5), F(4, 5)), q(0)], [q(0), q(F(5, 13), F(12, 13))]]
PH2 = [[q(F(5, 13), F(-12, 13)), q(0)], [q(0), q(F(5, 13), F(-12, 13))]]
US = [R35, PH, PH2, mm2(R35, PH), mm2(PH2, mm2(R35, PH))]

LAMBDA = F(3)
H2 = LAMBDA / 3
g, gp = F(2, 3), F(1, 2)

FRAMES = (F(1, 2), F(3), F(10))
NEIGHBOURS = (F(9, 10), F(11, 10), F(2), F(1, 3))
W_SAMPLES = ((F(1, 5), F(7)), (F(2), F(1, 3)))
W_FRAMES = (F(1, 2), F(3))

SAMPLES = [
    ([q(1, 2), q(-3, 1)], [q(2, -1), q(F(1, 2), 3)]),
    ([q(F(1, 3)), q(2, 2)], [q(0, 1), q(-1)]),
    ([q(5, -2), q(0)], [q(1, 1), q(4, -3)]),
]
OFF = ([q(1), q(2)], [q(-H2) - q(2) * q(0, 1), q(0, 1)])     # on L, off the family


def clam(lam):
    return ([q(H2 / lam), q(0)], [q(-lam), q(0)])


def dclam(lam):
    return ([q(-H2 / (lam * lam)), q(0)], [q(-1), q(0)])


def make_V(zeta, kappa, N0):
    def V(c):
        mus = mu(c)
        return ((g * g * sum(x * x for x in mus[:3]) + gp * gp * (mus[3] - zeta) ** 2) / 2
                + kappa * (N(c) - N0) ** 2)
    return V


def basis_vec(k):
    al = [q(0), q(0)]
    be = [q(0), q(0)]
    comp = k // 2
    val = q(1) if k % 2 == 0 else q(0, 1)
    if comp < 2:
        al[comp] = val
    else:
        be[comp - 2] = val
    return (al, be)


E8 = [basis_vec(k) for k in range(8)]


def nullspace(M, n):
    M = [row[:] for row in M]
    piv_cols = []
    r = 0
    for ccol in range(n):
        p = next((rr for rr in range(r, len(M)) if M[rr][ccol] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][ccol]
        M[r] = [v / pv for v in M[r]]
        for rr in range(len(M)):
            if rr != r and M[rr][ccol] != 0:
                f = M[rr][ccol]
                M[rr] = [a - f * b for a, b in zip(M[rr], M[r])]
        piv_cols.append(ccol)
        r += 1
    free = [cc for cc in range(n) if cc not in piv_cols]
    vecs = []
    for fcol in free:
        v = [F(0)] * n
        v[fcol] = F(1)
        for i, pc in enumerate(piv_cols):
            v[pc] = -M[i][fcol]
        vecs.append(v)
    return vecs


def physical_dirs(cs):
    """G-orthogonal complement of the gauge orbit inside the tangent space of L at cs."""
    gauge = [t(cs) for t in T] + [Y(cs)]
    rows = []
    for k in range(8):
        qb = Qb(cs, E8[k])
        rows.append([qb.re, qb.im] + [G(gv, E8[k]) for gv in gauge])
    M = [[rows[k][r] for k in range(8)] for r in range(6)]
    phys = []
    for v in nullspace(M, 8):
        d = ([q(0), q(0)], [q(0), q(0)])
        for k in range(8):
            d = cadd(d, E8[k], v[k])
        phys.append(d)
    return phys


def hess_on_L(V, cs, d):
    """(first derivative, second derivative) at eps = 0 of V along c(eps) = cs + eps d + eps^2 e on L,
    e = -(Q(d)/(2 Q(cs))) cs, by exact interpolation of the degree-8 polynomial V(c(eps))."""
    s_e = q(-1) * Q(d) / (q(2) * Q(cs))
    e = ([s_e * a for a in cs[0]], [s_e * a for a in cs[1]])

    def c_of(s):
        return ([a + s * b + s * s * ee for a, b, ee in zip(cs[0], d[0], e[0])],
                [a + s * b + s * s * ee for a, b, ee in zip(cs[1], d[1], e[1])])
    pts = [F(k, 3) for k in range(-4, 5)]
    vals = [V(c_of(p)) for p in pts]
    n = len(pts)
    A = [[p ** j for j in range(n)] + [vals[i]] for i, p in enumerate(pts)]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]
        A[col] = [v / pv for v in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [a - f * b for a, b in zip(A[r], A[col])]
    return A[1][n], 2 * A[2][n]


def check_invariants_moment_maps_and_orbit_space():
    """(1): |alpha|^2, |beta|^2 and Q are U(2)-invariant; mu_Y = m/2 and sum_j mu_j^2 = (N^2 - |Q|^2)/4;
    on the lift family N^2 - m^2 = H^4 with mu_1 = mu_2 = 0, mu_3 = m/2; an off-family point of L has
    N^2 - m^2 > H^4 and all four moment maps nonzero; c -> c* keeps N and conjugates Q but reverses m."""
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("synthesis.rung-unit-is-frame-boost")
    for c in SAMPLES:
        for X in US:
            d = u2(X)(c)
            GA.check("|alpha|^2, |beta|^2 invariant", absq(d[0]) == absq(c[0]) and absq(d[1]) == absq(c[1]))
            GA.check("Q invariant under U(2)", Q(d) == Q(c))
        mus = mu(c)
        qq = Q(c)
        GA.check("mu_Y = m/2", mus[3] == m(c) / 2)
        GA.check("sum mu_j^2 = (N^2 - |Q|^2)/4",
                 sum(x * x for x in mus[:3]) == (N(c) ** 2 - (qq.re ** 2 + qq.im ** 2)) / 4)
        cstar = ([conj(z) for z in c[1]], [conj(z) for z in c[0]])
        GA.check("c -> c*: N kept, m reversed, Q conjugated",
                 N(cstar) == N(c) and m(cstar) == -m(c) and Q(cstar) == conj(Q(c)))
    for lam in (F(1, 3), F(1), F(2), F(7, 2)):
        c = clam(lam)
        GA.check("c_lambda on L", Q(c) == q(-H2))
        GA.check("family saturates N^2 - m^2 = H^4", N(c) ** 2 - m(c) ** 2 == H2 ** 2)
        mus = mu(c)
        GA.check("mu_1 = mu_2 = 0, mu_3 = m/2 on the family", mus[0] == 0 and mus[1] == 0 and mus[2] == m(c) / 2)
    GA.check("OFF on L", Q(OFF) == q(-H2))
    GA.check("off the family N^2 - m^2 > H^4", N(OFF) ** 2 - m(OFF) ** 2 > H2 ** 2)
    GA.check("off the family all four moment maps nonzero", all(x != 0 for x in mu(OFF)))
    return True


def check_d_term_vacuum_and_tree_masses():
    """(2), (3): with kappa = 0 the vacuum is on the family at m* = g'^2 xi/(g^2 + g'^2) (neighbours along the
    family and the off-family formula V = (1/2)[g^2 (N^2 - H^4)/4 + g'^2 (m/2 - zeta)^2] checked), and the
    Hessian of V on L gives m_h^2 = M_Z^2 on the neutral mode and M_W^2 on the charged pair, in three frames."""
    premise("synthesis.rung-field-on-the-lift-locus")
    for lamstar in FRAMES:
        cs = clam(lamstar)
        mstar, Nst = m(cs), N(cs)
        xi = mstar * (g * g + gp * gp) / (gp * gp)
        V = make_V(xi / 2, F(0), F(0))
        Vs = V(cs)
        for fac in NEIGHBOURS:
            GA.check("V larger at neighbouring frames", V(clam(lamstar * fac)) > Vs)
        Noff = N(OFF)
        GA.check("V(N, m) formula on L",
                 V(OFF) == (g * g * (Noff ** 2 - H2 ** 2) / 4 + gp * gp * (m(OFF) / 2 - xi / 2) ** 2) / 2)
        MZ2 = (g * g + gp * gp) * Nst / 2
        MW2 = g * g * Nst / 2
        d0 = dclam(lamstar)
        Kd0 = (d0[0], [-z for z in d0[1]])
        GA.check("dm/dlambda = 2 G(c, K dc)", 2 * G(cs, Kd0) == -H2 ** 2 / lamstar ** 3 - lamstar)
        GA.check("kinetic coefficient N(dc/dlambda) = N/lambda^2", N(d0) == Nst / lamstar ** 2)
        GA.check("neutral direction tangent to L", Qb(cs, d0) == q(0))
        first, h0 = hess_on_L(V, cs, d0)
        GA.check("critical along the family", first == 0)
        GA.check("m_h^2 = M_Z^2", h0 / (2 * N(d0)) == MZ2)
        phys = physical_dirs(cs)
        GA.check("three physical directions", len(phys) == 3)
        charged = []
        for d in phys:
            dd = cadd(d, d0, -G(d, d0) / G(d0, d0))
            if N(dd) != 0:
                charged.append(dd)
        GA.check("charged plane two-dimensional", len(charged) == 2)
        for d in charged + [cadd(charged[0], charged[1])]:
            first, hh = hess_on_L(V, cs, d)
            GA.check("critical in the charged plane", first == 0)
            GA.check("charged mass^2 = M_W^2", hh / (2 * N(d)) == MW2)
        GA.check("sinh 2 eta* = -m*/H^2 and N* = sqrt(m*^2 + H^4)", Nst ** 2 == mstar ** 2 + H2 ** 2)
    return True


def check_added_invariant_shifts_masses():
    """(4): with W(N) = kappa (N - N_0)^2 added, on the family m_h^2 = M_Z^2 + 2 W'' m*^2/N* + 2 W' H^4/N*^2,
    the charged pair has M_W^2 + 2 W'(N*), which is twice the outward N-derivative g^2 N*/4 + W'(N*) of V
    at the boundary (negative for one sample: a charge-breaking instability)."""
    premise("synthesis.rung-field-on-the-lift-locus")
    signs = set()
    for lamstar in W_FRAMES:
        for kappa, N0 in W_SAMPLES:
            cs = clam(lamstar)
            mstar, Nst = m(cs), N(cs)
            Wp = 2 * kappa * (Nst - N0)
            Wpp = 2 * kappa
            xi = mstar + (4 / (gp * gp)) * (g * g * mstar / 4 + Wp * mstar / Nst)
            V = make_V(xi / 2, kappa, N0)
            MZ2 = (g * g + gp * gp) * Nst / 2
            MW2 = g * g * Nst / 2
            d0 = dclam(lamstar)
            first, h0 = hess_on_L(V, cs, d0)
            GA.check("critical with W", first == 0)
            GA.check("m_h^2 with W", h0 / (2 * N(d0)) == MZ2 + 2 * Wpp * mstar ** 2 / Nst + 2 * Wp * H2 ** 2 / Nst ** 2)
            phys = physical_dirs(cs)
            charged = []
            for d in phys:
                dd = cadd(d, d0, -G(d, d0) / G(d0, d0))
                if N(dd) != 0:
                    charged.append(dd)
            for d in charged + [cadd(charged[0], charged[1])]:
                first, hh = hess_on_L(V, cs, d)
                GA.check("critical in the charged plane with W", first == 0)
                GA.check("charged mass^2 = M_W^2 + 2 W'", hh / (2 * N(d)) == MW2 + 2 * Wp)
                GA.check("charged mass^2 = twice the outward derivative", hh / (2 * N(d)) == 2 * (g * g * Nst / 4 + Wp))
            signs.add((MW2 + 2 * Wp) > 0)
    GA.check("both a stable and a charge-breaking sample occur", signs == {True, False})
    return True
