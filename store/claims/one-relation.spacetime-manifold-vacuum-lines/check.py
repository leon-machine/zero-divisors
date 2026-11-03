"""one-relation.spacetime-manifold-vacuum-lines: exact checks.

Model (shared Fock core below): R^{2,4} with e+ = e0, e- = e2, n0 = (e+ + e-)/2 = w0, ninf = e+ - e- = 2 w'0,
spacetime the complement span(e1; e3, e4, e5) (signature (1,3), e1 the time direction), so for a speed
c the point x = (t, x1, x2, x3) is c t e1 + x1 e3 + x2 e4 + x3 e5 with Q(x) = c^2 t^2 - |x|^2, and
X(x) = n0 + x - (1/2) Q(x) ninf. Seven sample points give timelike, null and spacelike Q.
(1) At each point and speed c = 1, 2, 3/2: Q(X(x)) = 0, the GA square X(x) X(x) = 0 and X(x) != 0, so X(x)
    is a nonzero nilpotent (non-invertible); with slot coefficient s in place of -1/2 the square is
    Q(x)(1 + 2s), nonzero for Q(x) != 0 unless s = -1/2.
(2) c(X(x))^2 = 0; its kernel has dimension 4 on the module and 2 on CS (the incidence line L_x); two
    independent spinors on L_x and their sum are pure (annihilators of dimension 3), with pairwise distinct
    annihilators, each containing X(x); X and -X give the same line (the double cover); the seven lines are
    pairwise distinct, and two lines meet (span of rank 3) exactly when the points are null-separated (3 of
    the 21 pairs), with <X(x), X(y)> = -(1/2) Q(x - y) on all 21 pairs.
(3) Over a chosen vacuum u on L_x, a dual isotropic complement gives three ladder pairs obeying the CAR
    {c(w_i), c(u_j)} = delta_ij (the Witt normalisation <w_i, u_j> = delta_ij / 2) with u annihilated.
The interpretive clauses (which theory lives where, and the singularity as degeneration of the vacuum
family, a reading of the sheaf paper's localisation theorem) have no further finite content.
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
POINTS = [(0, 0, 0, 0), (1, 0, 0, 0), (2, 1, 0, 0), (1, 1, 0, 0), (F(3, 2), -1, 2, F(1, 3)), (-5, 2, F(7, 4), -1),
          (3, 2, 2, 1)]


def xv(p, c=1):
    return gvec([0, q(c) * q(p[0]), 0, p[1], p[2], p[3]])


def Xpt(p, c=1, s=F(-1, 2)):
    x = xv(p, c)
    return GA.add(N0V, x, gscal(q(s) * gip(x, x), NIV))


def annihilator(u):
    cols = [apply(CB[k], u) for k in range(6)]
    return [[v[k] for k in range(6)] for v in kernel([[cols[k][r] for k in range(6)] for r in range(8)])]


def even_vec(c4):
    out = [Z0] * 8
    for k, m in enumerate(EVEN):
        out[m] = c4[k]
    return out


def incidence_line(p):
    M = rep(Xpt(p))
    return kernel([[M[r][m] for m in EVEN] for r in range(8)])


def check_every_point_is_null():
    premise("one-relation.imported-pure-spinors-incidence-chart")
    assert gip(N0V, N0V) == Z0 and gip(NIV, NIV) == Z0 and gip(N0V, NIV) == ONE
    Qs = set()
    for c in (1, 2, F(3, 2)):
        for p in POINTS:
            x = xv(p, c)
            X = Xpt(p, c)
            Qx = gip(x, x)
            assert Qx == QI(c * c) * q(p[0]) * q(p[0]) - q(p[1]) * q(p[1]) - q(p[2]) * q(p[2]) - q(p[3]) * q(p[3])
            Qs.add((Qx.re > 0) - (Qx.re < 0))
            assert gip(X, X) == Z0 and gmul(X, X) == {} and X != {}
            for s in (F(0), F(1), F(-1), F(1, 2)):
                Xs = Xpt(p, c, s)
                assert gip(Xs, Xs) == Qx * q(1 + 2 * s)
    assert Qs == {-1, 0, 1}
    return True


def check_points_are_lines_of_vacua():
    premise("one-relation.imported-pure-spinors-incidence-chart")
    lines = []
    for p in POINTS:
        X = Xpt(p)
        M = rep(X)
        assert mzero(mmul(M, M))
        assert len(kernel(M)) == 4
        L = incidence_line(p)
        assert len(L) == 2
        assert same_span(L, kernel([[rep(gscal(-1, X))[r][m] for m in EVEN] for r in range(8)]))
        Xc = [X.get((k,), Z0) for k in range(6)]
        Z1, Z2 = even_vec(L[0]), even_vec(L[1])
        Z3 = [a + b for a, b in zip(Z1, Z2)]
        anns = [annihilator(Z) for Z in (Z1, Z2, Z3)]
        for A in anns:
            assert len(A) == 3 and GA.field_rank(A + [Xc]) == 3
        for i in range(3):
            for j in range(i + 1, 3):
                assert GA.field_rank(anns[i] + anns[j]) > 3
        lines.append(L)
    met = 0
    for i in range(len(POINTS)):
        for j in range(i + 1, len(POINTS)):
            d = [q(a) - q(b) for a, b in zip(POINTS[i], POINTS[j])]
            Qd = d[0] * d[0] - d[1] * d[1] - d[2] * d[2] - d[3] * d[3]
            assert gip(Xpt(POINTS[i]), Xpt(POINTS[j])) == QI(F(-1, 2)) * Qd
            rk = GA.field_rank(lines[i] + lines[j])
            assert rk >= 3 and (rk == 3) == (Qd == Z0)
            met += rk == 3
    assert met == 3
    return True


def check_car_over_a_chosen_vacuum():
    premise("one-relation.two-presentations")
    premise("one-relation.imported-pure-spinors-incidence-chart")
    for p in POINTS[2:4]:
        L = incidence_line(p)
        u = even_vec(L[0])
        Wu = [gvec(v) for v in annihilator(u)]
        Vs = []
        for j in range(3):
            M = [[gip(Wu[i], E[c]) for c in range(6)] + [QI(F(-1, 2)) if i == j else Z0] for i in range(3)]
            sol = next(s for s in kernel(M) if s[6])
            Vs.append(gvec([s_ / sol[6] for s_ in sol[:6]]))
        Us = [GA.sub(Vs[j], GA.add(*[gscal(gip(Vs[j], Vs[k]), Wu[k]) for k in range(3)])) for j in range(3)]
        for i in range(3):
            assert all(not x for x in apply(rep(Wu[i]), u))
            for j in range(3):
                ac = madd(mmul(rep(Wu[i]), rep(Us[j])), mmul(rep(Us[j]), rep(Wu[i])))
                assert ac == (ident() if i == j else zmat())
                assert mzero(madd(mmul(rep(Us[i]), rep(Us[j])), mmul(rep(Us[j]), rep(Us[i]))))
    return True
