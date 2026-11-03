"""singularity.envelope-endpoint-why-boundary-mode-locality: exact checks of the envelope, the
endpoint, and the necessity of (L_E).

Exact amplitudes, qubits R_k = 2k, L_k = 2k+1; entropies are exact formal logarithms (LogVecs) of
rational spectra and inequalities are decided by rigorous rational bounds on ln p.
(1) Envelope and endpoint under number-diagonal (controlled-Z) window dynamics, on the model table's
    run and on a five-pair run with a decreasing schedule: S_R = S_L <= min(S_th, C) at every stage
    (S_R = S_L through equal trace moments where the radiation has at most six qubits) and S_R = 0 at
    complete evaporation.
(2) (L_E) cannot be dropped: two pairs (24/25, 7/25), the rotation |00> -> 3/5|00> + 4/5|11>,
    |11> -> -4/5|00> + 3/5|11> on (L_1, L_2) (orthogonal, changes L_1's and L_2's occupations, so not
    number diagonal), then L_1 evicted: rho_L2 = diag(5968/15625, 9657/15625), global purity holds
    (S_R = S_L through tr rho_R^m = tr rho_L^m, m = 2, 3), and S_R > S_th strictly. In bits S_R lies in
    (0.95, 0.97); S_th = 2 H(576/625) lies in (0.54, 0.56) nats, that is (0.78, 0.80) bits.
"""
from fractions import Fraction as F

import GA
import series
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

# --- formal logarithms: a LogVec is a finite rational combination sum_p a_p ln p over primes, so
# entropies of rational spectra are exact LogVecs; inequalities are decided by rigorous rational
# bounds on ln p (ln p = a ln 2 + 2 atanh z, atanh summed with an explicit geometric tail bound) ---

def factorise(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


class LogVec(object):
    def __init__(self, d=None):
        self.d = {p: F(c) for p, c in (d or {}).items() if c != 0}

    @staticmethod
    def ln_int(n):
        return LogVec({p: e for p, e in factorise(n).items()})

    @staticmethod
    def ln_rat(q):
        q = F(q)
        assert q > 0
        return LogVec.ln_int(q.numerator) - LogVec.ln_int(q.denominator)

    def __add__(self, o):
        d = dict(self.d)
        for p, c in o.d.items():
            d[p] = d.get(p, F(0)) + c
        return LogVec(d)

    def __neg__(self):
        return LogVec({p: -c for p, c in self.d.items()})

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, c):
        return LogVec({p: v * F(c) for p, v in self.d.items()})

    __rmul__ = __mul__

    def __eq__(self, o):
        return self.d == o.d

    def __ne__(self, o):
        return not self.__eq__(o)


_LNB = {}


def ln_bounds(n):
    """Rational (lower, upper) bounds on ln n, n a positive integer (series.ln_bounds, memoised)."""
    if n not in _LNB:
        _LNB[n] = series.ln_bounds(n)
    return _LNB[n]


def logvec_bounds(v):
    lo, hi = F(0), F(0)
    for p, c in v.d.items():
        a, b = ln_bounds(p)
        if c > 0:
            lo += c * a
            hi += c * b
        else:
            lo += c * b
            hi += c * a
    return lo, hi


def logvec_lt(u, v):
    """u < v, decided rigorously; equal vectors give False."""
    if u == v:
        return False
    lo, hi = logvec_bounds(v - u)
    if lo > 0:
        return True
    if hi < 0:
        return False
    raise ValueError("bounds too weak")


def logvec_le(u, v):
    return u == v or logvec_lt(u, v)


def entropy(probs):
    """-sum p ln p of a rational spectrum, as a LogVec (nats)."""
    out = LogVec()
    for p in probs:
        if p != 0:
            assert p > 0
            out = out - LogVec.ln_rat(p) * p
    return out

MODEL_PAIRS = [(F(4, 5), F(3, 5)), (F(4, 5), F(3, 5)), (F(4, 5), F(3, 5)), (F(12, 13), F(5, 13))]
PAIRS_B = [(F(24, 25), F(7, 25)), (F(3, 5), F(4, 5)), (F(12, 13), F(5, 13)), (F(20, 29), F(21, 29)),
           (F(8, 17), F(15, 17))]
RUNS = [(MODEL_PAIRS, [2, 2, 2, 2, 1, 0]), (PAIRS_B, [3, 3, 3, 2, 2, 1, 1, 0])]
# Qubits per thermofield pair (R_k = 2k, L_k = 2k + 1).
QUBITS_PER_PAIR = 2
# Largest radiation (in qubits) whose dense marginal is built to compare tr rho^2 and tr rho^3.
MAX_RAD_QUBITS = 6
WITNESS = (F(24, 25), F(7, 25))
ROT = (F(3, 5), F(4, 5))


def check_envelope_and_endpoint_under_diagonal_dynamics():
    premise("singularity.eviction-window-thermal-product-radiation-entropy")
    premise("singularity.l-boundary-mode-locality")
    premise("singularity.rate-models-kinematic-inputs-l-u")
    ln2 = LogVec.ln_int(2)
    assert entropy([F(1, 2), F(1, 2)]) == ln2          # a qubit's capacity ln 2, attained when maximally mixed
    for pairs, schedule in RUNS:
        nq = QUBITS_PER_PAIR * len(pairs)
        stages = run_model(pairs, schedule)
        for t, (state, rad, win) in enumerate(stages):
            S_th = LogVec()
            for k in range(min(t + 1, len(pairs))):
                c, s = pairs[k]
                S_th = S_th + entropy([c * c, s * s])
            rL = marginal(sorted(win), state, nq)
            S_L = entropy([rL[i][i] for i in range(len(rL))])
            assert is_diag(rL)
            assert logvec_le(S_L, S_th) and logvec_le(S_L, ln2 * len(win))
            if len(win) == len(rad):
                # nothing evicted yet (one R radiated and one L in the window per injected pair, no
                # scrambling applied): the window is the L halves of a product of pairs, so the envelope
                # is attained, S_L = S_th
                assert S_L == S_th
            if len(rad) <= MAX_RAD_QUBITS:
                rR = marginal(sorted(rad), state, nq)
                assert purity(rR) == purity(rL) and trace_cube(rR) == trace_cube(rL)
        state, rad, win = stages[-1]
        assert win == [] and purity(marginal(sorted(rad), state, nq)) == 1


def witness_state():
    c, s = WITNESS
    co, si = ROT
    st = pair_state(c, s, 1, pair_state(c, s, 0, {0: F(1)}))
    both = (1 << 1) | (1 << 3)
    rot = {}
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
    return st, rot


def check_locality_premise_is_necessary():
    premise("singularity.l-boundary-mode-locality")
    st, rot = witness_state()
    assert sum(a * a for a in rot.values()) == 1
    # the rotation is not number diagonal: it moves weight between |00> and |11> of (L_1, L_2)
    assert any(((m >> 1) & 1) != ((m >> 0) & 1) for m in rot)
    rL = marginal([3], rot, 4)                      # window after evicting L_1: L_2 alone
    rR = marginal([0, 1, 2], rot, 4)                 # radiation: R_1, R_2 and the evicted L_1
    assert rL == [[F(5968, 15625), F(0)], [F(0), F(9657, 15625)]]
    assert purity(rR) == purity(rL) and trace_cube(rR) == trace_cube(rL)
    S_R = entropy([rL[0][0], rL[1][1]])
    c, s = WITNESS
    S_th = entropy([c * c, s * s]) * 2
    assert c * c == F(576, 625)
    assert logvec_lt(S_th, S_R)
    ln2 = LogVec.ln_int(2)
    assert logvec_lt(ln2 * F(95, 100), S_R) and logvec_lt(S_R, ln2 * F(97, 100))
    lo, hi = logvec_bounds(S_th)
    assert F(54, 100) < lo and hi < F(56, 100)
    assert logvec_lt(ln2 * F(78, 100), S_th) and logvec_lt(S_th, ln2 * F(80, 100))
    # without the rotation (number-diagonal dynamics) the same eviction stays inside the envelope
    rL0 = marginal([3], st, 4)
    assert rL0 == [[c * c, F(0)], [F(0), s * s]] and logvec_lt(entropy([c * c, s * s]), S_th)
