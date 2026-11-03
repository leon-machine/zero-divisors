"""sheaf.base-unipotents-wall: exact checks.

Two wall fibres. (a) GA: the degenerate Clifford algebra Cl(1,2,1), covectors at the wall point as
GA vectors with G = GA.dot, the radical spanned by k = e_3 (square 0); vectors u' are coordinate
lists paired with covectors by alpha(u') = sum alpha_i u'_i. (b) The Schwarzschild wall Gram on the
frame (rho, dt, mu_1, mu_2) at r = 0, [[m^2, -m, 0, 0], [-m, 1, 0, 0], 0, 0; diag(-1, -1)] with
m = 2, radical k = rho + m dt, as a rational matrix.
For lambda in ker k (sampled, and a basis of ker k), g_lambda(alpha) = alpha + alpha(lambda) k:
G(g alpha, g alpha') = G(alpha, alpha') on all basis pairs and samples; g_lambda k = k;
g_lambda g_lambda' = g_(lambda + lambda'); the dual action on vectors is u' -> u' - k(u') lambda
(checked as (g^-1 alpha)(u') = alpha(u' - k(u') lambda)); on transversals (k(u') = 1) it is translation
by -lambda, free (only lambda = 0 fixes a transversal) and transitive (any two transversals differ by
an element of ker k).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise  # noqa: F401  (self-contained lemma: no premises)

# (a) GA wall fibre: e_0 (+1), e_1, e_2 (-1), e_3 = k (0)
SQ = GA.sig(1, 2, 1)
N = 4
BASIS = [GA.gen(i) for i in range(N)]


def covector(c):
    return GA.add(*[GA.scal(c[i], BASIS[i]) for i in range(N)])


def coords(x):
    return [x.get((i,), F(0)) for i in range(N)]


def pair(alpha, u):
    return sum((a * b for a, b in zip(coords(alpha), u)), F(0))


K_GA = BASIS[3]
K_VEC_DUAL = [F(0), F(0), F(0), F(1)]          # k as a functional on vectors: k(u') = u'_3


def g_ga(lam, alpha):
    return GA.add(alpha, GA.scal(pair(alpha, lam), K_GA))


# ker k = {u : u_3 = 0}
KER_SAMPLES = [[F(1), F(0), F(0), F(0)], [F(0), F(2), F(-1), F(0)], [F(3, 2), F(-1), F(5), F(0)]]
ALPHA_SAMPLES = [covector([F(1), F(2), F(0), F(-1)]), covector([F(0), F(1, 3), F(4), F(2)]),
                 covector([F(-2), F(0), F(1), F(7)])] + BASIS
TRANSVERSALS = [[F(0), F(0), F(0), F(1)], [F(2), F(-1), F(3), F(1)], [F(1, 2), F(5), F(0), F(1)]]

# (b) the Schwarzschild wall Gram at r = 0, m = 2, in the frame (rho, dt, mu1, mu2)
M = F(2)
G_SCH = [[M * M, -M, F(0), F(0)], [-M, F(1), F(0), F(0)], [F(0), F(0), F(-1), F(0)], [F(0), F(0), F(0), F(-1)]]
K_SCH = [F(1), M, F(0), F(0)]                   # k = rho + m dt (covector coordinates)


def check_unipotents_are_isometries_fixing_k():
    ok = all(GA.dot(K_GA, x, SQ) == 0 for x in BASIS)                 # k spans the radical
    for lam in KER_SAMPLES:
        ok = ok and pair(K_GA, lam) == 0
        for a in ALPHA_SAMPLES:
            for b in ALPHA_SAMPLES:
                ok = ok and GA.dot(g_ga(lam, a), g_ga(lam, b), SQ) == GA.dot(a, b, SQ)
        ok = ok and GA.eq(g_ga(lam, K_GA), K_GA)
    # the Schwarzschild wall: k in the radical, and isometry of the matrix form
    ok = ok and GA.mat_mul(G_SCH, [[x] for x in K_SCH]) == [[F(0)]] * 4
    for lam in ([F(2), F(-1), F(0), F(0)], [F(0), F(0), F(1), F(3)], [F(4), F(-2), F(1, 2), F(0)]):
        # k(lambda) = lambda . K_SCH = 0 for these (rho-coefficient 1, dt-coefficient m)
        ok = ok and sum(a * b for a, b in zip(K_SCH, lam)) == 0
        g = [[F(int(i == j)) + K_SCH[i] * lam[j] for j in range(4)] for i in range(4)]
        gt = [list(r) for r in zip(*g)]
        ok = ok and GA.mat_mul(GA.mat_mul(gt, G_SCH), g) == G_SCH
        ok = ok and GA.mat_mul(g, [[x] for x in K_SCH]) == [[x] for x in K_SCH]
    GA.check("wall unipotents: g_lambda is a G-isometry and fixes k (GA fibre and Schwarzschild wall)", ok)
    return ok


def check_composition_and_translation_action():
    ok = True
    for lam in KER_SAMPLES:
        for lam2 in KER_SAMPLES:
            s = [a + b for a, b in zip(lam, lam2)]
            ok = ok and all(GA.eq(g_ga(lam, g_ga(lam2, a)), g_ga(s, a)) for a in ALPHA_SAMPLES)
        neg = [-x for x in lam]
        for a in ALPHA_SAMPLES:
            ok = ok and GA.eq(g_ga(neg, g_ga(lam, a)), a)                 # g_(-lambda) is the inverse
            for u in TRANSVERSALS + KER_SAMPLES:
                ku = sum(x * y for x, y in zip(K_VEC_DUAL, u))
                moved = [u[i] - ku * lam[i] for i in range(N)]
                ok = ok and pair(g_ga(neg, a), u) == pair(a, moved)
    # on transversals: translation by -lambda, free and transitive
    for u in TRANSVERSALS:
        ok = ok and u[3] == 1
        for lam in KER_SAMPLES:
            img = [u[i] - lam[i] for i in range(N)]
            ok = ok and img[3] == 1 and img != u
        for u2 in TRANSVERSALS:
            diff = [u[i] - u2[i] for i in range(N)]
            ok = ok and diff[3] == 0                                     # lambda = u - u2 in ker k
    GA.check("wall unipotents: g_lambda g_lambda' = g_(lambda + lambda'); dual action translates transversals", ok)
    return ok
