"""singularity.deficit-carried-quanta-correlations: exact checks that the deficit is inter-quanta.

E_N is the joint-number pinching (complete dephasing in the computational basis); C(rho) is the
total correlation sum_k S(rho_k) - S(rho). Entropies are exact formal logarithms (LogVecs) of
rational spectra; positivity is decided by rigorous rational bounds on ln p.
(1) Marginals pass through E_N unchanged when they are diagonal: for every single mode of the
    model's final radiation (eight qubits, controlled-Z scrambled), of the scrambled two-pair state,
    and of two mixed states built to have diagonal marginals (a two-qubit and a three-qubit state
    rho = W diag(p) W^T, W a product of rotations inside the even and inside the odd sector, so
    every coherence joins basis states differing in at least two bits). Control: for a state with a coherent single-mode marginal the marginal of E_N rho differs.
(2) D(rho || E_N rho) = C(rho) - C(E_N rho) exactly on the two mixed states, with D computed from
    its definition tr rho ln rho - tr rho ln E_N rho (ln rho = W diag(ln p) W^T), and D > 0.
(3) For globally pure states (the model's final radiation and the scrambled two-pair state),
    S(rho) = 0 (tr rho^2 = 1) and the deficit S(E_N rho) - S(rho) of the deficit theorem equals the
    total correlation drop, which is the whole descended entropy: for the model run
    3 H(16/25) + H(144/169) nats, the full thermal sum.
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
SPEC2 = [F(1, 2), F(1, 4), F(1, 6), F(1, 12)]
SPEC3 = [F(1, 4), F(1, 5), F(1, 6), F(1, 8), F(1, 10), F(1, 12), F(1, 15), F(1, 120)]
ROT2 = [(0b00, 0b11, F(3, 5), F(4, 5)), (0b01, 0b10, F(5, 13), F(12, 13))]
ROT3 = [(0b000, 0b011, F(3, 5), F(4, 5)), (0b101, 0b110, F(4, 5), F(-3, 5)),
        (0b000, 0b101, F(5, 13), F(12, 13)), (0b001, 0b010, F(8, 17), F(15, 17)),
        (0b100, 0b111, F(3, 5), F(4, 5)), (0b001, 0b111, F(4, 5), F(3, 5))]


def rotation(dim, rots):
    W = [[F(int(i == j)) for j in range(dim)] for i in range(dim)]
    for (a, b, c, s) in rots:
        G = [[F(int(i == j)) for j in range(dim)] for i in range(dim)]
        G[a][a], G[b][b], G[a][b], G[b][a] = c, c, -s, s
        W = mm(W, G)
    return W


def mixed(spec, rots):
    d = len(spec)
    W = rotation(d, rots)
    rho = [[sum((W[i][k] * spec[k] * W[j][k] for k in range(d)), F(0)) for j in range(d)] for i in range(d)]
    return rho, W


def mode_marginal(rho, k):
    out = [[F(0), F(0)], [F(0), F(0)]]
    for i in range(len(rho)):
        for j in range(len(rho)):
            if (i | (1 << k)) == (j | (1 << k)):
                out[(i >> k) & 1][(j >> k) & 1] += rho[i][j]
    return out


def nmodes(rho):
    return len(rho).bit_length() - 1


def model_final():
    stages = run_model(MODEL_PAIRS, [2, 2, 2, 2, 1, 0])
    state, rad, win = stages[-1]
    assert not win
    return marginal(sorted(rad), state, 8)


def two_pair():
    (c1, s1), (c2, s2) = MODEL_PAIRS[0], MODEL_PAIRS[1]
    st = apply_cz(1, 3, pair_state(c2, s2, 1, pair_state(c1, s1, 0, {0: F(1)})))
    return marginal([0, 1, 2, 3], st, 4)


def check_diagonal_marginals_pass_through_descent():
    states = [model_final(), two_pair(), mixed(SPEC2, ROT2)[0], mixed(SPEC3, ROT3)[0]]
    for rho in states:
        Er = pinch(rho)
        assert Er != rho
        for k in range(nmodes(rho)):
            mk = mode_marginal(rho, k)
            assert mk[0][1] == 0 and mk[1][0] == 0
            assert mode_marginal(Er, k) == mk
    # control: |+>|0> has a coherent mode-0 marginal, which E_N changes
    plus = [[F(1, 2), F(1, 2), F(0), F(0)], [F(1, 2), F(1, 2), F(0), F(0)],
            [F(0), F(0), F(0), F(0)], [F(0), F(0), F(0), F(0)]]
    assert mode_marginal(plus, 0) == [[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]]
    assert mode_marginal(pinch(plus), 0) == [[F(1, 2), F(0)], [F(0), F(1, 2)]]


def total_correlation(rho, S_rho):
    tot = LogVec()
    for k in range(nmodes(rho)):
        mk = mode_marginal(rho, k)
        tot = tot + entropy([mk[0][0], mk[1][1]])
    return tot - S_rho


def check_deficit_is_total_correlation_drop_mixed():
    for spec, rots in ((SPEC2, ROT2), (SPEC3, ROT3)):
        assert sum(spec) == 1
        rho, W = mixed(spec, rots)
        d = len(rho)
        Er = pinch(rho)
        WtrW = mm(mm([list(r) for r in zip(*W)], rho), W)
        tr_rho_ln_rho = LogVec()
        for k in range(d):
            assert WtrW[k][k] == spec[k]
            tr_rho_ln_rho = tr_rho_ln_rho + LogVec.ln_rat(spec[k]) * WtrW[k][k]
        tr_rho_ln_Er = LogVec()
        for i in range(d):
            tr_rho_ln_Er = tr_rho_ln_Er + LogVec.ln_rat(Er[i][i]) * rho[i][i]
        D = tr_rho_ln_rho - tr_rho_ln_Er
        C_rho = total_correlation(rho, entropy(spec))
        C_Er = total_correlation(Er, entropy([Er[i][i] for i in range(d)]))
        assert D == C_rho - C_Er
        assert logvec_lt(LogVec(), D)


def check_pure_state_deficit_is_whole_descended_entropy():
    premise("singularity.deficit-theorem-cost-descent-exactly")
    for rho, want in ((model_final(), entropy([F(16, 25), F(9, 25)]) * 3 + entropy([F(144, 169), F(25, 169)])),
                      (two_pair(), entropy([F(16, 25), F(9, 25)]) * 2)):
        d = len(rho)
        assert mtrace(rho) == 1 and purity(rho) == 1
        Er = pinch(rho)
        S_Er = entropy([Er[i][i] for i in range(d)])
        D = S_Er - LogVec()                       # deficit theorem with S(rho) = 0
        assert D == total_correlation(rho, LogVec()) - total_correlation(Er, S_Er)
        assert D == want
