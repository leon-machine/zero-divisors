"""synthesis.capacity-per-mode-independent-of-helicity: exact checks.

(a) One ladder pair of a hyperbolic plane (Cl(1,1), v = (e+ + e-)/2, w = (e+ - e-)/2) acts on a
two-dimensional Fock space: the vacuum projector w v is a rank-one idempotent and the minimal left
ideal Cl(1,1) w v has dimension 2, so the maximal entropy of one mode is ln 2 (one qubit).
(b) Grouping bookkeeping with entropies in units of ln 2 (exact rationals): for fixed lists of
per-mode entropies s_j in [0, 1] (units ln 2) matching a fixed total, grouping the modes into units
of h ladder pairs divides the unit count by h and multiplies the mean entropy per unit by h, so
kappa per unit = kappa per mode / h and 1/(4 <s>_unit) = (1/h) * 1/(4 <s>_mode); the mode density
and the equality case (every s_j = 1) are unchanged.
"""
from fractions import Fraction as F
import GA
from GA import mul, add, sub, scal, sc, gen
from tp_premise import premise


def check_one_mode_one_qubit():
    premise("scrambling.pair-mode-qubit-one-object")
    sq = GA.sig(1, 1)
    v = scal(F(1, 2), add(gen(0), gen(1)))
    w = scal(F(1, 2), sub(gen(0), gen(1)))
    assert mul(v, v, sq) == {} and mul(w, w, sq) == {}
    assert add(mul(v, w, sq), mul(w, v, sq)) == sc(1)
    P = mul(w, v, sq)
    assert mul(P, P, sq) == P and P != {} and P != sc(1)
    # dimension of the left ideal Cl(1,1) P
    blades = GA.all_blades(2)
    vecs = [GA.basis_vector_of(mul({b: F(1)}, P, sq), blades) for b in blades]
    assert GA.rank_of_vectors(vecs) == 2
    return True


# fixed per-pair entropies in units of ln 2 (each in (0, 1]), and the expected bookkeeping:
# (mean entropy per pair, residue per pair, residue per two-pair unit), all in units with ln 2 = 1
CASES = [
    ([F(1), F(1, 2), F(3, 4), F(1, 4)], F(5, 8), F(2, 5), F(1, 5)),
    ([F(1), F(1), F(1), F(1), F(1), F(1)], F(1), F(1, 4), F(1, 8)),
    ([F(1, 3), F(2, 3), F(1, 2), F(1, 2)], F(1, 2), F(1, 2), F(1, 4)),
    ([F(9, 10), F(1, 10), F(3, 5), F(2, 5), F(1), F(1, 5)], F(8, 15), F(15, 32), F(15, 64)),
]


def check_grouping_rescales_unit_only():
    premise("synthesis.residue-from-mode-entropy")
    premise("scrambling.residue-each-convention")
    premise("scrambling.mode-count")
    for (s, mean_expected, kappa1_expected, kappa2_expected) in CASES:
        assert len(s) % 2 == 0 and all(F(0) < x <= 1 for x in s)
        # residue-from-mode-entropy (i): kappa = 1/(4 <s>), here in units where ln 2 = 1
        mean_mode = sum(s) / len(s)
        assert mean_mode == mean_expected
        kappa = {}
        for h in (1, 2):
            units = [sum(s[k * h:(k + 1) * h]) for k in range(len(s) // h)]
            mean_unit = sum(units) / len(units)
            assert mean_unit == h * mean_mode
            kappa[h] = 1 / (4 * mean_unit)
            assert kappa[h] >= F(1, 4 * h)                 # >= 1/(4 h ln 2): s_j <= ln 2
            assert (kappa[h] == F(1, 4 * h)) == all(x == 1 for x in s)
        assert (kappa[1], kappa[2]) == (kappa1_expected, kappa2_expected)
        assert kappa[2] * 2 == kappa[1]                    # one count, two units
        # the number of ladder pairs is unchanged by the grouping: 2 * (pairs / 2)
        assert 2 * (len(s) // 2) == len(s)
    return True
