"""synthesis.transverse-corank-two-walls-are-wild: exact checks.

Polynomial determinants by cofactor expansion over GA's exact polynomials, signatures by GA's
congruence diagonalisation, ranks by exact Gaussian elimination. Everything is over Fraction.
"""
from fractions import Fraction as F
from itertools import product
import GA
from tp_premise import premise

# generic data (module level, so that the mutation test perturbs the structural integers)
PS = [[[1, 2, 0, 1], [0, 1, 3, 0], [2, 0, 1, 1], [1, 1, 1, 2]],
      [[2, 1, 0, 0], [1, 1, 1, 0], [0, 0, 1, 3], [1, 0, 0, 1]]]
DS = [[0, 1, -1, -1], [0, -1, -1, -1], [0, 1, 1, -1]]
HS = [[[1, 0, 2, 0], [0, 3, 1, 1], [2, 1, 0, 5], [0, 1, 5, -2]],
      [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
      [[-3, 1, 1, 2], [1, 1, 0, 0], [1, 0, 2, 1], [2, 0, 1, 7]]]
PERTS = [[[1, 2, 1, 0], [2, -1, 0, 3], [1, 0, 2, 1], [0, 3, 1, 1]],
         [[0, 1, 4, 1], [1, 5, 1, 0], [4, 1, -2, 2], [1, 0, 2, 3]]]
LPERT = [[1, 2, 0], [0, 1, 3], [2, 1, 1]]
CONE_CASES = [([[-1, 0], [0, -1]], {(2, 2, 0), (1, 3, 0), (0, 4, 0)}),
              ([[1, 0], [0, -1]], {(3, 1, 0), (2, 2, 0), (1, 3, 0)}),
              ([[1, 0], [0, 1]], {(4, 0, 0), (3, 1, 0), (2, 2, 0)})]
THIS_WORLD, TWO_TIME = (1, 3), (2, 2)
SCALES = [F(1), F(1, 10), F(1, 1000)]
DIRS = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (1, 2, 3, 4), (2, -1, 5, 1)]
LINES = [(1, 1, 1, 0), (1, -1, 1, 0), (4, 2, 1, 0), (0, 0, 0, 1)]
TS = [F(1), F(-3), F(5, 2), F(-7, 3)]
RESTS = [[[-1, 0, 0], [0, -1, 0], [0, 0, -1]], [[1, 0, 0], [0, -1, 0], [0, 0, -1]]]
EPS1 = F(1, 5)


def sample_points(e):
    return [(e, 0, e, 0), (-e, 0, -e, 0), (e, 0, -e, 0), (0, e, 0, 0), (e, e, e, e)]



def pdet(M):
    """Determinant of a square matrix of polynomials (coefficient lists), cofactor expansion."""
    n = len(M)
    if n == 1:
        return M[0][0]
    acc = []
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in M[1:]]
        term = GA.pmul(M[0][j], pdet(minor))
        acc = GA.padd(acc, term if j % 2 == 0 else GA.pneg(term))
    return GA.ptrim(acc)


def coef(p, k):
    p = GA.ptrim(p)
    return p[k] if k < len(p) else F(0)


def line_matrix(G0, H):
    """The polynomial matrix G0 + t H."""
    n = len(G0)
    return [[GA.ptrim([F(G0[i][j]), F(H[i][j])]) for j in range(n)] for i in range(n)]


def det(M):
    return coef(pdet([[GA.pconst(F(x)) for x in row] for row in M]), 0)


def adjugate(M):
    n = len(M)
    out = [[F(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            minor = [row[:j] + row[j + 1:] for k, row in enumerate(M) if k != i]
            out[j][i] = (-1) ** (i + j) * det(minor)
    return out


def transpose(A):
    return [list(r) for r in zip(*A)]


def block(A, B):
    """Block-diagonal A + B."""
    a, b = len(A), len(B)
    M = [[F(0)] * (a + b) for _ in range(a + b)]
    for i in range(a):
        for j in range(a):
            M[i][j] = F(A[i][j])
    for i in range(b):
        for j in range(b):
            M[a + i][a + j] = F(B[i][j])
    return M


def sig2(M):
    p, q, z = GA.congruence_signature(M)
    return (p, q, z)


# --------------------------------------------------------------------------------------------
def check_corank_one_differential_is_delta():
    """(T3) <=> d det G != 0 at a corank-one point: adj(G0) = c k k^T with c != 0, and the
    t-derivative of det(G0 + tH) is c * H(k, k) = c * delta(k (x) k) for every direction H."""
    premise("sheaf.invariant-form-t3")
    seen_zero_and_nonzero = set()
    for P in PS:
        P = GA.frac_matrix(P)
        for D in DS:
            Dm = [[F(D[i]) if i == j else F(0) for j in range(4)] for i in range(4)]
            G0 = GA.mat_mul(transpose(P), GA.mat_mul(Dm, P))      # cometric of corank one
            assert GA.mat_rank(G0) == 3
            # radical covector k: G0 k = 0 (P^{-1} e_1 in this frame)
            adj = adjugate(G0)
            # adj(G0) has rank one and is c k k^T: pick a nonzero column as k
            col = next(j for j in range(4) if any(adj[i][j] != 0 for i in range(4)))
            k = [adj[i][col] for i in range(4)]
            assert all(sum(G0[i][j] * k[j] for j in range(4)) == 0 for i in range(4))
            kk = [[k[i] * k[j] for j in range(4)] for i in range(4)]
            # c from one nonzero entry, then the whole matrix must agree
            i0 = next(i for i in range(4) if k[i] != 0)
            c = adj[i0][i0] / kk[i0][i0]
            assert c != 0
            assert all(adj[i][j] == c * kk[i][j] for i in range(4) for j in range(4))
            for H in HS + [G0]:            # G0 itself is a direction with H(k, k) = 0
                H = GA.frac_matrix(H)
                d1 = coef(pdet(line_matrix(G0, H)), 1)
                Hkk = sum(k[i] * H[i][j] * k[j] for i in range(4) for j in range(4))
                assert d1 == c * Hkk
                seen_zero_and_nonzero.add(Hkk == 0)
    # both cases occur: directions with delta = 0 (non-transverse) and delta != 0
    assert seen_zero_and_nonzero == {True, False}
    return True


def G_cone(x, B):
    """The corank-two model: A(x) = [[x1, x2], [x2, x3]] beside a nondegenerate block B."""
    x1, x2, x3 = x[0], x[1], x[2]
    return block([[x1, x2], [x2, x3]], B)


def check_transverse_corank_two_three_signatures():
    """At a transverse corank-two point three signatures meet; next to (1,3) the third is (2,2)."""
    premise("sheaf.invariant-form-t3")
    for B, expected in CONE_CASES:
        assert GA.mat_rank(G_cone([0, 0, 0, 0], B)) == 2
        found = set()
        for e in SCALES:
            for pt in sample_points(e):
                s = sig2(G_cone([F(a) for a in pt], B))
                if s[2] == 0:
                    found.add(s)
            # all three signatures occur at every scale e
            scale = {sig2(G_cone([F(a) for a in pt], B)) for pt in sample_points(e)[:3]}
            assert scale == expected
        assert found == expected
    # this world's signature (1,3) next to a transverse corank-two point always brings (2,2)
    for B, _ in CONE_CASES[:2]:
        sigs = {sig2(G_cone([F(a) for a in pt], B))[:2] for pt in sample_points(F(1))[:3]}
        assert THIS_WORLD in sigs and TWO_TIME in sigs
    # corank r: r + 1 signatures, r = 1, 2, 3 (diagonal sample of a neighbourhood of 0 in Sym_r)
    for r in (1, 2, 3):
        sigs = set()
        for signs in product((-1, 1), repeat=r):
            A = [[F(signs[i], 7) if i == j else F(0) for j in range(r)] for i in range(r)]
            sigs.add(sig2(block(A, [[-1]]))[:2])
        assert len(sigs) == r + 1
    return True


def check_cone_is_not_a_hypersurface():
    """det G vanishes to second order at the corank-two point (every line through it has zero
    linear coefficient), and the zero set contains lines through 0 spanning all of R^4, so it is
    not a smooth hypersurface there: (T1) and (T2) both fail."""
    premise("sheaf.invariant-form-t3")
    B = CONE_CASES[0][0]
    quad_nonzero = False
    for v in DIRS:
        # G_cone is linear in x, so G(t v) = t * G_cone(v) on the A block; B block is constant
        M = [[GA.ptrim([F(0), F(G_cone(list(v), B)[i][j])]) if (i < 2 and j < 2)
              else GA.pconst(F(G_cone(list(v), B)[i][j])) for j in range(4)] for i in range(4)]
        p = pdet(M)
        assert coef(p, 0) == 0 and coef(p, 1) == 0
        quad_nonzero = quad_nonzero or coef(p, 2) != 0
    assert quad_nonzero
    for v in LINES:
        for t in TS:
            assert det(G_cone([t * a for a in v], B)) == 0
    assert GA.rank_of_vectors([[F(a) for a in v] for v in LINES]) == 4
    # the corank-two locus is the x4-line (codimension three)
    for t in TS:
        assert GA.mat_rank(G_cone([0, 0, 0, t], B)) == 2
    return True


def check_corank_two_point_survives_perturbation():
    """Every perturbation in two exact families keeps a corank-two point within O(eps) of 0."""
    premise("sheaf.invariant-form-t3")
    B = GA.frac_matrix([[-1, 0], [0, -1]])
    for H in PERTS:
        H = GA.frac_matrix(H)
        for eps in (F(1, 10), F(1, 100), F(1, 1000)):
            # Schur complement of the perturbed B-block
            Bp = [[B[i][j] + eps * H[2 + i][2 + j] for j in range(2)] for i in range(2)]
            dB = Bp[0][0] * Bp[1][1] - Bp[0][1] * Bp[1][0]
            assert dB != 0
            Binv = [[Bp[1][1] / dB, -Bp[0][1] / dB], [-Bp[1][0] / dB, Bp[0][0] / dB]]
            C = [[eps * H[i][2 + j] for j in range(2)] for i in range(2)]
            CBC = GA.mat_mul(C, GA.mat_mul(Binv, transpose(C)))
            target = [[-(eps * H[i][j] - CBC[i][j]) for j in range(2)] for i in range(2)]
            x = [target[0][0], target[0][1], target[1][1], F(0)]
            Gp = [[G_cone(x, B)[i][j] + eps * H[i][j] for j in range(4)] for i in range(4)]
            assert GA.mat_rank(Gp) == 2
            assert all(abs(c) <= 10 * eps for c in x)
    # position-dependent perturbation A(x) + eps L(x): the corank-two line persists
    L = LPERT                                      # x_A -> x_A + eps L x_A + eps (1, 1, 1) x4
    for eps in (F(1, 10), F(1, 100)):
        for x4 in (F(0), F(1), F(-2)):
            M = [[(F(1) if i == j else F(0)) + eps * L[i][j] for j in range(3)] for i in range(3)]
            rhs = [-eps * x4] * 3
            sol = GA.field_solve(M, rhs)
            xa = list(sol)
            Ax = [xa[i] + eps * sum(L[i][j] * xa[j] for j in range(3)) + eps * x4 for i in range(3)]
            assert all(a == 0 for a in Ax)
            Gp = block([[Ax[0], Ax[1]], [Ax[1], Ax[2]]], B)
            assert GA.mat_rank(Gp) == 2
    return True


def check_tame_wall_is_two_signature():
    """A transverse corank-one wall separates exactly two signatures, differing by one swap."""
    premise("sheaf.invariant-form-t3")
    for rest in RESTS:
        s_plus = sig2(block([[EPS1]], rest))
        s_minus = sig2(block([[-EPS1]], rest))
        assert s_plus[2] == 0 and s_minus[2] == 0
        assert s_plus[0] - s_minus[0] == 1 and s_minus[1] - s_plus[1] == 1
        assert sig2(block([[F(0)]], rest))[2] == 1
    return True


if __name__ == "__main__":
    for f in (check_corank_one_differential_is_delta, check_transverse_corank_two_three_signatures,
              check_cone_is_not_a_hypersurface, check_corank_two_point_survives_perturbation,
              check_tame_wall_is_two_signature):
        print(f.__name__, f())
