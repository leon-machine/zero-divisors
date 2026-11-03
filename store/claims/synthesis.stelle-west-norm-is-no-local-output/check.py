"""The Stelle-West norm is no local output: exact checks.

Cl(2,4) with generators e0..e3 (the middle slot, store signature +,-,-,-) and e4, e5 with squares +1, -1;
n_inf = e4 + e5, n_0 = (e4 - e5)/2, so <n_0, n_inf> = 1 and both are null. The frozen point in its own
scale is I = n_inf + (Lambda/6) n_0, the canonical tractor X = n_0, and V_c = X - (3/Lambda) I.
eps(A1, ..., A6) is the coefficient of e0 e1 e2 e3 e4 e5 in A1 ^ ... ^ A6. A bivector-valued two-form F
has components F(a, b) = 1/2 F^{cd}_{ab} e_c ^ e_d; the soldering form is e(a) = e_a. The densities are
the coefficients of the four-forms, summed against eps^{abcd}:
  L1(V) = eps(I, V, F, F),  L3(V) = eps(I, V, e, e, F),  L5(V) = eps(I, V, e, e, e, e),
with nabla V = t e for V = t V_c (the frame scales with V).
(1) Kinematics: for every null X with <X, I> = sigma != 0 and Q(I) != 0, V = X/sigma - I/Q(I) has
    <V, I> = 0 and Q(V) Q(I) = -1; in the frozen point's scale V = V_c with tractor components
    (-3/Lambda, 0, 1/2), and I ^ V_c = n_inf ^ n_0 for every Lambda.
(2) The Euler identity: L1, L3, L5 are homogeneous of degrees 1, 3, 5 in (V, nabla V), and every density
    with V in two slots of eps vanishes, so the V-equation contracted with V is 1 c1 L1 + 3 c3 L3 + 5 c5 L5.
(3) Pointwise values on torsion-free Einstein blocks F = W + kappa (e ^ e), W any Weyl curvature:
    L1 = t (kappa^2 + |W|^2/24) lam5, L3 = kappa t^3 lam5, L5 = t^5 lam5 with lam5 = eps(I, V_c, e,e,e,e)
    = -24 != 0; the tangential components eps(I, e_a, F, F) and eps(I, e_a, e, e, F) vanish.
(4) Schwarzschild-de Sitter (lapse f = 1 - 2M/r - Lambda r^2/3, sectional curvatures from f): Einstein
    with Lambda, Lorentz block the Weyl part with |W|^2 = 48 M^2/r^6, L1 = -48 M^2/r^6 != 0 at every point,
    different at two radii; de Sitter has L1 = 0 for every t.
(6) The stored chart (n_0 = (e4 + e5)/2, n_inf = e4 - e5, plane-pair sum): lam = 6, the Schwarzschild-de
    Sitter value 12 M^2/r^6, the same ratio kappa^2 + |W|^2/24, and every density -1/4 of the other convention's.
(5) Couplings: with c1 = 0, kappa = -(5 c5/(3 c3)) t^2 solves the V-equation; with c1 != 0, for fixed
    (t, kappa) the V-equation at two radii of the Schwarzschild-de Sitter field differs by
    c1 t (|W|^2(r1) - |W|^2(r2))/24 lam5 != 0.
Exact arithmetic only (Fractions); fixed sample tables.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
ETA = (1, -1, -1, -1)
R4 = range(4)
FULL = (0, 1, 2, 3, 4, 5)
LAMBDAS = (F(3), F(-3, 2), F(1, 7))
SIGMAS = (F(1), F(5, 3), F(-2))
TS = (F(1), F(2), F(-3, 4))
KAPPAS = (F(0), F(1), F(2, 3), F(-5, 2))
SDS = [(F(1), F(3, 7), F(2)), (F(2, 5), F(-1, 2), F(3)), (F(1), F(3), F(1, 2))]
LAM5 = F(-24)
SDS_K = F(48)
COUPLINGS = [(F(2), F(-3)), (F(1, 2), F(5, 7))]
L_HOM = F(3)
TORSION_LEG = (0, 1, 2)
TRIPLES = ((F(1), F(0), F(0)), (F(2), F(-1, 3), F(5)), (F(0), F(1), F(1, 2)))
S_SAMPLES = (F(2), F(-1, 3), F(5, 2))
WRONG_KAPPA_SHIFT = F(1)
M_SDS = F(1)
C_TRIPLE = (F(1), F(2), F(-1))
RADII = (F(2), F(3))


def _m(*xs):
    out = xs[0]
    for y in xs[1:]:
        out = GA.mul(out, y, SQ)
    return out


def _grade(x, g):
    return {b: c for b, c in x.items() if len(b) == g}


def _deg(x):
    return max((len(b) for b in x), default=0)


def _wedge(*xs):
    out = xs[0]
    g = _deg(out)
    for y in xs[1:]:
        g += _deg(y)
        out = _grade(_m(out, y), g)
    return out


def _vec(cs):
    out = {}
    for i, c in enumerate(cs):
        if c:
            out = GA.add(out, GA.scal(F(c), GA.gen(i)))
    return out


def _ip(x, y):
    return GA.add(_m(x, y), _m(y, x)).get((), F(0)) / 2


NINF = _vec([0, 0, 0, 0, 1, 1])
N0 = _vec([0, 0, 0, 0, F(1, 2), F(-1, 2)])


def _frozen(L):
    return GA.add(NINF, GA.scal(L / 6, N0))


def _vc(L):
    return GA.sub(N0, GA.scal(3 / L, _frozen(L)))


def _c6(x):
    return x.get(FULL, F(0))


EPS4 = {(a, b, c, d): _wedge(GA.gen(a), GA.gen(b), GA.gen(c), GA.gen(d)).get((0, 1, 2, 3), F(0))
        for a in R4 for b in R4 for c in R4 for d in R4}
QUADS = [k for k, v in EPS4.items() if v]


def _zero_curv():
    return {(a, b, c, d): F(0) for a in R4 for b in R4 for c in R4 for d in R4}


def _const(k):
    """k (eta_ac eta_bd - eta_ad eta_bc): the e^e block with coefficient k."""
    return {(a, b, c, d): k * ((ETA[a] if a == c else 0) * (ETA[b] if b == d else 0)
                               - (ETA[a] if a == d else 0) * (ETA[b] if b == c else 0))
            for a in R4 for b in R4 for c in R4 for d in R4}


def _add(*Rs):
    return {k: sum(R[k] for R in Rs) for k in Rs[0]}


def _scale(c, R):
    return {k: c * v for k, v in R.items()}


def _ric(R):
    return [[sum(F(1, ETA[a]) * R[a, b, a, d] for a in R4) for d in R4] for b in R4]


def _scalar(M):
    return sum(F(1, ETA[a]) * M[a][a] for a in R4)


def _kn(h, k):
    return {(a, b, c, d): h[a][c] * k[b][d] + h[b][d] * k[a][c] - h[a][d] * k[b][c] - h[b][c] * k[a][d]
            for a in R4 for b in R4 for c in R4 for d in R4}


def _sym(rows):
    M = [[F(0)] * 4 for _ in R4]
    for (i, j, v) in rows:
        M[i][j] = M[j][i] = F(v)
    return M


ETAM = [[F(ETA[a]) if a == b else F(0) for b in R4] for a in R4]
H1 = _sym([(0, 0, 2), (0, 1, F(1, 3)), (1, 1, -1), (1, 2, F(5, 2)), (2, 3, 1), (3, 3, F(-7, 4)), (0, 3, 3)])
K1 = _sym([(0, 0, -1), (0, 2, F(2, 5)), (1, 1, 4), (1, 3, -2), (2, 2, F(1, 2)), (3, 3, 1), (2, 3, F(-3, 2))])
H2 = _sym([(0, 1, 1), (1, 1, F(3, 2)), (2, 2, -3), (0, 2, -1), (1, 3, F(4, 3)), (3, 3, 2)])


def _weyl_part(R):
    Ric = _ric(R)
    s = _scalar(Ric)
    P = [[(Ric[a][b] - s / 6 * ETAM[a][b]) / 2 for b in R4] for a in R4]
    PK = _kn(P, ETAM)
    return {k: R[k] - PK[k] for k in R}


def _sectional(s01, s02, s12, s23):
    R = _zero_curv()
    for (a, b), v in {(0, 1): s01, (0, 2): s02, (0, 3): s02, (1, 2): s12, (1, 3): s12, (2, 3): s23}.items():
        R[a, b, a, b] = R[b, a, b, a] = v
        R[a, b, b, a] = R[b, a, a, b] = -v
    return R


def _sds(M, L, r):
    """Curvature of the static field with lapse f = 1 - 2M/r - L r^2/3, orthonormal frame (t, r, th, ph):
    sectional curvatures f''/2, f'/(2r), -f'/(2r), (1 - f)/r^2."""
    f = 1 - 2 * M / r - L * r * r / 3
    f1 = 2 * M / (r * r) - 2 * L * r / 3
    f2 = -4 * M / (r * r * r) - 2 * L / 3
    return _sectional(f2 / 2, f1 / (2 * r), -f1 / (2 * r), (1 - f) / (r * r))


WEYLS = [_weyl_part(_add(_kn(H1, K1), _kn(H2, H2))), _weyl_part(_kn(H1, H2)), _weyl_part(_kn(K1, H1)),
         _sectional(F(-2), F(1), F(-1), F(2))]


def _norm2(W):
    return sum(F(1, ETA[a] * ETA[b] * ETA[c] * ETA[d]) * W[a, b, c, d] ** 2
               for a in R4 for b in R4 for c in R4 for d in R4)


def _fb(R):
    out = {}
    for a in R4:
        for b in R4:
            x = {}
            for c in R4:
                for d in R4:
                    co = F(1, 2) * F(1, ETA[c] * ETA[d]) * R[c, d, a, b]
                    if c != d and co:
                        x = GA.add(x, GA.scal(co, _wedge(GA.gen(c), GA.gen(d))))
            out[a, b] = x
    return out


def _sw(I, U, E):
    return sum(EPS4[q] * _c6(_wedge(I, U, *E(q))) for q in QUADS)


def L1(I, V, Fb):
    return _sw(I, V, lambda q: (Fb[q[0], q[1]], Fb[q[2], q[3]]))


def L3(I, V, De, Fb):
    return _sw(I, V, lambda q: (GA.scal(De, GA.gen(q[0])), GA.scal(De, GA.gen(q[1])), Fb[q[2], q[3]]))


def L5(I, V, De):
    return _sw(I, V, lambda q: tuple(GA.scal(De, GA.gen(i)) for i in q))


def check_norm_of_the_stelle_west_vector_is_fixed_by_the_frozen_point():
    premise("dark-energy.stelle-west-vector-frozen-point")
    premise("dark-energy.imported-frozen-point-geometry")
    GA.check("n_0, n_inf null with <n_0, n_inf> = 1",
             _ip(N0, N0) == 0 and _ip(NINF, NINF) == 0 and _ip(N0, NINF) == 1)
    for L in LAMBDAS:
        I = _frozen(L)
        GA.check("Q(I) = Lambda/3", _ip(I, I) == L / 3)
        for s in SIGMAS:
            X = GA.scal(s, N0)
            GA.check("X null with <X, I> = sigma", _ip(X, X) == 0 and _ip(X, I) == s)
            V = GA.sub(GA.scal(1 / s, X), GA.scal(1 / _ip(I, I), I))
            GA.check("<V, I> = 0", _ip(V, I) == 0)
            GA.check("Q(V) Q(I) = -1", _ip(V, V) * _ip(I, I) == -1)
            GA.check("Q(V) = -3/Lambda", _ip(V, V) == -3 / L)
        Vc = _vc(L)
        GA.check("V_c = -(3/Lambda) n_inf + (1/2) n_0, components (-3/Lambda, 0, 1/2)",
                 GA.eq(Vc, GA.add(GA.scal(-3 / L, NINF), GA.scal(F(1, 2), N0))))
        GA.check("I ^ V_c = n_inf ^ n_0 for every Lambda", GA.eq(_wedge(I, Vc), _wedge(NINF, N0)))
        GA.check("a non-null X would break the identity",
                 _ip(GA.sub(GA.add(N0, GA.gen(1)), GA.scal(1 / _ip(I, I), I)),
                     GA.sub(GA.add(N0, GA.gen(1)), GA.scal(1 / _ip(I, I), I))) * _ip(I, I) != -1)


def check_released_norm_equation_is_the_euler_identity():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    I = _frozen(L_HOM)
    Vc = _vc(L_HOM)
    gen_R = _add(_kn(H1, K1), _kn(H2, H2))
    Fb = _fb(gen_R)
    # a general reduced field strength with a translational leg (torsion), to test homogeneity off the
    # torsion-free sector as well
    p, q, k = TORSION_LEG
    Ft = dict(Fb)
    Ft[p, q] = GA.add(Fb[p, q], _wedge(GA.gen(k), Vc))
    Ft[q, p] = GA.neg(Ft[p, q])
    for t in TS:
        V = GA.scal(t, Vc)
        for Fx in (Fb, Ft):
            GA.check("L1 homogeneous of degree 1", L1(I, V, Fx) == t * L1(I, Vc, Fx))
            GA.check("L3 homogeneous of degree 3", L3(I, V, t, Fx) == t ** 3 * L3(I, Vc, 1, Fx))
        GA.check("L5 homogeneous of degree 5", L5(I, V, t) == t ** 5 * L5(I, Vc, 1))
    # every term of V . dL/d(nabla V) carries V in two slots of eps, hence vanishes
    GA.check("eps(I, V, V, e, e, F) = 0", _sw(I, Vc, lambda q: (Vc, GA.gen(q[0]), Ft[q[2], q[3]])) == 0
             and all(_c6(_wedge(I, Vc, Vc, GA.gen(a), Ft[c, d])) == 0 for a in R4 for c in R4 for d in R4))
    GA.check("eps(I, V, V, e, e, e) = 0",
             all(_c6(_wedge(I, Vc, Vc, GA.gen(a), GA.gen(b), GA.gen(c))) == 0
                 for a in R4 for b in R4 for c in R4))
    GA.check("translational legs e ^ V drop out of L1 and L3 (V would fill two slots)",
             L1(I, Vc, Ft) == L1(I, Vc, Fb) and L3(I, Vc, 1, Ft) == L3(I, Vc, 1, Fb))
    GA.check("the homogeneity samples are not vacuous", L1(I, Vc, Fb) != 0 and L3(I, Vc, 1, Fb) != 0)
    # the V-equation contracted with V: d/ds of the Lagrangian along V -> sV at s = 1, degrees 1, 3, 5
    for (c1, c3, c5) in TRIPLES:
        lag = lambda s: c1 * L1(I, GA.scal(s, Vc), Fb) + c3 * L3(I, GA.scal(s, Vc), s, Fb) + c5 * L5(I, GA.scal(s, Vc), s)
        euler = 1 * c1 * L1(I, Vc, Fb) + 3 * c3 * L3(I, Vc, 1, Fb) + 5 * c5 * L5(I, Vc, 1)
        # the Lagrangian is an odd polynomial of degree 5 in s; recover its derivative at 1 exactly
        a1 = c1 * L1(I, Vc, Fb)
        a3 = c3 * L3(I, Vc, 1, Fb)
        a5 = c5 * L5(I, Vc, 1)
        GA.check("Lagrangian along V -> sV is a1 s + a3 s^3 + a5 s^5",
                 all(lag(s) == a1 * s + a3 * s ** 3 + a5 * s ** 5 for s in S_SAMPLES))
        GA.check("V-equation along V = 1 c1 L1 + 3 c3 L3 + 5 c5 L5", a1 + 3 * a3 + 5 * a5 == euler)


def check_pointwise_values_on_torsion_free_einstein_blocks():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    for L in LAMBDAS[:2]:
        I = _frozen(L)
        Vc = _vc(L)
        GA.check("lam5 = eps(I, V_c, e, e, e, e) = -24", L5(I, Vc, 1) == LAM5)
        for W in WEYLS:
            GA.check("W is Ricci-free", all(x == 0 for row in _ric(W) for x in row))
            GA.check("W is nonzero", any(W.values()))
            for kap in KAPPAS:
                Fb = _fb(_add(W, _const(kap)))
                for t in TS:
                    V = GA.scal(t, Vc)
                    GA.check("L1 = t (kappa^2 + |W|^2/24) lam5",
                             L1(I, V, Fb) == t * (kap * kap + _norm2(W) / 24) * LAM5)
                    GA.check("L3 = kappa t^3 lam5 (the Weyl part drops out)", L3(I, V, t, Fb) == kap * t ** 3 * LAM5)
                    GA.check("L5 = t^5 lam5", L5(I, V, t) == t ** 5 * LAM5)
                GA.check("tangential components vanish on torsion-free blocks",
                         all(L1(I, GA.gen(a), Fb) == 0 and L3(I, GA.gen(a), 1, Fb) == 0 for a in R4))
        GA.check("a Weyl curvature with |W|^2 != 0 occurs among the samples",
                 any(_norm2(W) != 0 for W in WEYLS))


def check_schwarzschild_de_sitter_is_excluded_and_de_sitter_norm_is_free():
    premise("singularity.non-removability-invariant-argument")
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    for (M, L, r) in SDS:
        R = _sds(M, L, r)
        GA.check("the static field is Einstein: Ric = Lambda eta",
                 all(_ric(R)[a][b] == (L * ETA[a] if a == b else 0) for a in R4 for b in R4))
        W = _add(R, _const(-L / 3))
        GA.check("Lorentz block of the canonical pair is the Weyl part", all(x == 0 for row in _ric(W) for x in row))
        GA.check("|W|^2 = 48 M^2/r^6", _norm2(W) == SDS_K * M * M / r ** 6)
        I = _frozen(L)
        val = L1(I, _vc(L), _fb(W))
        GA.check("released-norm equation of the bare functional: L1 = -48 M^2/r^6 != 0",
                 val == -SDS_K * M * M / r ** 6 and val != 0)
        Wr = _add(_sds(M, L, 2 * r), _const(-L / 3))
        GA.check("L1 differs at r and 2r (not constant)", L1(I, _vc(L), _fb(Wr)) != val)
        cov = [L1(I, GA.gen(a), _fb(W)) for a in R4] + [val]
        GA.check("the bare released equation is a covector on I-perp fixed by the connection: zero on e_a, "
                 "nonzero on V_c, so no V in I-perp is stationary", cov[:4] == [0] * 4 and cov[4] != 0)
    for L in LAMBDAS[:2]:
        I = _frozen(L)
        Fb = _fb(_zero_curv())
        GA.check("de Sitter: L1 = 0 for every norm", all(L1(I, GA.scal(t, _vc(L)), Fb) == 0 for t in TS))
        GA.check("Q(t V_c) = -3/Lambda_t with Lambda_t = Lambda/t^2 the constant of the frame t e",
                 all(_ip(GA.scal(t, _vc(L)), GA.scal(t, _vc(L))) * (L / (t * t)) == -3 for t in TS))
        GA.check("de Sitter with Lambda' != Lambda: block kappa != 0 gives L1 != 0",
                 L1(I, _vc(L), _fb(_const(F(1, 3)))) != 0)


def check_coupling_ratio_and_the_weyl_obstruction():
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("singularity.non-removability-invariant-argument")
    L = L_HOM
    I = _frozen(L)
    Vc = _vc(L)
    for (c3, c5) in COUPLINGS:
        for t in TS:
            kap = -F(5) * c5 * t * t / (3 * c3)
            Fb = _fb(_const(kap))
            eq = 3 * c3 * L3(I, GA.scal(t, Vc), t, Fb) + 5 * c5 * L5(I, GA.scal(t, Vc), t)
            GA.check("c1 = 0: kappa = -(5 c5/(3 c3)) t^2 solves the V-equation", eq == 0)
            Fb2 = _fb(_const(kap + WRONG_KAPPA_SHIFT))
            GA.check("and another kappa does not",
                     3 * c3 * L3(I, GA.scal(t, Vc), t, Fb2) + 5 * c5 * L5(I, GA.scal(t, Vc), t) != 0)
    M = M_SDS
    c1, c3, c5 = C_TRIPLE
    for t in TS:
        for kap in KAPPAS:
            vals = []
            for r in RADII:
                W = _add(_sds(M, L, r), _const(-L / 3))
                Fb = _fb(_add(W, _const(kap)))
                V = GA.scal(t, Vc)
                vals.append((c1 * L1(I, V, Fb) + 3 * c3 * L3(I, V, t, Fb) + 5 * c5 * L5(I, V, t), _norm2(W)))
            GA.check("c1 != 0: the V-equation at two radii differs by c1 t (|W|^2(r1) - |W|^2(r2))/24 lam5",
                     vals[0][0] - vals[1][0] == c1 * t * (vals[0][1] - vals[1][1]) / 24 * LAM5
                     and vals[0][0] != vals[1][0])


NINF_S = _vec([0, 0, 0, 0, 1, -1])
N0_S = _vec([0, 0, 0, 0, F(1, 2), F(1, 2)])
PLANES = [(a, b) for a in R4 for b in R4 if a < b]
STORE_LAM = F(6)
STORE_SDS = F(12)
CONVERSION = F(-1, 4)


def _plane_sum(I, U, E):
    tot = F(0)
    for (a, b) in PLANES:
        c, d = [x for x in R4 if x not in (a, b)]
        tot += EPS4[a, b, c, d] * _c6(_wedge(I, U, *E(a, b, c, d)))
    return tot


def check_store_chart_normalisation():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    premise("singularity.non-removability-invariant-argument")
    GA.check("stored chart: n_0, n_inf null with <n_0, n_inf> = 1",
             _ip(N0_S, N0_S) == 0 and _ip(NINF_S, NINF_S) == 0 and _ip(N0_S, NINF_S) == 1)
    for L in LAMBDAS[:2]:
        I = GA.add(NINF_S, GA.scal(L / 6, N0_S))
        Vc = GA.sub(N0_S, GA.scal(3 / L, I))
        GA.check("stored chart: I ^ V_c = n_inf ^ n_0 = minus the other chart's", GA.eq(_wedge(I, Vc), GA.neg(_wedge(NINF, N0))))
        lam = _plane_sum(I, Vc, lambda a, b, c, d: (GA.gen(a), GA.gen(b), GA.gen(c), GA.gen(d)))
        GA.check("stored chart: lam = eps(I, V_c, e, e, e, e) = 6", lam == STORE_LAM)
        GA.check("conversion: lam = -1/4 of the 24-ordering value in the other chart",
                 lam == CONVERSION * L5(_frozen(L), _vc(L), 1))
        for W in WEYLS:
            for kap in KAPPAS:
                Fb = _fb(_add(W, _const(kap)))
                v = _plane_sum(I, Vc, lambda a, b, c, d: (Fb[a, b], Fb[c, d]))
                GA.check("stored chart: L1/lam = kappa^2 + |W|^2/24", v == (kap * kap + _norm2(W) / 24) * lam)
                GA.check("conversion factor -1/4 for L1", v == CONVERSION * L1(_frozen(L), _vc(L), Fb))
        for (M, L2, r) in SDS:
            if L2 != L:
                continue
            W = _add(_sds(M, L, r), _const(-L / 3))
            Fb = _fb(W)
            GA.check("stored chart: Schwarzschild-de Sitter value 12 M^2/r^6",
                     _plane_sum(I, Vc, lambda a, b, c, d: (Fb[a, b], Fb[c, d])) == STORE_SDS * M * M / r ** 6)


if __name__ == "__main__":
    check_norm_of_the_stelle_west_vector_is_fixed_by_the_frozen_point()
    check_released_norm_equation_is_the_euler_identity()
    check_pointwise_values_on_torsion_free_einstein_blocks()
    check_schwarzschild_de_sitter_is_excluded_and_de_sitter_norm_is_free()
    check_coupling_ratio_and_the_weyl_obstruction()
    check_store_chart_normalisation()
    print("FAILURES:", GA.FAILURES)
