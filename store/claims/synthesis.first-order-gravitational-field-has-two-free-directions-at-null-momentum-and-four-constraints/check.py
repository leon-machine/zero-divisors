"""The first-order gravitational field by channel: free directions at null momentum, constraints, and tests.

Stored first-order curvature (Cl(1,3), signature (+,-,-,-)): R_k[h](B) = -1/2 k ^ h(B.k), Ricci map
Ric(a) = sum_b e^b . R(e_b ^ a), Einstein map G = Ric - 1/2 id tr Ric, on symmetric maps h (ten dimensions).
A symmetric map is held as a matrix H with h(a) = sum H[m][n] (a.e_m) e_n.

(i)   kernel at null k: {h : h(k) = 1/2 tr(h) k} = displacements + the two transverse trace-free maps;
(ii)  the Einstein map is symmetric for the pairing; its image at null k is the conserved sources that pair to
      zero with the two transverse trace-free maps;
(iii) for a conserved source at null k, T - 1/2 id tr T minus its transverse trace-free part is a displacement;
(iv)  on conserved sources at null k the bilinear B is the sum of the two squared pairings;
(v)   the components of the Einstein map along e_0 carry no second power of the frequency;
(vi)  the curvatures of the two free directions are exchanged by the pseudoscalar;
(vii) the static coupling does not separate the trace-free channel from the trace; pair production does;
(viii) the burst ratio under the options for the gravitational term.
"""
from fractions import Fraction as F

import GA
from GA import add, gen, mul, scal, sub
from tp_premise import premise

# ---------------------------------------------------------------------------------------------------------
# sample momenta and frames (module level)
# ---------------------------------------------------------------------------------------------------------
TIMELIKE = [(2, 0, 0, 0), (3, 1, 0, 2)]
SPACELIKE = [(1, 2, 0, 0), (0, 1, 1, 3)]
# null momenta with two unit spacelike vectors orthogonal to k, to e_0 and to each other, and the handedness
# of (m1, m2, spatial momentum divided by the frequency)
NULLS = [((1, 0, 0, 1), [(0, 1, 0, 0), (0, 0, 1, 0)], 1),
         ((5, 3, 0, 4), [(0, 0, 1, 0), (0, F(4, 5), 0, F(-3, 5))], -1),
         ((-5, 3, 0, 4), [(0, 0, 1, 0), (0, F(4, 5), 0, F(-3, 5))], 1)]
NULL3 = [((1, 0, 1), [(0, 1, 0)]), ((5, 3, 4), [(0, F(4, 5), F(-3, 5))])]
NULL5 = [((1, 0, 0, 0, 1), [(0, 1, 0, 0, 0), (0, 0, 1, 0, 0), (0, 0, 0, 1, 0)])]
KAPPA = (3, 0, 4)                      # spatial momentum of the frequency scan
FREQS = [0, 1, 2, 3, 4]
STATIC_K = (0, 1, 2, 2)
PAIR = ((5, 0, 0, 5), (5, 0, 0, -5), (5, 3, 0, 4), (5, -3, 0, -4))     # p1, p2 -> p3, p4, all null


class ST:
    """Cl(1, d-1): vectors, symmetric maps as matrices, the stored first-order curvature and its Einstein map."""

    def __init__(self, d):
        self.d = d
        self.S = GA.sig(1, d - 1)
        self.eta = [1] + [-1] * (d - 1)
        self.e = [gen(i) for i in range(d)]
        self.rec = [scal(self.eta[i], self.e[i]) for i in range(d)]

    def vec(self, comps):
        return {(i,): F(c) for i, c in enumerate(comps) if c}

    def dot(self, a, b):
        return GA.dot(a, b, self.S)

    def g1(self, x):
        return {b: c for b, c in x.items() if len(b) == 1}

    def wedge(self, a, b):
        return scal(F(1, 2), sub(mul(a, b, self.S), mul(b, a, self.S)))

    def vdotB(self, a, B):
        return self.g1(scal(F(1, 2), sub(mul(a, B, self.S), mul(B, a, self.S))))

    def apply(self, H, a):
        out = {}
        for m in range(self.d):
            am = self.dot(a, self.e[m])
            if am == 0:
                continue
            for n in range(self.d):
                if H[m][n]:
                    out = add(out, scal(am * H[m][n], self.e[n]))
        return out

    def riem(self, H, k, B):
        return scal(F(-1, 2), self.wedge(k, self.apply(H, GA.neg(self.vdotB(k, B)))))

    def einstein(self, H, k):
        R = [[F(0)] * self.d for _ in range(self.d)]
        for m in range(self.d):
            img = {}
            for b in range(self.d):
                img = add(img, self.vdotB(self.rec[b], self.riem(H, k, self.wedge(self.e[b], self.rec[m]))))
            for n in range(self.d):
                R[m][n] = self.dot(img, self.rec[n])
        t = self.trace(R)
        return [[R[m][n] - (F(1, 2) * t * self.eta[m] if m == n else 0) for n in range(self.d)]
                for m in range(self.d)]

    def trace(self, M):
        return sum(self.eta[a] * M[a][a] for a in range(self.d))

    def idmat(self):
        return [[F(self.eta[m]) if m == n else F(0) for n in range(self.d)] for m in range(self.d)]

    def pair(self, A, B):
        return sum(self.eta[a] * self.eta[n] * A[a][n] * B[a][n] for a in range(self.d) for n in range(self.d))

    def outer(self, x, y):
        """the symmetric map a -> (a.x) y + (a.y) x."""
        return [[F(x[m]) * F(y[n]) + F(y[m]) * F(x[n]) for n in range(self.d)] for m in range(self.d)]

    def sym_basis(self):
        out = []
        for m in range(self.d):
            for n in range(m, self.d):
                H = [[F(0)] * self.d for _ in range(self.d)]
                H[m][n] = F(1)
                H[n][m] = F(1)
                out.append(H)
        return out

    def flat(self, M):
        return [M[m][n] for m in range(self.d) for n in range(self.d)]

    def Q(self, kc):
        return sum(self.eta[i] * F(kc[i]) ** 2 for i in range(self.d))

    def mdot(self, x, y):
        return sum(self.eta[i] * F(x[i]) * F(y[i]) for i in range(self.d))


def madd(A, B, c=1):
    return [[A[m][n] + c * B[m][n] for n in range(len(A))] for m in range(len(A))]


def mscal(c, A):
    return [[c * x for x in row] for row in A]


def rank(rows):
    return GA.mat_rank([list(r) for r in rows]) if rows else 0


def displacements(st, kc):
    return [st.outer(kc, [1 if i == j else 0 for i in range(st.d)]) for j in range(st.d)]


def tt_maps(st, trans):
    """the transverse trace-free maps built on the orthonormal transverse vectors trans."""
    out = []
    n = len(trans)
    for i in range(n):
        for j in range(i + 1, n):
            out.append(st.outer(trans[i], trans[j]))
    for i in range(1, n):
        out.append(madd(mscal(F(1, 2), st.outer(trans[0], trans[0])), mscal(F(1, 2), st.outer(trans[i], trans[i])), -1))
    return out


def kernel_data(d, kc, trans):
    st = ST(d)
    k = st.vec(kc)
    basis = st.sym_basis()
    G = [st.einstein(H, k) for H in basis]
    disp = displacements(st, kc)
    tt = tt_maps(st, trans) if trans else []
    cond = []
    for H in basis:
        v = sub(st.apply(H, k), scal(F(1, 2) * st.trace(H), k))
        cond.append([st.dot(v, st.rec[i]) for i in range(d)])
    return dict(
        nsym=len(basis),
        rank=rank([st.flat(g) for g in G]),
        disp_rank=rank([st.flat(M) for M in disp]),
        disp_in_kernel=all(all(x == 0 for x in st.flat(st.einstein(M, k))) for M in disp),
        ntt=len(tt),
        tt_in_kernel=all(all(x == 0 for x in st.flat(st.einstein(M, k))) for M in tt),
        span_rank=rank([st.flat(M) for M in disp + tt]),
        cond_rank=rank(cond),
        cond_stacked_rank=rank([cond[i] + st.flat(G[i]) for i in range(len(basis))]),
        image_conserved=all(GA.is_zero(st.apply(g, k)) for g in G),
        image_perp_tt=all(st.pair(g, n) == 0 for g in G for n in tt),
        symmetric=all(st.pair(basis[i], G[j]) == st.pair(basis[j], G[i])
                      for i in range(len(basis)) for j in range(len(basis))),
        Q=st.Q(kc))


def conserved_basis(st, kc):
    basis = st.sym_basis()
    k = st.vec(kc)
    rows = []
    for H in basis:
        img = st.apply(H, k)
        rows.append([st.dot(img, st.rec[i]) for i in range(st.d)])
    A = [[rows[i][j] for i in range(len(basis))] for j in range(st.d)]
    out = []
    for c in GA.field_kernel(A):
        T = [[F(0)] * st.d for _ in range(st.d)]
        for ci, H in zip(c, basis):
            T = madd(T, mscal(F(ci), H))
        out.append(T)
    return out


def tt_project(st, T, tt):
    out = [[F(0)] * st.d for _ in range(st.d)]
    for n in tt:
        out = madd(out, mscal(st.pair(T, n) / st.pair(n, n), n))
    return out


def bform(st, T1, T2):
    return st.pair(T1, T2) - F(1, 2) * st.trace(T1) * st.trace(T2)


def poly_degree(vals):
    d, deg, n = list(vals), -1, 0
    while d:
        if any(x != 0 for x in d):
            deg = n
        d = [d[i + 1] - d[i] for i in range(len(d) - 1)]
        n += 1
    return deg


def channels(st, T1, T2, kc):
    """(trace-free part, trace part, B, trace-only bilinear normalised to the Newtonian coupling)."""
    q = st.Q(kc)
    th = madd(st.idmat(), mscal(F(1, 2) / q, st.outer(kc, kc)), -1)
    t1, t2 = st.trace(T1), st.trace(T2)
    tf1, tf2 = madd(T1, mscal(t1 / 3, th), -1), madd(T2, mscal(t2 / 3, th), -1)
    return st.pair(tf1, tf2), -t1 * t2 / 6, bform(st, T1, T2), F(1, 2) * t1 * t2


def scalar_pair(st, p1, p2, xi):
    kc = [a + b for a, b in zip(p1, p2)]
    T = madd(mscal(st.mdot(p1, p2), st.idmat()), st.outer(p1, p2), -1)
    imp = madd(mscal(F(1, 2), st.outer(kc, kc)), mscal(st.Q(kc), st.idmat()), -1)
    return madd(T, mscal(2 * xi, imp)), kc


# ---------------------------------------------------------------------------------------------------------
# checks
# ---------------------------------------------------------------------------------------------------------
def check_kernel_at_null_momentum_is_displacements_plus_two_transverse_trace_free_maps():
    premise("synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel")
    premise("synthesis.gravitational-pair-production-from-the-operator-source-at-first-order")
    ok = True
    for kc in TIMELIKE + SPACELIKE:
        r = kernel_data(4, kc, None)
        ok = ok and r["Q"] != 0 and r["nsym"] - r["rank"] == 4 and r["disp_rank"] == 4 and r["disp_in_kernel"]
    for kc, trans, _ in NULLS:
        r = kernel_data(4, kc, trans)
        ok = ok and r["Q"] == 0 and r["nsym"] == 10 and r["rank"] == 4
        ok = ok and r["disp_in_kernel"] and r["tt_in_kernel"] and r["ntt"] == 2 and r["span_rank"] == 6
        # the kernel is cut out by h(k) = 1/2 tr(h) k: four independent conditions with the same kernel
        ok = ok and r["cond_rank"] == 4 and r["cond_stacked_rank"] == 4
    # controls: three dimensions have no free direction, five dimensions have five
    for kc, trans in NULL3:
        r = kernel_data(3, kc, trans)
        ok = ok and r["Q"] == 0 and r["nsym"] - r["rank"] == 3 and r["disp_rank"] == 3 and r["ntt"] == 0
    for kc, trans in NULL5:
        r = kernel_data(5, kc, trans)
        ok = ok and r["Q"] == 0 and r["nsym"] - r["rank"] == 10 and r["ntt"] == 5 and r["span_rank"] == 10
        ok = ok and r["tt_in_kernel"]
    GA.check("kernel of the first-order Einstein map: displacements at four non-null momenta; displacements plus the "
             "two transverse trace-free maps at three null momenta, cut out by h(k) = tr(h) k / 2; no free direction "
             "in Cl(1,2), five in Cl(1,4)", ok)
    return ok


def check_image_at_null_momentum_is_the_sources_without_transverse_trace_free_part():
    premise("synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel")
    ok = True
    st = ST(4)
    for kc in TIMELIKE + SPACELIKE:
        ok = ok and kernel_data(4, kc, None)["symmetric"]
    for kc, trans, _ in NULLS:
        r = kernel_data(4, kc, trans)
        ok = ok and r["symmetric"] and r["image_conserved"] and r["image_perp_tt"]
        # conserved sources have dimension 6; two conditions leave 4, the rank of the map
        ok = ok and len(conserved_basis(st, kc)) == 6 and r["rank"] == 6 - 2
    GA.check("the Einstein map is symmetric for the pairing at seven momenta; at null momentum its image is conserved, "
             "pairs to zero with the two transverse trace-free maps, and has the dimension 4 of that space", ok)
    return ok


def check_pole_at_the_null_cone_is_in_the_transverse_trace_free_part():
    premise("synthesis.gravitational-pair-production-from-the-operator-source-at-first-order")
    ok = True
    st = ST(4)
    for kc, trans, _ in NULLS:
        k = st.vec(kc)
        cb = conserved_basis(st, kc)
        tt = tt_maps(st, trans)
        disp = displacements(st, kc)
        for T in cb:
            x = madd(madd(T, mscal(F(1, 2) * st.trace(T), st.idmat()), -1), tt_project(st, T, tt), -1)
            ok = ok and rank([st.flat(M) for M in disp + [x]]) == 4
            ok = ok and all(GA.is_zero(st.riem(x, k, st.wedge(st.e[a], st.e[b])))
                            for a in range(4) for b in range(a + 1, 4))
        # B on conserved sources at null k is the sum of the squared pairings with the two maps, each of norm 2
        ok = ok and all(st.pair(n, n) == 2 for n in tt)
        ok = ok and all(bform(st, a, b) == sum(st.pair(a, n) * st.pair(b, n) / 2 for n in tt) for a in cb for b in cb)
        ok = ok and GA.congruence_signature([[bform(st, a, b) for b in cb] for a in cb]) == (2, 0, 4)
    for kc in TIMELIKE:
        cb = conserved_basis(st, kc)
        ok = ok and GA.congruence_signature([[bform(st, a, b) for b in cb] for a in cb]) == (5, 1, 0)
    for kc in SPACELIKE:
        cb = conserved_basis(st, kc)
        ok = ok and GA.congruence_signature([[bform(st, a, b) for b in cb] for a in cb]) == (3, 3, 0)
    GA.check("at null momentum T - id tr T / 2 minus the transverse trace-free part of a conserved source is a "
             "displacement with zero curvature, and B is the sum of two squares (signature (2,0), radical 4); "
             "B has signature (5,1) at timelike and (3,3) at spacelike momentum", ok)
    return ok


def check_constraint_components_carry_no_second_power_of_the_frequency():
    premise("synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel")
    st = ST(4)
    degs = {}
    for H in st.sym_basis():
        Es = [st.einstein(H, st.vec((w,) + KAPPA)) for w in FREQS]
        for m in range(4):
            for n in range(m, 4):
                key = "tt" if m + n == 0 else ("ts" if m == 0 else "ss")
                degs[key] = max(degs.get(key, -1), poly_degree([E[m][n] for E in Es]))
    ok = degs == {"tt": 0, "ts": 1, "ss": 2}
    GA.check("components of the first-order Einstein map against the frequency, on the ten symmetric maps: degree 0 "
             "along e_0 e_0, degree 1 along e_0 e_i, degree 2 on the spatial ones", ok)
    return ok


def check_free_directions_are_exchanged_by_the_pseudoscalar():
    premise("field-theory.fock-space-maxwell-modes")
    ok = True
    st = ST(4)
    I4 = {(0, 1, 2, 3): F(1)}
    ok = ok and GA.eq(mul(I4, I4, st.S), GA.sc(-1))
    for kc, trans, hand in NULLS:
        k = st.vec(kc)
        ncross, nplus = tt_maps(st, trans)
        seen = 0
        for a in range(4):
            for b in range(a + 1, 4):
                B = st.wedge(st.e[a], st.e[b])
                Rp, Rc = st.riem(nplus, k, B), st.riem(ncross, k, B)
                ok = ok and GA.eq(mul(I4, Rp, st.S), scal(-hand, Rc))
                ok = ok and GA.eq(mul(I4, Rc, st.S), scal(hand, Rp))
                ok = ok and GA.eq(st.riem(nplus, k, mul(I4, B, st.S)), mul(I4, Rp, st.S))
                seen += 0 if GA.is_zero(Rp) else 1
        ok = ok and seen >= 4
    GA.check("I4 R[n+] = -(handedness) R[nx] and I4 R[nx] = (handedness) R[n+] on all six bivectors at three null "
             "momenta, with R[n](I4 B) = I4 R[n](B); the curvature is nonzero on at least four of the six", ok)
    return ok


def check_static_coupling_does_not_separate_the_channels_and_pair_production_does():
    premise("field-theory.operator-newtonian-coupling")
    premise("synthesis.gravitational-pair-production-from-the-operator-source-at-first-order")
    ok = True
    st = ST(4)
    e0 = (1, 0, 0, 0)
    T1, T2 = mscal(F(7, 2), st.outer(e0, e0)), mscal(F(3, 2), st.outer(e0, e0))      # bodies of mass 7 and 3
    tf, trc, b, bn = channels(st, T1, T2, STATIC_K)
    ok = ok and tf == F(2, 3) * 21 and trc == F(-1, 6) * 21 and b == F(1, 2) * 21 and bn == b
    p1, p2, p3, p4 = PAIR
    Ta, kc = scalar_pair(st, p1, p2, F(0))
    Tb, _ = scalar_pair(st, p3, p4, F(0))
    s = st.Q(kc)
    t = st.Q([x - y for x, y in zip(p1, p3)])
    u = st.Q([x - y for x, y in zip(p1, p4)])
    ok = ok and (s, t, u) == (100, -10, -90) and GA.is_zero(st.apply(Ta, st.vec(kc)))
    tf, trc, b, bn = channels(st, Ta, Tb, kc)
    ok = ok and b == -t * u and trc == -s * s / 6 and bn == s * s / 2 and tf + trc == b
    # a conformally coupled pair is trace-free: the trace-only bilinear vanishes, the bracket does not
    Tc, _ = scalar_pair(st, p1, p2, F(1, 6))
    tf2, trc2, b2, bn2 = channels(st, Tc, Tb, kc)
    ok = ok and st.trace(Tc) == 0 and bn2 == 0 and trc2 == 0 and b2 == tf and b2 != 0
    # channel weights in units of pi/180: the stored trace term is 5 tau tau; the trace-only one, normalised to the
    # same Newtonian coupling, is 9 times that: 4 pi (1/2)^2 (1/4) = pi/4 = 45 pi/180 against 4 pi (1/6)^2 (1/4)
    w_trace_only = 4 * F(1, 2) ** 2 * F(1, 4) * 180
    w_stored_trace = 4 * F(1, 6) ** 2 * F(1, 4) * 180
    ok = ok and w_trace_only == 45 and w_stored_trace == 5

    def alpha(cj, tauj, ns, nw, nv, sumtau, wtr, spin_two):
        """rate coefficient over pi^3, from the stored closed form; spin_two = 0 switches the trace-free channel off."""
        return (spin_two * cj * (ns + 12 * nv) + wtr * tauj * sumtau) / F(225 * 17280) + spin_two * 49 * cj * nw / F(4800 * 17280)
    stored_scalar = alpha(1, 1, 4, 45, 12, 4, 5, 1)
    stored_total = 4 * stored_scalar + 45 * alpha(3, 0, 4, 45, 12, 4, 5, 1) + 12 * alpha(12, 0, 4, 45, 12, 4, 5, 1)
    ok = ok and stored_scalar == F(5789, 82944000) and stored_total == F(1519247, 82944000)
    only_scalar = alpha(1, 1, 4, 45, 12, 4, 45, 0)
    only_total = 4 * only_scalar + 45 * alpha(3, 0, 4, 45, 12, 4, 45, 0) + 12 * alpha(12, 0, 4, 45, 12, 4, 45, 0)
    ok = ok and only_scalar == F(1, 21600) and only_total == F(1, 5400)
    ok = ok and only_scalar / stored_scalar == F(3840, 5789) and only_total / stored_total == F(15360, 1519247)
    ok = ok and F(1, 100) < only_total / stored_total < F(11, 1000)
    GA.check("static bodies: trace-free part 2/3, trace part -1/6, B = 1/2 of m1 m2, equal to the trace-only bilinear; "
             "scalar pairs: B = -tu against s^2/2; a conformally coupled pair has zero trace-only bilinear; with the "
             "trace-only bilinear the rate of a copy of the Standard Model's content is 15360/1519247 of the stored one", ok)
    return ok


def check_burst_ratio_under_the_options_for_the_gravitational_term():
    premise("synthesis.dimmed-burst-time-rescaled-copy")

    def ratio(g_hole, g_standard, o):
        return (2 + g_hole + o) / (1 + g_standard)
    g = F(2, 98)                 # gravitons 2 percent of the power of a hole emitting neutrinos, photons and gravitons
    ok = True
    ok = ok and ratio(g, g, 0) == F(99, 50)            # the free part emits as in standard physics
    ok = ok and ratio(0, g, 0) == F(49, 25)            # no emission into the two components; standard baseline kept
    ok = ok and ratio(0, 0, 0) == 2                    # the stored parenthesis: baseline redefined without gravitons
    ok = ok and ratio(g, g, 0) - ratio(0, g, 0) == g / (1 + g) == F(1, 50)
    ok = ok and all(ratio(g, g, o) - ratio(0, g, o) == F(1, 50) for o in (F(1, 3), F(2), F(7, 2)))
    GA.check("burst ratio (2 + g_hole + o)/(1 + g_standard) at g = 2/98, o = 0: 99/50 with the gravitational term, "
             "49/25 without it against the standard baseline, 2 with the baseline redefined; the two options differ by "
             "g/(1 + g) = 1/50 for every o", ok)
    return ok
