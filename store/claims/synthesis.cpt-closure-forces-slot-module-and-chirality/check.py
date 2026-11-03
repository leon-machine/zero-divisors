"""synthesis.cpt-closure-forces-slot-module-and-chirality: exact checks.

A graded polynomial U(2) slot module F is a multiset of irreducibles F_lambda, lambda = (l1 >= l2 >= 0),
slot number n = l1 + l2, weak spin (l1 - l2)/2. The composite space V = F (x) Lambda W has isotypic
components (2j, colour, Y) with colour 1, 3, 3bar, 1 for k = 0..3 and Y = (3n - 2k)/6. A CPT halving is
V = V+ (+) V- with V- the conjugate of V+. Equivariant maps are computed by exact linear algebra with
GA.field_kernel / GA.rank_of_vectors over the rationals.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

COLOUR = {0: '1', 1: '3', 2: '3b', 3: '1'}
CONJ = {'1': '1', '3': '3b', '3b': '3'}


def V_of(Fm):
    c = Counter()
    for (l1, l2), m in Fm.items():
        n = l1 + l2
        for k in range(4):
            c[(l1 - l2, COLOUR[k], F(3 * n - 2 * k, 6))] += m
    return c


def conj(R):
    s2, t, y = R
    return (s2, CONJ[t], -y)


def selfconj(c):
    return all(c[conj(R)] == m for R, m in c.items())


def tau(s2):
    j = F(s2, 2)
    return F(2, 3) * j * (j + 1) * (2 * j + 1)


def dcol(t):
    return 1 if t == '1' else 3


def four(half):
    """The four sums of the imported anomaly fact, in its normalisation."""
    grav = sum((m * (s2 + 1) * dcol(t) * y for (s2, t, y), m in half.items()), F(0))
    su2 = sum((m * tau(s2) * dcol(t) * y for (s2, t, y), m in half.items()), F(0))
    su3 = sum((m * (s2 + 1) * y for (s2, t, y), m in half.items() if t != '1'), F(0))
    y3 = sum((m * (s2 + 1) * dcol(t) * y ** 3 for (s2, t, y), m in half.items()), F(0))
    return (grav, su2, su3, y3)


def cubic_su3(half):
    return sum((m * (s2 + 1) * (1 if t == '3' else -1) for (s2, t, y), m in half.items() if t != '1'), 0)


def doublets(half):
    return sum((m * dcol(t) for (s2, t, y), m in half.items() if s2 == 1), 0)


def halvings(c):
    pairs, reals = [], []
    seen = set()
    for R in sorted(c):
        if R in seen:
            continue
        seen.add(R)
        seen.add(conj(R))
        (reals if conj(R) == R else pairs).append(R)
    if any(c[R] % 2 for R in reals):
        return
    base = Counter({R: c[R] // 2 for R in reals})
    for ch in product(*[range(c[R] + 1) for R in pairs]):
        h = Counter(base)
        for R, k in zip(pairs, ch):
            if k:
                h[R] += k
            if c[R] - k:
                h[conj(R)] += c[R] - k
        yield h


def anomaly_free(c):
    return [h for h in halvings(c) if four(h) == (0, 0, 0, 0)]


def ab_form(a, b):
    Fm = {}
    if a:
        Fm[(0, 0)] = a
        Fm[(1, 1)] = a
    if b:
        Fm[(1, 0)] = b
    return Fm


def half_by_parity(Fm, pi, parity):
    h = Counter()
    for (l1, l2), m in Fm.items():
        n = l1 + l2
        for k in range(4):
            if (pi * n + k) % 2 == parity:
                h[(l1 - l2, COLOUR[k], F(3 * n - 2 * k, 6))] += m
    return h


def check_cpt_closure_classification():
    premise("standard-model.imported-pair-systems-two-chirality-halves")
    premise("standard-model.global-form-quotient-determined")
    irreps = [(l1, l2) for l1 in range(4) for l2 in range(l1 + 1)]
    assert len(irreps) == 10
    # the (S) module: 32 states in 11 isotypes, (1,1)_0 twice, the rest in 5 conjugate pairs of each kind
    V1 = V_of(ab_form(1, 1))
    assert sum(((s2 + 1) * dcol(t) * mlt for (s2, t, y), mlt in V1.items()), 0) == 32
    assert len(V1) == 11 and V1[(0, '1', F(0))] == 2
    assert sorted(y for (s2, t, y) in V1) == sorted([F(0), F(-1, 3), F(-2, 3), F(-1), F(1, 2), F(1, 6),
                                                     F(-1, 6), F(-1, 2), F(1), F(2, 3), F(1, 3)])
    count = 0
    seen = 0
    for ms in product(range(2), repeat=len(irreps)):
        Fm = {lam: mlt for lam, mlt in zip(irreps, ms) if mlt}
        if not Fm:
            continue
        sc = selfconj(V_of(Fm))
        a = Fm.get((0, 0), 0)
        b = Fm.get((1, 0), 0)
        assert sc == (Fm == ab_form(a, b) and Fm.get((1, 1), 0) == a)
        count += sc
        seen += 1
    assert count == 3 and seen == 1023    # (0,0)+(1,1), (1,0), (0,0)+(1,0)+(1,1)
    for a in range(4):
        for b in range(4):
            assert selfconj(V_of(ab_form(a, b)))
            for extra in [(2, 0), (2, 1), (2, 2), (3, 0)]:
                G2 = dict(ab_form(a, b))
                G2[extra] = 1
                assert not selfconj(V_of(G2))
    return True


def gl2_action_on_pairs(X):
    """X in gl(2) acting on C^2 (x) C^2 as X (x) 1 + 1 (x) X (4x4)."""
    M = [[F(0)] * 4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    M[2 * i + j][2 * k + l] = X[i][k] * (1 if j == l else 0) + X[j][l] * (1 if i == k else 0)
    return M


def equivariant_maps(src_gens, tgt_gens, ds, dt):
    """Basis of {T : T S_g = T_g T} for matrices T (dt x ds), solved with GA.field_kernel."""
    rows = []
    for S, Tg in zip(src_gens, tgt_gens):
        for r in range(dt):
            for s in range(ds):
                row = [F(0)] * (dt * ds)
                for k in range(ds):
                    row[r * ds + k] += S[k][s]
                for k in range(dt):
                    row[k * ds + s] -= Tg[r][k]
                rows.append(row)
    ker = GA.field_kernel([[GA.qi(x) for x in row] for row in rows])
    return [[[v[r * ds + s].re for s in range(ds)] for r in range(dt)] for v in ker]


def check_generation_forces_fermionic_slots():
    premise("standard-model.imported-pair-systems-two-chirality-halves")
    premise("standard-model.global-form-quotient-determined")
    gens = [[[F(1), F(0)], [F(0), F(0)]], [[F(0), F(1)], [F(0), F(0)]],
            [[F(0), F(0)], [F(1), F(0)]], [[F(0), F(0)], [F(0), F(1)]]]
    src = [gl2_action_on_pairs(X) for X in gens]
    # Lambda^2 C^2: X acts by trace; Sym^2 C^2 in basis e1e1, e1e2, e2e2
    lam2 = [[[X[0][0] + X[1][1]]] for X in gens]

    def sym2(X):
        return [[2 * X[0][0], X[0][1], F(0)], [2 * X[1][0], X[0][0] + X[1][1], 2 * X[0][1]],
                [F(0), X[1][0], 2 * X[1][1]]]
    homL = equivariant_maps(src, lam2, 4, 1)
    homS = equivariant_maps(src, [sym2(X) for X in gens], 4, 3)
    assert len(homL) == 1 and len(homS) == 1
    sym_tensors = [[1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1]]
    alt = [0, 1, -1, 0]
    T = homL[0]
    assert all(sum(T[0][i] * v[i] for i in range(4)) == 0 for v in sym_tensors)
    assert sum(T[0][i] * alt[i] for i in range(4)) != 0
    S = homS[0]
    assert all(sum(S[r][i] * alt[i] for i in range(4)) == 0 for r in range(3))
    # generated modules: F_0 = C, F_{n+1} a quotient of C^2 (x) F_n; Pieri rule for the constituents
    def pieri(lam):
        l1, l2 = lam
        out = [(l1 + 1, l2)]
        if l2 + 1 <= l1:
            out.append((l1, l2 + 1))
        return out
    survivors = []
    frontier = [({(0, 0): 1}, {(0, 0): 1})]
    for _ in range(4):
        nxt = []
        for Fm, top in frontier:
            cons = Counter()
            for lam, mlt in top.items():
                for mu in pieri(lam):
                    cons[mu] += mlt
            keys = sorted(cons)
            for ch in product(*[range(cons[k] + 1) for k in keys]):
                new = {k: x for k, x in zip(keys, ch) if x}
                G2 = dict(Fm)
                for k, x in new.items():
                    G2[k] = G2.get(k, 0) + x
                if not new:
                    continue
                if selfconj(V_of(G2)):
                    survivors.append(G2)
                nxt.append((G2, new))
        frontier = nxt
    assert survivors == [{(0, 0): 1, (1, 0): 1, (1, 1): 1}]
    # the bosonic generated module Sym C^2 truncated anywhere is never CPT-closed
    for top in range(1, 5):
        assert not selfconj(V_of({(l, 0): 1 for l in range(top + 1)}))
    return True


def check_anomaly_free_halvings():
    premise("standard-model.imported-anomaly-coefficients")
    premise("standard-model.global-form-quotient-determined")
    premise("standard-model.imported-pair-systems-two-chirality-halves")
    for b in range(6):
        good = anomaly_free(V_of(ab_form(1, b)))
        assert len(good) == (2 if b % 2 else 0)
        for h in good:
            assert cubic_su3(h) == 0 and doublets(h) % 2 == 0
    # the four conditions on the five net chiralities (e1, e2, e3, s_t, s_u) have a one-dimensional
    # solution space, spanned by the tower-grading choice (-1, 1, -1, -1, 1)
    rows = [[F(-1), F(-2), F(-1), F(1), F(1)],
            [F(0), F(0), F(0), F(1, 2), F(1, 2)],
            [F(-1, 3), F(-2, 3), F(0), F(0), F(1, 3)],
            [F(-1, 9), F(-8, 9), F(-1), F(1, 4), F(1, 36)]]
    ker = GA.field_kernel([[GA.qi(x) for x in r] for r in rows])
    assert len(ker) == 1
    v = [z.re for z in ker[0]]
    assert [x / v[1] for x in v] == [-1, 1, -1, -1, 1]
    # the coefficients are those of the four sums
    reps = [(0, '3', F(-1, 3)), (0, '3b', F(-2, 3)), (0, '1', F(-1)), (1, '1', F(1, 2)), (1, '3', F(1, 6))]
    for col, R in enumerate(reps):
        assert list(four(Counter({R: 1}))) == [rows[i][col] for i in range(4)]
    # b = 3: one generation plus a vectorlike quark doublet pair and a vectorlike lepton doublet pair
    good3 = anomaly_free(V_of(ab_form(1, 3)))
    for h in good3:
        assert h[(1, '3', F(1, 6))] + h[(1, '3b', F(-1, 6))] == 3
        assert abs(h[(1, '3', F(1, 6))] - h[(1, '3b', F(-1, 6))]) == 1
    return True


def check_chirality_is_mode_parity():
    premise("standard-model.imported-anomaly-coefficients")
    premise("standard-model.global-form-quotient-determined")
    premise("standard-model.imported-pair-systems-two-chirality-halves")
    Fm = ab_form(1, 1)
    good = anomaly_free(V_of(Fm))
    even, odd = half_by_parity(Fm, 1, 0), half_by_parity(Fm, 1, 1)
    neutral = (0, '1', F(0))
    strip = lambda h: Counter({R: m for R, m in h.items() if R != neutral})   # noqa: E731
    assert sorted(map(lambda h: sorted(strip(h).items()), good)) == \
        sorted([sorted(strip(even).items()), sorted(strip(odd).items())])
    assert even[neutral] == 1 and odd[neutral] == 1          # the neutral line is the free choice
    # the even half is one generation: Q, u^c, d^c, L, e^c, nu^c
    assert strip(even) == Counter({(1, '3', F(1, 6)): 1, (0, '3b', F(-2, 3)): 1, (0, '3b', F(1, 3)): 1,
                                   (1, '1', F(-1, 2)): 1, (0, '1', F(1)): 1})
    # at slot parity 0 neither tower-grading half is anomaly-free (the grading is not the chirality)
    assert four(half_by_parity(Fm, 0, 0)) != (0, 0, 0, 0)
    assert four(half_by_parity(Fm, 0, 1)) != (0, 0, 0, 0)
    assert four(even) == (0, 0, 0, 0) and four(odd) == (0, 0, 0, 0)
    return True
