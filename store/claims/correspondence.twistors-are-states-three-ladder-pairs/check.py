"""correspondence.twistors-are-states-three-ladder-pairs: exact checks.

Model (shared Fock core below): the Fock model of correspondence.fock-model-complexified-ascended-algebra.
W_u = {v : c(v) u = 0} is computed as a kernel; samples: the vacuum, the top-adjacent even states, generic
even spinors with Gaussian coefficients (six in all), and two odd spinors.
(1) For each sample u in CS: dim W_u = 3 and W_u is totally isotropic (pure); the joint kernel of c(W_u) on
    all of Lambda W is exactly C u; non-proportional samples have different W_u; equivariance under Spin:
    for g = x y (x, y real vectors with Q(x) Q(y) = 1) the annihilator of c(g) u is Ad_g(W_u) = g W_u g^{-1},
    computed in GA.py.
(2) A dual isotropic complement U' of W_u (built as in T09's proof) gives three ladder pairs with the CAR
    {c(w_i), c(u_j)} = delta_ij, squares zero, and u annihilated; xi -> c(xi) u on the eight products of U'
    vectors has rank 8 (a linear isomorphism Lambda U' -> Lambda W); the even products give CS (rank 4 in
    the even block) and the odd ones CS- (rank 4 in the odd block).
(3) Every vector is a sum of the six pair operators (the w_i, u_j form a basis of V_C); for each of the 8
    coordinate maximal isotropic subspaces (w_k or w'_k per mode) and for every sample W_u, the joint kernel
    of c(W) on the whole module is one line, of one parity: no maximal isotropic annihilates both a nonzero
    even and a nonzero odd spinor.
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

EVEN_S = [e8(0), e8(3), lin((1, e8(0)), (2, e8(6)), (QI(0, 1), e8(5)), (QI(1, -1), e8(3))),
          lin((3, e8(0)), (QI(0, -2), e8(3))), lin((1, e8(6)), (1, e8(5))),
          lin((1, e8(0)), (1, e8(3)), (1, e8(5)), (1, e8(6)))]
ODD_S = [lin((1, e8(1)), (QI(0, 1), e8(2)), (3, e8(7))), e8(7)]
# sample spin elements g = x y (products of two non-null vectors) and the generic even spinors they move
SPIN_PAIRS = ((E[0], E[1]), (gvec([F(5, 3), 0, F(4, 3), 0, 0, 0]), E[3]), (E[2], E[4]))
MOVED_S = EVEN_S[2:4]


def annihilator(u):
    cols = [apply(CB[k], u) for k in range(6)]
    return [gvec(v) for v in kernel([[cols[k][r] for k in range(6)] for r in range(8)])]


def joint_kernel(vecs):
    rows = []
    for v in vecs:
        rows += rep(v)
    return kernel(rows)


def vrow(v):
    return [v.get((k,), Z0) for k in range(6)]


def dual_complement(Wu):
    Vs = []
    for j in range(3):
        M = [[gip(Wu[i], E[c]) for c in range(6)] + [QI(F(-1, 2)) if i == j else Z0] for i in range(3)]
        sol = next(s for s in kernel(M) if s[6])
        Vs.append(gvec([s_ / sol[6] for s_ in sol[:6]]))
    return [GA.sub(Vs[j], GA.add(*[gscal(gip(Vs[j], Vs[k]), Wu[k]) for k in range(3)])) for j in range(3)]


def check_every_conformal_spinor_is_pure():
    premise("correspondence.fock-model-complexified-ascended-algebra")
    premise("correspondence.spin-representation")
    spaces = []
    for u in EVEN_S:
        Wu = annihilator(u)
        assert len(Wu) == 3 and all(gip(x, y) == Z0 for x in Wu for y in Wu)
        K = joint_kernel(Wu)
        assert len(K) == 1 and GA.field_rank([K[0], u]) == 1
        spaces.append([vrow(v) for v in Wu])
    for i in range(len(spaces)):
        for j in range(i):
            assert not same_span(spaces[i], spaces[j])
    for (x, y) in SPIN_PAIRS:
        g = gmul(x, y)
        ginv = gmul(gscal(ONE / gip(y, y), y), gscal(ONE / gip(x, x), x))
        assert gmul(g, ginv) == {(): ONE}
        for u in MOVED_S:
            gu = apply(rep(g), u)
            moved = [vrow(gmul(g, w, ginv)) for w in annihilator(u)]
            assert same_span(moved, [vrow(v) for v in annihilator(gu)])
    return True


def check_vacuum_of_own_three_pair_system():
    premise("correspondence.imported-ladder-pairs-fock-modules-over")
    for u in EVEN_S + ODD_S:
        Wu = annihilator(u)
        Us = dual_complement(Wu)
        for i in range(3):
            for j in range(3):
                assert gip(Wu[i], Us[j]) == (QI(F(1, 2)) if i == j else Z0)
                assert gip(Us[i], Us[j]) == Z0
                ac = madd(mmul(rep(Wu[i]), rep(Us[j])), mmul(rep(Us[j]), rep(Wu[i])))
                assert ac == (ident() if i == j else zmat())
            assert all(not x for x in apply(rep(Wu[i]), u))
        states, parity = [], []
        for S in range(8):
            M = ident()
            for k in range(3):
                if (S >> k) & 1:
                    M = mmul(M, rep(Us[k]))
            states.append(apply(M, u))
            parity.append(bin(S).count("1") % 2)
        assert GA.field_rank(states) == 8
        ev = [s for s, p in zip(states, parity) if p == 0]
        od = [s for s, p in zip(states, parity) if p == 1]
        u_even = any(u[m] for m in EVEN)
        same, other = (EVEN, ODD) if u_even else (ODD, EVEN)
        assert all(not s[m] for s in ev for m in other) and GA.field_rank([[s[m] for m in same] for s in ev]) == 4
        assert all(not s[m] for s in od for m in same) and GA.field_rank([[s[m] for m in other] for s in od]) == 4
    return True


def check_states_not_operators_and_disjoint_families():
    premise("correspondence.fock-model-complexified-ascended-algebra")
    u = EVEN_S[2]
    Wu = annihilator(u)
    Us = dual_complement(Wu)
    assert GA.field_rank([vrow(v) for v in Wu + Us]) == 6
    for S in range(8):
        Wc = [W[k] if (S >> k) & 1 else WP[k] for k in range(3)]
        assert all(gip(x, y) == Z0 for x in Wc for y in Wc)
        K = joint_kernel(Wc)
        assert len(K) == 1
        ev = any(K[0][m] for m in EVEN)
        od = any(K[0][m] for m in ODD)
        assert ev != od
        assert ev == (bin(S).count("1") % 2 == 0)
    for u in EVEN_S + ODD_S:
        K = joint_kernel(annihilator(u))
        assert len(K) == 1 and (any(K[0][m] for m in EVEN) != any(K[0][m] for m in ODD))
    return True
