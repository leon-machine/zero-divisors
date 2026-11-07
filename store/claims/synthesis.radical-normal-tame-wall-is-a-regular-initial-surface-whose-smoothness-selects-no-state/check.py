"""Tame corank-one walls as initial surfaces for the descended fields: exact checks.

Aligned model walls in coordinates (t, x, y, z), wall t = 0, physical side t > 0: cometric
G = diag(-t^a, t^b, 1, 1), metric g = diag(-t^-a, t^-b, 1, 1); tame (first order, corank one) for
(a, b) = (1, 0) (radical dt, the conormal) and (0, 1) (radical dx, tangent). Curvature is computed by a small
exact engine for diagonal metrics whose entries are monomials c t^e with rational e (Christoffel symbols,
Ricci tensor, R and Ric.Ric); the expected values are derived by hand in the proof and compared exactly.
The Dirac part works in the spacetime algebra Cl(1,3) of GA.py in Hestenes form (unit imaginary I sigma3 on
the right); the conclusion uses only M^2 = -(k^2 + m^2), not the choice of unit imaginary.
The proof's GTG route (check_gtg_wall_field_strengths): each metric as the derived metric of a diagonal gauge field
on exact jets (lib/gtg.py), Omega solved from the torsion equation, store-sign field strength, Ricci and Einstein
maps; it reproduces the flat bracket, the scalars of the five pairs, the Friedmann exponents and the radiation
Ricci square.
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


def wall_metric(a, b):
    return [lp(-1, -a), lp(1, -b), lp(1, 0), lp(1, 0)]


# ---------------------------------------------------------------- check 1
def check_aligned_tame_walls_regular_iff_radical_normal():
    """Aligned tame walls: radical normal -> flat, finite proper time, Riemannian far side, and the metric is
    -dtau^2 + dx^2 in tau = 2 sqrt t; radical tangent -> R = (3/2) t^-2, signature (2,2) far side."""
    premise("dark-energy.imported-walls-sphere-theorem")
    premise("sheaf.metrics-residue-square-root-twist")
    premise("sheaf.tameness")  # the models' tameness: (T1) to (T3) of the definition, an assumes edge
    ok = True
    for (a, b) in ((1, 0), (0, 1), (2, 0), (0, 2), (1, 1)):
        # det G = -t^(a+b): tame (first-order corank-one) iff a + b = 1 and exactly one exponent is 1
        tame = (a + b == 1)
        radical_normal = (a == 1 and b == 0)
        # far side (t = -1): signs of the cometric diagonal
        far = (-((-1) ** a), (-1) ** b, 1, 1)
        npos = sum(1 for s in far if s > 0)
        # proper time to the wall along x = const: int_0^t s^(-a/2) ds finite iff a/2 < 1
        finite_tau = F(a, 2) < 1
        Ric, R, RR, od = curvature(wall_metric(a, b))
        expected_R = lp(F(b, 2) * (b + 2 - a), a - 2) if b * (b + 2 - a) != 0 else {}
        ok &= od and R == expected_R
        if (a, b) == (1, 0):
            ok &= tame and radical_normal and finite_tau and npos == 4 and R == {} and RR == {}
            ok &= all(v == {} for v in Ric.values())
        if (a, b) == (0, 1):
            ok &= tame and not radical_normal and finite_tau and npos == 2
            ok &= R == lp(F(3, 2), -2) and RR != {}
        if (a, b) in ((2, 0), (0, 2), (1, 1)):
            ok &= not tame
    # tau = 2 sqrt t: pull back g_tt dt^2 with t = tau^2/4, dt = (tau/2) dtau (monomials in tau)
    t_of_tau = lp(F(1, 4), 2)
    dt_dtau = ld(t_of_tau)
    g_tt = {e * 2: c * F(1, 4) ** e for e, c in lp(-1, -1).items()}   # -t^-1 written in tau
    pulled = lmul(g_tt, lmul(dt_dtau, dt_dtau))
    ok &= dt_dtau == lp(F(1, 2), 1) and pulled == lp(-1, 0)
    GA.check("aligned tame walls: radical normal -> flat half-spacetime -dtau^2 + dx^2, Riemannian far side; "
             "radical tangent -> R = (3/2) t^-2, signature (2,2) far side", ok)
    return ok


# ---------------------------------------------------------------- check 2
def friedmann_exponent(w):
    return F(2) / (3 * (1 + w))


def check_radiation_origin_is_conformally_a_radical_normal_wall():
    """FRW a = t^p: g = t^(2p) (-t^(-2p) dt^2 + dx^2); the bracket's cometric diag(-t^(2p), 1,1,1) is tame
    corank one iff 2p = 1; Friedmann gives p = 2/(3(1+w)), so only w = 1/3. Radiation FRW: R = 0,
    Ric.Ric = (3/4) t^-4 (curvature singular), Einstein tensor ratio gives w = 1/3."""
    ok = True
    tame_ws = []
    for w in (F(0), F(1, 3), F(1), F(-1, 3), F(1, 2)):
        p = friedmann_exponent(w)
        frw = [lp(-1, 0), lp(1, 2 * p), lp(1, 2 * p), lp(1, 2 * p)]
        bracket = [lp(-1, -2 * p), lp(1, 0), lp(1, 0), lp(1, 0)]
        conf = lp(1, 2 * p)
        ok &= all(lmul(conf, bk) == fr for bk, fr in zip(bracket, frw))
        # cometric of bracket: G^tt = -t^(2p); det order 2p; tame iff 2p == 1 (in the cosmic coordinate t)
        # every p < 1: conformal time eta = t^(1-p)/(1-p), d eta/dt = t^(-p); the bracket is -d eta^2 + delta,
        # which is g_{1,0} in t' = eta^2/4 (as in check 1): tameness is a property of the time coordinate
        if p < 1:
            eta = lp(F(1) / (1 - p), 1 - p)
            ok &= ld(eta) == lp(1, -p)
            ok &= lmul(bracket[0], lmul(linv_monomial(ld(eta)), linv_monomial(ld(eta)))) == lp(-1, 0)
        if 2 * p == 1:
            tame_ws.append(w)
        # Einstein tensor: check G_xx / (a^2 G_tt) = w (perfect fluid, comoving), from the engine
        Ric, R, RR, od = curvature(frw)
        Gtt = ladd(Ric[(0, 0)], lscal(F(1, 2), lmul(R, lp(1, 0))))           # G_tt = R_tt - (1/2) g_tt R, g_tt=-1
        Gxx = ladd(Ric[(1, 1)], lscal(F(-1, 2), lmul(R, frw[1])))
        ratio_ok = lmul(Gxx, lp(1, 0)) == lscal(w, lmul(Gtt, frw[1]))
        ok &= od and ratio_ok and Gtt != {}
    ok &= tame_ws == [F(1, 3)]
    p = friedmann_exponent(F(1, 3))
    Ric, R, RR, od = curvature([lp(-1, 0), lp(1, 2 * p), lp(1, 2 * p), lp(1, 2 * p)])
    ok &= p == F(1, 2) and R == {} and RR == lp(F(3, 4), -4)
    GA.check("among power-law FRW origins only radiation (w = 1/3, a = t^(1/2)) is conformal (factor t) to a "
             "tame corank-one wall, radical normal; there R = 0, Ric.Ric = (3/4) t^-4", ok)
    return ok


# ---------------------------------------------------------------- check 3
NMAX = 14


def cos_series_tau(om2):
    """cos(omega tau) as coefficients in tau, omega^2 = om2 rational."""
    c = [F(0)] * (NMAX + 1)
    fact = F(1)
    for n in range(0, NMAX + 1):
        if n > 0:
            fact *= n
        if n % 2 == 0:
            c[n] = F((-1) ** (n // 2)) * om2 ** (n // 2) / fact
    return c


def sinc_series_tau(om2):
    """sin(omega tau)/omega in tau."""
    c = [F(0)] * (NMAX + 1)
    fact = F(1)
    for n in range(0, NMAX + 1):
        if n > 0:
            fact *= n
        if n % 2 == 1:
            c[n] = F((-1) ** ((n - 1) // 2)) * om2 ** ((n - 1) // 2) / fact
    return c


def check_wall_smooth_scalar_solutions_are_a_lagrangian_half():
    """On a radical-normal wall, d_tau^2 = t d_t^2 + (1/2) d_t with indicial roots {0, 1/2}; the even
    tau-modes are power series in t (wall-smooth) and solve it exactly; the odd ones carry t^(1/2);
    the symplectic form vanishes on the even ones (conjugate momentum sqrt(t) d_t phi -> 0)."""
    premise("dark-energy.imported-walls-sphere-theorem")
    ok = True
    # indicial polynomial of t d_t^2 + (1/2) d_t on t^r: r(r-1) + r/2
    roots = [r for r in (F(0), F(1, 2), F(1), F(3, 2)) if r * (r - 1) + F(1, 2) * r == 0]
    ok &= roots == [F(0), F(1, 2)]
    for om2 in (F(1), F(13, 4), F(2) + F(9, 25)):     # omega^2 = k^2 + m^2
        cs = cos_series_tau(om2)
        ss = sinc_series_tau(om2)
        ok &= all(cs[n] == 0 for n in range(1, NMAX + 1, 2)) and all(ss[n] == 0 for n in range(0, NMAX + 1, 2))
        # even mode as a series in t: tau^(2j) = (4t)^j
        C = [cs[2 * j] * 4 ** j for j in range(NMAX // 2 + 1)]
        # apply L = t d_t^2 + (1/2) d_t to C (exact on truncation) and compare with -omega^2 C
        J = len(C)
        LC = [F(0)] * J
        for j in range(J):
            # t^j -> j(j-1) t^(j-1) + (j/2) t^(j-1)
            if j >= 1:
                LC[j - 1] += C[j] * (j * (j - 1) + F(j, 2))
        ok &= all(LC[j] == -om2 * C[j] for j in range(J - 1))
        # symplectic form at tau = 0: phi1 d_tau phi2 - phi2 d_tau phi1 (d_tau phi = coefficient of tau^1)
        def W(p1, p2):
            return p1[0] * p2[1] - p2[0] * p1[1]
        ok &= W(cs, cs) == 0 and W(cs, ss) == 1
        # momentum of a wall-smooth mode: sqrt(t) d_t C has lowest power t^(1/2) (vanishes at the wall)
        mom = ladd(*[lp(C[j] * j, F(j) - 1 + F(1, 2)) for j in range(1, J)])
        ok &= min(mom.keys()) == F(1, 2)
    GA.check("radical-normal wall: wall-smooth scalar modes are the tau-even ones, Lagrangian (symplectic form 0); "
             "the t^(1/2) branch is the other half", ok)
    return ok


# ---------------------------------------------------------------- check 4 (STA, Hestenes form)
SQ = (1, -1, -1, -1)
EVEN_BLADES = [(), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2, 3)]


def coords(x, blades):
    return [x.get(b, F(0)) for b in blades]


def check_wall_smooth_dirac_solutions_are_static_zero_modes():
    """Hestenes form on the tau side with plane-wave spatial factor: gamma0 phi' I sigma3 + (k.gamma) phi = m phi gamma0,
    so phi' = M(phi) with M(phi) = gamma0 (m phi gamma0 - (k.gamma) phi) (I sigma3)^-1. M^2 = -(|k|^2 + m^2):
    phi(tau) = cos(omega tau) phi0 + sin(omega tau)/omega M phi0, tau-even (wall-smooth) iff M phi0 = 0 iff phi0 = 0
    unless k = m = 0 (rank of M on the even subalgebra is 8, else 0)."""
    premise("dark-energy.imported-walls-sphere-theorem")
    g0 = GA.gen(0)
    I = {(0, 1, 2, 3): F(1)}
    sigma3 = GA.mul(GA.gen(3), g0, SQ)
    Is3 = GA.mul(I, sigma3, SQ)
    Is3_inv = GA.neg(Is3)
    ok = GA.eq(GA.mul(Is3, Is3, SQ), GA.sc(-1))
    ok &= GA.commutes(Is3, g0, SQ)
    samples = ((F(1), F(0), F(0), F(0)), (F(0), F(3, 2), F(-1), F(1, 3)),
               (F(2, 5), F(0), F(0), F(7, 3)), (F(-1), F(1), F(2), F(1, 2)), (F(0), F(0), F(0), F(0)))
    for (k1, k2, k3, m) in samples:
        kg = GA.add(GA.scal(k1, GA.gen(1)), GA.scal(k2, GA.gen(2)), GA.scal(k3, GA.gen(3)))

        def M(phi):
            inner = GA.sub(GA.scal(m, GA.mul(phi, g0, SQ)), GA.mul(kg, phi, SQ))
            return GA.mul(GA.mul(g0, inner, SQ), Is3_inv, SQ)
        omega2 = k1 * k1 + k2 * k2 + k3 * k3 + m * m
        cols = []
        for b in EVEN_BLADES:
            e = {b: F(1)}
            Me = M(e)
            ok &= all(len(bb) % 2 == 0 for bb in Me)                       # M preserves the even subalgebra
            ok &= GA.eq(M(Me), GA.scal(-omega2, e))                         # M^2 = -omega^2
            cols.append(coords(Me, EVEN_BLADES))
        rank = GA.rank_of_vectors(cols)
        ok &= rank == (8 if omega2 != 0 else 0)
    GA.check("radical-normal wall: a Dirac plane wave smooth across the wall must have M phi0 = 0, and M^2 = -(k^2+m^2), "
             "so it vanishes unless k = m = 0", ok)
    return ok


# ---------------------------------------------------------------- check 5
def check_radiation_field_smoothness_in_t_depends_on_the_conformal_weight():
    """Radiation field a = t^(1/2), conformal time tau = 2 sqrt t, a = tau/2. Massless scalar (R = 0, so minimal =
    conformal coupling): phi'' + (3/(2t)) phi' + (k^2/t) phi = 0 has indicial roots 0 and -1/2; phi = t^(-1/2) phi_flat,
    and the t-smooth solution is 2 sin(k tau)/tau (tau-ODD flat data), while 2 cos(k tau)/tau carries t^(-1/2).
    Massless Dirac: psi = a^(-3/2) psi_flat has t-exponents -3/4 + n/2, never integers: no nonzero t-smooth solution."""
    premise("dark-energy.imported-walls-sphere-theorem")
    ok = True
    roots = [r for r in (F(-1), F(-1, 2), F(0), F(1, 2), F(1)) if r * (r - 1) + F(3, 2) * r == 0]
    ok &= roots == [F(-1, 2), F(0)]
    for k2 in (F(1), F(9, 4), F(7, 3)):
        ss = sinc_series_tau(k2)          # sin(k tau)/k, odd powers of tau
        cs = cos_series_tau(k2)
        # u = sin(k tau)/(k tau) as a series in t: tau^(2j) = (4t)^j
        U = [ss[2 * j + 1] * 4 ** j for j in range(NMAX // 2)]
        J = len(U)
        # u'' + (3/(2t)) u' + (k^2/t) u: coefficient of t^(j-1) is (j(j-1) + 3j/2) U_j + k^2 U_(j-1)
        resid = [U[j] * (j * (j - 1) + F(3, 2) * j) + k2 * U[j - 1] for j in range(1, J)]
        ok &= all(r_ == 0 for r_ in resid) and U[0] == 1
        # cos(k tau)/tau = (1/2) t^(-1/2) (1 - ...): lowest exponent -1/2 (not smooth)
        cos_over_tau = ladd(*[lp(cs[2 * j] * 4 ** j * F(1, 2), F(j) - F(1, 2)) for j in range(NMAX // 2 + 1)])
        ok &= min(cos_over_tau.keys()) == F(-1, 2)
    # Dirac weight: a^(-3/2) = (tau/2)^(-3/2) = t^(-3/4); flat field tau^n = 2^n t^(n/2)
    exps = [F(-3, 4) + F(n, 2) for n in range(0, 2 * NMAX)]
    ok &= all(e.denominator != 1 for e in exps)
    # scalar weight a^(-1) = t^(-1/2): integer exponents exactly for odd n
    sexps = [F(-1, 2) + F(n, 2) for n in range(0, 2 * NMAX)]
    ok &= all((e.denominator == 1) == (n % 2 == 1) for n, e in enumerate(sexps))
    GA.check("radiation field: t-smooth scalar solutions are the tau-odd flat half (indicial 0, -1/2); "
             "no nonzero massless Dirac solution is t-smooth (exponents -3/4 + n/2)", ok)
    return ok


if __name__ == "__main__":
    check_aligned_tame_walls_regular_iff_radical_normal()
    check_radiation_origin_is_conformally_a_radical_normal_wall()
    check_wall_smooth_scalar_solutions_are_a_lagrangian_half()
    check_wall_smooth_dirac_solutions_are_static_zero_modes()
    print("FAILURES:", GA.FAILURES)


# ---------------------------------------------------------------- the proof's GTG route (lib/gtg.py)
WALL_PAIRS = ((1, 0), (0, 1), (2, 0), (0, 2), (1, 1))
FLRW_W = (F(0), F(1, 3), F(1), F(-1, 3), F(1, 2))


def _diag_field(N, As):
    TH = [[F(0)] * 4 for _ in range(4)]
    TH[0][0] = N
    for i in range(3):
        TH[i + 1][i + 1] = As[i]
    return gtg.Field(TH)


def check_gtg_wall_field_strengths():
    """Diagonal gauge fields hb^{-1}(e_t) = N e0, hb^{-1}(e_i) = A_i e_i on exact jets, Omega solved from the
    torsion equation: Omega(e_t) = 0, Omega(e_{x^i}) = -(dA_i/N) B_i; (i) the radical-normal bracket
    (N = t^(-1/2)) has zero field strength; (iii) for (a, b) the scalar is (b/2)(b + 2 - a) t^(a - 2),
    3/2 t^-2 for (0, 1); (iv) the field A_i = t^p has Einstein map G(e0) = -3p^2 t^-2 e0,
    G(e_j) = p(2 - 3p) t^-2 e_j, so P = w rho exactly at p = 2/(3(1 + w)); at p = 1/2 the scalar is 0 and the
    Ricci square 3/4 t^-4."""
    premise("dark-energy.imported-walls-sphere-theorem")
    ok = True
    t0 = F(16)
    T = gtg.Jet.var(0, t0, 4, 2)
    for (a, b) in WALL_PAIRS:
        N = T.pw(F(-a, 2), F(1, 4) ** a)          # t0^(-a/2), t0 = 16
        A1 = T.pw(F(-b, 2), F(1, 4) ** b)
        fld = _diag_field(N, [A1, F(1), F(1)])
        ok = ok and fld.Omega(0) == {} and GA.eq(fld.Omega(1), GA.scal(-A1.d(0).v / N.v, gtg.biv(0, 1)))
        Rc = fld.curvature()
        kappa = F(b, 4) * (b + 2 - a) * t0 ** (a - 2)
        ok = ok and GA.eq(Rc[(0, 1)], GA.scal(kappa, gtg.biv(0, 1)))
        ok = ok and gtg.ricci_scalar(Rc) == F(b, 2) * (b + 2 - a) * t0 ** (a - 2)
        if (a, b) == (1, 0):
            ok = ok and all(fld.Omega(m) == {} for m in range(4)) and all(v == {} for v in Rc.values())
        if (a, b) == (0, 1):
            ok = ok and gtg.ricci_scalar(Rc) == F(3, 2) / t0 ** 2
    for w in FLRW_W:
        p = 2 / (3 * (1 + w))
        tau, fld0 = gtg.kasner_field((p, p, p), 2)
        fld = gtg.Field(fld0.TH)
        Rc = fld.curvature()
        t2 = 1 / tau ** 2
        ok = ok and GA.eq(gtg.einstein(Rc, GA.gen(0)), GA.scal(-3 * p * p * t2, GA.gen(0)))
        G1 = gtg.einstein(Rc, GA.gen(1))
        ok = ok and GA.eq(G1, GA.scal(p * (2 - 3 * p) * t2, GA.gen(1)))
        rho, P = 3 * p * p * t2, p * (2 - 3 * p) * t2
        ok = ok and P == w * rho
        ok = ok and gtg.ricci_scalar(Rc) == 6 * p * (2 * p - 1) * t2
        if p == F(1, 2):
            sq_ = sum((gtg.vdot(gtg.ricci(Rc, gtg.er(m)), gtg.ricci(Rc, GA.gen(m)), gtg.S13) for m in range(4)), F(0))
            ok = ok and gtg.ricci_scalar(Rc) == 0 and sq_ == F(3, 4) * t2 * t2
    _tp_rv = (ok); assert _tp_rv is not False, "check_gtg_wall_field_strengths"; return _tp_rv
