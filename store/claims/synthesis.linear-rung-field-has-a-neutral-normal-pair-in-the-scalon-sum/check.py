"""synthesis.rung-field-as-a-linear-quantum-field-and-its-normal-pair: exact checks.

The rung field c = sum_a (alpha_a v_a + beta_a w_a) of synthesis.rung-field-on-the-lift-locus, alpha, beta in C^2 as
Gaussian rationals (GA.QI); Q(c) = alpha^T beta, N = (|alpha|^2 + |beta|^2)/2, m = (|alpha|^2 - |beta|^2)/2; U(2):
alpha -> X alpha, beta -> conj(X) beta. The LINEAR field: all eight real components of the complexified rung summand,
with a polynomial potential; masses are eigenvalues of the real Hessian in the basis E8 (each basis vector has
kinetic coefficient 2 N(e) = 1 for the stored Hermitian kinetic term). Vacuum on the cone Q = 0 (the H -> 0 limit):
alpha = 0, beta = (-lam, 0). Clause (1) uses the GA engine on Cl(3,5) (spacetime and the two rung planes).
Exact arithmetic throughout (Fractions, Gaussian rationals, rational interval bounds for pi and arcsin^2).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise, quantity

QI = GA.QI
I = GA.QI_I


def q(re, im=0):
    return QI(F(re), F(im))


def absq(v):
    return sum((z.re * z.re + z.im * z.im for z in v), F(0))


def N(c):
    return (absq(c[0]) + absq(c[1])) / 2


def m(c):
    return (absq(c[0]) - absq(c[1])) / 2


def Q(c):
    return c[0][0] * c[1][0] + c[0][1] * c[1][1]


def G(c, d):
    return sum((x.conj() * y for x, y in zip(c[0] + c[1], d[0] + d[1])), QI(0)).re / 2


def cadd(c, d, s=F(1)):
    return ([a + b * QI(s) for a, b in zip(c[0], d[0])], [a + b * QI(s) for a, b in zip(c[1], d[1])])


def mv(M, v):
    return [M[i][0] * v[0] + M[i][1] * v[1] for i in range(2)]


def mconj(M):
    return [[M[i][j].conj() for j in range(2)] for i in range(2)]


S1 = [[q(0), q(1)], [q(1), q(0)]]
S2 = [[q(0), q(0, -1)], [q(0, 1), q(0)]]
S3 = [[q(1), q(0)], [q(0), q(-1)]]
ONE2 = [[q(1), q(0)], [q(0), q(1)]]


def gen(sig):
    A = [[I * F(1, 2) * sig[i][j] for j in range(2)] for i in range(2)]
    return lambda c: (mv(A, c[0]), mv(mconj(A), c[1]))


T = [gen(S1), gen(S2), gen(S3)]
Y = gen(ONE2)


def moment(c, g):
    h = g(c)
    return G(c, ([z * (-I) for z in h[0]], [z * (-I) for z in h[1]]))


def V_D(gg, gp, zeta):
    def V(c):
        mus = [moment(c, t) for t in T]
        my = moment(c, Y)
        return (gg * gg * sum(x * x for x in mus) + gp * gp * (my - zeta) ** 2) / 2
    return V


def V_Qterms(k8, k9, k10, H2=F(0)):
    def V(c):
        z = Q(c) + q(H2)
        z2 = Q(c) * Q(c)
        return k8 * z2.re + k9 * z2.im + k10 * (z.re * z.re + z.im * z.im)
    return V


def V_sum(*vs):
    return lambda c: sum((v(c) for v in vs), F(0))


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


E8 = [basis_vec(k) for k in range(8)]   # a1r a1i a2r a2i b1r b1i b2r b2i


def line_coeffs(V, c, d):
    """Exact coefficients of the polynomial s -> V(c + s d) (degree <= 4) by interpolation at s = -2..2."""
    pts = [F(k) for k in range(-2, 3)]
    vals = [V(cadd(c, d, p)) for p in pts]
    n = 5
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
    return [A[j][n] for j in range(n)]


def grad(V, c):
    return [line_coeffs(V, c, e)[1] for e in E8]


def hessian(V, c):
    d2 = [2 * line_coeffs(V, c, e)[2] for e in E8]
    M = [[F(0)] * 8 for _ in range(8)]
    for i in range(8):
        M[i][i] = d2[i]
        for j in range(i + 1, 8):
            s = 2 * line_coeffs(V, c, cadd(E8[i], E8[j]))[2]
            M[i][j] = M[j][i] = (s - d2[i] - d2[j]) / 2
    return M


def mult(M, r):
    n = len(M)
    return n - GA.mat_rank([[M[i][j] - (r if i == j else 0) for j in range(n)] for i in range(n)])


def vec_of(c):
    return [x for z in c[0] + c[1] for x in (z.re, z.im)]


# samples: (g, g', lam, w1, w2, k8, k9, k10) with r = sqrt(k8^2 + k9^2) rational
SAMPLES = [
    (F(2, 3), F(1, 2), F(2), F(1, 5), F(1, 3), F(3, 25), F(4, 25), F(1, 2)),
    (F(13, 20), F(7, 20), F(3), F(-1, 10), F(1, 7), F(0), F(5, 13), F(1)),
    (F(1, 2), F(1, 3), F(1), F(2), F(-1, 4), F(-6, 5), F(8, 5), F(5, 2)),
]


def vacuum_zeta(g, gp, lam, w1, w2):
    """Level fixing the cone family point alpha = 0, beta = (-lam, 0) as a critical point:
    (g^2 + g'^2) lam^2 + 4 g'^2 zeta + 8 W'(N) = 0, W' = w1 + w2 N, N = lam^2/2 (stored clause (4), H -> 0)."""
    Wp = w1 + w2 * lam * lam / 2
    return -((g * g + gp * gp) * lam * lam + 8 * Wp) / (4 * gp * gp)


def check_i4_is_the_rung_fields_imaginary_unit_and_hypercharge_is_the_imaginary_rapidity_boost():
    """(1): in Cl(3,5) (gamma_0 .. gamma_3, then e_a, f_a for the rung planes a = 4, 5), v_a = (e_a + f_a)/2,
    w_a = (e_a - f_a)/2: I4 = gamma_0123 squares to -1 and commutes with every rung vector; for c with coefficients
    in span{1, I4}, c^2 = Q(c) = alpha^T beta in span{1, I4}; with b = sum_a (v_a w_a - 1/2) (= v_a ^ w_a),
    [b, v_a] = v_a, [b, w_a] = -w_a; Ad(exp(t b)) is the stored rung boost e^{tK} (v -> e^t v, w -> e^{-t} w, at
    e^t = 4), and Ad(exp(phi I4 b)) multiplies v_a by e^{phi I4} and w_a by e^{-phi I4} (the hypercharge rotation,
    at cos phi = -7/25, sin phi = 24/25): on the rung summand the hypercharge is the rung boost at I4-imaginary
    rapidity; I4 b anticommutes with every gamma_mu, so the same automorphism moves each gamma_mu (to
    exp(2 phi I4 b) gamma_mu): the identification holds on rung values, not on spacetime points."""
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("field-theory.boost-modes")
    sq = GA.sig(1, 3) + (F(1), F(-1), F(1), F(-1))
    sq = tuple(F(x) for x in sq)
    mul = lambda x, y: GA.mul(x, y, sq)
    I4 = mul(mul(GA.gen(0), GA.gen(1)), mul(GA.gen(2), GA.gen(3)))
    GA.check("I4^2 = -1", GA.eq(mul(I4, I4), GA.sc(-1)))
    v = {a: GA.scal(F(1, 2), GA.add(GA.gen(e), GA.gen(e + 1))) for a, e in ((4, 4), (5, 6))}
    w = {a: GA.scal(F(1, 2), GA.sub(GA.gen(e), GA.gen(e + 1))) for a, e in ((4, 4), (5, 6))}
    for a in (4, 5):
        GA.check("I4 commutes with v_a and w_a", GA.commutes(I4, v[a], sq) and GA.commutes(I4, w[a], sq))
        GA.check("v_a, w_a null", GA.is_zero(mul(v[a], v[a])) and GA.is_zero(mul(w[a], w[a])))
        for bb in (4, 5):
            GA.check("{v_a, w_b} = delta_ab",
                     GA.eq(GA.add(mul(v[a], w[bb]), mul(w[bb], v[a])), GA.sc(1 if a == bb else 0)))
        GA.check("gamma_0 anticommutes with v_a: I4 is not central in the whole algebra",
                 GA.anticommutes(GA.gen(0), v[a], sq))

    def cnum(x, y):
        return GA.add(GA.sc(x), GA.scal(y, I4))
    coeffs = [(F(1, 2), F(-3)), (F(2), F(1, 3)), (F(-1), F(5, 4)), (F(3, 7), F(2))]   # alpha_4, alpha_5, beta_4, beta_5
    al = [cnum(*coeffs[0]), cnum(*coeffs[1])]
    be = [cnum(*coeffs[2]), cnum(*coeffs[3])]
    c = GA.add(mul(al[0], v[4]), mul(al[1], v[5]), mul(be[0], w[4]), mul(be[1], w[5]))
    Qc = GA.add(mul(al[0], be[0]), mul(al[1], be[1]))
    GA.check("c^2 = alpha^T beta, complex-bilinear over span{1, I4}", GA.eq(mul(c, c), Qc))
    zq = QI(coeffs[0][0], coeffs[0][1]) * QI(coeffs[2][0], coeffs[2][1]) + QI(coeffs[1][0], coeffs[1][1]) * QI(coeffs[3][0], coeffs[3][1])
    GA.check("the span{1, I4} value is the Gaussian value of Q", GA.eq(Qc, cnum(zq.re, zq.im)))
    b = GA.add(*[GA.sub(mul(v[a], w[a]), GA.sc(F(1, 2))) for a in (4, 5)])
    for a in (4, 5):
        GA.check("[b, v_a] = v_a", GA.eq(GA.sub(mul(b, v[a]), mul(v[a], b)), v[a]))
        GA.check("[b, w_a] = -w_a", GA.eq(GA.sub(mul(b, w[a]), mul(w[a], b)), GA.neg(w[a])))
        ba = GA.sub(mul(v[a], w[a]), GA.sc(F(1, 2)))
        GA.check("b_a^2 = 1/4, (I4 b_a)^2 = -1/4", GA.eq(mul(ba, ba), GA.sc(F(1, 4)))
                 and GA.eq(mul(mul(I4, ba), mul(I4, ba)), GA.sc(F(-1, 4))))
    # real rapidity: exp(t b_a) = cosh(t/2) + 2 b_a sinh(t/2), cosh = 5/4, sinh = 3/4 (e^t = 4)
    # imaginary rapidity: exp(phi I4 b_a) = cos(phi/2) + 2 I4 b_a sin(phi/2), cos = 3/5, sin = 4/5
    R = GA.sc(1)
    Ri = GA.sc(1)
    Rb = GA.sc(1)
    Rbi = GA.sc(1)
    for a in (4, 5):
        ba = GA.sub(mul(v[a], w[a]), GA.sc(F(1, 2)))
        R = mul(R, GA.add(GA.sc(F(3, 5)), GA.scal(F(8, 5), mul(I4, ba))))
        Ri = mul(Ri, GA.sub(GA.sc(F(3, 5)), GA.scal(F(8, 5), mul(I4, ba))))
        Rb = mul(Rb, GA.add(GA.sc(F(5, 4)), GA.scal(F(3, 2), ba)))
        Rbi = mul(Rbi, GA.sub(GA.sc(F(5, 4)), GA.scal(F(3, 2), ba)))
    GA.check("rotor inverses", GA.eq(mul(R, Ri), GA.sc(1)) and GA.eq(mul(Rb, Rbi), GA.sc(1)))
    ph = cnum(F(-7, 25), F(24, 25))
    phb = cnum(F(-7, 25), F(-24, 25))
    for a in (4, 5):
        GA.check("Ad(exp(t b)) is the rung boost: v -> 4 v, w -> w/4",
                 GA.eq(mul(mul(Rb, v[a]), Rbi), GA.scal(4, v[a])) and GA.eq(mul(mul(Rb, w[a]), Rbi), GA.scal(F(1, 4), w[a])))
        GA.check("Ad(exp(phi I4 b)): v -> e^{phi I4} v, w -> e^{-phi I4} w",
                 GA.eq(mul(mul(R, v[a]), Ri), mul(ph, v[a])) and GA.eq(mul(mul(R, w[a]), Ri), mul(phb, w[a])))
    # values, not points: I4 b anticommutes with every spacetime vector, so the rotor moves them
    I4b = mul(I4, b)
    GA.check("I4 b anticommutes with gamma_0 .. gamma_3", all(GA.anticommutes(I4b, GA.gen(mu), sq) for mu in range(4)))
    for mu in range(4):
        img = mul(mul(R, GA.gen(mu)), Ri)
        GA.check("Ad(exp(phi I4 b)) gamma_mu = exp(2 phi I4 b) gamma_mu, not gamma_mu",
                 GA.eq(img, mul(mul(R, R), GA.gen(mu))) and not GA.eq(img, GA.gen(mu)))
    # on coefficients this is alpha -> e^{phi I4} alpha, beta -> e^{-phi I4} beta: exp(2 phi Y) with Y = (i/2) 1, i = I4
    cy = Y(([q(1), q(0)], [q(1), q(0)]))
    GA.check("stored Y acts as +i/2 on alpha and -i/2 on beta", cy[0][0] == q(0, F(1, 2)) and cy[1][0] == q(0, F(-1, 2)))
    return True


def check_linear_field_spectrum_at_the_family_point():
    """(2): V = V_D(level) + W(N) + k8 Re Q^2 + k9 Im Q^2 + k10 |Q|^2 on all eight components, W = w1 N + w2 N^2/2,
    at the cone family point with the level fixed by the stored vacuum condition: the point is critical; the Hessian
    has 0 (three times: the gauge orbit), m_h^2 = M_Z^2 + 2 N W'', m_pm^2 = M_W^2 + 2 W' (twice), and the normal
    pair 2 W' + 4 N (k10 +- r), r^2 = k8^2 + k9^2; the normal pair spans the directions that change Q; no mixing."""
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    for (g, gp, lam, w1, w2, k8, k9, k10) in SAMPLES:
        zeta = vacuum_zeta(g, gp, lam, w1, w2)
        Wfun = lambda c, w1=w1, w2=w2: w1 * N(c) + w2 * N(c) ** 2 / 2
        V = V_sum(V_D(g, gp, zeta), Wfun, V_Qterms(k8, k9, k10))
        c0 = ([q(0), q(0)], [q(-lam), q(0)])
        Nst = N(c0)
        GA.check("critical point", all(x == 0 for x in grad(V, c0)))
        M = hessian(V, c0)
        r2 = k8 * k8 + k9 * k9
        r = next(F(p, 65) for p in range(0, 65 * 10) if F(p, 65) ** 2 == r2)
        Wp, Wpp = w1 + w2 * Nst, w2
        MW2, MZ2 = g * g * Nst / 2, (g * g + gp * gp) * Nst / 2
        mh2, mpm2 = MZ2 + 2 * Nst * Wpp, MW2 + 2 * Wp
        mHp, mHm = 2 * Wp + 4 * Nst * (k10 + r), 2 * Wp + 4 * Nst * (k10 - r)
        expect = {}
        for val in (F(0), F(0), F(0), mh2, mpm2, mpm2, mHp, mHm):
            expect[val] = expect.get(val, 0) + 1
        GA.check("eight masses: 0 x3, m_h^2, m_pm^2 x2, normal pair 2W' + 4N(k10 +- r)",
                 all(mult(M, val) == k for val, k in expect.items()) and sum(expect.values()) == 8)
        GA.check("trace", sum(M[i][i] for i in range(8)) == mh2 + 2 * mpm2 + mHp + mHm)
        gauge = [vec_of(t(c0)) for t in T] + [vec_of(Y(c0))]
        GA.check("gauge orbit spans the kernel (rank 3, one unbroken generator)", GA.mat_rank(gauge) == 3)
        GA.check("gauge directions are null vectors of the Hessian",
                 all(all(sum(M[i][j] * gv[j] for j in range(8)) == 0 for i in range(8)) for gv in gauge))
        # the normal pair is the block of alpha_1 (a1r, a1i): the directions that change Q at first order
        GA.check("normal block decoupled from the rest", all(M[i][j] == 0 for i in (0, 1) for j in range(2, 8)))
        dQ = [(Q(cadd(c0, E8[k], F(1))) - Q(c0)) for k in range(8)]
        GA.check("only alpha_1 changes Q at first order", all((dQ[k] != q(0)) == (k in (0, 1)) for k in range(8)))
    # pure D-term: the normal pair is massless (D-flat), the stored tangent masses M_Z, M_W
    g, gp, lam = F(2, 3), F(1, 2), F(2)
    zeta = vacuum_zeta(g, gp, lam, F(0), F(0))
    c0 = ([q(0), q(0)], [q(-lam), q(0)])
    M = hessian(V_D(g, gp, zeta), c0)
    Nst = N(c0)
    GA.check("pure D-term: kernel of dimension five (three gauge, the normal pair)", mult(M, F(0)) == 5)
    GA.check("pure D-term: m_h = M_Z, m_pm = M_W", mult(M, (g * g + gp * gp) * Nst / 2) == 1 and mult(M, g * g * Nst / 2) == 2)
    return True


def poly_interp(xs, ys):
    n = len(xs)
    A = [[x ** j for j in range(n)] + [ys[i]] for i, x in enumerate(xs)]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]
        A[col] = [v / pv for v in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [a - f * b for a, b in zip(A[r], A[col])]
    return [A[j][n] for j in range(n)]


def check_null_lift_level_of_the_linear_vacuum():
    """(2), level: with V_Q = k10 |Q + t|^2 (t = H^2), the alpha_1-gradient at alpha = (t rho/lam, 0),
    beta = (-lam, 0), as a polynomial in t, has zero constant and linear terms exactly for
    rho = 1 - 2W'/m_H^2, m_H^2 = 2W' + 4 N k10: the linear vacuum sits at Q = -rho H^2 to first order in H^2; rho -> 1
    as k10 -> infinity, and rho = 1 for the pure D-term (W' = 0). Mutation: rho = 1 fails when W' != 0."""
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    for (g, gp, lam, w1, w2, k10, rho_pin) in ((F(2, 3), F(1, 2), F(2), F(1, 5), F(1, 3), F(1, 2), F(30, 43)),
                                              (F(13, 20), F(7, 20), F(3), F(-1, 10), F(1, 7), F(3), F(945, 964))):
        zeta = vacuum_zeta(g, gp, lam, w1, w2)
        Wfun = lambda c, w1=w1, w2=w2: w1 * N(c) + w2 * N(c) ** 2 / 2
        Nst = lam * lam / 2
        Wp = w1 + w2 * Nst
        mH2 = 2 * Wp + 4 * Nst * k10
        coeffs = {}
        for rho in (1 - 2 * Wp / mH2, F(1)):
            ts = [F(k) for k in range(0, 6)]
            ys = []
            for t in ts:
                V = V_sum(V_D(g, gp, zeta), Wfun, V_Qterms(F(0), F(0), k10, H2=t))
                c = ([q(t * rho / lam), q(0)], [q(-lam), q(0)])
                ys.append(line_coeffs(V, c, E8[0])[1])
            coeffs[rho] = poly_interp(ts, ys)
        good, plain = coeffs[1 - 2 * Wp / mH2], coeffs[F(1)]
        GA.check("constant and first-order terms vanish at rho = 1 - 2W'/m_H^2", good[0] == 0 and good[1] == 0)
        GA.check("rho = 1 is not critical when W' != 0: linear term 2W'/lam", Wp != 0 and plain[1] == 2 * Wp / lam)
        GA.check("rho pinned", 1 - 2 * Wp / mH2 == rho_pin)
    return True


def V4full(k):
    """Scale-free quartic on all of R_C over the ten stored invariants:
    k1 A^2 + k2 B^2 + k3 AB + A(k4 ReQ + k5 ImQ) + B(k6 ReQ + k7 ImQ) + k8 Re Q^2 + k9 Im Q^2 + k10 |Q|^2."""
    def V(c):
        A, B, z = absq(c[0]), absq(c[1]), Q(c)
        z2 = z * z
        return (k[0] * A * A + k[1] * B * B + k[2] * A * B + A * (k[3] * z.re + k[4] * z.im)
                + B * (k[5] * z.re + k[6] * z.im) + k[7] * z2.re + k[8] * z2.im + k[9] * (z.re * z.re + z.im * z.im))
    return V


def abe(k):
    return k[0] + k[1] + k[2], k[0] + k[1] - k[2], 2 * (k[0] - k[1])


# flat physical ray: K_+ = a + b - e = 2 k2 = 0; admissible e = 2 k1 >= 0, 2a - e = 2 k3 >= 0
FLAT = [
    [F(1, 4), F(0), F(3, 2), F(0), F(0), F(0), F(0), F(3, 25), F(4, 25), F(1, 2)],
    [F(0), F(0), F(2), F(0), F(0), F(0), F(0), F(0), F(0), F(-1, 3)],
    [F(1), F(0), F(1, 2), F(1, 3), F(-2), F(0), F(0), F(-6, 5), F(8, 5), F(3)],
]


def check_scale_free_linear_field_on_the_flat_ray():
    """(3): for the scale-free quartic on all eight components with K_+ = 0 (k2 = 0) and the stored admissibility
    (e >= 0, 2a >= e): the ray alpha = 0 is critical iff k6 = k7 = 0 (else a tadpole along alpha_1); there the masses
    are 0 (four: three gauge directions and the scalon), m_pm^2 = 2(2a - e)N twice, and the normal pair
    2(2a - e)N + 4N(k10 +- r); with k4 = k5 = 0 and k10 >= r the potential is nonnegative (sampled on a grid)."""
    premise("synthesis.scale-free-rung-potentials-need-the-flat-physical-branch")
    premise("synthesis.rung-field-on-the-lift-locus")
    for k in FLAT:
        a, b, e = abe(k)
        GA.check("flat and admissible", a + b - e == 0 and e >= 0 and 2 * a >= e)
        for lam in (F(1), F(5, 2)):
            c0 = ([q(0), q(0)], [q(-lam), q(0)])
            Nst = N(c0)
            V = V4full(k)
            GA.check("ray critical with k6 = k7 = 0", all(x == 0 for x in grad(V, c0)))
            M = hessian(V, c0)
            r2 = k[7] ** 2 + k[8] ** 2
            r = next(F(p, 65) for p in range(0, 65 * 10) if F(p, 65) ** 2 == r2)
            mpm2 = 2 * (2 * a - e) * Nst
            expect = {}
            for val in (F(0),) * 4 + (mpm2, mpm2, mpm2 + 4 * Nst * (k[9] + r), mpm2 + 4 * Nst * (k[9] - r)):
                expect[val] = expect.get(val, 0) + 1
            GA.check("masses 0 x4, m_pm^2 x2, normal pair m_pm^2 + 4N(k10 +- r)",
                     all(mult(M, val) == cnt for val, cnt in expect.items()))
            GA.check("all masses proportional to N (degree-four homogeneity)",
                     hessian(V, ([q(0), q(0)], [q(-2 * lam), q(0)])) == [[4 * x for x in row] for row in M])
        for k67 in ((F(1, 2), F(0)), (F(0), F(-1, 3))):
            kk = k[:5] + list(k67) + k[7:]
            GA.check("k6 or k7 != 0: tadpole along alpha_1", grad(V4full(kk), ([q(0), q(0)], [q(-1), q(0)]))[0:2] != [F(0), F(0)])
    # nonnegativity for k4 = k5 = 0, k10 >= r (samples 1; sample 2 has k10 < r = 0 excluded; sample 3 has k4, k5)
    k = FLAT[0]
    grid = [F(n, 2) for n in (-2, -1, 0, 1, 3)]
    vals = []
    for x1 in grid:
        for y1 in grid:
            for x2 in grid[1:4]:
                for y3 in grid[1:4]:
                    c = ([q(x1, y1), q(x2, 1)], [q(y3, x1), q(1, -y1)])
                    vals.append(V4full(k)(c))
    GA.check("V >= 0 on the grid (k4 = k5 = 0, k10 >= r)", min(vals) >= 0 and len(vals) == 225)
    kneg = [F(0), F(0), F(1, 2), F(0), F(0), F(0), F(0), F(0), F(0), F(-1)]
    a, b, e = abe(kneg)
    GA.check("k10 < -(2a - e)/2: tachyonic normal pair", 2 * (2 * a - e) * F(1, 2) + 4 * F(1, 2) * kneg[9] < 0)
    GA.check("and the potential is negative next to the ray", V4full(kneg)(([q(F(1, 10)), q(0)], [q(-1), q(0)])) == F(-1, 200))
    return True


# ---------------------------------------------------------------- Gildener-Weinberg with the normal pair
PI_LO, PI_HI = F(333, 106), F(355, 113)
V_LO, V_HI = F(246), F(247)
MT_LO, MT_HI = F(162), F(173)
MH_LO, MH_HI = F(125), F(1254, 10)
TOP, HN, HC = F(456), F(542), F(383)
TWO, FOUR = F(2), F(4)


def light():
    mb = quantity("quantity.bottom-quark-mass")
    mc = quantity("quantity.charm-quark-mass")
    mtau = quantity("quantity.tau-mass") / 1000
    return 12 * mb ** 4 + 12 * mc ** 4 + 4 * mtau ** 4


def Xsum(pi, v, mh, mt, MW, MZ):
    """X = 2 m_pm^4 + m_H^4 + m_A^4 from 8 pi^2 v^2 m_h^2 = 6 M_W^4 + 3 M_Z^4 + X - 12 m_t^4 - light."""
    return 8 * pi * pi * v * v * mh * mh - 6 * MW ** 4 - 3 * MZ ** 4 + 12 * mt ** 4 + light()


def p4(x):
    return x * x * x * x


RAY1 = ([q(0), q(0)], [q(-1), q(0)])
LO_PM, CENTRAL_HI = F(450), F(455)


def check_scalon_sum_with_the_normal_pair():
    """(4): real-scalar content on the flat ray of the linear field: eight components minus three gauge minus the
    scalon leaves four, the charged pair (two) and the normal pair (two), all with M^2 proportional to N; so (GW)
    gives 2 m_pm^4 + m_H^4 + m_A^4 = X. Over the stored input box X/2 lies in (450^4, 456^4); hence m_pm < 456 GeV,
    m_H, m_A < 542 GeV, and with m_H, m_A >= m_pm (k4 = k5 = 0, k10 >= r) m_pm < 383 GeV; the stored bracket for m_pm
    is the case m_H = m_A = 0. Lower ends pinned: X > 535^4, X/4 > 378^4."""
    premise("synthesis.transmutation-of-the-rung-field-needs-a-charged-pair-near-450-gev")
    premise("synthesis.imported-coleman-weinberg-gildener-weinberg-scalon-mass")
    MW = quantity("quantity.w-boson-mass")
    MZ = quantity("quantity.z-boson-mass")
    mh = quantity("quantity.higgs-boson-mass")
    mt = quantity("quantity.top-quark-mass")
    mtz = quantity("quantity.top-quark-mass-mz")
    vF = quantity("quantity.fermi-scale")
    GA.check("stored inputs inside the box", MH_LO <= mh <= MH_HI and MT_LO <= mt <= MT_HI and MT_LO <= mtz <= MT_HI
             and V_LO <= vF <= V_HI)
    M = hessian(V4full(FLAT[0]), RAY1)
    GA.check("four massive real scalars on the ray", 8 - mult(M, F(0)) == 4)
    lo = Xsum(PI_LO, V_LO, MH_LO, MT_LO, MW, MZ)
    hi = Xsum(PI_HI, V_HI, MH_HI, MT_HI, MW, MZ)
    GA.check("X/2 above 450^4 over the box", p4(LO_PM) < lo / 2)
    GA.check("m_pm^4 <= X/2 < 456^4", hi < TWO * p4(TOP))
    GA.check("m_H^4, m_A^4 <= X < 542^4", hi < p4(HN))
    GA.check("with m_H, m_A >= m_pm: 4 m_pm^4 <= X < 4 * 383^4", hi < FOUR * p4(HC))
    GA.check("lower ends: X > 535^4 and X/4 > 378^4", lo > p4(F(535)) and lo / 4 > p4(F(378)))
    central = Xsum(PI_HI, vF, mh, mt, MW, MZ)
    GA.check("central inputs: X/2 above 454^4 (massless normal pair: m_pm in (454, 455))",
             central / 2 > p4(F(454)) and central < TWO * p4(CENTRAL_HI))
    return True


TAU_TERMS = 70
ROUND = 10 ** 15
MU_TOP = F(900, 1000)


def binom(n, kk):
    r = 1
    for i in range(kk):
        r = r * (n - i) // (i + 1)
    return r


def rdown(x):
    return F((x.numerator * ROUND) // x.denominator, ROUND)


def rup(x):
    return -rdown(-x)


def arcsin2(tau):
    S = F(0)
    for n in range(1, TAU_TERMS + 1):
        S += (4 * tau) ** n / (2 * n * n * binom(2 * n, n))
        S = rdown(S)
    return S, rup(S + tau ** (TAU_TERMS + 1) / (1 - tau) + F(TAU_TERMS, ROUND))


def amps(tau):
    flo, fhi = arcsin2(tau)
    A1 = sorted(-(2 * tau * tau + 3 * tau + 3 * (2 * tau - 1) * fv) / (tau * tau) for fv in (flo, fhi))
    A12 = sorted(2 * (tau + (tau - 1) * fv) / (tau * tau) for fv in (flo, fhi))
    A0 = sorted(-(tau - fv) / (tau * tau) for fv in (flo, fhi))
    return A1, A12, A0


def check_diphoton_below_090_for_every_charged_mass():
    """(5): A0(tau) = (f - tau)/tau^2 = (1/2) sum_{n >= 2} 4^n tau^(n-2)/(n^2 C(2n, n)) has positive coefficients, so it
    increases with tau = m_h^2/(4 m_pm^2), i.e. as m_pm decreases; the charged pair enters with unit weight on the flat
    ray and the neutral normal pair not at all; the SM amplitude is negative and larger in size than A0 < 1, so
    mu_gamgam = ((A_SM + A0)/A_SM)^2 decreases as m_pm decreases. At m_pm = 456 GeV it is below 0.900, hence below
    0.900 for every m_pm in (m_h/2, 456] GeV; sampled values decrease."""
    premise("synthesis.transmutation-of-the-rung-field-needs-a-charged-pair-near-450-gev")
    mh = quantity("quantity.higgs-boson-mass")
    MW = quantity("quantity.w-boson-mass")
    mt = quantity("quantity.top-quark-mass")
    GA.check("A0 series: leading coefficient 1/3 and all coefficients positive",
             F(4 ** 2, 2 * 4 * binom(4, 2)) == F(1, 3)
             and all(F(4 ** n, 2 * n * n * binom(2 * n, n)) > 0 for n in range(2, TAU_TERMS + 1)))
    A1, _, _ = amps(mh * mh / (4 * MW * MW))
    _, A12, _ = amps(mh * mh / (4 * mt * mt))
    den = [A1[0] + F(4, 3) * A12[0], A1[1] + F(4, 3) * A12[1]]
    GA.check("SM amplitude below -6.4, so |A_SM| > 1", den[1] < F(-64, 10))
    prev = None
    for mpm in (F(456), F(400), F(300), F(200), F(100), F(70)):
        tau = mh * mh / (4 * mpm * mpm)
        GA.check("below threshold", 0 < tau < 1)
        _, _, A0 = amps(tau)
        GA.check("0 < A0 < 1", F(1, 3) < A0[0] and A0[1] < 1)
        mus = [((d + a0) / d) ** 2 for d in den for a0 in A0]
        GA.check("mu_gamgam below 0.900", max(mus) < MU_TOP)
        if prev is not None:
            GA.check("mu decreases with the charged mass", max(mus) < prev)
        prev = min(mus)
    return True
