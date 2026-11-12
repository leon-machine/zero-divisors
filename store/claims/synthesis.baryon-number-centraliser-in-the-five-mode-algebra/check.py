"""synthesis.baryon-number-centraliser-in-the-five-mode-algebra: exact checks.

The five-mode algebra is Cl(5,5) over the rationals, computed with GA.py: generators e_1..e_5 of
square +1 (indices 0..4) and f_1..f_5 of square -1 (indices 5..9), set v_i = (e_i + f_i)/2 and
clear w_i = (e_i - f_i)/2, n_i = v_i w_i. Modes 1, 2, 3 are the pairs and 4, 5 the slots.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

SQ = GA.sig(5, 5)
ONE = GA.sc(1)


def mul(*xs):
    r = xs[0]
    for x in xs[1:]:
        r = GA.mul(r, x, SQ)
    return r


def comm(a, b):
    return GA.sub(mul(a, b), mul(b, a))


def acomm(a, b):
    return GA.add(mul(a, b), mul(b, a))


E = [GA.gen(i) for i in range(5)]
Fm = [GA.gen(5 + i) for i in range(5)]
V = [GA.scal(F(1, 2), GA.add(E[i], Fm[i])) for i in range(5)]
W = [GA.scal(F(1, 2), GA.sub(E[i], Fm[i])) for i in range(5)]
N = [mul(V[i], W[i]) for i in range(5)]
PAIRS, SLOTS = (0, 1, 2), (3, 4)


def parity(idx):
    return mul(*[GA.sub(ONE, GA.scal(2, N[i])) for i in idx])


K = GA.add(*[N[a] for a in PAIRS])
J = GA.add(*[N[s] for s in SLOTS])
P = parity(PAIRS)                       # pair parity
GAM = parity(range(5))                  # parity of the total mode number
CHI = GA.neg(parity(SLOTS))             # rung parity: +1 on one occupied slot
BL = GA.sub(ONE, GA.scal(F(2, 3), K))   # B - L in pair-number form
NB = GA.scal(F(1, 4), GA.sub(BL, P))
NL = GA.scal(F(-1, 4), GA.add(P, GA.scal(3, BL)))
T = mul(*V)
TD = mul(*reversed(W))
HALF = GA.scal(F(1, 2), ONE)

U3 = [mul(V[a], W[b]) for a in PAIRS for b in PAIRS if a != b] + [GA.sub(N[a], HALF) for a in PAIRS]
LQ = [mul(V[a], V[b]) for a, b in combinations(PAIRS, 2)] + [mul(W[a], W[b]) for a, b in combinations(PAIRS, 2)]
SO4 = [mul(V[3], W[4]), mul(V[4], W[3]), mul(V[3], V[4]), mul(W[4], W[3]),
       GA.sub(N[3], HALF), GA.sub(N[4], HALF)]
MIX = [mul(x[s], y[a]) for s in SLOTS for a in PAIRS for x in (V, W) for y in (V, W)]
BIV = [mul(g, h) for g, h in combinations(E + Fm, 2)]


def exchange(x):
    """The exchange of set and clear on all five modes: f_i -> -f_i."""
    return {b: (c if sum(1 for i in b if i >= 5) % 2 == 0 else -c) for b, c in x.items()}


def rank(elements):
    blades = sorted({b for x in elements for b in x})
    if not blades:
        return 0
    return GA.rank_of_vectors([[x.get(b, F(0)) for b in blades] for x in elements])


def commuting_dimension(q, basis):
    return len(basis) - rank([comm(q, x) for x in basis])


def proportional(x, y):
    return rank([x, y]) < 2


def check_baryon_and_lepton_number_as_elements():
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.under-s-composites-state-space-spinor")
    premise("standard-model.proton-decay-only-through-slot-pair")
    for i in range(5):
        assert mul(V[i], V[i]) == {} and mul(W[i], W[i]) == {}
        for j in range(5):
            assert acomm(V[i], W[j]) == (ONE if i == j else {})
            if i != j:
                assert acomm(V[i], V[j]) == {} and acomm(W[i], W[j]) == {}
    # spectral projections of the pair number: k (k-1)(k-2)(k-3) = 0
    km = [GA.sub(K, GA.sc(c)) for c in range(4)]
    assert mul(*km) == {}
    proj = [GA.scal(F(-1, 6), mul(km[1], km[2], km[3])), GA.scal(F(1, 2), mul(km[0], km[2], km[3])),
            GA.scal(F(-1, 2), mul(km[0], km[1], km[3])), GA.scal(F(1, 6), mul(km[0], km[1], km[2]))]
    assert GA.eq(GA.add(*proj), ONE)
    nb_values = [F(0), F(1, 3), F(-1, 3), F(0)]
    nl_values = [F(-1), F(0), F(0), F(1)]
    for kap in range(4):
        assert GA.eq(mul(proj[kap], proj[kap]), proj[kap]) and proj[kap] != {}
        assert GA.eq(mul(NB, proj[kap]), GA.scal(nb_values[kap], proj[kap]))
        assert GA.eq(mul(NL, proj[kap]), GA.scal(nl_values[kap], proj[kap]))
        assert GA.eq(mul(BL, proj[kap]), GA.scal(1 - F(2, 3) * kap, proj[kap]))
    # on the sixteen (even total mode number) these are the stored expressions with chi
    even = GA.scal(F(1, 2), GA.add(ONE, GAM))
    odd = GA.scal(F(1, 2), GA.sub(ONE, GAM))
    assert GA.eq(mul(CHI, GAM), GA.neg(P))
    assert GA.eq(mul(NB, even), mul(GA.scal(F(1, 4), GA.add(BL, CHI)), even))
    assert GA.eq(mul(NL, even), mul(GA.scal(F(1, 4), GA.sub(CHI, GA.scal(3, BL))), even))
    assert GA.eq(mul(NB, odd), mul(GA.scal(F(1, 4), GA.sub(BL, CHI)), odd))
    # the stored chi form extended verbatim to the odd half is off by chi/2 there
    stored = GA.scal(F(1, 4), GA.add(BL, CHI))
    assert GA.eq(mul(GA.sub(stored, NB), odd), mul(GA.scal(F(1, 2), CHI), odd))
    assert mul(GA.sub(stored, NB), even) == {}
    assert GA.eq(mul(GA.add(GA.scal(3, NB), NL), even), mul(CHI, even))
    # grades: B - L is a bivector, the grading element of the three pairs; n_B is not a bivector
    assert GA.eq(BL, GA.scal(F(1, 3), GA.add(*[mul(E[a], Fm[a]) for a in PAIRS])))
    assert GA.eq(P, GA.neg(mul(E[0], E[1], E[2], Fm[0], Fm[1], Fm[2])))
    assert sorted({len(b) for b in NB}) == [2, 6] and sorted({len(b) for b in NL}) == [2, 6]
    for a in PAIRS:
        assert GA.eq(comm(K, V[a]), V[a]) and GA.eq(comm(K, W[a]), GA.neg(W[a]))
        assert GA.eq(comm(BL, V[a]), GA.scal(F(-2, 3), V[a]))
        assert sorted({len(b) for b in comm(NB, E[a])}) == [1, 5]
    return True


def check_centraliser_is_the_shifts_by_multiples_of_three():
    premise("standard-model.proton-decay-only-through-slot-pair")
    subsets = [s for r in range(4) for s in combinations(PAIRS, r)]
    assert len(subsets) == 8
    count = {d: 0 for d in range(-3, 4)}
    commuting = {d: 0 for d in range(-3, 4)}
    monomials = []
    for s in subsets:
        for t in subsets:
            m = mul(ONE, *[V[a] for a in s], *[W[a] for a in t])
            assert m != {}
            d = len(s) - len(t)
            assert GA.eq(comm(K, m), GA.scal(d, m))
            count[d] += 1
            if comm(NB, m) == {}:
                commuting[d] += 1
            monomials.append(m)
    assert rank(monomials) == 64                       # a basis of the pair algebra Cl(3,3)
    assert [count[d] for d in range(-3, 4)] == [1, 6, 15, 20, 15, 6, 1]
    assert [commuting[d] for d in range(-3, 4)] == [1, 0, 0, 20, 0, 0, 1]
    assert commuting_dimension(NB, monomials) == 22    # the centraliser in the pair algebra
    assert commuting_dimension(K, monomials) == 20
    assert commuting_dimension(NL, monomials) == 38    # lepton number: 1 + 36 + 1, a different class
    # slot generators commute with n_B, so the centraliser in Cl(5,5) is 22 * 16 = 352
    for s in SLOTS:
        assert comm(NB, V[s]) == {} and comm(NB, W[s]) == {}
    slot_subsets = [s for r in range(3) for s in combinations(SLOTS, r)]
    slot_monomials = [mul(ONE, *[V[s] for s in a], *[W[s] for s in b]) for a in slot_subsets for b in slot_subsets]
    assert rank(slot_monomials) == 16 and all(comm(NB, x) == {} for x in slot_monomials)
    # 352 and 320 by the multiplicities of the values on the 32 states (8 pair states times 4 slot states)
    mult = [1, 3, 3, 1]
    assert (4 * (mult[0] + mult[3])) ** 2 + (4 * mult[1]) ** 2 + (4 * mult[2]) ** 2 == 22 * len(slot_monomials) == 352
    assert sum((4 * z) ** 2 for z in mult) == 20 * len(slot_monomials) == 320
    # a mixed element: the part of shift 1 obstructs
    assert comm(NB, GA.add(mul(V[0], W[1]), V[2])) != {}
    return True


def check_table_of_the_forty_five():
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    premise("standard-model.proton-decay-only-through-slot-pair")
    assert (len(U3), len(SO4), len(LQ), len(MIX)) == (9, 6, 6, 24)
    assert rank(U3 + SO4 + LQ + MIX) == 45 and rank(BIV) == 45
    assert rank(BIV + U3 + SO4 + LQ + MIX) == 45       # the typed generators span the bivectors
    assert commuting_dimension(NB, BIV) == 15
    assert commuting_dimension(BL, BIV) == 15
    assert commuting_dimension(P, BIV) == 21
    assert commuting_dimension(CHI, BIV) == 21
    for x in U3 + SO4:
        assert comm(NB, x) == {} and comm(NL, x) == {} and comm(BL, x) == {}
    for x in LQ:
        assert comm(P, x) == {} and comm(CHI, x) == {}
        assert comm(NB, x) != {}
        assert GA.eq(comm(NB, x), GA.scal(F(1, 4), comm(BL, x)))
        assert proportional(comm(BL, x), x)
    assert all(GA.eq(comm(BL, x), GA.scal(F(-4, 3), x)) for x in LQ[:3])
    assert all(GA.eq(comm(BL, x), GA.scal(F(4, 3), x)) for x in LQ[3:])
    for x in MIX:
        assert acomm(P, x) == {} and acomm(CHI, x) == {}
        assert comm(NB, x) != {}
        assert not proportional(comm(NB, x), x)      # no weight of the generator compensates
        assert proportional(comm(BL, x), x)
    return True


def check_majorana_element_and_rung_vectors():
    premise("standard-model.majorana-element")
    premise("standard-model.bidoublet-complex")
    assert comm(NB, T) == {} and comm(NB, TD) == {}
    assert GA.eq(comm(BL, T), GA.scal(-2, T))
    assert GA.eq(comm(NL, T), GA.scal(2, T))
    assert GA.eq(comm(K, T), GA.scal(3, T))
    assert acomm(P, T) == {}
    for x in U3[:6] + SO4[:2] + [GA.sub(N[3], N[4])]:
        assert comm(x, T) == {}                        # su(3) and su(2)_L
    hyper = GA.add(GA.scal(F(1, 2), GA.sub(J, ONE)), GA.scal(F(1, 2), BL))
    assert comm(hyper, T) == {}
    for s in SLOTS:                                    # rung vectors a v_s + b w_s
        c = GA.add(GA.scal(F(3, 7), V[s]), GA.scal(F(-5, 2), W[s]))
        assert comm(NB, c) == {} and comm(NL, c) == {} and comm(BL, c) == {}
    for a in PAIRS:                                    # a vector of a pair plane is outside all three
        for q in (NB, NL, BL):
            assert comm(q, V[a]) != {} and comm(q, W[a]) != {}
    for x in LQ + MIX:                                 # (vi), last sentence
        assert comm(NB, x) != {}
    # a product of members stays inside: conjugation by an invertible member fixes n_B
    u = GA.add(ONE, GA.scal(F(1, 3), T), GA.scal(F(2, 5), TD), GA.scal(F(1, 2), mul(V[0], W[1])))
    assert comm(NB, u) == {} and comm(BL, u) != {}
    return True


def check_exchange_reverses_the_charges():
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    premise("standard-model.majorana-element")
    for i in range(5):
        assert GA.eq(exchange(V[i]), W[i]) and GA.eq(exchange(W[i]), V[i])
    u = mul(*E)
    assert mul(u, u) == ONE
    for x in V + W + [NB, T, MIX[5]]:
        assert GA.eq(mul(u, x, u), exchange(x))
    for q in (NB, NL, BL, P, GAM):
        assert GA.eq(exchange(q), GA.neg(q))
    assert GA.eq(exchange(CHI), CHI)
    assert GA.eq(exchange(T), TD)
    for family in (U3, SO4, LQ, MIX):
        assert rank(family + [exchange(x) for x in family]) == len(family)
    su2l = SO4[:2] + [GA.sub(N[3], N[4])]
    assert rank(su2l + [exchange(x) for x in su2l]) == 3
    return True
