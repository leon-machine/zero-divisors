"""singularity.no-attic-derived-model: exact checks that the model's kinematics leave no attic.

Rate-model runs on exact amplitudes (qubits R_k = 2k, L_k = 2k+1), controlled-Z scrambling before each
eviction: the model table's run (four pairs, capacity 2, flush) and a five-pair run on the schedule
3,3,2,2,1,1,0 with unequal angles.
(1) Kinematics: at every stage W(t) and R(t) are disjoint and together are exactly the 2 x (number
    injected) qubits; every eviction moves one qubit from W to R and none leaves the two sectors.
(2) Dynamics: the global state on R u L stays normalised (pure), and the two sectors' nonzero spectra
    agree at every stage of both runs (up to ten radiation qubits): rho_L is diagonal, and for each
    window configuration j the radiation vector v_j (the amplitudes with window part j) is an
    eigenvector of rho_R with eigenvalue the j-th diagonal entry p_j of rho_L; the v_j are mutually
    orthogonal with |v_j|^2 = p_j and sum_j p_j = tr rho_R = 1, so (rho_R being positive) every
    other eigenvalue is 0. No q-number content is held outside L u R.
(3) At each eviction the evicted qubit L_j is diag(c_j^2, s_j^2), and its complement in R u L has
    nonzero spectrum exactly {c_j^2, s_j^2} (computed as in (2)); with the global state pure, the
    mutual information I(L_j : rest) = S(L_j) + S(rest) - S(R u L), assembled as a formal
    combination of entropies of computed spectra, is 2 H(c_j^2) = 2 h_j: all of the evicted
    qubit's correlation sits inside L(t) u R(t).
"""
from fractions import Fraction as F

import GA
from pyutil import get_or_set
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


def nonzero_spectrum(diag_side, other_side, state, nq):
    """Nonzero spectrum of the marginal on other_side, for a pure state whose marginal on diag_side
    is diagonal: returns (rho_other, {j: p_j}) after asserting that each vector v_j (amplitudes with
    diag_side part j, indexed by the other_side configuration) satisfies rho_other v_j = p_j v_j,
    that the v_j are mutually orthogonal with |v_j|^2 = p_j, and that sum_j p_j = tr rho_other."""
    rd = marginal(diag_side, state, nq)
    assert is_diag(rd)
    ro = marginal(other_side, state, nq)
    vs = {}
    for m, a in state.items():
        i = sum(((m >> q) & 1) << t for t, q in enumerate(other_side))
        j = sum(((m >> q) & 1) << t for t, q in enumerate(diag_side))
        v = get_or_set(vs, j, {})
        v[i] = v.get(i, F(0)) + a
    spec = {j: rd[j][j] for j in vs}
    assert sorted(vs) == [j for j in range(len(rd)) if rd[j][j] != 0]
    rows = [[(c, x) for c, x in enumerate(r) if x != 0] for r in ro]
    for j, v in vs.items():
        assert sum(x * x for x in v.values()) == spec[j]
        for i in range(len(ro)):
            assert sum((x * v.get(c, 0) for c, x in rows[i]), F(0)) == spec[j] * v.get(i, 0)
        for j2, v2 in vs.items():
            if j2 != j:
                assert sum((x * v2.get(i, 0) for i, x in v.items()), F(0)) == 0
    assert sum(spec.values()) == mtrace(ro)
    return ro, spec


def spectrum_key(probs):
    """The entropy -sum p ln p of a spectrum as a formal symbol: its sorted nonzero eigenvalues;
    the zero entropy (a single eigenvalue 1) is the empty key."""
    key = tuple(sorted(p for p in probs if p != 0))
    return () if key == (F(1),) else key


def entropy_combination(terms):
    """A formal integer combination sum_i n_i S(spec_i), as {key: n} with zero entries dropped."""
    out = {}
    for n, probs in terms:
        k = spectrum_key(probs)
        if k:
            out[k] = out.get(k, 0) + n
    return {k: n for k, n in out.items() if n != 0}


MODEL_PAIRS = [(F(4, 5), F(3, 5)), (F(4, 5), F(3, 5)), (F(4, 5), F(3, 5)), (F(12, 13), F(5, 13))]
PAIRS_B = [(F(24, 25), F(7, 25)), (F(3, 5), F(4, 5)), (F(12, 13), F(5, 13)), (F(20, 29), F(21, 29)),
           (F(8, 17), F(15, 17))]
RUNS = [(MODEL_PAIRS, [2, 2, 2, 2, 1, 0]), (PAIRS_B, [3, 3, 2, 2, 1, 1, 0])]


def check_two_sectors_exhaust_the_qubits():
    premise("singularity.rate-models-kinematic-inputs-l-u")
    for (pairs, schedule), want_evictions in zip(RUNS, (4, 5)):
        prev_rad, prev_win, evictions = [], [], 0
        for t, (state, rad, win) in enumerate(run_model(pairs, schedule)):
            inj = min(t + 1, len(pairs))
            assert not set(rad) & set(win)
            assert sorted(rad + win) == list(range(2 * inj))
            moved = [q for q in prev_win if q in rad]
            evictions += len(moved)
            assert all(q % 2 == 1 for q in moved)
            assert set(prev_rad) <= set(rad)
            prev_rad, prev_win = rad, win
        assert evictions == want_evictions


def check_sector_spectra_agree():
    premise("singularity.rate-models-kinematic-inputs-l-u")
    n_stages = 0
    for pairs, schedule in RUNS:
        nq = 2 * len(pairs)
        for state, rad, win in run_model(pairs, schedule):
            n_stages += 1
            assert sum(a * a for a in state.values()) == 1
            rR, spec = nonzero_spectrum(sorted(win), sorted(rad), state, nq)
            rL = marginal(sorted(win), state, nq)
            assert mtrace(rR) == mtrace(rL) == 1
            assert sorted(spec.values()) == sorted(rL[i][i] for i in range(len(rL)) if rL[i][i] != 0)
    assert n_stages == 13


def check_evicted_correlations_stay_in_the_sectors():
    n_evicted = 0
    for pairs, schedule in RUNS:
        nq = 2 * len(pairs)
        prev_win = []
        for state, rad, win in run_model(pairs, schedule):
            for q in [q for q in prev_win if q in rad]:
                n_evicted += 1
                c, s = pairs[q // 2]
                rq = marginal([q], state, nq)
                assert rq == [[c * c, F(0)], [F(0), s * s]]
                rest = [x for x in sorted(rad + win) if x != q]
                rr, spec = nonzero_spectrum([q], rest, state, nq)
                assert sorted(spec.values()) == sorted([c * c, s * s])
                assert purity(rr) == purity(rq) == c ** 4 + s ** 4
                # I(L_j : rest) = S(L_j) + S(rest) - S(R u L); the global state is a unit vector
                mi = entropy_combination([(1, [c * c, s * s]), (1, spec.values()), (-1, [F(1)])])
                assert mi == {tuple(sorted([c * c, s * s])): 2}
            prev_win = win
    assert n_evicted == 9
