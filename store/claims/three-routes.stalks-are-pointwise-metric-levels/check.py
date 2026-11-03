"""three-routes.stalks-are-pointwise-metric-levels: exact checks in a smooth family of single-mode fibres.

Fibre A_x = Mat_2 with ladder v = [[0,1],[0,0]], v* = v^T and parity sigma = v* v - v v* = diag(-1, 1), moved
smoothly along a base coordinate x by the polynomial conjugation g_x = [[1, x], [0, 1]]:
sigma_x = g_x sigma g_x^{-1}, entries polynomial in x. The point's grading is alpha_x = Ad(sigma_x).
(1) The projection P_x(a) = (a + sigma_x a sigma_x)/2, as a 4 x 4 matrix of rational functions of x, is
idempotent identically in x (P_x^2 = P_x), has polynomial entries (a smooth bundle map), and rank 2 at six sample
points: A^+ is a locally trivial subbundle, framed by the smooth sections 1 and sigma_x.
(2) Its range at each sample is the even part A_x^+ = {a : alpha_x(a) = a} = span{1, sigma_x}, and its kernel is
the odd part (alpha_x = -1), span{g_x v g_x^{-1}, g_x v* g_x^{-1}}: P_x is the descent E(a) = (a + sigma a sigma)/2
of the premise, at each point.
(3) A local section a(x) of A^+ (a germ) is f(x) 1 + h(x) sigma_x: for two polynomial families, P applied to a
family with odd admixture returns exactly its even germ; the stalk's algebra fibre at x is A_x^+.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

X = GA.RF.var()
XS = (F(0), F(1, 2), F(-1), F(2), F(-3, 4), F(5))


def C(x):
    return GA.RF.const(F(x))


def m2(A, B):
    return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)] for i in range(2)]


def madd(A, B, c):
    return [[A[i][j] + c * B[i][j] for j in range(2)] for i in range(2)]


G = [[GA.RF1, X], [GA.RF0, GA.RF1]]
GINV = [[GA.RF1, -X], [GA.RF0, GA.RF1]]
SIG0 = [[C(-1), GA.RF0], [GA.RF0, GA.RF1]]
V0 = [[GA.RF0, GA.RF1], [GA.RF0, GA.RF0]]
VD0 = [[GA.RF0, GA.RF0], [GA.RF1, GA.RF0]]


def conj(M):
    return m2(m2(G, M), GINV)


SIGX = conj(SIG0)
UNITS = [[[GA.RF1 if (i, j) == (r, c) else GA.RF0 for j in range(2)] for i in range(2)]
         for r in range(2) for c in range(2)]


def proj(a):
    return [[(a[i][j] + m2(m2(SIGX, a), SIGX)[i][j]) * C(F(1, 2)) for j in range(2)] for i in range(2)]


def flat(M):
    return [M[0][0], M[0][1], M[1][0], M[1][1]]


def pmatrix():
    cols = [flat(proj(E)) for E in UNITS]
    return [[cols[c][r] for c in range(4)] for r in range(4)]


def check_projection_is_smooth_idempotent_constant_rank():
    premise("singularity.descent-parity-average")
    ok = True
    Pm = pmatrix()
    sq = [[sum((Pm[i][t] * Pm[t][j] for t in range(4)), GA.RF0) for j in range(4)] for i in range(4)]
    ok = ok and all(sq[i][j].eqrf(Pm[i][j]) for i in range(4) for j in range(4))
    ok = ok and all(len(Pm[i][j].den) == 1 for i in range(4) for j in range(4))
    ranks = [GA.mat_rank([[e.eval(x0) for e in row] for row in Pm]) for x0 in XS]
    ok = ok and ranks == [2] * 6
    # 1 and sigma_x frame the range at every point
    for x0 in XS:
        one = [F(1), F(0), F(0), F(1)]
        sg = [e.eval(x0) for e in flat(SIGX)]
        ok = ok and GA.rank_of_vectors([one, sg]) == 2
    GA.check("P_x = (id + alpha_x)/2 is a polynomial idempotent of constant rank 2: A^+ is locally trivial", ok)
    return ok


def check_range_is_even_part_kernel_odd_part():
    premise("singularity.descent-parity-average")
    ok = True
    vx, vdx = conj(V0), conj(VD0)
    for x0 in XS:
        Pm = [[e.eval(x0) for e in row] for row in pmatrix()]
        sg = [e.eval(x0) for e in flat(SIGX)]
        even = [[F(1), F(0), F(0), F(1)], sg]
        odd = [[e.eval(x0) for e in flat(vx)], [e.eval(x0) for e in flat(vdx)]]
        for a in even:
            ok = ok and [sum(Pm[i][j] * a[j] for j in range(4)) for i in range(4)] == a
        for a in odd:
            ok = ok and all(sum(Pm[i][j] * a[j] for j in range(4)) == 0 for i in range(4))
        # alpha_x acts as -1 on the odd part: sigma v sigma = -v
        sm = [[e.eval(x0) for e in row] for row in SIGX]
        vm = [[e.eval(x0) for e in row] for row in vx]
        svs = [[sum(sm[i][a] * vm[a][b] * sm[b][j] for a in range(2) for b in range(2)) for j in range(2)]
               for i in range(2)]
        ok = ok and svs == [[-vm[i][j] for j in range(2)] for i in range(2)]
        ok = ok and GA.rank_of_vectors(even + odd) == 4
    GA.check("the range of P_x is span{1, sigma_x} (alpha_x-fixed), the kernel the odd ladder sector", ok)
    return ok


# generic germs: (f, h, q) for a family f 1 + h sigma_x + q v_x
GERMS = ((C(2) + X, X * X, C(3)), (C(-1), C(F(1, 2)) * X, X))


def check_even_germs_are_the_stalk():
    premise("singularity.descent-parity-average")
    ok = True
    vx = conj(V0)
    for f, h, q in GERMS:
        even = madd([[f, GA.RF0], [GA.RF0, f]], SIGX, h)
        family = madd(even, vx, q)
        got = proj(family)
        ok = ok and all(got[i][j].eqrf(even[i][j]) for i in range(2) for j in range(2))
        # the odd remainder is q v_x, and the frame coordinates are f = tr(P a)/2, h = tr(sigma_x P a)/2
        rest = madd(family, got, C(-1))
        ok = ok and all(rest[i][j].eqrf(q * vx[i][j]) for i in range(2) for j in range(2))
        ok = ok and ((got[0][0] + got[1][1]) * C(F(1, 2))).eqrf(f)
        sg = m2(SIGX, got)
        ok = ok and ((sg[0][0] + sg[1][1]) * C(F(1, 2))).eqrf(h)
    GA.check("P takes a family to its even germ f 1 + h sigma_x: the stalk fibre is A_x^+", ok)
    return ok
