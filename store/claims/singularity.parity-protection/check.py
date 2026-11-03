"""singularity.parity-protection: exact checks of parity protection in the finite-ledger model.

The model is simulated on exact amplitudes (Gaussian rationals, GA.QI), qubits R_k = 2k, L_k = 2k+1.
Pairs c_k|00> + s_k|11> are injected one per event; before each eviction an arbitrary
number-basis-diagonal window unitary is applied, drawn from a program of diagonal gates: controlled-Z,
single-qubit phases (3+4i)/5 and (5-12i)/13, a controlled phase (8+15i)/17, a controlled-controlled-Z,
and sign flips. Four programs over two pair lists (four and five pairs, unequal angles).
(1) At every stage every single-qubit reduced density matrix, radiation or window, early or evicted,
    is exactly diag(c_k^2, s_k^2), coherence zero.
(2) The mechanism of the proof: the support constraint R_k = L_k holds in every configuration at
    every stage, and each configuration's squared modulus is the product of its pairs' populations.
(3) Controls showing the hypothesis does work: a hopping rotation (cos, sin) = (3/5, 4/5) between L_1
    and L_2, which is not number diagonal, moves the L_1 population from 9/25 to 23689/105625; the
    pairing rotation |00> -> 3/5|00> + 4/5|11> on (L_1, L_2) at (c, s) = (24/25, 7/25) moves the L_2
    marginal to diag(5968/15625, 9657/15625).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise  # noqa: F401 (no premises: the claim has none)

QI = GA.QI
PAIRS_A = [(F(4, 5), F(3, 5)), (F(12, 13), F(5, 13)), (F(3, 5), F(4, 5)), (F(15, 17), F(8, 17))]
PAIRS_B = [(F(24, 25), F(7, 25)), (F(4, 5), F(3, 5)), (F(20, 29), F(21, 29)), (F(5, 13), F(12, 13)),
           (F(4, 5), F(3, 5))]
PH1, PH2, PH3 = QI(F(3, 5), F(4, 5)), QI(F(5, 13), F(-12, 13)), QI(F(8, 17), F(15, 17))
# diagonal gates on window positions: (kind, positions, phase)
PROGRAMS = [
    [("cz", (0, 1), None)],
    [("ph", (0,), PH1), ("cp", (0, 1), PH3), ("ph", (1,), PH2)],
    [("ccz", (0, 1, 2), None), ("cz", (0, 2), None), ("ph", (2,), PH2), ("flip", (1,), None)],
    [("cp", (1, 0), PH1), ("ccz", (0, 1, 2), None), ("ph", (0,), PH3)],
]
CAPS = [2, 3, 3, 2]


def apply_diag(gate, window, state):
    kind, pos, z = gate
    qs = [window[p] for p in pos if p < len(window)]
    if len(qs) < len(pos):
        return state
    out = {}
    for m, a in state.items():
        on = all((m >> q) & 1 for q in qs)
        if kind in ("cz", "ccz", "flip"):
            out[m] = -a if on else a
        else:
            out[m] = a * z if on else a
    return out


def run(pairs, cap, program):
    """Inject, scramble with the diagonal program, evict down to cap; flush at the end."""
    state = {0: QI(1)}
    window, radiation, stages = [], [], []

    def evict():
        nonlocal state
        for gate in program:
            state = apply_diag(gate, window, state)
        radiation.append(window.pop(0))

    for k, (c, s) in enumerate(pairs):
        new = {}
        for m, a in state.items():
            new[m] = a * c
            new[m | (1 << (2 * k)) | (1 << (2 * k + 1))] = a * s
        state = new
        radiation.append(2 * k)
        window.append(2 * k + 1)
        while len(window) > cap:
            evict()
        stages.append((dict(state), list(radiation), list(window)))
    while window:
        evict()
        stages.append((dict(state), list(radiation), list(window)))
    return stages


def single_marginal(q, state):
    """2x2 reduced density matrix of qubit q (complex amplitudes)."""
    rho = [[QI(0), QI(0)], [QI(0), QI(0)]]
    for m1, a1 in state.items():
        for m2, a2 in state.items():
            if (m1 | (1 << q)) == (m2 | (1 << q)):
                rho[(m1 >> q) & 1][(m2 >> q) & 1] += a1 * a2.conj()
    return rho


def check_every_single_qubit_marginal_is_thermal():
    for pairs in (PAIRS_A, PAIRS_B):
        for cap, program in zip(CAPS, PROGRAMS):
            stages = run(pairs, cap, program)
            assert len(stages) == len(pairs) + min(cap, len(pairs))
            for state, rad, win in stages:
                assert sorted(rad + win) == list(range(2 * ((len(rad) + len(win)) // 2)))
                for q in rad + win:
                    c, s = pairs[q // 2]
                    rho = single_marginal(q, state)
                    assert rho[0][0] == c * c and rho[1][1] == s * s
                    assert rho[0][1] == 0 and rho[1][0] == 0


def check_support_constraint_and_populations():
    for pairs in (PAIRS_A, PAIRS_B):
        n = len(pairs)
        for cap, program in zip(CAPS, PROGRAMS):
            for state, rad, win in run(pairs, cap, program):
                nk = (len(rad) + len(win)) // 2
                assert len(state) == 2 ** nk
                for m, a in state.items():
                    assert all(((m >> (2 * k)) & 1) == ((m >> (2 * k + 1)) & 1) for k in range(n))
                    w = F(1)
                    for k in range(nk):
                        c, s = pairs[k]
                        w *= s * s if (m >> (2 * k)) & 1 else c * c
                    assert (a * a.conj()) == QI(w)


def check_non_diagonal_unitaries_break_protection():
    # hopping rotation between L_1 (qubit 1) and L_2 (qubit 3): |10> -> c|10> + s|01>, |01> -> c|01> - s|10>
    (c1, s1), (c2, s2) = PAIRS_A[0], PAIRS_A[1]
    co, si = F(3, 5), F(4, 5)
    st = {0: F(1)}
    for k, (c, s) in enumerate(((c1, s1), (c2, s2))):
        new = {}
        for m, a in st.items():
            new[m] = a * c
            new[m | (1 << (2 * k)) | (1 << (2 * k + 1))] = a * s
        st = new
    hop = {}
    for m, a in st.items():
        l1, l2 = (m >> 1) & 1, (m >> 3) & 1
        if l1 != l2:
            flip = m ^ (1 << 1) ^ (1 << 3)
            hop[m] = hop.get(m, F(0)) + co * a
            hop[flip] = hop.get(flip, F(0)) + (si if l1 else -si) * a
        else:
            hop[m] = hop.get(m, F(0)) + a
    p1 = sum((a * a for m, a in hop.items() if (m >> 1) & 1), F(0))
    assert sum((a * a for a in hop.values()), F(0)) == 1
    assert s1 * s1 == F(9, 25) and p1 == F(23689, 105625)
    # pairing rotation on (L_1, L_2) at (c, s) = (24/25, 7/25), then L_2's marginal
    c, s = PAIRS_B[0]
    st = {0: F(1)}
    for k in range(2):
        new = {}
        for m, a in st.items():
            new[m] = a * c
            new[m | (1 << (2 * k)) | (1 << (2 * k + 1))] = a * s
        st = new
    rot = {}
    both = (1 << 1) | (1 << 3)
    for m, a in st.items():
        l1, l2 = (m >> 1) & 1, (m >> 3) & 1
        if (l1, l2) == (0, 0):
            rot[m] = rot.get(m, F(0)) + co * a
            rot[m | both] = rot.get(m | both, F(0)) + si * a
        elif (l1, l2) == (1, 1):
            rot[m & ~both] = rot.get(m & ~both, F(0)) - si * a
            rot[m] = rot.get(m, F(0)) + co * a
        else:
            rot[m] = rot.get(m, F(0)) + a
    p_empty = sum((a * a for m, a in rot.items() if not (m >> 3) & 1), F(0))
    assert c * c == F(576, 625) and p_empty == F(5968, 15625) and 1 - p_empty == F(9657, 15625)
