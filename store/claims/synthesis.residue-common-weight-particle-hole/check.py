"""synthesis.residue-common-weight-particle-hole: exact checks.

Everything is exact: integer Jordan-Wigner matrices and Fractions; no floating point.
The one-particle space C^n carries the principal sl2 as an integer triple (e, f, h);
second quantisation is X -> sum_ij X_ij c_i^dagger c_j.  Occupations q are rational
parameters standing for n(x) = 1/(e^x + 1), so no exponential is evaluated.

(i)   commutant of the principal sl2 in Mat_n is the scalars (n = 2..6), against the
      2-dimensional commutant of the partition (n-1, 1); quasi-free number-preserving
      generators commuting with the second-quantised triple form the line of N_tot
      (n = 2, 3, 4), while the full Fock commutant is larger (n = 2, 3).
(ii)  N_tot is central in A_0 = alg{E_ij}, dim A_0 = sum_k C(n,k)^2; rho_q is tracial on
      A_0 for every q tested, and <N_tot> = n q separates the states.
(iii) the sl2-invariant bilinear form exists, is nondegenerate, and is antisymmetric for even
      n (half-integer j) and symmetric for odd n (n = 2..6); eps^2 = -1 (spin 1/2), +1 (spin 1),
      so C^2 is the parity automorphism or the identity; for spin 1/2
      and spin 1 in orthonormal real bases the particle-hole map C fixes every
      second-quantised rotation generator, preserves the gl(n) relations, sends N_tot to
      n - N_tot, and rho_q o C = rho_{1-q} on a spanning set of A_0.
(iv)  the spectrum of h/2 on n = 2j + 1 is {-j, ..., j}, the weights of (Q) on a window,
      and h does not commute with e.
"""
from fractions import Fraction as F
from itertools import product
import GA
from pyutil import get_or_set
import fock
from GA import rank_of_vectors
from tp_premise import premise

PREMISES = (
    "scrambling.principality-indifference-sphere",
    "scrambling.imported-kostant-madore-partition-data",
    "scrambling.boundary-mode-space-matrix",
    "hawking.imported-quasi-free-states-car-algebra",
    "synthesis.boundary-mode-thermal-entropy",
    "synthesis.residue-from-mode-entropy",
)


def touch_premises():
    for p in PREMISES:
        premise(p)


def comb(n, k):
    # exact binomial coefficient by the multiplicative recursion over Fractions
    c = F(1)
    for i in range(k):
        c = c * (n - i) / (i + 1)
    return c


# ---------------- exact matrix kit ----------------
def zeros(r, c):
    return [[F(0)] * c for _ in range(r)]


def eye(n):
    m = zeros(n, n)
    for i in range(n):
        m[i][i] = F(1)
    return m


def mm(a, b):
    n, k, m = len(a), len(b), len(b[0])
    out = zeros(n, m)
    for i in range(n):
        for t in range(k):
            x = a[i][t]
            if x:
                bt = b[t]
                oi = out[i]
                for j in range(m):
                    if bt[j]:
                        oi[j] += x * bt[j]
    return out


def add(a, b, s=1):
    return [[a[i][j] + s * b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scal(c, a):
    return [[c * x for x in row] for row in a]


def comm(a, b):
    return add(mm(a, b), mm(b, a), -1)


def is_zero(a):
    return all(x == 0 for row in a for x in row)


def eq(a, b):
    return is_zero(add(a, b, -1))


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def T(a):
    return [list(r) for r in zip(*a)]


def flat(a):
    return [x for row in a for x in row]


def rank(rows):
    rows = [list(r) for r in rows if any(r)]
    return rank_of_vectors(rows) if rows else 0


class Echelon:
    """incremental row echelon form over Fractions: add(v) reports whether v is new."""

    def __init__(self):
        self.rows = {}          # pivot column -> normalised row (list)

    def reduce(self, v):
        v = list(v)
        for col in sorted(self.rows):
            if v[col] != 0:
                r = self.rows[col]
                f = v[col]
                v = [a - f * b for a, b in zip(v, r)]
        return v

    def add(self, v):
        v = self.reduce(v)
        piv = next((i for i, x in enumerate(v) if x != 0), None)
        if piv is None:
            return False
        pv = v[piv]
        v = [x / pv for x in v]
        for col in list(self.rows):
            r = self.rows[col]
            if r[piv] != 0:
                f = r[piv]
                self.rows[col] = [a - f * b for a, b in zip(r, v)]
        self.rows[piv] = v
        return True


def commutant_dim(gens, dim):
    cols = []
    for p in range(dim * dim):
        X = zeros(dim, dim)
        X[p // dim][p % dim] = F(1)
        img = []
        for g in gens:
            img += flat(comm(X, g))
        cols.append(img)
    return dim * dim - rank(cols)


def principal_triple(n):
    h, e, f = zeros(n, n), zeros(n, n), zeros(n, n)
    for i in range(n):
        h[i][i] = F(n - 1 - 2 * i)
    for i in range(n - 1):
        e[i][i + 1] = F((i + 1) * (n - 1 - i))
        f[i + 1][i] = F(1)
    return e, f, h


def block_triple(parts):
    n = sum(parts)
    E, Fm, H = zeros(n, n), zeros(n, n), zeros(n, n)
    off = 0
    for p in parts:
        e, f, h = principal_triple(p)
        for i in range(p):
            for j in range(p):
                E[off + i][off + j], Fm[off + i][off + j], H[off + i][off + j] = e[i][j], f[i][j], h[i][j]
        off += p
    return E, Fm, H


def triple_ok(e, f, h):
    return eq(comm(h, e), scal(2, e)) and eq(comm(h, f), scal(-2, f)) and eq(comm(e, f), h)


def jw(n):
    """Dense annihilators and creators, mode 0 the leading tensor factor (fock MSB order)."""
    cs = [fock.to_dense(fock.ann(i, n, fock.MSB), 2 ** n) for i in range(n)]
    return cs, [T(c) for c in cs]


def sq(m, cs, cd):
    dim = len(cs[0])
    out = zeros(dim, dim)
    for i in range(len(cs)):
        for j in range(len(cs)):
            if m[i][j]:
                out = add(out, scal(m[i][j], mm(cd[i], cs[j])))
    return out


def generated_algebra(gens):
    dim = len(gens[0][0])
    ech = Echelon()
    ech.add(flat(eye(dim)))
    basis = [(eye(dim), ())]
    frontier = list(basis)
    while frontier:
        new = []
        for M, w in frontier:
            for G, lab in gens:
                P = mm(M, G)
                if ech.add(flat(P)):
                    basis.append((P, w + (lab,)))
                    new.append((P, w + (lab,)))
        frontier = new
    return basis


def rho(n, q):
    dim = 2 ** n
    r = zeros(dim, dim)
    for s in range(dim):
        k = bin(s).count("1")
        r[s][s] = q ** k * (1 - q) ** (n - k)
    return r


# ---------------- checks ----------------
def check_common_weight():
    touch_premises()
    premise("scrambling.principality-indifference-sphere")
    premise("scrambling.imported-kostant-madore-partition-data")
    premise("scrambling.boundary-mode-space-matrix")
    for n in range(2, 7):
        e, f, h = principal_triple(n)
        assert triple_ok(e, f, h)
        assert commutant_dim([e, f, h], n) == 1          # one spin-0 summand: scalars
        if n >= 3:
            E, Fm, H = block_triple([n - 1, 1])
            assert triple_ok(E, Fm, H) and commutant_dim([E, Fm, H], n) == 2
    for n in (2, 3, 4):
        cs, cd = jw(n)
        dim = 2 ** n
        for i in range(n):
            for j in range(n):
                acomm = add(mm(cs[i], cd[j]), mm(cd[j], cs[i]))
                assert eq(acomm, eye(dim) if i == j else zeros(dim, dim))
        e, f, h = principal_triple(n)
        Je, Jf, Jh = (sq(m, cs, cd) for m in (e, f, h))
        assert triple_ok(Je, Jf, Jh)
        cols = []
        for p in range(n * n):
            hm = zeros(n, n)
            hm[p // n][p % n] = F(1)
            Hh = sq(hm, cs, cd)
            cols.append(flat(comm(Hh, Je)) + flat(comm(Hh, Jf)) + flat(comm(Hh, Jh)))
        assert n * n - rank(cols) == 1                  # only omega * N_tot
        if n <= 3:
            assert commutant_dim([Je, Jf, Jh], dim) == {2: 5, 3: 8}[n]   # Schur needs quasi-freeness
    return True


def check_weight_invisible_on_gauge_invariant_algebra():
    touch_premises()
    # (n, q, dim A_0, <N_tot>, <E_ii>): stated values, recomputed below
    cases = (
        (2, F(1, 2), 6, F(1), F(1, 2)),
        (2, F(1, 3), 6, F(2, 3), F(1, 3)),
        (2, F(9, 10), 6, F(9, 5), F(9, 10)),
        (3, F(1, 2), 20, F(3, 2), F(1, 2)),
        (3, F(2, 7), 20, F(6, 7), F(2, 7)),
        (4, F(1, 3), 70, F(4, 3), F(1, 3)),
    )
    built = {}
    seen = {}
    for n, q, dimA, Nexp, margexp in cases:
        if n not in built:
            cs, cd = jw(n)
            dim = 2 ** n
            E = {(i, j): mm(cd[i], cs[j]) for i in range(n) for j in range(n)}
            N = zeros(dim, dim)
            for i in range(n):
                N = add(N, E[(i, i)])
            assert all(is_zero(comm(N, E[k])) for k in E)          # N_tot central in A_0
            A0 = generated_algebra([(E[k], k) for k in E])
            assert len(A0) == sum(comb(n, k) ** 2 for k in range(n + 1))
            built[n] = (E, N, A0)
        E, N, A0 = built[n]
        assert len(A0) == dimA
        r = rho(n, q)
        assert tr(r) == 1
        # rho_q commutes with every generator E_ij, hence with A_0, so
        # tr(rho A B) = tr(B rho A) = tr(rho B A): tracial (KMS for the trivial flow) on A_0
        assert all(is_zero(comm(r, E[k])) for k in E)
        if n == 2:   # and directly, pair by pair, on the whole basis
            for (A, _), (B, _) in product(A0, A0):
                assert tr(mm(r, mm(A, B))) == tr(mm(r, mm(B, A)))
        assert tr(mm(r, N)) == Nexp == n * q
        marg = [tr(mm(r, E[(i, i)])) for i in range(n)]
        assert all(m == margexp for m in marg)
        # maximally mixed marginals (s = ln 2) exactly at q = 1/2
        assert (marg[0] == 1 - marg[0]) == (2 * q == 1)
        get_or_set(seen, n, set()).add(Nexp)
    # distinct q give distinct states on A_0, all tracial: the weight is not fixed there
    assert {n: len(v) for n, v in seen.items()} == {2: 3, 3: 2, 4: 1}
    return True


def _ph_case(n, eps, Jreal, sq_sign):
    cs, cd = jw(n)
    dim = 2 ** n
    I = eye(dim)
    E = {(i, j): mm(cd[i], cs[j]) for i in range(n) for j in range(n)}
    assert eq(mm(eps, T(eps)), eye(n))
    # C^2(psi_i) = sum_l (eps^2)_il psi_l: order 2 for integer j, parity for half-integer j
    assert eq(mm(eps, eps), scal(sq_sign, eye(n)))
    assert eq(T(eps), scal(sq_sign, eps))
    CE = {}
    for (i, j) in E:
        M = zeros(dim, dim)
        for k in range(n):
            for l in range(n):
                c = eps[i][k] * eps[j][l]
                if c:
                    M = add(M, scal(c, add(I if k == l else zeros(dim, dim), E[(l, k)], -1)))
        CE[(i, j)] = M
    for (i, j) in E:
        for (k, l) in E:
            rhs = zeros(dim, dim)
            if j == k:
                rhs = add(rhs, CE[(i, l)])
            if l == i:
                rhs = add(rhs, CE[(k, j)], -1)
            assert eq(comm(CE[(i, j)], CE[(k, l)]), rhs)
    for Ja in Jreal:
        CJ = zeros(dim, dim)
        for i in range(n):
            for j in range(n):
                if Ja[i][j]:
                    CJ = add(CJ, scal(Ja[i][j], CE[(i, j)]))
        assert eq(CJ, sq(Ja, cs, cd))
    N, CN = zeros(dim, dim), zeros(dim, dim)
    for i in range(n):
        N, CN = add(N, E[(i, i)]), add(CN, CE[(i, i)])
    assert eq(CN, add(scal(n, I), N, -1))
    A0 = generated_algebra([(E[k], k) for k in E])

    def C_word(w):
        M = I
        for lab in w:
            M = mm(M, CE[lab])
        return M
    for q in (F(1, 3), F(1, 2), F(3, 5)):
        rq, r1 = rho(n, q), rho(n, 1 - q)
        assert all(tr(mm(rq, C_word(w))) == tr(mm(r1, M)) for M, w in A0)
        inv = all(tr(mm(rq, C_word(w))) == tr(mm(rq, M)) for M, w in A0)
        assert inv == (q == F(1, 2))


def check_particle_hole():
    touch_premises()
    premise("scrambling.principality-indifference-sphere")
    premise("hawking.imported-quasi-free-states-car-algebra")
    # an invariant nondegenerate bilinear form exists for every principal triple
    for n in range(2, 7):
        e, f, h = principal_triple(n)
        cols = []
        for p in range(n * n):
            X = zeros(n, n)
            X[p // n][p % n] = F(1)
            img = []
            for g in (e, f, h):
                img += flat(add(mm(X, g), mm(T(g), X)))
            cols.append(img)
        assert n * n - rank(cols) == 1
        # build the solution: eps_{a,b} nonzero only for a + b = n - 1 (weights m, -m)
        # solve the recursion directly and test nondegeneracy and the invariance equations
        eps = zeros(n, n)
        eps[0][n - 1] = F(1)
        for a in range(1, n):
            b = n - 1 - a
            # (X e + e^T X)_{a, b+1} = 0 links eps[a][b] and eps[a-1][b+1]
            eps[a][b] = -eps[a - 1][b + 1] * e[a - 1][a] / e[b][b + 1]
        for g in (e, f, h):
            assert is_zero(add(mm(eps, g), mm(T(g), eps)))
        assert rank([list(r) for r in eps]) == n
        # symmetric for integer j (odd n), symplectic for half-integer j (even n)
        sgn = 1 if n % 2 == 1 else -1
        assert eq(T(eps), scal(sgn, eps))
    half = F(1, 2)
    Jx = [[F(0), half], [half, F(0)]]
    Ky = [[F(0), -half], [half, F(0)]]       # J_y = i K_y
    Jz = [[half, F(0)], [F(0), -half]]
    _ph_case(2, [[F(0), F(1)], [F(-1), F(0)]], [Jx, Ky, Jz], -1)

    LEVI = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}

    def levi(a, b, c):
        return F(LEVI.get((a, b, c), 0))
    L = [[[-levi(a, b, c) for c in range(3)] for b in range(3)] for a in range(3)]   # J_a = i L_a
    _ph_case(3, eye(3), L, 1)
    return True


def check_q_weights_are_a_rotation():
    touch_premises()
    premise("synthesis.residue-from-mode-entropy")
    for n in (3, 5, 7):
        e, f, h = principal_triple(n)
        j = (n - 1) // 2
        assert sorted(h[i][i] / 2 for i in range(n)) == [F(k) for k in range(-j, j + 1)]
        assert not is_zero(comm(h, e))
    return True
