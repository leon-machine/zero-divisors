"""hawking.current-commutator-exactly-edge-split: exact checks.

Finite window of L fermionic modes 1..L (stored as bits 0..L-1 of a Fock bitmask, Jordan-Wigner signs),
currents a_m = sum_{k=1}^{L-m} psi_k^dagger psi_{k+m}, N_k = psi_k^dagger psi_k. Operators are applied to
every basis state, so each identity is an operator identity on the whole Fock space.
(1) [a_m, a_m^dagger] = B_m - T_m on all 2^L states, for every m = 1..L-1, L = 6 and 7.
(2) For 2m <= L, on every edge-clean state (bottom m filled, top m empty) [a_m, a_m^dagger] = m.
(3) [a_m, a_m'] = 0 for all m, m' (L = 6, all states).
(4) For m != m' the one-body matrix of [a_m, a_m'^dagger] (the commutator of the shift matrices) has
    every nonzero entry (a, b) with a, b both among the lowest max(m, m') modes or both among the highest
    max(m, m'), its second quantisation is the Fock commutator (checked on all states), and it annihilates
    every state edge-clean at depth max(m, m').
"""
from fractions import Fraction as F

import GA

WINDOWS = [6, 7]


def basis_state(s):
    """The Fock basis state with occupation bitmask s, coefficient 1."""
    return {s: F(1)}


def popcount(s):
    return bin(s).count("1")


def bilin(a, b, vec):
    """psi_a^dagger psi_b on a state {mask: coeff} (0-indexed modes)."""
    out = {}
    for s, c in vec.items():
        if not (s >> b) & 1:
            continue
        sg = -1 if popcount(s & ((1 << b) - 1)) % 2 else 1
        s1 = s & ~(1 << b)
        if (s1 >> a) & 1:
            continue
        sg *= -1 if popcount(s1 & ((1 << a) - 1)) % 2 else 1
        s2 = s1 | (1 << a)
        out[s2] = out.get(s2, F(0)) + sg * c
    return {k: v for k, v in out.items() if v != 0}


def apply_sum(terms, vec):
    """terms: list of (coeff, a, b) meaning sum coeff psi_a^dagger psi_b."""
    out = {}
    for (c, a, b) in terms:
        for s, v in bilin(a, b, vec).items():
            out[s] = out.get(s, F(0)) + c * v
    return {k: v for k, v in out.items() if v != 0}


def comm(t1, t2, vec):
    x = apply_sum(t1, apply_sum(t2, vec))
    y = apply_sum(t2, apply_sum(t1, vec))
    for s, v in y.items():
        x[s] = x.get(s, F(0)) - v
    return {k: v for k, v in x.items() if v != 0}


def cur(m, L, dagger=False):
    if dagger:
        return [(F(1), k + m, k) for k in range(L - m)]
    return [(F(1), k, k + m) for k in range(L - m)]


def check_commutator_is_edge_difference():
    n_cases = 0
    for L in WINDOWS:
        for m in range(1, L):
            Bm = [(F(1), k, k) for k in range(m)]
            Tm = [(F(-1), k, k) for k in range(L - m, L)]
            for s in range(1 << L):
                v = basis_state(s)
                assert comm(cur(m, L), cur(m, L, True), v) == apply_sum(Bm + Tm, v)
                n_cases += 1
    # every m = 1..L-1 on all 2^L states: (L - 1) 2^L summed over L = 6, 7 is 5 * 64 + 6 * 128 = 1088
    assert n_cases == 1088
    return True


def check_edge_clean_scalar():
    for L in WINDOWS:
        for m in range(1, L // 2 + 1):
            n_clean = 0
            for s in range(1 << L):
                if all((s >> k) & 1 for k in range(m)) and not any((s >> k) & 1 for k in range(L - m, L)):
                    n_clean += 1
                    assert comm(cur(m, L), cur(m, L, True), {s: F(1)}) == {s: F(m)}
            assert n_clean == 2 ** (L - 2 * m)
    return True


def check_currents_commute():
    L = 6
    for m in range(1, L):
        for mp in range(1, L):
            for s in range(1 << L):
                assert comm(cur(m, L), cur(mp, L), {s: F(1)}) == {}
    # contrast: with the adjoint the commutator is not zero, e.g. N_1 - N_6 on the state with mode 1 filled
    assert comm(cur(1, L), cur(1, L, True), {1: F(1)}) == {1: F(1)}
    return True


def check_cross_commutator_edge_supported():
    L = 7
    for m in range(1, 4):
        for mp in range(1, 4):
            if m == mp:
                continue
            d = max(m, mp)
            # one-body matrices h[a][b] (coefficient of psi_a^dagger psi_b)
            h1 = [[F(1) if b == a + m else F(0) for b in range(L)] for a in range(L)]
            h2 = [[F(1) if a == b + mp else F(0) for b in range(L)] for a in range(L)]
            hc = [[sum((h1[a][k] * h2[k][b] - h2[a][k] * h1[k][b] for k in range(L)), F(0))
                   for b in range(L)] for a in range(L)]
            low, high = set(range(d)), set(range(L - d, L))
            nz = [(a, b) for a in range(L) for b in range(L) if hc[a][b] != 0]
            assert nz and all((a in low and b in low) or (a in high and b in high) for (a, b) in nz)
            assert all(a != b for (a, b) in nz)
            terms = [(hc[a][b], a, b) for (a, b) in nz]
            for s in range(1 << L):
                v = {s: F(1)}
                assert comm(cur(m, L), cur(mp, L, True), v) == apply_sum(terms, v)
                if all((s >> k) & 1 for k in range(d)) and not any((s >> k) & 1 for k in range(L - d, L)):
                    assert apply_sum(terms, v) == {}
    return True
