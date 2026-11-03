"""dark-tower-matter.anomalies: exact checks.

(i) Three-dimensional towers (premise: their content): the four cells of R^2 (x) R^2 have weights
(s, p) in {+-1}^2 and charges q_+- = (s +- p)/2. Under each U(1)_+- exactly two cells are charged, with
charges +1 and -1, and they are each other's conjugate (weight negated): one unit-charge two-component
fermion per U(1). With the parity-anomaly shift sign(m)/2 per such fermion (premise: the imported
parity anomaly), the effective level k + sign(m)/2 is an integer for both signs of m exactly when the
bare level k is in Z + 1/2 (tested on k in {-3, -5/2, ..., 3}); no such k is zero.
(ii) Five-dimensional towers (premise: the content computed in five-dimensional-content, imported
through its export): in units q' = 3Y with colour multiplicities, sum q'^3 = -6 and sum q' = 0, and the
induced abelian Chern-Simons coefficient (1/2) sum sign(m) mult q'^3 (premise: the imported 5D shift) is
an integer for all 16 choices of the species' mass signs, while the D and E terms alone are half-odd.
"""
from fractions import Fraction as F
from itertools import product
import GA
from tp_premise import premise

LEVELS = [F(k, 2) for k in range(-6, 7)]


def check_three_dimensional_parity_anomaly():
    premise("dark-tower-matter.three-dimensional-content")
    premise("rule2.imported-parity-anomaly")
    cells = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    q = {c: (F(c[0] + c[1], 2), F(c[0] - c[1], 2)) for c in cells}
    ok = q[(1, 1)] == (1, 0) and q[(1, -1)] == (0, 1)
    for idx in (0, 1):
        charged = [c for c in cells if q[c][idx] != 0]
        ok = ok and len(charged) == 2 and sorted(q[c][idx] for c in charged) == [-1, 1]
        ok = ok and charged[0] == (-charged[1][0], -charged[1][1])
    good = [k for k in LEVELS if all((k + F(sg, 2)).denominator == 1 for sg in (1, -1))]
    ok = ok and good == [k for k in LEVELS if k.denominator == 2] and len(good) == 6 and F(0) not in good
    GA.check("prop:anomaly(i): one unit-charge fermion per U(1); bare levels in Z + 1/2 exactly, never zero", ok)
    return ok


def check_five_dimensional_chern_simons_integrality():
    sp = premise("dark-tower-matter.five-dimensional-content")["species"]()
    premise("rule2.imported-five-dimensional-chern-simons-shift")
    names = ["U", "D", "E", "N"]
    qp = [3 * sp[nm][1] for nm in names]
    mult = [sp[nm][0] for nm in names]
    ok = qp == [2, -1, -3, 0] and mult == [3, 3, 1, 1]
    cube = sum(m * x ** 3 for m, x in zip(mult, qp))
    lin = sum(m * x for m, x in zip(mult, qp))
    ok = ok and cube == -6 and lin == 0
    ok = ok and all(sum(F(sg, 2) * m * x ** 3 for sg, m, x in zip(sgs, mult, qp)).denominator == 1
                    for sgs in product((1, -1), repeat=4))
    ok = ok and (F(1, 2) * mult[1] * qp[1] ** 3).denominator == 2 and (F(1, 2) * mult[2] * qp[2] ** 3).denominator == 2
    GA.check("prop:anomaly(ii): sum q'^3 = -6, sum q' = 0; the induced coefficient is integral for all 16 sign choices",
             ok)
    return ok
