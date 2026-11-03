"""synthesis.point-spectrum-boost-admits-no-half-sided-translations: exact checks.

Exact Jordan-Wigner matrices and Fractions; no floating point.  Complex matrices P = X + iY
are handled as real pairs, so the equation [K, P] = i c P becomes the real linear system
[K, X] = -c Y, [K, Y] = c X.

(i)  on a window of three modes, for the weights of (Q) (-1, 0, 1, in units of kappa) and
     for positive weights (1, 2, 3), the boost generator K = sum omega_k N_k admits no
     nonzero P with [K, P] = i c P for c = 1, 2, 7 (the real system has full rank), while
     for c = 0 the solutions are the commutant of K, of dimension sum of squared
     multiplicities of the spectrum of K (pinned values 24 and 10);
(iv) the spectrum of ad K on the window is the set of differences of eigenvalues of K, real
     and, for the weights of (Q), integral: the flow returns to the identity at rapidity
     2 pi, so every orbit is periodic, hence relatively compact.
"""
from fractions import Fraction as F
import GA
from GA import rank_of_vectors, mat_mul
from tp_premise import premise

PREMISES = (
    "angle.imported-theorems-deliver-their-hypotheses",
    "hawking.imported-algebra-boundary-modes-car-algebra",
    "hawking.modular-structure-completed-pair",
    "singularity.modular-theory-matrix-factor-proved-outright",
)


def zeros(r, c):
    return [[F(0)] * c for _ in range(r)]


def eye(n):
    m = zeros(n, n)
    for i in range(n):
        m[i][i] = F(1)
    return m


def kron(a, b):
    ra, ca, rb, cb = len(a), len(a[0]), len(b), len(b[0])
    out = zeros(ra * rb, ca * cb)
    for i in range(ra):
        for j in range(ca):
            if a[i][j]:
                for k in range(rb):
                    for l in range(cb):
                        out[i * rb + k][j * cb + l] = a[i][j] * b[k][l]
    return out


LOW = [[F(0), F(1)], [F(0), F(0)]]
ZZ = [[F(1), F(0)], [F(0), F(-1)]]


def jw(n):
    cs = []
    for i in range(n):
        m = [[F(1)]]
        for k in range(n):
            m = kron(m, ZZ if k < i else (LOW if k == i else eye(2)))
        cs.append(m)
    return cs


def boost(weights):
    n = len(weights)
    cs = jw(n)
    d = 2 ** n
    K = zeros(d, d)
    for w, c in zip(weights, cs):
        N = mat_mul([list(r) for r in zip(*c)], c)
        for i in range(d):
            K[i][i] += w * N[i][i]
    return K


def ad_rows(K):
    # K is diagonal: ad K acts on the matrix unit E_ab by (K_aa - K_bb)
    d = len(K)
    return [K[a][a] - K[b][b] for a in range(d) for b in range(d)]


def solution_dim(K, c):
    # unknowns (X_ab, Y_ab); equations (K_aa - K_bb) X_ab + c Y_ab = 0,
    #                                   (K_aa - K_bb) Y_ab - c X_ab = 0
    lam = ad_rows(K)
    m = len(lam)
    rows = []
    for idx, l in enumerate(lam):
        r1 = [F(0)] * (2 * m)
        r1[idx] = l
        r1[m + idx] = F(c)
        r2 = [F(0)] * (2 * m)
        r2[m + idx] = l
        r2[idx] = F(-c)
        rows.append(r1)
        rows.append(r2)
    return 2 * m - rank_of_vectors(rows)


def check_no_dilated_generator_on_windows():
    premise("hawking.imported-algebra-boundary-modes-car-algebra")
    premise("angle.imported-theorems-deliver-their-hypotheses")
    ok = True
    for weights, commutant in (((F(-1), F(0), F(1)), 24), ((F(1), F(2), F(3)), 10)):
        K = boost(weights)
        for c in (1, 2, 7):
            ok = ok and solution_dim(K, c) == 0
        # c = 0: real and imaginary parts each range over the commutant
        ok = ok and solution_dim(K, 0) == 2 * commutant
        spec = [K[i][i] for i in range(len(K))]
        ok = ok and sum(spec.count(v) ** 2 for v in set(spec)) == commutant
    GA.check("(i) no nonzero P with [K, P] = i c P (c != 0) on a window; at c = 0 the "
             "solutions are the commutant", ok)
    return ok


def check_point_spectrum_and_recurrence():
    premise("hawking.modular-structure-completed-pair")
    premise("hawking.imported-algebra-boundary-modes-car-algebra")
    premise("singularity.modular-theory-matrix-factor-proved-outright")
    K = boost((F(-1), F(0), F(1)))
    lam = ad_rows(K)
    ok = sorted(set(lam)) == [F(v) for v in range(-2, 3)]
    ok = ok and all(v.denominator == 1 for v in lam)
    # odd half-integer weights: ad K is integral exactly on even matrix units, so the flow
    # at rapidity 2 pi is the parity automorphism
    Kh = boost((F(1, 2), F(3, 2), F(5, 2)))
    lamh = ad_rows(Kh)
    d = len(Kh)
    par = [bin(a).count("1") + bin(b).count("1") for a in range(d) for b in range(d)]
    ok = ok and all((2 * v).denominator == 1 for v in lamh) and max(lamh) == F(9, 2)
    ok = ok and (len(lamh) == len(par) and all((v.denominator == 1) == (p % 2 == 0) for v, p in zip(lamh, par)))
    GA.check("(iv) ad K has real point spectrum on windows; for the weights of (Q) it is "
             "integral, so the flow is periodic at rapidity 2 pi", ok)
    return ok


def run():
    return all([check_no_dilated_generator_on_windows(), check_point_spectrum_and_recurrence()])


if __name__ == "__main__":
    import sys
    sys.exit(0 if run() else 1)
