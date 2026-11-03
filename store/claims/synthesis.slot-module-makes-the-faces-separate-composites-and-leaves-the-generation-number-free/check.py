"""Separate face composites and the free generation number: exact checks.

Exterior states of the modes are frozensets (GA's exterior model); weights are read from occupation
numbers, exactly, with Fractions.
(1) Polynomial irreducible representations of GL(2) of degree d are labelled by lam1 >= lam2 >= 0,
    lam1 + lam2 = d, of dimension lam1 - lam2 + 1: in degree one only the doublet, so F_1 is
    even-dimensional and, under (G), the doublet; the three-slot space is no slot module.
(2) In the shared space Lambda(S + W) (S = three slots, W = three pair modes) read with the gauge
    group of one face: the third slot has slot number one but weight zero under the face's centre
    (clause (a) fails); counted with the face's slot number every weight occurs exactly twice
    (two slot vacua, clause (G) fails); and the even half under the mode-number parity carries the
    weights of the face's whole module, particle half plus antiparticle half: it is vectorlike.
(3) One slot module (two slots, three pair modes, particle half of even mode number, Y = (3n - 2k)/6):
    every anomaly sum of the stored anomaly Fact vanishes, and the colour cubic, so n separate copies
    are anomaly-free for every n; four weak doublets per copy.
(4) The Dynkin sums of one copy give the stored running coefficients; colour asymptotically free
    exactly for n <= 8, weak isospin for n <= 5 at one or two doublets.
(5) In the spacetime algebra of three dimensions every bivector is a blade and
    (Xa) ^ (Xb) = det(X) X^{-T} acting through the dual: the face planes of a three-slot space span a
    three-dimensional space that is the dual triplet of the slot GL(3), twisted by det; C(N, 2) = N
    only for N = 3.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter

import GA
from tp_premise import premise


def states(nmodes):
    return [frozenset(s) for r in range(nmodes + 1) for s in combinations(range(nmodes), r)]


def colour_key(S, pair):
    return tuple(1 if p in S else 0 for p in pair)


def check_degree_one_slot_space_is_the_doublet():
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    premise("standard-model.slot-module-hypothesis")  # clauses (a) and (G), restated in (1)
    dims = {}
    for d in range(5):
        dims[d] = sorted((l1 - l2 + 1) for l1 in range(d + 1) for l2 in range(l1 + 1) if l1 + l2 == d)
        # torus weights (p, q), p + q = d, of the irreducible (l1, l2): q from l2 to l1
        for l1 in range(d + 1):
            for l2 in range(l1 + 1):
                if l1 + l2 != d:
                    continue
                wts = [(d - q, q) for q in range(l2, l1 + 1)]
                assert len(wts) == l1 - l2 + 1
                assert all(p + q == d and p >= 0 and q >= 0 for p, q in wts)
                assert sorted(wts) == sorted((q, p) for p, q in wts)         # Weyl symmetric
    assert dims == {0: [1], 1: [2], 2: [1, 3], 3: [2, 4], 4: [1, 3, 5]}
    assert all(x % 2 == 0 for x in dims[1])                                  # F_1 even-dimensional
    # (G): C^2 (x) F_0 -> F_1 onto with dim F_0 = 1 gives dim F_1 <= 2, so F_1 = C^2 or 0
    assert max(dims[1]) * 1 == 2
    # a three-slot one-slot space: 3 is not a sum of degree-one dimensions
    assert all(3 != k * dims[1][0] for k in range(4))
    return True


def check_shared_space_breaks_the_slot_module_for_one_face():
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    premise("synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group")
    slots, pair = [0, 1, 2], [3, 4, 5]
    allst = states(6)
    assert len(allst) == 64
    for face in [(0, 1), (0, 2), (1, 2)]:
        other = [s for s in slots if s not in face][0]
        # the face's centre mu*1 on the slots acts on a slot state as mu^(face slots occupied)
        bad = [S for S in allst if len(S & set(slots)) != len(S & set(face))]
        assert len(bad) == 32 and all(other in S for S in bad)
        one = frozenset([other])
        assert len(one & set(slots)) == 1 and len(one & set(face)) == 0       # (a) fails on it
        # regraded by the face's slot number: weight key (2 T3, n_F, colour occupation)
        def key(S):
            return (len(S & {face[0]}) - len(S & {face[1]}), len(S & set(face)), colour_key(S, pair))
        big = Counter(key(S) for S in allst)
        facemod = [S for S in allst if other not in S]
        assert len(facemod) == 32
        small = Counter(key(S) for S in facemod)
        assert set(big) == set(small) and all(big[k] == 2 * small[k] for k in small)
        f0 = [S for S in allst if not (S & set(pair)) and not (S & set(face))]
        assert len(f0) == 2                                                   # two slot vacua
        # the even half (mode-number parity) carries the whole face module's weights
        even = [S for S in allst if len(S) % 2 == 0]
        assert len(even) == 32
        assert Counter(key(S) for S in even) == small
        # it contains the face's particle half once and the antiparticle half once
        part = Counter(key(S) for S in facemod if len(S) % 2 == 0)
        anti = Counter(key(S) for S in facemod if len(S) % 2 == 1)
        assert Counter(key(S) for S in even if other not in S) == part
        assert Counter(key(S) for S in even if other in S) == anti
        # the injective map x -> e_other ^ x carries the odd face states onto the even shared ones
        vecs = []
        for S in facemod:
            if len(S) % 2 == 1:
                st = GA.ext_wedge(other, {S: F(1)})
                vecs.append([st.get(T, F(0)) for T in allst])
        assert GA.rank_of_vectors(vecs) == 16
    return True


def one_copy():
    """Particle half of one slot module: slots 0, 1; pairs 2, 3, 4; n + k even."""
    out = []
    for S in states(5):
        n = len(S & {0, 1})
        k = len(S & {2, 3, 4})
        if (n + k) % 2:
            continue
        Y = F(3 * n - 2 * k, 6)
        t3 = F(len(S & {0}) - len(S & {1}), 2)
        occ = [1 if p in S else 0 for p in (2, 3, 4)]
        h3 = F(occ[0] - occ[1], 2)                       # colour Cartan, tr over a triplet = 1/2
        h8 = F(occ[0] + occ[1] - 2 * occ[2])             # colour Cartan (1, 1, -2)
        # Lambda^2 C^3 carries -(h8 of the missing mode): weights of the pair states as stored
        out.append({"n": n, "k": k, "Y": Y, "t3": t3, "h3": h3, "h8": h8})
    return out


def check_separate_copies_are_anomaly_free_for_every_number():
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    premise("standard-model.imported-anomaly-coefficients")
    premise("synthesis.imported-witten-global-su2-anomaly")  # the doublet count 4n is even
    c = one_copy()
    assert len(c) == 16
    # the content: Y multiset of the particle half
    ys = Counter(s["Y"] for s in c)
    assert ys == Counter({F(1, 6): 6, F(-2, 3): 3, F(1, 3): 3, F(-1, 2): 2, F(1): 1, F(0): 1})
    for ncopy in range(1, 11):
        sY = ncopy * sum((s["Y"] for s in c), F(0))
        sY3 = ncopy * sum((s["Y"] ** 3 for s in c), F(0))
        s2 = ncopy * sum((s["Y"] * s["t3"] ** 2 for s in c), F(0))
        s3 = ncopy * sum((s["Y"] * s["h3"] ** 2 for s in c), F(0))
        c3 = ncopy * sum((s["h8"] ** 3 for s in c), F(0))
        assert (sY, sY3, s2, s3, c3) == (0, 0, 0, 0, 0)
        doublets = ncopy * sum((1 for s in c if s["n"] == 1), 0) // 2
        assert doublets == 4 * ncopy and doublets % 2 == 0
    # sensitivity: a wrong hypercharge normalisation (3n - k)/6 is anomalous
    bad = sum((F(3 * s["n"] - s["k"], 6) ** 3 for s in c), F(0))
    assert bad != 0
    # one copy without the neutral singlet (15 states) keeps the gauge sums: the singlet has Y = 0
    assert [s for s in c if s["n"] == 0 and s["k"] == 0][0]["Y"] == 0
    return True


def check_asymptotic_freedom_bounds_the_number():
    premise("synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces")
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    c = one_copy()
    t2 = sum((s["t3"] ** 2 for s in c), F(0))            # sum of T(R) over su(2) multiplets
    t3c = sum((s["h3"] ** 2 for s in c), F(0))           # sum of T(R) over su(3) multiplets
    assert (t2, t3c) == (2, 2)
    ok3, ok2 = [], {1: [], 2: []}
    for ng in range(1, 13):
        b3 = F(-11) + F(2, 3) * t3c * ng
        assert b3 == F(-11) + F(4 * ng, 3)
        if b3 < 0:
            ok3.append(ng)
        for nh in (1, 2):
            b2 = F(-22, 3) + F(2, 3) * t2 * ng + F(nh, 6)
            if b2 < 0:
                ok2[nh].append(ng)
    assert ok3 == list(range(1, 9))
    assert ok2[1] == list(range(1, 6)) and ok2[2] == list(range(1, 6))
    # the stored values at (3, 2)
    assert (F(-22, 3) + F(4 * 3, 3) + F(2, 6), F(-11) + F(4 * 3, 3)) == (F(-3), F(-7))
    return True


SQ3 = GA.sig(3, 0)


def v3(c):
    return {(i,): F(x) for i, x in enumerate(c) if x != 0}


def wedge2(a, b):
    return GA.scal(F(1, 2), GA.sub(GA.mul(a, b, SQ3), GA.mul(b, a, SQ3)))


def check_face_space_is_the_dual_triplet():
    premise("families.three-identical-families-mixing-shared-slots")
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    e = [v3([1 if i == j else 0 for i in range(3)]) for j in range(3)]
    faces = [wedge2(e[a], e[b]) for a, b in [(1, 2), (2, 0), (0, 1)]]
    blades = [(1, 2), (0, 2), (0, 1)]
    # the face blades span the bivectors (dimension 3) and every bivector is a blade: B ^ B = 0
    assert GA.rank_of_vectors([[f.get(b, F(0)) for b in blades] for f in faces]) == 3
    for co in [(1, 2, 3), (F(1, 2), -1, 4), (0, 5, -2)]:
        B = GA.add(*[GA.scal(F(co[i]), faces[i]) for i in range(3)])
        BB = GA.mul(B, B, SQ3)
        assert all(len(k) != 4 for k in BB)
    # (Xa) ^ (Xb) = det(X) X^{-T} (a x b) through the dual: with the dual coordinates of a ^ b
    def dual(B):
        return [B.get((1, 2), F(0)), -B.get((0, 2), F(0)), B.get((0, 1), F(0))]
    def app(X, a):
        return v3([sum((X[i][j] * a.get((j,), F(0)) for j in range(3)), F(0)) for i in range(3)])
    for X in [[[1, 2, 0], [0, 1, 3], [1, 0, 1]], [[2, 1, 1], [1, 3, 0], [0, -1, 2]]]:
        X = [[F(x) for x in r] for r in X]
        det = (X[0][0] * (X[1][1] * X[2][2] - X[1][2] * X[2][1])
               - X[0][1] * (X[1][0] * X[2][2] - X[1][2] * X[2][0])
               + X[0][2] * (X[1][0] * X[2][1] - X[1][1] * X[2][0]))
        cof = [[(X[(i + 1) % 3][(j + 1) % 3] * X[(i + 2) % 3][(j + 2) % 3]
                 - X[(i + 1) % 3][(j + 2) % 3] * X[(i + 2) % 3][(j + 1) % 3]) for j in range(3)]
               for i in range(3)]                                  # cof = det(X) X^{-T}
        for a, b in [(0, 1), (1, 2), (0, 2)]:
            lhs = dual(wedge2(app(X, e[a]), app(X, e[b])))
            d0 = dual(wedge2(e[a], e[b]))
            rhs = [sum((cof[i][j] * d0[j] for j in range(3)), F(0)) for i in range(3)]
            assert lhs == rhs
        inv_t_det = [[cof[i][j] / det for j in range(3)] for i in range(3)]
        assert all(sum((inv_t_det[k][i] * X[k][j] for k in range(3)), F(0)) == (1 if i == j else 0)
                   for i in range(3) for j in range(3))
    # C(N, 2) = N only at N = 3
    assert [N for N in range(1, 30) if N * (N - 1) // 2 == N] == [3]
    return True
