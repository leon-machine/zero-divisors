"""singularity.eviction-window-thermal-product-radiation-entropy: exact checks of the eviction theorem.

The rate model is simulated on exact amplitudes (qubits R_k = 2k, L_k = 2k+1): event t injects pair
t (while pairs remain) and evicts the oldest window qubits down to the capacity schedule, with a
controlled-Z (number diagonal, (L_E)) between the two oldest window qubits before each eviction.
Three runs: the model table's run (four pairs, capacity 2, flush), a five-pair run with unequal angles
and a decreasing schedule 3,3,3,2,2,1,1,0, and the maximally entangled idealisation (amplitudes 1, 1,
normalised at the end) on the schedule 3,3,3,3,2,2,1,1,0. Entropies are exact formal logarithms
(LogVecs); inequalities use rigorous rational bounds on ln p.
(1) At every stage rho_L = tensor_{k in W} diag(c_k^2, s_k^2) entrywise, so S_L = sum_{W} h_k; the
    radiation and window have equal trace moments tr rho^m, m = 2, 3, where the radiation has at most
    six qubits (S_R = S_L), and the global state stays normalised.
(2) S_R <= min(S_th, C) at every stage and S_R = 0 at complete evaporation.
(3) Before the first eviction S_R = S_th exactly.
(4) S_R = C - sum_{W}(ln 2 - h_k) exactly at every stage; S_R < C strictly whenever the window is
    nonempty and no member has c = s; in the idealisation S_R = min(S_th, C) exactly at every stage.
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
IDEAL = [(F(1), F(1))] * 6
RUNS = [(MODEL_PAIRS, [2, 2, 2, 2, 1, 0]), (PAIRS_B, [3, 3, 3, 2, 2, 1, 1, 0]),
        (IDEAL, [3, 3, 3, 3, 2, 2, 1, 1, 0])]


def h(pair):
    c, s = pair
    n = c * c + s * s
    return entropy([c * c / n, s * s / n])


def stage_data(pairs, schedule):
    """Per stage: (normalised rho_L, rho_R or None, W members, S_th, number injected, evicted yet)."""
    nq = 2 * len(pairs)
    out = []
    for t, (state, rad, win) in enumerate(run_model(pairs, schedule)):
        norm = sum(a * a for a in state.values())
        rhoL = [[x / norm for x in row] for row in marginal(sorted(win), state, nq)]
        rhoR = None
        if len(rad) <= 6:
            rhoR = [[x / norm for x in row] for row in marginal(sorted(rad), state, nq)]
        injected = min(t + 1, len(pairs))
        S_th = LogVec()
        for k in range(injected):
            S_th = S_th + h(pairs[k])
        out.append((rhoL, rhoR, [q // 2 for q in sorted(win)], S_th, injected,
                    any(q % 2 for q in rad)))
    return out


def check_window_is_thermal_product():
    premise("singularity.rate-models-kinematic-inputs-l-u")
    premise("singularity.l-boundary-mode-locality")
    premise("singularity.no-attic-derived-model")
    for pairs, schedule in RUNS:
        data = stage_data(pairs, schedule)
        assert len(data) == len(schedule)
        for rhoL, rhoR, W, S_th, inj, ev in data:
            d = len(rhoL)
            assert d == 2 ** len(W) and is_diag(rhoL)
            S_W = LogVec()
            for idx in range(d):
                pr = F(1)
                for pos, k in enumerate(W):
                    c, s = pairs[k]
                    n = c * c + s * s
                    pr *= s * s / n if (idx >> pos) & 1 else c * c / n
                assert rhoL[idx][idx] == pr
            for k in W:
                S_W = S_W + h(pairs[k])
            assert entropy([rhoL[i][i] for i in range(d)]) == S_W
            if rhoR is not None:
                assert mtrace(rhoR) == 1 and mtrace(rhoL) == 1
                R2, L2 = mm(rhoR, rhoR), mm(rhoL, rhoL)
                assert mtrace(R2) == mtrace(L2) and mtrace(mm(R2, rhoR)) == mtrace(mm(L2, rhoL))


def check_envelope_endpoint_and_rising_branch():
    premise("singularity.rate-models-kinematic-inputs-l-u")
    ln2 = LogVec.ln_int(2)
    for (pairs, schedule), want_rising in zip(RUNS, (2, 3, 3)):
        data = stage_data(pairs, schedule)
        n_rising = 0
        for rhoL, rhoR, W, S_th, inj, evicted in data:
            S_R = entropy([rhoL[i][i] for i in range(len(rhoL))])
            C = ln2 * len(W)
            assert logvec_le(S_R, S_th) and logvec_le(S_R, C)
            if not evicted:
                n_rising += 1
                assert S_R == S_th and len(W) == inj
        rhoL = data[-1][0]
        assert data[-1][2] == [] and entropy([rhoL[i][i] for i in range(len(rhoL))]) == LogVec()
        assert n_rising == want_rising


def check_falling_branch_and_idealisation():
    ln2 = LogVec.ln_int(2)
    for pairs, schedule in RUNS:
        for rhoL, rhoR, W, S_th, inj, ev in stage_data(pairs, schedule):
            S_R = entropy([rhoL[i][i] for i in range(len(rhoL))])
            C = ln2 * len(W)
            short = LogVec()
            for k in W:
                short = short + (ln2 - h(pairs[k]))
            assert S_R == C - short
            maximal = all(pairs[k][0] == pairs[k][1] for k in W)
            assert (S_R == C) == maximal
            if W and not maximal:
                assert logvec_lt(S_R, C)
            if pairs is IDEAL:
                assert S_R == (S_th if logvec_le(S_th, C) else C)
