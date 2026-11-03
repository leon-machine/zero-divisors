"""field-theory.no-canonical-commutation-relations-tower: exact checks of the finite statement.

Floors of the tower: Cl(1,3) with k = 0, 1, 2 hyperbolic tower planes adjoined (generators of
square +1, -1 per plane), i.e. Cl(2,4) and Cl(3,5) at k = 1, 2 (n = 4, 6, 8 generators).
(1) The trace argument (the premise's), exhaustively: for every pair of basis blades A, B of each
floor, <AB>_0 = <BA>_0, so by bilinearity the scalar part of every commutator [a, a*] vanishes,
while <1>_0 = 1. Hence no floor contains a pair with [a, a*] = 1. The same in matrices: on the
Jordan-Wigner Fock space of 1, 2, 3 modes, tr([X, Y]) = 0 for all matrix units while tr(1) = 2^N.
(2) Bosons made of fermions are not excluded by this: the pair operator b = v_1 v_2 on two
Jordan-Wigner modes has [b, b*] = 1 - N_1 - N_2, which is 1 on the vacuum (and on no other number
state), a composite that obeys the canonical relation on the vacuum sector without contradicting (1).
The bounded statement in the CAR limit (Wielandt-Wintner) is an imported theorem with no finite
content beyond (1) and is not checked.
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise


def floor_sig(k):
    return tuple([1, -1, -1, -1] + [1, -1] * k)


def lower(n, k):
    """a_k on n Jordan-Wigner modes as a dense matrix (mode 0 the most significant bit)."""
    return fock.to_dense(fock.ann(k, n, fock.MSB), 2 ** n)


mm = GA.mat_mul


def tp(A):
    return [list(r) for r in zip(*A)]


def check_scalar_part_is_a_trace_on_every_floor():
    premise("field-theory.imported-statistics-no-go-palatial-algebra")
    pairs = 0
    for k in (0, 1, 2):
        sq = floor_sig(k)
        n = len(sq)
        blades = GA.all_blades(n)
        for A in blades:
            for B in blades:
                sAB, bAB = GA.blade_mul(A, B, sq)
                sBA, bBA = GA.blade_mul(B, A, sq)
                cAB = sAB if bAB == () else 0
                cBA = sBA if bBA == () else 0
                assert cAB == cBA
                pairs += 1
        assert GA.sc(1).get(()) == 1
    assert pairs == 16 ** 2 + 64 ** 2 + 256 ** 2, pairs


def check_matrix_trace_kills_commutators():
    premise("field-theory.imported-statistics-no-go-palatial-algebra")
    pairs = 0
    for n in (1, 2, 3):
        D = 2 ** n
        units = []
        for i in range(D):
            for j in range(D):
                M = [[F(0)] * D for _ in range(D)]
                M[i][j] = F(1)
                units.append(M)
        for X in units:
            for Y in units:
                # tr(XY) - tr(YX) = sum_{a,b} (X_ab Y_ba - Y_ab X_ba)
                assert sum((X[a][b] * Y[b][a] - Y[a][b] * X[b][a] for a in range(D) for b in range(D)), F(0)) == 0
                pairs += 1
    assert pairs == 4 ** 2 + 16 ** 2 + 64 ** 2
    for n in (1, 2, 3):
        D = 2 ** n
        one = mm(lower(n, 0), tp(lower(n, 0)))
        one = [[one[a][b] + mm(tp(lower(n, 0)), lower(n, 0))[a][b] for b in range(D)] for a in range(D)]
        assert sum(one[a][a] for a in range(D)) == 2 ** n            # tr(v v* + v* v) = tr(1) = 2^N
        v = lower(n, n - 1)
        c = [[mm(v, tp(v))[a][b] - mm(tp(v), v)[a][b] for b in range(D)] for a in range(D)]
        assert sum(c[a][a] for a in range(D)) == 0


def check_composite_pair_is_not_excluded():
    n = 2
    D = 4
    v1, v2 = lower(n, 0), lower(n, 1)
    b = mm(v1, v2)
    bs = tp(b)
    comm = [[mm(b, bs)[i][j] - mm(bs, b)[i][j] for j in range(D)] for i in range(D)]
    N1, N2 = mm(tp(v1), v1), mm(tp(v2), v2)
    want = [[(F(1) if i == j else F(0)) - N1[i][j] - N2[i][j] for j in range(D)] for i in range(D)]
    assert comm == want
    assert [comm[i][i] for i in range(D)] == [F(1), F(0), F(0), F(-1)]
