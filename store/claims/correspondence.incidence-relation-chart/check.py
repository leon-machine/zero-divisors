"""correspondence.incidence-relation-chart: exact checks.

Model (shared Fock core below). n0 = w0, ninf = 2 w'0 (the conformal model's n0 = (e+ + e-)/2,
ninf = e+ - e- with e+ = e0, e- = e2); N0 = psi(n0), N_inf = psi(ninf) (correspondence.spinor-identification),
S_pi = plane of N0 with basis pi1 = -t2, pi2 = t3 (pi1 ^ pi2 = N0) and S_omega = plane of N_inf with basis
e1 = t0, e2 = 2 t1 (e1 ^ e2 = N_inf); eps = -eps0/2. A in Hom(S_pi, S_omega) is a 2x2 matrix in these bases.
X(m) = n0 + m - (1/2) Q(m) ninf.
(1) P(A) = N0 + phi(A) + det(A) N_inf, with phi(A) in the mixed blocks (S_omega ^ S_pi), for the four
    matrix units and Gaussian samples (singular included).
(2) phi is injective on the four matrix units (rank 4), psi^{-1}(phi(A)) = m(A) is orthogonal to n0 and
    ninf (so phi is onto the mixed slot {n0, ninf}^perp), Q(m(A)) = -2 det A, psi^{-1}(P(A)) = X(m(A)) exactly,
    and P(A) is simple (Pf = 0).
(3) <psi^{-1} P(A), ninf> = 1 on the chart; a line meeting L_inf gives 0. Every null X with <X, ninf> = 1
    (sample m in W_C, complex included) is X(m) and equals psi^{-1} P(A) for A = phi^{-1}(psi(m)). Sample
    planes complementary to S_omega are graphs of a unique A (recovered and re-checked).
(4) (i) the planes of N_inf and N0 are skew (complementary). (iii) I6 = e0...e5 acts on CS as a scalar
    square root of -1 (here -i; +i on CS-); for real and complex x in W_C, A_x = (1/2) c(x) c(ninf) maps S_pi
    to S_omega, equals -(1/2) c(ninf) c(x) there (x is orthogonal to ninf), is linear in x, and its graph is
    the incidence line ker c(X(x)) on CS, with m(A_x) = x: omega = (1/2) x ninf pi is the incidence relation
    of the point x.
    (iv) Over all 15 bivectors of the null basis (w_i, w'_i), 10 fix ninf, 1 rescales it and 4 move it;
    the stabiliser of the ray of ninf, computed as a kernel in so(V_C), has dimension 11 and coincides with
    the stabiliser of S_omega; the stabiliser of both rays (the Levi factor, dimension 7) preserves both
    planes (its chiral action is checked in correspondence.chiral-planes-summand-spaces).
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
UNITS2 = [[[ONE if (i, j) == (a, b) else Z0 for j in range(2)] for i in range(2)] for a in range(2) for b in range(2)]
SAMPLES = UNITS2 + [[[ONE, Z0], [Z0, ONE]], [[QI(1, 1), QI(0, 2)], [QI(2), QI(1, -1)]],
                    [[ONE, QI(2)], [QI(3), QI(6)]], [[QI(0, 3), QI(1, 1)], [QI(-1, 1), QI(0, 1)]]]
MSAMP = [[0, 1, 0, 0, 0, 0], [0, 2, 0, 1, 3, 0], [0, 1, 0, QI(0, 1), 2, QI(1, -1)], [0, 0, 0, 1, 1, 1]]


def v4(*terms):
    return [sum((q(c) * v[k] for c, v in terms), Z0) for k in range(4)]


def img(A, j):
    return v4((A[0][j], E1), (A[1][j], E2))


def P_of(A):
    return wedge4(v4((1, PI1), (1, img(A, 0))), v4((1, PI2), (1, img(A, 1))))


def phi(A):
    return madd(wedge4(img(A, 0), PI2), wedge4(PI1, img(A, 1)))


def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def Xof(m):
    return GA.add(N0V, m, gscal(-gip(m, m) / QI(2), NIV))


def check_expansion_and_chart():
    premise("correspondence.spinor-identification")
    premise("correspondence.skew-lines-splittings-hyperbolic-planes-one")
    N0, Ninf = psi(N0V), psi(NIV)
    assert wedge4(PI1, PI2) == N0 and wedge4(E1, E2) == Ninf
    for A in SAMPLES:
        P = P_of(A)
        ph = phi(A)
        assert P == madd(N0, ph, mscal(det2(A), Ninf))
        assert all(not ph[i][j] for i in (0, 1) for j in (0, 1))
        assert all(not ph[i][j] for i in (2, 3) for j in (2, 3))
        m = psi_inv(ph)
        assert gip(m, N0V) == Z0 and gip(m, NIV) == Z0
        assert gip(m, m) == QI(-2) * det2(A)
        assert eps0(ph, ph) / QI(-2) == QI(-2) * det2(A)
        assert psi_inv(P) == Xof(m)
        assert pfaff(P) == Z0
    assert GA.field_rank([flat6(phi(A)) for A in UNITS2]) == 4
    return True


def check_coverage_of_the_affine_chart():
    premise("correspondence.spinor-identification")
    premise("correspondence.skew-lines-splittings-hyperbolic-planes-one")
    for A in SAMPLES:
        assert gip(psi_inv(P_of(A)), NIV) == ONE
    meet = wedge4(E1, v4((1, PI1), (1, E2)))
    assert gip(psi_inv(meet), NIV) == Z0 and pfaff(meet) == Z0
    phimat = [flat6(phi(A)) for A in UNITS2]
    for cs in MSAMP:
        m = gvec(cs)
        X = Xof(m)
        assert gip(X, X) == Z0 and gip(X, NIV) == ONE
        coeffs = GA.field_solve([[phimat[k][c] for k in (0, 1, 2, 3)] for c in (1, 2, 3, 4)],
                                [flat6(psi(m))[c] for c in (1, 2, 3, 4)])
        A = [[coeffs[0], coeffs[1]], [coeffs[2], coeffs[3]]]
        assert phi(A) == psi(m) and psi_inv(P_of(A)) == X
    # a plane complementary to S_omega is the graph of a unique A
    for L in ([[1, 2, 1, 0], [0, 1, 0, 1]], [[QI(0, 1), 0, 1, 1], [3, 1, 0, 2]]):
        L = [[q(x) for x in v] for v in L]
        assert GA.field_rank([E1, E2] + L) == 4
        # rows: L = graph iff each pi_j + A pi_j lies in L; solve for the graph vectors
        g = []
        for target in (PI1, PI2):
            M = [[L[0][r], L[1][r], E1[r], E2[r], -target[r]] for r in range(4)]
            sol = next(s for s in kernel(M) if s[4])
            g.append([s_ / sol[4] for s_ in sol[:4]])
        A = [[-g[0][2], -g[1][2]], [-g[0][3], -g[1][3]]]
        gl = [v4((1, PI1), (1, img(A, 0))), v4((1, PI2), (1, img(A, 1)))]
        assert same_span(gl, L)
    return True


def check_consequences_incidence_and_stabilisers():
    premise("correspondence.skew-lines-splittings-hyperbolic-planes-one")
    premise("correspondence.chiral-planes-summand-spaces")
    premise("correspondence.imported-stabilisers-flat-model")
    Som, Spi = plane(psi(NIV)), plane(psi(N0V))
    assert GA.field_rank(Som + Spi) == 4
    I6 = gmul(*E)
    I6m = rep(I6)
    assert all(I6m[r][c] == (QI(0, -1) if r == c else Z0) for r in EVEN for c in EVEN)
    assert all(I6m[r][c] == (QI(0, 1) if r == c else Z0) for r in ODD for c in ODD)
    xs = [gvec(cs) for cs in MSAMP]
    for x in xs:
        Ax = cs_block(mscal(F(1, 2), mmul(rep(x), rep(NIV))))
        assert Ax == cs_block(mscal(F(-1, 2), mmul(rep(NIV), rep(x))))
        A = []
        for p in (PI1, PI2):
            y = [sum((Ax[i][j] * p[j] for j in range(4)), Z0) for i in range(4)]
            assert y[2] == Z0 and y[3] == Z0
            A.append([y[0], y[1] / QI(2)])
        A = [[A[0][0], A[1][0]], [A[0][1], A[1][1]]]
        assert psi_inv(phi(A)) == x
        gl = [v4((1, PI1), (1, img(A, 0))), v4((1, PI2), (1, img(A, 1)))]
        assert same_span(gl, cs_kernel(Xof(x)))
    s = GA.add(xs[0], xs[1])
    As = cs_block(mscal(F(1, 2), mmul(rep(s), rep(NIV))))
    assert As == madd(cs_block(mscal(F(1, 2), mmul(rep(xs[0]), rep(NIV)))),
                      cs_block(mscal(F(1, 2), mmul(rep(xs[1]), rep(NIV)))))
    # stabiliser census in the null basis
    nb = W + WP
    bivs = [gwedge(nb[a], nb[b]) for a in range(6) for b in range(a + 1, 6)]
    fix = scale = move = 0
    for B in bivs:
        y = vact(B, NIV)
        if y == {}:
            fix += 1
        elif all(k == (2,) or k == (0,) for k in y) and GA.field_rank([[y.get((k,), Z0) for k in range(6)],
                                                                         [NIV.get((k,), Z0) for k in range(6)]]) == 1:
            scale += 1
        else:
            move += 1
    assert (fix, scale, move) == (10, 1, 4)
    # as kernels in so(V_C): stabiliser of the ray of ninf, and of the plane S_omega
    onb = [gmul(E[a], E[b]) for a in range(6) for b in range(a + 1, 6)]
    ray_rows, plane_rows = [], []
    ys = [vact(B, NIV) for B in onb]
    for k in range(6):
        if k in (0, 2):
            continue
        ray_rows.append([y.get((k,), Z0) for y in ys])
    ray_rows.append([y.get((0,), Z0) + y.get((2,), Z0) for y in ys])
    blocks = [cs_block(rho(B)) for B in onb]
    for i in (2, 3):
        for j in (0, 1):
            plane_rows.append([Bm[i][j] for Bm in blocks])
    kr, kp = kernel(ray_rows), kernel(plane_rows)
    assert len(kr) == 11 and len(kp) == 11 and same_span(kr, kp)
    # the Levi factor: also fixes the ray of n0; it preserves both planes
    zs = [vact(B, N0V) for B in onb]
    levi_rows = ray_rows + [[z.get((k,), Z0) for z in zs] for k in (1, 3, 4, 5)]
    levi_rows.append([z.get((0,), Z0) - z.get((2,), Z0) for z in zs])
    kl = kernel(levi_rows)
    assert len(kl) == 7
    for vec in kl:
        Bm = madd(*[mscal(vec[t], blocks[t]) for t in range(15)])
        assert all(not Bm[i][j] for i in (2, 3) for j in (0, 1)) and all(not Bm[i][j] for i in (0, 1) for j in (2, 3))
    return True
