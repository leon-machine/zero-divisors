"""singularity.purity-correlation-transfer-recovery: exact checks of the two-pair, one-gate model.

Qubits (R_1, L_1, R_2, L_2) = (0, 1, 2, 3); pairs c_k|00> + s_k|11>; one controlled-Z between L_1
and L_2. Exact rational amplitudes, for the script's pair (4/5, 3/5) twice and for five further
choices of (c_1, s_1; c_2, s_2), including gamma < 0 and gamma close to 0.
(1) The global state is pure (norm 1, Schmidt purity equality across R = {R_1, R_2} and L at every
    stage); after both window qubits are evicted the radiation is all four qubits and tr rho_R^2 = 1.
(2) The (R_1, L_1) marginal is supported on {|00>, |11>} with coherence c_1 s_1 gamma,
    gamma = c_2^2 - s_2^2, populations c_1^2, s_1^2; its purity is c_1^4 + s_1^4 + 2 c_1^2 s_1^2 gamma^2,
    strictly below 1 whenever gamma^2 < 1; without the gate the marginal is the pure pair.
(3) <X_R1 X_L1> = 2 c_1 s_1 gamma and <X_R1 X_L1 Z_L2> = 2 c_1 s_1 with the gate, the two values
    exchanged without it; at the script's numbers (24/25, 168/625) against (168/625, 24/25). Every
    single-qubit marginal is the same thermal matrix in both histories.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

# --- exact multi-qubit simulator (states: dict {bitmask: amplitude}; qubit R_k = 2k, L_k = 2k+1) ---

def pair_state(c, s, k, state):
    """Tensor the thermofield pair c|00> + s|11> on (R_k, L_k) onto the state."""
    out = {}
    for m, a in state.items():
        out[m] = out.get(m, 0) + a * c
        m2 = m | (1 << (2 * k)) | (1 << (2 * k + 1))
        out[m2] = out.get(m2, 0) + a * s
    return {m: a for m, a in out.items() if a != 0}


def apply_cz(i, j, state):
    return {m: (-a if (m >> i) & 1 and (m >> j) & 1 else a) for m, a in state.items()}


def marginal(qubits, state, nq):
    """Reduced density matrix (unnormalised if the state is) over the listed qubits; bit t of the
    row index is the occupation of qubits[t]."""
    d = 1 << len(qubits)
    rho = [[F(0)] * d for _ in range(d)]
    rest = [q for q in range(nq) if q not in qubits]
    for m1, a1 in state.items():
        for m2, a2 in state.items():
            if all(((m1 >> r) & 1) == ((m2 >> r) & 1) for r in rest):
                i = sum(((m1 >> q) & 1) << t for t, q in enumerate(qubits))
                j = sum(((m2 >> q) & 1) << t for t, q in enumerate(qubits))
                rho[i][j] += a1 * a2
    return rho


mm = GA.mat_mul


def mtrace(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def purity(rho):
    d = len(rho)
    return sum((rho[i][j] * rho[j][i] for i in range(d) for j in range(d)), F(0))


def pinch(rho):
    """The descent E_N: complete dephasing in the joint number basis."""
    d = len(rho)
    return [[rho[i][j] if i == j else F(0) for j in range(d)] for i in range(d)]


def is_diag(rho):
    d = len(rho)
    return all(rho[i][j] == 0 for i in range(d) for j in range(d) if i != j)


def expect_xz(xs, zs, rho):
    """<prod_{i in xs} X_i prod_{j in zs} Z_j> against a density matrix (positions within its qubits)."""
    xmask = 0
    for i in xs:
        xmask ^= (1 << i)
    tot = F(0)
    for i in range(len(rho)):
        sign = 1
        for j in zs:
            if (i >> j) & 1:
                sign = -sign
        tot += rho[i ^ xmask][i] * sign
    return tot


def run_model(pairs, schedule, scramble=True):
    """The rate model: event t injects pair t (if any) and then evicts the oldest window qubits
    until |W| <= schedule[t], applying a controlled-Z between the two oldest window qubits before
    each eviction (number-diagonal scrambling). Returns stages [(state, radiation, window)]."""
    state = {0: F(1)}
    window, radiation, stages = [], [], []
    for t, cap in enumerate(schedule):
        if t < len(pairs):
            c, s = pairs[t]
            state = pair_state(c, s, t, state)
            radiation.append(2 * t)
            window.append(2 * t + 1)
        while len(window) > cap:
            if scramble and len(window) >= 2:
                state = apply_cz(window[0], window[1], state)
            radiation.append(window.pop(0))
        stages.append((dict(state), list(radiation), list(window)))
    return stages


def trace_cube(A):
    """tr A^3 with sparse rows."""
    rows = [[(j, x) for j, x in enumerate(r) if x != 0] for r in A]
    return sum((x * y * A[k][i] for i in range(len(A)) for j, x in rows[i] for k, y in rows[j]), F(0))

PAIR_SETS = [((F(4, 5), F(3, 5)), (F(4, 5), F(3, 5))),
             ((F(12, 13), F(5, 13)), (F(3, 5), F(4, 5))),
             ((F(8, 17), F(15, 17)), (F(24, 25), F(7, 25))),
             ((F(20, 29), F(21, 29)), (F(12, 13), F(5, 13))),
             ((F(3, 5), F(4, 5)), (F(20, 29), F(21, 29))),
             ((F(7, 25), F(24, 25)), (F(15, 17), F(8, 17)))]


def histories(p1, p2):
    plain = pair_state(p2[0], p2[1], 1, pair_state(p1[0], p1[1], 0, {0: F(1)}))
    return plain, apply_cz(1, 3, plain)


def check_global_purity_and_pure_radiation_at_completion():
    for p1, p2 in PAIR_SETS:
        plain, scr = histories(p1, p2)
        assert sum(a * a for a in scr.values()) == 1
        # stage with both window qubits present, and after the first eviction (L_1 to R)
        for rad, win in (([0, 2], [1, 3]), ([0, 1, 2], [3])):
            assert purity(marginal(rad, scr, 4)) == purity(marginal(win, scr, 4))
        assert purity(marginal(win, scr, 4)) < 1
        # completion: the radiation is all four qubits and is pure
        rho_all = marginal([0, 1, 2, 3], scr, 4)
        assert mtrace(rho_all) == 1 and purity(rho_all) == 1


def check_pair_coherence_damped_by_visibility():
    for (c1, s1), (c2, s2) in PAIR_SETS:
        plain, scr = histories((c1, s1), (c2, s2))
        gamma = c2 * c2 - s2 * s2
        rho = marginal([0, 1], scr, 4)
        # support {|00>, |11>} (indices 0 and 3), populations untouched, coherence c1 s1 gamma
        assert all(rho[i][j] == 0 for i in range(4) for j in range(4) if not (i in (0, 3) and j in (0, 3)))
        assert rho[0][0] == c1 * c1 and rho[3][3] == s1 * s1
        assert rho[0][3] == c1 * s1 * gamma and rho[3][0] == c1 * s1 * gamma
        pur = purity(rho)
        assert pur == c1 ** 4 + s1 ** 4 + 2 * c1 ** 2 * s1 ** 2 * gamma ** 2
        assert pur < 1 and 1 - pur == 2 * c1 * c1 * s1 * s1 * (1 - gamma * gamma)
        rho0 = marginal([0, 1], plain, 4)
        assert rho0[0][3] == c1 * s1 and purity(rho0) == 1


def check_correlators_carry_the_gate_pattern():
    premise("singularity.parity-protection")
    for (c1, s1), (c2, s2) in PAIR_SETS:
        plain, scr = histories((c1, s1), (c2, s2))
        gamma = c2 * c2 - s2 * s2
        rp, rs = marginal([0, 1, 2, 3], plain, 4), marginal([0, 1, 2, 3], scr, 4)
        assert expect_xz([0, 1], [], rp) == 2 * c1 * s1
        assert expect_xz([0, 1], [3], rp) == 2 * c1 * s1 * gamma
        assert expect_xz([0, 1], [], rs) == 2 * c1 * s1 * gamma
        assert expect_xz([0, 1], [3], rs) == 2 * c1 * s1
        # single-qubit states identical (thermal) in both histories
        for q in range(4):
            c, s = ((c1, s1), (c2, s2))[q // 2]
            for st in (plain, scr):
                assert marginal([q], st, 4) == [[c * c, F(0)], [F(0), s * s]]
    plain, scr = histories(*PAIR_SETS[0])
    rp, rs = marginal([0, 1, 2, 3], plain, 4), marginal([0, 1, 2, 3], scr, 4)
    assert (expect_xz([0, 1], [], rp), expect_xz([0, 1], [3], rp)) == (F(24, 25), F(168, 625))
    assert (expect_xz([0, 1], [], rs), expect_xz([0, 1], [3], rs)) == (F(168, 625), F(24, 25))
