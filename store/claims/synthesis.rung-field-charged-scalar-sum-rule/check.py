"""synthesis.rung-field-charged-scalar-sum-rule: exact checks.

Same coordinates and conventions as the stored check of the D-term action
(synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus): c = sum_a alpha_a v_a + beta_a w_a over
the Gaussian rationals; N, m, Q, G, moment maps mu; lift locus L: Q(c) = -H^2; lift family c_lambda.
V = (1/2)[g^2 sum_j mu_j^2 + g'^2 (mu_Y - zeta)^2] + W(N), W a polynomial sum_k w_k N^k (k = 1, 2, 3), the level
xi = 2 zeta chosen so that the family point c_lambda* is critical. Masses from the Hessian of V restricted to L
(curves c + eps d + eps^2 e on L) divided by the kinetic coefficient 2 N(d), as in the stored check.
Sum rule: (m_pm^2 - M_W^2) - (m_h^2 - M_Z^2) = 2 (m*/N*)^2 (W'(N*) - N* W''(N*)).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise, quantity

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


def hess_on_L(V, cs, d, NP=4):
    """(first derivative, second derivative) at eps = 0 of V along c(eps) = cs + eps d + eps^2 e on L,
    e = -(Q(d)/(2 Q(cs))) cs, by exact interpolation of the degree-8 polynomial V(c(eps))."""
    s_e = q(-1) * Q(d) / (q(2) * Q(cs))
    e = ([s_e * a for a in cs[0]], [s_e * a for a in cs[1]])

    def c_of(s):
        return ([a + s * b + s * s * ee for a, b, ee in zip(cs[0], d[0], e[0])],
                [a + s * b + s * s * ee for a, b, ee in zip(cs[1], d[1], e[1])])
    pts = [F(k, 3) for k in range(-NP, NP + 1)]
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



SR_FRAMES = (F(1, 2), F(3), F(7))
SR_SAMPLES = ({1: F(3, 7)}, {2: F(2, 5)}, {1: F(-1, 4), 2: F(3, 2)}, {3: F(1, 9)}, {1: F(2), 2: F(-1, 3), 3: F(1, 5)})
EQ_FRAMES = (F(1, 3), F(2), F(9))
EQ_KAPPAS = (F(1, 8), F(5, 3))
MU_LIN = F(-2, 3)
MH_LO, MH_HI = F(125), F(1254, 10)   # GeV, bracket of the measured Higgs mass (cited in the proof)
LEP_REACH = F(105)                    # GeV


def W_of(ws):
    """W(N) = sum_k ws[k] N^k (k >= 1), with W' and W''."""
    def W(x):
        return sum((w * x ** k for k, w in ws.items()), F(0))

    def Wp(x):
        return sum((k * w * x ** (k - 1) for k, w in ws.items()), F(0))

    def Wpp(x):
        return sum((k * (k - 1) * w * x ** (k - 2) for k, w in ws.items() if k >= 2), F(0))
    return W, Wp, Wpp


def make_VW(zeta, W, km=F(0)):
    def V(c):
        mus = mu(c)
        return (g * g * sum(x * x for x in mus[:3]) + gp * gp * (mus[3] - zeta) ** 2) / 2 + W(N(c)) + km * m(c) ** 2
    return V


def masses(lamstar, ws, km=F(0)):
    """(m_h^2, m_pm^2 list, M_Z^2, M_W^2, m*, N*, W'(N*), W''(N*)) at the family point c_lambda*, with the level
    chosen so that it is critical; asserts criticality in every direction used."""
    W, Wp, Wpp = W_of(ws)
    cs = clam(lamstar)
    mstar, Nst = m(cs), N(cs)
    xi = mstar + (4 / (gp * gp)) * (g * g * mstar / 4 + Wp(Nst) * mstar / Nst + 2 * km * mstar)
    V = make_VW(xi / 2, W, km)
    NP = 4 + 2 * max(0, max(ws) - 2) if ws else 4
    d0 = dclam(lamstar)
    first, h0 = hess_on_L(V, cs, d0, NP)
    GA.check("critical along the family", first == 0)
    mh2 = h0 / (2 * N(d0))
    charged = []
    for d in physical_dirs(cs):
        dd = cadd(d, d0, -G(d, d0) / G(d0, d0))
        if N(dd) != 0:
            charged.append(dd)
    GA.check("charged plane two-dimensional", len(charged) == 2)
    mpm = []
    for d in charged + [cadd(charged[0], charged[1])]:
        first, hh = hess_on_L(V, cs, d, NP)
        GA.check("critical in the charged plane", first == 0)
        mpm.append(hh / (2 * N(d)))
    return mh2, mpm, (g * g + gp * gp) * Nst / 2, g * g * Nst / 2, mstar, Nst, Wp(Nst), Wpp(Nst)


def check_charged_scalar_sum_rule():
    """For W linear, quadratic and cubic in N (with and without a constant shift of scale), in three frames:
    the charged pair is degenerate and (m_pm^2 - M_W^2) - (m_h^2 - M_Z^2) = 2 (m*/N*)^2 (W' - N* W'')."""
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("synthesis.rung-field-on-the-lift-locus")
    seen_nonzero = False
    for lamstar in SR_FRAMES:
        for ws in SR_SAMPLES:
            mh2, mpm, MZ2, MW2, mstar, Nst, Wp, Wpp = masses(lamstar, ws)
            mp = mpm.pop()
            GA.check("charged pair degenerate", all(x == mp for x in mpm))
            delta = (mp - MW2) - (mh2 - MZ2)
            rhs = 2 * (mstar / Nst) ** 2 * (Wp - Nst * Wpp)
            GA.check("sum rule (m_pm^2 - M_W^2) - (m_h^2 - M_Z^2) = 2 (m*/N*)^2 (W' - N* W'')", delta == rhs)
            GA.check("boundary relation N*^2 = m*^2 + H^4", Nst ** 2 == mstar ** 2 + H2 ** 2)
            seen_nonzero = seen_nonzero or delta != 0
    GA.check("the sum rule is not vacuous: some sample has a nonzero defect", seen_nonzero)
    return True


def check_scale_free_invariant_gives_the_equal_shift():
    """W = kappa N^2 (no constant of its own): the defect vanishes in every frame, m_pm^2 - M_W^2 = m_h^2 - M_Z^2
    = 4 kappa N*; a linear term mu N leaves a defect 2 mu (m*/N*)^2, below 2 |mu|."""
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("synthesis.rung-field-on-the-lift-locus")
    for lamstar in EQ_FRAMES:
        for kappa in EQ_KAPPAS:
            mh2, mpm, MZ2, MW2, mstar, Nst, Wp, Wpp = masses(lamstar, {2: kappa})
            GA.check("equal shift", mpm[0] - MW2 == mh2 - MZ2 == 4 * kappa * Nst)
            mu_lin = MU_LIN
            mh2b, mpmb, MZ2b, MW2b, ms, Ns, _, _ = masses(lamstar, {1: mu_lin, 2: kappa})
            dfct = (mpmb[0] - MW2b) - (mh2b - MZ2b)
            GA.check("linear term: defect 2 mu (m*/N*)^2", dfct == 2 * mu_lin * (ms / Ns) ** 2)
            GA.check("|defect| < 2 |mu|", abs(dfct) < 2 * abs(mu_lin) and dfct * mu_lin > 0)
    return True


def check_prediction_bracket_from_record_inputs():
    """With W = kappa N^2 and v >> H: m_pm^2 = M_W^2 + m_h^2 - M_Z^2 exactly (defect zero), so with
    M_W^2 = cos^2(theta_W) M_Z^2 at tree level: m_pm^2 = m_h^2 - sin^2(theta_W) M_Z^2. With the stored M_Z and
    sin^2 theta_W at M_Z and m_h in a bracket [125, 125.4] GeV containing the stored measured value 125.20 GeV,
    m_pm lies in [116, 119] GeV, below the top mass minus the bottom mass (stored record values)."""
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    MZ = quantity("quantity.z-boson-mass")
    s2w = quantity("quantity.weak-mixing-angle-mz")
    mt = quantity("quantity.top-quark-mass")
    mb = quantity("quantity.bottom-quark-mass")
    mh = quantity("quantity.higgs-boson-mass")
    GA.check("stored m_h = 125.20 GeV inside the bracket [125, 125.4] GeV", MH_LO < mh < MH_HI and mh * 5 == 626)
    lo = MH_LO ** 2 - s2w * MZ ** 2
    hi = MH_HI ** 2 - s2w * MZ ** 2
    GA.check("m_pm^2 bracket [13702, 13803] GeV^2 (m_pm in [117.06, 117.48] GeV)",
             13702 < lo < 13703 and 13802 < hi < 13803)
    GA.check("m_pm^2 inside [116^2, 119^2] GeV^2", 116 ** 2 < lo and hi < 119 ** 2)
    GA.check("t -> b H+ kinematically open: (m_t - m_b)^2 in [28355, 28356]", hi < (mt - mb) ** 2
             and 28355 < (mt - mb) ** 2 < 28356)
    GA.check("and above the LEP pair-production reach", lo > LEP_REACH ** 2)
    return True


def check_moment_map_invariant_breaks_the_equality():
    """The equality of the two shifts is special to functions of N alone: adding the invariant kappa m^2 of the
    hypercharge moment map (no dimensionful constant either) to the D-term action, with the level re-solved
    for criticality, gives a nonzero defect, -17/10 at lambda* = 1/2 and -164/45 at lambda* = 3 for
    kappa = 1/5, and the charged pair stays degenerate."""
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("synthesis.rung-field-on-the-lift-locus")
    km = F(1, 5)
    for lamstar, expected in ((F(1, 2), F(-17, 10)), (F(3), F(-164, 45))):
        mh2, mpm, MZ2, MW2, mstar, Nst, Wp, Wpp = masses(lamstar, {}, km)
        mp = mpm.pop()
        GA.check("charged pair degenerate with kappa m^2", all(x == mp for x in mpm))
        dfct = (mp - MW2) - (mh2 - MZ2)
        GA.check("kappa m^2 defect as tabulated", dfct == expected)
    return True
