"""Gravitational pair production from the operator source at first order: exact checks.

Spacetime algebra Cl(1,3), signature (+,-,-,-), exact rational kinematics.

(1) First-order field at momentum p from the stored curvature map R_p[h](B) = -1/2 p ^ h(B.p): the Einstein map
    of h = T - 1/2 id tr T is 1/2 Q(p) T for every conserved source T; its kernel on symmetric maps is the
    4-dimensional displacement space at non-null p and has dimension 6 at null p.
(2) The bilinear B(T1, T2) = <T1, T2> - 1/2 tr T1 tr T2 is the pairing of T1 with T2 - 1/2 id tr T2; for two
    sources at rest it is m1 m2 / 2, so 8 pi G B / Q(k) is the transform of -G m1 m2 / r.
(3) Pair sources: scalars with curvature coupling xi, vectors through T(a) = -1/2 (F1 a F2 + F2 a F1), one
    helicity pair of a massless fermion through the scalar part of a product of four vectors.
(4) All nine channels: the angular integral of the summed squared bracket, with the factor 1/2 for each pair of
    identical quanta, is (pi/180) s^4 (c_i c_j + 5 t_i t_j) with c = 1, 3, 12 and t = (1 - 6 xi)^2 on scalars.
(5) The rate coefficient, the two published values and the stored one.
"""
from fractions import Fraction as F

import GA
from GA import add, dot, gen, mul, scal, sub
from tp_premise import premise

S = GA.sig(1, 3)
ETA = [1, -1, -1, -1]
E = [gen(i) for i in range(4)]
REC = [E[0]] + [GA.neg(x) for x in E[1:]]
I4 = mul(mul(mul(E[0], E[1], S), E[2], S), E[3], S)


def vec(c):
    return {(i,): F(x) for i, x in enumerate(c) if x}


def d(a, b):
    return dot(a, b, S)


def s0(x):
    return x.get((), F(0))


def grade1(x):
    return {b: c for b, c in x.items() if len(b) == 1}


def wedge(a, b):
    return scal(F(1, 2), sub(mul(a, b, S), mul(b, a, S)))


def vdotB(a, B):
    """a . B for a vector a and a bivector B."""
    return grade1(scal(F(1, 2), sub(mul(a, B, S), mul(B, a, S))))


def lin(H):
    """The linear map with matrix H (H[m][n] = e^m . h(e_n))."""
    def h(a):
        out = {}
        for n in range(4):
            an = d(REC[n], a)
            if an:
                for m in range(4):
                    if H[m][n]:
                        out = add(out, scal(an * H[m][n], E[m]))
        return out
    return h


def comp(T):
    """Lower components T_{mn} = e_m . T(e_n) of a linear map."""
    return [[d(E[m], T(E[n])) for n in range(4)] for m in range(4)]


def tr_low(C):
    return sum(ETA[m] * C[m][m] for m in range(4))


def con(A, B):
    return sum(ETA[m] * ETA[n] * A[m][n] * B[m][n] for m in range(4) for n in range(4))


def reduce_(C):
    t = tr_low(C)
    return [[C[m][n] - F(1, 2) * (ETA[m] if m == n else 0) * t for n in range(4)] for m in range(4)]


def bracket(C1, C2):
    """<T1, T2 - 1/2 id tr T2>: the pairing of one source with the reduced other."""
    return con(C1, reduce_(C2))


# ---------------------------------------------------------------------------------------------------------
# (1) the first-order Einstein map at momentum p
# ---------------------------------------------------------------------------------------------------------
def einstein_low(h, p):
    """Lower components of G_p[h] = Ric - 1/2 a R, with R_p[h](B) = -1/2 p ^ h(B.p), Ric(a) = e^b . R(e_b ^ a)."""
    def riem(B):
        return scal(F(-1, 2), wedge(p, h(GA.neg(vdotB(p, B)))))   # B.p = -(p.B)

    def ric(a):
        out = {}
        for b in range(4):
            out = add(out, vdotB(REC[b], riem(wedge(E[b], a))))
        return out
    R = comp(ric)
    sc_ = tr_low(R)
    return [[R[m][n] - F(1, 2) * (ETA[m] if m == n else 0) * sc_ for n in range(4)] for m in range(4)]


def sym_basis():
    out = []
    for m in range(4):
        for n in range(m, 4):
            H = [[F(0)] * 4 for _ in range(4)]
            H[m][n] = F(1)
            H[n][m] = F(1)
            # H is given with lower indices; raise the first for the map
            out.append([[ETA[a] * H[a][b] for b in range(4)] for a in range(4)])
    return out


def conserved(p, seed):
    """A symmetric lower-index source with T(p) = 0: w (x) w summed over vectors w orthogonal to p."""
    pc = [d(REC[m], p) for m in range(4)]            # contravariant components
    ws = []
    for k, row in enumerate(seed):
        w = vec(row)
        if d(p, p) != 0:
            w = sub(w, scal(d(w, p) / d(p, p), p))
        ws.append(w)
    C = [[F(0)] * 4 for _ in range(4)]
    for k, w in enumerate(ws):
        wl = [d(E[m], w) for m in range(4)]
        for m in range(4):
            for n in range(4):
                C[m][n] += (k + 1) * wl[m] * wl[n] * (-1) ** k
    assert all(sum(C[m][n] * pc[n] for n in range(4)) == 0 for m in range(4)) or d(p, p) == 0
    return C


def check_first_order_field_at_non_null_momentum_is_fixed_by_the_source():
    premise("synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel")
    premise("synthesis.imported-einstein-cartan-matter-coupling")
    ok = True
    seeds = [[(1, 2, 0, 1), (0, 1, 3, -1), (2, 0, 1, 1)], [(3, 1, 1, 0), (1, -2, 0, 5), (0, 0, 1, 2)]]
    qs = []
    for pv in [(2, 0, 0, 0), (3, 1, 0, 2), (1, 2, 0, 0), (0, 1, 1, 3)]:
        p = vec(pv)
        Q = d(p, p)
        qs.append(Q)
        ok = ok and Q != 0
        for seed in seeds:
            T = conserved(p, seed)
            Rr = reduce_(T)                                   # T - 1/2 eta tr T, lower indices
            h = lin([[ETA[a] * Rr[a][b] for b in range(4)] for a in range(4)])
            G = einstein_low(h, p)
            ok = ok and all(G[m][n] == F(1, 2) * Q * T[m][n] for m in range(4) for n in range(4))
        rows = []
        for Hm in sym_basis():
            G = einstein_low(lin(Hm), p)
            rows.append([G[m][n] for m in range(4) for n in range(4)])
        ok = ok and GA.mat_rank(rows) == 6                    # kernel 10 - 6 = 4: the displacements
    ok = ok and qs == [4, 4, -3, -11]
    # one case in full: p = 2 e0, T the unit source on e1 (conserved), h = T - 1/2 id tr T = diag(1/2, 1/2, -1/2, -1/2)
    p = vec((2, 0, 0, 0))
    T = [[F(0)] * 4 for _ in range(4)]
    T[1][1] = F(1)                                            # lower components: T(a) = -(a.e1) e1, trace -1
    ok = ok and tr_low(T) == -1
    Rr = reduce_(T)
    ok = ok and [Rr[m][m] for m in range(4)] == [F(1, 2), F(1, 2), F(-1, 2), F(-1, 2)]
    G = einstein_low(lin([[ETA[a] * Rr[a][b] for b in range(4)] for a in range(4)]), p)
    ok = ok and G[1][1] == 2 and all(G[m][n] == 0 for m in range(4) for n in range(4) if (m, n) != (1, 1))
    # a displacement has zero Einstein map: h(a) = (a.p) xi + (a.xi) p
    p = vec((3, 1, 0, 2))
    xi = vec((1, -2, 5, 0))
    disp = comp(lambda a: add(scal(d(a, p), xi), scal(d(a, xi), p)))
    G = einstein_low(lin([[ETA[a] * disp[a][b] for b in range(4)] for a in range(4)]), p)
    ok = ok and all(G[m][n] == 0 for m in range(4) for n in range(4))
    for pv in [(1, 0, 0, 1), (5, 3, 0, 4)]:                   # null momenta
        p = vec(pv)
        ok = ok and d(p, p) == 0
        rows = []
        for Hm in sym_basis():
            G = einstein_low(lin(Hm), p)
            rows.append([G[m][n] for m in range(4) for n in range(4)])
        ok = ok and GA.mat_rank(rows) == 4                    # kernel 6: displacements and two more directions
    GA.check("G_p[T - 1/2 id tr T] = 1/2 Q(p) T for conserved T at four non-null momenta; the Einstein map has "
             "rank 6 (kernel 4) at non-null p and rank 4 (kernel 6) at null p", ok)
    return ok


# ---------------------------------------------------------------------------------------------------------
# (2) normalisation by the static limit
# ---------------------------------------------------------------------------------------------------------
def check_bilinear_is_normalised_by_the_stored_newtonian_coupling():
    premise("field-theory.operator-newtonian-coupling")
    ok = True
    for (m1, m2) in [(F(3), F(5)), (F(7, 2), F(2, 9))]:
        u = E[0]
        T1 = comp(lambda a: scal(m1 * d(a, u), u))
        T2 = comp(lambda a: scal(m2 * d(a, u), u))
        ok = ok and bracket(T1, T2) == m1 * m2 / 2
        ok = ok and bracket(T1, T2) == bracket(T2, T1) == con(T1, T2) - F(1, 2) * tr_low(T1) * tr_low(T2)
        # 8 pi G B / Q(k) with Q(k) = -|k|^2 is -4 pi G m1 m2 / |k|^2, the transform of -G m1 m2 / r
        ok = ok and 8 * bracket(T1, T2) == 4 * m1 * m2
    # without the trace term the static coupling would be twice as large
    T1 = comp(lambda a: scal(d(a, E[0]), E[0]))
    ok = ok and con(T1, T1) == 1 and bracket(T1, T1) == F(1, 2)
    GA.check("B(T1, T2) = <T1, T2 - 1/2 id tr T2> is symmetric and equals m1 m2 / 2 for two sources at rest, so "
             "8 pi G B / Q(k) is the transform of the stored Newtonian coupling", ok)
    return ok


# ---------------------------------------------------------------------------------------------------------
# (3) pair sources
# ---------------------------------------------------------------------------------------------------------
def scalar_low(p, q, xi=F(0)):
    k = add(p, q)
    k2 = d(k, k)
    return comp(lambda a: add(scal(-d(a, q), p), scal(-d(a, p), q), scal(d(p, q), a),
                              scal(2 * xi * d(a, k), k), scal(-2 * xi * k2, a)))


def vector_low(F1, F2):
    def T(a):
        x = add(mul(mul(F1, a, S), F2, S), mul(mul(F2, a, S), F1, S))
        return scal(F(-1, 2), grade1(x))
    return comp(T)


def pols(p, q):
    """Two unit polarisation vectors orthogonal to p and q (momenta in the 1-3 plane, back to back)."""
    pc = [d(REC[m], p) for m in range(4)]
    n = vec([0, pc[3], 0, -pc[1]])
    assert d(n, p) == 0 and d(n, q) == 0 and d(n, n) == -1
    return (n, E[2])


def scalar_pair(p, q, xi=F(0)):
    return ("real", [scalar_low(p, q, xi)])


def vector_pair(p, q):
    return ("real", [vector_low(wedge(p, a1), wedge(q, a2)) for a1 in pols(p, q) for a2 in pols(p, q)])


def weyl_pair(p, q):
    dd = sub(p, q)
    dc = [d(E[m], dd) for m in range(4)]
    XS = [[2 * s0(mul(mul(mul(q, E[m], S), p, S), E[r], S)) for r in range(4)] for m in range(4)]
    XA = [[2 * s0(mul(mul(mul(mul(q, E[m], S), p, S), E[r], S), I4, S)) for r in range(4)] for m in range(4)]
    return ("weyl", dc, XS, XA)


def sumsq(src1, src2, sign=1):
    """Sum over polarisations of the squared bracket of two pair sources."""
    if src1[0] == "real" and src2[0] == "real":
        return sum(con(T1, reduce_(T2)) ** 2 for T1 in src1[1] for T2 in src2[1])
    if src1[0] == "real":
        return sumsq(src2, src1)
    _, d1, S1, A1 = src1
    if src2[0] == "real":
        tot = F(0)
        for T2 in src2[1]:
            R = reduce_(T2)
            w = [sum(R[m][n] * ETA[n] * d1[n] for n in range(4)) for m in range(4)]
            tot += F(1, 4) * sum(ETA[m] * ETA[r] * w[m] * w[r] * S1[m][r] for m in range(4) for r in range(4))
        return tot
    _, d2, S2, A2 = src2
    d1d2 = sum(ETA[m] * d1[m] * d2[m] for m in range(4))
    d1u = [ETA[m] * d1[m] for m in range(4)]
    d2u = [ETA[m] * d2[m] for m in range(4)]
    Cm = [[d1d2 * (ETA[m] if m == a else 0) + d2u[m] * d1u[a] for a in range(4)] for m in range(4)]

    def quad(X1, X2):
        tot = F(0)
        for m in range(4):
            for a in range(4):
                if Cm[m][a]:
                    for r in range(4):
                        for b in range(4):
                            if Cm[r][b]:
                                tot += Cm[m][a] * Cm[r][b] * X1[m][r] * X2[a][b]
        return tot
    return F(1, 64) * (quad(S1, S2) - sign * quad(A1, A2))


def kin(c, sn):
    return vec([1, 0, 0, 1]), vec([1, 0, 0, -1]), vec([1, sn, 0, c]), vec([1, -sn, 0, -c])


POINTS = [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(-7, 25), F(24, 25)), (F(-8, 17), F(15, 17)),
          (F(20, 29), F(21, 29)), (F(-12, 37), F(35, 37)), (F(9, 41), F(40, 41))]


def check_pair_sources_and_their_brackets():
    premise("synthesis.imported-maxwell-stress-spacetime-algebra")
    premise("synthesis.electron-positron-to-muon-pairs-in-the-spacetime-algebra-lsz-tree-cross-section-and-one-loop-unitarity")
    ok = True
    for (c, sn) in POINTS[:4]:
        p1, p2, p3, p4 = kin(c, sn)
        s = d(add(p1, p2), add(p1, p2))
        t = d(sub(p1, p3), sub(p1, p3))
        u = d(sub(p1, p4), sub(p1, p4))
        ok = ok and s == 4 and s + t + u == 0
        # scalars: bracket -tu at xi = 0; spin-two and trace parts for general xi
        ok = ok and bracket(scalar_low(p1, p2), scalar_low(p3, p4)) == -t * u
        for (x1, x2) in [(F(1, 7), F(2, 5)), (F(1, 6), F(0)), (F(1, 6), F(1, 6))]:
            want = (s * s / 4) * (c * c - F(1, 3)) - (s * s / 6) * (1 - 6 * x1) * (1 - 6 * x2)
            ok = ok and bracket(scalar_low(p1, p2, x1), scalar_low(p3, p4, x2)) == want
        ok = ok and tr_low(scalar_low(p1, p2, F(1, 6))) == 0 and tr_low(scalar_low(p1, p2)) == s
        # vectors: trace-free, conserved, and the sum over linear polarisations of the squared bracket is 2 t^2 u^2
        vp = vector_pair(p1, p2)
        k = add(p1, p2)
        kc = [d(REC[m], k) for m in range(4)]
        ok = ok and all(tr_low(T) == 0 for T in vp[1])
        ok = ok and all(sum(T[m][n] * kc[n] for n in range(4)) == 0 for T in vp[1] for m in range(4))
        ok = ok and sumsq(vp, scalar_pair(p3, p4)) == 2 * t * t * u * u
        # one helicity pair of a massless fermion against a scalar pair: (t - u)^2 t u / 4
        ok = ok and sumsq(weyl_pair(p1, p2), scalar_pair(p3, p4)) == (t - u) ** 2 * t * u / 4
        # the spin sum as a scalar part: 2 <p2 w p1 w>_0 = 4 (p1.w)(p2.w) - 2 Q(w) p1.p2
        w = vec([2, 1, -1, 3])
        lhs = 2 * s0(mul(mul(mul(p2, w, S), p1, S), w, S))
        ok = ok and lhs == 4 * d(p1, w) * d(p2, w) - 2 * d(w, w) * d(p1, p2)
    GA.check("pair sources: scalar bracket -tu and its spin-two and trace parts for three pairs of curvature "
             "couplings; vector sources trace-free and conserved with summed square 2 t^2 u^2; one helicity pair "
             "of a massless fermion gives (t-u)^2 tu / 4 (four configurations)", ok)
    return ok


# ---------------------------------------------------------------------------------------------------------
# (4) the nine channels
# ---------------------------------------------------------------------------------------------------------
def fit_and_integrate(vals):
    """Fit a polynomial in c through the points and integrate it over [-1, 1]."""
    n = len(vals)
    M = [[c ** k for k in range(n)] for c, _ in vals]
    rhs = [v for _, v in vals]
    for i in range(n):
        piv = next(r for r in range(i, n) if M[r][i] != 0)
        M[i], M[piv] = M[piv], M[i]
        rhs[i], rhs[piv] = rhs[piv], rhs[i]
        for r in range(n):
            if r != i and M[r][i] != 0:
                f = M[r][i] / M[i][i]
                M[r] = [a - f * b for a, b in zip(M[r], M[i])]
                rhs[r] -= f * rhs[i]
    co = [rhs[i] / M[i][i] for i in range(n)]
    return co, sum(co[k] * F(2, k + 1) for k in range(0, n, 2))


KINDS = {"s": scalar_pair, "w": weyl_pair, "v": vector_pair}
CW = {"s": 1, "w": 3, "v": 12}
SYM = {"s": F(1, 2), "w": F(1), "v": F(1, 2)}


def channel_weight(a, b, sign=1):
    """W / pi: the integral over the sphere of the summed squared bracket over s^4, with the identical-quanta factors."""
    vals = []
    for (c, sn) in POINTS:
        p1, p2, p3, p4 = kin(c, sn)
        vals.append((c, sumsq(KINDS[a](p1, p2), KINDS[b](p3, p4), sign) / F(4) ** 4))
    co, integ = fit_and_integrate(vals)
    return co, 2 * integ * SYM[a] * SYM[b]


def check_channel_weights_are_products_of_the_spin_two_weights():
    premise("synthesis.electron-positron-to-muon-pairs-in-the-spacetime-algebra-lsz-tree-cross-section-and-one-loop-unitarity")
    ok = True
    for a in "swv":
        for b in "swv":
            for sign in ((1, -1) if a == b == "w" else (1,)):
                co, W = channel_weight(a, b, sign)
                ok = ok and all(x == 0 for x in co[5:])                   # degree four in the cosine
                ok = ok and W == F(CW[a] * CW[b] + (5 if a == b == "s" else 0), 180)
    # the two helicity arrangements of fermion to fermion: ((1 -+ c)(2c +- 1))^2 / 64
    co_p, _ = channel_weight("w", "w", 1)
    co_m, _ = channel_weight("w", "w", -1)
    ok = ok and co_p[:5] == [F(1, 64), F(1, 32), F(-3, 64), F(-1, 16), F(1, 16)]
    ok = ok and co_m[:5] == [F(1, 64), F(-1, 32), F(-3, 64), F(1, 16), F(1, 16)]
    # conformally coupled scalars: only the spin-two part is left
    vals = []
    for (c, sn) in POINTS:
        p1, p2, p3, p4 = kin(c, sn)
        vals.append((c, sumsq(scalar_pair(p1, p2, F(1, 6)), scalar_pair(p3, p4)) / F(4) ** 4))
    _, integ = fit_and_integrate(vals)
    ok = ok and 2 * integ * F(1, 4) == F(1, 180)
    GA.check("nine channels: W = (pi/180)(c_i c_j + 5 on scalar to scalar) with c = 1, 3, 12, both helicity "
             "arrangements of fermion to fermion included; a conformally coupled scalar keeps the spin-two part only", ok)
    return ok


# ---------------------------------------------------------------------------------------------------------
# (5) the rate coefficient and the published values
# ---------------------------------------------------------------------------------------------------------
def coefficient(cj, tj, n_s, n_w, n_v, t_bath=1, fermion_weight=3):
    """alpha / pi^3 in  Gamma = alpha T^8 / Mbar^4, for a produced species of spin-two weight cj and trace weight tj."""
    bose = F(6, 90)                  # Gamma(4) zeta(4) / pi^4 = 1/15
    fermi = bose * (1 - F(1, 8))     # (1 - 2^-3)/15 = 7/120
    c_b = n_s * 1 + n_v * 12
    c_f = n_w * fermion_weight
    sum_b = F(cj * c_b + 5 * tj * n_s * t_bath, 180)
    sum_f = F(cj * c_f, 180)
    phase = F(32, 3) / 1024          # from the two-body phase spaces and the angle between the incoming momenta
    return phase * (bose * bose * sum_b + fermi * fermi * sum_f)


def check_rate_coefficients_and_the_published_values():
    ok = True
    # the weights used below are the computed channel weights, not constants: W(a, scalar) for a = s, w, v
    ws = {a: channel_weight(a, "s")[1] for a in "swv"}
    ok = ok and ws == {"s": F(CW["s"] + 5, 180), "w": F(CW["w"], 180), "v": F(CW["v"], 180)}
    bose, fermi = F(1, 15), F(7, 120)
    direct = F(32, 3) / 1024 * (bose * bose * (4 * ws["s"] + 12 * ws["v"]) + fermi * fermi * 45 * ws["w"])
    ok = ok and direct == F(5789, 82944000)
    ok = ok and F(6, 90) == F(1, 15) and F(6, 90) * (1 - F(1, 8)) == F(7, 120)
    # integral over the angle between the incoming momenta of s^2 = (2 E1 E2 (1 - x))^2: 32/3 (E1 E2)^2
    ok = ok and 4 * F(8, 3) == F(32, 3)
    scalar = coefficient(1, 1, 4, 45, 12)
    weyl = coefficient(3, 0, 4, 45, 12)
    dirac = coefficient(6, 0, 4, 45, 12)
    vector = coefficient(12, 0, 4, 45, 12)
    ok = ok and scalar == F(5789, 82944000)
    ok = ok and weyl == F(16087, 82944000)
    ok = ok and dirac == 2 * weyl and vector == 4 * weyl
    # closed form of the general coefficient
    for (cj, tj, n_s, n_w, n_v) in [(1, 1, 4, 45, 12), (3, 0, 8, 48, 12), (12, 0, 4, 45, 12), (1, 1, 8, 48, 12)]:
        closed = (F(cj * (n_s + 12 * n_v) + 5 * tj * n_s, 225) + F(49 * cj * 3 * n_w, 14400)) / 17280
        ok = ok and coefficient(cj, tj, n_s, n_w, n_v) == closed
    # the later published values follow with each of the 45 fermions given the weight of a Dirac fermion
    ok = ok and coefficient(1, 1, 4, 45, 12, fermion_weight=6) == F(3997, 41472000)
    ok = ok and coefficient(6, 0, 4, 45, 12, fermion_weight=6) == F(11351, 20736000)
    # the earlier source's squared amplitudes (1/16, 1/32, 1/8 of t^2u^2, tu(t-u)^2, t^2u^2, no symmetry factors,
    # fermion summed over both helicities) against the canonical ones (1, 1/2, 2): one sixteenth each
    ok = ok and [F(1, 16) / 1, F(1, 32) / F(1, 2), F(1, 8) / 2] == [F(1, 16)] * 3
    stored = F(3997, 663552000)
    ok = ok and coefficient(1, 1, 4, 45, 12, fermion_weight=6) / 16 == stored
    ok = ok and scalar / stored == F(46312, 3997)
    # conformally coupled scalars on either side lose the trace term
    ok = ok and coefficient(1, 0, 4, 45, 12) == scalar - F(20, 225) / 17280
    # the total over a produced copy of the same content (the mirror)
    total = 4 * scalar + 45 * weyl + 12 * vector
    ok = ok and total == (F(283 * 148 + 80, 225) + F(49 * 283 * 135, 14400)) / 17280 == F(1519247, 82944000)
    GA.check("rate coefficients over pi^3: scalar 5789/82944000 from four scalars, 45 Weyl fermions and twelve "
             "vectors; 3997/41472000 and 11351/20736000 with Dirac weights; the stored 3997/663552000 is one "
             "sixteenth of the first of these", ok)
    return ok
