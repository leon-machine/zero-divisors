"""singularity.deficit-theorem-cost-descent-exactly: exact checks of the deficit theorem.

Four complete families of orthogonal projectors on R^4 (two qubits): the joint-number pinching E_N
(four coordinate projectors), the two parity blocks span{|00>,|11>}, span{|01>,|10>}, a rotated
rank-one family u_k u_k^T and a rotated pair of rank-two blocks, the rotations being rational
orthogonal matrices, products of Givens rotations at (3/5, 4/5).
(1) Each family is complete and orthogonal; E(x) = sum_k P_k x P_k is idempotent, trace preserving
    and Hilbert-Schmidt self-adjoint, tr(E(a) b) = tr(a E(b)), on generic rational a, b.
(2) The proof's key lemma, tr(rho f(E rho)) = tr(E(rho) f(E rho)), in moment form f(x) = x^m,
    m = 1..4, for every family on three density matrices with coherences; control: it fails for
    f(E rho) replaced by rho.
(3) The identity S(E rho) - S(rho) = D(rho || E rho) as an identity of formal logarithms (exact
    LogVecs) wherever both sides have rational spectra: mixed states rho = V diag(p) V^T under the
    rotated rank-one family (ln rho = V diag(ln p) V^T and ln E rho = sum_k ln q_k P_k, the traces
    taken by matrix products), pure states under all four families (the blocks of E rho are rank one),
    and the scrambled two-pair state of the model under E_N, where D = S(E_N rho) = 2 H(16/25).
    D > 0 (rigorous bounds) in every case with rho != E rho, and D = 0 for rho = E rho.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise  # noqa: F401 (the claim has no premises)

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
_DEN = 1 << 160


def _atanh_bounds(z, K=30):
    """Rational bounds on atanh z for 0 <= z <= 1/3."""
    zz = z * z
    term, part = z, F(0)
    for k in range(K):
        part += term / (2 * k + 1)
        term *= zz
    tail = term / ((2 * K + 1) * (1 - zz))
    return part, part + tail


def _out(lo, hi):
    return F((lo.numerator * _DEN) // lo.denominator, _DEN), \
        F(-((-hi.numerator * _DEN) // hi.denominator), _DEN)


def ln_bounds(n):
    """Rational (lower, upper) bounds on ln n, n a positive integer."""
    if n in _LNB:
        return _LNB[n]
    if n == 1:
        return F(0), F(0)
    l2lo, l2hi = _atanh_bounds(F(1, 3))
    l2lo, l2hi = 2 * l2lo, 2 * l2hi
    a = n.bit_length() - 1
    x = F(n, 1 << a)
    zlo, zhi = _atanh_bounds((x - 1) / (x + 1))
    res = _out(a * l2lo + 2 * zlo, a * l2hi + 2 * zhi)
    _LNB[n] = res
    return res


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

N4 = 4


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def madd(A, B, c=1):
    return [[A[i][j] + c * B[i][j] for j in range(len(A))] for i in range(len(A))]


def mmul(A, B):
    return GA.mat_mul(A, B)


def tr(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def transpose(A):
    return [list(r) for r in zip(*A)]


def givens(i, j, c, s):
    G = eye(N4)
    G[i][i], G[j][j], G[i][j], G[j][i] = c, c, -s, s
    return G


def outer(u, v):
    return [[x * y for y in v] for x in u]


U = mmul(mmul(givens(0, 1, F(3, 5), F(4, 5)), givens(2, 3, F(3, 5), F(4, 5))), givens(1, 2, F(4, 5), F(3, 5)))
V = mmul(givens(0, 2, F(4, 5), F(-3, 5)), givens(1, 3, F(3, 5), F(4, 5)))
COLS_U = [[U[i][k] for i in range(N4)] for k in range(N4)]


def coord(i):
    return [F(int(j == i)) for j in range(N4)]


FAMILIES = {
    "E_N": [outer(coord(i), coord(i)) for i in range(N4)],
    "parity": [madd(outer(coord(0), coord(0)), outer(coord(3), coord(3))),
               madd(outer(coord(1), coord(1)), outer(coord(2), coord(2)))],
    "rotated rank one": [outer(u, u) for u in COLS_U],
    "rotated rank two": [madd(outer(COLS_U[0], COLS_U[0]), outer(COLS_U[2], COLS_U[2])),
                         madd(outer(COLS_U[1], COLS_U[1]), outer(COLS_U[3], COLS_U[3]))],
}
A_GEN = [[F(1), F(2), F(3), F(4)], [F(5), F(6), F(7), F(8)],
         [F(9), F(1, 2), F(2, 3), F(3, 5)], [F(4, 7), F(1, 9), F(8, 3), F(11)]]
B_GEN = [[F(2), F(1), F(0), F(5)], [F(3), F(7), F(1, 3), F(2)],
         [F(1, 5), F(4), F(6), F(1)], [F(9), F(2, 7), F(3), F(8)]]
P_SPEC = [F(1, 2), F(1, 4), F(1, 6), F(1, 12)]
PSI = [[F(1, 2), F(1, 2), F(1, 2), F(1, 2)], [F(2, 7), F(3, 7), F(6, 7), F(0)],
       [F(1, 3), F(-2, 3), F(0), F(2, 3)]]


def E(fam, x):
    out = [[F(0)] * N4 for _ in range(N4)]
    for P in fam:
        out = madd(out, mmul(mmul(P, x), P))
    return out


def rho_mixed(W, spec):
    return mmul(mmul(W, [[spec[i] if i == j else F(0) for j in range(N4)] for i in range(N4)]),
                transpose(W))


def check_pinching_structure():
    for fam in FAMILIES.values():
        tot = [[F(0)] * N4 for _ in range(N4)]
        for a, P in enumerate(fam):
            tot = madd(tot, P)
            for b, Q in enumerate(fam):
                assert mmul(P, Q) == (P if a == b else [[F(0)] * N4 for _ in range(N4)])
        assert tot == eye(N4)
        EA, EB = E(fam, A_GEN), E(fam, B_GEN)
        assert E(fam, EA) == EA and EA != A_GEN
        assert tr(EA) == tr(A_GEN)
        assert tr(mmul(EA, B_GEN)) == tr(mmul(A_GEN, EB))


def check_key_lemma_moment_form():
    states = [rho_mixed(V, P_SPEC), rho_mixed(mmul(V, U), [F(3, 5), F(1, 5), F(1, 10), F(1, 10)]),
              outer(PSI[0], PSI[0])]
    for fam in FAMILIES.values():
        for rho in states:
            Er = E(fam, rho)
            assert tr(rho) == 1 and Er != rho
            Em = Er
            for m in range(1, 5):
                assert tr(mmul(rho, Em)) == tr(mmul(Er, Em))
                Em = mmul(Em, Er)
            assert tr(mmul(rho, rho)) != tr(mmul(Er, rho))


def check_entropy_identity_exact():
    # (a) mixed rho = V diag(p) V^T under the rotated rank-one family
    fam = FAMILIES["rotated rank one"]
    rho = rho_mixed(V, P_SPEC)
    Er = E(fam, rho)
    q = [tr(mmul(P, Er)) for P in fam]
    for P, qk in zip(fam, q):
        assert mmul(Er, P) == [[qk * x for x in row] for row in P]
    assert sum(q) == 1
    VtrV = mmul(mmul(transpose(V), rho), V)
    tr_rho_ln_rho = LogVec()
    for i in range(N4):
        tr_rho_ln_rho = tr_rho_ln_rho + LogVec.ln_rat(P_SPEC[i]) * VtrV[i][i]
    tr_rho_ln_Er = LogVec()
    for P, qk in zip(fam, q):
        tr_rho_ln_Er = tr_rho_ln_Er + LogVec.ln_rat(qk) * tr(mmul(rho, P))
    D = tr_rho_ln_rho - tr_rho_ln_Er
    assert D == entropy(q) - entropy(P_SPEC)
    assert logvec_lt(LogVec(), D)
    # rho = E rho: zero deficit
    rho0 = madd(madd(fam[0], fam[1], F(1, 3)), madd(fam[2], fam[3], F(1, 5)), F(1, 2))
    rho0 = [[x * F(15, 29) for x in row] for row in rho0]
    assert tr(rho0) == 1 and E(fam, rho0) == rho0
    # (b) pure states under every family: blocks of E rho are rank one with weight w_k
    for fam in FAMILIES.values():
        for psi in PSI:
            nrm = sum(x * x for x in psi)
            rho = [[x / nrm for x in row] for row in outer(psi, psi)]
            Er = E(fam, rho)
            w = [tr(mmul(P, rho)) for P in fam]
            tr_rho_ln_Er = LogVec()
            for P, wk in zip(fam, w):
                if wk == 0:
                    continue
                Pi = [[x / wk for x in row] for row in mmul(mmul(P, rho), P)]
                assert mmul(Pi, Pi) == Pi and mmul(Er, Pi) == [[wk * x for x in row] for row in Pi]
                tr_rho_ln_Er = tr_rho_ln_Er + LogVec.ln_rat(wk) * tr(mmul(rho, Pi))
            D = LogVec() - tr_rho_ln_Er
            assert D == entropy(w)
            assert (Er == rho) == (D == LogVec())
            if Er != rho:
                assert logvec_lt(LogVec(), D)
    # (c) the model's scrambled two-pair state under E_N: D = S(E_N rho) = 2 H(16/25)
    c, s = F(4, 5), F(3, 5)
    amp = {(b1, b2): (c if b1 == 0 else s) * (c if b2 == 0 else s) * (-1 if b1 and b2 else 1)
           for b1 in (0, 1) for b2 in (0, 1)}
    psi16 = [F(0)] * 16
    for (b1, b2), a in amp.items():
        psi16[b1 * 3 + b2 * 12] = a
    diag = [x * x for x in psi16]
    assert sorted(x for x in diag if x) == [F(81, 625), F(144, 625), F(144, 625), F(256, 625)]
    assert entropy(diag) == entropy([F(16, 25), F(9, 25)]) * 2
