"""sheaf.imported-classification-values: exact checks.

The five stated values, Cl(1,3) = Mat_2(H), Cl(0,4) = Mat_2(H), Cl(0,3) = H + H, Cl(2,4) = Mat_4(H)
and Cl(1,2) = Mat_2(C), are read off by the primer's exact classifier (taken from the premise's
check through premise(): semisimple trace form, centre, primitive idempotent with corner identified
as R, C or H, dim(A f) = k dim D). For Cl(1,2) and Cl(0,3) the centre is also exhibited directly:
omega is central with omega^2 = -1 (a copy of C) and +1 (two central idempotents).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def check_five_values():
    ex = premise("primer.classification-real-clifford-algebras")
    clifford_type = ex["clifford_type"]
    # (p, q): (D, k, number of simple summands)
    stated = {(1, 3): ("H", 2, 1), (0, 4): ("H", 2, 1), (0, 3): ("H", 1, 2),
              (2, 4): ("H", 4, 1), (1, 2): ("C", 2, 1)}
    ok = True
    for (p, q), (D, k, s) in stated.items():
        t = clifford_type(p, q)
        ok = ok and t["semisimple"] and t["D"] == D and t["k"] == k and t["summands"] == s
    GA.check("Cl(1,3), Cl(0,4), Cl(0,3), Cl(2,4), Cl(1,2) have the stated types", ok)
    return ok


def check_centres_of_the_odd_values():
    ok = True
    for (p, q, w2) in ((1, 2, -1), (0, 3, 1)):
        sq = GA.sig(p, q)
        n = p + q
        omega = {tuple(range(n)): F(1)}
        ok = ok and all(GA.commutes(GA.gen(i), omega, sq) for i in range(n))
        ok = ok and GA.eq(GA.mul(omega, omega, sq), GA.sc(w2))
    GA.check("omega central with omega^2 = -1 in Cl(1,2) and +1 in Cl(0,3)", ok)
    return ok
