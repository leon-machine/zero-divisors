"""Weyl curvature of the diagonal Kasner fields with sum p = 1: exact checks.

Field g = -dt^2 + t^(2 p1) dx^2 + t^(2 p2) dy^2 + t^(2 p3) dz^2 with p3 = 1 - p1 - p2 (any matter). A small
exact engine handles diagonal metrics whose entries are monomials c t^e with rational e: Christoffel symbols,
the Riemann tensor (R^r_{s m n} = d_m G^r_{n s} - d_n G^r_{m s} + G^r_{m l} G^l_{n s} - G^r_{n l} G^l_{m s}),
Ricci, R and the Weyl components C_{abab} in the coordinate basis, divided by g_aa g_bb (the mixed components C_{ab}^{ab}).
The elimination uses GA's rational functions in one variable (Sylvester determinant).
Exact arithmetic only (Fractions); no transcendental number is evaluated.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise
import gtg

# ---------------------------------------------------------------- Laurent "polynomials" in t, rational exponents
def lp(c, e):
    return {F(e): F(c)} if c != 0 else {}


def ladd(*xs):
    out = {}
    for x in xs:
        for e, c in x.items():
            out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c != 0}


def lmul(x, y):
    out = {}
    for e1, c1 in x.items():
        for e2, c2 in y.items():
            out[e1 + e2] = out.get(e1 + e2, F(0)) + c1 * c2
    return {e: c for e, c in out.items() if c != 0}


def lscal(s, x):
    return {e: s * c for e, c in x.items() if s * c != 0}


def ld(x):
    return {e - 1: c * e for e, c in x.items() if c * e != 0}


def linv_monomial(x):
    assert len(x) == 1
    (e, c), = x.items()
    return {-e: F(1) / c}


def curvature(diag):
    """diag: list of 4 monomials g_mumu(t). Returns (Ricci dict, scalar R, Ric.Ric) for a diagonal metric
    depending on t = coordinate 0 only."""
    n = len(diag)
    ginv = [linv_monomial(g) for g in diag]
    dg = [ld(g) for g in diag]

    def dgc(lam, mu, nu):  # partial_lam g_{mu nu}, diagonal metric, t-dependence only
        if lam != 0 or mu != nu:
            return {}
        return dg[mu]
    Gam = {}
    for lam in range(n):
        for mu in range(n):
            for nu in range(n):
                s = ladd(dgc(mu, lam, nu), dgc(nu, lam, mu), lscal(-1, dgc(lam, mu, nu)))
                Gam[(lam, mu, nu)] = lscal(F(1, 2), lmul(ginv[lam], s))

    def dGam(d, key):
        return ld(Gam[key]) if d == 0 else {}
    Ric = {}
    for s_ in range(n):
        for nu in range(n):
            acc = {}
            for r in range(n):
                acc = ladd(acc, dGam(r, (r, nu, s_)), lscal(-1, dGam(nu, (r, r, s_))))
                for l in range(n):
                    acc = ladd(acc, lmul(Gam[(r, r, l)], Gam[(l, nu, s_)]),
                               lscal(-1, lmul(Gam[(r, nu, l)], Gam[(l, r, s_)])))
            Ric[(s_, nu)] = acc
    R = ladd(*[lmul(ginv[m], Ric[(m, m)]) for m in range(n)])
    RR = ladd(*[lmul(lmul(ginv[m], ginv[m]), lmul(Ric[(m, m)], Ric[(m, m)])) for m in range(n)])
    offdiag_zero = all(Ric[(a, b)] == {} for a in range(n) for b in range(n) if a != b)
    return Ric, R, RR, offdiag_zero




def riemann_and_weyl(diag):
    """Returns ({(a, b): C_abab / (g_aa g_bb)}, R, Ricci) as Laurent dicts for a diagonal metric depending on t
    only; C_abab / (g_aa g_bb) is the orthonormal-frame component."""
    n = len(diag)
    ginv = [linv_monomial(g) for g in diag]
    dg = [ld(g) for g in diag]

    def dgc(lam, mu, nu):
        if lam != 0 or mu != nu:
            return {}
        return dg[mu]
    Gam = {}
    for lam in range(n):
        for mu in range(n):
            for nu in range(n):
                s = ladd(dgc(mu, lam, nu), dgc(nu, lam, mu), lscal(-1, dgc(lam, mu, nu)))
                Gam[(lam, mu, nu)] = lscal(F(1, 2), lmul(ginv[lam], s))

    def dGam(d, key):
        return ld(Gam[key]) if d == 0 else {}

    def riem_up(r, s_, m, nn):
        acc = ladd(dGam(m, (r, nn, s_)), lscal(-1, dGam(nn, (r, m, s_))))
        for l in range(n):
            acc = ladd(acc, lmul(Gam[(r, m, l)], Gam[(l, nn, s_)]), lscal(-1, lmul(Gam[(r, nn, l)], Gam[(l, m, s_)])))
        return acc
    Ric = {}
    for s_ in range(n):
        for nu in range(n):
            Ric[(s_, nu)] = ladd(*[riem_up(r, s_, r, nu) for r in range(n)])
    R = ladd(*[lmul(ginv[m], Ric[(m, m)]) for m in range(n)])
    C = {}
    for a in range(n):
        for b in range(a + 1, n):
            Rabab = lmul(diag[a], riem_up(a, b, a, b))
            # C_abab = R_abab - (1/2)(g_aa R_bb + g_bb R_aa) + (R/6) g_aa g_bb   (a != b, diagonal metric)
            c = ladd(Rabab, lscal(F(-1, 2), ladd(lmul(diag[a], Ric[(b, b)]), lmul(diag[b], Ric[(a, a)]))),
                     lscal(F(1, 6), lmul(R, lmul(diag[a], diag[b]))))
            C[(a, b)] = lmul(c, lmul(linv_monomial(diag[a]), linv_monomial(diag[b])))
    return C, R, Ric


def kasner(p1, p2):
    p3 = 1 - p1 - p2
    return [lp(-1, 0), lp(1, 2 * p1), lp(1, 2 * p2), lp(1, 2 * p3)]


def E1(p1, p2):
    return p1 * p1 - 2 * p1 * p2 - p1 - 2 * p2 * p2 + 2 * p2


def E2(p1, p2):
    return 2 * p1 * p1 + 2 * p1 * p2 - 2 * p1 - p2 * p2 + p2


SAMPLES = ((F(1, 3), F(1, 3)), (F(0), F(0)), (F(0), F(1)), (F(1), F(0)), (F(-1, 3), F(2, 3)),
           (F(1, 2), F(1, 2)), (F(2, 7), F(3, 7)), (F(-1, 5), F(1, 2)), (F(3, 4), F(-1, 8)))
WEYL_FLAT = {(F(1, 3), F(1, 3)), (F(0), F(0)), (F(0), F(1)), (F(1), F(0))}


def check_kasner_weyl_components_match_the_two_conics():
    """Engine values (mixed components C_{ab}^{ab}): t^2 C_{01}^{01} = E1/3, t^2 C_{02}^{02} = -E2/3, and generally
    t^2 C_{0i}^{0i} = p_i^2 - p_i + (1 - S)/3, S = sum p^2; C_{jk}^{jk} = C_{0i}^{0i}; every component a pure t^-2
    term; zero exactly at the four listed points among the samples; Einstein tensor G_00 = G_ii/g_ii = (1 - S)/(2t^2)
    (a stiff source P = rho)."""
    premise("synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching")
    ok = True
    for (p1, p2) in SAMPLES:
        C, R, Ric = riemann_and_weyl(kasner(p1, p2))
        ok &= C[(0, 1)] == lp(F(1, 3) * E1(p1, p2), -2) and C[(0, 2)] == lp(F(-1, 3) * E2(p1, p2), -2)
        ok &= C[(2, 3)] == C[(0, 1)] and C[(1, 3)] == C[(0, 2)] and C[(1, 2)] == C[(0, 3)]
        ok &= ladd(C[(0, 1)], C[(0, 2)], C[(0, 3)]) == {}           # electric part traceless
        ok &= all(set(v.keys()) <= {F(-2)} for v in C.values())
        flat_weyl = all(v == {} for v in C.values())
        ok &= flat_weyl == ((p1, p2) in WEYL_FLAT)
        p3 = 1 - p1 - p2
        S = p1 * p1 + p2 * p2 + p3 * p3
        # mixed components C_{0i}^{0i} = (p_i^2 - p_i + (1 - S)/3) t^-2 (the eigenvalues of the Weyl map)
        for i, pi in ((1, p1), (2, p2), (3, p3)):
            ok &= C[(0, i)] == lp(pi * pi - pi + F(1, 3) * (1 - S), -2)
        # Einstein tensor: G_00 = G_ii / g_ii = (1 - S)/(2 t^2): a stiff source P = rho
        g = kasner(p1, p2)
        G00 = ladd(Ric[(0, 0)], lscal(F(1, 2), R))
        ok &= G00 == lp(F(1, 2) * (1 - S), -2)
        for i in (1, 2, 3):
            Gii = ladd(Ric[(i, i)], lscal(F(-1, 2), lmul(R, g[i])))
            ok &= lmul(Gii, linv_monomial(g[i])) == G00
        if (p1, p2) == (F(1, 3), F(1, 3)):
            ok &= R == lp(F(-2, 3), -2)                       # stiff-fluid field, R t^2 = -2/3
        if (p1, p2) in ((F(0), F(0)), (F(0), F(1)), (F(1), F(0))):
            ok &= R == {} and all(v == {} for v in Ric.values())  # Milne points: flat
        ok &= p3 == 1 - p1 - p2
    GA.check("Kasner plane: Weyl components are E1/3, -E2/3 times t^-2; zero exactly at the Milne points and "
             "(1/3, 1/3, 1/3) among the samples", ok)
    return ok


def poly_in_p1(coeffs):
    return GA.RF(GA.ptrim([F(c) for c in coeffs]))


def check_the_two_conics_meet_exactly_at_four_points():
    """Resultant in p2 of E1 and E2 is -9 p1^2 (p1 - 1)(3 p1 - 1); the fibres give exactly (0,0), (0,1), (1,0),
    (1/3,1/3), so by Bezout these are all the Weyl-flat points of the Kasner plane."""
    premise("synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching")
    ok = True
    # E1 = -2 p2^2 + (2 - 2 p1) p2 + (p1^2 - p1);  E2 = -p2^2 + (2 p1 + 1) p2 + (2 p1^2 - 2 p1)
    a2, a1, a0 = poly_in_p1([-2]), poly_in_p1([2, -2]), poly_in_p1([0, -1, 1])
    b2, b1, b0 = poly_in_p1([-1]), poly_in_p1([1, 2]), poly_in_p1([0, -2, 2])
    Z = GA.RF0
    S = [[a2, a1, a0, Z], [Z, a2, a1, a0], [b2, b1, b0, Z], [Z, b2, b1, b0]]
    res = GA.rf_mat_det(S)
    target = poly_in_p1([0, 0, -9, 36, -27])           # -9 p1^2 (p1 - 1)(3 p1 - 1)
    ok &= res.eqrf(target)
    pts = set()
    for r in (F(1), F(1, 3)):
        # solve E1(r, p2) = 0 and E2(r, p2) = 0 for p2: common roots of two quadratics, by gcd
        e1 = GA.ptrim([r * r - r, 2 - 2 * r, F(-2)])
        e2 = GA.ptrim([2 * r * r - 2 * r, 2 * r + 1, F(-1)])
        g = GA.pgcd(e1, e2)
        ok &= len(g) == 2                                   # one common root (linear gcd) in each of these fibres
        if len(g) == 2:
            pts.add((r, -g[0] / g[1]))
    # p1 = 0: E1 = -2 p2 (p2 - 1), E2 = -p2 (p2 - 1): gcd is quadratic
    g0 = GA.pgcd(GA.ptrim([F(0), F(2), F(-2)]), GA.ptrim([F(0), F(1), F(-1)]))
    ok &= len(g0) == 3
    pts |= {(F(0), F(0)), (F(0), F(1))}
    ok &= all(E1(*p) == 0 and E2(*p) == 0 for p in pts)
    ok &= pts == WEYL_FLAT
    GA.check("the Weyl conics meet exactly at (0,0), (0,1), (1,0), (1/3,1/3): resultant -9 p1^2 (p1 - 1)(3 p1 - 1)", ok)
    return ok


def check_weyl_flat_points_in_cosmic_and_conformal_time():
    """Isotropic point: the engine finds g = t^(2/3) x (flat bracket); the bracket's cometric entry -t^(2/3) has
    order 2/3 in cosmic time (not tame), while in conformal time eta = (3/2) t^(2/3) the bracket is -d eta^2 + delta,
    i.e. -dt'^2/t' in t' = eta^2/4 (the radical-normal wall). Milne point (0,0,1): flat; the metric entry t^2 vanishes
    at order 2 while the cometric entry t^-2 has a pole (the opposite of a tame wall). Lambda_i = 0 forces
    p_i^2 - p_i equal for all i: on the plane only the four points (enumerated over the r-ansatz)."""
    premise("dark-energy.imported-walls-sphere-theorem")
    premise("synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching")
    ok = True
    p = F(1, 3)
    full = kasner(p, p)
    bracket = [lmul(gi, lp(1, -2 * p)) for gi in full]
    Cb, Rb, Ricb = riemann_and_weyl(bracket)
    ok &= Rb == {} and all(v == {} for v in Ricb.values()) and all(v == {} for v in Cb.values())
    ok &= bracket[0] == lp(-1, -2 * p) and bracket[1] == lp(1, 0)
    cometric_tt = linv_monomial(bracket[0])
    ok &= list(cometric_tt.keys()) == [F(2, 3)]                       # order 2/3, not 1: not tame in t
    eta = lp(F(1) / (1 - p), 1 - p)
    ok &= eta == lp(F(3, 2), F(2, 3))
    deta = ld(eta)
    ok &= lmul(bracket[0], lmul(linv_monomial(deta), linv_monomial(deta))) == lp(-1, 0)   # -d eta^2
    # t' = eta^2/4: d eta/dt' = 2/eta, so -d eta^2 = -(4/eta^2) dt'^2 = -dt'^2/t'   (eta^2 = 4 t')
    tprime = lscal(F(1, 4), lmul(eta, eta))
    dtp_deta = lp(F(1, 2), 1)                                          # d t'/d eta = eta/2, as a monomial in eta
    ok &= lmul(lp(-1, 0), lmul(linv_monomial(dtp_deta), linv_monomial(dtp_deta))) == lp(-4, -2)
    ok &= lmul(lp(-4, -2), lp(F(1, 4), 2)) == lp(-1, 0)                # -(4/eta^2) * (eta^2/4) = -1: -dt'^2/t'
    ok &= tprime == lp(F(9, 16), F(4, 3))
    milne = kasner(F(0), F(0))
    Cm, Rm, Ricm = riemann_and_weyl(milne)
    ok &= Rm == {} and all(v == {} for v in Ricm.values()) and all(v == {} for v in Cm.values())
    ok &= milne[3] == lp(1, 2) and linv_monomial(milne[3]) == lp(1, -2)
    # the short route: lambda_i = 0 for all i iff p_i^2 - p_i equal; each p_i in {r, 1 - r}; with sum 1:
    sols = set()
    for n_r in (3, 2, 1):            # number of exponents equal to r (the rest equal 1 - r)
        # n_r r + (3 - n_r)(1 - r) = 1  =>  (2 n_r - 3) r = n_r - 2
        r = F(n_r - 2, 2 * n_r - 3)
        trip = tuple(sorted([r] * n_r + [1 - r] * (3 - n_r)))
        sols.add(trip)
    ok &= sols == {(F(1, 3), F(1, 3), F(1, 3)), (F(0), F(0), F(1))}      # up to permutation
    ok &= all(E1(t_[0], t_[1]) == 0 and E2(t_[0], t_[1]) == 0 for t_ in sols)
    GA.check("Weyl-flat Kasner points: isotropic point flat bracket, order 2/3 in cosmic time, radical-normal wall in "
             "t' = eta^2/4; Milne point flat with degenerate metric; short route gives exactly these points", ok)
    return ok


GTG_POINTS = ((F(2, 7), F(3, 7)), (F(-1, 3), F(2, 3)), (F(1, 2), F(1, 2)), (F(3, 4), F(-1, 8)), (F(1, 3), F(1, 3)),
              (F(1), F(0)), (F(0), F(0)))


def check_gtg_kasner_field_strength_and_weyl_map():
    """The proof's GTG computation for the synchronous gauge field hb^{-1}(e_t) = e0, hb^{-1}(e_i) = t^{p_i} e_i
    (derived metric -g_p): Omega solved from the torsion equation is -p_i t^{p_i - 1} B_i on e_{x^i} and 0 on
    e_t; calR(B_i) = p_i (p_i - 1) t^-2 B_i, calR(e_i ^ e_j) = p_i p_j t^-2 e_i ^ e_j; Ricci calR(e0) =
    (S - 1) t^-2 e0, calR(e_j) = 0; scalar (S - 1) t^-2; Weyl map W(B_i) = lambda_i B_i and W(I4 B_i) =
    lambda_i I4 B_i with t^2 lambda_1 = E1/3, t^2 lambda_2 = -E2/3, trace zero; zero exactly at the Weyl-flat
    points; field strength zero at the Milne points."""
    premise("synthesis.imported-gtg-dictionary")
    premise("synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching")
    ok = True
    sq = gtg.S13
    I4 = gtg.pseudoscalar(sq)
    for (p1, p2) in GTG_POINTS:
        p = (p1, p2, 1 - p1 - p2)
        S = sum(x * x for x in p)
        tau, given = gtg.kasner_field(p, 2)
        fld = gtg.Field(given.TH)                          # Omega from the torsion equation alone
        ok &= fld.torsion_free()
        B = [None] + [gtg.biv(0, i) for i in (1, 2, 3)]
        ok &= fld.Omega(0) == {}
        for i in (1, 2, 3):
            tp = given.TH[i][i].v                          # t^{p_i}
            ok &= GA.eq(fld.Omega(i), GA.scal(-p[i - 1] * tp / tau, B[i]))
            ok &= GA.eq(fld.omega(i), GA.scal(-p[i - 1] / tau, B[i]))
        Rc = fld.curvature()
        t2 = 1 / (tau * tau)
        for i in (1, 2, 3):
            ok &= GA.eq(Rc[(0, i)], GA.scal(p[i - 1] * (p[i - 1] - 1) * t2, B[i]))
            for j in range(i + 1, 4):
                ok &= GA.eq(Rc[(i, j)], GA.scal(p[i - 1] * p[j - 1] * t2, gtg.biv(i, j)))
        ok &= GA.eq(gtg.ricci(Rc, GA.gen(0)), GA.scal((S - 1) * t2, GA.gen(0)))
        ok &= all(gtg.ricci(Rc, GA.gen(j)) == {} for j in (1, 2, 3))
        ok &= gtg.ricci_scalar(Rc) == (S - 1) * t2
        ok &= GA.eq(gtg.einstein(Rc, GA.gen(0)), GA.scal(F(1, 2) * (S - 1) * t2, GA.gen(0)))
        W = gtg.weyl_op(Rc)
        lam = [(x * x - x + F(1, 3) * (1 - S)) * t2 for x in p]
        for i in (1, 2, 3):
            ok &= GA.eq(gtg.apply_op(W, B[i]), GA.scal(lam[i - 1], B[i]))
            dual = GA.mul(I4, B[i], sq)
            ok &= GA.eq(gtg.apply_op(W, dual), GA.scal(lam[i - 1], dual))
        ok &= lam[0] == F(1, 3) * E1(p1, p2) * t2 and lam[1] == F(-1, 3) * E2(p1, p2) * t2 and sum(lam) == 0
        ok &= all(v == {} for v in W.values()) == ((p1, p2) in WEYL_FLAT)
        if (p1, p2) in WEYL_FLAT and (p1, p2) != (F(1, 3), F(1, 3)):
            ok &= all(v == {} for v in Rc.values())        # Milne points: zero field strength
    # the isotropic bracket -t^(-2/3) dt^2 + delta: hb^{-1}(e_t) = t^(-1/3) e0, Omega = 0, zero field strength
    T = gtg.Jet.var(0, F(8), 4, 2)
    TH = [[F(0)] * 4 for _ in range(4)]
    TH[0][0] = T.pw(F(-1, 3), F(1, 2))
    for i in (1, 2, 3):
        TH[i][i] = F(1)
    br = gtg.Field(TH)
    ok &= all(br.Omega(mu) == {} for mu in range(4)) and all(v == {} for v in br.curvature().values())
    GA.check("Kasner plane in GTG: torsion-solved Omega, store-sign field strength, Ricci map and Weyl map "
             "with eigenvalues E1/3, -E2/3 on B_i and I4 B_i", ok)
    _tp_rv = (ok); assert _tp_rv is not False, "check_gtg_kasner_field_strength_and_weyl_map"; return _tp_rv
