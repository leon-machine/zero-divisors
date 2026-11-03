from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def pauli():
    i = GA.QI(0, 1)
    z = GA.QI(0)
    return [S.mat([[0, 1], [1, 0]]), [[z, -i], [i, z]], S.mat([[1, 0], [0, -1]])]


def check_pauli_reading_and_the_pseudoscalar():
    premise("std-algebra.existence-uniqueness")
    premise("std-algebra.blade-basis")
    premise("primer.centre")
    premise("primer.sign")
    ok = True
    s = pauli()
    ok = ok and S.check_matrix_rep(s, GA.sig(3, 0), 8)
    prod = S.mat_mul(S.mat_mul(s[0], s[1]), s[2])
    ok = ok and S.mat_eq(prod, S.mat_scal(GA.QI(0, 1), S.mat_id(2)))
    sq = GA.sig(3, 0)
    I = S.pseudoscalar(3)
    ok = ok and GA.eq(GA.mul(I, I, sq), GA.sc(-1))
    ok = ok and all(GA.commutes(I, GA.gen(a), sq) for a in range(3))
    ok = ok and len(S.centre_basis(sq)) == 2
    # control: two Pauli matrices with a sign error do not anticommute
    bad = [s[0], S.mat([[0, 1], [-1, 0]]), s[2]]
    ok = ok and not S.check_matrix_rep(bad, GA.sig(3, 0), 8)
    GA.check("Cl(3,0) = M_2(C) via the Pauli matrices; I = e1e2e3 maps to i and spans the centre with 1", ok)
    return ok
