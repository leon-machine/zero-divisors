"""correspondence.chiral-planes-summand-spaces: exact checks.

Model (shared Fock core below). The splitting of correspondence.skew-lines-splittings-hyperbolic-planes-one
for n0 = w0, ninf = 2 w'0: S_omega = plane of psi(ninf), S_pi = plane of psi(n0), W_C = {n0, ninf}^perp =
span(e1, e3, e4, e5) (signature (1,3)). l is spanned by the six GA bivectors e_i e_j of W_C, acting on W_C by
B . x, on CS by rho(B) = c(B)/2; g+ = {B - i I4 B}, g- = {B + i I4 B}, I4 = e1 e3 e4 e5, as in
correspondence.chirality-split-ordering-insensitivity-asd-sector.
(1) rho(l) preserves S_omega and S_pi; omega (x) pi -> psi^{-1}(omega ^ pi) has rank 4 onto W_C and is
    l-equivariant: psi^{-1}(rho(B) omega ^ pi + omega ^ rho(B) pi) = B . psi^{-1}(omega ^ pi) for all six B and
    all basis tensors. One of g+, g- acts on S_omega by three linearly independent 2x2 matrices (faithfully)
    and by zero on S_pi; the other the reverse.
(2) The l-equivariant maps W_C (x) S_pi -> S_omega and W_C (x) S_omega -> S_pi, computed as the kernel of the
    16-unknown linear system of equivariance under the six generators, are one-dimensional each.
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
WC = [E[1], E[3], E[4], E[5]]
LOR = [(1, 3), (1, 4), (1, 5), (3, 4), (3, 5), (4, 5)]
I4 = gmul(E[1], E[3], E[4], E[5])


def coeffs_in(basis, y):
    """Coefficients c with sum c_i basis_i = y (y assumed in the span)."""
    n = len(basis)
    M = [[basis[i][r] for i in range(n)] + [-y[r]] for r in range(len(y))]
    sol = next(s for s in kernel(M) if s[n])
    return [s_ / sol[n] for s_ in sol[:n]]


def restrict(M, basis):
    cols = []
    for b in basis:
        y = [sum((M[i][j] * b[j] for j in range(4)), Z0) for i in range(4)]
        cols.append(coeffs_in(basis, y))
    return [[cols[j][i] for j in range(len(basis))] for i in range(len(basis))]


def vcoords(v):
    return [v.get((k,), Z0) for k in (1, 3, 4, 5)]


def wc_matrix(B):
    cols = [vcoords(vact(B, x)) for x in WC]
    return [[cols[j][i] for j in range(4)] for i in range(4)]


def setup():
    Som, Spi = plane(psi(NIV)), plane(psi(N0V))
    base = [gmul(E[i], E[j]) for (i, j) in LOR]
    gp = [GA.sub(B, gscal(IU, gmul(I4, B))) for B in base[:3]]
    gm = [GA.add(B, gscal(IU, gmul(I4, B))) for B in base[:3]]
    return Som, Spi, base, gp, gm


def check_planes_are_chiral_doublets():
    premise("correspondence.skew-lines-splittings-hyperbolic-planes-one")
    premise("correspondence.chirality-split-ordering-insensitivity-asd-sector")
    Som, Spi, base, gp, gm = setup()
    assert len(Som) == 2 and len(Spi) == 2
    for B in base:
        R = cs_block(rho(B))
        for pl in (Som, Spi):
            for b in pl:
                y = [sum((R[i][j] * b[j] for j in range(4)), Z0) for i in range(4)]
                assert GA.field_rank(pl + [y]) == 2
    imgs = []
    for o in Som:
        for p in Spi:
            v = psi_inv(wedge4(o, p))
            assert gip(v, N0V) == Z0 and gip(v, NIV) == Z0
            imgs.append(v)
            for B in base:
                R = cs_block(rho(B))
                Ro = [sum((R[i][j] * o[j] for j in range(4)), Z0) for i in range(4)]
                Rp = [sum((R[i][j] * p[j] for j in range(4)), Z0) for i in range(4)]
                lhs = psi_inv(madd(wedge4(Ro, p), wedge4(o, Rp)))
                assert lhs == vact(B, v)
    assert GA.field_rank([vcoords(v) for v in imgs]) == 4
    pattern = []
    for g in (gp, gm):
        on_om = [restrict(cs_block(rho(X)), Som) for X in g]
        on_pi = [restrict(cs_block(rho(X)), Spi) for X in g]
        kills_pi = all(all(not v for row in M for v in row) for M in on_pi)
        kills_om = all(all(not v for row in M for v in row) for M in on_om)
        faithful_om = GA.field_rank([[v for row in M for v in row] for M in on_om]) == 3
        faithful_pi = GA.field_rank([[v for row in M for v in row] for M in on_pi]) == 3
        pattern.append((kills_pi and faithful_om, kills_om and faithful_pi))
    assert sorted(pattern) == [(False, True), (True, False)]
    return True


def equivariant_maps(src_plane, dst_plane, base):
    """Kernel of the equivariance system for T: W_C (x) src -> dst, T[d][w][s] flattened."""
    def idx(d, w, s):
        return d * 8 + w * 2 + s
    rows = []
    for B in base:
        R = cs_block(rho(B))
        Wm = wc_matrix(B)
        Rs, Rd = restrict(R, src_plane), restrict(R, dst_plane)
        for w in range(4):
            for s in range(2):
                for d in range(2):
                    row = [Z0] * 16
                    # (Rd T(w (x) s))_d - T(B w (x) s)_d - T(w (x) Rs s)_d = 0
                    for d2 in range(2):
                        row[idx(d2, w, s)] = row[idx(d2, w, s)] + Rd[d][d2]
                    for w2 in range(4):
                        row[idx(d, w2, s)] = row[idx(d, w2, s)] - Wm[w2][w]
                    for s2 in range(2):
                        row[idx(d, w, s2)] = row[idx(d, w, s2)] - Rs[s2][s]
                    rows.append(row)
    return kernel(rows)


def check_summand_hom_spaces_one_dimensional():
    premise("correspondence.skew-lines-splittings-hyperbolic-planes-one")
    premise("correspondence.chirality-split-ordering-insensitivity-asd-sector")
    Som, Spi, base, gp, gm = setup()
    assert len(equivariant_maps(Spi, Som, base)) == 1
    assert len(equivariant_maps(Som, Spi, base)) == 1
    # control: without the W_C factor there is no nonzero equivariant map S_pi -> S_omega
    rows = []
    for B in base:
        R = cs_block(rho(B))
        Rs, Rd = restrict(R, Spi), restrict(R, Som)
        for s in range(2):
            for d in range(2):
                row = [Z0] * 4
                for d2 in range(2):
                    row[d2 * 2 + s] = row[d2 * 2 + s] + Rd[d][d2]
                for s2 in range(2):
                    row[d * 2 + s2] = row[d * 2 + s2] - Rs[s2][s]
                rows.append(row)
    assert kernel(rows) == []
    return True
