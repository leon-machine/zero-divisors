"""The frozen point stays parallel off the Einstein region exactly for the I-preserving connection.

Cl(2,4) with generators e0 (+1), e1, e2, e3 (-1), e+ (+1), e- (-1) (stored chart);
n0 = (e+ + e-)/2, ninf = e+ - e-, n0.ninf = 1; canonical tractor X = n0; frozen point
I_rho = ninf + rho n0 (Q = 2 rho, Lambda = 6 rho). A connection of the soldered tractor shape is,
at a point and along the direction a with frame vector u = hb^{-1}(a),
    A(a) = Omega(a) - ninf ^ u + n0 ^ s + beta n0 ^ ninf,
with Omega(a) a Lorentz bivector, s = S(u) the special-conformal slot, beta the dilation slot;
it acts on vectors by the commutator product (dilation generator n0 ^ ninf, as in the stored tractor theorem). The normal tractor connection has S = Sch, beta = 0;
the I-preserving connection has S = rho id, beta = 0.
(1) A(a) x I_rho = rho u - s - beta (ninf - rho n0): I_rho is parallel iff s = rho u, beta = 0
    (rho constant); the linear map (s, beta) -> A x I has rank 5 and Omega drops out.
(2) Normal minus I-preserving: D^N_a I - D^rho_a I = (rho - Sch)(u). With the field equation
    Ric + 8 pi G T = (Lambda + 4 pi G tau) g, Sch - rho g = -4 pi G (T - tau/3 g), and
    T -> T - tau/3 g is injective on symmetric T: D^N I = 0 iff T = 0.
(3) Topology/gauge: for every rho the section I_rho exists; the orbit map xi -> xi x I_rho on the
    15 bivectors has rank 5 (rho != 0 and rho = 0), stabiliser dimension 10; signature of I^perp
    (1,4) for rho > 0, (2,3) for rho < 0, degenerate for rho = 0.
(4) Transport off the Einstein region: the dust field g = tau^4 eta (conformal time, a = tau^2) has
    a parallel tractor of the normal connection, sigma = h tau^3, with Q = h^2 for every h, but
    X.I = sigma is not constant; in its own scale no parallel tractor exists since g is not Einstein.
Exact arithmetic only.
"""
from fractions import Fraction as Fr
from itertools import combinations

import GA
from tp_premise import premise

S = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
N0 = GA.scal(Fr(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])
ETA = [1, -1, -1, -1]
FP_SLOT = Fr(-10457, 90)
FP_MATTER = Fr(-53, 21)


def mul(x, y):
    return GA.mul(x, y, S)


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k and c != 0}


def wedge(x, y):
    return grade(mul(x, y), 2)


def comm(x, y):
    return GA.scal(Fr(1, 2), GA.sub(mul(x, y), mul(y, x)))


def dot(a, b):
    return GA.dot(a, b, S)


def vec(cs):
    return GA.add(*[GA.scal(Fr(c), E[i]) for i, c in enumerate(cs) if c != 0]) if any(cs) else {}


def frozen(rho):
    return GA.add(NI, GA.scal(Fr(rho), N0))


def conn(Om, u, s, beta):
    return GA.add(Om, GA.neg(wedge(NI, u)), wedge(N0, s), GA.scal(Fr(beta), wedge(N0, NI)))


def coords(x):
    return [x.get((i,), Fr(0)) for i in range(6)]


LOR = [wedge(E[i], E[j]) for i, j in combinations(range(4), 2)]
BIV = [wedge(E[i], E[j]) for i, j in combinations(range(6), 2)]
SAMPLE_OM = GA.add(GA.scal(Fr(2), LOR[0]), GA.scal(Fr(-3, 7), LOR[3]), GA.scal(Fr(5), LOR[5]))
SAMPLE_U = [vec([1, Fr(1, 2), 0, -2, 0, 0]), vec([0, 3, 1, 0, 0, 0]), vec([Fr(2, 3), 0, -1, 1, 0, 0])]
SAMPLE_S = [vec([Fr(1, 5), -1, 2, 0, 0, 0]), vec([3, 0, 0, Fr(-1, 4), 0, 0])]


def check_slot_rho_is_the_unique_parallel_extension():
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    premise("synthesis.curvature-only-tractor-actions-are-macdowell-mansouri")
    GA.check("n0, ninf null, n0.ninf = 1", dot(N0, N0) == 0 and dot(NI, NI) == 0 and dot(N0, NI) == 1)
    fp = Fr(0)
    for rho, q in ((Fr(1, 2), Fr(1)), (Fr(-3, 2), Fr(-3)), (Fr(0), Fr(0)), (Fr(7, 6), Fr(7, 3))):
        I = frozen(rho)
        GA.check("Q(I_rho) = 2 rho and X.I = 1, rho=%s" % rho, dot(I, I) == q and dot(N0, I) == 1)
        GA.check("Lorentz block commutes with I_rho", GA.is_zero(comm(SAMPLE_OM, I)))
        for u in SAMPLE_U:
            for s in SAMPLE_S + [GA.scal(rho, u)]:
                for beta in (Fr(0), Fr(2, 3)):
                    lhs = comm(conn(SAMPLE_OM, u, s, beta), I)
                    rhs = GA.add(GA.scal(rho, u), GA.neg(s), GA.scal(-beta, GA.sub(NI, GA.scal(rho, N0))))
                    GA.check("A x I = rho u - s + beta(ninf - rho n0)", GA.eq(lhs, rhs))
                    fp += sum((i + 1) * c for i, c in enumerate(coords(lhs)))
            # the I-preserving connection: slot rho u, no dilation
            GA.check("slot rho u keeps I_rho parallel",
                     GA.is_zero(comm(conn(SAMPLE_OM, u, GA.scal(rho, u), 0), I)))
            # linear map (s, beta) -> A x I at fixed u, Omega: rank 5, so the solution is unique
            cols = []
            for k in range(4):
                cols.append(coords(comm(wedge(N0, E[k]), I)))
            cols.append(coords(comm(wedge(N0, NI), I)))
            GA.check("(s, beta) -> A x I injective (rank 5)", GA.rank_of_vectors(cols) == 5)
            # the normal-type slot with a generic Schouten value breaks parallelism
            GA.check("a slot other than rho u is not parallel",
                     not GA.is_zero(comm(conn(SAMPLE_OM, u, GA.add(GA.scal(rho, u), SAMPLE_S[0]), 0), I)))
    GA.check("regression value of the sampled A x I", fp == FP_SLOT)
    # gauge: the special-conformal rotor U = 1 + (1/2) n0 ^ y (nilpotent generator) fixes X = n0 but
    # moves I_rho off span(ninf, n0), so the slot form rho id is a statement in a gauge
    y = vec([1, 2, 0, -1, 0, 0])
    gen_ = wedge(N0, y)
    GA.check("special-conformal generator is nilpotent", GA.is_zero(mul(gen_, gen_)))
    U = GA.add(GA.sc(Fr(1)), GA.scal(Fr(1, 2), gen_))
    Ut = GA.reverse(U)
    GA.check("U is a rotor", GA.eq(mul(U, Ut), GA.sc(Fr(1))))
    GA.check("U fixes X = n0", GA.eq(mul(mul(U, N0), Ut), N0))
    I2 = mul(mul(U, frozen(Fr(1, 2))), Ut)
    sp = coords(I2)[:4]
    GA.check("U moves I_rho off span(ninf, n0)", any(c != 0 for c in sp))
    GA.check("its spacetime part is -<X,I> y", sp == [-c for c in coords(y)[:4]])
    return True


def _sym(rows):
    return [[Fr(x) for x in r] for r in rows]


def _lower(Tup):
    # T_ab from mixed T^a_b: lower with eta
    return [[ETA[a] * Tup[a][b] for b in range(4)] for a in range(4)]


def _apply(M, u):
    # M^a_b u^b, M given as covariant M_ab, u a vector of span(e0..e3)
    uc = [u.get((i,), Fr(0)) for i in range(4)]
    return vec([sum(ETA[a] * M[a][b] * uc[b] for b in range(4)) for a in range(4)] + [0, 0])


def check_transport_differs_from_it_by_the_matter_term():
    premise("synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part")
    premise("interior.scale-tractor-leaves-cone")
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    Ts = [_sym([[2, 1, 0, 0], [1, 1, 0, Fr(1, 2)], [0, 0, 3, 0], [0, Fr(1, 2), 0, -1]]),
          _sym([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
          _sym([[5, 0, 0, 0], [0, 5, 0, 0], [0, 0, 5, 0], [0, 0, 0, 5]])]
    k = Fr(3, 7)  # k stands for 4 pi G: the identity is linear in it, so a rational value tests it
    fp = Fr(0)
    for Lam in (Fr(3), Fr(-3, 2)):
        rho = Lam / 6
        for T in Ts:
            tau = sum(ETA[a] * T[a][a] for a in range(4))
            g = [[Fr(ETA[a]) if a == b else Fr(0) for b in range(4)] for a in range(4)]
            Ric = [[(Lam + k * tau) * g[a][b] - 2 * k * T[a][b] for b in range(4)] for a in range(4)]
            R = sum(ETA[a] * Ric[a][a] for a in range(4))
            Sch = [[Fr(1, 2) * (Ric[a][b] - R * g[a][b] / 6) for b in range(4)] for a in range(4)]
            target = [[rho * g[a][b] - k * (T[a][b] - tau * g[a][b] / 3) for b in range(4)] for a in range(4)]
            GA.check("on shell Sch = rho g - 4 pi G (T - tau/3 g)", Sch == target)
            I = frozen(rho)
            for u in SAMPLE_U:
                DN = comm(conn(SAMPLE_OM, u, _apply(Sch, u), 0), I)
                Drho = comm(conn(SAMPLE_OM, u, GA.scal(rho, u), 0), I)
                GA.check("D^rho I = 0", GA.is_zero(Drho))
                M = [[k * (T[a][b] - tau * g[a][b] / 3) for b in range(4)] for a in range(4)]
                GA.check("D^N I = 4 pi G (T - tau/3 g)(u)", GA.eq(GA.sub(DN, Drho), _apply(M, u)))
                fp += sum((i + 1) * c for i, c in enumerate(coords(DN)))
    # T -> T - tau/3 g is injective on symmetric tensors (rank 10)
    rows = []
    for a, b in [(a, b) for a in range(4) for b in range(a, 4)]:
        T = [[Fr(0)] * 4 for _ in range(4)]
        T[a][b] = T[b][a] = Fr(1)
        tau = sum(ETA[c] * T[c][c] for c in range(4))
        rows.append([T[c][d] - tau * (ETA[c] if c == d else 0) / 3 for c in range(4) for d in range(c, 4)])
    GA.check("T -> T - tau/3 g has rank 10", GA.rank_of_vectors(rows) == 10)
    GA.check("regression value of the sampled D^N I", fp == FP_MATTER)
    return True


def check_sections_exist_for_every_norm_and_are_gauge():
    premise("dark-energy.imported-frozen-point-geometry")
    premise("odd-extensions.transport-constrains-frozen-point-only-through")
    for rho, q, sig in ((Fr(1, 2), Fr(1), (1, 4, 0)), (Fr(5), Fr(10), (1, 4, 0)),
                        (Fr(-1, 3), Fr(-2, 3), (2, 3, 0)), (Fr(0), Fr(0), None)):
        I = frozen(rho)
        GA.check("Q(I_rho) = %s" % q, dot(I, I) == q)
        img = [coords(comm(B, I)) for B in BIV]
        GA.check("orbit map rank 5 (stabiliser dim 10), rho=%s" % rho, GA.rank_of_vectors(img) == 5)
        GA.check("orbit tangent is I^perp", all(dot(comm(B, I), I) == 0 for B in BIV))
        if sig is not None:
            # Gram matrix of I^perp in the basis e0..e3, ninf - rho n0
            basis = E[:4] + [GA.sub(NI, GA.scal(rho, N0))]
            Gm = [[dot(x, y) for y in basis] for x in basis]
            GA.check("all basis vectors orthogonal to I", all(dot(x, I) == 0 for x in basis))
            GA.check("signature of I^perp is %s" % (sig,), GA.congruence_signature(Gm) == sig)
    return True


# ---- (4) the dust field in conformal time: exact rational functions of tau ----
TAU = GA.RF.var()


def _c(x):
    return GA.RF.const(x)


def _pw(f, k):
    out = _c(1)
    for _ in range(k):
        out = out * f
    return out


def _geometry(a):
    """Metric a(tau)^2 eta; returns g, ginv, Gamma, store Ricci (minus the coordinate formula)."""
    a2 = a * a
    g = [[(a2 * _c(ETA[i]) if i == j else _c(0)) for j in range(4)] for i in range(4)]
    gi = [[(_c(ETA[i]) / a2 if i == j else _c(0)) for j in range(4)] for i in range(4)]

    def d(f, k):
        return f.deriv() if k == 0 else _c(0)

    Gam = [[[_c(0)] * 4 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                s = _c(0)
                for m in range(4):
                    s = s + gi[i][m] * (d(g[m][k], j) + d(g[m][j], k) - d(g[j][k], m))
                Gam[i][j][k] = s * _c(Fr(1, 2))
    Ric = [[_c(0)] * 4 for _ in range(4)]
    for b in range(4):
        for dd in range(4):
            s = _c(0)
            for i in range(4):
                s = s + d(Gam[i][dd][b], i) - d(Gam[i][i][b], dd)
                for e in range(4):
                    s = s + Gam[i][i][e] * Gam[e][dd][b] - Gam[i][dd][e] * Gam[e][i][b]
            Ric[b][dd] = -s  # store convention: de Sitter has Ric = Lambda g in signature (+,-,-,-)
    return g, gi, Gam, Ric


def _schouten(g, gi, Ric):
    R = _c(0)
    for i in range(4):
        R = R + gi[i][i] * Ric[i][i]
    P = [[(Ric[i][j] - R * g[i][j] * _c(Fr(1, 6))) * _c(Fr(1, 2)) for j in range(4)] for i in range(4)]
    J = _c(0)
    for i in range(4):
        J = J + gi[i][i] * P[i][i]
    return P, J, R


def _scale_tractor(sig, g, gi, Gam, P, J):
    """(sigma, mu_b, rho) with mu = d sigma, rho = (sigma J - Lap sigma)/4; returns residuals and Q."""
    ds = [sig.deriv(), _c(0), _c(0), _c(0)]
    hess = [[(ds[0].deriv() if (i == 0 and j == 0) else _c(0)) for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                hess[i][j] = hess[i][j] - Gam[k][i][j] * ds[k]
    lap = _c(0)
    for i in range(4):
        lap = lap + gi[i][i] * hess[i][i]
    rho = (sig * J - lap) * _c(Fr(1, 4))
    mid = [[hess[i][j] + g[i][j] * rho - P[i][j] * sig for j in range(4)] for i in range(4)]
    bot = []
    for i in range(4):
        s = (rho.deriv() if i == 0 else _c(0))
        for b in range(4):
            s = s + P[i][b] * gi[b][b] * ds[b]
        bot.append(s)
    Q = sig * rho * _c(2)
    for i in range(4):
        Q = Q + gi[i][i] * ds[i] * ds[i]
    return mid, bot, Q


def check_transport_parallel_tractor_off_einstein_has_no_physical_scale():
    premise("interior.imported-tractor-connection")
    premise("interior.scale-tractor-leaves-cone")
    # calibration: de Sitter in conformal time, a = 1/(H tau), Ric = 3 H^2 g, P = (H^2/2) g
    for H, H2 in ((Fr(1), Fr(1)), (Fr(2, 3), Fr(4, 9))):
        a = _c(1) / (TAU * _c(H))
        g, gi, Gam, Ric = _geometry(a)
        GA.check("de Sitter: Ric = 3H^2 g (store sign), H=%s" % H,
                 all(Ric[i][j].eqrf(g[i][j] * _c(3 * H2)) for i in range(4) for j in range(4)))
        P, J, R = _schouten(g, gi, Ric)
        mid, bot, Q = _scale_tractor(_c(1), g, gi, Gam, P, J)
        GA.check("de Sitter: I = (1, 0, Lambda/6) parallel in its own scale, Q = Lambda/3",
                 all(m.is_zero() for r in mid for m in r) and all(b.is_zero() for b in bot)
                 and Q.eqrf(_c(H2)))
    # the dust field a = tau^2 (Lambda = 0, conformally flat, not Einstein)
    a = TAU * TAU
    g, gi, Gam, Ric = _geometry(a)
    P, J, R = _schouten(g, gi, Ric)
    GA.check("dust field: R = 12/tau^6", R.eqrf(_c(12) / _pw(TAU, 6)))
    tf = [[Ric[i][j] - R * g[i][j] * _c(Fr(1, 4)) for j in range(4)] for i in range(4)]
    GA.check("dust field is not Einstein (trace-free Ricci nonzero)", not tf[0][0].is_zero())
    # in its own scale (sigma = 1) the scale tractor is not parallel
    mid, bot, Q = _scale_tractor(_c(1), g, gi, Gam, P, J)
    GA.check("own-scale tractor (1, 0, J/4) not parallel", not all(m.is_zero() for r in mid for m in r))
    GA.check("own-scale norm J/2 = R/12 varies", Q.eqrf(_c(1) / _pw(TAU, 6)))
    for h, h2 in ((Fr(1), Fr(1)), (Fr(3), Fr(9)), (Fr(-2, 5), Fr(4, 25))):
        sig = _c(h) * _pw(TAU, 3)
        mid, bot, Q = _scale_tractor(sig, g, gi, Gam, P, J)
        GA.check("sigma = h tau^3 gives a parallel tractor of the normal connection, h=%s" % h,
                 all(m.is_zero() for r in mid for m in r) and all(b.is_zero() for b in bot))
        GA.check("its norm is h^2 (every positive value)", Q.eqrf(_c(h2)))
        GA.check("X.I = sigma is not constant", not sig.deriv().is_zero())
    # sigma = a = tau^2 is the flat scale: parallel and null; combinations stay parallel, norm constant
    for h in (Fr(0), Fr(1), Fr(-5, 2)):
        sig = _pw(TAU, 2) + _c(h) * _pw(TAU, 3)
        mid, bot, Q = _scale_tractor(sig, g, gi, Gam, P, J)
        GA.check("sigma = tau^2 + h tau^3 parallel with constant norm, h=%s" % h,
                 all(m.is_zero() for r in mid for m in r) and all(b.is_zero() for b in bot)
                 and Q.deriv().is_zero())
        if h == 0:
            GA.check("the flat scale tractor is null", Q.is_zero())
    # other exponents are not parallel
    for k in (1, 4, 5):
        mid, bot, Q = _scale_tractor(_pw(TAU, k), g, gi, Gam, P, J)
        GA.check("sigma = tau^%d is not parallel" % k, not all(m.is_zero() for r in mid for m in r))
    return True
