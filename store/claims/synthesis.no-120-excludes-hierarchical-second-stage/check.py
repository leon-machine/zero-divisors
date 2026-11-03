"""synthesis.no-120-excludes-hierarchical-second-stage: exact checks.

(a) Under the Clebsch structure with 10s and a 126 only, M_e and M_D are rational combinations of
    symmetric family matrices, hence symmetric; writing M = d(J + delta(E + X)) at the S3->S2
    direction E = e3 e3^T, X is symmetric, so the light-plane compression has y = x (one type).
    Adding a 120 (antisymmetric h) gives X an antisymmetric part and y != x.
(b) With the sum rule's one-type bound Delta <= arctan sqrt(me/mmu) + arctan (m1/m2)^(1/4) and the
    data bound tan Delta >= 0.6375 (cos^2 Delta <= 0.711), (m1/m2)^(1/4) >= (0.6375 - a)/(1 + 0.6375 a)
    with a = 0.06955 >= sqrt(me/mmu), so m1/m2 > 0.0874 > 0.01: Premise (H)'s inequality fails.
"""
from fractions import Fraction as F
import GA
from GA import mat_mul
from tp_premise import premise


def mat(rows):
    return [[F(x) for x in r] for r in rows]


def add(A, B, c=F(1)):
    return [[a + c * b for a, b in zip(r, s)] for r, s in zip(A, B)]


def sc(c, A):
    return [[c * a for a in r] for r in A]


def tr(A):
    return [list(r) for r in zip(*A)]


def vAw(v, A, w):
    return sum(v[i] * A[i][j] * w[j] for i in range(3) for j in range(3))


J = mat([[1, 1, 1]] * 3)
E = mat([[0, 0, 0], [0, 0, 0], [0, 0, 1]])
BE, BO = [F(1), F(1), F(-2)], [F(1), F(-1), F(0)]


def texture_X(M, d, delta):
    return add(sc(F(1) / delta, add(sc(F(1) / d, M), J, F(-1))), E, F(-1))


def check_no_120_stages_are_one_type():
    premise("standard-model.imported-clebsch-structure-seesaw")
    premise("standard-model.hyp-s-slot-statistics")
    premise("synthesis.solar-angle-light-plane-sum-rule")
    Y1 = mat([[F(1, 3), 2, -1], [2, 5, F(1, 7)], [-1, F(1, 7), 4]])
    Y2 = mat([[-2, F(1, 2), 0], [F(1, 2), F(1, 9), 3], [0, 3, F(7, 3)]])
    f = mat([[F(2, 5), -1, 1], [-1, 0, F(3, 2)], [1, F(3, 2), -6]])
    h = mat([[0, 1, F(-2, 3)], [-1, 0, 5], [F(2, 3), -5, 0]])
    assert tr(h) == sc(F(-1), h)
    for (v1, v2, w, c) in [(F(1), F(-2), F(3), F(0)), (F(5, 4), F(1, 3), F(-1, 2), F(0)),
                           (F(1), F(-2), F(3), F(7, 5))]:
        Me = add(add(sc(v1, Y1), sc(v2, Y2)), add(sc(-3 * w, f), sc(c, h)))   # M_e, lepton Clebsch -3
        X = texture_X(Me, F(2), F(3, 7))
        x_unnorm, y_unnorm = vAw(BE, add(E, X), BO), vAw(BO, add(E, X), BE)
        if c == 0:
            assert Me == tr(Me) and X == tr(X) and x_unnorm == y_unnorm
        else:
            assert X != tr(X) and x_unnorm != y_unnorm
            anti = sc(F(1, 2), add(X, tr(X), F(-1)))
            assert anti == sc(c / (2 * F(3, 7)), h)          # the antisymmetric part is the 120's
    assert vAw(BE, E, BE) == 4                               # (even,even) entry of E: 4/6 = 2/3


def check_hierarchy_bound_fails():
    premise("synthesis.solar-angle-light-plane-sum-rule")
    premise("standard-model.neutrino-dirac-matrix-charged-fermions")
    me, mmu = F(51099895, 10 ** 8), F(1056583755, 10 ** 7)
    a = F(6955, 10 ** 5)
    assert a * a >= me / mmu                                 # a >= sqrt(me/mmu)
    edge = (1 - F(711, 1000)) / F(711, 1000)                 # tan^2 Delta at cos^2 Delta = 0.711
    T0 = F(6375, 10000)
    assert T0 * T0 <= edge                                   # tan Delta >= T0 whenever cos^2 Delta <= 0.711
    b_low = (T0 - a) / (1 + T0 * a)                          # (m1/m2)^(1/4) >= b_low
    assert F(5438, 10000) < b_low < F(5439, 10000)
    assert b_low ** 4 > F(874, 10000) > F(1, 100)
    assert b_low ** 4 / F(1, 100) > F(87, 10)                # (H) missed by a factor above 8.7


EXPORTS = {}
