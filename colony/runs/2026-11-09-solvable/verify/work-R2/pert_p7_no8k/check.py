"""synthesis.d-term-level-free-at-fixed-n: exact checks.

The stored rung field (synthesis.rung-field-on-the-lift-locus, synthesis.rung-field-d-term-action-and-tree-masses-on-the-
lift-locus): c = sum_a alpha_a v_a + beta_a w_a, alpha, beta in C^2 as Gaussian rationals (GA.QI, the unit standing for
the field theory's unit I_4); Q(c) = alpha^T beta; N(c) = (|alpha|^2 + |beta|^2)/2; G(c, d) = Re(c* . d); moment maps of
the U(2) generators; lift locus Q(c) = -H^2, H^2 = Lambda/3; lift family c_lambda: alpha = (H^2/lambda, 0),
beta = (-lambda, 0). V = (1/2)[g^2 sum_j mu_j^2 + g'^2 (mu_Y - zeta)^2] + kappa N^2, xi = 2 zeta. Masses from the
Hessian of V on L divided by the kinetic coefficient 2 N(d), as in the stored check. Gravity enters only through
G = M_P^-2 and N = M_P/H. Two models share G, Lambda, g, g', kappa and differ in the frame lambda, hence in xi.
Exact throughout.
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

def clam(lam, H2):
    return ([q(H2 / lam), q(0)], [q(-lam), q(0)])


def dclam(lam, H2):
    return ([q(-H2 / (lam * lam)), q(0)], [q(-1), q(0)])


def make_V(zeta, kappa, N0, g, gp):
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


H2 = F(1)                       # H^2 = Lambda/3 in the models' unit
g, gp, KAPPA = F(2, 3), F(1, 2), F(1, 5)
GN = F(1, 100)                  # Newton's constant G = M_P^-2, so N = M_P/H = 10
FRAMES = (F(1, 3), F(1, 5))     # the two models' vacuum frames
NEIGH = (F(9, 10), F(11, 10), F(1, 2), F(2))


def model(lam, H2=H2):
    cs = clam(lam, H2)
    mstar, Nst = m(cs), N(cs)
    xi = mstar * (g * g + gp * gp + 4 * KAPPA) / (gp * gp)
    return cs, mstar, Nst, xi, make_V(xi / 2, KAPPA, F(0), g, gp)


def check_two_frames_are_vacua_with_the_same_dimensionless_spectrum():
    """(i) For both frames, xi = m (g^2 + g'^2 + 8 kappa)/g'^2 puts a critical point of V = V_D + kappa N^2 on L at
    c_lambda (on L, on the boundary N^2 - m^2 = H^4, lower than neighbouring frames), with xi/m > 1; the Hessian on L
    gives m_h^2 = M_Z^2 + 4 kappa N and the charged pair M_W^2 + 4 kappa N, so m_h^2/N = 413/360, m_pm^2/N = 46/45,
    M_W^2/N = 2/9, M_Z^2/N = 25/72 in both models: the dimensionless tree spectrum is the same."""
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("synthesis.rung-field-level-needed-off-balance-and-not-right-invariant")
    spectra = set()
    for lam in FRAMES:
        cs, mstar, Nst, xi, V = model(lam)
        GA.check("c_lambda on L", Q(cs) == q(-H2))
        GA.check("boundary N^2 - m^2 = H^4", Nst ** 2 - mstar ** 2 == H2 ** 2)
        GA.check("level above the moment map, xi/m* > 1", xi / mstar > 1)
        Vs = V(cs)
        GA.check("lower than neighbouring frames", all(V(clam(lam * t, H2)) > Vs for t in NEIGH))
        d0 = dclam(lam, H2)
        first, h0 = hess_on_L(V, cs, d0)
        GA.check("critical along the family", first == 0)
        MW2, MZ2 = g * g * Nst / 2, (g * g + gp * gp) * Nst / 2
        mh2 = h0 / (2 * N(d0))
        GA.check("m_h^2 = M_Z^2 + 4 kappa N", mh2 == MZ2 + 4 * KAPPA * Nst)
        charged = []
        for d in physical_dirs(cs):
            dd = cadd(d, d0, -G(d, d0) / G(d0, d0))
            if N(dd) != 0:
                charged.append(dd)
        GA.check("charged plane two-dimensional", len(charged) == 2)
        mpm = set()
        for d in charged + [cadd(charged[0], charged[1])]:
            first, hh = hess_on_L(V, cs, d)
            GA.check("critical in the charged plane", first == 0)
            mpm.add(hh / (2 * N(d)))
        GA.check("charged pair m_pm^2 = M_W^2 + 4 kappa N", mpm == {MW2 + 4 * KAPPA * Nst})
        spectra.add((mh2 / Nst, mpm.pop() / Nst, MW2 / Nst, MZ2 / Nst))
    GA.check("one dimensionless spectrum in both models", spectra == {(F(413, 360), F(46, 45), F(2, 9), F(25, 72))})
    return True


def check_the_two_models_differ_in_xi_g_at_equal_n():
    """(ii) At equal G and Lambda, so equal N = M_P/H = 10 (N^2 = 1/(G H^2), G Lambda = 3 N^-2), the models have
    N* = 41/9 and 313/25, xi = 3304/81 and 42952/375, xi G = 826/2025 and 10738/9375, (v/M_P)^2 = 2 G N* = 41/450 and
    313/1250; G v^2 N^2 = (v/H)^2 and (m_h/M_P)^2 N^2 = m_h^2/H^2 hold in both; on the boundary V = (1/2)(g^2 m^2/4 +
    g'^2 (m/2 - zeta)^2) + kappa N^2, the D-term part with no H. At N = 10^61 the frames lambda = 10^-44 H and 2 10^-44 H give (v/H)^2 above
    10^87 and values of (v/M_P)^2 in the ratio (H^4/lambda_1^2 + lambda_1^2)/(H^4/lambda_2^2 + lambda_2^2), near 4."""
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion")
    premise("synthesis.smallness-monomials-exact-hierarchy-casimir")
    NN2 = 1 / (GN * H2)
    GA.check("N^2 = 100 and G Lambda = 3 N^-2", NN2 == 100 and GN * 3 * H2 == 3 / NN2)
    out = []
    for lam in FRAMES:
        cs, mstar, Nst, xi, V = model(lam)
        v2 = 2 * Nst
        GA.check("G v^2 N^2 = (v/H)^2", GN * v2 * NN2 == v2 / H2)
        mh2 = (g * g + gp * gp) * Nst / 2 + 4 * KAPPA * Nst
        GA.check("(m_h/M_P)^2 N^2 = m_h^2/H^2", mh2 * GN * NN2 == mh2 / H2)
        VD = make_V(xi / 2, F(0), F(0), g, gp)
        GA.check("boundary D-term potential has no H, W adds kappa N^2",
                 VD(cs) == (g * g * mstar ** 2 / 4 + gp * gp * (mstar / 2 - xi / 2) ** 2) / 2
                 and V(cs) == VD(cs) + KAPPA * Nst ** 2)
        out.append((Nst, xi, xi * GN, v2 * GN))
    GA.check("model values", out == [(F(41, 9), F(3304, 81), F(826, 2025), F(41, 450)),
                                     (F(313, 25), F(42952, 375), F(10738, 9375), F(313, 1250))])
    GA.check("xi G and v/M_P differ at equal N", out[0][2] != out[1][2] and out[0][3] != out[1][3])
    big_G = F(1, 10 ** 122)
    lams = (F(1, 10 ** 44), F(2, 10 ** 44))
    vals = []
    for lam in lams:
        cs, mstar, Nst, xi, V = model(lam)
        GA.check("realistic frame on the boundary", Nst ** 2 - mstar ** 2 == H2 ** 2 and 2 * Nst / H2 > 10 ** 87)
        vals.append(2 * Nst * big_G)
    r = vals[0] / vals[1]
    GA.check("v/M_P differs at N = 10^61, ratio of squares between 3 and 5", 3 < r < 5
             and r == (H2 ** 2 / lams[0] ** 2 + lams[0] ** 2) / (H2 ** 2 / lams[1] ** 2 + lams[1] ** 2))
    return True
