"""standard-model.yukawa-pattern-two-rung-module: exact checks.

The five-mode module Lambda(C^5) is built in the occupation basis e_S, S a subset of {1,...,5}
(pairs 1, 2, 3; rungs 4, 5). The ten vectors act as v_a = creation (e_a wedge) and w_a = interior
contraction, which satisfy v_a w_b + w_b v_a = delta_ab. The pairing is the premise's
B(psi, phi) = sum_S (-1)^(|S|(|S|-1)/2) eps(S, S^c) psi_S phi_(S^c). The sixteen is the even part,
with species by (j, k) = (occupied rungs, occupied pairs): nu^c (0,0), u^c (0,2), Q (1,1),
L (1,3), e^c (2,0), d^c (2,2) (Hypothesis (S)). For every one of the ten vectors x, every nonzero
Y_x(e_S, e_T) = B(e_S, x e_T) on the 16 x 16 basis pairs is recorded by species pair:
(i) rung creation v_4, v_5: exactly (L, nu^c), (Q, u^c); rung annihilation w_4, w_5: (L, e^c), (Q, d^c);
(ii) pair creation v_1..v_3: (Q, Q), (d^c, nu^c), (e^c, u^c); pair annihilation: (Q, L), (u^c, d^c);
(iii) Y_x is symmetric for every x (basis vectors and sample combinations), 6 Y(S) + 6 Y(T) + 6 Y(x) = 0
on every nonzero entry (Y(state) = (3j - 2k)/6, Y(v_a) = 1/2 or -1/3, Y(w_a) the negative), and
B(psi, phi) = 0 for psi, phi both in the sixteen (no mass term without a vector).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

N = 5
STATES = [frozenset(c) for r in range(N + 1) for c in combinations(range(1, N + 1), r)]
FULL = frozenset(range(1, N + 1))
EVEN = [S for S in STATES if len(S) % 2 == 0]


def act(op, st):
    """op = {('v' | 'w', mode): coeff} acting on st = {frozenset: coeff}."""
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


def perm_sign(seq):
    s = 1
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                s = -s
    return s


def B(psi, phi):
    tot = F(0)
    for S, a in psi.items():
        Sc = FULL - S
        if Sc in phi:
            k = len(S)
            tot += (-1) ** (k * (k - 1) // 2) * perm_sign(sorted(S) + sorted(Sc)) * a * phi[Sc]
    return tot


def jk(S):
    return len(S & {4, 5}), len(S & {1, 2, 3})


NAMES = {(0, 0): "nu^c", (0, 2): "u^c", (1, 1): "Q", (1, 3): "L", (2, 0): "e^c", (2, 2): "d^c"}


def y_state(S):
    j, k = jk(S)
    return F(3 * j - 2 * k, 6)


def y_vec(kind, a):
    y = F(1, 2) if a in (4, 5) else F(-1, 3)
    return y if kind == "v" else -y


def entries(x):
    """All nonzero Y_x(e_S, e_T) on the sixteen, as {(S, T): value}."""
    out = {}
    for S in EVEN:
        for T in EVEN:
            val = B({S: F(1)}, act(x, {T: F(1)}))
            if val != 0:
                out[(S, T)] = val
    return out


def species_pairs(x):
    return sorted({tuple(sorted((NAMES[jk(S)], NAMES[jk(T)]))) for (S, T) in entries(x)})


COMBOS = [{("v", 4): F(2), ("w", 5): F(-3)}, {("v", 1): F(1), ("w", 2): F(5, 7), ("v", 5): F(1, 3)},
          {("w", 3): F(4), ("w", 4): F(-1), ("v", 2): F(2, 9)}]
RUNGS, PAIRS = (4, 5), (1, 2, 3)
BASIS = [{(kind, a): F(1)} for kind in ("v", "w") for a in PAIRS + RUNGS]


def species_counts(x):
    out = {}
    for (S, T), v in entries(x).items():
        key = tuple(sorted((NAMES[jk(S)], NAMES[jk(T)])))
        out[key] = out.get(key, 0) + 1
        if abs(v) != 1:
            out["bad"] = 1
    return out


def check_rung_vectors_carry_dirac_yukawas():
    premise("standard-model.invariant-pairing-five-modes")
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    for a in RUNGS:
        # v_a: nu^c with the one L state lacking a (both orders); three Q states with three u^c
        ok = ok and species_counts({("v", a): F(1)}) == {("L", "nu^c"): 2, ("Q", "u^c"): 6}
        ok = ok and species_counts({("w", a): F(1)}) == {("L", "e^c"): 2, ("Q", "d^c"): 6}
    # two entries by hand: v_4 e_1235 = -e_12345, B(e_0, e_12345) = 1; w_4 e_1234 = -e_123,
    # B(e_45, e_123) = (-1)^1 eps(45, 123) = -1
    ok = ok and entries({("v", 4): F(1)})[(frozenset(), frozenset({1, 2, 3, 5}))] == -1
    ok = ok and entries({("w", 4): F(1)})[(frozenset({4, 5}), frozenset({1, 2, 3, 4}))] == 1
    GA.check("Yukawa (i): rung vectors couple exactly (L, nu^c), (Q, u^c) and (L, e^c), (Q, d^c)", ok)
    return ok


def check_pair_vectors_carry_triplet_couplings():
    premise("standard-model.invariant-pairing-five-modes")
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    for a in PAIRS:
        ok = ok and species_counts({("v", a): F(1)}) == {("Q", "Q"): 4, ("d^c", "nu^c"): 2, ("e^c", "u^c"): 2}
        ok = ok and species_counts({("w", a): F(1)}) == {("L", "Q"): 4, ("d^c", "u^c"): 4}
    GA.check("Yukawa (ii): pair vectors couple exactly (Q,Q), (d^c,nu^c), (e^c,u^c) and (Q,L), (u^c,d^c)", ok)
    return ok


def check_symmetric_hypercharge_conserving_and_no_bare_mass():
    premise("standard-model.invariant-pairing-five-modes")
    premise("standard-model.hyp-s-slot-statistics")
    ok = len(BASIS) == 10
    for x in BASIS + COMBOS:
        ent = entries(x)
        ok = ok and all(ent.get((T, S)) == v for (S, T), v in ent.items())
    for x in BASIS:
        (kind, a), = x.keys()
        ent = entries(x)
        ok = ok and len(ent) == 8
        ok = ok and all(6 * y_state(S) + 6 * y_state(T) + 6 * y_vec(kind, a) == 0 for (S, T) in ent)
    # no invariant pairing of two sixteens without a vector
    ok = ok and all(B({S: F(1)}, {T: F(1)}) == 0 for S in EVEN for T in EVEN)
    # B pairs each state with its complement only, with values +-1; 32 such pairs
    ok = ok and sum(1 for S in STATES for T in STATES if B({S: F(1)}, {T: F(1)}) != 0) == 32
    ok = ok and all(abs(B({S: F(1)}, {FULL - S: F(1)})) == 1 for S in STATES)
    GA.check("Yukawa (iii): Y_x symmetric, hypercharge conserved, no mass term without a vector", ok)
    return ok
