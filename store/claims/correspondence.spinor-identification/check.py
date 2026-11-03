"""correspondence.spinor-identification: exact checks.

Model (shared Fock core below): the Fock model of correspondence.fock-model-complexified-ascended-algebra
and the Chevalley pairing B of correspondence.chevalley-pairing. psi(v) is the bivector of CS obtained from
the antisymmetric form (s, s') -> B(s, c(v) s') on CS- through the perfect pairing B: CS- x CS -> C;
eps0 is the volume functional with eps0(t0 t1 t2 t3) = 1.
(1) The form is antisymmetric for every basis vector; psi is injective (rank 6), hence V_C = Lambda^2 CS;
    it is Spin-equivariant, psi(B . v) = rho(B) psi(v) + psi(v) rho(B)^T, for all 15 basis bivectors and
    6 basis vectors; and eps0(psi(v) ^ psi(v')) = -2 <v, v'> on all 21 pairs, so with eps := -eps0/2 the
    quadratic form is P -> eps(P ^ P) (in particular Q(v) = eps(psi(v) ^ psi(v))).
(2) Pf(psi(v)) = -Q(v) at real and complex samples: a vector is null iff psi(v) is simple (rank 2); for null
    samples the plane of psi(v) is exactly ker c(v) on CS (a line of P(CS)); non-null samples have rank 4.
(3) psi(t v) = t psi(v) has the same plane for t = -1, 2, i, so v and -v (one null line, two rays) give
    one line of P(CS); eight pairwise non-proportional real null vectors give eight distinct planes.
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

NULLS = [[0, 1, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 0, 0, 1, 0], [1, 0, 0, 0, 0, -1],
         [3, 4, 0, 0, 0, 5], [1, 1, 1, 1, 0, 0], [2, 1, 0, 2, 1, 0], [1, 0, 0, F(3, 5), F(4, 5), 0]]
NONNULL = [[1, 0, 0, 0, 0, 0], [1, 2, 0, 1, 0, 3], [QI(0, 1), 0, 1, 0, 0, 0]]
CNULL = [[1, QI(0, 1), 0, 0, 0, 0], [0, 0, 0, 1, QI(0, 1), 0]]
PF_SAMPLE = [1, 2, 3, QI(0, 1), 0, 2]        # a further generic complex vector for Pf(psi(v)) = -<v, v>
RAY_SCALARS = (QI(-1), QI(2), QI(0, 1))     # sample nonzero scalars t: psi(t v) = t psi(v), same plane


def check_canonical_isomorphism_and_form():
    premise("correspondence.fock-model-complexified-ascended-algebra")
    premise("correspondence.chevalley-pairing")
    for k in range(6):
        Cv = rep(E[k])
        G = [[bpair(SB[i], apply(Cv, SB[j])) for j in range(4)] for i in range(4)]
        assert all(G[i][j] == -G[j][i] for i in range(4) for j in range(4))
    assert GA.field_rank([flat6(P) for P in PSI_E]) == 6
    for a in range(6):
        for b in range(a, 6):
            assert eps0(PSI_E[a], PSI_E[b]) == QI(-2) * gip(E[a], E[b])
    for a in range(6):
        for b in range(a + 1, 6):
            B = gmul(E[a], E[b])
            R = cs_block(rho(B))
            Rt = [[R[j][i] for j in range(4)] for i in range(4)]
            for k in range(6):
                lhs = psi(vact(B, E[k]))
                assert lhs == madd(mmul(R, PSI_E[k]), mmul(PSI_E[k], Rt))
    return True


def check_null_iff_simple_plane_is_kernel():
    premise("correspondence.fock-model-complexified-ascended-algebra")
    premise("correspondence.chevalley-pairing")
    for cs in NULLS + CNULL:
        v = gvec(cs)
        assert gip(v, v) == Z0
        P = psi(v)
        assert pfaff(P) == Z0 and GA.field_rank(P) == 2
        assert same_span(plane(P), cs_kernel(v)) and len(cs_kernel(v)) == 2
    for cs in NONNULL:
        v = gvec(cs)
        P = psi(v)
        assert gip(v, v) != Z0 and pfaff(P) == -gip(v, v) and GA.field_rank(P) == 4
        assert cs_kernel(v) == []
    v = gvec(PF_SAMPLE)
    assert pfaff(psi(v)) == -gip(v, v)
    return True


def check_rays_double_cover_lines():
    premise("correspondence.imported-forced-completion-fibre-quadric")
    premise("correspondence.chevalley-pairing")
    planes = []
    for cs in NULLS:
        v = gvec(cs)
        assert gip(v, v) == Z0
        P = psi(v)
        for t in RAY_SCALARS:
            Pt = psi(gscal(t, v))
            assert Pt == mscal(t, P) and same_span(plane(Pt), plane(P))
        planes.append(plane(P))
    for i in range(len(planes)):
        for j in range(i):
            assert not same_span(planes[i], planes[j])
    assert len(planes) == 8
    return True
