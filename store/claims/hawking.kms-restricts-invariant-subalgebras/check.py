"""hawking.kms-restricts-invariant-subalgebras: exact checks of the finite-dimensional core.

The claim is about C*-algebras and analytic continuation; its finite-dimensional content is checked on
B = Mat_4 (two modes, basis |n1 n2>) with H = N_1 + 2 N_2 (weights h = 0, 2, 1, 3), the flow
alpha_t(E_ij) = z^(h_i - h_j) E_ij (z = e^(it)) and the Gibbs state omega(x) = Tr(rho x), rho = diag(q^h),
q = e^(-beta) a rational Boltzmann symbol; alpha_(i beta) is the same scaling with z replaced by q.
(1) omega is KMS on B: omega(xy) = omega(y alpha_(i beta)(x)) on all 256 pairs of matrix units, for q = 1/2, 3.
(2) For four unital subalgebras C (the diagonal algebra, Mat_2 (x) 1 of mode 1, the even subalgebra, the
    number-conserving algebra), invariance under the real flow is checked as invariance under the scaling
    by seven distinct z (weight differences lie in -3..3, so this forces C to be a sum of weight spaces,
    by Vandermonde); C is closed under products and contains 1; alpha_(i beta)(C) = C; and omega restricted
    to C satisfies the KMS identity for alpha restricted to C on every pair of basis elements of C.
(3) Control: the unital algebra span{1, X}, X the swap of |00> and |01> (plus 1 on the rest), is not
    invariant (its scaled image leaves it), so alpha does not restrict to it.
"""
from fractions import Fraction as F

import GA
import fock

HW = [0, 2, 1, 3]
QS = [F(1, 2), F(3)]
ZS = [F(2), F(-1), F(1, 3), F(3), F(-2), F(5), F(1, 7)]


def unit(i, j):
    return {(i, j): F(1)}


mm, madd = fock.mm, fock.madd


def scale(x, z):
    return {(i, j): c * z ** (HW[i] - HW[j]) for (i, j), c in x.items()}


def omega(x, q):
    return sum((c * q ** HW[i] for (i, j), c in x.items() if i == j), F(0))


def rank(elems):
    rows = [[x.get((i, j), F(0)) for i in range(4) for j in range(4)] for x in elems]
    return GA.field_rank(rows)


ONE = fock.eye(4)
SUBALGEBRAS = {
    "diagonal": [unit(i, i) for i in range(4)],
    "mode-1 Mat_2": [madd(unit(a, b), unit(a + 1, b + 1)) for a in (0, 2) for b in (0, 2)],
    "even": [unit(i, j) for i in range(4) for j in range(4) if (bin(i).count("1") + bin(j).count("1")) % 2 == 0],
    "number-conserving": [unit(i, j) for i in range(4) for j in range(4) if bin(i).count("1") == bin(j).count("1")],
}
SWAP = madd(unit(0, 1), unit(1, 0), unit(2, 2), unit(3, 3))


def check_gibbs_state_is_kms_on_b():
    ok = True
    units = [unit(i, j) for i in range(4) for j in range(4)]
    for q in QS:
        ok = ok and all(omega(mm(x, y), q) == omega(mm(y, scale(x, q)), q) for x in units for y in units)
    ok = ok and len(units) ** 2 == 256
    GA.check("the Gibbs state diag(q^h) is KMS on Mat_4 for the scaled flow", ok)
    return ok


def check_restriction_to_invariant_subalgebras():
    ok = True
    dims = []
    for name, C in SUBALGEBRAS.items():
        d = rank(C)
        dims.append(d)
        ok = ok and rank(C + [ONE]) == d
        ok = ok and all(rank(C + [mm(x, y)]) == d for x in C for y in C)
        ok = ok and all(rank(C + [scale(x, z)]) == d for x in C for z in ZS)
        for q in QS:
            ok = ok and all(rank(C + [scale(x, q)]) == d for x in C)
            ok = ok and all(omega(mm(x, y), q) == omega(mm(y, scale(x, q)), q) for x in C for y in C)
    ok = ok and dims == [4, 4, 8, 6]
    ok = ok and len(set(HW[i] - HW[j] for i in range(4) for j in range(4))) == 7 and len(set(ZS)) == 7
    GA.check("invariant unital subalgebras (dims 4, 4, 8, 6): the restricted Gibbs state is KMS for the restricted flow", ok)
    return ok


def check_non_invariant_control():
    ok = True
    C = [ONE, SWAP]
    ok = ok and mm(SWAP, SWAP) == ONE
    ok = ok and rank(C) == 2 and rank(C + [scale(SWAP, ZS[0])]) == 3
    GA.check("control: span{1, swap} is a unital subalgebra the flow does not preserve", ok)
    return ok
