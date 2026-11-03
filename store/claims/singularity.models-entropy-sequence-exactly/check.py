"""singularity.models-entropy-sequence-exactly: exact checks of the model run's entropy sequence.

The run of the model table: pairs (4/5, 3/5) three times then (12/13, 5/13), window capacity two,
a controlled-Z between the two oldest window qubits before each eviction, and a final flush (six
stages). Exact rational amplitudes; entropies are exact formal logarithms (LogVecs); inequalities
are decided by rigorous rational bounds on ln 2, ln 3, ln 5, ln 13.
(1) At every stage rho_L is diagonal in the number basis with the product distribution of its
    members; S_L = sum_{k in W} H(c_k^2) exactly; tr rho_R^2 = prod_{k in W}(c_k^4 + s_k^4), the
    printed sequence 337/625, (337/625)^2, (337/625)^2, (337/625)(21361/28561), 21361/28561, 1; the
    global state is a unit vector at every stage. S_R = S_L because rho_R and rho_L have the same
    nonzero spectrum, computed at every stage (all six, up to eight radiation qubits): for each
    window configuration j the radiation vector v_j (the amplitudes with window part j) satisfies
    rho_R v_j = p_j v_j with p_j the j-th diagonal entry of rho_L, the v_j are mutually orthogonal
    with |v_j|^2 = p_j, and sum_j p_j = tr rho_R, so (rho_R being positive) every other eigenvalue
    of rho_R is 0.
(2) Phase I (events 1 and 2, no eviction yet): S_R = S_th exactly. Phase II (the three later stages
    with a nonempty window): S_R <= S_th and S_R < C = |W| ln 2 strictly, since no pair is maximally
    entangled. Completion: S_R = 0 and tr rho_R^2 = 1. Here S_R is computed as the entropy of the
    rho_L spectrum, which (1) shows is the nonzero spectrum of rho_R.
"""
from fractions import Fraction as F

import GA
from pyutil import get_or_set
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
SCHEDULE = [2, 2, 2, 2, 1, 0]
NQ = 8


def H(c):
    return entropy([c * c, 1 - c * c])


def check_window_product_and_entropy_identity():
    premise("singularity.parity-protection")
    stages = run_model(MODEL_PAIRS, SCHEDULE)
    want_purity = [F(337, 625), F(337, 625) ** 2, F(337, 625) ** 2,
                   F(337, 625) * F(21361, 28561), F(21361, 28561), F(1)]
    assert len(stages) == len(want_purity)
    for (state, rad, win), wp in zip(stages, want_purity):
        assert sum(a * a for a in state.values()) == 1
        members = [q // 2 for q in sorted(win)]
        S_sum, pur = LogVec(), F(1)
        for k in members:
            c, s = MODEL_PAIRS[k]
            S_sum = S_sum + H(c)
            pur *= c ** 4 + s ** 4
        assert pur == wp
        rhoL = marginal(sorted(win), state, NQ)
        assert is_diag(rhoL)
        spec = [rhoL[i][i] for i in range(len(rhoL))]
        for idx in range(len(spec)):
            pr = F(1)
            for pos, k in enumerate(members):
                c, s = MODEL_PAIRS[k]
                pr *= s * s if (idx >> pos) & 1 else c * c
            assert spec[idx] == pr
        assert entropy(spec) == S_sum
        rad_s = sorted(rad)
        rhoR = marginal(rad_s, state, NQ)
        assert purity(rhoR) == wp
        # nonzero spectrum of rho_R: the radiation vectors v_j, one per window configuration j
        vs = {}
        for m, a in state.items():
            i = sum(((m >> q) & 1) << t for t, q in enumerate(rad_s))
            j = sum(((m >> q) & 1) << t for t, q in enumerate(sorted(win)))
            v = get_or_set(vs, j, {})
            v[i] = v.get(i, F(0)) + a
        assert sorted(vs) == [j for j in range(len(spec)) if spec[j] != 0]
        rows = [[(c, x) for c, x in enumerate(r) if x != 0] for r in rhoR]
        for j, v in vs.items():
            assert sum(x * x for x in v.values()) == spec[j]
            for i in range(len(rhoR)):
                assert sum((x * v.get(c, 0) for c, x in rows[i]), F(0)) == spec[j] * v.get(i, 0)
            for j2, v2 in vs.items():
                if j2 != j:
                    assert sum((x * v2.get(i, 0) for i, x in v.items()), F(0)) == 0
        assert sum(spec[j] for j in vs) == mtrace(rhoR) == 1


def check_phase_one_two_and_completion():
    premise("singularity.parity-protection")
    stages = run_model(MODEL_PAIRS, SCHEDULE)
    ln2 = LogVec.ln_int(2)
    n_phase1 = n_phase2 = n_end = 0
    for t, (state, rad, win) in enumerate(stages):
        injected = min(t + 1, len(MODEL_PAIRS))
        S_th = LogVec()
        for k in range(injected):
            S_th = S_th + H(MODEL_PAIRS[k][0])
        rhoL = marginal(sorted(win), state, NQ)
        S_R = entropy([rhoL[i][i] for i in range(len(rhoL))])
        C = ln2 * len(win)
        if all(q % 2 == 0 for q in rad):          # no eviction yet
            n_phase1 += 1
            assert S_R == S_th
        elif win:
            n_phase2 += 1
            assert logvec_le(S_R, S_th) and logvec_lt(S_R, C)
            assert S_R != S_th
        else:
            n_end += 1
            assert S_R == LogVec() and purity(marginal(sorted(rad), state, NQ)) == 1
    assert (n_phase1, n_phase2, n_end) == (2, 3, 1)
