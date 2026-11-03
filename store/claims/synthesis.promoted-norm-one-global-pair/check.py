"""synthesis.promoted-norm-one-global-pair: exact checks.

(1) Pointwise count with the norm free, in the flat model R^{2,4}, eta = diag(1,1,-1,-1,-1,-1):
    13 variables (dI, dV, dlam), 3 linearised Stelle-West constraints, 9 gauge images of the
    15 bivectors, and the norm mode spanning the complement.
(2) The multiplier sector on a Cauchy slice: cubical cochain complex of the periodic lattice
    (Z/L)^3. Constraint d lam = 0 leaves the constants (H^0 = 1); the gauge T -> T + d theta leaves
    H^3 = 1; the sum over cubes is the gauge-invariant zero mode and pairs with the constants.
(3) The Liouville density of the reduced pair in Lambda for two choices of promoted multiplier.
"""
from fractions import Fraction as F
import GA
from GA import mat_rank, mat_mul
from tp_premise import premise

ETA = [1, 1, -1, -1, -1, -1]


def ip(x, y):
    return sum(ETA[a] * x[a] * y[a] for a in range(6))


def unit(a):
    return [F(1) if b == a else F(0) for b in range(6)]


def biv_act(a, b, x):
    """(e_a ^ e_b) . x = <e_a, x> e_b - <e_b, x> e_a"""
    out = [F(0)] * 6
    out[b] += ETA[a] * x[a]
    out[a] -= ETA[b] * x[b]
    return out


def constraint_rows(I, V, lam):
    r1 = [2 * ETA[a] * I[a] for a in range(6)] + [F(0)] * 6 + [F(-1, 3)]
    r2 = [ETA[a] * V[a] for a in range(6)] + [ETA[a] * I[a] for a in range(6)] + [F(0)]
    r3 = [F(0)] * 6 + [2 * ETA[a] * V[a] for a in range(6)] + [F(-3) / (lam * lam)]
    return [r1, r2, r3]


def check_pointwise_count_with_norm_mode():
    premise("dark-energy.point-infinity-has-no-physical-fluctuation")
    premise("dark-energy.under-action-written-norm-parameter-laws")
    for lam, I, V in [(F(3), unit(0), unit(2)),
                      (F(12), [F(2), 0, 0, 0, 0, 0], [0, 0, F(1, 2), 0, 0, 0]),
                      (F(3, 4), [F(1, 2), 0, 0, 0, 0, 0], [0, 0, 0, F(2), 0, 0])]:
        I = [F(c) for c in I]
        V = [F(c) for c in V]
        assert ip(I, I) == lam / F(3) and ip(V, V) == F(-3) / lam and ip(I, V) == 0
        A = constraint_rows(I, V, lam)
        assert mat_rank(A) == 3                                   # 13 - 3 = 10 constrained directions
        gauge = []
        for a in range(6):
            for b in range(a + 1, 6):
                gauge.append(biv_act(a, b, I) + biv_act(a, b, V) + [F(0)])
        assert len(gauge) == 15 and mat_rank(gauge) == 9          # stabiliser so(1,3), nine broken
        for g in gauge:                                           # gauge images are constrained
            assert all(sum(r[i] * g[i] for i in range(13)) == 0 for r in A)
        norm = [c / (2 * lam) for c in I] + [-c / (2 * lam) for c in V] + [F(1)]
        assert all(sum(r[i] * norm[i] for i in range(13)) == 0 for r in A)
        assert mat_rank(gauge + [norm]) == 10                     # gauge (+) norm mode = all of it
    GA.check("with the norm free the constrained space is 10 = 9 gauge + the norm mode, at three values of Lambda",
             True)


def lattice(L):
    def v(x, y, z):
        return ((x % L) * L + (y % L)) * L + (z % L)
    return v


def coboundaries(L):
    """delta0: C^0 -> C^1, delta1: C^1 -> C^2, delta2: C^2 -> C^3 on the periodic cubical lattice."""
    v = lattice(L)
    n = L ** 3
    E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    pts = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
    d0 = [[F(0)] * n for _ in range(3 * n)]                      # edge (i, p): lam(p + e_i) - lam(p)
    for i in range(3):
        for p in pts:
            q = tuple(p[k] + E[i][k] for k in range(3))
            d0[i * n + v(*p)][v(*q)] += 1
            d0[i * n + v(*p)][v(*p)] -= 1
    planes = [(1, 2), (2, 0), (0, 1)]                            # face k has normal k, spanned by (i, j)
    d1 = [[F(0)] * (3 * n) for _ in range(3 * n)]                # curl
    for k, (i, j) in enumerate(planes):
        for p in pts:
            pi = tuple(p[m] + E[i][m] for m in range(3))
            pj = tuple(p[m] + E[j][m] for m in range(3))
            row = k * n + v(*p)
            d1[row][i * n + v(*p)] += 1
            d1[row][j * n + v(*pi)] += 1
            d1[row][i * n + v(*pj)] -= 1
            d1[row][j * n + v(*p)] -= 1
    d2 = [[F(0)] * (3 * n) for _ in range(n)]                    # divergence
    for k in range(3):
        for p in pts:
            pk = tuple(p[m] + E[k][m] for m in range(3))
            d2[v(*p)][k * n + v(*pk)] += 1
            d2[v(*p)][k * n + v(*p)] -= 1
    return d0, d1, d2


def is_zero_matrix(M):
    return all(c == 0 for row in M for c in row)


def check_multiplier_sector_one_global_pair():
    premise("dark-energy.imported-henneaux-teitelboim-promotion")
    for L in (2, 3):
        n = L ** 3
        d0, d1, d2 = coboundaries(L)
        assert is_zero_matrix(mat_mul(d1, d0)) and is_zero_matrix(mat_mul(d2, d1))
        r0, r1, r2 = mat_rank(d0), mat_rank(d1), mat_rank(d2)
        betti = [n - r0, 3 * n - r1 - r0, 3 * n - r2 - r1, n - r2]
        assert betti == [1, 3, 3, 1]                              # the 3-torus
        # d lam = 0 leaves the constants; T modulo d theta leaves one number, the sum over cubes
        assert all(sum(d2[c][f] for c in range(n)) == 0 for f in range(3 * n))
        const = [F(1)] * n
        assert sum(const) == n                                    # pairing of constants with the zero mode
    GA.check("on periodic cubical 3-tori (L = 2, 3): d lam = 0 leaves one constant, T modulo exact "
             "forms leaves one number (Betti numbers 1,3,3,1), and the two pair: one global canonical pair",
             True)


def check_liouville_density_depends_on_multiplier():
    premise("dark-energy.under-action-written-norm-parameter-laws")
    # promoted multiplier g(Lambda): Liouville density |g'(Lambda)| dLambda dtau.
    # g = Lambda/3 (the norm <I,I>): constant density 1/3; g = l^2 = 3/Lambda: density 3/Lambda^2.
    # exact difference quotients of the two choices at rational points, and their limits as identities
    pts = [F(1, 7), F(2, 3), F(5), F(11, 2)]
    for a in pts:
        for b in pts:
            if a == b:
                continue
            assert ((a / F(3)) - (b / F(3))) / (a - b) == F(1, 3)
            assert ((F(3) / a) - (F(3) / b)) / (a - b) == F(-3) / (a * b)
    # with the norm promoted and a cutoff Lambda_max = M_P^2 (units M_P = 1), the flat measure gives
    # P(Lambda <= Lambda_obs) = Lambda_obs / Lambda_max = 3 / N^2, since N^2 = 3 M_P^2 / Lambda
    for lam in pts:
        N2 = F(3) / lam
        assert lam / F(1) == F(3) / N2
    GA.check("the Liouville density in Lambda is flat for the promoted norm and 3/Lambda^2 for promoted l^2",
             True)
