"""correspondence.chevalley-pairing: exact checks.

Model (shared Fock core below): Lambda W with its monomial basis (the paper's), the operators c(v) of
Cl(2,4)_C, exact over Q(i). B(x, y) = top(alpha(x) ^ y) is computed from the definition: alpha reverses a
monomial of degree k by (-1)^(k(k-1)/2), and the wedge sign is the sign of the merged index sequence.
(1) B vanishes on CS x CS and CS- x CS- (all 32 monomial pairs each) and is perfect on CS- x CS (rank 4);
    the degree count (deg x + deg y = 3 for a nonzero value) is what forces it.
(2) B(y, x) = -B(x, y) on all 64 monomial pairs and on complex sample vectors.
(3) B(c(v) x, y) = B(x, c(v) y) for the six basis vectors (all 64 pairs) and complex sample vectors.
(4) For every orthogonal pair of basis vectors (15 pairs) and for orthogonal complex samples (isotropic
    w0, w1; mixed vectors), beta = (1/2) c(u) c(v) satisfies B(beta x, y) + B(x, beta y) = 0; for a
    non-orthogonal pair the same expression fails, so orthogonality is used.
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

SAMPLES = [[1, QI(0, 2), 0, -1, 3, 0, QI(1, 1), 2], [0, 1, QI(-1, 1), 2, 0, QI(0, 3), 1, -1],
           [QI(2, -1), 0, 1, 0, 1, 1, 0, QI(0, 1)]]


def check_vanishing_and_perfect_on_chiralities():
    for S in EVEN:
        for T in EVEN:
            assert bpair(e8(S), e8(T)) == Z0
    for S in ODD:
        for T in ODD:
            assert bpair(e8(S), e8(T)) == Z0
    M = [[bpair(e8(S), e8(T)) for T in EVEN] for S in ODD]
    assert GA.field_rank(M) == 4
    nz = [(S, T) for S in MASKS for T in MASKS if bpair(e8(S), e8(T))]
    assert len(nz) == 8 and all(bin(S).count("1") + bin(T).count("1") == 3 for S, T in nz)
    # sample value: B(1, w0 w1 w2) = 1 and B(w0 w1 w2, 1) = alpha(w0w1w2) = -1
    assert bpair(e8(0), e8(7)) == ONE and bpair(e8(7), e8(0)) == QI(-1)
    return True


def check_antisymmetry():
    for S in MASKS:
        for T in MASKS:
            assert bpair(e8(S), e8(T)) == -bpair(e8(T), e8(S))
    xs = [[q(v) for v in s] for s in SAMPLES]
    for x in xs:
        for y in xs:
            assert bpair(x, y) == -bpair(y, x)
    # by hand: B(w1 w2, w0) = top(alpha(w1 w2) ^ w0) = -w1 w2 w0 = -w0 w1 w2, and B(w0, w1 w2) = +1
    assert bpair(e8(6), e8(1)) == QI(-1) and bpair(e8(1), e8(6)) == ONE
    return True


def check_vectors_self_transpose():
    vecs = [E[k] for k in range(6)] + [gvec([1, QI(0, 1), 2, 0, -1, 3]), W[2], WP[0]]
    for v in vecs:
        Cv = rep(v)
        for S in MASKS:
            for T in MASKS:
                assert bpair(apply(Cv, e8(S)), e8(T)) == bpair(e8(S), apply(Cv, e8(T)))
        xs = [[q(t) for t in s] for s in SAMPLES]
        assert bpair(apply(Cv, xs[0]), xs[1]) == bpair(xs[0], apply(Cv, xs[1]))
    # by hand: c(e0) w1 w2 = w0 w1 w2, so B(c(e0) w1 w2, 1) = alpha(w0 w1 w2) = -1 = B(w1 w2, c(e0) 1)
    assert bpair(apply(CB[0], e8(6)), e8(0)) == QI(-1) == bpair(e8(6), apply(CB[0], e8(0)))
    return True


# sample inputs for (4): orthogonal complex pairs (isotropic and mixed), and a non-orthogonal pair
ORTH_SAMPLE_PAIRS = [(W[0], W[1]), (W[1], WP[2]),
                     (gvec([1, 1, 0, 0, 0, 0]), gvec([0, 0, 1, 1, 0, 0])),
                     (gvec([2, 0, 1, 0, QI(0, 1), 0]), gvec([0, 3, 0, 1, 0, 2]))]
NON_ORTHOGONAL_PAIR = (E[0], E[0])


def check_bivectors_infinitesimally_invariant():
    n = len(E)
    pairs = [(E[a], E[b]) for a in range(n) for b in range(a + 1, n)]
    assert len(pairs) == 15                     # the basis bivectors, which span so(2,4)
    for (u, v) in pairs + ORTH_SAMPLE_PAIRS:
        assert gip(u, v) == Z0
        beta = mscal(F(1, 2), mmul(rep(u), rep(v)))
        # beta_uv is the spin generator of the rotation in the u-v plane:
        # [beta_uv, c(w)] = <v, w> c(u) - <u, w> c(v)
        for w in E:
            rhs = madd(mscal(gip(v, w), rep(u)), mscal(-gip(u, w), rep(v)))
            assert mcomm(beta, rep(w)) == rhs
        for S in MASKS:
            for T in MASKS:
                assert bpair(apply(beta, e8(S)), e8(T)) + bpair(e8(S), apply(beta, e8(T))) == Z0
    # without orthogonality the identity fails: for u = v = e0, c(u)c(v) = 1 and B + B = 2B
    u, v = NON_ORTHOGONAL_PAIR
    assert gip(u, v) != Z0
    beta = mmul(rep(u), rep(v))
    assert any(bpair(apply(beta, e8(S)), e8(T)) + bpair(e8(S), apply(beta, e8(T))) != Z0
               for S in MASKS for T in MASKS)
    return True
