"""synthesis.a-division-no-rung-of-the-switch-tower-performs: exact checks.

Rungs Cl_Q(k,k) computed with GA.py (generators 0..k-1 square +1, k..2k-1 square -1). The size is
the rank of {a * blade} divided by the number of blades. The non-existence of a solution in a lower
rung is checked directly, as the inconsistency of a linear system for the coefficients of x.
"""
from fractions import Fraction as F

import GA

H = F(1, 2)
THIRD = F(1, 3)


def rung(k):
    return GA.sig(k, k)


def mul(x, y, k):
    return GA.mul(x, y, rung(k))


def v_(i, k):
    return GA.scal(H, GA.add(GA.gen(i - 1), GA.gen(k + i - 1)))


def w_(i, k):
    return GA.scal(H, GA.sub(GA.gen(i - 1), GA.gen(k + i - 1)))


def on_(i, k):
    return mul(v_(i, k), w_(i, k), k)


def off_(i, k):
    return mul(w_(i, k), v_(i, k), k)


def prod(xs, k):
    out = GA.sc(1)
    for x in xs:
        out = mul(out, x, k)
    return out


def g_(j, k):
    return prod([off_(i, k) for i in range(1, j)] + [on_(j, k)], k)


def p_(m, k):
    return prod([off_(i, k) for i in range(1, m + 1)], k)


def vec(x, blades, index):
    row = [F(0)] * len(blades)
    for bb, c in x.items():
        row[index[bb]] = c
    return row


def size(a, k):
    blades = GA.all_blades(2 * k)
    index = {b: i for i, b in enumerate(blades)}
    return F(GA.rank_of_vectors([vec(mul(a, {b: F(1)}, k), blades, index) for b in blades]), len(blades))


def total(xs):
    out = {}
    for x in xs:
        out = GA.add(out, x)
    return out


K3 = 3
G3 = {j: g_(j, K3) for j in (1, 2, 3)}


def check_first_on_tests_are_exclusive_with_sizes():
    k = K3
    for j, x in G3.items():
        assert GA.eq(mul(x, x, k), x)
        assert size(x, k) == F(1, 2 ** j)
    assert (size(G3[1], k), size(G3[2], k), size(G3[3], k)) == (H, F(1, 4), F(1, 8))      # hand values
    for i in G3:
        for j in G3:
            if i != j:
                assert GA.is_zero(mul(G3[i], G3[j], k))
    for m, hand in ((0, F(1)), (1, H), (2, F(1, 4)), (3, F(1, 8))):
        pm = p_(m, k)
        assert GA.eq(mul(pm, pm, k), pm) and size(pm, k) == hand
        assert GA.eq(GA.add(total([G3[j] for j in range(1, m + 1)]), pm), GA.sc(1))
    return True


def check_finite_parts_are_solved_by_partial_sums():
    k = K3
    for members in ((2,), (1, 3), (2, 3), (1, 2, 3), ()):
        for n in (1, 2, 3):
            en = total([G3[j] for j in members if j <= n])
            for j in range(1, n + 1):
                want = G3[j] if j in members else {}
                assert GA.eq(mul(en, G3[j], k), want)
    # a finite J is solved outright, and so is a cofinite one, on every g_j of the rung
    for members in ((2,), (1, 3)):
        e_fin = total([G3[j] for j in members])
        e_cof = GA.sub(GA.sc(1), e_fin)
        for j in (1, 2, 3):
            assert GA.eq(mul(e_fin, G3[j], k), G3[j] if j in members else {})
            assert GA.eq(mul(e_cof, G3[j], k), {} if j in members else G3[j])
    return True


def _lower_rung_blades(m, k):
    """the blades of the subalgebra of switches 1..m inside rung k."""
    allowed = set(range(m)) | set(range(k, k + m))
    return [b for b in GA.all_blades(2 * k) if set(b) <= allowed]


def _solvable(m, k, j_in, j_out):
    """is there x in A_m with x g_{j_in} = g_{j_in} and x g_{j_out} = 0 (computed in rung k)?"""
    blades = GA.all_blades(2 * k)
    index = {b: i for i, b in enumerate(blades)}
    unknowns = _lower_rung_blades(m, k)
    gin, gout = g_(j_in, k), g_(j_out, k)
    cols = [vec(mul({b: F(1)}, gin, k), blades, index) + vec(mul({b: F(1)}, gout, k), blades, index) for b in unknowns]
    rhs = vec(gin, blades, index) + [F(0)] * len(blades)
    return GA.rank_of_vectors(cols + [rhs]) == GA.rank_of_vectors(cols)


def check_no_solution_in_a_lower_rung_by_linear_algebra():
    assert len(_lower_rung_blades(1, 3)) == 4 and len(_lower_rung_blades(2, 3)) == 16
    # x in A_1 cannot be 1 on g_2 and 0 on g_3, nor the reverse (both tests lie beyond switch 1)
    assert not _solvable(1, 3, 2, 3)
    assert not _solvable(1, 3, 3, 2)
    # control: the same demand is met once x may use the switch that tells the tests apart
    assert _solvable(2, 3, 2, 3)
    assert _solvable(3, 3, 3, 2)
    # and x in A_1 can separate g_1 from g_2, which switch 1 already tells apart
    assert _solvable(1, 3, 1, 2)
    return True


def check_factorisation_used_in_the_proof():
    k = K3
    p1 = p_(1, k)
    h2 = on_(2, k)
    h3 = mul(off_(2, k), on_(3, k), k)
    assert GA.eq(G3[2], mul(p1, h2, k)) and GA.eq(G3[3], mul(p1, h3, k))
    assert size(h2, k) == H and size(h3, k) == F(1, 4)
    # N(c h) = N(c) N(h) for c in A_1 and h even on switches 2, 3
    for c in (v_(1, k), on_(1, k), GA.gen(0), GA.add(GA.sc(1), GA.gen(0)), GA.sub(mul(v_(1, k), p1, k), p1)):
        for h in (h2, h3):
            assert size(mul(c, h, k), k) == size(c, k) * size(h, k)
    return True


def check_sizes_of_partial_solutions_and_the_gap_from_one_third():
    k = 4
    g2, g4 = g_(2, k), g_(4, k)
    e2, e4 = g2, GA.add(g2, g4)
    assert size(e2, k) == F(1, 4) == THIRD * (1 - F(1, 4))
    assert size(e4, k) == F(5, 16) == THIRD * (1 - F(1, 16))
    assert size(GA.sub(e4, e2), k) == F(1, 16)
    # no fraction j / 2^m is within 1 / (3 * 2^m) of 1/3 (strictly closer), m up to 16
    for m in range(0, 17):
        gap = min(abs(F(j, 2 ** m) - THIRD) for j in (2 ** m // 3, 2 ** m // 3 + 1))
        assert gap >= F(1, 3 * 2 ** m)
    assert abs(F(5, 16) - THIRD) == F(1, 48) == F(1, 3 * 16)          # the bound is attained at m = 4
    # the stated lower bound on N(E_4 - x) for x in rung 1 (m = 1, n = 2): 1/6 - 1/48 = 7/48
    bound = F(1, 6) - F(1, 48)
    assert bound == F(7, 48)
    for x in ({}, GA.sc(1), on_(1, k), off_(1, k), v_(1, k), GA.add(GA.sc(1), GA.gen(0))):
        assert size(GA.sub(e4, x), k) >= bound
    return True
