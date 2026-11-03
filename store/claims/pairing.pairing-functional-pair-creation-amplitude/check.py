"""pairing.pairing-functional-pair-creation-amplitude: exact checks.

Cl(1,3) with eta = diag(1, -1, -1, -1), l = e0 + e1, n = e0 - e1, m = e2 + i e3, mb = e2 - i e3. The pairing
class pv(B) = <B . l, m> (B . v = [B, v]/2, <,> complex bilinear) is computed in GA.py on real bivectors and
extended complex-linearly; the claim takes these basis values as the defining formula of pv (no uses entry,
so no premise() call).
The two-mode Fock module: Jordan-Wigner matrices over Q(i) (GA.QI), |0>, |1>, |2>, |12> = a1^dag a2^dag |0>,
e0 = a1 + a1^dag, e1 = a1 - a1^dag, e2 = a2 - a2^dag, e3 = -i (a2 + a2^dag): the Clifford relations hold,
c(l) = 2 a1 and c(m) = 2 a2 annihilate the vacuum, c(n) = 2 a1^dag and c(mb) = -2 a2^dag create.
(1) <12| e_a e_b |0> = -pv(e_a e_b) on the six basis bivectors (0, -1, -i, 1, i, 0 against pv = 0, 1, i, -1, -i,
    0), and on sample complex combinations by linearity.
(2) The even sector span{|0>, |12>}: the hops a1^dag a2, a2^dag a1 kill both states, a1 a2 kills |0> and sends
    |12> to -|0>, a1^dag a2^dag sends |0> to |12>, the Cartan elements a_i^dag a_i - 1/2 are diagonal; every
    basis bivector preserves the sector and acts on the vacuum through its Cartan scalar and its |12> amplitude.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
import fock

QI = GA.QI
S13 = GA.sig(1, 3)
D = 4
PAIRS = list(combinations(range(4), 2))
COMBOS = [[QI(1), QI(2), QI(0, 1), QI(-1), QI(3), QI(1, 1)], [QI(0), QI(1, -2), QI(0), QI(4), QI(0, 3), QI(-1)]]


def pv(i, j):
    """pv(e_i e_j) = <(e_i e_j) . l, m>, as a Gaussian rational."""
    B = GA.mul(GA.gen(i), GA.gen(j), S13)
    l = GA.add(GA.gen(0), GA.gen(1))
    Bl = GA.scal(F(1, 2), GA.sub(GA.mul(B, l, S13), GA.mul(l, B, S13)))
    return QI(GA.dot(Bl, GA.gen(2), S13), GA.dot(Bl, GA.gen(3), S13))


qmm = GA.field_mat_mul


def qadd(a, b, c=1):
    return [[a[i][j] + b[i][j] * c for j in range(D)] for i in range(D)]


def qid():
    return [[QI(1) if i == j else QI(0) for j in range(D)] for i in range(D)]


def ann(j):
    """a_j on two Jordan-Wigner modes, dense over GA.QI (LSB bitmask basis)."""
    return fock.to_dense(fock.msc(QI(1), fock.ann(j, 2)), D, QI(0))


def dag(m):
    return [[m[j][i].conj() for j in range(D)] for i in range(D)]


A1, A2 = ann(0), ann(1)
C1, C2 = dag(A1), dag(A2)
GEN = [qadd(A1, C1), qadd(A1, C1, -1), qadd(A2, C2, -1), [[x * QI(0, -1) for x in r] for r in qadd(A2, C2)]]
VAC, ONE, TWO, BOTH = 0, 1, 2, 3


def col(M, k):
    return [M[r][k] for r in range(D)]


def check_vacuum_to_pair_amplitude_is_minus_pv():
    eta = [1, -1, -1, -1]
    ok = True
    for a in range(4):
        for b in range(4):
            anti = qadd(qmm(GEN[a], GEN[b]), qmm(GEN[b], GEN[a]))
            ok = ok and anti == [[x * (2 * eta[a] if a == b else 0) for x in r] for r in qid()]
    # dictionary of the null vectors
    cl, cm = qadd(GEN[0], GEN[1]), qadd(GEN[2], [[x * QI(0, 1) for x in r] for r in GEN[3]])
    cn, cmb = qadd(GEN[0], GEN[1], -1), qadd(GEN[2], [[x * QI(0, -1) for x in r] for r in GEN[3]])
    ok = ok and cl == [[x * 2 for x in r] for r in A1] and cm == [[x * 2 for x in r] for r in A2]
    ok = ok and cn == [[x * 2 for x in r] for r in C1] and cmb == [[x * -2 for x in r] for r in C2]
    ok = ok and col(cl, VAC) == [QI(0)] * D and col(cm, VAC) == [QI(0)] * D
    ok = ok and qmm(C1, qmm(C2, qid()))[BOTH][VAC] == QI(1)
    amps = [qmm(GEN[i], GEN[j])[BOTH][VAC] for i, j in PAIRS]
    ok = ok and amps == [QI(0), QI(-1), QI(0, -1), QI(1), QI(0, 1), QI(0)]
    pvs = [pv(i, j) for i, j in PAIRS]
    ok = ok and pvs == [QI(0), QI(1), QI(0, 1), QI(-1), QI(0, -1), QI(0)]
    ok = ok and (len(amps) == len(pvs) and all(x == -y for x, y in zip(amps, pvs)))
    for coef in COMBOS:
        lhs = sum((c * x for c, x in zip(coef, amps)), QI(0))
        rhs = sum((c * y for c, y in zip(coef, pvs)), QI(0))
        ok = ok and lhs == -rhs
    _tp_rv = (ok); assert _tp_rv is not False, "check_vacuum_to_pair_amplitude_is_minus_pv"; return _tp_rv


def check_even_sector_two_by_two_structure():
    ok = True
    for hop in (qmm(C1, A2), qmm(C2, A1)):
        ok = ok and col(hop, VAC) == [QI(0)] * D and col(hop, BOTH) == [QI(0)] * D
    an = qmm(A1, A2)
    cr = qmm(C1, C2)
    ok = ok and col(an, VAC) == [QI(0)] * D and col(an, BOTH) == [QI(-1), QI(0), QI(0), QI(0)]
    ok = ok and col(cr, VAC) == [QI(0), QI(0), QI(0), QI(1)]
    half = [[x * F(1, 2) for x in r] for r in qid()]
    for c, a in ((C1, A1), (C2, A2)):
        cart = qadd(qmm(c, a), half, -1)
        ok = ok and all(cart[i][j] == 0 for i in range(D) for j in range(D) if i != j)
        ok = ok and cart[VAC][VAC] == QI(F(-1, 2)) and cart[BOTH][BOTH] == QI(F(1, 2))
    # every basis bivector preserves span{|0>, |12>}; on the vacuum it is (scalar)|0> + (amplitude)|12>
    scalars = []
    for i, j in PAIRS:
        B = qmm(GEN[i], GEN[j])
        ok = ok and B[ONE][VAC] == 0 and B[TWO][VAC] == 0 and B[ONE][BOTH] == 0 and B[TWO][BOTH] == 0
        scalars.append(B[VAC][VAC])
    ok = ok and scalars == [QI(-1), QI(0), QI(0), QI(0), QI(0), QI(0, -1)]
    _tp_rv = (ok); assert _tp_rv is not False, "check_even_sector_two_by_two_structure"; return _tp_rv
