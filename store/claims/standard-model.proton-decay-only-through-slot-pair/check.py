"""standard-model.proton-decay-only-through-slot-pair: exact checks.

Five-mode module Lambda(C^5), occupation basis (pairs 1, 2, 3; slots/rungs 4, 5), v_a creation and
w_a contraction. The ten Majoranas are g_a+ = v_a + w_a (square +1) and g_a- = v_a - w_a
(square -1), real, so the 45 bivectors (1/2) g_m g_n act by rational matrices; the slot generators
are the four g_4+-, g_5+-, the pair generators the six g_1+-..g_3+-. On the sixteen (even states)
chi = -(-1)^(N_4 + N_5) (+1 on Q, L; -1 on u^c, d^c, e^c, nu^c) and B - L = 1 - (2/3) k.
(1) n_B = ((B - L) + chi)/4 and n_L = (chi - 3(B - L))/4 reproduce every species' baryon and
lepton number (hand table) on all 16 states, and 3 n_B + n_L = chi.
(2) The 21 split-preserving bivectors commute with chi on the sixteen, the 24 mixing ones
anticommute with it (and so flip chi on every state they do not annihilate).
(3) p -> e+ pi0: from the species numbers, Delta(B - L) = 0 and Delta(3 n_B + n_L) = -4, so the
process changes chi and no product of the 21 can mediate it; the mixing bivectors can.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

N = 5
STATES = [frozenset(c) for r in range(N + 1) for c in combinations(range(1, N + 1), r)]
EVEN = [S for S in STATES if len(S) % 2 == 0]
NAMES = {(0, 0): "nu^c", (0, 2): "u^c", (1, 1): "Q", (1, 3): "L", (2, 0): "e^c", (2, 2): "d^c"}
SLOT_MODES, PAIR_MODES = (4, 5), (1, 2, 3)


def act(op, st):
    out = {}
    for (kind, i), c in op.items():
        for S, a in st.items():
            if kind == "v" and i not in S:
                T = S | {i}
            elif kind == "w" and i in S:
                T = S - {i}
            else:
                continue
            sign = -1 if sum(1 for j in S if j < i) % 2 else 1
            out[T] = out.get(T, 0) + sign * c * a
    return {k: v for k, v in out.items() if v != 0}


def majorana(a, s):
    return {("v", a): F(1), ("w", a): F(s)}


MAJ = [(a, s) for a in PAIR_MODES + SLOT_MODES for s in (1, -1)]


def bivector(m, n):
    return lambda st: {k: v / 2 for k, v in act(majorana(*m), act(majorana(*n), st)).items()}


BIVECTORS = [((m, n), bivector(m, n)) for m, n in combinations(MAJ, 2)]


def jk(S):
    return len(S & {4, 5}), len(S & {1, 2, 3})


def chi(S):
    return -(-1) ** len(S & {4, 5})


def b_minus_l(S):
    return 1 - F(2, 3) * jk(S)[1]


def nB(S):
    return (b_minus_l(S) + chi(S)) / 4


def nL(S):
    return (chi(S) - 3 * b_minus_l(S)) / 4


def check_baryon_and_lepton_number_from_chi():
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    table = {"Q": (F(1, 3), 0), "u^c": (F(-1, 3), 0), "d^c": (F(-1, 3), 0),
             "L": (0, 1), "e^c": (0, -1), "nu^c": (0, -1)}
    ok = len(EVEN) == 16
    for S in EVEN:
        ok = ok and (nB(S), nL(S)) == table[NAMES[jk(S)]]
        ok = ok and 3 * nB(S) + nL(S) == chi(S)
    ok = ok and sorted(chi(S) for S in EVEN) == [-1] * 8 + [1] * 8
    GA.check("proton: n_B = ((B-L) + chi)/4, n_L = (chi - 3(B-L))/4 on every state, 3 n_B + n_L = chi", ok)
    return ok


def check_chi_commutes_with_21_and_anticommutes_with_24():
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    ok = len(BIVECTORS) == 45
    preserving = mixing = 0
    for (m, n), X in BIVECTORS:
        mixes = (m[0] in SLOT_MODES) != (n[0] in SLOT_MODES)
        for S in EVEN:
            img = X({S: F(1)})
            # X chi e_S = chi(S) X e_S; chi X e_S = sum chi(T) X_TS e_T
            if mixes:
                ok = ok and all(chi(T) == -chi(S) for T in img)
            else:
                ok = ok and all(chi(T) == chi(S) for T in img)
        # every bivector acts nontrivially on the sixteen
        ok = ok and any(X({S: F(1)}) for S in EVEN)
        mixing += mixes
        preserving += not mixes
    ok = ok and (preserving, mixing) == (21, 24)
    GA.check("proton: the 21 split-preserving bivectors commute with chi, the 24 mixing ones anticommute", ok)
    return ok


def check_proton_channel_needs_mixing():
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    by_species = {}
    for S in EVEN:
        by_species[NAMES[jk(S)]] = (nB(S), nL(S), b_minus_l(S), chi(S))
    quark = by_species["Q"]
    # p = three quarks of Q; e+ is the e^c state; pi0 carries nothing
    initial = tuple(3 * v for v in quark[:2])
    final = by_species["e^c"][:2]
    d_bl = (final[0] - final[1]) - (initial[0] - initial[1])
    d_chi = (3 * final[0] + final[1]) - (3 * initial[0] + initial[1])
    ok = initial == (1, 0) and final == (0, -1) and d_bl == 0 and d_chi == -4
    ok = ok and (final[0] - initial[0], final[1] - initial[1]) == (-1, -1)
    # a product of split-preserving bivectors keeps chi; a single mixing bivector flips it
    preserving = [X for (m, n), X in BIVECTORS if (m[0] in SLOT_MODES) == (n[0] in SLOT_MODES)]
    mixing = [X for (m, n), X in BIVECTORS if (m[0] in SLOT_MODES) != (n[0] in SLOT_MODES)]
    for S in EVEN:
        for X in preserving[:7]:
            for Yb in preserving[7:14]:
                ok = ok and all(chi(T) == chi(S) for T in X(Yb({S: F(1)})))
    ok = ok and all(any(chi(T) != chi(S) for S in EVEN for T in X({S: F(1)})) for X in mixing)
    GA.check("proton: p -> e+ pi0 has Delta(B-L) = 0, Delta(3 n_B + n_L) = -4: only the mixing generators", ok)
    return ok
