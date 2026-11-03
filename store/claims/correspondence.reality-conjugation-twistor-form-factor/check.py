"""correspondence.reality-conjugation-twistor-form-factor: exact checks.

Model (shared Fock core below): the Fock model of correspondence.fock-model-complexified-ascended-algebra,
the Chevalley pairing B of correspondence.chevalley-pairing, and the chart of
correspondence.incidence-relation-chart (n0 = w0, ninf = 2 w'0, bases pi1 = -t2, pi2 = t3 of S_pi and
e1 = t0, e2 = 2 t1 of S_omega). The real points of V_C are the real combinations of e0..e5; b4, the fourth
negative basis vector, is e5 (the only generator whose operator is imaginary). J conjugates monomial
coefficients, so an antilinear map is x -> K conj(x) for a matrix K.
(1) kappa = Gamma c(e5) J satisfies kappa c(v) = c(vbar) kappa for the six basis vectors and their
    i-multiples on every basis state; the matrices K with K conj(c(e_k)) = c(e_k) K for all k form a computed
    one-dimensional space, spanned by Gamma c(e5) (uniqueness up to a complex multiple); kappa maps CS to
    CS-; K conj(K) = -1, i.e. kappa^2 = -id.
(2) Sigma(Z1, Z2) = B(kappa Z1, Z2) on CS has rank 4 and is Hermitian (lambda = 1); with kappa rescaled by
    the phase (3 + 4i)/5 the relation Sigma(Z2, Z1) = lambda conj Sigma(Z1, Z2) holds with lambda = (-7 + 24i)/25,
    of modulus one (and the conjugate relation fails); the 15 real bivectors act anti-Hermitianly,
    rho^dagger H + H rho = 0.
(3) For eight real null vectors the plane of psi(v) = ker c(v) on CS is Sigma-null; so are S_omega and S_pi.
(4) The real form [[Re H, -Im H], [Im H, Re H]] has signature (4, 4, 0): Sigma has signature (2, 2).
(5) I6 acts on CS as a scalar square root of -1. Over the reals, three 4-dimensional subspaces of
    Hom(S_pi, S_omega) = C^4 = R^8 coincide: (b) the A with Sigma-null graph (a real-linear condition, its
    kernel computed), (c) {I6 xhat : xhat sigma-Hermitian} (kernel computed), and (a) {A : m(A) real}, which is
    the real span of A_x = (1/2) c(ninf) c(x) for real x in W_{1,3} (m(A_x) = -x real). On real points
    Q(m) = -2 det A = 2 det xhat.
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

N0V, NIV = W[0], gscal(2, WP[0])
PI1, PI2 = [Z0, Z0, QI(-1), Z0], [Z0, Z0, Z0, ONE]
E1, E2 = [ONE, Z0, Z0, Z0], [Z0, QI(2), Z0, Z0]
GAMMA = [[QI(1 if bin(r).count("1") % 2 == 0 else -1) if r == c else Z0 for c in range(8)] for r in range(8)]
KMAT = mmul(GAMMA, CB[5])
REALNULL = [[1, 0, 1, 0, 0, 0], [0, 1, 0, 0, 1, 0], [1, 0, 0, 0, 0, -1], [3, 4, 0, 0, 0, 5],
            [1, 1, 1, 1, 0, 0], [2, 1, 0, 2, 1, 0], [1, 0, 0, F(3, 5), F(4, 5), 0], [0, 1, 0, 1, 0, 0]]


def conjv(x):
    return [v.conj() for v in x]


def conjm(M):
    return [[v.conj() for v in row] for row in M]


def kappa(x, K=KMAT):
    return apply(K, conjv(x))


def vbar(v):
    return {b: q(c).conj() for b, c in v.items()}


def sigma_matrix(K=KMAT):
    return [[bpair(kappa(TB[i], K), TB[j]) for j in range(4)] for i in range(4)]


def sig(Hm, z1, z2):
    return sum((z1[i].conj() * Hm[i][j] * z2[j] for i in range(4) for j in range(4)), Z0)


def check_conjugation_intertwines_and_is_unique():
    premise("correspondence.fock-model-complexified-ascended-algebra")
    for k in range(6):
        for v in (E[k], gscal(IU, E[k])):
            for S in MASKS:
                assert kappa(apply(rep(v), e8(S))) == apply(rep(vbar(v)), kappa(e8(S)))
    # uniqueness: K conj(c(e_k)) = c(e_k) K, 64 unknowns
    rows = []
    for k in range(6):
        Cb, C = conjm(CB[k]), CB[k]
        for r in range(8):
            for c in range(8):
                row = [Z0] * 64
                for t in range(8):
                    row[r * 8 + t] = row[r * 8 + t] + Cb[t][c]
                    row[t * 8 + c] = row[t * 8 + c] - C[r][t]
                rows.append(row)
    ker = kernel(rows)
    assert len(ker) == 1
    assert GA.field_rank([ker[0], [v for row in KMAT for v in row]]) == 1
    for S in EVEN:
        assert all(not kappa(e8(S))[T] for T in EVEN)
    assert mmul(KMAT, conjm(KMAT)) == mscal(-1, ident())
    return True


def check_twistor_form_hermitian_invariant():
    premise("correspondence.chevalley-pairing")
    Hm = sigma_matrix()
    assert GA.field_rank(Hm) == 4
    assert all(Hm[j][i] == Hm[i][j].conj() for i in range(4) for j in range(4))
    ph = QI(F(3, 5), F(4, 5))
    H2 = sigma_matrix(mscal(ph, KMAT))
    lam = QI(F(-7, 25), F(24, 25))
    assert lam * lam.conj() == ONE
    assert all(H2[j][i] == lam * H2[i][j].conj() for i in range(4) for j in range(4))
    assert not all(H2[j][i] == lam.conj() * H2[i][j].conj() for i in range(4) for j in range(4))
    for a in range(6):
        for b in range(a + 1, 6):
            R = cs_block(rho(gmul(E[a], E[b])))
            Rd = [[R[j][i].conj() for j in range(4)] for i in range(4)]
            assert mzero(madd(mmul(Rd, Hm), mmul(Hm, R)))
    return True


def check_null_planes_and_signature():
    premise("correspondence.chevalley-pairing")
    Hm = sigma_matrix()
    for cs in REALNULL:
        v = gvec(cs)
        assert gip(v, v) == Z0
        pl = cs_kernel(v)
        assert len(pl) == 2 and all(sig(Hm, a, b) == Z0 for a in pl for b in pl)
    for pl in ([E1, E2], [PI1, PI2]):
        assert all(sig(Hm, a, b) == Z0 for a in pl for b in pl)
    re = [[Hm[i][j].re for j in range(4)] for i in range(4)]
    im = [[Hm[i][j].im for j in range(4)] for i in range(4)]
    real8 = [re[i] + [-x for x in im[i]] for i in range(4)] + [im[i] + re[i] for i in range(4)]
    assert tuple(GA.congruence_signature(real8)[:3]) == (4, 4, 0)
    return True


def r8(A):
    """A (2x2 over Q(i)) as a real 8-vector."""
    return [A[i][j].re for i in range(2) for j in range(2)] + [A[i][j].im for i in range(2) for j in range(2)]


def from_r8(v):
    return [[QI(v[2 * i + j], v[4 + 2 * i + j]) for j in range(2)] for i in range(2)]


def img(A, j):
    return [A[0][j] * E1[k] + A[1][j] * E2[k] for k in range(4)]


def same_real_span(xs, ys):
    r = GA.rank_of_vectors(xs)
    return r == GA.rank_of_vectors(ys) == GA.rank_of_vectors(xs + ys)


def check_real_chart_three_ways():
    premise("correspondence.incidence-relation-chart")
    premise("correspondence.chevalley-pairing")
    Hm = sigma_matrix()
    I6m = cs_block(rep(gmul(*E)))
    assert I6m == mscal(QI(0, -1), ident(4))
    basis8 = [[F(1) if i == k else F(0) for i in range(8)] for k in range(8)]
    # (b) Sigma-null graph: linear in A since S_pi and S_omega are Sigma-null
    cols = []
    for bv in basis8:
        A = from_r8(bv)
        g = [[PI1[k] + img(A, 0)[k] for k in range(4)], [PI2[k] + img(A, 1)[k] for k in range(4)]]
        vals = [sig(Hm, g[a], g[b]) for a in range(2) for b in range(2)]
        cols.append([v.re for v in vals] + [v.im for v in vals])
    kb = GA.field_kernel([[cols[c][r] for c in range(8)] for r in range(8)])
    assert len(kb) == 4
    # (c) I6 xhat with xhat sigma-Hermitian: sigma(xhat pi, pi') = conj sigma(xhat pi', pi)
    cols = []
    for bv in basis8:
        X = from_r8(bv)
        vals = []
        for a, pa in enumerate((PI1, PI2)):
            for b, pb in enumerate((PI1, PI2)):
                vals.append(sig(Hm, img(X, a), pb) - sig(Hm, img(X, b), pa).conj())
        cols.append([v.re for v in vals] + [v.im for v in vals])
    kc = GA.field_kernel([[cols[c][r] for c in range(8)] for r in range(8)])
    assert len(kc) == 4
    kc_A = [r8([[QI(0, -1) * x for x in row] for row in from_r8(v)]) for v in kc]
    # (a) real chart points: A_x for real x in W_{1,3}
    ka = []
    for k in (1, 3, 4, 5):
        Ax = cs_block(mscal(F(1, 2), mmul(rep(NIV), rep(E[k]))))
        A = []
        for p in (PI1, PI2):
            y = [sum((Ax[i][j] * p[j] for j in range(4)), Z0) for i in range(4)]
            A.append([y[0], y[1] / QI(2)])
        A = [[A[0][0], A[1][0]], [A[0][1], A[1][1]]]
        m = psi_inv(madd(wedge4(img(A, 0), PI2), wedge4(PI1, img(A, 1))))
        assert m == gscal(-1, E[k])
        ka.append(r8(A))
    assert same_real_span(kb, kc_A) and same_real_span(kb, ka)
    # chart norm on real points: Q(m) = -2 det A = 2 det xhat
    for v in kc:
        X = from_r8(v)
        A = [[QI(0, -1) * x for x in row] for row in X]
        m = psi_inv(madd(wedge4(img(A, 0), PI2), wedge4(PI1, img(A, 1))))
        dA = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        dX = X[0][0] * X[1][1] - X[0][1] * X[1][0]
        assert gip(m, m) == QI(-2) * dA == QI(2) * dX
        assert all(c.im == 0 for c in m.values())
    return True
