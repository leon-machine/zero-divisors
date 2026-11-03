"""synthesis.scale-free-rung-potentials-need-the-flat-physical-branch: exact checks.

Coordinates of the stored rung field (synthesis.rung-field-on-the-lift-locus): c = sum_a alpha_a v_a + beta_a w_a,
alpha, beta in C^2 as Gaussian rationals (GA.QI); Q(c) = alpha^T beta; N(c) = (|alpha|^2 + |beta|^2)/2;
m(c) = (|alpha|^2 - |beta|^2)/2; G(c, d) = Re(c* . d); U(2): alpha -> X alpha, beta -> conj(X) beta; c* = (conj beta, conj alpha).
Lift locus L: Q = -H^2; lift family c_lambda: alpha = (H^2/lambda, 0), beta = (-lambda, 0), physical half lambda >= H.
Cone L0 (the H -> 0 limit): Q = 0, flat physical ray alpha = 0, beta = (-lambda, 0).
Scale-free potential: V = sum_i k_i I_i over the ten real quartic invariants I_i built from |alpha|^2, |beta|^2, Q.
Masses: Hessian of V along curves on L (or L0) divided by the kinetic coefficient 2 N(d) of the stored Hermitian term.
Exact throughout (Fractions, Gaussian rationals); the conformal identity uses the GA engine.
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




# ---------------------------------------------------------------- scale-free quartic invariants
def reQ(c):
    return Q(c).re


def imQ(c):
    return Q(c).im


def INV(c):
    """The ten real quartic U(2)-invariants generated by |alpha|^2, |beta|^2, Q, conj Q."""
    A, B, qq = absq(c[0]), absq(c[1]), Q(c)
    q2 = qq * qq
    return [A * A, B * B, A * B, A * qq.re, A * qq.im, B * qq.re, B * qq.im, q2.re, q2.im,
            qq.re * qq.re + qq.im * qq.im]


def Vk(k):
    return lambda c: sum((ki * Ii for ki, Ii in zip(k, INV(c))), F(0))


def reduced(k, H2v):
    """(a, b, e, d, f, c0) of V = sum k_i I_i restricted to Q = -H^2."""
    a = k[0] + k[1] + k[2]
    b = k[0] + k[1] - k[2]
    e = 2 * (k[0] - k[1])
    d = -(k[3] + k[5])
    f = -(k[3] - k[5])
    c0 = k[7] + k[9]
    return a, b, e, d, f, c0


def V_red(coef, Nv, mv_, H2v):
    a, b, e, d, f, c0 = coef
    return a * Nv * Nv + b * mv_ * mv_ + e * Nv * mv_ + H2v * (d * Nv + f * mv_) + c0 * H2v * H2v


KS = [
    [F(1, 3), F(-2, 5), F(7, 4), F(3), F(-1, 2), F(5, 6), F(2), F(-3, 7), F(4, 9), F(1, 8)],
    [F(-1), F(2), F(1, 2), F(0), F(1), F(-4, 3), F(0), F(5), F(-1), F(3, 2)],
    [F(2, 7), F(2, 7), F(-1, 5), F(1, 3), F(0), F(1, 3), F(0), F(0), F(0), F(-1)],
]


def on_L(alpha, b2, H2v):
    """A point of L with given alpha (alpha_1 != 0) and beta_2 = b2."""
    b1 = (q(-H2v) - alpha[1] * b2) / alpha[0]
    return (alpha, [b1, b2])


L_PTS = [on_L([q(1, 2), q(-3, 1)], q(2, -1), H2), on_L([q(F(1, 3)), q(2, 2)], q(0, 1), H2),
         on_L([q(5, -2), q(1)], q(4, -3), H2), on_L([q(-2, 1), q(0, 3)], q(F(1, 2)), H2)]


def check_quartic_invariants_restrict_to_five_couplings():
    """(1): the ten quartic invariants are U(2)-invariant; on L every V = sum k_i I_i equals
    a N^2 + b m^2 + e N m + H^2 (d N + f m) + c0 H^4 with the stated linear map k -> (a, b, e, d, f, c0);
    c -> c* sends (e, f) to (-e, -f) and fixes (a, b, d, c0); the D-term is homogeneous of degree four
    exactly when its level vanishes, and then (a, b, e, d, f, c0) = (g^2/8, g'^2/8, 0, 0, 0, -g^2/8)."""
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    for c in SAMPLES + L_PTS:
        for X in US:
            GA.check("quartic invariants U(2)-invariant", INV(u2(X)(c)) == INV(c))
    for c in L_PTS:
        GA.check("sample point on L", Q(c) == q(-H2))
        for k in KS:
            V = Vk(k)
            coef = reduced(k, H2)
            GA.check("restriction to L is the five-coupling form", V(c) == V_red(coef, N(c), m(c), H2))
            cst = ([conj(z) for z in c[1]], [conj(z) for z in c[0]])
            a, b, e, d, f, c0 = coef
            GA.check("c* on L: (e, f) -> (-e, -f)", V(cst) == V_red((a, b, -e, d, -f, c0), N(c), m(c), H2))
    # the restricted coefficients separate the five couplings: the five-coupling form takes
    # independent values at points of L (the (N, m) samples are not on one conic)
    rows = [[N(c) ** 2, m(c) ** 2, N(c) * m(c), H2 * N(c), H2 * m(c), H2 * H2] for c in L_PTS + [clam(F(2)), clam(F(3))]]
    GA.check("five couplings and the constant are independent on L", GA.mat_rank(rows) == 6)
    for zeta in (F(0), F(1, 3)):
        V = make_V(zeta, F(0), F(0))
        s = F(2)
        homog = all(V(([s * z for z in c[0]], [s * z for z in c[1]])) == s ** 4 * V(c) for c in SAMPLES)
        GA.check("D-term homogeneous of degree four iff level zero", homog == (zeta == 0))
    V = make_V(F(0), F(0), F(0))
    for c in L_PTS:
        GA.check("D-term at level zero in five-coupling form",
                 V(c) == V_red((g * g / 8, gp * gp / 8, F(0), F(0), F(0), -g * g / 8), N(c), m(c), H2))
    return True


def fam_F(coef, X):
    """V(c_lambda)/H^4 - (a + c0) with X = lambda^2/H^2 = e^t: (a+b) s^2 - e s u + d u - f s."""
    a, b, e, d, f, c0 = coef
    u = (X + 1 / X) / 2
    s = (X - 1 / X) / 2
    return (a + b) * s * s - e * s * u + d * u - f * s


def fam_dF(coef, X):
    a, b, e, d, f, c0 = coef
    u = (X + 1 / X) / 2
    s = (X - 1 / X) / 2
    return 2 * (a + b) * s * u - e * (u * u + s * s) + d * s - f * u


FRAMES_T = (F(1, 3), F(1), F(2), F(7, 2))
# (a, b, e, d, f) with K_+ > 0 and K_+ |K_-| a rational square (root given)
BOUNDED = [((F(1), F(-3, 8), F(3, 8), F(3), F(-2)), F(1, 2)),
           ((F(1, 10), F(1, 10), F(0), F(1, 2), F(1, 2)), F(1, 5)),
           ((F(2), F(1, 2), F(3, 2), F(-5), F(0)), F(2))]
# (a, b, e, d, X*) for exactly constructed critical points
CRIT = [(F(1, 3), F(1, 5), F(1, 7), F(2), F(9)), (F(1, 2), F(-1, 3), F(1, 9), F(-3), F(4)),
        (F(1, 1000), F(1, 1000), F(1, 1000), F(1), F(1000))]
# near-saturating critical points: (d, f, K_-, X*, a) with d < 0 < f, f > |d|; K_+ solved for criticality
SAT = [(F(-1), F(3), F(1, 2), F(20), F(1)), (F(-2, 5), F(1), F(2), F(100), F(1, 3))]
RUNAWAY = [(F(1, 4), F(-1, 2), F(0), F(1), F(-1)), (F(1), F(0), F(3, 2), F(1), F(-1))]
XS_FAR = [F(10), F(100), F(1000), F(10000)]
HSTEP = F(1, 1000000)
TOL = F(1, 1000)
ZERO = F(0)
ONE = F(1)
GRID = [F(8 + j, 8) for j in range(40)]


def check_family_potential_scaling_and_frame_bound():
    """(2): along the family V(c_lambda) = H^4 [a + c0 + (a+b) s^2 - e s u + d u - f s], u = cosh t, s = sinh t,
    e^t = X = lambda^2/H^2; the joint scaling (c, H) -> (2c, 2H) maps c_lambda(H) to c_{2 lambda}(2H) and V to 16 V;
    the exact expansion 4F = K_+ X^2 + K_- X^-2 - 2(a+b) + 2(d - f) X + 2(d + f)/X and
    2F' = K_+ X^2 - K_- X^-2 + 2(d s - f u), K_pm = a + b -+ e; at X0 = (2D + R)/K_+, R^2 = K_+|K_-|, D = |d| + |f|:
    K_+ X0^2 - 2 D X0 - |K_-| = 2 D R/K_+, and F' > 0 above X0; at exact critical points
    K_+ <= 2D/X + |K_-|/X^2; for K_+ < 0 the expansion is negative and decreasing at large X."""
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("synthesis.rung-unit-transverse-to-norm")
    for k in KS:
        V = Vk(k)
        coef = reduced(k, H2)
        a, b, e, d, f, c0 = coef
        Kp, Km = a + b - e, a + b + e
        for lam in FRAMES_T:
            X = lam * lam / H2
            cl = clam(lam)
            GA.check("family potential formula", V(cl) == H2 * H2 * (a + c0 + fam_F(coef, X)))
            c2 = ([q(4 * H2 / (2 * lam)), q(0)], [q(-2 * lam), q(0)])
            GA.check("joint scaling maps the family to the family", c2 == ([q(2) * z for z in cl[0]], [q(2) * z for z in cl[1]]))
            GA.check("joint scaling multiplies V by s^4", V(c2) == 16 * V(cl))
            u = (X + 1 / X) / 2
            s = (X - 1 / X) / 2
            GA.check("expansion of 4F", 4 * fam_F(coef, X) == Kp * X * X + Km / (X * X) - 2 * (a + b)
                     + 2 * (d - f) * X + 2 * (d + f) / X)
            GA.check("2F' identity", 2 * fam_dF(coef, X) == Kp * X * X - Km / (X * X) + 2 * (d * s - f * u))
            num = fam_F(coef, X * (1 + HSTEP)) - fam_F(coef, X * (1 - HSTEP))
            GA.check("F' agrees with a difference quotient of F", abs(num / (2 * HSTEP) - fam_dF(coef, X)) < TOL * (ONE + X * X))
    for (a, b, e, d, f), R in BOUNDED:
        coef = (a, b, e, d, f, ZERO)
        Kp, Km = a + b - e, a + b + e
        D = abs(d) + abs(f)
        GA.check("sample has K_+ > 0 and R^2 = K_+ |K_-|", Kp > 0 and R * R == Kp * abs(Km))
        X0 = (2 * D + R) / Kp
        GA.check("value of the quadratic at X0", Kp * X0 * X0 - 2 * D * X0 - abs(Km) == 2 * D * R / Kp)
        for X in [max(X0, ONE) * gm for gm in GRID]:
            GA.check("2F' >= K_+ X^2 - 2 D X - |K_-| > 0 above X0",
                     2 * fam_dF(coef, X) >= Kp * X * X - 2 * D * X - abs(Km) > 0)
    for a, b, e, d, Xs in CRIT:
        u = (Xs + 1 / Xs) / 2
        s = (Xs - 1 / Xs) / 2
        f = (2 * (a + b) * s * u - e * (u * u + s * s) + d * s) / u
        coef = (a, b, e, d, f, ZERO)
        Kp, Km = a + b - e, a + b + e
        GA.check("constructed critical point", fam_dF(coef, Xs) == 0)
        GA.check("criticality: K_+ X^2 - K_- X^-2 = 2(f u - d s)", Kp * Xs * Xs - Km / (Xs * Xs) == 2 * (f * u - d * s))
        GA.check("K_+ <= 2D/X + |K_-|/X^2 at the critical point",
                 Kp <= 2 * (abs(d) + abs(f)) / Xs + abs(Km) / (Xs * Xs))
        GA.check("N*/H^2 = cosh t <= e^t", u <= Xs)
    for d, f, Km, Xs, a in SAT:
        D = abs(d) + abs(f)
        Kp = D / Xs + (f - abs(d)) / Xs ** 3 + Km / Xs ** 4
        e = (Km - Kp) / 2
        b = (Kp + Km) / 2 - a
        coef = (a, b, e, d, f, ZERO)
        GA.check("near-saturating critical point", fam_dF(coef, Xs) == 0 and a + b - e == Kp and a + b + e == Km)
        GA.check("true bound holds", Kp <= 2 * D / Xs + abs(Km) / (Xs * Xs))
        GA.check("the bound without the factor 2 and the K_- term fails", Kp > D / Xs)
        GA.check("K_+ X - D is the next order (f - |d|)/X^2 + K_-/X^3", Kp * Xs - D == (f - abs(d)) / (Xs * Xs) + Km / Xs ** 3)
    for a, b, e, d, f in RUNAWAY:
        coef = (a, b, e, d, f, ZERO)
        Kp = a + b - e
        GA.check("sample has K_+ < 0", Kp < ZERO)
        vals = [fam_F(coef, X) for X in XS_FAR]
        GA.check("potential decreases without bound", all(x > y for x, y in zip(vals, vals[1:])))
    return True


def V4(a, b, e):
    return lambda c: a * N(c) ** 2 + b * m(c) ** 2 + e * N(c) * m(c)


def check_gildener_weinberg_admissibility():
    """(3): V4 = a N^2 + b m^2 + e N m >= 0 on the cone |m| <= N with V4 = 0 on the physical ray m = -N iff
    a + b = e, e >= 0, 2a >= e: on admissible samples V4 >= 0 on a grid of s = -m/N in [-1, 1] and the minimum of
    a + b s^2 - e s on [-1, 1] is at s = 1; each violated inequality gives an explicit negative value."""
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    adm = [(F(1), F(-1), F(0)), (F(3, 4), F(-1, 4), F(1, 2)), (F(1, 2), F(1, 2), F(1)), (F(2), F(-3, 2), F(1, 2))]
    grid = [F(j, 48) for j in range(-48, 49)]
    for a, b, e in adm:
        GA.check("admissible sample satisfies the conditions", a + b == e and e >= 0 and 2 * a >= e)
        fs = [a + b * s * s - e * s for s in grid]
        GA.check("V4 >= 0 on the cone grid", min(fs) >= 0)
        GA.check("V4 = 0 on the physical ray", a + b - e == 0)
        GA.check("slope at the physical ray non-positive", 2 * b - e <= 0)
        GA.check("mirror ray value 2e", a + b + e == 2 * e)
    # violations: K_+ != 0 (no flat physical ray), e < 0 (mirror ray negative), 2a < e (negative just inside)
    a, b, e = F(1), F(-1, 2), F(0)
    GA.check("K_+ > 0: physical ray not flat", a + b - e > 0)
    a, b, e = F(-1, 4), F(-3, 4), F(-1)
    GA.check("e < 0: V4 negative on the mirror ray", a + b - e == 0 and a + b + e < 0)
    a, b, e = F(1, 4), F(3, 4), F(1)
    s = F(9, 10)
    GA.check("2a < e: V4 negative inside the cone", a + b - e == 0 and 2 * a < e and a + b * s * s - e * s < 0)
    # the cone value from field points: a point of L0 with s = -m/N
    al, be = [q(0), q(1)], [q(-3), q(0)]
    c = (al, be)
    GA.check("point on the cone L0", Q(c) == q(0) and abs(m(c)) <= N(c))
    a, b, e = F(1, 4), F(3, 4), F(1)
    GA.check("V4 at a field point matches the cone formula",
             V4(a, b, e)(c) == N(c) ** 2 * (a + b * (m(c) / N(c)) ** 2 + e * (m(c) / N(c))))
    return True


def hess_on_L0(V, cs, d):
    """(first, second) derivative at 0 of V along cs + eps d + eps^2 e on Q = 0, for cs = (0, (beta1, 0)):
    e = (Q(d)/(-beta1)... chosen so that Qb(cs, e) = -Q(d)."""
    beta1 = cs[1][0]
    e = ([q(-1) * Q(d) / beta1, q(0)], [q(0), q(0)])

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


def physical_dirs_L0(cs):
    gauge = [t(cs) for t in T] + [Y(cs)]
    rows = []
    for k in range(8):
        qb = Qb(cs, E8[k])
        rows.append([qb.re, qb.im] + [G(gv, E8[k]) for gv in gauge])
    M = [[rows[k][r] for k in range(8)] for r in range(6)]
    return nullspace(M, 8)


def check_flat_ray_tree_masses():
    """(3): on the flat physical ray of an admissible V4 (exact Hessians on the cone L0): the tangent space minus the
    gauge orbit is three-dimensional; the neutral mode (beta scaled) is massless; the charged plane (alpha_2) has
    mass^2 = 2(2a - e) N, i.e. (2a - e) v^2 with v^2 = 2N; neutral and charged directions do not mix."""
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    for a, b, e in ((F(1), F(-1), F(0)), (F(3, 4), F(-1, 4), F(1, 2)), (F(2), F(-3, 2), F(1, 2))):
        V = V4(a, b, e)
        for lam in (F(1), F(5, 2)):
            cs = ([q(0), q(0)], [q(-lam), q(0)])
            Nst = N(cs)
            GA.check("ray on L0 with m = -N", Q(cs) == q(0) and m(cs) == -Nst)
            GA.check("three physical directions on L0", len(physical_dirs_L0(cs)) == 3)
            dn = ([q(0), q(0)], [q(-1), q(0)])
            dc1 = ([q(0), q(1)], [q(0), q(0)])
            dc2 = ([q(0), q(0, 1)], [q(0), q(0)])
            gauge = [t(cs) for t in T] + [Y(cs)]
            for d in (dn, dc1, dc2):
                GA.check("direction tangent to L0", Qb(cs, d) == q(0))
                GA.check("direction orthogonal to the gauge orbit", all(G(gv, d) == 0 for gv in gauge))
            first, hn = hess_on_L0(V, cs, dn)
            GA.check("flat: first derivative zero, neutral mass zero", first == 0 and hn == 0)
            for d in (dc1, dc2):
                first, hc = hess_on_L0(V, cs, d)
                GA.check("charged: m^2 = 2 (2a - e) N", first == 0 and hc / (2 * N(d)) == 2 * (2 * a - e) * Nst)
            _, hs = hess_on_L0(V, cs, cadd(dn, dc1))
            _, h1 = hess_on_L0(V, cs, dc1)
            GA.check("no neutral-charged mixing", hs == hn + h1)
    return True


def check_d_term_with_norm_quartic_is_not_admissible():
    """(4): the level-zero D-term plus kappa N^2 is flat on the physical ray only for kappa = -(g^2 + g'^2)/8, and there
    the charged mass^2 is -g'^2 N/2 = M_W^2 - M_Z^2 < 0 (exact Hessian of the moment-map D-term on L0) and V < 0 at an
    interior point of the cone; adding kappa' m^2 with kappa' < -g'^2/8 gives an admissible flat ray with m_pm^2 > 0."""
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("synthesis.rung-field-charged-scalar-sum-rule")
    VD = make_V(F(0), F(0), F(0))
    kap = -(g * g + gp * gp) / 8
    for kp in (F(0), -gp * gp / 8 - F(1, 5)):
        def V(c, kp=kp):
            return VD(c) + kap * N(c) ** 2 + kp * m(c) ** 2 + (-kp) * N(c) ** 2
        for lam in (F(1), F(3)):
            cs = ([q(0), q(0)], [q(-lam), q(0)])
            Nst = N(cs)
            MW2, MZ2 = g * g * Nst / 2, (g * g + gp * gp) * Nst / 2
            GA.check("flat along the physical ray", V(cs) == 0 and V(([q(0), q(0)], [q(-2 * lam), q(0)])) == 0)
            dc = ([q(0), q(1)], [q(0), q(0)])
            _, hc = hess_on_L0(V, cs, dc)
            mpm2 = hc / (2 * N(dc))
            if kp == 0:
                GA.check("kappa N^2 alone: m_pm^2 = M_W^2 - M_Z^2 < 0", mpm2 == MW2 - MZ2 and mpm2 < 0)
                inner = ([q(1), q(0)], [q(0), q(1)])
                GA.check("interior point of the cone", Q(inner) == q(0) and m(inner) == 0)
                GA.check("V < 0 inside the cone: unbounded below", V(inner) < 0)
            else:
                # a = g^2/8 + kap - kp, b = g'^2/8 + kp, e = 0 ; m_pm^2 = 4 a N
                a = g * g / 8 + kap - kp
                GA.check("with kappa' m^2: m_pm^2 = 4 a N > 0", mpm2 == 4 * a * Nst and mpm2 > 0)
    return True


SQ = (1, -1, 1, -1)
E1, E2, EP, EM = GA.gen(0), GA.gen(1), GA.gen(2), GA.gen(3)
X_SAMPLES = [GA.add(GA.scal(3, E1), E2), GA.add(GA.scal(F(1, 2), E1), GA.scal(-2, E2))]
MU_SAMPLES = [F(1, 3), F(2), F(7)]
I_GROUND = GA.scal(F(3, 2), E1)


def check_rung_unit_is_the_conformal_dilatation():
    """(5): in the conformal model of a ground plane (GA engine, e1^2 = 1, e2^2 = -1, e+^2 = 1, e-^2 = -1),
    v = (e- + e+)/2, w = (e+ - e-)/2, n0 = -w, ninf = 2v: X_mu(x) = mu n0 + x + Q(x)/(2 mu) ninf is null and equals
    mu X_1(x/mu), the conformal dilatation of the ground point by 1/mu; for Q(I) = H^2 its rung component is
    c_mu = -mu w + (H^2/mu) v, with Q(c_mu) = -H^2 for every mu."""
    premise("synthesis.rung-unit-transverse-to-norm")
    vv = GA.scal(F(1, 2), GA.add(EM, EP))
    ww = GA.scal(F(1, 2), GA.sub(EP, EM))
    n0, ninf = GA.neg(ww), GA.scal(2, vv)

    def Qf(x):
        return GA.mul(x, x, SQ).get((), F(0))

    def X(mu, x):
        return GA.add(GA.scal(mu, n0), x, GA.scal(Qf(x) / (2 * mu), ninf))
    GA.check("v, w null with vw + wv = 1", Qf(vv) == 0 and Qf(ww) == 0
             and GA.eq(GA.add(GA.mul(vv, ww, SQ), GA.mul(ww, vv, SQ)), GA.sc(1)))
    for x in X_SAMPLES:
        for mu in MU_SAMPLES:
            GA.check("X_mu(x) null", Qf(X(mu, x)) == 0)
            GA.check("X_mu(x) = mu X_1(x/mu)", GA.eq(X(mu, x), GA.scal(mu, X(F(1), GA.scal(1 / mu, x)))))
    H2v = Qf(I_GROUND)
    for mu in MU_SAMPLES:
        rung = GA.sub(X(mu, I_GROUND), I_GROUND)
        cmu = GA.add(GA.scal(-mu, ww), GA.scal(H2v / mu, vv))
        GA.check("rung component c_mu = -mu w + (H^2/mu) v", GA.eq(rung, cmu))
        GA.check("Q(c_mu) = -H^2 for every mu", Qf(cmu) == -H2v)
    return True
