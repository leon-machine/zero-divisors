"""correspondence.chirality-split-ordering-insensitivity-asd-sector: exact checks.

Model (shared Fock core below). The splitting is the hyperbolic plane of mode 0, n0 = w0 = (e0 + e2)/2,
ninf = 2 w'0 = e0 - e2; its Minkowski complement W_{1,3} = span(e1; e3, e4, e5) has signature (1,3), and
l = Lambda^2 (W_{1,3})_C is spanned by the six GA bivectors e_i e_j there. The duality operator of
correspondence.lorentzian-duality-complex-structure is *B = I4 B with I4 = e1 e3 e4 e5 (sign +1 there),
so g+ = {B - i I4 B}, g- = {B + i I4 B}. The palatial algebra is the polynomial realisation of
correspondence.symmetrised-quadratics-palatial-algebra (its EXPORTS), with Z^alpha the t-coordinates of CS
and q(rho(B)) built from the spinor action rho(B) = c(B)/2 on CS (correspondence.spin-representation).
(1) I4^2 = -1 and I4 B is in l; g+ and g- are 3-dimensional, l = g+ + g-, [g+, g-] = 0 (GA commutator
    product), [g, g] = g for each (rank 3): a perfect 3-dimensional complex Lie algebra, sl(2, C).
(2a) For X, Y in g-: [q(rho X), q(rho Y)] = hbar q(rho(X x Y)) with X x Y in g-, and the length-three
    reordering ABC - CBA = hbar(q(rho[A,B]) C + B q(rho[A,C]) + q(rho[B,C]) A) lies in hbar A^- (samples).
(2b) [q(rho X), q(rho Y)] = 0 for X in g-, Y in g+ (all nine basis pairs).
(2c) For X, Y in g+, ad_{q(rho X)/hbar} q(rho Y) = q(rho(X x Y)), nonzero for some pair: the googly slot is a
    copy of the adjoint representation; the generators of A^- and their products of length two are killed
    by ad g+, so they lie in the trivial isotypic part (zero adjoint component).
Operators are compared on all monomials of degree <= 2.
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

HB = QI(F(3, 2))
LOR = [(1, 3), (1, 4), (1, 5), (3, 4), (3, 5), (4, 5)]
I4 = gmul(E[1], E[3], E[4], E[5])


def lie(A, B):
    return gscal(F(1, 2), GA.sub(GA.mul(A, B, SQ), GA.mul(B, A, SQ)))


def gcoords(x):
    return [x.get(b, Z0) for b in [(i, j) for i in range(6) for j in range(i + 1, 6)]]


def sectors():
    base = [gmul(E[i], E[j]) for (i, j) in LOR]
    gp = [GA.sub(B, gscal(IU, gmul(I4, B))) for B in base[:3]]
    gm = [GA.add(B, gscal(IU, gmul(I4, B))) for B in base[:3]]
    return base, gp, gm


def check_two_commuting_sl2_sectors():
    premise("correspondence.lorentzian-duality-complex-structure")
    base, gp, gm = sectors()
    assert gmul(I4, I4) == {(): QI(-1)}
    for B in base:
        IB = gmul(I4, B)
        assert all(len(b) == 2 and set(b) <= {1, 3, 4, 5} for b in IB)
    for X in gp:
        assert gmul(I4, X) == gscal(IU, X)
    for X in gm:
        assert gmul(I4, X) == gscal(QI(0, -1), X)
    assert GA.field_rank([gcoords(x) for x in gp]) == 3 and GA.field_rank([gcoords(x) for x in gm]) == 3
    assert GA.field_rank([gcoords(x) for x in gp + gm]) == 6
    for X in gp:
        for Y in gm:
            assert lie(X, Y) == {}
    for g in (gp, gm):
        brackets = [gcoords(lie(X, Y)) for X in g for Y in g]
        assert GA.field_rank(brackets) == 3 and GA.field_rank(brackets + [gcoords(x) for x in g]) == 3
    return True


def opmul(ops, f):
    for op in reversed(ops):
        f = op(f)
    return f


def check_asd_reorderings_stay_in_asd_algebra():
    premise("correspondence.lorentzian-duality-complex-structure")
    premise("correspondence.spin-representation")
    P = premise("correspondence.symmetrised-quadratics-palatial-algebra")
    opq, padd, pscal, monos = P["opq"], P["padd"], P["pscal"], P["monos"]
    base, gp, gm = sectors()
    Q = [cs_block(rho(X)) for X in gm]

    def qop(M):
        return lambda f: opq(M, f, HB)

    for i, X in enumerate(gm):
        for j, Y in enumerate(gm):
            Z = lie(X, Y)
            assert GA.field_rank([gcoords(x) for x in gm] + [gcoords(Z)]) == 3
            for e in monos(2):
                f = {e: ONE}
                lhs = padd(opq(Q[i], opq(Q[j], f, HB), HB), opq(Q[j], opq(Q[i], f, HB), HB), QI(-1))
                assert lhs == pscal(HB, opq(cs_block(rho(Z)), f, HB))
    A, B, C = (qop(M) for M in Q)
    AB, AC, BC = (qop(cs_block(rho(lie(gm[a], gm[b])))) for (a, b) in ((0, 1), (0, 2), (1, 2)))
    for e in monos(2):
        f = {e: ONE}
        lhs = padd(opmul([A, B, C], f), opmul([C, B, A], f), QI(-1))
        rhs = padd(padd(opmul([AB, C], f), opmul([B, AC], f)), opmul([BC, A], f))
        assert lhs == pscal(HB, rhs)
    return True


def check_asd_commutes_with_googly_slot_adjoint():
    premise("correspondence.lorentzian-duality-complex-structure")
    premise("correspondence.spin-representation")
    P = premise("correspondence.symmetrised-quadratics-palatial-algebra")
    opq, padd, pscal, monos = P["opq"], P["padd"], P["pscal"], P["monos"]
    base, gp, gm = sectors()
    Qp = [cs_block(rho(X)) for X in gp]
    Qm = [cs_block(rho(X)) for X in gm]
    for M in Qm:
        for N in Qp:
            for e in monos(2):
                f = {e: ONE}
                assert padd(opq(M, opq(N, f, HB), HB), opq(N, opq(M, f, HB), HB), QI(-1)) == {}
            # products of two A^- generators are also killed by ad g+
            for e in monos(1):
                f = {e: ONE}
                prod = lambda g: opq(M, opq(Qm[0], g, HB), HB)
                assert padd(prod(opq(N, f, HB)), opq(N, prod(f), HB), QI(-1)) == {}
    nonzero = 0
    for i, X in enumerate(gp):
        for j, Y in enumerate(gp):
            Zb = cs_block(rho(lie(X, Y)))
            if any(v for row in Zb for v in row):
                nonzero += 1
            for e in monos(2):
                f = {e: ONE}
                ad = padd(opq(Qp[i], opq(Qp[j], f, HB), HB), opq(Qp[j], opq(Qp[i], f, HB), HB), QI(-1))
                assert ad == pscal(HB, opq(Zb, f, HB))
    assert nonzero == 6
    return True
