"""A field slaved to an operator source, and the free part that restores commutation at spacelike separation.

Matter: one quantum on two paths, in the algebra of a completed pair Cl(1,1) (e1^2 = 1, e2^2 = -1): v, w null with
vw + wv = 1, path projectors P1 = vw, P2 = wv, source J = c1 P1 + c2 P2, recombiner U = p + q e2 (p^2 + q^2 = 1),
detection O = U^-1 P1 U.

Field: a scalar on a line of sites with the exact light cone, phi_n(t+1) = phi_{n+1}(t) + phi_{n-1}(t) - phi_n(t-1),
sourced at site 0 at the times t' = 0..5; all coefficients integers.

(1) The matter factor [J, O] = (c1 - c2) p q (e2 - 2 p q e1e2 ... ) is nonzero exactly when c1 != c2 and p q != 0.
(2) The free field keeps its commutation form; the retarded response G equals minus the commutator function for
    t > t' and vanishes for t <= t' (Kubo), and is supported in the forward cone.
(3) Slaved field, phi = g J sum G: its commutator with O is -g [J, O] sum_t' G, nonzero at events spacelike to the
    detection event (0, 8).
(4) With the free part, the first-order commutator is -g [J, O] sum_t' (G + Delta): zero at every spacelike event
    of the grid, supported in the past cones of the source events, nonzero at timelike events.
(5) The Einstein map of the stored first-order curvature R_k[h](B) = -1/2 k ^ h(B.k) on symmetric maps: rank 6 at
    non-null momenta (kernel: the four displacements), rank 4 at null momenta (kernel of dimension six).
"""
from fractions import Fraction as F

import GA
from GA import add, gen, mul, scal, sc, sub
from tp_premise import premise

S11 = GA.sig(1, 1)
L, TMAX = 40, 18
N = 2 * L + 1
KICKS = list(range(0, 6))
TDET = 8
WINDOW = range(-18, 19)


def idx(n):
    return n + L


# ---------------------------------------------------------------------------------------------------------
# matter
# ---------------------------------------------------------------------------------------------------------
def matter(c1, c2, p, q):
    e1, e2 = gen(0), gen(1)
    v = scal(F(1, 2), add(e1, e2))
    w = scal(F(1, 2), sub(e1, e2))
    P1, P2 = mul(v, w, S11), mul(w, v, S11)
    J = add(scal(c1, P1), scal(c2, P2))
    U = add(sc(p), scal(q, e2))
    Uinv = sub(sc(p), scal(q, e2))
    O = mul(mul(Uinv, P1, S11), U, S11)
    comm = sub(mul(J, O, S11), mul(O, J, S11))
    return dict(v=v, w=w, P1=P1, P2=P2, J=J, U=U, Uinv=Uinv, O=O, comm=comm, e1=e1, e2=e2)


def check_matter_factor_is_nonzero_when_paths_source_differently():
    premise("synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane")
    premise("field-theory.operator-newtonian-coupling")
    ok = True
    m = matter(F(7), F(2), F(3, 5), F(4, 5))
    one = sc(1)
    ok = ok and GA.is_zero(mul(m["v"], m["v"], S11)) and GA.is_zero(mul(m["w"], m["w"], S11))
    ok = ok and GA.eq(add(mul(m["v"], m["w"], S11), mul(m["w"], m["v"], S11)), one)
    ok = ok and GA.eq(mul(m["P1"], m["P1"], S11), m["P1"]) and GA.eq(add(m["P1"], m["P2"]), one)
    ok = ok and GA.is_zero(mul(m["P1"], m["P2"], S11))
    ok = ok and GA.eq(mul(m["U"], m["Uinv"], S11), one)
    ok = ok and GA.eq(mul(m["O"], m["O"], S11), m["O"])
    # e2 exchanges the two path projectors
    ok = ok and GA.eq(mul(mul(m["e2"], m["P1"], S11), m["e2"], S11), GA.neg(m["P2"]))
    # O = p^2 P1 + q^2 P2 + p q [P1, e2], and [J, O] = (c1 - c2) p q [P1, [P1, e2]] = (c1 - c2) p q e2
    pq = F(3, 5) * F(4, 5)
    P1e2 = sub(mul(m["P1"], m["e2"], S11), mul(m["e2"], m["P1"], S11))
    ok = ok and GA.eq(m["O"], add(scal(F(9, 25), m["P1"]), scal(F(16, 25), m["P2"]), scal(pq, P1e2)))
    ok = ok and GA.eq(m["comm"], scal((7 - 2) * pq, m["e2"]))
    ok = ok and not GA.is_zero(m["comm"])
    # controls: equal sources, or no mixing, give a vanishing factor
    ok = ok and GA.is_zero(matter(F(5), F(5), F(3, 5), F(4, 5))["comm"])
    ok = ok and GA.is_zero(matter(F(7), F(2), F(1), F(0))["comm"])
    GA.check("in Cl(1,1): path projectors, recombiner and detection are as stated, and [J, O] = (c1 - c2) p q e2, "
             "nonzero for c = (7, 2), (p, q) = (3/5, 4/5), zero for equal sources or no recombination", ok)
    return ok


# ---------------------------------------------------------------------------------------------------------
# field
# ---------------------------------------------------------------------------------------------------------
def free_field():
    """phi_n(t) as integer linear forms in the data X_m = phi_m(0), Y_m = phi_m(1): (A, B) coefficient vectors."""
    zero = [0] * N

    def unit(m):
        u = [0] * N
        u[m] = 1
        return u
    A = {0: [unit(i) for i in range(N)], 1: [list(zero) for _ in range(N)]}
    B = {0: [list(zero) for _ in range(N)], 1: [unit(i) for i in range(N)]}
    for t in range(1, TMAX):
        An, Bn = [], []
        for i in range(N):
            a = [-x for x in A[t - 1][i]]
            b = [-x for x in B[t - 1][i]]
            for j in (i - 1, i + 1):
                if 0 <= j < N:
                    a = [x + y for x, y in zip(a, A[t][j])]
                    b = [x + y for x, y in zip(b, B[t][j])]
            An.append(a)
            Bn.append(b)
        A[t + 1], B[t + 1] = An, Bn
    return A, B


def response(tp):
    """Field at all times from zero data and a unit kick into phi_0(tp + 1)."""
    field = {0: [0] * N, 1: [0] * N}
    if tp == 0:
        field[1][idx(0)] += 1
    for t in range(1, TMAX):
        nxt = []
        for i in range(N):
            s = -field[t - 1][i]
            if i - 1 >= 0:
                s += field[t][i - 1]
            if i + 1 < N:
                s += field[t][i + 1]
            nxt.append(s)
        if t == tp:
            nxt[idx(0)] += 1
        field[t + 1] = nxt
    return field


_CACHE = {}


def model():
    if not _CACHE:
        A, B = free_field()
        G = {tp: response(tp) for tp in KICKS}

        def delta(n, t, k, tp):
            a1, b1, a2, b2 = A[t][idx(n)], B[t][idx(n)], A[tp][idx(k)], B[tp][idx(k)]
            return sum(a1[m] * b2[m] - b1[m] * a2[m] for m in range(N))

        def gret(n, t, tp):
            return G[tp][t][idx(n)]
        _CACHE["delta"], _CACHE["gret"] = delta, gret
    return _CACHE["delta"], _CACHE["gret"]


def spacelike_events():
    return [(n, t) for t in range(0, TMAX + 1) for n in WINDOW if abs(n) > abs(TDET - t)]


def check_free_field_keeps_its_form_and_the_response_is_minus_the_commutator():
    delta, gret = model()
    ok = True
    ok = ok and all(delta(n, t, m, t + 1) == (1 if n == m else 0)
                    for t in range(7) for n in range(-5, 6) for m in range(-5, 6))
    ok = ok and all(delta(n, t, m, t) == 0 for t in range(7) for n in range(-5, 6) for m in range(-5, 6))
    for tp in KICKS:
        for t in range(TMAX + 1):
            for n in WINDOW:
                g = gret(n, t, tp)
                ok = ok and g == (-delta(n, t, 0, tp) if t > tp else 0)
                if abs(n) > t - tp - 1:
                    ok = ok and g == 0                       # nothing outside the forward cone of the kicked site
    ok = ok and gret(0, 1, 0) == 1 and gret(1, 2, 0) == 1 and gret(3, 4, 0) == 1 and gret(0, 2, 0) == 0
    GA.check("the free lattice field keeps its commutation form for seven steps; the retarded response equals minus "
             "the commutator function for t > t', vanishes for t <= t' and outside the forward cone (six source times, "
             "37 sites, 19 times)", ok)
    return ok


def check_slaved_field_does_not_commute_at_spacelike_separation():
    premise("field-theory.operator-newtonian-coupling")
    delta, gret = model()
    ok = True
    sl = spacelike_events()
    ok = ok and len(sl) == 502
    s_slaved = {(n, t): sum(gret(n, t, tp) for tp in KICKS) for (n, t) in sl}
    bad = sorted(e for e, val in s_slaved.items() if val != 0)
    ok = ok and len(bad) == 172
    # the failing events are those inside the forward cone of a source event and outside the cone of the detection
    ok = ok and all(any(abs(n) <= t - tp - 1 for tp in KICKS) for (n, t) in bad)
    ok = ok and (8, 9) in bad and s_slaved[(8, 9)] == 1 and (-9, 10) in bad and s_slaved[(-9, 10)] == 1
    # events at the detection time itself: the retarded time is before the recombination
    ok = ok and s_slaved[(7, 8)] == 1 and s_slaved[(3, 8)] == 3 and s_slaved[(2, 8)] == 3
    # with the matter factor: the commutator [phi_slaved, O] = -g [J, O] S, nonzero when the paths source differently
    m = matter(F(7), F(2), F(3, 5), F(4, 5))
    ok = ok and not GA.is_zero(scal(-s_slaved[(8, 9)], m["comm"]))
    ok = ok and GA.is_zero(scal(-s_slaved[(8, 9)], matter(F(5), F(5), F(3, 5), F(4, 5))["comm"]))
    # the slaved field's own bracket vanishes: its values are multiples of J
    ok = ok and GA.is_zero(sub(mul(scal(3, m["J"]), scal(-2, m["J"]), S11), mul(scal(-2, m["J"]), scal(3, m["J"]), S11)))
    GA.check("slaved field: the coefficient sum_t' G of its commutator with the detection is nonzero at 172 of the 502 "
             "grid events spacelike to the detection event (0, 8), all inside the forward cone of a source event", ok)
    return ok


def check_free_part_restores_commutation_at_spacelike_separation():
    premise("synthesis.locality-of-the-attached-free-fields-fixes-their-statistics")
    delta, gret = model()
    ok = True
    sl = spacelike_events()

    def s_full(n, t):
        return sum(gret(n, t, tp) + delta(n, t, 0, tp) for tp in KICKS)
    ok = ok and all(s_full(n, t) == 0 for (n, t) in sl)
    # support: only inside the past cones of the source events
    allev = [(n, t) for t in range(TMAX + 1) for n in WINDOW]
    ok = ok and all(s_full(n, t) == 0 or any(abs(n) <= tp - t for tp in KICKS) for (n, t) in allev)
    # control: nonzero at some timelike events (before the sources), e.g. (0, 0) from the kick at t' = 1
    ok = ok and s_full(0, 0) == sum(delta(0, 0, 0, tp) for tp in KICKS) and s_full(0, 0) != 0
    ok = ok and any(s_full(n, t) != 0 for (n, t) in allev if abs(n) < abs(TDET - t))
    # the free part alone does not commute either: it is the sum that vanishes
    ok = ok and any(sum(delta(n, t, 0, tp) for tp in KICKS) != 0 for (n, t) in sl)
    GA.check("with the free part: sum_t' (G + Delta) vanishes at all 502 spacelike events, is supported in the past "
             "cones of the source events and is nonzero at timelike events; the free part alone fails as the slaved "
             "part does", ok)
    return ok


# ---------------------------------------------------------------------------------------------------------
# (5) the first-order Einstein map in Cl(1,3)
# ---------------------------------------------------------------------------------------------------------
S13 = GA.sig(1, 3)
ETA = [1, -1, -1, -1]
E4 = [gen(i) for i in range(4)]
REC4 = [E4[0]] + [GA.neg(x) for x in E4[1:]]


def _d(a, b):
    return GA.dot(a, b, S13)


def _grade1(x):
    return {b: c for b, c in x.items() if len(b) == 1}


def _wedge(a, b):
    return scal(F(1, 2), sub(mul(a, b, S13), mul(b, a, S13)))


def _vdotB(a, B):
    return _grade1(scal(F(1, 2), sub(mul(a, B, S13), mul(B, a, S13))))


def einstein_rank(pv):
    p = {(i,): F(x) for i, x in enumerate(pv) if x}
    rows = []
    for m in range(4):
        for n in range(m, 4):
            def h(a, m=m, n=n):
                # the symmetric map with lower components delta_m delta_n + delta_n delta_m
                out = {}
                am, an = _d(E4[m], a) * ETA[m], _d(E4[n], a) * ETA[n]      # contravariant components of a
                out = add(out, scal(an * ETA[m], E4[m]))
                if m != n:
                    out = add(out, scal(am * ETA[n], E4[n]))
                return out

            def riem(B):
                return scal(F(-1, 2), _wedge(p, h(GA.neg(_vdotB(p, B)))))

            def ric(a):
                out = {}
                for b in range(4):
                    out = add(out, _vdotB(REC4[b], riem(_wedge(E4[b], a))))
                return out
            R = [[_d(E4[a], ric(E4[b])) for b in range(4)] for a in range(4)]
            tr = sum(ETA[a] * R[a][a] for a in range(4))
            rows.append([R[a][b] - F(1, 2) * (ETA[a] if a == b else 0) * tr for a in range(4) for b in range(4)])
    return GA.mat_rank(rows), _d(p, p)


def check_einstein_map_kernels_at_non_null_and_null_momentum():
    premise("synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel")
    premise("field-theory.no-canonical-commutation-relations-tower")
    ok = True
    non_null = [einstein_rank(pv) for pv in [(2, 0, 0, 0), (3, 1, 0, 2), (1, 2, 0, 0), (0, 1, 1, 3)]]
    null = [einstein_rank(pv) for pv in [(1, 0, 0, 1), (5, 3, 0, 4)]]
    ok = ok and [q for _, q in non_null] == [4, 4, -3, -11] and [q for _, q in null] == [0, 0]
    ok = ok and [r for r, _ in non_null] == [6, 6, 6, 6]       # kernel 10 - 6 = 4
    ok = ok and [r for r, _ in null] == [4, 4]                 # kernel 10 - 4 = 6
    GA.check("first-order Einstein map on the ten symmetric maps: rank 6 at four non-null momenta (kernel the four "
             "displacements), rank 4 at two null momenta (two further directions)", ok)
    return ok
