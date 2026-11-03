"""correspondence.fock-model-complexified-ascended-algebra: exact checks.

Model (shared Fock core below): Cl(2,4)_C acts on Lambda W = C^8 through c(e_k) = CB[k], exact over
Q(i); GA.py supplies the vectors (complex coefficients allowed) and their products.
(1) W = span(w_k) and W' = span(w'_k) are totally isotropic, of dimension 3 (maximal in dimension 6),
    dual under the bilinear form (<w_j, w'_k> = delta_jk/2 here, delta_jk for the paper's sqrt2-scaled
    basis); c(w_k) is the wedge and c(w'_k) the contraction on the monomial basis; c(u)^2 = Q(u) id on all
    36 basis pairs (anticommutators) and at complex sample vectors, so c extends to Cl(V_C).
(2) The 64 ordered blade products are linearly independent in End(C^8) (rank 64): Cl(V_C) = End(Lambda W),
    hence Lambda W is irreducible (and, Mat_8(C) being simple, its unique irreducible module).
(3) Every vector maps CS = Lambda^even to CS- = Lambda^odd and back; each half has dimension 4; the 32 even
    blades act block-diagonally and their restrictions have rank 16 on each half and 32 jointly:
    Cl^0(2,4)_C = End(CS) + End(CS-).
(4) A second dual pair of maximal isotropic subspaces (the annihilator W_u of a sample spinor and its
    dual complement, built as in T09) is the image of (W, W') under a linear map preserving the form,
    an element of O(V_C): the pairs are conjugate (two even and one odd sample spinor).
"""
from fractions import Fraction as F
from itertools import permutations

import GA
from tp_premise import premise

# ---------------------------------------------------------------------------
# Fock model of Cl(2,4)_C on Lambda W (exact over Q(i)).  GA.py generators e0, e1 (square +1),
# e2, e3, e4, e5 (square -1).  Isotropic pairs: mode 0 from (e0, e2), mode 1 from (e1, e3), mode 2
# from (e4, e5): w_k = (e_a + e_b)/2, w'_k = (e_a - e_b)/2 for k = 0, 1 and w_2 = (e4 + i e5)/2,
# w'_2 = (-e4 + i e5)/2, so <w_j, w'_k> = delta_jk / 2.  The paper's isotropic basis (pairing
# delta_jk) is sqrt2 times these, and the Fock basis |S> (S a subset of the modes) is its monomial
# basis; on it c(w_k) acts as the paper's wedge and c(w'_k) as its contraction, so the paper's
# c(w) = sqrt2 w ^ and c(w') = sqrt2 iota_w' hold exactly while c(e_k)^2 = Q(e_k).
# ---------------------------------------------------------------------------
QI = GA.QI
Z0, ONE, IU = QI(0), QI(1), QI(0, 1)
SQ = GA.sig(2, 4)
MASKS = list(range(8))
EVEN = [m for m in MASKS if bin(m).count("1") % 2 == 0]
ODD = [m for m in MASKS if bin(m).count("1") % 2 == 1]


def q(x):
    return x if isinstance(x, QI) else QI(x)


def zmat(r=8, c=8):
    return [[Z0] * c for _ in range(r)]


def ident(n=8):
    return [[ONE if i == j else Z0 for j in range(n)] for i in range(n)]


def madd(*Ms):
    return [[sum((M[i][j] for M in Ms), Z0) for j in range(len(Ms[0][0]))] for i in range(len(Ms[0]))]


def mscal(c, M):
    c = q(c)
    return [[c * v for v in row] for row in M]


def mmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B)) if A[i][k] and B[k][j]), Z0)
             for j in range(len(B[0]))] for i in range(len(A))]


def mcomm(A, B):
    return madd(mmul(A, B), mscal(-1, mmul(B, A)))


def mzero(M):
    return all(not v for row in M for v in row)


def apply(M, u):
    return [sum((M[r][c] * u[c] for c in range(len(u)) if M[r][c] and u[c]), Z0) for r in range(len(M))]


def _sign_below(m, i):
    return -1 if bin(m & ((1 << i) - 1)).count("1") % 2 else 1


def wedge_op(i):
    M = zmat()
    for m in MASKS:
        if not (m >> i) & 1:
            M[m | (1 << i)][m] = QI(_sign_below(m, i))
    return M


def contract_op(i):
    M = zmat()
    for m in MASKS:
        if (m >> i) & 1:
            M[m & ~(1 << i)][m] = QI(_sign_below(m, i))
    return M


AW = [wedge_op(i) for i in range(3)]
BW = [contract_op(i) for i in range(3)]
CB = [madd(AW[0], BW[0]), madd(AW[1], BW[1]), madd(AW[0], mscal(-1, BW[0])),
      madd(AW[1], mscal(-1, BW[1])), madd(AW[2], mscal(-1, BW[2])), mscal(QI(0, -1), madd(AW[2], BW[2]))]
E = [GA.gen(k) for k in range(6)]


def gscal(c, x):
    """Scale a GA element by a (possibly complex) scalar."""
    c = q(c)
    return {b: c * v for b, v in x.items() if c * v}


def gvec(cs):
    """GA vector with coefficients cs (QI or rational) on e0..e5."""
    out = {}
    for k in range(6):
        if q(cs[k]):
            out[(k,)] = q(cs[k])
    return out


def gmul(*xs):
    r = {(): ONE}
    for x in xs:
        r = GA.mul(r, x, SQ)
    return r


def gwedge(a, b):
    """Outer product of two vectors, (ab - ba)/2."""
    return gscal(F(1, 2), GA.sub(GA.mul(a, b, SQ), GA.mul(b, a, SQ)))


def gip(a, b):
    """Complex-bilinear inner product of two vectors."""
    return q(GA.dot(a, b, SQ))


_BLADE_CACHE = {}


def rep_blade(b):
    if b not in _BLADE_CACHE:
        M = ident()
        for k in b:
            M = mmul(M, CB[k])
        _BLADE_CACHE[b] = M
    return _BLADE_CACHE[b]


def rep(x):
    """The operator of a GA multivector (complex coefficients allowed)."""
    M = zmat()
    for b, v in x.items():
        M = madd(M, mscal(v, rep_blade(b)))
    return M


def rho(B):
    """Spinor action of a GA bivector B: rho(B) = B/2, so [rho(B), c(x)] = c(B . x)."""
    return mscal(F(1, 2), rep(B))


def vact(B, x):
    """Vector action of a GA bivector: B . x = (Bx - xB)/2."""
    return gscal(F(1, 2), GA.sub(GA.mul(B, x, SQ), GA.mul(x, B, SQ)))


W = [gscal(F(1, 2), GA.add(E[0], E[2])), gscal(F(1, 2), GA.add(E[1], E[3])),
     gscal(F(1, 2), GA.add(E[4], gscal(IU, E[5])))]
WP = [gscal(F(1, 2), GA.sub(E[0], E[2])), gscal(F(1, 2), GA.sub(E[1], E[3])),
      gscal(F(1, 2), GA.add(gscal(-1, E[4]), gscal(IU, E[5])))]


def e8(m):
    return [ONE if i == m else Z0 for i in range(8)]


def lin(*terms):
    """Linear combination sum c_i v_i of 8-vectors (or 4-vectors)."""
    n = len(terms[0][1])
    return [sum((q(c) * v[i] for c, v in terms), Z0) for i in range(n)]


def kernel(rows):
    return GA.field_kernel(rows) if rows else []


def solve_inv(M):
    n = len(M)
    cols = [GA.field_solve([r[:] for r in M], [ONE if r == j else Z0 for r in range(n)]) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


# the Chevalley pairing B(x, y) = top(alpha(x) ^ y) on the monomial basis
_REV = {0: 1, 1: 1, 2: -1, 3: -1}


def _wsign(S, T):
    vals = [x for x in range(3) if (S >> x) & 1] + [x for x in range(3) if (T >> x) & 1]
    inv = sum(1 for i in range(len(vals)) for j in range(i + 1, len(vals)) if vals[i] > vals[j])
    return -1 if inv % 2 else 1


def b_mono(S, T):
    if (S | T) != 7 or (S & T):
        return 0
    return _REV[bin(S).count("1")] * _wsign(S, T)


def bpair(x, y):
    return sum((x[S] * y[T] * b_mono(S, T) for S in MASKS for T in MASKS
                if x[S] and y[T] and b_mono(S, T)), Z0)


# bases of CS = Lambda^even W (t0 = 1, t1 = w1 w2, t2 = w2 w0, t3 = w0 w1) and CS- = Lambda^odd W
TB = [e8(0), e8(6), lin((-1, e8(5))), e8(3)]
SB = [e8(1), e8(2), e8(4), e8(7)]


def cs_coords(x):
    """Coordinates of an even 8-vector in the t-basis."""
    return [x[0], x[6], -x[5], x[3]]


def cs_vec(c):
    return lin(*[(c[k], TB[k]) for k in range(4)])


def cs_block(M):
    """The 4x4 matrix of an even operator restricted to CS, in the t-basis."""
    cols = [cs_coords(apply(M, TB[j])) for j in range(4)]
    return [[cols[j][i] for j in range(4)] for i in range(4)]


BST = [[bpair(SB[i], TB[j]) for j in range(4)] for i in range(4)]
BINV = solve_inv(BST)


def psi(v):
    """The spinor identification V_C -> Lambda^2 CS: the antisymmetric coefficient matrix P (P = sum
    P_kl t_k (x) t_l, t_k ^ t_l = t_k (x) t_l - t_l (x) t_k counted once) of the form
    (s, s') -> B(s, c(v) s') on CS-, transported to CS through the pairing B: CS- x CS -> C."""
    Cv = rep(v)
    G = [[bpair(SB[i], apply(Cv, SB[j])) for j in range(4)] for i in range(4)]
    return [[sum((BINV[k][i] * G[i][j] * BINV[l][j] for i in range(4) for j in range(4)), Z0)
             for l in range(4)] for k in range(4)]


def eps0(P, Qm):
    """eps0(P ^ Q) for antisymmetric coefficient matrices in the t-basis (t0 t1 t2 t3 -> 1)."""
    out = Z0
    for perm in permutations(range(4)):
        inv = sum(1 for i in range(4) for j in range(i + 1, 4) if perm[i] > perm[j])
        out = out + QI(-1 if inv % 2 else 1) * P[perm[0]][perm[1]] * Qm[perm[2]][perm[3]]
    return out / QI(4)


def wedge4(u, v):
    return [[u[k] * v[l] - u[l] * v[k] for l in range(4)] for k in range(4)]


def pfaff(P):
    return P[0][1] * P[2][3] - P[0][2] * P[1][3] + P[0][3] * P[1][2]


def flat6(P):
    return [P[0][1], P[0][2], P[0][3], P[1][2], P[1][3], P[2][3]]


PSI_E = [psi(E[k]) for k in range(6)]
_PSIT = [[flat6(PSI_E[k])[c] for k in range(6)] for c in range(6)]


def psi_inv(P):
    """The vector v (as coefficients on e0..e5) with psi(v) = P."""
    return gvec(GA.field_solve([r[:] for r in _PSIT], flat6(P)))


def plane(P):
    """Basis (t-coordinates) of the image of an antisymmetric matrix: its plane when simple."""
    cols = [[P[i][j] for i in range(4)] for j in range(4)]
    out = []
    for c in cols:
        if GA.field_rank(out + [c]) > len(out):
            out.append(c)
    return out


def cs_kernel(v):
    """Basis (t-coordinates) of {u in CS : c(v) u = 0}."""
    Cv = rep(v)
    cols = [apply(Cv, TB[j]) for j in range(4)]
    return kernel([[cols[j][r] for j in range(4)] for r in range(8)])


def same_span(xs, ys):
    r = GA.field_rank(xs) if xs else 0
    return r == (GA.field_rank(ys) if ys else 0) == (GA.field_rank(xs + ys) if xs + ys else 0)

# sample inputs: generic complex vectors, and the null vector e0 + e2 = 2 w_0
NULL_SAMPLE = gvec([1, 0, 1, 0, 0, 0])
VECTOR_SAMPLES = [gvec([1, 2, 0, -1, 3, QI(0, 1)]), gvec([QI(1, 1), 0, QI(2, -1), 1, 0, 5]),
                  NULL_SAMPLE]


def check_isotropic_pair_and_clifford_relations():
    for j in range(3):
        for k in range(3):
            assert gip(W[j], W[k]) == Z0 and gip(WP[j], WP[k]) == Z0
            assert gip(W[j], WP[k]) == (QI(F(1, 2)) if j == k else Z0)
    rows = [[w.get((k,), Z0) for k in range(len(E))] for w in W + WP]
    assert GA.field_rank(rows[:3]) == 3 and GA.field_rank(rows) == 6
    for k in range(3):
        assert rep(W[k]) == wedge_op(k) and rep(WP[k]) == contract_op(k)
    for a in range(len(CB)):
        for b in range(len(CB)):
            ac = madd(mmul(CB[a], CB[b]), mmul(CB[b], CB[a]))
            assert ac == mscal(2 * SQ[a] if a == b else 0, ident())
    for u in VECTOR_SAMPLES:
        assert mmul(rep(u), rep(u)) == mscal(gip(u, u), ident())
    # the null sample squares to zero
    assert gip(NULL_SAMPLE, NULL_SAMPLE) == Z0 and mzero(mmul(rep(NULL_SAMPLE), rep(NULL_SAMPLE)))
    return True


def check_blade_products_span_all_endomorphisms():
    blades = GA.all_blades(6)
    assert len(blades) == 64
    rows = [[v for row in rep_blade(b) for v in row] for b in blades]
    assert GA.field_rank(rows) == 64
    # the representation is multiplicative on sample blade pairs (it is built from the generators)
    for b1 in blades[::7]:
        for b2 in blades[::9]:
            prod = GA.mul({b1: ONE}, {b2: ONE}, SQ)
            assert rep(prod) == mmul(rep_blade(b1), rep_blade(b2))
    return True


def check_chirality_halves_and_even_subalgebra():
    assert len(EVEN) == 4 and len(ODD) == 4
    for k in range(6):
        for r in MASKS:
            for c in MASKS:
                if (r in EVEN) == (c in EVEN):
                    assert not CB[k][r][c]
    even = [b for b in GA.all_blades(6) if len(b) % 2 == 0]
    assert len(even) == 32
    on_cs, on_csm, both = [], [], []
    for b in even:
        M = rep_blade(b)
        assert all(not M[r][c] for r in EVEN for c in ODD) and all(not M[r][c] for r in ODD for c in EVEN)
        on_cs.append([M[r][c] for r in EVEN for c in EVEN])
        on_csm.append([M[r][c] for r in ODD for c in ODD])
        both.append(on_cs[-1] + on_csm[-1])
    assert GA.field_rank(on_cs) == 16 and GA.field_rank(on_csm) == 16 and GA.field_rank(both) == 32
    return True


def annihilator(u):
    cols = [apply(CB[k], u) for k in range(6)]
    return kernel([[cols[k][r] for k in range(6)] for r in range(8)])


# sample inputs: pure spinors (Fock vectors with a three-dimensional annihilator)
PURE_SAMPLES = [lin((1, e8(0)), (2, e8(6)), (QI(0, 1), e8(5)), (QI(1, -1), e8(3))),
                lin((3, e8(0)), (QI(0, -2), e8(3))),
                lin((1, e8(1)), (QI(0, 1), e8(2)), (3, e8(7)))]


def check_dual_pairs_conjugate_under_orthogonal_group():
    n = len(E)
    for u in PURE_SAMPLES:
        Wu = [gvec(v) for v in annihilator(u)]
        assert len(Wu) == 3
        assert all(gip(x, y) == Z0 for x in Wu for y in Wu)
        # dual complement: v_j with <w_i, v_j> = delta_ij / 2, then made isotropic
        Vs = []
        for j in range(len(Wu)):
            M = [[gip(Wu[i], E[c]) for c in range(n)] + [QI(F(-1, 2)) if i == j else Z0]
                 for i in range(len(Wu))]
            sol = next(s for s in kernel(M) if s[n])
            Vs.append(gvec([s_ / sol[n] for s_ in sol[:n]]))
        Us = [GA.sub(Vs[j], GA.add(*[gscal(gip(Vs[j], Vs[k]), Wu[k]) for k in range(len(Wu))]))
              for j in range(len(Wu))]
        new, old = Wu + Us, W + WP
        for a in range(n):
            for b in range(n):
                assert gip(new[a], new[b]) == gip(old[a], old[b])
        # the linear map old -> new, written on e0..e5, preserves the form: T^t G T = G
        Mold = [[old[j].get((k,), Z0) for j in range(6)] for k in range(6)]
        Mnew = [[new[j].get((k,), Z0) for j in range(6)] for k in range(6)]
        T = mmul(Mnew, solve_inv(Mold))
        G = [[QI(SQ[i]) if i == j else Z0 for j in range(6)] for i in range(6)]
        Tt = [[T[j][i] for j in range(6)] for i in range(6)]
        assert mmul(mmul(Tt, G), T) == G
        assert all(not x for w in Wu for x in apply(rep(w), u))
    return True
