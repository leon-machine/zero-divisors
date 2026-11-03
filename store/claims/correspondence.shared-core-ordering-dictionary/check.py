"""correspondence.shared-core-ordering-dictionary: exact checks.

Model (shared Fock core below); the twistor form Sigma(Z1, Z2) = B(kappa Z1, Z2), kappa = Gamma c(e5) J, of
correspondence.reality-conjugation-twistor-form-factor (matrix H on CS, t-basis); the spinor action rho of
correspondence.spin-representation; the palatial realisation and q of
correspondence.symmetrised-quadratics-palatial-algebra (its EXPORTS), Z^alpha the t-coordinates, hbar = 2/5.
(1) [q(M), q(N)] = hbar q([M, N]) on samples (closure on gl(4, C)); u(2,2) = {M : M^dagger H + H M = 0},
    computed as a real kernel, has real dimension 16; the 15 real bivectors act inside it, tracelessly, and
    are real-linearly independent: su(2,2) (dimension 15) is their span, the image of so(2,4).
(2) The 15 bivectors act on CS by traceless maps of complex rank 15 (sl(CS)).
(3) beta -> q(rho(beta))/hbar: [q(rho A), q(rho B)] = hbar q(rho(A x B)) for 30 basis pairs; the 15 operators
    q(rho(e_a e_b)) are linearly independent (injective); [q(rho beta), Z^g] = -hbar (rho(beta) Z)^g and
    [q(rho beta), Zbar_g] = +hbar (rho(beta)^T Zbar)_g for all 15 basis bivectors.
(4) q(id) = sum Z^a Zbar_a - 2 hbar (minus hbar/2 per complex dimension of CS), and for each of the three
    Witt pairs rho(w_k ^ 2 w'_k) = N_k - 1/2: both shifts are negative, one half per dimension or mode.
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

HB = QI(F(2, 5))
GAMMA = [[QI(1 if bin(r).count("1") % 2 == 0 else -1) if r == c else Z0 for c in range(8)] for r in range(8)]
KMAT = mmul(GAMMA, CB[5])
BIV = [(a, b) for a in range(6) for b in range(a + 1, 6)]


def hmat():
    return [[bpair(apply(KMAT, [v.conj() for v in TB[i]]), TB[j]) for j in range(4)] for i in range(4)]


def lie(A, B):
    return gscal(F(1, 2), GA.sub(GA.mul(A, B, SQ), GA.mul(B, A, SQ)))


def check_palatial_quadratics_and_u22():
    premise("correspondence.reality-conjugation-twistor-form-factor")
    premise("correspondence.spin-representation")
    P = premise("correspondence.symmetrised-quadratics-palatial-algebra")
    opq, padd, pscal, monos = P["opq"], P["padd"], P["pscal"], P["monos"]
    M = [[QI(1), QI(0, 2), Z0, QI(-1)], [QI(2), QI(1, 1), Z0, Z0], [Z0, QI(3), QI(1), Z0], [QI(1, -1), Z0, QI(2), Z0]]
    N = [[Z0, ONE, Z0, Z0], [QI(0, 1), QI(2), Z0, QI(3)], [ONE, Z0, Z0, Z0], [Z0, ONE, Z0, QI(2, 1)]]
    for e in monos(2):
        f = {e: ONE}
        lhs = padd(opq(M, opq(N, f, HB), HB), opq(N, opq(M, f, HB), HB), QI(-1))
        assert lhs == pscal(HB, opq(mcomm(M, N), f, HB))
    H = hmat()
    # u(2,2): real unknowns (Re M_ij, Im M_ij), equations Re/Im of (M^dag H + H M)_kl
    cols = []
    for t in range(32):
        X = [[Z0] * 4 for _ in range(4)]
        i, j = (t % 16) // 4, t % 4
        X[i][j] = ONE if t < 16 else IU
        Xd = [[X[c][r].conj() for c in range(4)] for r in range(4)]
        Y = madd(mmul(Xd, H), mmul(H, X))
        cols.append([Y[k][l].re for k in range(4) for l in range(4)] + [Y[k][l].im for k in range(4) for l in range(4)])
    ku = GA.field_kernel([[cols[c][r] for c in range(32)] for r in range(32)])
    assert len(ku) == 16
    reals = []
    for (a, b) in BIV:
        R = cs_block(rho(gmul(E[a], E[b])))
        Rd = [[R[c][r].conj() for c in range(4)] for r in range(4)]
        assert mzero(madd(mmul(Rd, H), mmul(H, R)))
        assert sum((R[i][i] for i in range(4)), Z0) == Z0
        reals.append([R[i][j].re for i in range(4) for j in range(4)] + [R[i][j].im for i in range(4) for j in range(4)])
    assert GA.rank_of_vectors(reals) == 15 and GA.rank_of_vectors(reals + ku) == 16
    return True


def check_bivectors_act_as_sl():
    premise("correspondence.spin-representation")
    blocks = [cs_block(rho(gmul(E[a], E[b]))) for (a, b) in BIV]
    assert all(sum((R[i][i] for i in range(4)), Z0) == Z0 for R in blocks)
    assert GA.field_rank([[v for row in R for v in row] for R in blocks]) == 15
    return True


def check_klein_identification_is_lie_embedding():
    premise("correspondence.spin-representation")
    P = premise("correspondence.symmetrised-quadratics-palatial-algebra")
    opq, opZ, opZbar, padd, pscal, monos = P["opq"], P["opZ"], P["opZbar"], P["padd"], P["pscal"], P["monos"]
    bl = {p: cs_block(rho(gmul(E[p[0]], E[p[1]]))) for p in BIV}
    pairs = [(BIV[i], BIV[(3 * i + 5) % 15]) for i in range(15)] + [(BIV[i], BIV[(i + 1) % 15]) for i in range(15)]
    for (p, r) in pairs:
        Zb = cs_block(rho(lie(gmul(E[p[0]], E[p[1]]), gmul(E[r[0]], E[r[1]]))))
        for e in monos(2):
            f = {e: ONE}
            lhs = padd(opq(bl[p], opq(bl[r], f, HB), HB), opq(bl[r], opq(bl[p], f, HB), HB), QI(-1))
            assert lhs == pscal(HB, opq(Zb, f, HB))
    keys = monos(2)
    rows = []
    for p in BIV:
        vals = []
        for e in monos(1):
            im = opq(bl[p], {e: ONE}, HB)
            vals += [im.get(k, Z0) for k in keys]
        rows.append(vals)
    assert GA.field_rank(rows) == 15
    for p in BIV:
        R = bl[p]
        for g in range(4):
            for e in monos(1):
                f = {e: ONE}
                lhs = padd(opq(R, opZ(g, f), HB), opZ(g, opq(R, f, HB)), QI(-1))
                rhs = {}
                for a in range(4):
                    if R[g][a]:
                        rhs = padd(rhs, opZ(a, f), -HB * R[g][a])
                assert lhs == rhs
                lhs2 = padd(opq(R, opZbar(g, f, HB), HB), opZbar(g, opq(R, f, HB), HB), QI(-1))
                rhs2 = {}
                for b in range(4):
                    if R[b][g]:
                        rhs2 = padd(rhs2, opZbar(b, f, HB), HB * R[b][g])
                assert lhs2 == rhs2
    return True


def check_same_ordering_shift_both_storeys():
    premise("correspondence.clifford-side-ordering-shift")
    P = premise("correspondence.symmetrised-quadratics-palatial-algebra")
    opq, opZ, opZbar, padd, monos = P["opq"], P["opZ"], P["opZbar"], P["padd"], P["monos"]
    ID = ident(4)
    for e in monos(3):
        f = {e: ONE}
        normal = {}
        for a in range(4):
            normal = padd(normal, opZ(a, opZbar(a, f, HB)))
        assert padd(opq(ID, f, HB), normal, QI(-1)) == {e: QI(-4) * HB / QI(2)}
    for k in range(3):
        Nk = [[QI(1 if (r == c and (r >> k) & 1) else 0) for c in range(8)] for r in range(8)]
        rE = rho(gwedge(W[k], gscal(2, WP[k])))
        assert rE == madd(Nk, mscal(F(-1, 2), ident()))
    return True
