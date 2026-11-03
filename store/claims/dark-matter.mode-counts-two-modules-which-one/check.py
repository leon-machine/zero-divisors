"""dark-matter.mode-counts-two-modules-which-one: exact checks.

(i) Rung factor: for every populated P3 representative (r = 6, 2, 1, 7, 3, 5) min(p,q) = 1 mutually
orthogonal null vectors e_i + e_(p+i) are exhibited (isotropy exact) and dim U^perp = n - min(p,q);
at rung height k the signature is (p+k, q+k), Witt index 1 + k in every tower. The Fock factor: in
Cl(k,k) the k null pairs satisfy the CAR and the left ideal Cl(k,k) f, f = w_1...w_k, has real
dimension 2^k (k = 1, 2, 3), the same for every tower.
(ii) Ground module: from the type computation exported by type-residue-what-each-tower-can (GA.py,
primitive idempotent certified by its corner's trace form), dim_R S_r with both modules where the
centre splits (the P2 reading) is 8, 4, 4, 4, 8, 16 at r = 6, 2, 1, 7, 3, 5, and with one module 2 at
r = 1 and 8 at r = 5.
(iii) The weightings sum_(r != 6) n_r/n_6 = 9/2 (both) and 13/4 (one each), and in the opposite
convention (divide by the 4-dimensional real module) 10 and 15/2, computed from (ii).
(iv) The pair counts of the odd towers' conformal spinors: over C, the ambient of dimension 5 (three-
dimensional towers) and 7 (five-dimensional) carries 2 and 3 mutually orthogonal null vectors
(Gaussian rationals, rank over Q(i)) and their span has dim U^perp = N - m, so m <= N/2 is the maximum.
The mirror's weight 1 (iv) is the mirror theorem's content, checked in its own check; the conversion of
(iv) into mode counts for the odd towers is not determined, as the claim says.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

POP = [6, 2, 1, 7, 3, 5]
P3 = {6: (1, 3), 2: (3, 1), 1: (2, 1), 7: (1, 2), 3: (4, 1), 5: (1, 4)}


def isotropic_family(p, q):
    sq = GA.sig(p, q)
    n = p + q
    k = min(p, q)
    us = [[F(1) if j in (i, p + i) else F(0) for j in range(n)] for i in range(k)]
    ip = lambda a, b: sum(F(sq[j]) * a[j] * b[j] for j in range(n))
    ok = all(ip(a, b) == 0 for a in us for b in us) and GA.rank_of_vectors(us) == k
    perp = n - GA.rank_of_vectors([[F(sq[j]) * u[j] for j in range(n)] for u in us])
    return ok, k, perp


def check_rung_factor_is_residue_independent():
    premise("tower.witt-index-quantum-capacity")
    premise("tower.fock-module-one-qubit-per-rung")
    premise("dark-matter.p1-single-frozen-point")
    ok = True
    for r in POP:
        p, q = P3[r]
        good, k, perp = isotropic_family(p, q)
        ok = ok and good and k == 1 and perp == p + q - 1
        for h in (1, 2, 3):
            good, kk, perp = isotropic_family(p + h, q + h)
            ok = ok and good and kk == 1 + h
    for k in (1, 2, 3):
        sq = GA.sig(k, k)
        w = [GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(k + i))) for i in range(k)]
        v = [GA.scal(F(1, 2), GA.sub(GA.gen(i), GA.gen(k + i))) for i in range(k)]
        ok = ok and all(GA.eq(GA.add(GA.mul(v[i], w[j], sq), GA.mul(w[j], v[i], sq)), GA.sc(1 if i == j else 0))
                        for i in range(k) for j in range(k))
        f = GA.sc(1)
        for x in w:
            f = GA.mul(f, x, sq)
        bl = GA.all_blades(2 * k)
        dim = GA.rank_of_vectors([[GA.mul({b: F(1)}, f, sq).get(c, F(0)) for c in bl] for b in bl])
        ok = ok and dim == 2 ** k
    GA.check("thm:modes(i): Witt index 1 for every populated representative, 1 + k at height k; Fock factor "
             "of dimension 2^k (k = 1, 2, 3)", ok)
    return ok


def ground_dims():
    ct = premise("dark-matter.type-residue-what-each-tower-can")["clifford_type"]
    both, single = {}, {}
    for r in POP:
        t = ct(*P3[r])
        both[r] = t["dimS"] * t["comps"]
        single[r] = t["dimS"]
    return both, single


def check_ground_module_dimensions():
    premise("dark-matter.p2-indifference")
    both, single = ground_dims()
    ok = both == {6: 8, 2: 4, 1: 4, 7: 4, 3: 8, 5: 16}
    ok = ok and single[1] == 2 and single[5] == 8
    GA.check("thm:modes(ii): dim S_r = 8, 4, 4, 4, 8, 16 (both modules), 2 and 8 at r = 1, 5 (one each)", ok)
    return ok


def check_weightings_depend_on_the_convention():
    premise("dark-matter.p2-indifference")
    both, single = ground_dims()
    s_both = sum(F(both[r], both[6]) for r in POP if r != 6)
    s_single = sum(F(single[r], single[6]) for r in POP if r != 6)
    o_both = sum(F(both[r], both[2]) for r in POP if r != 2)
    o_single = sum(F(single[r], single[2]) for r in POP if r != 2)
    terms = [F(both[r], both[6]) for r in (2, 1, 7, 3, 5)]
    ok = terms == [F(1, 2), F(1, 2), F(1, 2), 1, 2]
    ok = ok and s_both == F(9, 2) and s_single == F(13, 4) and o_both == 10 and o_single == F(15, 2)
    ok = ok and sum(both[r] for r in POP if r != 2) == 40 and sum(single[r] for r in POP if r != 2) == 30
    GA.check("thm:modes(iii): weightings 9/2 and 13/4; opposite convention 40/4 = 10 and 30/4 = 15/2", ok)
    return ok


def check_odd_tower_pair_counts():
    ok = True
    counts = {}
    for N in (5, 7, 6):
        m = N // 2
        sq = [1] * (N - m) + [-1] * m if N == 6 else [1] * N
        i_ = GA.QI_I
        # over C every form is equivalent to the sum of squares; null pairs e_a + i e_b
        U = []
        for a in range(m):
            v = [GA.qi(0)] * N
            v[2 * a] = GA.qi(1)
            v[2 * a + 1] = i_ if sq[2 * a + 1] == 1 else GA.qi(1)
            if sq[2 * a] == -1:
                v[2 * a] = i_
            U.append(v)
        bil = lambda x, y: sum((x[k] * y[k] * sq[k] for k in range(N)), GA.qi(0))
        ok = ok and all(bil(x, y) == 0 for x in U for y in U) and GA.field_rank(U) == m
        perp = N - GA.field_rank([[x[k] * sq[k] for k in range(N)] for x in U])
        ok = ok and perp == N - m and m <= perp
        counts[N] = m
    ok = ok and counts == {5: 2, 7: 3, 6: 3}
    GA.check("thm:modes(iv): complex Witt index 2 (ambient 5, three-dimensional towers) and 3 (ambient 7, "
             "five-dimensional), 3 for ambient 6", ok)
    return ok
