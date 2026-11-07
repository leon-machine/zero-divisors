"""Clause (f) of the slot-module hypothesis is a Klein convention on V: exact checks in Cl(5,5).

Realisation (the floor of synthesis.even-slots-need-a-spectator-generator): generators e_0..e_4 (square +1) and
f_0..f_4 (square -1), null pairs v_k = (e_k + f_k)/2, w_k = (e_k - f_k)/2 (v w + w v = 1 as vectors); modes 0, 1
are the slots, 2, 3, 4 the pairs; vacuum f = w_0 ... w_4; V is spanned by the 32 states x_K x_J f (pair
creators x_K to the left of slot creators x_J), so the pair vectors act as 1 (x) b and the slot vectors as the
Klein-twisted a (x) (-1)^k. Gamma_W = prod_p (1 - 2 v_p w_p) is the pair parity (-1)^k; the untwisted
(tensor-product) slot operators are v_i Gamma_W, w_i Gamma_W.

(1) Both conventions satisfy the slot CAR; the untwisted ones commute with every pair vector, the twisted ones
    (the vectors) anticommute; on the Fock basis they differ by the sign (-1)^k only (generation unchanged).
(2) Gamma_W = e_2 f_2 e_3 f_3 e_4 f_4 (one blade, 1 - 2 v w = e f); it commutes with every slot-slot and every
    pair-pair bilinear (so both conventions are covariant in the same way); the 6 slot-slot and 15 pair-pair
    Majorana bivectors (21) are the same elements in both conventions; the grading prod_k (1 - 2 v_k w_k)
    anticommutes with all ten twisted Majoranas and with the four untwisted slot Majoranas.
(3) Uniqueness: with the commutation form b(S, T) = |S||T| + |S cap T| mod 2 of
    synthesis.blade-square-signs-f2-quadratic-form (checked against the products), the only blade anticommuting
    with the six pair Majoranas and commuting with the four untwisted slot Majoranas is that of Gamma_W; so a
    twist K commuting with the slot operators and making them anticommute with the pairs is c Gamma_W, and the
    CAR hold for a_i K exactly when c^2 = 1 (c = 1, -1 pass, c = 2 fails).
Exact arithmetic only.
"""
from fractions import Fraction as F
from itertools import combinations
import GA
from tp_premise import premise

NM = 5
SQ = tuple([1] * NM + [-1] * NM)
EG = [GA.gen(k) for k in range(NM)]
FG = [GA.gen(NM + k) for k in range(NM)]
V = [GA.scal(F(1, 2), GA.add(EG[k], FG[k])) for k in range(NM)]
W = [GA.scal(F(1, 2), GA.sub(EG[k], FG[k])) for k in range(NM)]
SLOTS = [0, 1]
PAIRS = [2, 3, 4]


def _m(*xs):
    r = GA.sc(1)
    for x in xs:
        r = GA.mul(r, x, SQ)
    return r


def _parity(modes):
    g = GA.sc(1)
    for k in modes:
        g = _m(g, GA.sub(GA.sc(1), GA.scal(F(2), _m(V[k], W[k]))))
    return g


GW = _parity(PAIRS)
GTOT = _parity(range(NM))
VAC = _m(*W)


def _states():
    out = []
    for kk in range(len(PAIRS) + 1):
        for K in combinations(PAIRS, kk):
            for jj in range(len(SLOTS) + 1):
                for J in combinations(SLOTS, jj):
                    out.append((len(K), _m(*([V[p] for p in K] + [V[i] for i in J] + [VAC]))))
    return out


def _labelled_states():
    """{(K, J): x_K x_J f}, the identification with u_J (x) t_K of Step 1."""
    out = {}
    for kk in range(len(PAIRS) + 1):
        for K in combinations(PAIRS, kk):
            for jj in range(len(SLOTS) + 1):
                for J in combinations(SLOTS, jj):
                    out[(K, J)] = _m(*([V[p] for p in K] + [V[i] for i in J] + [VAC]))
    return out


def _matrix_entry(op, lab):
    """op on each labelled state as (target label, sign), or None for zero."""
    out = {}
    for key, s in lab.items():
        img = _m(op, s)
        out[key] = None
        if GA.is_zero(img):
            continue
        for key2, s2 in lab.items():
            for sg in (1, -1):
                if GA.eq(img, GA.scal(F(sg), s2)):
                    out[key] = (key2, sg)
    return out


def _acomm(x, y):
    return GA.add(_m(x, y), _m(y, x))


def _comm(x, y):
    return GA.sub(_m(x, y), _m(y, x))


def check_both_slot_conventions_obey_the_car_and_differ_by_the_pair_parity():
    premise("synthesis.even-slots-need-a-spectator-generator")
    tw = [(V[i], W[i]) for i in SLOTS]
    un = [(_m(V[i], GW), _m(W[i], GW)) for i in SLOTS]
    pair_ops = [V[p] for p in PAIRS] + [W[p] for p in PAIRS]
    ok_car = True
    for ops in (tw, un):
        for i in range(2):
            for j in range(2):
                ok_car = ok_car and GA.eq(_acomm(ops[i][0], ops[j][1]), GA.sc(1 if i == j else 0))
                ok_car = ok_car and GA.is_zero(_acomm(ops[i][0], ops[j][0]))
                ok_car = ok_car and GA.is_zero(_acomm(ops[i][1], ops[j][1]))
    GA.check("(1) both conventions satisfy the slot CAR", ok_car)
    GA.check("(1) untwisted slot operators commute with every pair operator",
             all(GA.is_zero(_comm(x, y)) for pr in un for x in pr for y in pair_ops))
    GA.check("(1) twisted slot operators anticommute with every pair operator",
             all(GA.is_zero(_acomm(x, y)) for pr in tw for x in pr for y in pair_ops))
    sts = _states()
    GA.check("(1) the 32 Fock states are independent",
             len(sts) == 32 and GA.rank_of_vectors([[s.get(b, F(0)) for b in GA.all_blades(10)] for _, s in sts]) == 32)
    ok_sign = True
    for k, s in sts:
        for i in range(2):
            for x, y in zip(tw[i], un[i]):
                ok_sign = ok_sign and GA.eq(_m(y, s), GA.scal(F((-1) ** k), _m(x, s)))
    GA.check("(1) on the Fock basis the two conventions differ by (-1)^k (same images: generation kept)", ok_sign)
    # Step 1's identification: in the basis x_K x_J f the untwisted v_i Gamma_W, w_i Gamma_W act as a (x) 1
    # (pair label kept, sign independent of K), the vectors as a (x) (-1)^k
    lab = _labelled_states()
    ok_un = ok_tw = True
    for i in range(2):
        for x, y in zip(tw[i], un[i]):
            mx, my = _matrix_entry(x, lab), _matrix_entry(y, lab)
            for (K, J), e in my.items():
                ref = my[((), J)]
                if e is None or ref is None:
                    ok_un = ok_un and (e is None) == (ref is None)
                    continue
                ok_un = ok_un and e[0][0] == K and e[0][1] == ref[0][1] and e[1] == ref[1]
                ok_tw = ok_tw and mx[(K, J)] == (e[0], e[1] * (-1) ** len(K))
    GA.check("(1) untwisted slot operators are a (x) 1 in the basis x_K x_J f", ok_un)
    GA.check("(1) the slot vectors are a (x) (-1)^k in that basis", ok_tw)


def check_split_preserving_bivectors_and_grading_are_convention_free():
    premise("synthesis.even-slots-need-a-spectator-generator")
    blade = _m(EG[2], FG[2], EG[3], FG[3], EG[4], FG[4])
    GA.check("(2) Gamma_W is the blade e2 f2 e3 f3 e4 f4 and squares to 1",
             GA.eq(GW, blade) and GA.eq(_m(GW, GW), GA.sc(1)))
    bil = [_m(x, y) for a in SLOTS for b in SLOTS for x in (V[a], W[a]) for y in (V[b], W[b])]
    bil += [_m(x, y) for a in PAIRS for b in PAIRS for x in (V[a], W[a]) for y in (V[b], W[b])]
    GA.check("(2) Gamma_W commutes with every slot-slot and pair-pair bilinear",
             all(GA.is_zero(_comm(GW, x)) for x in bil))
    smaj = [EG[i] for i in SLOTS] + [FG[i] for i in SLOTS]
    pmaj = [EG[p] for p in PAIRS] + [FG[p] for p in PAIRS]
    smaj_un = [_m(x, GW) for x in smaj]
    same = [GA.eq(_m(smaj[a], smaj[b]), _m(smaj_un[a], smaj_un[b])) for a, b in combinations(range(4), 2)]
    GA.check("(2) the 6 slot-slot Majorana bivectors agree in both conventions", len(same) == 6 and all(same))
    GA.check("(2) 6 + 15 = 21 split-preserving bivectors",
             len(same) + len(list(combinations(pmaj, 2))) == 21)
    GA.check("(2) the grading anticommutes with all ten twisted Majoranas",
             all(GA.is_zero(_acomm(GTOT, x)) for x in smaj + pmaj))
    GA.check("(2) and with the four untwisted slot Majoranas",
             all(GA.is_zero(_acomm(GTOT, x)) for x in smaj_un))
    # the residual sign c = -1 is Ad of the slot parity U = e0 f0 e1 f1 (central -1 of the slot U(2)):
    # U U~ = 1, U flips the slot Majoranas, fixes the pair ones, so negates the 24 cross bivectors
    U = _m(EG[0], FG[0], EG[1], FG[1])
    Ui = GA.reverse(U)
    cross = [_m(x, y) for x in smaj for y in pmaj]
    GA.check("(2) U = e0 f0 e1 f1 is the slot parity, U U~ = 1",
             GA.eq(U, _parity(SLOTS)) and GA.eq(_m(U, Ui), GA.sc(1)))
    GA.check("(2) Ad(U) flips the slot Majoranas, fixes the pair ones, negates the 24 cross bivectors",
             all(GA.eq(_m(U, x, Ui), GA.neg(x)) for x in smaj)
             and all(GA.eq(_m(U, x, Ui), x) for x in pmaj)
             and len(cross) == 24 and all(GA.eq(_m(U, x, Ui), GA.neg(x)) for x in cross))


def _bform(S, T):
    return (len(S) * len(T) + len(set(S) & set(T))) % 2


def check_the_klein_twist_is_unique_up_to_sign():
    premise("synthesis.blade-square-signs-f2-quadratic-form")
    P = (2, 3, 4, 7, 8, 9)
    pair_gens = [(p,) for p in P]
    slot_un = [tuple(sorted((i,) + P)) for i in (0, 1, 5, 6)]
    ok_form = True
    for S in GA.all_blades(10):
        for T in pair_gens + slot_un:
            anti = GA.anticommutes({S: F(1)}, {T: F(1)}, SQ)
            ok_form = ok_form and (anti == (_bform(S, T) == 1))
    GA.check("(3) b(S, T) = 1 exactly when the blades anticommute (10 generator blades, all S)", ok_form)
    sols = [S for S in GA.all_blades(10)
            if all(_bform(S, T) == 1 for T in pair_gens) and all(_bform(S, T) == 0 for T in slot_un)]
    GA.check("(3) the only such blade is the pair blade P (Gamma_W)", sols == [P])
    car = {}
    for c in (1, -1, 2):
        K = GA.scal(F(c), GW)
        a, ad = _m(W[0], GW, K), _m(V[0], GW, K)
        car[c] = GA.eq(_acomm(a, ad), GA.sc(1))
    GA.check("(3) a_i (c Gamma_W) satisfy the CAR exactly for c^2 = 1", car == {1: True, -1: True, 2: False})
