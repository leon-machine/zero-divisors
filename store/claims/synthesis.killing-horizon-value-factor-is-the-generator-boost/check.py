"""The Killing flow's value factor on the canonical light-ray component at a Killing horizon: exact checks.

Setting: the spacetime algebra Cl(1,3), store signature (+,-,-,-), background frame e0..e3; on a Killing
horizon the physical generator direction k (null) and its dual null vector m (k.m = 1, in the plane of k and
the frame vector e0), Lambda(a) = a e0/(2 a0), F_K = (1/2) D ^ K the Killing bivector (Fact
synthesis.imported-gtg-dictionary (vi)), B_r the boost with B k B~ = r^2 k (r = e^{lam/2} rational).
(1) Shape of the Killing bivector on the horizon: the bivectors F with Y.(X.F) = 0 for all X, Y orthogonal to
    k (the vanishing of the horizon's second fundamental form, which the proof derives from the Killing
    antisymmetry) form exactly span{k^m, k^a, k^b} (a, b spanning the transverse plane), for two null
    directions; the surface-gravity condition K.F = kappa K fixes the k^m coefficient at -kappa. Controls:
    the transverse rotation a^b and m^a violate the condition.
(2) The canonical block: Lambda(m) k = 0 and Lambda(m)(k^m) = -Lambda(m), so for every generator
    G = c k^m + k^w (w transverse) Lambda(m) G = -c Lambda(m), hence Lambda(m) G^n = (-c)^n Lambda(m). On the
    group: Lambda(m) B_r N_s = r^{-1} Lambda(m) for the null rotations N_s = 1 + (1/2) k s (s transverse),
    whatever s. Control: a transverse rotation acts on Lambda(m) by a non-scalar factor (a helicity phase).
(3) The f(r) class in Painleve-Gullstrand gauge: the connection forms of the coframe dt, dr + beta dt, r dth,
    r sin th dph satisfy Cartan's first structure equations exactly at sample points; contracted with the
    Killing vector d/dt only the radial boost survives, with coefficient -beta beta' = f'/2
    (Q(beta) = 1 - f). At a horizon (f = 0, Q(beta) = 1) the t-line is a null generator with physical
    tangent k = e0 + beta e1 and (K.D)K = (f'/2) K: Schwarzschild kappa = 1/4M, de Sitter -H, and both
    horizons of a Schwarzschild-de Sitter field with rational horizon radii.
(4) Composition: the value factor r^{-1} on Lambda(m) with the transport of the affine parameter by r^2
    preserves the canonical kernel (the stored unitary dilation), for both signs of kappa.
Exact arithmetic only (Fractions, multivectors over Fractions).
"""
from fractions import Fraction as F
from functools import reduce
import GA
from tp_premise import premise

SQ = (1, -1, -1, -1)
E = [GA.gen(i) for i in range(4)]
BIV = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def _m(*xs):
    return reduce(lambda a, b: GA.mul(a, b, SQ), xs)


def _v(c0, c1, c2, c3):
    return GA.add(GA.scal(F(c0), E[0]), GA.scal(F(c1), E[1]), GA.scal(F(c2), E[2]), GA.scal(F(c3), E[3]))


def _dot(a, b):
    return GA.dot(a, b, SQ)


def _wedge(a, b):
    return GA.scal(F(1, 2), GA.sub(_m(a, b), _m(b, a)))


def _vdotB(x, B):
    """x . B for a vector x and a bivector B: (xB - Bx)/2."""
    return GA.scal(F(1, 2), GA.sub(_m(x, B), _m(B, x)))


def _sc(x):
    return x.get((), F(0))


def _lam(a):
    a0 = _sc(_m(a, E[0]))
    return GA.scal(1 / (2 * a0), _m(a, E[0]))


def _boost_in_plane(k, m, r):
    """B = cosh(lam/2) + sinh(lam/2) k^m with e^{lam/2} = r; (k^m)^2 = 1 when k.m = 1."""
    c, s = (r + 1 / r) / 2, (r - 1 / r) / 2
    return GA.add(GA.sc(c), GA.scal(s, _wedge(k, m)))


# two horizon frames: k null, m null dual in the plane of k and e0, (a, b) transverse
FRAMES = []
# k = e0 + e1, m = (e0 - e1)/2
FRAMES.append((_v(1, 1, 0, 0), _v(F(1, 2), F(-1, 2), 0, 0), _v(0, 0, 1, 0), _v(0, 0, 0, 1)))
# k = 5 e0 + 3 e1 + 4 e2 (null), m = (5 e0 - 3 e1 - 4 e2)/50 (k.m = 1), transverse a = (4 e1 - 3 e2)/5, b = e3
FRAMES.append((_v(5, 3, 4, 0), _v(F(5, 50), F(-3, 50), F(-4, 50), 0), _v(0, F(4, 5), F(-3, 5), 0), _v(0, 0, 0, 1)))


def _constraint_rows(k, perp):
    """Rows: for each pair (X, Y) of a basis of k-perp, the linear form F -> Y.(X.F) in the 6 coefficients."""
    rows = []
    for X in perp:
        for Y in perp:
            row = []
            for b in BIV:
                Fb = {b: F(1)}
                row.append(_sc(_m(Y, _vdotB(X, Fb))))
            rows.append(row)
    return rows


def _coeffs(B):
    return [B.get(b, F(0)) for b in BIV]


def check_killing_bivector_shape_on_the_horizon():
    premise("synthesis.imported-gtg-dictionary")
    for (k, m, a, b) in FRAMES:
        GA.check("k null", _sc(_m(k, k)) == 0)
        GA.check("m null", _sc(_m(m, m)) == 0)
        GA.check("k.m = 1", _dot(k, m) == 1)
        for t in (a, b):
            GA.check("transverse vector orthogonal to k and m", _sc(_m(t, k)) == 0 and _sc(_m(t, m)) == 0)
        GA.check("Q(a) = Q(b) = -1, a.b = 0", _sc(_m(a, a)) == -1 and _sc(_m(b, b)) == -1 and _sc(_m(a, b)) == 0)
        perp = [k, a, b]                       # a basis of the horizon's tangent space k-perp (k is null)
        rows = []
        for X in perp:
            for Y in perp:
                rows.append([_sc(_m(Y, _vdotB(X, {bl: F(1)}))) for bl in BIV])
        rank = GA.mat_rank(GA.frac_matrix(rows))
        GA.check("the condition Y.(X.F) = 0 on k-perp has rank 3: a 3-dimensional solution space", rank == 3)
        span = [_wedge(k, m), _wedge(k, a), _wedge(k, b)]
        GA.check("k^m, k^a, k^b are independent", GA.mat_rank(GA.frac_matrix([_coeffs(B) for B in span])) == 3)
        for B in span:
            for X in perp:
                for Y in perp:
                    GA.check("each of k^m, k^a, k^b satisfies the condition", _sc(_m(Y, _vdotB(X, B))) == 0)
                # equivalently X.F lies on the ray of k
                xb = _vdotB(X, B)
                GA.check("X.F is a multiple of k", GA.is_zero(_wedge(xb, k)))
        for bad in (_wedge(a, b), _wedge(m, a), _wedge(m, b)):
            viol = any(_sc(_m(Y, _vdotB(X, bad))) != 0 for X in perp for Y in perp)
            GA.check("control: transverse rotation and m^a, m^b violate the condition", viol)
        # surface gravity fixes the k^m coefficient: K.F = kappa K with K = phi k
        for kappa in (F(1, 4), F(-2, 7), F(3)):
            for wa, wb in ((F(0), F(0)), (F(2, 3), F(-5))):
                Fk = GA.add(GA.scal(-kappa, _wedge(k, m)), GA.scal(wa, _wedge(k, a)), GA.scal(wb, _wedge(k, b)))
                for phi in (F(1), F(7, 3)):
                    K = GA.scal(phi, k)
                    KdotF = _vdotB(K, Fk)
                    GA.check("K . F_K = kappa K with F_K = -kappa k^m + k^w", GA.eq(KdotF, GA.scal(kappa, K)))
                GA.check("control: +kappa k^m gives -kappa", GA.eq(_vdotB(k, GA.scal(kappa, _wedge(k, m))), GA.scal(-kappa, k)))
    return True


def check_canonical_block_is_the_generator_boost():
    premise("field-theory.second-quantisation")
    premise("synthesis.boost-evolution-on-generators-is-one-unitary-group")
    for (k, m, a, b) in FRAMES:
        Lm, Lk = _lam(m), _lam(k)
        N = _wedge(k, m)
        GA.check("Lambda(m) idempotent", GA.eq(_m(Lm, Lm), Lm))
        GA.check("Lambda(m) + Lambda(k) = 1 (e0 in the plane of k and m)", GA.eq(GA.add(Lm, Lk), GA.sc(1)))
        GA.check("Lambda(m) k = 0", GA.is_zero(_m(Lm, k)))
        GA.check("Lambda(m) (k^m) = -Lambda(m)", GA.eq(_m(Lm, N), GA.scal(F(-1), Lm)))
        GA.check("control: Lambda(m) m != 0", not GA.is_zero(_m(Lm, m)))
        for c in (F(1, 2), F(-3, 4), F(5)):
            for w in (a, GA.add(GA.scal(F(2), a), GA.scal(F(-1, 3), b)), b):
                G = GA.add(GA.scal(c, N), _wedge(k, w))
                GA.check("Lambda(m) G = -c Lambda(m), whatever w", GA.eq(_m(Lm, G), GA.scal(-c, Lm)))
                P = Lm
                for n in range(1, 5):
                    P = _m(P, G)
                    GA.check("Lambda(m) G^n = (-c)^n Lambda(m)", GA.eq(P, GA.scal((-c) ** n, Lm)))
                GA.check("control: G Lambda(m) leaves the canonical range (the k^w part feeds Lambda(k))", not GA.eq(_m(G, Lm), GA.scal(-c, Lm)))
        # the group: boosts times null rotations about k
        for r in (F(3, 2), F(1, 5), F(7, 3)):
            B = _boost_in_plane(k, m, r)
            GA.check("B k B~ = r^2 k", GA.eq(_m(B, k, GA.reverse(B)), GA.scal(r * r, k)))
            for s in (a, GA.add(GA.scal(F(-4), a), GA.scal(F(3, 2), b))):
                Nr = GA.add(GA.sc(1), GA.scal(F(1, 2), _m(k, s)))
                GA.check("N_s is a rotor", GA.eq(_m(Nr, GA.reverse(Nr)), GA.sc(1)))
                GA.check("N_s fixes k", GA.eq(_m(Nr, k, GA.reverse(Nr)), k))
                GA.check("N_s moves m (a genuine null rotation)", not GA.eq(_m(Nr, m, GA.reverse(Nr)), m))
                R = _m(B, Nr)
                GA.check("Lambda(m) B N_s = r^-1 Lambda(m)", GA.eq(_m(Lm, R), GA.scal(1 / r, Lm)))
                R2 = _m(Nr, B)
                GA.check("Lambda(m) N_s B = r^-1 Lambda(m)", GA.eq(_m(Lm, R2), GA.scal(1 / r, Lm)))
        # control: a transverse rotation (rational rotor) is not a scalar on Lambda(m): a helicity phase
        t = F(1, 2)
        Rt = GA.add(GA.sc((1 - t * t) / (1 + t * t)), GA.scal(2 * t / (1 + t * t), _wedge(a, b)))
        GA.check("transverse rotor is a rotor", GA.eq(_m(Rt, GA.reverse(Rt)), GA.sc(1)))
        LR = _m(Lm, Rt)
        GA.check("control: transverse rotation commutes with Lambda(m)", GA.eq(LR, _m(Rt, Lm)))
        scal_mult = any(GA.eq(LR, GA.scal(q, Lm)) for q in (F(1), F(-1), (1 - t * t) / (1 + t * t)))
        GA.check("control: transverse rotation is not a scalar on Lambda(m)", not scal_mult)
    return True


# ---------- (3) the f(r) class in Painleve-Gullstrand gauge: Cartan's first structure equations ----------
# 1-forms as 4-vectors of coefficients on theta^0..theta^3; 2-forms as dicts {(i, j): c} with i < j.

def _w(al, be):
    out = {}
    for i in range(4):
        for j in range(4):
            c = al[i] * be[j]
            if c == 0 or i == j:
                continue
            key, sg = ((i, j), 1) if i < j else ((j, i), -1)
            out[key] = out.get(key, F(0)) + sg * c
    return {k_: v for k_, v in out.items() if v != 0}


def _add2(*xs):
    out = {}
    for x in xs:
        for k_, v in x.items():
            out[k_] = out.get(k_, F(0)) + v
    return {k_: v for k_, v in out.items() if v != 0}


def _neg2(x):
    return {k_: -v for k_, v in x.items()}


ETA = (1, -1, -1, -1)


def _pg_connection(beta, dbeta, r, cot):
    """Connection forms omega^a_b (as 1-forms in the coframe) of theta^0 = dt, theta^1 = dr + beta dt,
    theta^2 = r dth, theta^3 = r sin th dph, for the radial function beta(r) with derivative dbeta."""
    z = [F(0)] * 4

    def e(i, c):
        v = list(z)
        v[i] = c
        return v
    om = {}
    om[(1, 0)] = e(1, -dbeta)            # omega^1_0 = -beta' theta^1
    om[(2, 0)] = e(2, -beta / r)         # omega^2_0 = -(beta/r) theta^2
    om[(3, 0)] = e(3, -beta / r)
    om[(2, 1)] = e(2, 1 / r)             # omega^2_1 = theta^2 / r
    om[(3, 1)] = e(3, 1 / r)
    om[(3, 2)] = e(3, cot / r)           # omega^3_2 = (cot th / r) theta^3
    full = {}
    for (i, j), v in om.items():
        full[(i, j)] = v
        # omega_ij = eta_ii omega^i_j antisymmetric: omega^j_i = -eta_jj eta_ii omega^i_j
        full[(j, i)] = [-ETA[j] * ETA[i] * c for c in v]
    for i in range(4):
        full[(i, i)] = list(z)
    return full


def _pg_dtheta(beta, dbeta, r, cot):
    th = [[F(int(i == j)) for j in range(4)] for i in range(4)]
    d0 = {}
    d1 = _w([F(0), dbeta, F(0), F(0)], th[0])                 # beta' dr ^ dt = beta' theta^1 ^ theta^0
    dr = [-beta, F(1), F(0), F(0)]                            # dr = theta^1 - beta theta^0
    d2 = _w([c / r for c in dr], th[2])                        # dr ^ dth = (dr/r) ^ theta^2
    d3 = _add2(_w([c / r for c in dr], th[3]), _w([F(0), F(0), cot / r, F(0)], th[3]))
    return [d0, d1, d2, d3]


def _structure_holds(beta, dbeta, r, cot, dbeta_conn=None):
    om = _pg_connection(beta, dbeta if dbeta_conn is None else dbeta_conn, r, cot)
    dth = _pg_dtheta(beta, dbeta, r, cot)
    th = [[F(int(i == j)) for j in range(4)] for i in range(4)]
    for a_ in range(4):
        rhs = {}
        for b_ in range(4):
            rhs = _add2(rhs, _neg2(_w(om[(a_, b_)], th[b_])))
        if _add2(dth[a_], _neg2(rhs)):
            return False
    # metric compatibility: omega_ab antisymmetric
    for i in range(4):
        for j in range(4):
            if any(ETA[i] * x + ETA[j] * y != 0 for x, y in zip(om[(i, j)], om[(j, i)])):
                return False
    return True


def check_pg_rotation_field_on_the_killing_line():
    premise("synthesis.imported-gtg-dictionary")
    premise("singularity.plane-rate")
    samples = [(F(1, 3), F(-2, 5), F(3), F(1, 2)), (F(-7, 4), F(5, 9), F(2, 7), F(-3)), (F(1), F(-1, 4), F(2), F(0))]
    for (beta, dbeta, r, cot) in samples:
        GA.check("Cartan's first structure equations hold for the PG connection", _structure_holds(beta, dbeta, r, cot))
        GA.check("control: a connection with a wrong radial coefficient fails", not _structure_holds(beta, dbeta, r, cot, dbeta_conn=dbeta + 1))
        om = _pg_connection(beta, dbeta, r, cot)
        Kc = [F(1), beta, F(0), F(0)]          # d/dt = E_0 + beta E_1 in the coframe components
        val = {ij: sum(x * y for x, y in zip(om[ij], Kc)) for ij in om}
        GA.check("along d/dt only the radial boost survives", all(val[(i, j)] == 0 for (i, j) in val if {i, j} != {0, 1}))
        GA.check("its coefficient is -beta beta' = f'/2", val[(1, 0)] == -beta * dbeta)
    # horizons: Q(beta) = 1, f = 1 - beta^2, f' = -2 beta beta'
    cases = []
    for Mm in (F(1), F(3, 2), F(1, 7)):
        rh = 2 * Mm                                           # Schwarzschild beta = sqrt(2M/r): beta(rh) = 1
        cases.append(("Schwarzschild", F(1), -F(1) / (2 * rh), 1 / (4 * Mm)))
    for H in (F(1), F(2, 3)):
        cases.append(("de Sitter", F(1), H, -H))           # beta = H r, beta(1/H) = 1, beta' = H
    # Schwarzschild-de Sitter with horizons r1 = 1, r2 = 2: H^2 = 1/7, M = 3/7, f = 1 - 2M/r - H^2 r^2
    H2, Ms = F(1, 7), F(3, 7)
    for rh in (F(1), F(2)):
        f = 1 - 2 * Ms / rh - H2 * rh * rh
        fp = 2 * Ms / (rh * rh) - 2 * H2 * rh
        GA.check("SdS horizon: f(rh) = 0", f == 0)
        cases.append(("SdS", F(1), -fp / 2, fp / 2))     # beta = 1 at the horizon, beta' = -f'/(2 beta)
    for (name, beta, dbeta, kappa) in cases:
        Kphys = GA.add(E[0], GA.scal(beta, E[1]))          # hb^{-1}(e_t) = e_t + beta e_r
        GA.check(name + ": the Killing vector is null on the horizon", _sc(_m(Kphys, Kphys)) == 0)
        GA.check(name + ": the t-line is a radial null ray (dr/dt = 1 - beta = 0)", 1 - beta == 0)
        coef = -beta * dbeta
        Omega_t = GA.scal(coef, _m(E[1], E[0]))            # Omega(e_t) = coef sigma_r, sigma_r = e_r e_t
        KdK = GA.scal(F(1, 2), GA.sub(_m(Omega_t, Kphys), _m(Kphys, Omega_t)))   # Omega(e_t) x K, K constant
        GA.check(name + ": (K.D)K = kappa K", GA.eq(KdK, GA.scal(kappa, Kphys)))
        GA.check(name + ": coefficient = kappa", coef == kappa)
        # Omega(e_t) = -F_K: F_K = -kappa k^m with m the dual null vector
        mm = GA.scal(F(1, 2), GA.sub(E[0], GA.scal(beta, E[1])))
        GA.check(name + ": sigma_r = k ^ m", GA.eq(_wedge(Kphys, mm), _m(E[1], E[0])))
    GA.check("tabulated: Schwarzschild M = 1 gives kappa = 1/4, the SdS horizons 2/7 and -5/28",
             cases[0][3] == F(1, 4) and cases[-2][3] == F(2, 7) and cases[-1][3] == F(-5, 28))
    return True


def check_value_factor_and_transport_compose_to_the_dilation():
    premise("synthesis.boost-evolution-on-generators-is-one-unitary-group")
    premise("synthesis.affine-cell-boost-spreads-without-scrambling")
    k, m = FRAMES[0][0], FRAMES[0][1]
    Lm = _lam(m)
    cells = [(F(1, 3), F(2)), (F(5), F(17, 2))]
    for r in (F(3, 2), F(1, 5), F(7, 3)):                  # r = e^{kappa t/2}; r < 1 is the cosmological sign
        # parallel transport along the Killing line: U = B_{1/r} (dU/dt = -(1/2) Omega U, Omega = kappa k^m);
        # the invariant field's value relative to the parallel frame is B_r psi
        B = _boost_in_plane(k, m, r)
        U = _boost_in_plane(k, m, 1 / r)
        GA.check("U = B^{-1}", GA.eq(_m(U, B), GA.sc(1)))
        GA.check("parallel generator k_par = U k U~ = r^-2 k (affine tangent)", GA.eq(_m(U, k, GA.reverse(U)), GA.scal(1 / (r * r), k)))
        val = _m(Lm, B)
        GA.check("value factor on the canonical component r^-1", GA.eq(val, GA.scal(1 / r, Lm)))
        weight_sq = 1 / (r * r)                             # the kernel scales by the square of the value factor
        for (a_, b_) in cells:
            jac = (r * r * b_ - r * r * a_) / (b_ - a_)      # the flow carries u to r^2 u
            GA.check("value factor and affine transport preserve the kernel", weight_sq * jac == 1)
            GA.check("control: either alone does not", weight_sq != 1 and jac != 1)
    return True


def check_closed_form_and_frame_independence():
    premise("synthesis.imported-gtg-dictionary")
    premise("field-theory.second-quantisation")
    for (k, m, a, b) in FRAMES:
        Lm = _lam(m)
        for kappa in (F(1, 4), F(-2, 7)):
            for w in (None, GA.add(GA.scal(F(2, 3), a), GA.scal(F(-5), b))):
                Fk = GA.add(GA.scal(-kappa, _wedge(k, m)), _m(k, w) if w is not None else GA.sc(0))
                GA.check("F_K^2 = kappa^2: one boost in a tilted plane", GA.eq(_m(Fk, Fk), GA.sc(kappa * kappa)))
                GA.check("k F_K = kappa k", GA.eq(_m(k, Fk), GA.scal(kappa, k)))
                GA.check("Lambda(m) F_K = kappa Lambda(m)", GA.eq(_m(Lm, Fk), GA.scal(kappa, Lm)))
                rs = (F(3, 2), F(2, 5), F(7, 3))
                # R(t) = exp(-t F/2) = cosh(kappa t/2) - sinh(kappa t/2) F/kappa, with r = e^{kappa t/2}
                def R(r):
                    return GA.sub(GA.sc((r + 1 / r) / 2), GA.scal((r - 1 / r) / (2 * kappa), Fk))
                for r in rs:
                    GA.check("R is a rotor", GA.eq(_m(R(r), GA.reverse(R(r))), GA.sc(1)))
                    GA.check("Lambda(m) R = r^-1 Lambda(m)", GA.eq(_m(Lm, R(r)), GA.scal(1 / r, Lm)))
                    GA.check("k R = r^-1 k: the intrinsic data k psi scale the same way", GA.eq(_m(k, R(r)), GA.scal(1 / r, k)))
                    GA.check("R k R~ = r^2 k: the flow's differential stretches the generator by e^{kappa t}", GA.eq(_m(R(r), k, GA.reverse(R(r))), GA.scal(r * r, k)))
                    for r2 in rs:
                        GA.check("one-parameter group: R(r) R(r2) = R(r r2)", GA.eq(_m(R(r), R(r2)), R(r * r2)))
            # tabulated rotors exp(-t F_K/2) at e^{kappa t/2} = 3/2 (exact values, frame 0 at kappa = 1/4, frame 1 at -2/7)
    TAB = {
        (0, False): {(): F(13, 12), (0, 1): F(-5, 12)},
        (0, True): {(): F(13, 12), (0, 1): F(-5, 12), (0, 2): F(-10, 9), (0, 3): F(25, 3), (1, 2): F(-10, 9), (1, 3): F(25, 3)},
        (1, False): {(): F(13, 12), (0, 1): F(-1, 4), (0, 2): F(-1, 3)},
        (1, True): {(): F(13, 12), (0, 1): F(131, 36), (0, 2): F(-13, 4), (0, 3): F(-875, 24), (1, 2): F(-175, 36),
                    (1, 3): F(-175, 8), (2, 3): F(-175, 6)},
    }
    for (fi, hw), want in TAB.items():
        k, m, a, b = FRAMES[fi]
        kappa = F(1, 4) if fi == 0 else F(-2, 7)
        w = GA.add(GA.scal(F(2, 3), a), GA.scal(F(-5), b)) if hw else None
        Fk = GA.add(GA.scal(-kappa, _wedge(k, m)), _m(k, w) if w is not None else GA.sc(0))
        r = F(3, 2)
        Rt = GA.sub(GA.sc((r + 1 / r) / 2), GA.scal((r - 1 / r) / (2 * kappa), Fk))
        GA.check("tabulated rotor exp(-t F_K/2)", GA.eq(Rt, want))
        GA.check("tabulated F_K^2", GA.eq(_m(Fk, Fk), GA.sc(F(1, 16) if fi == 0 else F(4, 49))))
    for (k, m, a, b) in FRAMES:
        for kappa in (F(1, 4),):
            # changing the second null direction m (null rotation about k) leaves k psi data unchanged up to scale
            s = GA.add(a, GA.scal(F(3), b))
            Nr = GA.add(GA.sc(1), GA.scal(F(1, 2), _m(k, s)))
            m2 = _m(Nr, m, GA.reverse(Nr))
            GA.check("m2 null, k.m2 = 1", _sc(_m(m2, m2)) == 0 and _dot(k, m2) == 1)
            GA.check("k N_s = k: the intrinsic projection k psi does not see the choice of m", GA.eq(_m(k, Nr), k))
    return True
