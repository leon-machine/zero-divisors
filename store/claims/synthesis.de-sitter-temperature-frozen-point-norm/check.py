"""synthesis.de-sitter-temperature-frozen-point-norm: exact checks.

The gluing equation of (R_Lambda) on one CAR mode, its unique solution and the failure of
the boundary cases, the Gibbs and KMS forms, and the rate kappa^2 = B^2 = <I,I> in both
signs of the ambient form. r stands for exp(p omega) > 0, kept rational; the period
p = 2 pi / kappa enters only through r, so beta H = 2 pi is the identity kappa = H, checked as
B^2 = h^2 = <I,I>.
"""
from fractions import Fraction as F
import GA
from GA import mul, add, sub, scal, sc, gen, eq
from tp_premise import premise

RS = [F(3), F(1, 2), F(7, 5), F(41, 3), F(1, 9)]
HS = [F(1, 2), F(1), F(3), F(2, 7)]


def mat(a, b, c, d):
    return [[a, b], [c, d]]


mm = GA.mat_mul


def tr(A):
    return A[0][0] + A[1][1]


def check_de_sitter_temperature():
    premise("synthesis.cosmological-horizon-completed-pair")
    premise("singularity.p-univalence")                         # the marginal is diagonal
    premise("synthesis.r-lambda-regularity-cosmological-horizon")   # the gluing r n = 1 - n
    premise("synthesis.de-sitter-static-boost-frozen-point")
    premise("singularity.ascended-marginals-are-diagonal")
    premise("singularity.descended-form-state-independent")
    premise("singularity.kms-uniqueness-factor")
    # one mode in the number basis {|0>, |1>}: v = |0><1|, v* = |1><0|, N = v* v
    v = mat(F(0), F(1), F(0), F(0))
    vs = mat(F(0), F(0), F(1), F(0))
    one = mat(F(1), F(0), F(0), F(1))
    assert mm(v, v) == mat(F(0), F(0), F(0), F(0))
    s = [[mm(v, vs)[i][j] + mm(vs, v)[i][j] for j in range(2)] for i in range(2)]
    assert s == one
    for r in RS:
        # the gluing r n = 1 - n has the unique solution n = 1/(r + 1)
        n = 1 / (r + 1)
        assert r * n == 1 - n and 0 < n < 1
        for bad in (F(0), F(1, 2)):
            assert (r * bad == 1 - bad) == (r == 1)
        # the marginal diag(1 - n, n) is diag(1, 1/r)/(1 + 1/r) = exp(-p omega K)/Z
        rho = mat(1 - n, F(0), F(0), n)
        assert rho == mat(1 / (1 + 1 / r), F(0), F(0), (1 / r) / (1 + 1 / r))
        # KMS at inverse temperature p for alpha_t(v) = e^{-i t omega} v:
        # omega(a alpha_{i p}(b)) = omega(b a), with alpha_{ip}(v) = r v, alpha_{ip}(v*) = v*/r
        assert tr(mm(rho, mm(vs, scal_m(r, v)))) == tr(mm(rho, mm(v, vs)))
        assert tr(mm(rho, mm(v, scal_m(1 / r, vs)))) == tr(mm(rho, mm(vs, v)))
        # uniqueness: a diagonal state diag(1 - m, m) satisfies the first relation only at m = n
        for m in (F(1, 7), F(2, 3), n):
            rm = mat(1 - m, F(0), F(0), m)
            ok = tr(mm(rm, mm(vs, scal_m(r, v)))) == tr(mm(rm, mm(v, vs)))
            assert ok == (m == n)
    # the rate: kappa^2 = B^2 = <I,I> = L/3, in both signs of the ambient form, and beta H = 2 pi
    sq = (1, -1, -1, -1, 1, -1)
    mirror = tuple(-x for x in sq)
    n0 = scal(F(1, 2), add(gen(4), gen(5)))
    ninf = sub(gen(4), gen(5))
    for h in HS:
        L = 3 * h * h
        I = add(ninf, scal(L / 6, n0))
        W = sub(ninf, scal(L / 6, n0))
        for form in (sq, mirror):
            B = mul(gen(0), W, form)
            assert eq(mul(B, B, form), sc(h * h))
        II = add(mul(I, I, sq), mul(I, I, sq)).get((), F(0)) / 2
        assert II == h * h
    return True


def scal_m(c, A):
    return [[c * x for x in row] for row in A]
