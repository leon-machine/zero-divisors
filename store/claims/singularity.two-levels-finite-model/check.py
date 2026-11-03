"""singularity.two-levels-finite-model: exact checks of the two ledgers on the full model run.

The full run: four pairs (4/5, 3/5) x 3 and (12/13, 5/13), capacity two, controlled-Z scrambling
before each eviction, final flush; rho_R(t) the radiation state at each stage (exact rationals),
rho_R the complete radiation (all eight qubits), E the joint-number pinching. Entropies are exact
formal logarithms; inequalities use rigorous rational bounds.
(1) tr rho_R^2 = 1; tr (E rho_R)^2 = prod_k (c_k^4 + s_k^4) = 817544276833/6972900390625;
    S_2(E rho_R) = log_2 of the inverse lies in (3.08, 3.10) bits; S(E rho_R) = sum_k H(c_k^2) = S_th.
    Stage by stage S(E rho_R(t)) is non-decreasing and tr (E rho_R(t))^2 non-increasing, while the
    ascended entropy S(rho_R(t)) = S(rho_L(t)) rises and returns to 0; pinching never raises purity.
(2) D(rho_R || E rho_R) = S(E rho_R) - S(rho_R) = S_th; every single-qubit marginal is identical at
    the two levels; the decoding correlators (<X_R1 X_L1>, <X_R1 X_L1 Z_L2>) of the scrambled and the
    unscrambled two-pair histories, (168/625, 24/25) and (24/25, 168/625), become (0, 0) under E in
    both; the parity average (rho + Gamma rho Gamma)/2 keeps the even correlator at 24/25.
(3) Each (R_k, L_k) marginal of E rho_R is diag(c_k^2, 0, 0, s_k^2); every (R_k, R_l), k != l, reduced
    state of E rho_R is the product of its marginals, while the ascended rho_R has non-product
    two-pair reduced states.
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
SCHEDULE = [2, 2, 2, 2, 1, 0]
NQ = 8


def H(c):
    return entropy([c * c, 1 - c * c])


def final_radiation():
    stages = run_model(MODEL_PAIRS, SCHEDULE)
    state, rad, win = stages[-1]
    return stages, marginal(sorted(rad), state, NQ)


def reduced(rho, keep):
    """Partial trace of a density matrix on qubits 0..n-1 onto the positions in keep."""
    d = 1 << len(keep)
    out = [[F(0)] * d for _ in range(d)]
    n = len(rho).bit_length() - 1
    rest = [q for q in range(n) if q not in keep]
    for i in range(len(rho)):
        for j in range(len(rho)):
            if rho[i][j] != 0 and all(((i >> r) & 1) == ((j >> r) & 1) for r in rest):
                a = sum(((i >> q) & 1) << t for t, q in enumerate(keep))
                b = sum(((j >> q) & 1) << t for t, q in enumerate(keep))
                out[a][b] += rho[i][j]
    return out


def kron2(A, B):
    """A on bit 0, B on bit 1."""
    return [[A[i & 1][j & 1] * B[i >> 1][j >> 1] for j in range(4)] for i in range(4)]


def check_ascended_and_descended_ledgers():
    premise("singularity.purity-correlation-transfer-recovery")
    stages, rhoR = final_radiation()
    ER = pinch(rhoR)
    prod = F(1)
    for c, s in MODEL_PAIRS:
        prod *= c ** 4 + s ** 4
    assert purity(rhoR) == 1 and purity(ER) == prod
    assert prod == F(817544276833, 6972900390625)
    S2 = LogVec.ln_rat(1 / prod)
    ln2 = LogVec.ln_int(2)
    assert logvec_lt(ln2 * F(308, 100), S2) and logvec_lt(S2, ln2 * F(310, 100))
    S_th = LogVec()
    for c, s in MODEL_PAIRS:
        S_th = S_th + H(c)
    assert entropy([ER[i][i] for i in range(len(ER))]) == S_th
    assert S_th == H(F(4, 5)) * 3 + H(F(12, 13))
    prev_S, prev_p, asc = None, None, []
    for state, rad, win in stages:
        rho_t = marginal(sorted(rad), state, NQ)
        E_t = pinch(rho_t)
        S_t = entropy([E_t[i][i] for i in range(len(E_t))])
        p_t = purity(E_t)
        assert p_t <= purity(rho_t)
        if prev_S is not None:
            assert logvec_le(prev_S, S_t) and p_t <= prev_p
        prev_S, prev_p = S_t, p_t
        rhoL = marginal(sorted(win), state, NQ)
        asc.append(entropy([rhoL[i][i] for i in range(len(rhoL))]))
    assert prev_S == S_th
    assert logvec_lt(asc[-1], asc[3]) and asc[-1] == LogVec() and logvec_lt(asc[0], asc[3])


def two_pair_histories():
    (c1, s1), (c2, s2) = MODEL_PAIRS[0], MODEL_PAIRS[1]
    plain = pair_state(c2, s2, 1, pair_state(c1, s1, 0, {0: F(1)}))
    return marginal([0, 1, 2, 3], plain, 4), marginal([0, 1, 2, 3], apply_cz(1, 3, plain), 4)


def check_deficit_located_and_message_not_descending():
    premise("singularity.deficit-theorem-cost-descent-exactly")
    premise("singularity.deficit-carried-quanta-correlations")
    premise("singularity.parity-protection")
    premise("singularity.p-reduced-metric-level-reading-many")
    stages, rhoR = final_radiation()
    ER = pinch(rhoR)
    S_th = LogVec()
    for c, s in MODEL_PAIRS:
        S_th = S_th + H(c)
    D = entropy([ER[i][i] for i in range(len(ER))]) - LogVec()     # S(rho_R) = 0: pure
    assert D == S_th and purity(rhoR) == 1
    for q in range(NQ):
        assert reduced(rhoR, [q]) == reduced(ER, [q])
        c, s = MODEL_PAIRS[q // 2]
        assert reduced(ER, [q]) == [[c * c, F(0)], [F(0), s * s]]
    plain, scr = two_pair_histories()
    assert (expect_xz([0, 1], [], scr), expect_xz([0, 1], [3], scr)) == (F(168, 625), F(24, 25))
    assert (expect_xz([0, 1], [], plain), expect_xz([0, 1], [3], plain)) == (F(24, 25), F(168, 625))
    for rho in (plain, scr):
        Er = pinch(rho)
        assert expect_xz([0, 1], [], Er) == 0 and expect_xz([0, 1], [3], Er) == 0
    # total-parity average: Gamma = (-1)^N is diagonal; (rho + Gamma rho Gamma)/2 keeps even correlators
    par = [(-1) ** bin(i).count("1") for i in range(16)]
    avg = [[(scr[i][j] + par[i] * scr[i][j] * par[j]) / 2 for j in range(16)] for i in range(16)]
    assert avg == scr and expect_xz([0, 1], [3], avg) == F(24, 25)


def check_records_survive_inter_pair_destroyed():
    stages, rhoR = final_radiation()
    ER = pinch(rhoR)
    for k, (c, s) in enumerate(MODEL_PAIRS):
        pk = reduced(ER, [2 * k, 2 * k + 1])
        assert pk == [[c * c, F(0), F(0), F(0)], [F(0)] * 4, [F(0)] * 4, [F(0), F(0), F(0), s * s]]
    n_pairs = len(MODEL_PAIRS)
    for k in range(n_pairs):
        for l in range(k + 1, n_pairs):
            joint = reduced(ER, [2 * k, 2 * l])
            assert joint == kron2(reduced(ER, [2 * k]), reduced(ER, [2 * l]))
    # the ascended radiation does carry inter-pair correlation (scrambled neighbours)
    nonproduct = 0
    for k in range(n_pairs - 1):
        a, b = [2 * k, 2 * k + 1], [2 * k + 2, 2 * k + 3]
        four = reduced(rhoR, a + b)
        A, B = reduced(rhoR, a), reduced(rhoR, b)
        prodAB = [[A[i & 3][j & 3] * B[i >> 2][j >> 2] for j in range(16)] for i in range(16)]
        nonproduct += four != prodAB
    assert nonproduct == 3
