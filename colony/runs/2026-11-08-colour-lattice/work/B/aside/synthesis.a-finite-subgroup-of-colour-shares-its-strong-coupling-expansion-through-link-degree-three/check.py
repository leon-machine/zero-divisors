"""synthesis.a-finite-subgroup-of-colour-shares-its-strong-coupling-expansion-through-link-degree-three: exact checks.

Colour block: V = span(e3, ..., e8) in Cl(9,0), J = e34 + e56 + e78, the complex structure j(v) = v.J
(e3 -> e4, e4 -> -e3, ...), and the trivectors Re Omega = e357 - e368 - e458 - e467,
Im Omega = e457 + e367 + e358 - e468 (real and imaginary parts of the J-complex volume form on the
complex frame f1, f2, f3 = e3, e5, e7, j f_k = e4, e6, e8). su(3) is computed here as the bivectors of the
block commuting with J and with Re Omega. The finite group G (order 96) is the set of J-commuting signed
permutations of e3..e8 that fix Re Omega; each element is the sandwich action of a rational even versor.
Index m = 0..5 stands for e_{m+3}. A link U acts on V; its real trace tr_R U = sum_m e_m . U(e_m) is twice
the real part of its J-complex trace, and chi(U) = tr_R U / 6 is the plaquette weight's argument
(weight exp(beta chi), beta = 6/g^2).
Haar averages on SU(3) are never imported: for a compact group the average of U^{(x)k} is the orthogonal
projector onto the invariants of V^{(x)k}; G-invariants contain SU(3)-invariants, and the SU(3)-invariants
are the G-invariants annihilated by su(3) (SU(3) is connected). So equal subspaces mean equal averages.
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


# ------------------------------------------------------------------ checks
def check_colour_block_su3_and_the_finite_group_inside_it():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    su3 = su3_bivectors()
    assert len(su3) == 8
    # traceless: orthogonal to J in the trace form, and closed under the commutator
    for B in su3:
        assert mul(B, J, S9).get((), 0) == 0
    span = [{bl: v for bl, v in B.items()} for B in su3]
    for A in su3:
        for B in su3:
            assert in_span(comm(A, B), span)
    assert len(G) == 96
    # every element is a J-commuting rotation fixing Re Omega, given by a rational even versor
    for g in G:
        V, k = versor_of(g)
        assert k % 2 == 0
        for m in range(N):
            n, s = g[m]
            assert sandwich(V, gen(m + 3)) == scal(s, gen(n + 3))
        assert sandwich(V, J) == J and sandwich(V, RE_OMEGA) == RE_OMEGA and sandwich(V, IM_OMEGA) == IM_OMEGA
    # Re Omega detects the J-determinant: diag(i, 1, 1) is J-linear with determinant i and turns it to Im Omega
    d_i = from_complex([[I_, Z_, Z_], [Z_, O_, Z_], [Z_, Z_, O_]])
    V, k = versor_of(d_i)
    assert sandwich(V, J) == J and sandwich(V, RE_OMEGA) == IM_OMEGA
    # trivial centre: the only elements of the form a + b j are 1 (the centre of SU(3) needs b = +-sqrt(3)/2)
    scalars = [g for g in G if g[0][0] in (0, 1)
               and len({(g[2 * k][0] - 2 * k, g[2 * k][1]) for k in range(3)}) == 1]
    assert scalars == [IDENT]
    # a rational J-scalar a + b j with (a + bi)^3 = 1 is 1 (sampled denominators up to 6)
    roots = set()
    for den in range(1, 7):
        for a in range(-den, den + 1):
            for b in range(-den, den + 1):
                z = GA.qi(F(a, den), F(b, den))
                if z * z * z == GA.qi(1, 0):
                    roots.add((z.re, z.im))
    assert roots == {(F(1), F(0))}


def check_finite_group_averages_equal_haar_through_degree_three():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    dims = []
    for d in (1, 2, 3):
        gb, inv = invariant_data(d)
        dims.append((len(gb), len(inv)))
    assert dims == [(0, 0), (2, 2), (2, 2)]
    # degree 2: the metric and the Kaehler form of J; degree 3: Re and Im of the J-complex volume form
    gb2, inv2 = invariant_data(2)
    metric = {(m, m): F(1) for m in range(N)}
    kaehler = {}
    for m in range(0, N, 2):
        kaehler[(m, m + 1)] = F(1)
        kaehler[(m + 1, m)] = F(-1)
    assert in_span(metric, inv2) and in_span(kaehler, inv2)
    gb3, inv3 = invariant_data(3)
    assert in_span(blade_tensor(RE_OMEGA, 3), inv3) and in_span(blade_tensor(IM_OMEGA, 3), inv3)
    # the averages of U^(x)d over G, entry by entry, equal the orthogonal projector onto the invariants
    for d, (gb, inv) in ((2, invariant_data(2)), (3, invariant_data(3))):
        norms = [sum(x * x for x in v.values()) for v in gb]
        for a in product(range(N), repeat=d):
            for b in ((0,) * d, (0, 1, 2)[:d], (1, 0, 3)[:d]):
                avg = F(0)
                for g in G:
                    s = 1
                    for ai, bi in zip(a, b):
                        n, sg = g[bi]
                        s *= sg if n == ai else 0
                    avg += s
                avg /= len(G)
                proj = sum((v.get(a, 0) * v.get(b, 0) / nv for v, nv in zip(gb, norms)), F(0))
                assert avg == proj


def check_degree_four_separates_them_by_a_centre_violating_moment():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    gb4, inv4 = invariant_data(4)
    assert (len(gb4), len(inv4)) == (20, 12)
    # E[(tr_R U)^4] is the trace of the projector, the number of invariants
    assert sum((F(tr_r(g)) ** 4 for g in G), F(0)) / len(G) == 20
    # the J-derivation D on V^(x)4 (the u(1) of J); the centre exp(2 pi J/3) acts on its eigenvalue
    # i(p - q) as exp(2 pi i (p - q)/3)
    jmat = [[F(0)] * N for _ in range(N)]
    for m in range(N):
        n, s = jmap(m)
        jmat[n][m] = F(s)
    for v in inv4:
        assert derivation(jmat, v, 4) == {}
    norms = [sum(x * x for x in v.values()) for v in gb4]

    def coords(vec):
        return [sum((vec.get(t, 0) * x for t, x in b.items()), F(0)) / nb for b, nb in zip(gb4, norms)]
    D = [coords(derivation(jmat, b, 4)) for b in gb4]          # D[j] = image of basis j
    Dm = [[D[j][i] for j in range(len(gb4))] for i in range(len(gb4))]
    D2 = [[sum(Dm[i][k] * Dm[k][j] for k in range(len(gb4))) for j in range(len(gb4))] for i in range(len(gb4))]
    shifted = [[D2[i][j] + (16 if i == j else 0) for j in range(len(gb4))] for i in range(len(gb4))]
    assert len(gb4) - GA.field_rank(Dm) == 18
    assert len(gb4) - GA.field_rank(shifted) == 2
    # the complex trace t = sum_k (U_{2k,2k} + i U_{2k+1,2k}): E_G[t^4] = 1, E_G[|t|^4] = 3
    t4 = GA.qi(0)
    abs4 = F(0)
    for g in G:
        t = GA.qi(0)
        for k in range(3):
            n, s = g[2 * k]
            if n == 2 * k:
                t = t + GA.qi(s, 0)
            elif n == 2 * k + 1:
                t = t + GA.qi(0, s)
        t4 = t4 + t * t * t * t
        abs4 += (t.re * t.re + t.im * t.im) ** 2
    assert t4 / len(G) == GA.qi(1, 0) and abs4 / len(G) == 3


def check_gluing_rule_and_leading_loop_coefficients_agree():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    premise("synthesis.weak-factor-rotor-lattice-strong-coupling-area-law")
    # real matrices of the J-linear basis E_kl and i E_kl
    jl = []
    for k in range(3):
        for l in range(3):
            for ph in ((1, 0), (0, 1)):
                M = [[F(0)] * N for _ in range(N)]
                u = [[(0, 0)] * 3 for _ in range(3)]
                u[k][l] = ph
                a, b = ph
                M[2 * k][2 * l] += a
                M[2 * k + 1][2 * l + 1] += a
                M[2 * k + 1][2 * l] += b
                M[2 * k][2 * l + 1] -= b
                jl.append(M)
    assert len(jl) == 18

    def gmat(g):
        M = [[0] * N for _ in range(N)]
        for m, (n, s) in enumerate(g):
            M[n][m] = s
        return M

    def tr_prod(A, B):
        return sum(A[i][k] * B[k][i] for i in range(N) for k in range(N))
    mats = [(gmat(g), gmat(inverse(g))) for g in G]
    for X in jl:
        assert sum(tr_prod(X, U) for U, _ in mats) == 0
        for Y in jl:
            lhs = sum(tr_prod(X, U) * tr_prod(Ui, Y) for U, Ui in mats) / F(len(G))
            assert lhs == F(1, 3) * tr_prod(X, Y)
    # leading coefficients of the 1x1 and 2x1 fundamental loops in a tree gauge: (1/18)^A
    one = sum(chi(g) * chi(inverse(g)) for g in G) / len(G)
    assert one == F(1, 18)
    two = F(0)
    for a in G:
        for b in G:
            # free links V1 (x = 1), V2 (x = 2); loop = V2, plaquettes V1 and V2 V1^-1
            two += chi(b) * chi(a) * chi(compose(b, inverse(a)))
    assert two / len(G) ** 2 == F(1, 18) ** 2


def check_plaquette_series_agrees_through_beta_squared_and_differs_at_beta_cubed():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    premise("synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement")
    m_su3 = {0: F(1), 1: F(0)}
    m_g = {0: F(1), 1: F(0)}
    for d in (2, 3, 4):
        gb, inv = invariant_data(d)
        m_su3[d] = F(len(inv), N ** d)
        m_g[d] = F(len(gb), N ** d)
        assert m_g[d] == sum((chi(g) ** d for g in G), F(0)) / len(G)
    assert (m_su3[2], m_su3[3], m_su3[4]) == (F(1, 18), F(1, 108), F(1, 108))
    assert m_g[4] == F(5, 324)

    def cumulants(m):
        return {2: m[2], 3: m[3], 4: m[4] - 3 * m[2] ** 2}
    k_su3, k_g = cumulants(m_su3), cumulants(m_g)
    # <chi_p> = sum_n kappa_{n+1} beta^n / n! below the first closed surface (order beta^5)
    series_su3 = [k_su3[2], k_su3[3] / 2, k_su3[4] / 6]
    series_g = [k_g[2], k_g[3] / 2, k_g[4] / 6]
    assert series_su3 == [F(1, 18), F(1, 216), F(0)]
    assert series_g == [F(1, 18), F(1, 216), F(1, 972)]
    # the same series from the single-plaquette ratio E[chi e^{beta chi}] / E[e^{beta chi}] over G
    num = [sum((chi(g) ** (n + 1) for g in G), F(0)) / len(G) / fact(n) for n in range(4)]
    den = [sum((chi(g) ** n for g in G), F(0)) / len(G) / fact(n) for n in range(4)]
    ratio = GA.ps_mul(num, GA.ps_inv(den, 4), 4)
    assert ratio[1:4] == series_g


def fact(n):
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r


def check_finite_plaquette_weight_has_a_gap_and_colour_has_none():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    top = max(chi(g) for g in G if g != IDENT)
    assert top == F(1, 3)
    # colour: diag(z, conj z, 1) with z = ((n^2 - 1) + 2n i)/(n^2 + 1) has 1 - chi = 4/(3(n^2 + 1))
    for n in (2, 3, 7, 30):
        z = GA.qi(F(n * n - 1, n * n + 1), F(2 * n, n * n + 1))
        assert z * z.conj() == GA.qi(1, 0)
        re_trace = 2 * z.re + 1
        assert 1 - re_trace / 3 == F(4, 3 * (n * n + 1))
