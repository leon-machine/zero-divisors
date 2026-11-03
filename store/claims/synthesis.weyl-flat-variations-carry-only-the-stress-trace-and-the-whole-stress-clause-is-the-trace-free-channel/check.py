"""Exact checks: the linear channels of the position-gauge field at a momentum p, the Weyl-flat class as the
trace channel, the null flux as the trace-free channel, and the response of minimally coupled matter.

Conventions: background Cl(1,3), signature (+,-,-,-), frame e_0..e_3 with reciprocal e^a. A first-order field
with metric perturbation h (a symmetric map of vectors, g(a, b) = a.b + h(a).b) whose second derivatives are
h0 (p.a)(p.b) (the polynomial field h(x) = (p.x)^2 h0 / 2) has the constant linearised curvature
R_p[h0](B) = -1/2 p ^ h0(B.p) (overall sign fixed by the curvature convention; nothing below depends on it),
Ricci Ric(b) = sum_a e^a . R(e_a ^ b), scalar S = sum_b e^b . Ric(e_b), Schouten P(a) = (Ric(a) - a S/6)/2,
Weyl W(a ^ b) = R(a ^ b) - P(a) ^ b - a ^ P(b). A displacement x -> x + xi0 (p.x)^2/2 changes h0 by
(a.p) xi0 + (a.xi0) p (the gauge space G_p); a conformal change hb^{-1}(a) = phi a changes h0 by a multiple of
the identity (the line L).

(1) For p in {e0, e3, e0 + e1} (the Lorentz-orbit representatives, up to scale, of the nonzero momenta) and three
    further rational momenta: ker R_p = G_p (dim 4), ker W_p = G_p + L (dim 5), W_p trace-free; the kernel of the
    linearised scalar curvature has dim 9 and contains G_p; the scalar curvature of the identity is 3 Q(p), so the
    kernel misses L exactly when Q(p) != 0.
(2) The stabiliser of p (rational rotors, boosts and reflections) leaves G_p invariant and its commutant on the
    six-dimensional quotient Sym/G_p has dimension 2, for p = e0 and p = e3.
(3) Conserved sources at p (symmetric T0 with T0(p) = 0, dim 6): the pairing tr(h0 T0) vanishes on G_p, has rank
    6, its annihilator of G_p + L is the trace-free conserved sources (dim 5), and for Q(p) != 0 its annihilator
    of the scalar-curvature kernel is the line of Q(p) a - (a.p) p.
(4) Null fluxes k.T(k) over twelve rational null k determine a symmetric T up to a multiple of the identity; a
    conserved source at p != 0 that is a multiple of the identity is zero.
(5) Minimal coupling: L(hb) = <hb(F)^2>/(2 det hb) has derivative along hb = 1 + t delta equal to
    sum_a delta(e_a).T(e^a) with T(a) = -1/2 F a F (the stored Maxwell stress) and zero along delta = identity;
    L(hb) = (Q(hb(g)) - m^2 phi^2)/(2 det hb) has the canonical stress (a.g) g - a L, of trace -Q(g) + 2 m^2 phi^2.
    Derivatives are taken from exact evaluations at six rational t by interpolation, not from the formula.
(2') At p = e0 + e1 (null), with a transverse rotation, two null rotations and a reflection fixing p: gauge plus
    the two helicity-two directions, and that plus the identity, are further invariant classes; the scalar-flat
    kernel contains the identity; the helicity-two directions are not Weyl-flat.
(6) Point sources: kappa -> sum_n s_n kappa_n p_n on a momentum-conserving rational configuration of five
    momenta has kernel the constant vectors (one coupling); a null momentum has zero coupling to the line L.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

SQ = GA.sig(1, 3)
E = [GA.gen(i) for i in range(4)]
ETA = [1, -1, -1, -1]
ER = [GA.scal(F(1, ETA[i]), E[i]) for i in range(4)]
BV = list(combinations(range(4), 2))
SYM = [(i, j) for i in range(4) for j in range(i, 4)]

P_TIMELIKE = [F(3), F(1), F(2), F(0)]
P_SPACELIKE = [F(1), F(2), F(0), F(1)]
P_NULL = [F(5), F(3), F(4), F(0)]
NULLS = [[1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1], [1, -1, 0, 0], [1, 0, -1, 0], [1, 0, 0, -1],
         [5, 3, 4, 0], [5, 0, 3, 4], [5, 4, 0, 3], [13, 5, 12, 0], [3, 1, 2, 2], [3, -2, 2, 1]]
FIELD = [((0, 1), F(2)), ((0, 2), F(-1, 3)), ((1, 3), F(5, 4)), ((2, 3), F(1, 2)), ((0, 3), F(3)),
         ((1, 2), F(-2, 7))]
GRAD = [F(2), F(1, 3), F(-1), F(1, 2)]
PHI, M2 = F(3, 5), F(7, 4)
TS = [F(0), F(1, 3), F(-1, 2), F(2, 5), F(-3, 7), F(1, 9)]
# five momenta, signs s_n (+1 incoming, -1 outgoing), sum s_n p_n = 0
MOMENTA = [([F(5), F(3), F(4), F(0)], 1), ([F(3), F(0), F(1), F(1)], 1), ([F(2), F(1), F(1), F(1)], -1),
           ([F(1), F(0), F(0), F(0)], -1)]


# ---------------------------------------------------------------- helpers
def vec(c):
    out = {}
    for i in range(len(c)):
        out = GA.add(out, GA.scal(c[i], E[i]))
    return out


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def dotv(a, b):
    return GA.dot(a, b, SQ)


def wedge(a, b):
    return grade(GA.mul(a, b, SQ), 2)


def bv_dot_v(B, a):
    return grade(GA.mul(B, a, SQ), 1)


def v_dot_bv(a, B):
    return grade(GA.mul(a, B, SQ), 1)


def comps(x, blades):
    return [x.get(b, F(0)) for b in blades]


def unit(k, n):
    return [F(1) if i == k else F(0) for i in range(n)]


def sym_map(coeffs):
    def h(a):
        out = {}
        for (i, j), c in zip(SYM, coeffs):
            if c != 0:
                out = GA.add(out, GA.scal(c * dotv(a, E[i]), E[j]), GA.scal(c * dotv(a, E[j]), E[i]))
        return out
    return h


def _rref(rows, n):
    m = [list(r) for r in rows]
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, len(m)) if m[i][c] != 0), None)
        if p is None:
            continue
        m[r], m[p] = m[p], m[r]
        pv = m[r][c]
        m[r] = [x / pv for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [x - f * y for x, y in zip(m[i], m[r])]
        piv.append(c)
        r += 1
    return m, piv


def nullspace(rows, n):
    m, piv = _rref(rows, n)
    basis = []
    for fc in [c for c in range(n) if c not in piv]:
        v = unit(fc, n)
        for i, c in enumerate(piv):
            v[c] = -m[i][fc]
        basis.append(v)
    return basis


def solve(rows, rhs):
    n = len(rows[0])
    m, piv = _rref([list(r) + [b] for r, b in zip(rows, rhs)], n)
    for i in range(len(piv), len(m)):
        assert m[i][n] == 0
    x = [F(0)] * n
    for i, c in enumerate(piv):
        x[c] = m[i][n]
    return x


def rank(vs):
    return GA.rank_of_vectors(vs) if vs else 0


SYM_GRAM = [[dotv(E[k], sym_map(unit(s, 10))(E[l])) for s in range(10)] for k in range(4) for l in range(4)]


def sym_coords(h):
    return solve(SYM_GRAM, [dotv(E[k], h(E[l])) for k in range(4) for l in range(4)])


ID = sym_coords(lambda a: a)


def gauge(p, xi):
    return sym_coords(lambda a: GA.add(GA.scal(dotv(a, p), xi), GA.scal(dotv(a, xi), p)))


def curvature(h, p):
    return lambda B: GA.scal(F(-1, 2), wedge(p, h(bv_dot_v(B, p))))


def ricci(R):
    return lambda b: GA.add(*[v_dot_bv(ER[a], R(wedge(E[a], b))) for a in range(4)])


def scalar_curv(R):
    Ric = ricci(R)
    return sum(dotv(ER[b], Ric(E[b])) for b in range(4))


def weyl(R):
    Ric = ricci(R)
    s = scalar_curv(R)
    P = lambda v: GA.scal(F(1, 2), GA.sub(Ric(v), GA.scal(s / 6, v)))
    return lambda a, b: GA.sub(R(wedge(a, b)), GA.add(wedge(P(a), b), wedge(a, P(b))))


def R_matrix(p):
    cols = []
    for k in range(10):
        R = curvature(sym_map(unit(k, 10)), p)
        col = []
        for (a, b) in BV:
            col += comps(R(wedge(E[a], E[b])), BV)
        cols.append(col)
    return [list(r) for r in zip(*cols)]


def W_matrix(p):
    cols = []
    for k in range(10):
        W = weyl(curvature(sym_map(unit(k, 10)), p))
        col = []
        for (a, b) in BV:
            col += comps(W(E[a], E[b]), BV)
        cols.append(col)
    return [list(r) for r in zip(*cols)]


def S_row(p):
    return [scalar_curv(curvature(sym_map(unit(k, 10)), p)) for k in range(10)]


def versor(U, norm):
    Ur = GA.reverse(U)
    return lambda a: GA.scal(F(1) / norm, grade(GA.mul(GA.mul(U, a, SQ), Ur, SQ), 1))


def reflection(n):
    nn = dotv(n, n)
    return lambda a: GA.scal(F(-1) / nn, grade(GA.mul(GA.mul(n, a, SQ), n, SQ), 1))


def inverse_map(Lm):
    M = [[dotv(ER[i], Lm(E[j])) for j in range(4)] for i in range(4)]
    cols = [solve(M, unit(j, 4)) for j in range(4)]
    return lambda a: GA.add(*[GA.scal(dotv(a, ER[j]), vec(cols[j])) for j in range(4)])


def act(Lm, coeffs):
    Li = inverse_map(Lm)
    h = sym_map(coeffs)
    return sym_coords(lambda a: Lm(h(Li(a))))


def quotient_commutant(p, gens):
    G = [gauge(p, E[i]) for i in range(4)]
    Q = []
    for k in range(10):
        if rank(G + Q + [unit(k, 10)]) > len(G) + len(Q):
            Q.append(unit(k, 10))
    BT = [list(r) for r in zip(*(G + Q))]
    mats, g_invariant = [], True
    for Lm in gens:
        for g in G:
            c = solve(BT, act(Lm, g))
            g_invariant = g_invariant and all(x == 0 for x in c[len(G):])
        A = [solve(BT, act(Lm, q))[len(G):] for q in Q]
        mats.append([list(r) for r in zip(*A)])
    n = len(Q)
    rows = []
    for A in mats:
        for i in range(n):
            for j in range(n):
                row = [F(0)] * (n * n)
                for k in range(n):
                    row[i * n + k] += A[k][j]
                    row[k * n + j] -= A[i][k]
                rows.append(row)
    return g_invariant, len(Q), len(nullspace(rows, n * n))


def pair(hc, Tc):
    h, T = sym_map(hc), sym_map(Tc)
    return sum(dotv(ER[a], h(T(E[a]))) for a in range(4))


def conserved_basis(p):
    rows = [[dotv(ER[i], sym_map(unit(k, 10))(p)) for k in range(10)] for i in range(4)]
    return nullspace(rows, 10)


def combine(cs, basis):
    return [sum(cs[i] * basis[i][k] for i in range(len(basis))) for k in range(10)]


def trace_of(Tc):
    T = sym_map(Tc)
    return sum(dotv(ER[a], T(E[a])) for a in range(4))


def lin_map(M):
    return lambda a: GA.add(*[GA.scal(sum(M[i][j] * dotv(a, ER[j]) for j in range(4)), E[i]) for i in range(4)])


def outer_bv(Lm, B):
    out = {}
    for (a, b) in BV:
        c = B.get((a, b), F(0))
        if c:
            out = GA.add(out, GA.scal(c, wedge(Lm(E[a]), Lm(E[b]))))
    return out


def det(Lm):
    X = GA.mul(GA.mul(Lm(E[0]), Lm(E[1]), SQ), GA.mul(Lm(E[2]), Lm(E[3]), SQ), SQ)
    return X.get((0, 1, 2, 3), F(0))


def deriv_at_zero(ts, vals):
    d = F(0)
    for i in range(len(ts)):
        others = [ts[j] for j in range(len(ts)) if j != i]
        den = F(1)
        for t in others:
            den *= ts[i] - t
        s = F(0)
        for k in range(len(others)):
            pr = F(1)
            for j, t in enumerate(others):
                if j != k:
                    pr *= -t
            s += pr
        d += vals[i] * s / den
    return d


def response(density):
    """d/dt at t = 0 of density(1 + t E_ij) for each elementary map E_ij (E_ij(e_j) = e_i)."""
    out = [[None] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            vp, vd = [], []
            for t in TS:
                M = [[(F(1) if r == c else F(0)) + (t if (r, c) == (i, j) else F(0)) for c in range(4)]
                     for r in range(4)]
                num, dt = density(lin_map(M))
                vp.append(num)
                vd.append(dt)
            dp, dd = deriv_at_zero(TS, vp), deriv_at_zero(TS, vd)
            out[i][j] = dp / vd[0] - vp[0] * dd / (vd[0] * vd[0])
    return out


FBV = {}
for (bl, cf) in FIELD:
    FBV = GA.add(FBV, GA.scal(cf, wedge(E[bl[0]], E[bl[1]])))


def maxwell_density(hb):
    Fh = outer_bv(hb, FBV)
    return F(1, 2) * GA.mul(Fh, Fh, SQ).get((), F(0)), det(hb)


def scalar_density(hb):
    hg = hb(vec(GRAD))
    return F(1, 2) * dotv(hg, hg) - F(1, 2) * M2 * PHI * PHI, det(hb)


# ---------------------------------------------------------------- checks
def check_linear_curvature_kernels():
    premise("synthesis.twistor-flat-fields-give-nordstrom-not-einstein")
    reps = [unit(0, 4), unit(3, 4), [F(1), F(1), F(0), F(0)], P_TIMELIKE, P_SPACELIKE, P_NULL]
    ok = True
    for pc in reps:
        p = vec(pc)
        q = dotv(p, p)
        G = [gauge(p, E[i]) for i in range(4)]
        kR = nullspace(R_matrix(p), 10)
        kW = nullspace(W_matrix(p), 10)
        kS = nullspace([S_row(p)], 10)
        ok = ok and rank(G) == 4 and len(kR) == 4 and rank(kR + G) == 4
        ok = ok and len(kW) == 5 and rank(kW + G + [ID]) == 5
        ok = ok and len(kS) == 9 and rank(kS + G) == 9
        s_id = sum(a * b for a, b in zip(S_row(p), ID))
        ok = ok and s_id == 3 * q
        W = weyl(curvature(sym_map([F(k + 2, 7) for k in range(10)]), p))
        ok = ok and all(GA.add(*[v_dot_bv(ER[a], W(E[a], E[b])) for a in range(4)]) == {} for b in range(4))
        GA.check("kernels at p with Q(p) = %s" % q, ok)
    return ok


E0, E1, E2, E3 = E
# rational rotors (scalar part, bivector coefficient, plane) and their norms U rev(U)
R12 = versor(GA.sub(GA.sc(2), GA.mul(E1, E2, SQ)), 5)
R23 = versor(GA.sub(GA.sc(3), GA.scal(2, GA.mul(E2, E3, SQ))), 13)
R13 = versor(GA.sub(GA.sc(1), GA.scal(3, GA.mul(E1, E3, SQ))), 10)
B01 = versor(GA.add(GA.sc(2), GA.mul(E0, E1, SQ)), 3)
B02 = versor(GA.add(GA.sc(3), GA.mul(E0, E2, SQ)), 8)
TIME_STAB = [R12, R23, R13, reflection(E1), reflection(E3)]
SPACE_STAB = [R12, B01, B02, reflection(E1), reflection(E2)]


def check_stabiliser_commutant_on_gauge_quotient():
    # the elements are Lorentz maps with the stated angles and fix the momentum
    ok = dotv(R12(E1), ER[1]) == F(3, 5) and dotv(R23(E2), ER[2]) == F(5, 13)
    ok = ok and dotv(R13(E1), ER[1]) == F(-4, 5) and dotv(B01(E0), E0) == F(5, 3) and dotv(B02(E0), E0) == F(5, 4)
    ok = ok and all(Lm(E0) == E0 for Lm in TIME_STAB) and all(Lm(E3) == E3 for Lm in SPACE_STAB)
    ok = ok and all(dotv(Lm(a), Lm(b)) == dotv(a, b) for Lm in TIME_STAB + SPACE_STAB for a in E for b in E)
    gi_t, nq_t, dim_t = quotient_commutant(E0, TIME_STAB)
    gi_s, nq_s, dim_s = quotient_commutant(E3, SPACE_STAB)
    ok = ok and gi_t and gi_s and nq_t == 6 and nq_s == 6 and dim_t == 2 and dim_s == 2
    GA.check("stabiliser commutant on Sym/G_p is two-dimensional (timelike, spacelike)", ok)
    return ok


NULL_P = GA.add(E0, E1)
NULL_STAB = [versor(GA.sub(GA.sc(2), GA.mul(E2, E3, SQ)), 5), versor(GA.add(GA.sc(1), GA.mul(NULL_P, E2, SQ)), 1),
             versor(GA.add(GA.sc(1), GA.mul(NULL_P, E3, SQ)), 1), reflection(E2)]


def invariant(space, gens):
    r = rank(space)
    return all(rank(space + [act(Lm, v)]) == r for Lm in gens for v in space)


def check_null_momentum_has_further_classes():
    n = NULL_P
    ok = all(Lm(n) == n for Lm in NULL_STAB)
    ok = ok and all(dotv(Lm(a), Lm(b)) == dotv(a, b) for Lm in NULL_STAB for a in E for b in E)
    ok = ok and dotv(NULL_STAB[1](E2), E0) == -2 and dotv(NULL_STAB[0](E2), ER[2]) == F(3, 5)
    G = [gauge(n, E[i]) for i in range(4)]
    H = [sym_coords(lambda a: GA.sub(GA.scal(dotv(a, E2), E2), GA.scal(dotv(a, E3), E3))),
         sym_coords(lambda a: GA.add(GA.scal(dotv(a, E2), E3), GA.scal(dotv(a, E3), E2)))]
    kS = nullspace([S_row(n)], 10)
    kW = nullspace(W_matrix(n), 10)
    ok = ok and rank(G + H) == 6 and invariant(G + H, NULL_STAB)
    ok = ok and rank(G + H + [ID]) == 7 and invariant(G + H + [ID], NULL_STAB)
    ok = ok and invariant(G + [ID], NULL_STAB) and invariant(kS, NULL_STAB)
    ok = ok and len(kS) == 9 and rank(kS + G + H + [ID]) == 9
    ok = ok and rank(kW + H) == 7
    GA.check("null momentum: gauge plus helicity two is a further invariant class", ok)
    return ok


def check_conserved_source_pairing_channels():
    ok = True
    for pc in [unit(0, 4), P_TIMELIKE, P_SPACELIKE, P_NULL]:
        p = vec(pc)
        q = dotv(p, p)
        Tr = conserved_basis(p)
        G = [gauge(p, E[i]) for i in range(4)]
        ok = ok and len(Tr) == 6 and all(pair(g, t) == 0 for g in G for t in Tr)
        ok = ok and rank([[pair(unit(k, 10), t) for t in Tr] for k in range(10)]) == 6
        annL = nullspace([[pair(ID, t) for t in Tr]], 6)
        ok = ok and len(annL) == 5 and all(trace_of(combine(c, Tr)) == 0 for c in annL)
        if q != 0:
            kS = nullspace([S_row(p)], 10)
            annC = nullspace([[pair(h, t) for t in Tr] for h in kS], 6)
            line = sym_coords(lambda a: GA.sub(GA.scal(q, a), GA.scal(dotv(a, p), p)))
            ok = ok and len(annC) == 1 and rank([combine(annC[0], Tr), line]) == 1
    GA.check("conserved sources: Weyl-flat class sees only the trace", ok)
    return ok


def check_null_flux_is_the_trace_free_channel():
    NK = [vec([F(x) for x in k]) for k in NULLS]
    ok = all(dotv(k, k) == 0 for k in NK)
    rows = [[dotv(k, sym_map(unit(m, 10))(k)) for m in range(10)] for k in NK]
    ker = nullspace(rows, 10)
    ok = ok and len(ker) == 1 and rank(ker + [ID]) == 1
    for pc in [P_TIMELIKE, P_SPACELIKE, P_NULL]:
        p = vec(pc)
        Tr = conserved_basis(p)
        ok = ok and rank(Tr + [ID]) == 7
    GA.check("null fluxes fix T up to the identity; no conserved pure trace at p != 0", ok)
    return ok


def check_minimal_coupling_responses():
    premise("synthesis.imported-maxwell-stress-spacetime-algebra")
    Rm = response(maxwell_density)
    T = lambda a: GA.scal(F(-1, 2), grade(GA.mul(GA.mul(FBV, a, SQ), FBV, SQ), 1))
    cand = [[dotv(E[i], T(ER[j])) for j in range(4)] for i in range(4)]
    ok = Rm == cand and sum(Rm[i][i] for i in range(4)) == 0
    ok = ok and all(Rm[i][j] * ETA[j] == Rm[j][i] * ETA[i] for i in range(4) for j in range(4))
    Rs = response(scalar_density)
    g = vec(GRAD)
    L0 = F(1, 2) * dotv(g, g) - F(1, 2) * M2 * PHI * PHI
    Tc = lambda a: GA.sub(GA.scal(dotv(a, g), g), GA.scal(L0, a))
    cand = [[dotv(E[i], Tc(ER[j])) for j in range(4)] for i in range(4)]
    ok = ok and Rs == cand and sum(Rs[i][i] for i in range(4)) == -dotv(g, g) + 2 * M2 * PHI * PHI
    GA.check("minimal coupling: Maxwell response is -FaF/2, trace zero; scalar response canonical", ok)
    return ok


def check_point_source_coupling_is_universal():
    premise("synthesis.imported-nordstrom-scalar-theory-einstein-fokker-form")
    ps = [(vec(c), s) for c, s in MOMENTA]
    total = GA.add(*[GA.scal(s, p) for p, s in ps])
    ps.append((total, -1))  # fifth momentum, outgoing, closes the balance
    ok = GA.add(*[GA.scal(s, p) for p, s in ps]) == {}
    rows = [[s * dotv(ER[i], p) for p, s in ps] for i in range(4)]
    ker = nullspace(rows, 5)
    ok = ok and len(ker) == 1 and all(x == ker[0][0] for x in ker[0])
    k = vec([F(x) for x in NULLS[6]])
    ok = ok and dotv(total, total) == 5
    ok = ok and dotv(k, sym_map(ID)(k)) == 0 and dotv(ps[1][0], sym_map(ID)(ps[1][0])) == 7
    GA.check("one coupling for all point sources; null momenta decouple from the conformal line", ok)
    return ok


if __name__ == "__main__":
    for fn in [check_linear_curvature_kernels, check_stabiliser_commutant_on_gauge_quotient,
               check_conserved_source_pairing_channels, check_null_flux_is_the_trace_free_channel,
               check_minimal_coupling_responses, check_point_source_coupling_is_universal]:
        print(fn.__name__, fn())
