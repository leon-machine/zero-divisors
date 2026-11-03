"""synthesis.univalence-even-extension-split: exact checks.

Boundary modes in the Jordan-Wigner representation over the rationals: one mode is Mat_2 with
v = |0><1| (so v* v = n), parity P = diag(1, -1); two modes are Mat_4 with v1 = v (x) 1,
v2 = P (x) v, total parity Gamma = P (x) P. The Killing flow at imaginary time ip acts on the
matrix unit E_ij of one mode by r^(j - i), r = e^{p omega} kept rational (r = 1 is zero weight).
"""
from fractions import Fraction as F
from itertools import product
import GA
from tp_premise import premise

# data (module level so that the mutation test perturbs the structural integers)
RS = [F(1), F(2), F(1, 3), F(7, 2), F(10)]
CS = [F(1, 7), F(-1, 9), F(1, 20)]
RHO_GENERIC = [[F(4, 10), F(1, 10), F(0), F(1, 20)],
               [F(1, 10), F(3, 10), F(1, 30), F(0)],
               [F(0), F(1, 30), F(2, 10), F(1, 40)],
               [F(1, 20), F(0), F(1, 40), F(1, 10)]]


def _premises():
    premise("singularity.imported-univalence-superselection-rule")
    premise("singularity.descended-form-state-independent")


def mm(A, B):
    return GA.mat_mul(A, B)


def kron(A, B):
    return [[A[i // len(B)][j // len(B)] * B[i % len(B)][j % len(B)]
             for j in range(len(A) * len(B))] for i in range(len(A) * len(B))]


def tr(A):
    return sum(A[i][i] for i in range(len(A)))


def add(A, B, c=F(1)):
    return [[A[i][j] + c * B[i][j] for j in range(len(A))] for i in range(len(A))]


def unit(i, j, n=2):
    return [[F(1) if (a, b) == (i, j) else F(0) for b in range(n)] for a in range(n)]


I2 = [[F(1), F(0)], [F(0), F(1)]]
V = unit(0, 1)
VS = unit(1, 0)
P = [[F(1), F(0)], [F(0), F(-1)]]
X = add(V, VS)


def psd(M):
    p, q, z = GA.congruence_signature(M)
    return q == 0


def gibbs(r):
    """Single-mode Gibbs state of the number operator: occupation n = 1/(r + 1)."""
    n = 1 / (r + 1)
    return [[1 - n, F(0)], [F(0), n]], n


def flow_ip(i, j, r):
    """alpha_{ip}(E_ij) = r^(j - i) E_ij for the Killing flow of one mode."""
    return r ** (j - i)


def kms_residuals(rho, r, pairs):
    """omega(a alpha_{ip}(b)) - omega(b a) over the given pairs of matrix units."""
    out = []
    for (a, b) in pairs:
        A, B = unit(*a), unit(*b)
        lhs = flow_ip(b[0], b[1], r) * tr(mm(rho, mm(A, B)))
        rhs = tr(mm(rho, mm(B, A)))
        out.append(lhs - rhs)
    return out


UNITS = [(0, 0), (0, 1), (1, 0), (1, 1)]
PRODUCT_CASES = [(F(2), F(1, 7)), (F(7, 2), F(1, 20))]
R_EVEN = F(1, 3)
TWO = 2
C_SECOND = F(1, 9)
LADDER = [(0, 1), (1, 0)]          # v = E_01, v* = E_10


def check_even_part_is_unique_even_extension():
    """(i) omega o E is a state, even, equal to omega on the even part; E = (id + Ad Gamma)/2."""
    _premises()
    G = kron(P, P)
    rho = RHO_GENERIC
    assert psd(rho) and tr(rho) == 1
    rho_plus = [[(rho[i][j] + mm(G, mm(rho, G))[i][j]) / 2 for j in range(4)] for i in range(4)]
    assert psd(rho_plus) and tr(rho_plus) == 1
    # rho itself is not even: some odd expectation is nonzero
    odd_nonzero = False
    for i, j in product(range(4), repeat=2):
        E = unit(i, j, 4)
        parity = mm(G, mm(E, G))
        even = parity == E
        odd = parity == [[-x for x in row] for row in E]
        assert even or odd
        if even:
            assert tr(mm(rho_plus, E)) == tr(mm(rho, E))
        else:
            assert tr(mm(rho_plus, E)) == 0
            odd_nonzero = odd_nonzero or tr(mm(rho, E)) != 0
    assert odd_nonzero
    # uniqueness: an even state is fixed by Ad Gamma, so two even states equal on the even part
    # coincide; here: rho_plus is the even part of itself
    assert mm(G, mm(rho_plus, G)) == rho_plus
    return True


def check_ladder_kms_admits_coherence():
    """(ii) (R) as stated (ladder pairs only) holds for the coherent non-even marginal."""
    _premises()
    tested = 0
    for r in RS:
        g, n = gibbs(r)
        for c in CS:
            if c * c > n * (1 - n):
                continue
            tested += 1
            rho = [[1 - n, c], [c, n]]
            assert psd(rho)
            assert all(x == 0 for x in kms_residuals(rho, r, [(a, b) for a in LADDER for b in LADDER]))
            assert tr(mm(rho, V)) == c and c != 0          # omega(v) != 0: (P) fails
            # the descended (pinched) marginal is the Gibbs state
            assert [[rho[0][0], F(0)], [F(0), rho[1][1]]] == g
            # but full-algebra KMS fails for this state
            assert any(x != 0 for x in kms_residuals(rho, r, [(a, b) for a in UNITS for b in UNITS]))
    assert tested >= len(RS)
    return True


def check_full_kms_forces_single_mode_evenness():
    """(iii) Full-algebra KMS on one mode forces the Gibbs state, hence omega(v) = 0, at every
    weight, zero weight (r = 1, tracial) included: solve the linear KMS system exactly."""
    _premises()
    for r in RS:
        # unknown rho = [[a, b], [c, d]]: each KMS residual is linear in (a, b, c, d)
        rows = []
        for (p, q) in product(UNITS, repeat=2):
            row = []
            for (i, j) in UNITS:
                e = unit(i, j)
                row.append(kms_residuals(e, r, [(p, q)])[0])
            rows.append(row)
        rows.append([F(1), F(0), F(0), F(1)])          # trace one
        assert GA.mat_rank(rows) == 4                   # unique solution
        g, n = gibbs(r)
        sol = [g[0][0], g[0][1], g[1][0], g[1][1]]
        for row in rows[:-1]:
            assert sum(x * y for x, y in zip(row, sol)) == 0
        assert sol[1] == 0 and sol[2] == 0
    assert gibbs(F(1))[1] == F(1, 2)
    return True


def check_cross_mode_odd_correlation_with_even_gibbs_marginals():
    """(iv) Two modes: every single-mode marginal is an even Gibbs state, the state is not even."""
    _premises()
    G = kron(P, P)
    v1, v2 = kron(V, I2), kron(P, V)
    # CAR relations
    def acomm(A, B):
        return add(mm(A, B), mm(B, A))
    zero = [[F(0)] * 4 for _ in range(4)]
    one = [[F(1) if i == j else F(0) for j in range(4)] for i in range(4)]
    assert acomm(v1, v2) == zero and acomm(v1, [list(r) for r in zip(*v2)]) == zero
    assert acomm(v1, [list(r) for r in zip(*v1)]) == one
    odd = kron(X, P)                                     # (v1 + v1*) times the mode-2 parity
    assert mm(G, mm(odd, G)) == [[-x for x in row] for row in odd]
    for r1, r2, c in [(RS[1], RS[2], CS[2]), (RS[0], RS[3], -CS[2]), (RS[4], RS[1], CS[2])]:
        g1, _ = gibbs(r1)
        g2, _ = gibbs(r2)
        rho = add(kron(g1, g2), odd, c)
        assert psd(rho)
        assert tr(rho) == 1
        assert tr(mm(rho, odd)) == 4 * c != 0
        # marginal on mode 1: algebra spanned by E_ij (x) 1
        for i, j in product(range(2), repeat=2):
            assert tr(mm(rho, kron(unit(i, j), I2))) == g1[j][i]
        # marginal on mode 2: algebra generated by v2 = P (x) v, spanned by 1, n2, v2, v2*
        n2 = kron(I2, unit(1, 1))
        assert tr(mm(rho, v2)) == 0 and tr(mm(rho, [list(r) for r in zip(*v2)])) == 0
        assert tr(mm(rho, n2)) == g2[1][1]
    return True


def mode2_basis():
    """Basis of the mode-2 algebra in the Jordan-Wigner representation: 1 (x) E_kk, P (x) E_kl."""
    return [kron(I2, unit(0, 0)), kron(I2, unit(1, 1)), kron(P, unit(0, 1)), kron(P, unit(1, 0))]


def check_graded_product_has_one_odd_factor_at_most():
    """(v) Odd elements of disjoint modes anticommute, so a product state cannot be non-even on
    both factors: omega(x y) = omega(x) omega(y) = -omega(y x) forces omega(x) omega(y) = 0.
    Positive case: one coherent factor beside an even one is a product over all 16 cross-mode
    pairs. Negative case: two coherent factors violate the product property on (x, y)."""
    _premises()
    x = kron(X, I2)                                     # odd, mode 1
    y = kron(P, X)                                      # odd, mode 2 (v2 + v2*)
    assert mm(x, y) == [[-a for a in row] for row in mm(y, x)]
    for r1, c1 in PRODUCT_CASES:
        _, n1 = gibbs(r1)
        rho1 = [[1 - n1, c1], [c1, n1]]
        assert psd(rho1)
        w_x = tr(mm(rho1, X))
        assert w_x == TWO * c1 != 0
        # one odd factor with an even partner: a product state over all 16 cross-mode pairs
        g2, _ = gibbs(R_EVEN)
        rho = kron(rho1, g2)
        assert psd(rho)
        pairs = 0
        for i in range(2):
            for j in range(2):
                a = kron(unit(i, j), I2)
                for b in mode2_basis():
                    assert tr(mm(rho, mm(a, b))) == tr(mm(rho, a)) * tr(mm(rho, b))
                    pairs += 1
        assert pairs == 16
        assert tr(mm(rho, mm(x, y))) == 0 == tr(mm(rho, mm(y, x)))
        # two coherent factors: the product property fails on (x, y)
        _, n2 = gibbs(R_EVEN)
        rho2 = [[1 - n2, C_SECOND], [C_SECOND, n2]]
        assert psd(rho2)
        both = kron(rho1, rho2)
        assert psd(both)
        wx, wy, wxy = tr(mm(both, x)), tr(mm(both, y)), tr(mm(both, mm(x, y)))
        assert wx == TWO * c1 and wy == (1 - TWO * n1) * TWO * C_SECOND
        assert wxy == 0 and wx * wy != wxy
    return True
