"""correspondence.spin-representation: exact checks.

Model (shared Fock core below). Bivectors are GA.py elements of Cl(2,4)_C, with Lie bracket the
commutator product A x B = (AB - BA)/2 and vector action B . x = (Bx - xB)/2; the spinor action is
rho(B) = c(B)/2 restricted to CS (t-basis, 4x4 over Q(i)).
(a) The 15 basis bivectors e_a e_b close: every A x B is a pure bivector (grade 2), also for complex
    combinations; [rho(B), c(x)] = c(B . x) with B . x a vector, for all 15 bivectors and 6 vectors.
(b) rho is a Lie homomorphism on CS: rho(A x B) = [rho(A), rho(B)] for all 225 ordered pairs; every rho(B)
    is traceless, and the 15 images are linearly independent: rho is an isomorphism onto sl(CS) (dim 15).
(c) Spin elements: products u v of two vectors with Q(u) Q(v) = 1 (real and complex samples) act on CS
    with determinant 1, inside SL(CS); and at sample spinors u (basis vectors, generic, a null-plane
    vector) the tangent space {rho(B) u} is all of CS (rank 4), so the SL(CS) = image-of-Spin orbit of every
    nonzero spinor is open in the connected space CS \\ 0, i.e. the action is transitive.
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

BIV = [(a, b) for a in range(6) for b in range(a + 1, 6)]


def biv(a, b):
    return gmul(E[a], E[b])


def grade_set(x):
    return {len(b) for b in x}


def det4(M):
    A = [row[:] for row in M]
    n, d = len(A), ONE
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c]), None)
        if p is None:
            return Z0
        if p != c:
            A[c], A[p] = A[p], A[c]
            d = -d
        d = d * A[c][c]
        for r in range(c + 1, n):
            if A[r][c]:
                f = A[r][c] / A[c][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return d


def lie(A, B):
    return gscal(F(1, 2), GA.sub(GA.mul(A, B, SQ), GA.mul(B, A, SQ)))


# sample complex bivectors whose commutator is checked to be a nonzero bivector
BC_SAMPLE = GA.add(biv(0, 3), gscal(QI(0, 2), biv(1, 5)), gscal(3, biv(2, 4)))
DC_SAMPLE = GA.add(gscal(QI(1, 1), biv(0, 1)), biv(3, 4))


def check_bivectors_close_and_act_on_vectors():
    for (a, b) in BIV:
        for (c, d) in BIV:
            assert grade_set(lie(biv(a, b), biv(c, d))) <= {2}
        B = biv(a, b)
        for k in range(len(E)):
            x = vact(B, E[k])
            assert grade_set(x) <= {1}
            lhs = mcomm(rho(B), CB[k])
            assert lhs == rep(x)
    assert grade_set(lie(BC_SAMPLE, DC_SAMPLE)) == {2}
    # e0 e2 acting on e0 gives e2 . e0-component: (e0e2) . e0 = -e2 (e0^2 = 1)
    assert vact(biv(0, 2), E[0]) == gscal(-1, E[2])
    return True


def check_rho_is_isomorphism_onto_sl():
    blocks = {p: cs_block(rho(biv(*p))) for p in BIV}
    for p in BIV:
        assert sum((blocks[p][i][i] for i in range(4)), Z0) == Z0
    assert GA.field_rank([[v for row in blocks[p] for v in row] for p in BIV]) == 15
    for p in BIV:
        for r in BIV:
            lhs = cs_block(rho(lie(biv(*p), biv(*r))))
            assert lhs == mcomm(blocks[p], blocks[r])
    return True


def check_spin_image_in_sl_and_transitive():
    pairs = [(E[0], E[1]), (E[2], E[3]), (gvec([5, 0, 0, 0, 0, 0]), gvec([F(1, 5), 0, 0, 0, 0, 0])),
             (gvec([F(5, 3), 0, F(4, 3), 0, 0, 0]), E[1]), (E[4], gvec([0, 0, 0, 0, 0, 1])),
             (gvec([0, 0, 0, 0, F(5, 4), QI(0, F(3, 4))]), E[2])]
    for (u, v) in pairs:
        assert gip(u, u) * gip(v, v) == ONE
        g = cs_block(mmul(rep(u), rep(v)))
        assert det4(g) == ONE
    # a vector pair with Q(u)Q(v) = 4 scales the determinant to 16 = 4^2
    assert det4(cs_block(mmul(rep(gscal(2, E[0])), rep(E[1])))) == QI(16)
    us = [[1, 0, 0, 0], [0, 0, 0, 1], [1, QI(0, 2), -1, 3], [0, 0, 1, QI(1, 1)]]
    blocks = [cs_block(rho(biv(*p))) for p in BIV]
    for u in us:
        uu = [q(x) for x in u]
        tang = [[sum((B[i][j] * uu[j] for j in range(4)), Z0) for i in range(4)] for B in blocks]
        assert GA.field_rank(tang) == 4
    return True
