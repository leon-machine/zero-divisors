"""synthesis.definite-side-rung-count-on-every-quarter-turn-lens-wall-is-the-level: exact checks.

Integer arithmetic on the imported formula s(m) for the level, m = n + 1, against the numbers the store holds.
Scalars only (grade 0); GA supplies the check harness.
"""
import GA
from tp_premise import premise


def level(m):
    """The imported formula, for m >= 2."""
    r = m % 8
    if r in (0, 2):
        return m + 1
    if r == 4:
        return m + 3
    return m + 2


def count(n):
    """Clause (i), stated in n."""
    r = n % 8
    if r in (1, 7):
        return n + 2
    if r == 5:
        return n + 4
    return n + 3


def ceil_div(a, b):
    return -((-a) // b)


def check_level_formula_reproduces_the_stored_counts_and_lies_between_the_stored_bounds():
    premise("synthesis.imported-stolz-level-of-real-projective-spaces-under-the-quarter-turn")
    premise("synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five")
    premise("synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height")
    ok = True
    # the statement in n is the imported formula at m = n + 1
    ok = ok and all(count(n) == level(n + 1) for n in range(1, 201))
    ok = ok and [count(n) for n in range(1, 9)] == [3, 5, 6, 7, 9, 9, 9, 11]
    # stored: 3 on L(4,1), 5 on L^5(4), and the window 5 <= k_+ <= 6 on L^7(4)
    ok = ok and count(1) == 3 and count(2) == 5 and 5 <= count(3) <= 6 and count(3) == 6
    for n in range(1, 201):
        m = n + 1
        # the stored upper bound by explicit maps, the stored lower bounds (K-theory; 3; 5 from n = 2 on)
        ok = ok and count(n) <= ceil_div(3 * m, 2)
        ok = ok and count(n) >= 1 + ceil_div(n, 2) and count(n) >= 3
        if n >= 2:
            ok = ok and count(n) >= 5
        # the general bound m + 1 <= s(m) <= m + 3
        ok = ok and m + 1 <= count(n) <= m + 3
    # outside its range the formula would break the stored upper bound: at m = 1 it gives 3 > ceil(3/2) = 2
    ok = ok and level(1) == 3 and level(1) > ceil_div(3, 2)
    GA.check("the level formula gives 3, 5, 6, 7, 9, 9, 9, 11 and lies between the stored bounds for n = 1..200", ok)
    return ok


def check_explicit_maps_are_optimal_exactly_in_four_dimensions_and_the_period_is_eight():
    premise("synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five")
    ok = True
    optimal = [n for n in range(1, 401) if count(n) == ceil_div(3 * (n + 1), 2)]
    ok = ok and optimal == [1, 2, 3, 5]
    excess = {n: ceil_div(3 * (n + 1), 2) - count(n) for n in range(1, 401)}
    ok = ok and excess[4] == 1 and all(excess[n] >= 2 for n in range(6, 401))
    # k_+ - n depends on n + 1 modulo 8 only, and on no smaller period
    ok = ok and all(count(n + 8) - (n + 8) == count(n) - n for n in range(1, 393))
    ok = ok and any(count(n + 4) - (n + 4) != count(n) - n for n in range(1, 9))
    # the K-theory lower bound is about half: 2 (1 + ceil(n/2)) <= count(n) + 2 and count(n) <= 2 (1 + ceil(n/2)) + 2
    ok = ok and all(count(n) - 2 <= 2 * (1 + ceil_div(n, 2)) <= count(n) + 2 for n in range(1, 401))
    GA.check("explicit maps optimal exactly at n = 1, 2, 3, 5; period 8 and not 4; the K-theory bound is about half", ok)
    return ok
