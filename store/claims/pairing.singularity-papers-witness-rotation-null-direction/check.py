"""pairing.singularity-papers-witness-rotation-null-direction: exact checks.

Conventions of the pairing paper (as in the check of pairing.pairing-functional-pair-creation-amplitude):
Cl(1,3) with eta = diag(1, -1, -1, -1), l = e0 + e1, m = e2 + i e3; the two-mode Fock module by
Jordan-Wigner matrices over Q(i): e0 = a1 + a1^dag, e1 = a1 - a1^dag, e2 = a2 - a2^dag,
e3 = -i(a2 + a2^dag), so c(l) = 2 a1 and c(m) = 2 a2 annihilate |0>; |12> = a1^dag a2^dag |0>.
  (1) R = 3/5 + 4/5 e12 (GA.py): R R~ = 1; R l R~ = e0 - 7/25 e1 + 24/25 e2, null, with
      <R l R~, l> = 32/25, so not proportional to l; the frame rotation about e3 has
      (cos, sin) = (-7/25, 24/25) = (c^2 - s^2, 2cs) at (c, s) = (3/5, 4/5): the double angle
      (Fact pairing.imported-null-flags).
  (2) On the Fock module: R acts as 3/5 + 4/5 c(e1)c(e2), R|0> = 3/5|0> + 4/5|12> with no odd
      component, c(R l R~) = R c(l) R^-1 and c(R m R~) = R c(m) R^-1 as matrices, and both annihilate
      R|0>: it is the Witt vacuum of the rotated decomposition.
  (3) pv(e12) = <(e12) . l, m> = -1 and <12| e12 |0> = 1 = -pv(e12) (Proposition
      pairing.pairing-functional-pair-creation-amplitude); the hop and annihilation parts of e12 kill
      |0>, and its diagonal (Cartan) part on |0> is zero.
  (4) The boost rotor 5/3 + 4/3 e01 has R R~ = 1 and acts on |0> as the scalar 1/3.
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

QI = GA.QI
S13 = GA.sig(1, 3)
D = 4
VAC, ONE, TWO, BOTH = 0, 1, 2, 3


qmm = GA.field_mat_mul


def qadd(a, b, c=1):
    return [[a[i][j] + b[i][j] * c for j in range(D)] for i in range(D)]


def qscal(c, a):
    return [[x * c for x in r] for r in a]


def qid():
    return [[QI(1) if i == j else QI(0) for j in range(D)] for i in range(D)]


def ann(j):
    """a_j on two Jordan-Wigner modes, dense over GA.QI (LSB bitmask basis)."""
    return fock.to_dense(fock.msc(QI(1), fock.ann(j, 2)), D, QI(0))


def dag(M):
    return [[M[j][i].conj() for j in range(D)] for i in range(D)]


A1, A2 = ann(0), ann(1)
C1, C2 = dag(A1), dag(A2)
GEN = [qadd(A1, C1), qadd(A1, C1, -1), qadd(A2, C2, -1), qscal(QI(0, -1), qadd(A2, C2))]


def col(M, k):
    return [M[r][k] for r in range(D)]


def apply(M, v):
    return [sum((M[i][k] * v[k] for k in range(D)), QI(0)) for i in range(D)]


def cl(x):
    """Fock matrix of a (complex) multivector given as {blade: QI or Fraction}."""
    out = [[QI(0)] * D for _ in range(D)]
    for b, c in x.items():
        M = qid()
        for i in b:
            M = qmm(M, GEN[i])
        out = qadd(out, qscal(QI(c) if not isinstance(c, QI) else c, M))
    return out


def m(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, S13)
    return out


E = [GA.gen(i) for i in range(4)]
L = GA.add(E[0], E[1])
R = GA.add(GA.sc(F(3, 5)), GA.scal(F(4, 5), m(E[1], E[2])))
RB = GA.add(GA.sc(F(5, 3)), GA.scal(F(4, 3), m(E[0], E[1])))


def check_rotor_rotates_the_null_direction():
    ok = GA.eq(m(R, GA.reverse(R)), GA.sc(1))
    Rl = m(R, L, GA.reverse(R))
    ok = ok and GA.eq(Rl, GA.add(E[0], GA.scal(F(-7, 25), E[1]), GA.scal(F(24, 25), E[2])))
    ok = ok and GA.dot(Rl, Rl, S13) == 0 and GA.dot(Rl, L, S13) == F(32, 25)
    ok = ok and GA.dot(L, L, S13) == 0
    c, s = F(3, 5), F(4, 5)
    ok = ok and (c * c - s * s, 2 * c * s) == (F(-7, 25), F(24, 25))
    ok = ok and GA.eq(m(R, E[3], GA.reverse(R)), E[3])
    GA.check("R = 3/5 + 4/5 e12 sends l to e0 - 7/25 e1 + 24/25 e2, <Rl R~, l> = 32/25: the double angle", ok)
    return ok


def check_rotated_state_is_the_rotated_witt_vacuum():
    ok = True
    vac = [QI(1), QI(0), QI(0), QI(0)]
    Rf = cl(R)
    Rv = apply(Rf, vac)
    pair = apply(qmm(C1, C2), vac)
    ok = ok and pair == [QI(0), QI(0), QI(0), QI(1)]
    ok = ok and Rv == [QI(F(3, 5)), QI(0), QI(0), QI(F(4, 5))]
    Rinv = cl(GA.reverse(R))
    ok = ok and qmm(Rf, Rinv) == qid()
    Rl = m(R, L, GA.reverse(R))
    Rm_real = m(R, E[2], GA.reverse(R))
    Rm = dict((b, QI(c)) for b, c in Rm_real.items())
    Rm[(3,)] = Rm.get((3,), QI(0)) + QI(0, 1)
    cRl, cRm = cl(Rl), cl(Rm)
    cL = cl(L)
    cM = cl({(2,): QI(1), (3,): QI(0, 1)})
    ok = ok and cL == qscal(QI(2), A1) and cM == qscal(QI(2), A2)
    ok = ok and cRl == qmm(qmm(Rf, cL), Rinv) and cRm == qmm(qmm(Rf, cM), Rinv)
    ok = ok and apply(cRl, Rv) == [QI(0)] * 4 and apply(cRm, Rv) == [QI(0)] * 4
    ok = ok and apply(cL, Rv) != [QI(0)] * 4
    GA.check("R|0> = 3/5|0> + 4/5|12> is annihilated by c(R l R~) and c(R m R~): the rotated vacuum", ok)
    return ok


def check_rotation_acts_through_its_pairing_class():
    premise("pairing.pairing-functional-pair-creation-amplitude")
    premise("pairing.imported-null-flags")
    ok = True
    B = m(E[1], E[2])
    Bl = GA.scal(F(1, 2), GA.sub(m(B, L), m(L, B)))
    pv = QI(GA.dot(Bl, E[2], S13), GA.dot(Bl, E[3], S13))
    ok = ok and pv == QI(-1)
    Bf = cl(B)
    amp = col(Bf, VAC)
    ok = ok and amp[BOTH] == -pv and amp[VAC] == QI(0) and amp[ONE] == QI(0) and amp[TWO] == QI(0)
    # the hop and pair-annihilation operators of the two modes kill |0>
    hop = qadd(qmm(A1, C2), qmm(C1, A2))
    annih = qmm(A1, A2)
    vac = [QI(1), QI(0), QI(0), QI(0)]
    ok = ok and apply(hop, vac) == [QI(0)] * 4 and apply(annih, vac) == [QI(0)] * 4
    # the half angle: the spinor amplitudes (3/5, 4/5) are the half of the frame angle (-7/25, 24/25)
    ok = ok and F(3, 5) ** 2 - F(4, 5) ** 2 == F(-7, 25)
    GA.check("pv(e12) = -1 and <12|e12|0> = 1: the rotation acts on |0> through its pairing class", ok)
    return ok


def check_boost_rotor_fixes_the_ray():
    ok = GA.eq(m(RB, GA.reverse(RB)), GA.sc(1))
    vac = [QI(1), QI(0), QI(0), QI(0)]
    ok = ok and apply(cl(RB), vac) == [QI(F(1, 3)), QI(0), QI(0), QI(0)]
    GA.check("the boost rotor 5/3 + 4/3 e01 acts on |0> as the scalar 1/3", ok)
    return ok
