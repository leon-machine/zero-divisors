"""rungs.rung-spinor-module-mixings: exact checks.

The complexified spinor module of the n-th rung Cl(2+n, 4+n) (n = 0..3) as a Fock space over Q(i)
(GA.QI): m = 3 + n modes, modes 0..n-1 the new rung modes (R_n), modes n..n+2 the old modes (W).
States are bitmasks; a_i is the Jordan-Wigner annihilator. Operators are sparse matrices
{column: {row: QI}}. The real generators: for the old modes n, n+1 and every new mode a real
hyperbolic pair e = a^dag + a (square +1), f = a^dag - a (square -1); for the old mode n+2 two negative
generators g1 = i(a + a^dag), g2 = a - a^dag (both square -1). That is 2+n positive and 4+n negative
generators: the complexification of Cl(2+n, 4+n). Majoranas gamma_{2i} = a_i + a_i^dag,
gamma_{2i+1} = i(a_i - a_i^dag).
(1) The 6+2n generators satisfy the relations of Cl(2+n,4+n) on every state; dim = 2^(3+n) = 8, 16, 32,
    64; the vacuum spans the common kernel of the annihilators and the creation monomials on it span
    the module (so it is irreducible); the bigraded pieces have dimension C(n,j) C(3,k); the product
    of all generators acts as a scalar times (-1)^(j+k) (chirality = parity of j + k); at n = 2 the
    module has 5 modes and its halves have dimension 16.
(2) Block unitaries B (+) A (rational unitaries over Q(i), B on W, A on R_n) act by Lambda(B (+) A): the
    operator with matrix entries the minors det(U[T,S]) is unitary, preserves every piece
    Lambda^j R_n (x) Lambda^k W, and is Bogoliubov-covariant: Lambda(U) a_i^dag = sum_l U_li a_l^dag Lambda(U).
(3) The Majoranas are Hermitian, square to 1 and anticommute: a Euclidean Clifford algebra on 6+2n
    generators. The bilinears gamma_p gamma_q (p < q) act on span(gamma) by real matrices (on the Fock
    space for n <= 2, each commutator confirmed to be a real combination of the gammas; in GA.py's
    Cl(6+2n, 0) for every n) spanning a space of dimension 15, 28, 45, 66 = dim so(6+2n); for n <= 1 a
    rational rotor c + s gamma_p gamma_q (c^2 + s^2 = 1) is unitary and rotates span(gamma) orthogonally. At n = 2 each chirality half has a
    one-dimensional common kernel for the lowering operators of so(10) (a_i a_j and a_j^dag a_i,
    i < j), so Spin(10) acts irreducibly on each half (complete reducibility imported). Number
    preserving: for a sample X in u(m), phi(X) = (1/2) sum X_ij [a_i^dag, a_j] (quadratic in the
    Majoranas) equals dGamma(X) - (tr X / 2) 1, acts on a_k^dag as X does (the Lambda (x) det^(-1/2) action) and agrees with dGamma(X) when
    tr X = 0; the double cover: (gamma_{2i} gamma_{2i+1})^2 = -1 while conjugation by it negates a_i^dag
    only, so -1 in Spin covers the identity of U.
(4) At n = 3, u(3) (+) u(3) (18 generators) acts faithfully on the module (rank 18 on the one-mode
    sector), acts on the cell sector Lambda^1 R_3 (x) Lambda^1 W with rank 17, its kernel generator
    (i I, -i I) has eigenvalue i(j - k) on each piece (zero exactly on the cells) and is trace-free, and
    the trace-free subalgebra (17) acts on the cells with rank 16; at n = 2 u(2) (+) u(3) (13) acts on
    the cells with rank 12, the kernel generator is not trace-free, and s(u(2) (+) u(3)) (12) acts with
    rank 12. The counts 2^(3+n), dim so(6+2n) and dim(u(3) (+) u(n)) = 9 + n^2 are the computed
    dimensions and ranks.
Not computed: the identification with Hypothesis (S) beyond the shape of the module and action, and
the global (group-level) faithfulness beyond the Lie algebra.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from pyutil import get_or_set
from tp_premise import premise

QI = GA.QI
I_ = QI(0, 1)
ZERO = QI(0)


# ---- sparse operators over Q(i) ----
def op_add(*ops):
    out = {}
    for A in ops:
        for c, col in A.items():
            d = get_or_set(out, c, {})
            for r, v in col.items():
                d[r] = d.get(r, ZERO) + v
    return {c: {r: v for r, v in col.items() if v} for c, col in out.items() if any(col.values())}


def op_scal(z, A):
    z = QI._co(z)
    return {c: {r: v * z for r, v in col.items()} for c, col in A.items()} if z else {}


def op_mul(A, B):
    out = {}
    for c, colB in B.items():
        acc = {}
        for k, y in colB.items():
            for r, x in A.get(k, {}).items():
                acc[r] = acc.get(r, ZERO) + x * y
        acc = {r: v for r, v in acc.items() if v}
        if acc:
            out[c] = acc
    return out


def op_eq(A, B):
    return op_add(A, op_scal(-1, B)) == {}


def op_dag(A):
    out = {}
    for c, col in A.items():
        for r, v in col.items():
            get_or_set(out, r, {})[c] = v.conj()
    return out


def ident(dim):
    return {s: {s: QI(1)} for s in range(dim)}


def annih(i, m):
    out = {}
    for b in range(2 ** m):
        if b >> i & 1:
            sign = (-1) ** bin(b & ((1 << i) - 1)).count("1")
            out[b] = {b ^ (1 << i): QI(sign)}
    return out


class Fock(object):
    def __init__(self, n):
        self.n, self.m = n, 3 + n
        self.dim = 2 ** self.m
        self.a = [annih(i, self.m) for i in range(self.m)]
        self.ad = [op_dag(x) for x in self.a]
        self.one = ident(self.dim)

    def jk(self, b):
        return (sum(b >> i & 1 for i in range(self.n)), sum(b >> i & 1 for i in range(self.n, self.m)))

    def generators(self):
        """(operator, square) for the 6 + 2n real generators of Cl(2+n, 4+n)."""
        gens = []
        real = list(range(self.n)) + [self.n, self.n + 1]
        for i in real:
            gens.append((op_add(self.ad[i], self.a[i]), 1))
            gens.append((op_add(self.ad[i], op_scal(-1, self.a[i])), -1))
        c = self.n + 2
        gens.append((op_scal(I_, op_add(self.a[c], self.ad[c])), -1))
        gens.append((op_add(self.a[c], op_scal(-1, self.ad[c])), -1))
        return gens

    def majoranas(self):
        out = []
        for i in range(self.m):
            out.append(op_add(self.a[i], self.ad[i]))
            out.append(op_scal(I_, op_add(self.a[i], op_scal(-1, self.ad[i]))))
        return out

    def dgamma(self, X):
        """sum_ij X_ij a_i^dag a_j for an m x m matrix X of QI."""
        terms = [op_scal(X[i][j], op_mul(self.ad[i], self.a[j]))
                 for i in range(self.m) for j in range(self.m) if X[i][j]]
        return op_add(*terms) if terms else {}


def kernel_dim(ops, states, dim):
    """Dimension of the common kernel, inside span(states), of the given operators."""
    rows = []
    for A in ops:
        for r in range(dim):
            rows.append([A.get(s, {}).get(r, ZERO) for s in states])
    return len(states) - GA.field_rank(rows) if rows else len(states)


def u_basis(k):
    """Real basis of u(k) as k x k matrices of QI."""
    out = []
    for i in range(k):
        out.append([[I_ if (r, c) == (i, i) else ZERO for c in range(k)] for r in range(k)])
    for i, j in combinations(range(k), 2):
        out.append([[QI(1) if (r, c) == (i, j) else (QI(-1) if (r, c) == (j, i) else ZERO)
                     for c in range(k)] for r in range(k)])
        out.append([[I_ if (r, c) in ((i, j), (j, i)) else ZERO for c in range(k)] for r in range(k)])
    return out


def block(XW, XR, n):
    """The block matrix acting by XR on modes 0..n-1 (R_n) and XW on modes n..n+2 (W)."""
    m = 3 + n
    M = [[ZERO] * m for _ in range(m)]
    for r in range(n):
        for c in range(n):
            M[r][c] = XR[r][c]
    for r in range(3):
        for c in range(3):
            M[n + r][n + c] = XW[r][c]
    return M


def real_rank(ops, states):
    rows = []
    for A in ops:
        v = []
        for s in states:
            for t in states:
                z = A.get(s, {}).get(t, ZERO)
                v.extend([z.re, z.im])
        rows.append(v)
    return GA.rank_of_vectors(rows)


def check_spinor_module_irreducible_graded():
    premise("rungs.imported-tower-one-qubit-per-rung")
    premise("rungs.imported-spinor-identification-witt-data-line")
    for n in range(4):
        fk = Fock(n)
        gens = fk.generators()
        assert len(gens) == 6 + 2 * n
        assert sum(1 for _, s in gens if s == 1) == 2 + n
        for i, (x, sx) in enumerate(gens):
            assert op_eq(op_mul(x, x), op_scal(sx, fk.one))
            for y, _ in gens[i + 1:]:
                assert op_add(op_mul(x, y), op_mul(y, x)) == {}
        assert fk.dim == 2 ** (3 + n)
        states = list(range(fk.dim))
        assert kernel_dim(fk.a, states, fk.dim) == 1
        assert all(fk.a[i].get(0) is None for i in range(fk.m))
        imgs = []
        for b in states:
            v = {0: QI(1)}
            for i in reversed([i for i in range(fk.m) if b >> i & 1]):
                v = {r: x for r, x in op_mul(fk.ad[i], {0: v}).get(0, {}).items()}
            imgs.append([v.get(r, ZERO) for r in states])
        assert GA.field_rank(imgs) == fk.dim
        counts = {}
        for b in states:
            counts[fk.jk(b)] = counts.get(fk.jk(b), 0) + 1
        for (j, k), c in counts.items():
            assert c == len(list(combinations(range(n), j))) * len(list(combinations(range(3), k)))
        vol = fk.one
        for x, _ in gens:
            vol = op_mul(vol, x)
        c0 = vol[0][0]
        for b in states:
            j, k = fk.jk(b)
            assert vol[b] == {b: c0 * (-1) ** (j + k)}
        if n == 2:
            assert fk.m == 5 and sum(1 for b in states if sum(fk.jk(b)) % 2 == 0) == 16
    return True


def cayley_unitary(H):
    """(1 + i H)(1 - i H)^{-1} for a Hermitian H over Q(i): a rational unitary."""
    k = len(H)
    P = [[(QI(1) if r == c else ZERO) + I_ * H[r][c] for c in range(k)] for r in range(k)]
    Mm = [[(QI(1) if r == c else ZERO) - I_ * H[r][c] for c in range(k)] for r in range(k)]
    cols = [GA.field_solve(Mm, [QI(1) if r == c else ZERO for r in range(k)]) for c in range(k)]
    Minv = [[cols[c][r] for c in range(k)] for r in range(k)]
    return GA.field_mat_mul(P, Minv)


def det(Mx):
    if not Mx:
        return QI(1)
    tot = ZERO
    for c in range(len(Mx)):
        minor = [row[:c] + row[c + 1:] for row in Mx[1:]]
        if Mx[0][c]:
            tot = tot + Mx[0][c] * det(minor) * (-1) ** c
    return tot


def lambda_op(U, m):
    out = {}
    for S in range(2 ** m):
        sl = [i for i in range(m) if S >> i & 1]
        col = {}
        for T in range(2 ** m):
            tl = [i for i in range(m) if T >> i & 1]
            if len(tl) != len(sl):
                continue
            z = det([[U[r][c] for c in sl] for r in tl])
            if z:
                col[T] = z
        out[S] = col
    return out


HW = [[QI(1), QI(0, 2), ZERO], [QI(0, -2), QI(-1), QI(1)], [ZERO, QI(1), QI(3)]]
HR = {1: [[QI(2)]], 2: [[QI(0), QI(1, 1)], [QI(1, -1), QI(2)]],
      3: [[QI(1), ZERO, QI(0, 1)], [ZERO, QI(-2), QI(1)], [QI(0, -1), QI(1), ZERO]]}


def check_split_unitaries_act_by_exterior_powers():
    premise("rungs.imported-fock-representation-bogoliubov-group")
    for n in (1, 2, 3):
        fk = Fock(n)
        B, A = cayley_unitary(HW), cayley_unitary(HR[n])
        U = block(B, A, n)
        Ud = [[U[c][r].conj() for c in range(fk.m)] for r in range(fk.m)]
        assert GA.field_mat_mul(Ud, U) == [[QI(1) if r == c else ZERO for c in range(fk.m)]
                                           for r in range(fk.m)]
        L = lambda_op(U, fk.m)
        assert op_eq(op_mul(op_dag(L), L), fk.one)
        for S, col in L.items():
            for T in col:
                assert fk.jk(T) == fk.jk(S)
        for i in range(fk.m):
            lhs = op_mul(L, fk.ad[i])
            rhs = op_add(*[op_scal(U[l][i], op_mul(fk.ad[l], L)) for l in range(fk.m) if U[l][i]])
            assert op_eq(lhs, rhs)
    return True


def check_majoranas_and_bogoliubov_dimension():
    premise("rungs.imported-fock-representation-bogoliubov-group")
    premise("rungs.imported-tower-one-qubit-per-rung")
    for n in range(4):
        fk = Fock(n)
        gam = fk.majoranas()
        N = len(gam)
        for p in range(N):
            assert op_eq(op_dag(gam[p]), gam[p]) and op_eq(op_mul(gam[p], gam[p]), fk.one)
            for q in range(p + 1, N):
                assert op_add(op_mul(gam[p], gam[q]), op_mul(gam[q], gam[p])) == {}
        # adjoint action of the bilinears on span(gamma), on the Fock space for n <= 2: read the
        # gamma-coefficients off the vacuum column (gamma_2i |0> = |i>, gamma_2i+1 |0> = -i |i>),
        # confirming each commutator is exactly that real combination
        if n <= 2:
            mats = []
            for p, q in combinations(range(N), 2):
                Bpq = op_mul(gam[p], gam[q])
                row = []
                for r in range(N):
                    cm = op_add(op_mul(Bpq, gam[r]), op_scal(-1, op_mul(gam[r], Bpq)))
                    v0 = cm.get(0, {})
                    cf = []
                    for i in range(fk.m):
                        z = v0.get(1 << i, ZERO)
                        cf.extend([z.re, -z.im])
                    rebuilt = op_add(*[op_scal(cf[t], gam[t]) for t in range(N) if cf[t]]) if any(cf) else {}
                    assert op_eq(cm, rebuilt)
                    row.extend(cf)
                mats.append(row)
            assert GA.rank_of_vectors(mats) == N * (N - 1) // 2
        # the same algebra is Cl(N, 0) (the relations above): ranks in GA.py for every n
        SE = tuple([1] * N)
        mats = []
        for p, q in combinations(range(N), 2):
            Bpq = GA.mul(GA.gen(p), GA.gen(q), SE)
            row = []
            for r in range(N):
                cm = GA.sub(GA.mul(Bpq, GA.gen(r), SE), GA.mul(GA.gen(r), Bpq, SE))
                assert all(len(b) == 1 for b in cm)
                row.extend(cm.get((t,), F(0)) for t in range(N))
            mats.append(row)
        assert GA.rank_of_vectors(mats) == N * (N - 1) // 2 == [15, 28, 45, 66][n]
    return True


def check_number_preserving_part_and_double_cover():
    premise("rungs.imported-fock-representation-bogoliubov-group")
    for n in range(4):
        fk = Fock(n)
        gam = fk.majoranas()
        N = len(gam)
        if n <= 1:
            R = op_add(op_scal(F(3, 5), fk.one), op_scal(F(4, 5), op_mul(gam[0], gam[N - 1])))
            assert op_eq(op_mul(op_dag(R), R), fk.one)
            img = op_mul(op_mul(R, gam[0]), op_dag(R))
            assert op_eq(img, op_add(op_scal(F(-7, 25), gam[0]), op_scal(F(-24, 25), gam[N - 1])))
        # number-preserving part: phi(X) = (1/2) sum X_ij [a_i^dag, a_j] = dGamma(X) - tr(X)/2
        X = [[ZERO] * fk.m for _ in range(fk.m)]
        X[0][0], X[0][1], X[1][0], X[fk.m - 1][fk.m - 1] = I_, QI(2, 1), QI(-2, 1), QI(0, 3)
        phi = op_add(*[op_scal(X[i][j] * F(1, 2),
                               op_add(op_mul(fk.ad[i], fk.a[j]), op_scal(-1, op_mul(fk.a[j], fk.ad[i]))))
                       for i in range(fk.m) for j in range(fk.m) if X[i][j]])
        trX = sum((X[i][i] for i in range(fk.m)), ZERO)
        assert op_eq(phi, op_add(fk.dgamma(X), op_scal(trX * F(-1, 2), fk.one)))
        for k in range(fk.m):
            cm = op_add(op_mul(phi, fk.ad[k]), op_scal(-1, op_mul(fk.ad[k], phi)))
            want = op_add(*[op_scal(X[i][k], fk.ad[i]) for i in range(fk.m) if X[i][k]]) \
                if any(X[i][k] for i in range(fk.m)) else {}
            assert op_eq(cm, want)
        # double cover: (gamma_0 gamma_1)^2 = -1, and conjugation by it negates a_0^dag only
        g01 = op_mul(gam[0], gam[1])
        assert op_eq(op_mul(g01, g01), op_scal(-1, fk.one))
        ginv = op_scal(-1, g01)
        for k in range(fk.m):
            conj = op_mul(op_mul(g01, fk.ad[k]), ginv)
            assert op_eq(conj, op_scal(-1 if k == 0 else 1, fk.ad[k]))
    return True


def check_spin10_irreducible_on_each_half():
    premise("rungs.imported-fock-representation-bogoliubov-group")
    fk = Fock(2)
    low = []
    for i, j in combinations(range(fk.m), 2):
        low.append(op_mul(fk.a[i], fk.a[j]))
        low.append(op_mul(fk.ad[j], fk.a[i]))
    for parity in (0, 1):
        half = [b for b in range(fk.dim) if sum(fk.jk(b)) % 2 == parity]
        assert len(half) == 16
        assert kernel_dim(low, half, fk.dim) == 1
    return True


def check_cell_action_ranks_and_faithfulness():
    premise("rungs.imported-ladder-automorphism-group-no-lepton")
    for n in (2, 3):
        fk = Fock(n)
        gensW = [block(X, [[ZERO] * n for _ in range(n)], n) for X in u_basis(3)]
        gensR = [block([[ZERO] * 3 for _ in range(3)], X, n) for X in u_basis(n)]
        gens = gensW + gensR
        assert len(gens) == 9 + n * n
        ops = [fk.dgamma(X) for X in gens]
        one_mode = [1 << i for i in range(fk.m)]
        assert real_rank(ops, one_mode) == 9 + n * n
        cells = [b for b in range(fk.dim) if fk.jk(b) == (1, 1)]
        assert len(cells) == 3 * n
        full = real_rank(ops, cells)
        # trace-free subalgebra: off-diagonal generators plus trace-free diagonal combinations
        diag = [k for k, X in enumerate(gens) if sum((X[i][i] for i in range(fk.m)), ZERO)]
        rest = [ops[k] for k in range(len(gens)) if k not in diag]
        d0 = diag[0]
        tf = rest + [op_add(ops[d0], op_scal(-1, ops[k])) for k in diag[1:]]
        assert len(tf) == 8 + n * n
        tfr = real_rank(tf, cells)
        Kmat = block([[-I_ if r == c else ZERO for c in range(3)] for r in range(3)],
                     [[I_ if r == c else ZERO for c in range(n)] for r in range(n)], n)
        Kgen = fk.dgamma(Kmat)
        for b in range(fk.dim):
            j, k = fk.jk(b)
            assert Kgen.get(b, {}) == ({b: I_ * (j - k)} if j != k else {})
        trK = sum((Kmat[i][i] for i in range(fk.m)), ZERO)
        if n == 3:
            assert (full, tfr) == (17, 16) and trK == ZERO
        else:
            assert (full, tfr) == (12, 12) and trK != ZERO
    return True
