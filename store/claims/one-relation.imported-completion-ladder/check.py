"""one-relation.imported-completion-ladder: exact checks of the finite stages of the ladder.

(1) The minimal null-lift completion adjoins one hyperbolic plane (1,1): with the conformal model
    exported by the transport.minimality check, the lift X(x) of every sample x is null and the
    signature is (p+1, q+1), for 10 signatures.
(2) The tower: with rungs j = 1..k (generators e+_j, e-_j, f_j = e+_j e-_j) and twisted generators
    e_i' = e_i f_1 ... f_k, the e_i' satisfy the relations of Cl(p,q), commute with every rung
    generator, and the products (A' blade) x (rung blade) span Cl(p+k, q+k) (rank 2^(n+2k)):
    Cl(p+k, q+k) = Cl(p,q) (x) Cl(k,k). The rung algebra Cl(k,k) is Mat(2^k, R): the vacuum
    projector P = prod a_j a_j^dagger has corner P Cl(k,k) P of dimension 1 and left ideal
    Cl(k,k) P of dimension 2^k. Cases: n <= 2 with k = 1, 2; n = 3 with k = 1.
(3) One fermionic mode per rung: a_j = (e+_j + e-_j)/2, a_j^dagger = (e+_j - e-_j)/2 satisfy the
    CAR across rungs ({a_j, a_l^dagger} = delta_jl, {a_j, a_l} = 0) for k <= 3.
The completed limit Cl(p,q)_C (x) CAR (an inductive limit) is not tested beyond its finite
stages, which are (2) complexified; the odd-charge limit is stated as open.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def _rank(elems, m):
    blades = GA.all_blades(m)
    rows = [GA.basis_vector_of(x, blades) for x in elems if x]
    return GA.rank_of_vectors(rows) if rows else 0


def _tower(p, q, k):
    n = p + q
    sq = GA.sig(p, q) + (1, -1) * k
    rungs = [(GA.gen(n + 2 * j), GA.gen(n + 2 * j + 1)) for j in range(k)]
    Fprod = GA.sc(1)
    for ep, em in rungs:
        Fprod = GA.mul(Fprod, GA.mul(ep, em, sq), sq)
    twisted = [GA.mul(GA.gen(i), Fprod, sq) for i in range(n)]
    return n, sq, rungs, twisted


def _modes(rungs, sq):
    out = []
    for ep, em in rungs:
        out.append((GA.scal(F(1, 2), GA.add(ep, em)), GA.scal(F(1, 2), GA.sub(ep, em))))
    return out


# Sample signatures (p, q) of the base Cl(p,q), and sample coordinate lists (truncated to n) for x.
SIGNATURES = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (1, 2), (1, 3), (3, 1), (2, 2), (0, 3)]
POINT_COORDS = ([1, 2, -1, 3], [2, F(1, 3), 0, 1])
# Sample rung counts k for the CAR check, on the base Cl(1,1).
CAR_RUNG_COUNTS = (1, 2, 3)
CAR_BASE = (1, 1)


def check_one_hyperbolic_plane_per_completion():
    ex = premise("transport.minimality")
    conformal = ex["conformal"]
    ok = True
    for (p, q) in SIGNATURES:
        M = conformal(p, q)
        n, sq = M["n"], M["sq"]
        for cs in POINT_COORDS:
            Xx = M["X"](M["vec"](cs[:n]))
            ok = ok and GA.is_zero(GA.mul(Xx, Xx, sq))
        G = [[GA.dot(GA.gen(i), GA.gen(j), sq) for j in range(len(sq))] for i in range(len(sq))]
        ok = ok and GA.congruence_signature(G) == (p + 1, q + 1, 0)
    GA.check("each completion step adjoins one hyperbolic plane (1,1)", ok)
    return ok


def check_tower_is_matrix_amplification():
    premise("tower.answers-iteration-question")
    ok = True
    cases = [(p, n - p, k) for n in range(0, 3) for p in range(n + 1) for k in (1, 2)]
    cases += [(p, 3 - p, 1) for p in range(4)]
    for (p, q, k) in cases:
        n, sq, rungs, tw = _tower(p, q, k)
        m = n + 2 * k
        base = GA.sig(p, q)
        for i in range(n):
            ok = ok and GA.eq(GA.mul(tw[i], tw[i], sq), GA.sc(base[i]))
            for j in range(i + 1, n):
                ok = ok and GA.anticommutes(tw[i], tw[j], sq)
            for ep, em in rungs:
                ok = ok and GA.commutes(tw[i], ep, sq) and GA.commutes(tw[i], em, sq)
        rung_gens = [g for pair in rungs for g in pair]
        prods = []
        for b in GA.all_blades(n):
            a = GA.sc(1)
            for i in b:
                a = GA.mul(a, tw[i], sq)
            for c in GA.all_blades(2 * k):
                r = GA.sc(1)
                for i in c:
                    r = GA.mul(r, rung_gens[i], sq)
                prods.append(GA.mul(a, r, sq))
        ok = ok and _rank(prods, m) == 2 ** (n + 2 * k)
        # the rung algebra is Mat(2^k, R)
        P = GA.sc(1)
        for a, ad in _modes(rungs, sq):
            P = GA.mul(P, GA.mul(a, ad, sq), sq)
        ok = ok and GA.eq(GA.mul(P, P, sq), P)
        rung_blades = []
        for c in GA.all_blades(2 * k):
            r = GA.sc(1)
            for i in c:
                r = GA.mul(r, rung_gens[i], sq)
            rung_blades.append(r)
        corner = [GA.mul(GA.mul(P, r, sq), P, sq) for r in rung_blades]
        left = [GA.mul(r, P, sq) for r in rung_blades]
        ok = ok and _rank(corner, m) == 1 and _rank(left, m) == 2 ** k
    ok = ok and len(cases) == 16
    GA.check("Cl(p+k,q+k) = Cl(p,q) (x) Mat(2^k,R) by twisted generators, 16 cases", ok)
    return ok


def check_one_fermionic_mode_per_rung():
    premise("tower.car-limit-even-charge")
    ok = True
    for k in CAR_RUNG_COUNTS:
        n, sq, rungs, _ = _tower(*CAR_BASE, k)
        modes = _modes(rungs, sq)
        for j, (a, ad) in enumerate(modes):
            for l, (b, bd) in enumerate(modes):
                anti = GA.add(GA.mul(a, bd, sq), GA.mul(bd, a, sq))
                ok = ok and GA.eq(anti, GA.sc(1) if j == l else {})
                ok = ok and GA.is_zero(GA.add(GA.mul(a, b, sq), GA.mul(b, a, sq)))
                ok = ok and GA.is_zero(GA.add(GA.mul(ad, bd, sq), GA.mul(bd, ad, sq)))
    GA.check("each rung adjoins one fermionic mode: the CAR hold across k <= 3 rungs", ok)
    return ok
