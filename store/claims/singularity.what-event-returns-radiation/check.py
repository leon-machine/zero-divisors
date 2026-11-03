"""singularity.what-event-returns-radiation: exact checks of what an emission event returns.

Rate-model runs on exact amplitudes (qubits R_k = 2k, L_k = 2k+1; controlled-Z before each eviction):
the model table's run (five events with a block), a five-pair run whose schedule 3,3,3,1,1,0 evicts
three qubits in one event, and the maximally entangled idealisation (amplitudes 1, 1) with one eviction
per event. At each event A is the new radiation block (R_k and the evicted L_j), R_< the earlier
radiation. All entropies are exact formal logarithms of exact rational spectra: rho_A is checked
diagonal; S(R_<) and S(A u R_<) are read from the (diagonal) window before and after by global purity,
which is re-checked through equal purities where the radiation has at most six qubits.
(1) S(rho_A) = h_k + sum_{evicted} h_j and I(A : R_<) = 2 sum_{evicted} h_j at every event.
(2) Each evicted L_j has I(L_j : R_<) = 2 h_j (checked at every eviction of the model run and of the
    five-pair run on the schedule 3,3,3,3,3,2,1,0, where the complement's entropy is diagonal-readable:
    the new pair, if any, is verified to be an untouched pure factor), while I(L_j : R_j) < 2 h_j once
    a gate has acted: the (R_j, L_j) marginal keeps the populations c^2, s^2, its coherence is damped
    below c s and its purity is below 1, so S(R_j L_j) > 0.
(3) In the idealisation, I(A : R_<) = 2 ln 2 = S(rho_A) at every event with one eviction.
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
IDEAL = [(F(1), F(1))] * 5
RUNS = [(MODEL_PAIRS, [2, 2, 2, 2, 1, 0]), (PAIRS_B, [3, 3, 3, 1, 1, 0]), (IDEAL, [2, 2, 2, 2, 2, 1, 0])]


def h(pair):
    c, s = pair
    n = c * c + s * s
    return entropy([c * c / n, s * s / n])


def diag_entropy(rho):
    assert is_diag(rho)
    return entropy([rho[i][i] for i in range(len(rho))])


def events(pairs, schedule):
    nq = 2 * len(pairs)
    stages = run_model(pairs, schedule)
    out = []
    for t in range(1, len(stages)):
        (sp, radp, winp), (st, rad, win) = stages[t - 1], stages[t]
        A = sorted(set(rad) - set(radp))
        if not A:
            continue
        nrm = sum(a * a for a in st.values())
        nrmp = sum(a * a for a in sp.values())
        norm = lambda r, n: [[x / n for x in row] for row in r]
        rA = norm(marginal(A, st, nq), nrm)
        rWp = norm(marginal(sorted(winp), sp, nq), nrmp)
        rW = norm(marginal(sorted(win), st, nq), nrm)
        if len(radp) <= 6:
            assert purity(norm(marginal(sorted(radp), sp, nq), nrmp)) == purity(rWp)
        if len(rad) <= 6:
            assert purity(norm(marginal(sorted(rad), st, nq), nrm)) == purity(rW)
        out.append((A, diag_entropy(rA), diag_entropy(rWp), diag_entropy(rW), st, nq, nrm))
    return out


def check_block_entropy_and_returned_information():
    premise("singularity.eviction-window-thermal-product-radiation-entropy")
    for (pairs, schedule), want in zip(RUNS, (5, 5, 6)):
        evs = events(pairs, schedule)
        assert len(evs) == want
        two_at_once = 0
        for A, S_A, S_Rl, S_all, st, nq, nrm in evs:
            new = [q // 2 for q in A if q % 2 == 0]
            ev = [q // 2 for q in A if q % 2 == 1]
            two_at_once += len(ev) >= 2
            want_SA, want_I = LogVec(), LogVec()
            for k in new + ev:
                want_SA = want_SA + h(pairs[k])
            for j in ev:
                want_I = want_I + h(pairs[j]) * 2
            assert S_A == want_SA
            assert S_A + S_Rl - S_all == want_I
        assert two_at_once == (1 if pairs is PAIRS_B else 0)


def factorises(rho, X, Y, C):
    """rho over the qubit list C equals rho_X (x) rho_Y, X u Y = C (lists of qubits)."""
    pX, pY = [C.index(q) for q in X], [C.index(q) for q in Y]
    rX, rY = reduce_to(rho, pX), reduce_to(rho, pY)
    sub = lambda i, ps: sum(((i >> p) & 1) << t for t, p in enumerate(ps))
    return all(rho[i][j] == rX[sub(i, pX)][sub(j, pX)] * rY[sub(i, pY)][sub(j, pY)]
               for i in range(len(rho)) for j in range(len(rho))), rX, rY


def reduce_to(rho, keep):
    n = len(rho).bit_length() - 1
    rest = [p for p in range(n) if p not in keep]
    d = 1 << len(keep)
    out = [[F(0)] * d for _ in range(d)]
    for i in range(len(rho)):
        for j in range(len(rho)):
            if rho[i][j] != 0 and all(((i >> r) & 1) == ((j >> r) & 1) for r in rest):
                out[sum(((i >> p) & 1) << t for t, p in enumerate(keep))][
                    sum(((j >> p) & 1) << t for t, p in enumerate(keep))] += rho[i][j]
    return out


def check_evicted_qubit_correlated_with_radiation_not_partner():
    premise("singularity.purity-correlation-transfer-recovery")
    for (pairs, schedule), want in zip((RUNS[0], (PAIRS_B, [3, 3, 3, 3, 3, 2, 1, 0])), (4, 5)):
        nq = 2 * len(pairs)
        stages = run_model(pairs, schedule)
        n_checked = 0
        for t in range(1, len(stages)):
            (sp, radp, winp), (st, rad, win) = stages[t - 1], stages[t]
            A = sorted(set(rad) - set(radp))
            newR = [q for q in A if q % 2 == 0]
            for q in [q for q in A if q % 2 == 1]:
                j = q // 2
                c, s = pairs[j]
                # the partner pair (R_j, L_j): populations kept, coherence damped, purity < 1
                pair = marginal([2 * j, q], st, nq)
                assert pair[0][0] == c * c and pair[3][3] == s * s
                assert pair[0][3] ** 2 < (c * s) ** 2 and purity(pair) < 1
                # I(L_j : R_<) through the complement W u A minus L_j (global purity)
                comp = sorted(set(win) | set(A) - {q})
                rC = marginal(comp, st, nq)
                if newR:
                    k = newR[0] // 2
                    if len(comp) > 6:
                        continue
                    fac, rX, rY = factorises(rC, [x for x in comp if x // 2 != k], [2 * k, 2 * k + 1], comp)
                    if not fac or purity(rY) != 1:
                        continue
                    S_comp = diag_entropy(rX)
                else:
                    S_comp = diag_entropy(rC)
                S_Rl = diag_entropy(marginal(sorted(winp), sp, nq))
                assert diag_entropy(marginal([q], st, nq)) + S_Rl - S_comp == h(pairs[j]) * 2
                n_checked += 1
        assert n_checked == want


def check_idealisation_returns_two_ln_two():
    ln2 = LogVec.ln_int(2)
    pairs, schedule = RUNS[2]
    n_one = 0
    for A, S_A, S_Rl, S_all, st, nq, nrm in events(pairs, schedule):
        ev = [q for q in A if q % 2 == 1]
        if len(ev) == 1 and len(A) == 2:
            n_one += 1
            assert S_A == ln2 * 2 and S_A + S_Rl - S_all == ln2 * 2
    assert n_one == 3
