#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""fock.py: exact fermionic Fock spaces, sparse exact operators, and the exterior-algebra
(Chevalley and Fock) models of Clifford algebras, shared by the store's checks (ROADMAP item 6).

Conventions (fixed here):

- Operators are sparse matrices {(row, col): coefficient}, coefficients exact (Fraction, int, GA.QI,
  series.QS/CY); zero entries are never stored. Vectors are sparse dicts {index: coefficient}.
  Dimension is not stored: functions that need it take it (eye(dim)).
- Modes 0..m-1. Two basis orders, named explicitly by the `order` argument (default LSB in
  every function):
  * LSB ("bitmask"): state index s, mode k occupied iff bit k of s is set (mode 0 least
    significant). Used by standard-model.matching-traces and the Cl(2,4) Fock core (fockcore).
  * MSB ("occupation tuple"): index = sum n_k 2^(m-1-k) (mode 0 most significant), so the
    index of |sys> (x) |rec> is sys * 2^k + rec when the system modes come first. Used by
    descent-lift.parity-alone-forces-second-rung and its siblings.
  The Jordan-Wigner sign is the same in both: a_k^dag |n> = (-1)^(n_0 + ... + n_{k-1}) |n + e_k>
  (occupied modes with LOWER label are passed), so only the index layout differs.
- comm(A, B) = AB - BA and acomm(A, B) = AB + BA (plain, NOT halved; gtg.comm is the halved
  commutator product of geometric algebra).
- dag(A) is the conjugate transpose (entries with .conj() are conjugated; rationals unchanged);
  transpose(A) does not conjugate.
- Majoranas: kind "real" (standard-model gam): gamma_{2k} = a_k^dag + a_k (square +1),
  gamma_{2k+1} = a_k - a_k^dag (square -1); kind "herm": gamma_{2k} = a_k^dag + a_k,
  gamma_{2k+1} = i (a_k^dag - a_k) (both square +1, coefficients GA.QI).
- Chevalley model of Cl(V, B) on Lambda V (dim V = n, LSB bitmask basis, wedge from the left):
  c(alpha) = alpha ^ + iota_{B(alpha, .)}, so c(alpha)^2 = B(alpha, alpha); this is GA.ext_c as
  a sparse operator.
- Fock (spinor) model of a Clifford algebra on Lambda W, W maximal isotropic: each mode k is a
  pair of generators (a, b) of the GA signature sq; with w = wedge_k, i = iota_k:
  (+1, -1): c(e_a) = w + i, c(e_b) = w - i;  (-1, -1): c(e_a) = w - i, c(e_b) = -I(w + i);
  (+1, +1): c(e_a) = w + i, c(e_b) = I(w - i)  (I = GA.QI_I). With the pairs (0, 2), (1, 3), (4, 5)
  of GA.sig(2, 4) this is exactly the fockcore model of Cl(2,4)_C on C^8 (fock_cl24).

Pure functions; no I/O at import; Brython-safe (no dict.setdefault: the page's Brython keys
setdefault entries by str(key); every accumulation here uses d[k] = d.get(k, 0) + x).
"""

from fractions import Fraction

import GA

F = Fraction
LSB = "lsb"
MSB = "msb"


def _z(x):
    """Ints and bools become Fractions (as the pasted helpers did); other exact values pass through."""
    return F(int(x)) if isinstance(x, (int, bool)) else x


# ---------------------------------------------------------------------------
# 1. basis states
# ---------------------------------------------------------------------------

def occ(i, m, order=LSB):
    """Occupation tuple (n_0, ..., n_{m-1}) of basis index i (descent-lift occ is order=MSB)."""
    if order == LSB:
        return tuple((i >> k) & 1 for k in range(m))
    return tuple((i >> (m - 1 - k)) & 1 for k in range(m))


def idx(t, order=LSB):
    """Basis index of an occupation tuple (inverse of occ)."""
    out = 0
    if order == LSB:
        for k, b in enumerate(t):
            out |= (b & 1) << k
        return out
    for b in t:
        out = 2 * out + b
    return out


def bit(k, m, order=LSB):
    """The integer mask of mode k (1 << k in LSB order, 1 << (m-1-k) in MSB order)."""
    return 1 << k if order == LSB else 1 << (m - 1 - k)


def popcount(s):
    """Number of set bits of a nonnegative integer."""
    return bin(s).count("1")


def jw_sign(s, k, m, order=LSB):
    """(-1)^(number of occupied modes with label < k) in state s."""
    if order == LSB:
        below = s & ((1 << k) - 1)
    else:
        below = s >> (m - k)
    return -1 if popcount(below) % 2 else 1


def states(m, parity=None):
    """Basis indices 0..2^m - 1, optionally only those of even (parity=0) or odd (1) mode number."""
    out = range(2 ** m)
    if parity is None:
        return list(out)
    return [s for s in out if popcount(s) % 2 == parity]


def ket(t, order=LSB):
    """The basis vector |t> of an occupation tuple."""
    return {idx(t, order): F(1)}


def basis_vec(i):
    """The basis vector of index i."""
    return {i: F(1)}


# ---------------------------------------------------------------------------
# 2. sparse operators
# ---------------------------------------------------------------------------

def mm(*Ms):
    """Matrix product of sparse operators (left to right)."""
    A = Ms[0]
    for B in Ms[1:]:
        rows = {}
        for (k, j), c in B.items():
            lst = rows.get(k)
            if lst is None:
                lst = []
                rows[k] = lst
            lst.append((j, c))
        out = {}
        for (i, k), a in A.items():
            for j, b in rows.get(k, ()):
                out[(i, j)] = out.get((i, j), 0) + a * b
        A = {key: v for key, v in out.items() if v}
    return A


def madd(*Ms):
    """Sum of sparse operators."""
    out = {}
    for M in Ms:
        for key, v in M.items():
            out[key] = out.get(key, 0) + v
    return {key: v for key, v in out.items() if v}


def msc(c, M):
    """c M for a scalar c."""
    c = _z(c)
    if not c:
        return {}
    out = {}
    for key, v in M.items():
        t = c * v
        if t:
            out[key] = t
    return out


def msub(A, B):
    """A - B."""
    return madd(A, msc(-1, B))


def eye(d):
    """Identity on dimension d."""
    return {(i, i): F(1) for i in range(d)}


def diag(fn, d):
    """Diagonal operator with entries fn(i), i < d."""
    out = {}
    for i in range(d):
        v = _z(fn(i))
        if v:
            out[(i, i)] = v
    return out


def transpose(A):
    """Transpose (no conjugation)."""
    return {(j, i): c for (i, j), c in A.items()}


def _conj(c):
    return c.conj() if hasattr(c, "conj") else c


def dag(A):
    """Conjugate transpose (rational entries are unchanged, so on Fraction operators this is the transpose)."""
    return {(j, i): _conj(c) for (i, j), c in A.items()}


def comm(A, B):
    """AB - BA (not halved)."""
    return msub(mm(A, B), mm(B, A))


def acomm(A, B):
    """AB + BA (not halved)."""
    return madd(mm(A, B), mm(B, A))


def meq(A, B):
    """Exact equality of sparse operators."""
    return not msub(A, B)


def is_zero(A):
    """True for the zero operator or vector."""
    return not A


def trace(M):
    """Trace."""
    return sum((c for (i, j), c in M.items() if i == j), F(0))


def mpow(A, n, d):
    """A^n (n >= 0) on dimension d."""
    out = eye(d)
    for _ in range(n):
        out = mm(out, A)
    return out


def restrict(A, keep):
    """The entries of A with row and column in keep."""
    S = set(keep)
    return {k: x for k, x in A.items() if k[0] in S and k[1] in S}


def kron(A, B, dB):
    """Tensor product A (x) B with index i * dB + j (B of dimension dB)."""
    out = {}
    for (i, j), a in A.items():
        for (k, l), b in B.items():
            t = a * b
            if t:
                out[(i * dB + k, j * dB + l)] = t
    return out


def to_dense(M, n, zero=None, ncols=None):
    """Dense list-of-rows form (zero entries = zero, default Fraction(0))."""
    zero = F(0) if zero is None else zero
    ncols = n if ncols is None else ncols
    out = [[zero] * ncols for _ in range(n)]
    for (i, j), c in M.items():
        out[i][j] = c
    return out


def from_dense(D):
    """Sparse form of a dense list-of-rows matrix."""
    return {(i, j): c for i, row in enumerate(D) for j, c in enumerate(row) if c}


# ---------------------------------------------------------------------------
# 3. vectors
# ---------------------------------------------------------------------------

def apply(M, v):
    """M v for a sparse operator and a sparse vector."""
    out = {}
    for (i, j), c in M.items():
        if j in v:
            out[i] = out.get(i, 0) + c * v[j]
    return {i: c for i, c in out.items() if c}


def vadd(*vs):
    """Sum of sparse vectors."""
    out = {}
    for v in vs:
        for i, c in v.items():
            out[i] = out.get(i, 0) + c
    return {i: c for i, c in out.items() if c}


def vsc(c, v):
    """c v."""
    c = _z(c)
    return {i: c * x for i, x in v.items() if c * x} if c else {}


def outer(u, v):
    """|u><v| without conjugation (u v^T)."""
    return {(i, j): a * b for i, a in u.items() for j, b in v.items() if a * b}


def ket_bra(u, v):
    """|u><v| = u v^dag (conjugates v)."""
    return {(i, j): a * _conj(b) for i, a in u.items() for j, b in v.items() if a * _conj(b)}


def inner(u, v):
    """Bilinear sum u_i v_i (no conjugation)."""
    return sum((c * v.get(i, 0) for i, c in u.items()), F(0))


def braket(u, v):
    """<u|v> = sum conj(u_i) v_i."""
    return sum((_conj(c) * v.get(i, 0) for i, c in u.items()), F(0))


# ---------------------------------------------------------------------------
# 4. creation, annihilation, number, parity, Majoranas (Jordan-Wigner)
# ---------------------------------------------------------------------------

def cre(k, m, order=LSB):
    """a_k^dag on m modes: |n> -> (-1)^(n_0 + ... + n_{k-1}) |n + e_k> (standard-model create(k) in LSB)."""
    b = bit(k, m, order)
    out = {}
    for s in range(2 ** m):
        if not s & b:
            out[(s | b, s)] = F(jw_sign(s, k, m, order))
    return out


create = cre


def ann(k, m, order=LSB):
    """a_k on m modes: |n> -> (-1)^(n_0 + ... + n_{k-1}) n_k |n - e_k> (descent-lift ann is order=MSB)."""
    b = bit(k, m, order)
    out = {}
    for s in range(2 ** m):
        if s & b:
            out[(s & ~b, s)] = F(jw_sign(s, k, m, order))
    return out


def ann_on(k, v):
    """a_k applied directly to a sparse state vector in the LSB bitmask basis (any number of modes)."""
    out = {}
    b = 1 << k
    for s, c in v.items():
        if s & b:
            t = s ^ b
            out[t] = out.get(t, 0) + (-c if popcount(s & (b - 1)) % 2 else c)
    return {s: c for s, c in out.items() if c}


def cre_on(k, v):
    """a_k^dag applied directly to a sparse state vector in the LSB bitmask basis (any number of modes)."""
    out = {}
    b = 1 << k
    for s, c in v.items():
        if not s & b:
            t = s | b
            out[t] = out.get(t, 0) + (-c if popcount(s & (b - 1)) % 2 else c)
    return {s: c for s, c in out.items() if c}


def num(k, m, order=LSB):
    """Number operator N_k = a_k^dag a_k (diagonal)."""
    b = bit(k, m, order)
    return {(s, s): F(1) for s in range(2 ** m) if s & b}


def num_total(m, modes=None, order=LSB):
    """sum of N_k over modes (default all)."""
    modes = range(m) if modes is None else modes
    out = {}
    for s in range(2 ** m):
        c = sum(1 for k in modes if s & bit(k, m, order))
        if c:
            out[(s, s)] = F(c)
    return out


def mode_parity(k, m, order=LSB):
    """(-1)^(N_k) = 1 - 2 N_k (descent-lift par)."""
    b = bit(k, m, order)
    return {(s, s): F(-1 if s & b else 1) for s in range(2 ** m)}


def parity(m, modes=None, order=LSB):
    """Total parity (-1)^N over the given modes (default all)."""
    modes = range(m) if modes is None else modes
    mask = 0
    for k in modes:
        mask |= bit(k, m, order)
    return {(s, s): F(-1 if popcount(s & mask) % 2 else 1) for s in range(2 ** m)}


def majorana(p, m, order=LSB, kind="real"):
    """Majorana p of mode p // 2: real form (v + w, w - v; squares +1, -1) or herm form (v + w, i(v - w))."""
    k = p // 2
    v, w = cre(k, m, order), ann(k, m, order)
    if p % 2 == 0:
        return madd(v, w)
    if kind == "real":
        return msub(w, v)
    if kind == "herm":
        return msc(GA.QI_I, msub(v, w))
    raise ValueError("majorana kind must be 'real' or 'herm'")


def is_even_op(M, m=None):
    """True when M preserves total parity (index parity = popcount parity in both orders)."""
    return all((popcount(i) + popcount(j)) % 2 == 0 for (i, j) in M)


def is_even_vec(v):
    """True when every component of v has an even number of occupied modes."""
    return all(popcount(i) % 2 == 0 for i in v)


def even_states(m, order=LSB):
    """Occupation tuples of even mode number (descent-lift even_states is order=MSB)."""
    return [occ(i, m, order) for i in range(2 ** m) if popcount(i) % 2 == 0]


# ---------------------------------------------------------------------------
# 5. partial traces and states
# ---------------------------------------------------------------------------

def ptrace_rec(M, k):
    """Trace out the last k modes (low bits: the record in MSB order); returns the system operator."""
    d = 2 ** k
    out = {}
    for (i, j), c in M.items():
        if i % d == j % d:
            key = (i // d, j // d)
            out[key] = out.get(key, 0) + c
    return {key: v for key, v in out.items() if v}


def ptrace_sys(M, k):
    """Trace out all but the last k modes (keep the low bits); returns the record operator."""
    d = 2 ** k
    out = {}
    for (i, j), c in M.items():
        if i // d == j // d:
            key = (i % d, j % d)
            out[key] = out.get(key, 0) + c
    return {key: v for key, v in out.items() if v}


def ptrace(M, m, traced, order=LSB):
    """Trace out the modes in `traced` (bitwise; no fermionic sign) and relabel the kept modes in order."""
    tmask = 0
    for k in traced:
        tmask |= bit(k, m, order)
    keep = [k for k in range(m) if k not in set(traced)]
    mk = len(keep)

    def squeeze(s):
        t = 0
        for pos, k in enumerate(keep):
            if s & bit(k, m, order):
                t |= bit(pos, mk, order)
        return t
    out = {}
    for (i, j), c in M.items():
        if i & tmask == j & tmask:
            key = (squeeze(i), squeeze(j))
            out[key] = out.get(key, 0) + c
    return {key: v for key, v in out.items() if v}


def purity(rho):
    """Tr(rho^2)/Tr(rho)^2 (rho need not be normalised)."""
    return trace(mm(rho, rho)) / trace(rho) ** 2


# ---------------------------------------------------------------------------
# 6. exterior algebra: wedge, contraction, Chevalley and Fock models of Clifford algebras
# ---------------------------------------------------------------------------

def wedge_op(i, n, order=LSB):
    """Left exterior multiplication by the basis vector i on Lambda(C^n) (= cre(i, n, order))."""
    return cre(i, n, order)


def contract_op(i, n, order=LSB):
    """Contraction iota_i by the dual basis covector e^i on Lambda(C^n) (= ann(i, n, order))."""
    return ann(i, n, order)


def contraction(f, n, order=LSB):
    """Contraction iota_f by the covector with values f[j] = f(e_j)."""
    return madd(*[msc(f[j], contract_op(j, n, order)) for j in range(n) if f[j]]) if any(f) else {}


def chevalley(alpha, B, order=LSB):
    """c(alpha) = alpha ^ + iota_{B(alpha, .)} on Lambda V (dim V = len(alpha)): c(alpha)^2 = B(alpha, alpha)."""
    n = len(alpha)
    wed = madd(*[msc(alpha[i], wedge_op(i, n, order)) for i in range(n) if alpha[i]]) if any(alpha) else {}
    f = [sum((alpha[i] * B[i][j] for i in range(n)), F(0)) for j in range(n)]
    return madd(wed, contraction(f, n, order))


def ext_state(state, n=None, order=LSB):
    """Sparse vector of a GA.ext_* state {frozenset: coeff} (n needed for order=MSB)."""
    out = {}
    for S, c in state.items():
        s = 0
        for k in S:
            s |= bit(k, n, order)
        if c:
            out[s] = c
    return out


def fock_generators(pairs, sq, order=LSB):
    """Operators c(e_k) of the Fock model on Lambda W, mode j built from the generator pair pairs[j] of sq."""
    m = len(pairs)
    I = GA.QI_I
    gens = [None] * len(sq)
    for j, (a, b) in enumerate(pairs):
        w, i = wedge_op(j, m, order), contract_op(j, m, order)
        sa, sb = sq[a], sq[b]
        if sa == 1 and sb == -1:
            gens[a], gens[b] = madd(w, i), msub(w, i)
        elif sa == -1 and sb == -1:
            gens[a], gens[b] = msub(w, i), msc(-I, madd(w, i))
        elif sa == 1 and sb == 1:
            gens[a], gens[b] = madd(w, i), msc(I, msub(w, i))
        elif sa == -1 and sb == 1:
            gens[a], gens[b] = msub(w, i), madd(w, i)
        else:
            raise ValueError("fock_generators: degenerate generator in a pair")
    return gens


def fock_cl24():
    """The fockcore model of Cl(2,4)_C on C^8: generators of GA.sig(2, 4) paired (0,2), (1,3), (4,5), LSB order."""
    return fock_generators([(0, 2), (1, 3), (4, 5)], GA.sig(2, 4), LSB)


def blade_table(gens, dim):
    """{blade: operator} for every GA blade of the generators (products in increasing index order)."""
    n = len(gens)
    out = {(): eye(dim)}
    for b in GA.all_blades(n):
        if b:
            out[b] = mm(out[b[:-1]], gens[b[-1]])
    return out


def rep(x, table):
    """The operator of a GA multivector x (exact or GA.QI coefficients) from a blade_table."""
    return madd(*[msc(c, table[b]) for b, c in x.items()]) if x else {}


def spin_rep(B, table):
    """Spinor action of a bivector: rho(B) = rep(B)/2, so [rho(B), c(x)] = c(B . x)."""
    return msc(F(1, 2), rep(B, table))


def clifford_ok(gens, sq, dim):
    """True when c(e_a) c(e_b) + c(e_b) c(e_a) = 2 sq[a] delta_ab for all generators."""
    for a in range(len(gens)):
        for b in range(a, len(gens)):
            want = msc(2 * sq[a], eye(dim)) if a == b else {}
            if not meq(acomm(gens[a], gens[b]), want):
                return False
    return True
