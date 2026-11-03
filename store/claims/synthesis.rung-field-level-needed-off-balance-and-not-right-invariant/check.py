"""Exact checks: the hypercharge level is necessary for an off-balanced vacuum and is not invariant under the
right-handed su(2) of the slot bidoublet.

Coordinates of the stored rung field (synthesis.rung-field-on-the-lift-locus): c = sum_a alpha_a v_a + beta_a w_a,
alpha, beta in C^2 as Gaussian rationals (GA.QI); Q(c) = alpha^T beta; N(c) = (|alpha|^2 + |beta|^2)/2;
G(c, d) = Re(alpha^dag alpha' + beta^dag beta')/2; weak su(2): alpha -> X alpha, beta -> conj(X) beta with
T_j = (i/2) sigma_j; Y = (i/2) 1; m(c) = (|alpha|^2 - |beta|^2)/2. Right generators on C^4:
R1(alpha, beta) = (eps beta, eps alpha)/2, R2(alpha, beta) = (i eps beta, -i eps alpha)/2, R3 = Y, eps = [[0, 1], [-1, 0]].
Lift family c_lambda: alpha = (H^2/lambda, 0), beta = (-lambda, 0). Potential
V = (1/2)[g^2 sum_j mu_j^2 + g'^2 (mu_Y - zeta)^2] + W(N), xi = 2 zeta. Masses from exact Hessians on L divided
by the kinetic coefficient 2 N(d), as in the stored D-term check. Exact throughout.
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

LAMBDA = F(6)
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




EPS = [[q(0), q(1)], [q(-1), q(0)]]
Z2M = [[q(0), q(0)], [q(0), q(0)]]
HALF = q(F(1, 2))


def lin4(A11, A12, A21, A22):
    return lambda c: ([x + y for x, y in zip(mv(A11, c[0]), mv(A12, c[1]))],
                      [x + y for x, y in zip(mv(A21, c[0]), mv(A22, c[1]))])


R1 = lin4(Z2M, msc(HALF, EPS), msc(HALF, EPS), Z2M)
R2 = lin4(Z2M, msc(I * HALF, EPS), msc(-I * HALF, EPS), Z2M)
RR = [R1, R2, Y]
HR = [herm(r) for r in RR]
ZERO4 = ([q(0), q(0)], [q(0), q(0)])


def eqc(c, d):
    return all(a == b for a, b in zip(c[0] + c[1], d[0] + d[1]))


def comm(A, B):
    return lambda c: cadd(A(B(c)), B(A(c)), F(-1))


def opeq(A, B):
    return all(eqc(A(e), B(e)) for e in E8)


def scl(s, A):
    return lambda c: ([s * z for z in A(c)[0]], [s * z for z in A(c)[1]])


def muR(c):
    return [G(c, h(c)) for h in HR]


def cayley_R1(t):
    """((1 - t^2/4) + 2 t R1)/(1 + t^2/4), the Cayley image of t R1 (R1^2 = -1/4)."""
    s = t * t / 4
    a, b = (1 - s) / (1 + s), 2 * t / (1 + s)
    return lambda c: cadd(([a * z for z in c[0]], [a * z for z in c[1]]), R1(c), b)


SWAP = [[q(0), q(1)], [q(1), q(0)]]
T_SAMPLES = (F(1, 3), F(1), F(2), F(7, 2))
DZ = [[q(F(3, 5), F(4, 5)), q(0)], [q(0), q(F(3, 5), F(-4, 5))]]
SU2S = [R35, DZ, mm2(R35, DZ)]
PHY = [[q(F(5, 13), F(12, 13)), q(0)], [q(0), q(F(5, 13), F(12, 13))]]


def basis_mat(k):
    """Real basis of complex 4x4 matrices: k = 2 (4 r + s) + p, p = 0 real unit, p = 1 imaginary unit."""
    p, rs = k % 2, k // 2
    r, s = rs // 4, rs % 4
    M = [[q(0)] * 4 for _ in range(4)]
    M[r][s] = q(1) if p == 0 else q(0, 1)
    return M


def as4(op):
    cols = []
    for k in range(4):
        e = ([q(0), q(0)], [q(0), q(0)])
        (e[0] if k < 2 else e[1])[k % 2] = q(1)
        v = op(e)
        cols.append(v[0] + v[1])
    return [[cols[s][r] for s in range(4)] for r in range(4)]


def m4(A, B):
    return [[sum((A[r][k] * B[k][s] for k in range(4)), q(0)) for s in range(4)] for r in range(4)]


def m4sub(A, B):
    return [[A[r][s] - B[r][s] for s in range(4)] for r in range(4)]


def m4add(A, B):
    return [[A[r][s] + B[r][s] for s in range(4)] for r in range(4)]


def m4T(A):
    return [[A[s][r] for s in range(4)] for r in range(4)]


def m4H(A):
    return [[conj(A[s][r]) for s in range(4)] for r in range(4)]


SQ = [[q(0), q(0), q(1), q(0)], [q(0), q(0), q(0), q(1)], [q(1), q(0), q(0), q(0)], [q(0), q(1), q(0), q(0)]]
TW = [as4(t) for t in T]


def constraints(A):
    """Real coordinates of A^dag + A, A^T SQ + SQ A and [A, T_j]: zero exactly when A is in the isometry
    algebra of (G, Q) and commutes with the weak su(2)."""
    out = []
    mats = [m4add(m4H(A), A), m4add(m4(m4T(A), SQ), m4(SQ, A))] + [m4sub(m4(A, Tj), m4(Tj, A)) for Tj in TW]
    for Mx in mats:
        for r in range(4):
            for s in range(4):
                out += [Mx[r][s].re, Mx[r][s].im]
    return out


def check_commutant_of_weak_su2_is_su2_containing_hypercharge():
    """(ii) first part, complete over the 32 real matrix coordinates: the real-linear maps of the rung summand
    that preserve G and Q and commute with the weak su(2) form a three-dimensional algebra, spanned by R1, R2
    and the hypercharge Y, with su(2) brackets [R1, R2] = Y, [R2, Y] = R1, [Y, R1] = R2."""
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("standard-model.generation-ten-under-pati-salam")
    cols = [constraints(basis_mat(k)) for k in range(32)]
    M = [[cols[k][r] for k in range(32)] for r in range(len(cols[0]))]
    ker = nullspace(M, 32)
    GA.check("commutant has dimension 3", len(ker) == 3)
    for r in RR:
        GA.check("R in the commutant", all(x == 0 for x in constraints(as4(r))))
    GA.check("[R1, R2] = Y", opeq(comm(R1, R2), Y))
    GA.check("[R2, Y] = R1", opeq(comm(R2, Y), R1))
    GA.check("[Y, R1] = R2", opeq(comm(Y, R1), R2))
    GA.check("R1 is not a multiple of Y", not opeq(R1, scl(q(0), R1)) and not opeq(comm(Y, R1), scl(q(0), R1)))
    return True


def check_right_moment_maps_and_the_orbit_of_m():
    """(ii): sum_a mu_Ra^2 = (N^2 - |Q|^2)/4 = sum_j mu_j^2, mu_R3 = m/2; the Cayley elements C_t of R1 commute
    with U(2) samples, keep N and Q, and send m(c_lambda) to ((1 - s)^2 - 4 s)/(1 + s)^2 m(c_lambda), s = t^2/4,
    which is m at t = 0 and -m at t = 2."""
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    for c in SAMPLES + [OFF, clam(F(3)), clam(F(1, 5))]:
        qq = Q(c)
        rhs = (N(c) ** 2 - (qq.re ** 2 + qq.im ** 2)) / 4
        GA.check("sum mu_R^2 = (N^2 - |Q|^2)/4", sum(x * x for x in muR(c)) == rhs)
        GA.check("sum mu_L^2 the same", sum(x * x for x in mu(c)[:3]) == rhs)
        GA.check("mu_R3 = m/2", muR(c)[2] == m(c) / 2)
    for t in T_SAMPLES:
        C = cayley_R1(t)
        for c in SAMPLES:
            GA.check("C_t keeps N and Q", N(C(c)) == N(c) and Q(C(c)) == Q(c))
            for X in SU2S:
                GA.check("C_t commutes with weak SU(2)", eqc(C(u2(X)(c)), u2(X)(C(c))))
            GA.check("C_t does not commute with the hypercharge phase", not eqc(C(u2(PHY)(c)), u2(PHY)(C(c))))
        for lam in (F(1, 2), F(3)):
            s = t * t / 4
            fac = ((1 - s) ** 2 - 4 * s) / (1 + s) ** 2
            GA.check("m along the right orbit", m(C(clam(lam))) == fac * m(clam(lam)))
    GA.check("t = 2 reverses m", m(cayley_R1(F(2))(clam(F(3)))) == -m(clam(F(3))))
    return True




def check_level_not_right_invariant_and_mirror_in_right_group():
    """(ii), (iii): g^2 sum mu_L^2 + g_R^2 sum mu_R^2 is invariant under the C_t while the hypercharge moment map
    is not (mu_Y(C_2 c_lambda) = -mu_Y(c_lambda) != 0 off the balanced frame), so V_0 + k mu_Y with V_0 invariant
    is invariant only for k = 0; the electroweak D-term with level zeta != 0 changes under C_2; and the
    U(2) swap after C_2 = 2 R1 sends c_lambda to c_{H^2/lambda}, the mirror frame."""
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("synthesis.rung-unit-transverse-to-norm")
    gR = F(3, 4)

    def V0(c):
        return (g * g * sum(x * x for x in mu(c)[:3]) + gR * gR * sum(x * x for x in muR(c))) / 2
    for t in T_SAMPLES:
        C = cayley_R1(t)
        for c in SAMPLES + [OFF]:
            qq = Q(c)
            GA.check("left plus right D-term invariant", V0(C(c)) == V0(c))
            GA.check("left plus right D-term = (g^2 + g_R^2)(N^2 - |Q|^2)/8",
                     V0(c) == (g * g + gR * gR) * (N(c) ** 2 - (qq.re ** 2 + qq.im ** 2)) / 8)
    C2 = cayley_R1(F(2))
    GA.check("C_2 = 2 R1", all(eqc(C2(e), scl(q(2), R1)(e)) for e in E8))
    for lam in (F(1, 2), F(3), F(7)):
        c = clam(lam)
        GA.check("mu_Y nonzero off the balanced frame", mu(c)[3] != 0)
        GA.check("mu_Y on the family", mu(c)[3] == (H2 * H2 / (lam * lam) - lam * lam) / 4)
        GA.check("mu_Y reversed by C_2", mu(C2(c))[3] == -mu(c)[3])
        for k in (F(1), F(-2, 3)):
            GA.check("V_0 + k mu_Y changes by -k m", (V0(C2(c)) + k * mu(C2(c))[3]) - (V0(c) + k * mu(c)[3]) == -k * m(c))
        GA.check("V_0 + 0 mu_Y invariant", V0(C2(c)) == V0(c))
        zeta = F(5, 2)
        Vl = make_V(zeta, F(0), F(0))
        GA.check("level D-term changes under C_2 by 2 g'^2 zeta mu_Y", Vl(C2(c)) - Vl(c) == 2 * gp * gp * zeta * mu(c)[3])
        GA.check("swap after C_2 is the mirror frame", eqc(u2(SWAP)(C2(c)), clam(H2 / lam)))
    return True


def hess_on_L_n(V, cs, d, npts):
    s_e = q(-1) * Q(d) / (q(2) * Q(cs))
    e = ([s_e * a for a in cs[0]], [s_e * a for a in cs[1]])

    def c_of(s):
        return ([a + s * b + s * s * ee for a, b, ee in zip(cs[0], d[0], e[0])],
                [a + s * b + s * s * ee for a, b, ee in zip(cs[1], d[1], e[1])])
    h = npts // 2
    pts = [F(k, 3) for k in range(-h, h + 1)]
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


def make_VW(zeta, Wf):
    def V(c):
        mus = mu(c)
        return (g * g * sum(x * x for x in mus[:3]) + gp * gp * (mus[3] - zeta) ** 2) / 2 + Wf(N(c))
    return V


def charged_dirs(cs):
    d0 = dclam_any(cs)
    out = []
    for d in physical_dirs(cs):
        dd = cadd(d, d0, -G(d, d0) / G(d0, d0))
        if N(dd) != 0:
            out.append(dd)
    return out


def dclam_any(cs):
    lam = -cs[1][0].re
    return dclam(lam)


def check_level_necessary_for_an_off_balanced_vacuum():
    """(i): for V = V_D + W(N) with any W, at a critical family point with m* != 0 the charged pair has
    m_pm^2 = (M_Z^2 - M_W^2)(xi/m* - 1), by exact Hessians on L for a quadratic and a cubic W with
    constants, in two frames on either side of the balanced one; with xi = 0 the charged mass squared is
    -(M_Z^2 - M_W^2) < 0."""
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("synthesis.rung-field-on-the-lift-locus")
    Ws = [
        (lambda n: F(3, 2) * (n - F(7)) ** 2, lambda n: 3 * (n - F(7))),
        (lambda n: F(1, 4) * (n - F(2)) ** 3 + F(5) * n, lambda n: F(3, 4) * (n - F(2)) ** 2 + F(5)),
    ]
    seen_zero = False
    for lamstar in (F(1, 2), F(5)):
        cs = clam(lamstar)
        mstar, Nst = m(cs), N(cs)
        GA.check("off the balanced frame", mstar != 0)
        MZ2, MW2 = (g * g + gp * gp) * Nst / 2, g * g * Nst / 2
        tests = list(Ws)
        kz = F(1)
        N0 = Nst + (g * g + gp * gp) * Nst / (8 * kz)
        tests.append((lambda n, N0=N0: kz * (n - N0) ** 2, lambda n, N0=N0: 2 * kz * (n - N0)))
        for Wf, Wp in tests:
            xi = mstar + (4 / (gp * gp)) * (g * g * mstar / 4 + Wp(Nst) * mstar / Nst)
            V = make_VW(xi / 2, Wf)
            first, _ = hess_on_L_n(V, cs, dclam(lamstar), 17)
            GA.check("critical along the family", first == 0)
            pred = (MZ2 - MW2) * (xi / mstar - 1)
            cd = charged_dirs(cs)
            GA.check("charged plane two-dimensional", len(cd) == 2)
            for d in cd + [cadd(cd[0], cd[1])]:
                first, hh = hess_on_L_n(V, cs, d, 17)
                GA.check("critical in the charged plane", first == 0)
                GA.check("m_pm^2 = (M_Z^2 - M_W^2)(xi/m* - 1)", hh / (2 * N(d)) == pred)
            if xi == 0:
                seen_zero = True
                GA.check("xi = 0 gives m_pm^2 = -(M_Z^2 - M_W^2) < 0", pred == -(MZ2 - MW2) and pred < 0)
    GA.check("the xi = 0 case was reached", seen_zero)
    return True
