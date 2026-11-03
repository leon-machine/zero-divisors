"""dark-tower-matter.three-dimensional-phases: exact check of the computable core.

The phase classification is assembly level on imported dynamics (Polyakov confinement, the
topologically massive phase, flux attachment), which are not computable here. Checked:
(1) The phase split from the minimal bare level: each U(1) couples to one unit-charge cell
    (three-dimensional-content), whose mass sign shifts the level by sign(m)/2 (anomalies (i)).
    Over bare levels k = +-1/2 and both mass signs, the effective level k + sign(m)/2 is an integer,
    0 (phase C) exactly when the mass sign is opposite to the bare level and +-1 (phase T) exactly
    when aligned: two of each (so the photon mass e^2 |k_eff|/2pi is e^2/2pi in phase T). With an integral
    bare level (k = 0, 1) the effective level would not be an integer (control). Flux attachment at
    |k_eff| = 1 shifts the unit-charge cell's spin by q^2/2k = +-1/2, so spin 1/2 becomes 0 or 1
    (0 on the standard signs).
(2) Contact suppression: a contact amplitude ~ m/e^2 gives probabilities (m/e^2)^2; at
    e^2/m = 7e7 this is below 2.1e-16 and at 7.1e7 below 2e-16, the K4 threshold.
(3) At r = 7 the algebra's central unit: in Cl(2,3) omega commutes with every generator and
    omega^2 = -1 (residue-seven-unit), the extra conserved charge invoked for stability.
The Delta N_eff of about 4e-3 for two massless 2+1 photons comes from the supplementary script
CHECK_COS and is not checked.
"""
from fractions import Fraction as F

import GA
import series
from tp_premise import premise

K4_THRESHOLD = F(2, 10 ** 16)        # the K4 survival threshold of the survival proposition
# The docstring's ratios e^2/m with the probability bound stated at each, and a control ratio below.
CONTACT_CASES = [(F(7, 1) * 10 ** 7, F(21, 10 ** 17)), (F(71, 10) * 10 ** 7, K4_THRESHOLD)]
CONTROL_RATIO = F(69, 10) * 10 ** 7


def floor_sqrt(x):
    """The integer part of the square root of a nonnegative rational."""
    return series.iroot_bracket(x, 2, 1)[0]


def check_phase_split_from_minimal_level():
    premise("dark-tower-matter.anomalies")
    premise("dark-tower-matter.three-dimensional-content")
    q = 1                                        # unit-charge cell per U(1)
    phases = {'C': 0, 'T': 0}
    for k in (F(1, 2), F(-1, 2)):
        for sgn in (1, -1):
            keff = k + F(sgn * q * q, 2)
            assert keff.denominator == 1
            aligned = (k > 0) == (sgn > 0)
            if keff == 0:
                assert not aligned
                phases['C'] += 1
            else:
                assert aligned and abs(keff) == 1
                phases['T'] += 1
                shift = F(q * q, 2) / keff
                assert abs(shift) == F(1, 2)
                assert {F(1, 2) - abs(shift), F(1, 2) + abs(shift)} == {0, 1}
    assert phases == {'C': 2, 'T': 2}
    # control: an integral bare level is inconsistent with one unit-charge cell
    for k in (F(0), F(1)):
        for sgn in (1, -1):
            assert (k + F(sgn, 2)).denominator == 2
    return True


def check_contact_suppression():
    premise("dark-tower-matter.three-dimensional-content")
    for (ratio, bound) in CONTACT_CASES:
        prob = (1 / ratio) ** 2
        assert prob < bound
    assert (1 / CONTROL_RATIO) ** 2 > K4_THRESHOLD
    # Sharpness, by hand: the threshold ratio 1/sqrt(2e-16) = sqrt(50) 1e7 = 70710678.1, inside
    # (7.0e7, 7.1e7); at e^2/m = 7e7 the probability is 1/4.9e15 = 2.0408e-16, just below 2.1e-16.
    assert floor_sqrt(1 / K4_THRESHOLD) == 70710678
    assert int(10 ** 20 * (1 / CONTACT_CASES[0][0]) ** 2) == 20408
    return True


def check_r7_central_unit():
    premise("dark-tower-matter.residue-seven-unit")
    S = GA.sig(2, 3)
    w = {(0, 1, 2, 3, 4): F(1)}
    assert all(GA.commutes(w, GA.gen(a), S) for a in range(5))
    assert GA.mul(w, w, S) == {(): F(-1)}
    return True
