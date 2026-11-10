"""synthesis.colour-triplets-give-the-fundamental-colour-loop-a-perimeter-law-at-strong-coupling: exact checks.

Colour block as in the stored conventions of the colour factor: V = span(e3, ..., e8) in Cl(9,0),
J = e34 + e56 + e78, j(v) = v.J, Re Omega, Im Omega the J-volume trivectors; SU(3) = rotations of V commuting
with J and fixing Re Omega. Haar moments are derived, not imported: the average of U^(x)k is the orthogonal
projector onto the invariants, and the SU(3)-invariants are the invariants of the finite subgroup G of
J-commuting signed permutations (order 96) that every su(3) bivector annihilates (degree 4 included, where G has
more invariants). x = e3 . U(e3) is the real part of the J-complex entry u_11.
(a) Frozen colour triplet: unit vectors phi of V at the sites, hopping kappa sum <phi_x, U phi_y>; unitary gauge
    phi = e3; mean link M(kappa) = E[U e^{kappa x}] / E[e^{kappa x}] to order kappa^3 from the projectors.
(b) Wilson quarks (r = 1) at beta = 0: Euclidean directions are the vectors d1..d4 of Cl(4,0); a hop in
    direction +mu carries (1 - d_mu), in -mu (1 + d_mu); the spinor trace is 4 times the scalar part (the
    complex four-dimensional spinor module); closed walks are enumerated on the rectangle's patch.
Exact Fractions throughout.
"""
from fractions import Fraction as F
from itertools import product

import GA
from GA import mul, sc, gen, add, scal, sub, reverse
from tp_premise import premise

S9 = (1,) * 9
N = 6


def blade(*idx):
    r = sc(1)
    for i in idx:
        r = mul(r, gen(i), S9)
    return r


J = add(blade(3, 4), blade(5, 6), blade(7, 8))
RE_OMEGA = add(blade(3, 5, 7), scal(-1, blade(3, 6, 8)), scal(-1, blade(4, 5, 8)), scal(-1, blade(4, 6, 7)))
IM_OMEGA = add(blade(4, 5, 7), blade(3, 6, 7), blade(3, 5, 8), scal(-1, blade(4, 6, 8)))


def comm(x, y):
    return sub(mul(x, y, S9), mul(y, x, S9))


def su3_bivectors():
    pairs = [(a, b) for a in range(3, 9) for b in range(a + 1, 9)]
    rows = {}
    for k, (a, b) in enumerate(pairs):
        for tag, tgt in (("J", J), ("O", RE_OMEGA)):
            for bl, val in comm(blade(a, b), tgt).items():
                rows.setdefault((tag, bl), [F(0)] * len(pairs))[k] += val
    ker = GA.field_kernel(list(rows.values()))
    return [add(*[scal(v[k], blade(*pairs[k])) for k in range(len(pairs)) if v[k]]) for v in ker]


def vector_matrix(B):
    """6x6 matrix of v -> (vB - Bv)/2 on e3..e8."""
    M = [[F(0)] * N for _ in range(N)]
    for m in range(N):
        v = gen(m + 3)
        w = scal(F(1, 2), sub(mul(v, B, S9), mul(B, v, S9)))
        for bl, val in w.items():
            assert len(bl) == 1 and 3 <= bl[0] <= 8
            M[bl[0] - 3][m] = val
    return M


# ------------------------------------------------------------------ the finite group as signed permutations
def jmap(m):
    return (m + 1, 1) if m % 2 == 0 else (m - 1, -1)


def from_complex(u):
    """3x3 matrix with entries (a, b) = a + b i, monomial, a, b in {0, 1, -1} -> signed permutation of e3..e8."""
    img = [None] * N
    for col in range(3):
        hits = [(2 * k + (0 if u[k][col][0] else 1), u[k][col][0] or u[k][col][1])
                for k in range(3) if u[k][col] != (0, 0)]
        assert len(hits) == 1
        m, s = hits[0]
        img[2 * col] = (m, s)
        jm, js = jmap(m)
        img[2 * col + 1] = (jm, js * s)
    return tuple(img)


def compose(g, h):
    out = []
    for m in range(N):
        n, s = h[m]
        n2, s2 = g[n]
        out.append((n2, s * s2))
    return tuple(out)


IDENT = tuple((m, 1) for m in range(N))
O_, Z_, M_, I_, MI_ = (1, 0), (0, 0), (-1, 0), (0, 1), (0, -1)
GENERATORS = [from_complex([[I_, Z_, Z_], [Z_, MI_, Z_], [Z_, Z_, O_]]),
              from_complex([[O_, Z_, Z_], [Z_, I_, Z_], [Z_, Z_, MI_]]),
              from_complex([[Z_, Z_, O_], [O_, Z_, Z_], [Z_, O_, Z_]]),
              from_complex([[Z_, O_, Z_], [O_, Z_, Z_], [Z_, Z_, M_]])]


def closure(gens):
    group = {IDENT}
    frontier = [IDENT]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                k = compose(h, g)
                if k not in group:
                    group.add(k)
                    new.append(k)
        frontier = new
    return sorted(group)


G = closure(GENERATORS)


def tr_r(g):
    return sum(s for m, (n, s) in enumerate(g) if n == m)


def chi(g):
    return F(tr_r(g), N)


def inverse(g):
    out = [None] * N
    for m, (n, s) in enumerate(g):
        out[n] = (m, s)
    return tuple(out)


def versor_of(g):
    """Rational even versor V with V x V^-1 = g(x) on e3..e8 (Householder reflections)."""
    cur = list(g)
    vecs = []
    for m in range(N):
        n, s = cur[m]
        if (n, s) == (m, 1):
            continue
        nv = sub(gen(m + 3), scal(s, gen(n + 3))) if n != m else gen(m + 3)
        vecs.append(nv)
        # apply the reflection in nv to every image
        new = []
        for (p, t) in cur:
            if n != m and p in (m, n):
                q = n if p == m else m
                new.append((q, t * s))
            elif n == m and p == m:
                new.append((p, -t))
            else:
                new.append((p, t))
        cur = new
    assert cur == list(IDENT)
    V = sc(1)
    for nv in vecs:
        V = mul(V, nv, S9)
    return V, len(vecs)


def sandwich(V, x):
    nrm = mul(V, reverse(V), S9)
    assert set(nrm) <= {()}
    return scal(1 / nrm[()], mul(mul(V, x, S9), reverse(V), S9))


# ------------------------------------------------------------------ tensor invariants
def g_invariants(d):
    """Orthogonal basis of the G-invariants of V^{(x)d}: signed orbit sums with no sign clash."""
    seen = set()
    basis = []
    for t in product(range(N), repeat=d):
        if t in seen:
            continue
        orb = {}
        clash = False
        for g in G:
            s = 1
            img = []
            for a in t:
                n, sg = g[a]
                img.append(n)
                s *= sg
            img = tuple(img)
            if orb.get(img, s) != s:
                clash = True
            orb[img] = s
        seen.update(orb)
        if not clash:
            basis.append({k: F(v) for k, v in orb.items()})
    return basis


def derivation(Xm, vec, d):
    out = {}
    for t, c in vec.items():
        for pos in range(d):
            a = t[pos]
            for n in range(N):
                x = Xm[n][a]
                if x:
                    t2 = t[:pos] + (n,) + t[pos + 1:]
                    out[t2] = out.get(t2, 0) + c * x
    return {k: v for k, v in out.items() if v}


def su3_invariants(d, gbasis, mats):
    """Kernel of every su(3) derivation on the span of the G-invariants (coefficient vectors)."""
    rows = {}
    for j, v in enumerate(gbasis):
        for gi, Xm in enumerate(mats):
            for t, c in derivation(Xm, v, d).items():
                rows.setdefault((gi, t), [F(0)] * len(gbasis))[j] += c
    if not rows:
        return [[F(1) if i == j else F(0) for i in range(len(gbasis))] for j in range(len(gbasis))]
    return GA.field_kernel(list(rows.values()))


def combine(gbasis, coeffs):
    out = {}
    for c, v in zip(coeffs, gbasis):
        if c:
            for t, x in v.items():
                out[t] = out.get(t, 0) + c * x
    return {k: v for k, v in out.items() if v}


def blade_tensor(x, k):
    """Antisymmetric tensor of a k-vector of the block (sum over orderings with signs)."""
    out = {}
    for bl, val in x.items():
        assert len(bl) == k
        idx = [b - 3 for b in bl]
        for perm in product(range(k), repeat=k):
            if len(set(perm)) < k:
                continue
            inv = sum(1 for a in range(k) for b in range(a + 1, k) if perm[a] > perm[b])
            t = tuple(idx[p] for p in perm)
            out[t] = out.get(t, 0) + val * (-1) ** inv
    return out


def in_span(vec, vecs):
    keys = sorted(set(vec) | {k for v in vecs for k in v})
    M = [[v.get(k, 0) for v in vecs] for k in keys]
    r0 = GA.field_rank(M) if vecs else 0
    M2 = [row + [vec.get(k, 0)] for row, k in zip(M, keys)]
    return GA.field_rank(M2) == r0


_CACHE = {}


def invariant_data(d):
    if d not in _CACHE:
        mats = [vector_matrix(B) for B in su3_bivectors()]
        gb = g_invariants(d)
        ker = su3_invariants(d, gb, mats)
        _CACHE[d] = (gb, [combine(gb, c) for c in ker])
    return _CACHE[d]



S4 = (1, 1, 1, 1)


def colour_projector_entry(inv, a, b):
    """Entry (a, b) of the orthogonal projector onto span(inv) in V^(x)k."""
    k = len(inv)
    gram = [[sum((x * inv[j].get(t, 0) for t, x in inv[i].items()), F(0)) for j in range(k)] for i in range(k)]
    y = GA.field_solve(gram, [v.get(b, F(0)) for v in inv])
    return sum((v.get(a, F(0)) * w for v, w in zip(inv, y)), F(0))


def mean_link_series():
    """M_ab = kappa m1_ab + kappa^3 (m3_ab/6 - m2 m1_ab/2), with m1_ab = E[U_ab x], m3_ab = E[U_ab x^3], m2 = E[x^2]."""
    gb2, inv2 = invariant_data(2)
    gb4, inv4 = invariant_data(4)
    m2 = colour_projector_entry(inv2, (0, 0), (0, 0))
    m4 = colour_projector_entry(gb4, (0, 0, 0, 0), (0, 0, 0, 0))
    m1 = [[colour_projector_entry(inv2, (a, 0), (b, 0)) for b in range(N)] for a in range(N)]
    m3 = [[colour_projector_entry(gb4, (a, 0, 0, 0), (b, 0, 0, 0)) for b in range(N)] for a in range(N)]
    lin = m1
    cub = [[m3[a][b] / 6 - m2 * m1[a][b] / 2 for b in range(N)] for a in range(N)]
    return m2, m4, lin, cub


def check_colour_moments_of_a_matrix_entry_from_invariants():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    gb4, inv4 = invariant_data(4)
    assert (len(gb4), len(inv4)) == (20, 12)
    m2, m4, lin, cub = mean_link_series()
    assert (m2, m4) == (F(1, 6), F(1, 16))
    # the finite group alone would give a different fourth moment: degree four is not shared
    g4 = sum((F(1) for g in G if g[0][0] == 0), F(0)) / len(G)
    assert g4 == F(1, 6) and g4 != m4
    # and the second moment of x over G equals the Haar value (degree two is shared)
    assert sum((F(1) for g in G if g[0][0] == 0), F(0)) / len(G) == F(1, 6)


def check_frozen_triplet_mean_link_is_rank_one_and_its_coefficient():
    premise("synthesis.non-abelian-gauge-fixing-has-gribov-copies-and-the-weak-rotor-lattice-with-doublets-has-a-perimeter-law")
    m2, m4, lin, cub = mean_link_series()
    proj = [[F(1) if (a == b and a in (0, 1)) else F(0) for b in range(N)] for a in range(N)]
    assert lin == [[F(1, 6) * x for x in row] for row in proj]
    assert cub == [[F(-1, 288) * x for x in row] for row in proj]
    # c(kappa) = kappa/6 - kappa^3/288 from the scalar moments too
    assert F(1, 16) / 6 - F(1, 6) * F(1, 6) / 2 == F(-1, 288)
    # M = c Pi with Pi the projector on the complex line of e3: Pi^P = Pi, tr Pi = 2, so chi(M^P) = c^P / 3
    for P in (4, 6, 8):
        power = proj
        for _ in range(P - 1):
            power = [[sum(power[a][k] * proj[k][b] for k in range(N)) for b in range(N)] for a in range(N)]
        assert power == proj and F(sum(power[a][a] for a in range(N)), 6) == F(1, 3)
    # unitary gauge: the hopping term <phi_x, U phi_y> is unchanged by U -> g_x^-1 U g_y with g phi = e3
    for gx in G[:12]:
        for gy in G[40:52]:
            for U in G[::17]:
                phx = gx[0]
                phy = gy[0]
                # <g_x e3, U g_y e3>
                n, s = U[phy[0]]
                lhs = phx[1] * phy[1] * s * (1 if n == phx[0] else 0)
                V = compose(inverse(gx), compose(U, gy))
                rhs = V[0][1] if V[0][0] == 0 else 0
                assert lhs == rhs


def cliff4(*idx):
    r = sc(1)
    for i in idx:
        r = mul(r, gen(i), S4)
    return r


def hop(mu, sign):
    """Spin factor of a hop along +mu (sign = +1) or -mu (sign = -1): 1 - sign d_mu."""
    return add(sc(1), scal(-sign, gen(mu)))


def spin_trace(x):
    return 4 * x.get((), F(0))


def check_wilson_quark_corner_factor_is_independent_of_the_rectangle():
    premise("synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement")
    for mu in range(4):
        assert mul(hop(mu, 1), hop(mu, 1), S4) == scal(2, hop(mu, 1))
        assert mul(hop(mu, 1), hop(mu, -1), S4) == {}
    for mu in range(4):
        for nu in range(4):
            if mu == nu:
                continue
            for R in range(1, 4):
                for T in range(1, 4):
                    steps = [(mu, 1)] * R + [(nu, 1)] * T + [(mu, -1)] * R + [(nu, -1)] * T
                    for orient in (steps, [(d, -s) for d, s in reversed(steps)]):
                        prod = sc(1)
                        for d, s in orient:
                            prod = mul(prod, hop(d, s), S4)
                        P = 2 * (R + T)
                        assert spin_trace(prod) == -(2 ** (P - 1))


def walks(sites, nbrs, length, start):
    out = []

    def rec(path):
        if len(path) == length + 1:
            if path[-1] == start:
                out.append(list(path))
            return
        for y in nbrs[path[-1]]:
            rec(path + [y])
    rec([start])
    return out


def check_quark_loop_gives_the_rectangle_a_perimeter_term_at_beta_zero():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    premise("synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement")
    for R, T in ((1, 1), (2, 1)):
        sites = [(x, y) for x in range(R + 1) for y in range(T + 1)]
        links = [((x, y), (x + 1, y)) for x in range(R) for y in range(T + 1)]
        links += [((x, y), (x, y + 1)) for x in range(R + 1) for y in range(T)]
        nbrs = {s: [] for s in sites}
        for a, b in links:
            nbrs[a].append(b)
            nbrs[b].append(a)
        P = 2 * (R + T)
        boundary = [(x, 0) for x in range(R + 1)] + [(R, y) for y in range(1, T + 1)]
        boundary += [(x, T) for x in range(R - 1, -1, -1)] + [(0, y) for y in range(T - 1, 0, -1)]
        for sample in range(3):
            U = {l: G[(7 * k + 31 * sample) % len(G)] for k, l in enumerate(links)}

            def step(a, b):
                if (a, b) in U:
                    d = 0 if b[0] != a[0] else 1
                    return hop(d, 1), U[(a, b)]
                d = 0 if b[0] != a[0] else 1
                return hop(d, -1), inverse(U[(b, a)])
            # (1/P) sum over closed walks of length P of tr_spin(Gamma) times the real colour trace / 2:
            # the order-kappa^P part of -ln det(1 - kappa H) summed over both orientations
            total = F(0)
            for s0 in sites:
                for w in walks(sites, nbrs, P, s0):
                    spin = sc(1)
                    col = IDENT
                    for a, b in zip(w, w[1:]):
                        sp, u = step(a, b)
                        spin = mul(spin, sp, S4)
                        col = compose(col, u)
                    total += spin_trace(spin) * F(tr_r(col), 2)
            total = total / P
            col_c = IDENT
            for a, b in zip(boundary + [boundary[0]], boundary[1:] + [boundary[0]]):
                col_c = compose(col_c, step(a, b)[1])
            assert total == -(2 ** (P - 1)) * tr_r(col_c)
    # colour average of chi(U_C) tr_R(U_C) over G = 2/6 (degree two, the Haar value), so the leading term of
    # <chi(U_C)> per flavour is 2^{P-1} kappa^P * 2/6 = (2 kappa)^P / 6
    assert sum((chi(g) * tr_r(g) for g in G), F(0)) / len(G) == F(1, 3)
    for P in (4, 6, 8):
        assert 2 ** (P - 1) * F(1, 3) == F(2 ** P, 6)
