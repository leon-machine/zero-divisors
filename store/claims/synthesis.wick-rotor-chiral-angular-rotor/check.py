"""synthesis.wick-rotor-chiral-angular-rotor: exact checks in Cl(2,4) (GA blade engine).

GA indices: e0 (square +1), e1, e2, e3 (square -1), e+ = 4 (square +1), e- = 5 (square -1).
sigma = e0e1, I4 = e0e1e2e3, E = e+e-, I6 = I4 E. Rational points (c, s) = (cos(theta/2), sin(theta/2)) on
the unit circle stand in for theta; cos theta = c^2 - s^2 and sin theta = 2cs.
(i)   I4 sigma = e2e3; E^2 = 1, [I4, E] = 0; I6 sigma = E e2e3 is a single 4-blade (e+ e- e2 e3 up to
      sign), commuting with sigma and E, with square -1; I6 commutes with all 32 even blades (so left and
      right multiplication by I6 agree on the even algebra and on its left ideals); R^W = c + s E e2e3
      satisfies the group law R^W(c1,s1) R^W(c2,s2) = R^W(c1c2 - s1s2, s1c2 + c1s2) at sample pairs, and
      R^W(pi)^2 = -1, R^W(pi)^4 = +1 (periods 2 pi and 4 pi).
(ii)  eps_+- = (1 +- E)/2 are orthogonal idempotents summing to 1, commuting with e2e3, eps_+- E = +-eps_+-,
      eps_+- I6 = +-eps_+- I4, and R^W = eps_+ R_theta + eps_- R_-theta with R_theta = c + s e2e3, at four
      rational points.
(iii) R^W reverse(R^W) = (c^2 - s^2) + 2cs E e2e3 != 1, the inverse is c - s E e2e3, and R^W e2 (R^W)^-1
      has a nonzero grade-3 part at the four points (none in pi Z); at theta = pi the element E e2e3 is a
      versor (all six basis vectors go to vectors). The angular rotor R_theta has R reverse(R) = 1, fixes
      e0 and e1 and maps every basis vector to a vector.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
POINTS = [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(-8, 17), F(15, 17)), (F(24, 25), F(-7, 25))]
EVEN_BLADES = [b for b in GA.all_blades(6) if len(b) % 2 == 0]


def m(*xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out


def bl(*idx):
    return {tuple(idx): F(1)}


SIGMA, I4, E, E23 = bl(0, 1), bl(0, 1, 2, 3), bl(4, 5), bl(2, 3)
I6 = m(I4, E)
ONE = GA.sc(1)


def RW(c, s):
    return GA.add(GA.sc(c), GA.scal(s, m(E, E23)))


def Rang(c, s):
    return GA.add(GA.sc(c), GA.scal(s, E23))


def grades(x):
    return sorted({len(b) for b in x})


def check_generator_identities():
    premise("field-theory.where-each-lives")
    premise("state-selection.euclidean-partner-curvature-selected")
    premise("odd-extensions.imported-conformal-completion")
    ok = True
    ok = ok and m(I4, SIGMA) == E23
    ok = ok and m(E, E) == ONE and GA.commutes(I4, E, SQ)
    X = m(I6, SIGMA)
    ok = ok and X == m(E, E23) and len(X) == 1 and grades(X) == [4]
    ok = ok and GA.commutes(X, SIGMA, SQ) and GA.commutes(X, E, SQ)
    ok = ok and m(X, X) == GA.sc(-1)
    ok = ok and all(GA.commutes(I6, {b: F(1)}, SQ) for b in EVEN_BLADES) and len(EVEN_BLADES) == 32
    ok = ok and not GA.commutes(I6, GA.gen(0), SQ)
    for (c1, s1) in POINTS:
        for (c2, s2) in POINTS:
            ok = ok and m(RW(c1, s1), RW(c2, s2)) == RW(c1 * c2 - s1 * s2, s1 * c2 + c1 * s2)
    Rpi = RW(F(0), F(1))
    ok = ok and m(Rpi, Rpi) == GA.sc(-1) and m(Rpi, Rpi, Rpi, Rpi) == ONE
    GA.check("(i) I6 sigma = E e2e3, square -1, central in the even algebra; R^W group law and periods 2pi, 4pi", ok)
    return ok


def check_chiral_splitting():
    premise("field-theory.where-each-lives")
    ok = True
    ep = GA.scal(F(1, 2), GA.add(ONE, E))
    em = GA.scal(F(1, 2), GA.sub(ONE, E))
    ok = ok and m(ep, ep) == ep and m(em, em) == em and m(ep, em) == {} and GA.add(ep, em) == ONE
    ok = ok and GA.commutes(ep, E23, SQ) and GA.commutes(em, E23, SQ)
    ok = ok and m(ep, E) == ep and m(em, E) == GA.neg(em)
    ok = ok and m(ep, I6) == m(ep, I4) and m(em, I6) == GA.neg(m(em, I4))
    for c, s in POINTS:
        ok = ok and RW(c, s) == GA.add(m(ep, Rang(c, s)), m(em, Rang(c, -s)))
    GA.check("(ii) R^W = eps_+ R_theta + eps_- R_-theta; I6 = +-I4 on the two chiral halves", ok)
    return ok


def check_not_a_rotor_on_vectors():
    premise("singularity.euclidean-rotor-where-it-lies")
    ok = True
    for c, s in POINTS:
        R = RW(c, s)
        ok = ok and m(R, GA.reverse(R)) == GA.add(GA.sc(c * c - s * s), GA.scal(2 * c * s, m(E, E23)))
        ok = ok and m(R, GA.reverse(R)) != ONE
        Rinv = GA.sub(GA.sc(c), GA.scal(s, m(E, E23)))
        ok = ok and m(R, Rinv) == ONE
        conj = m(R, GA.gen(2), Rinv)
        g3 = {b: v for b, v in conj.items() if len(b) == 3}
        ok = ok and g3 != {} and set(abs(v) for v in g3.values()) == {abs(2 * c * s)}
        A = Rang(c, s)
        ok = ok and m(A, GA.reverse(A)) == ONE
        Ainv = GA.reverse(A)
        ok = ok and m(A, GA.gen(0), Ainv) == GA.gen(0) and m(A, GA.gen(1), Ainv) == GA.gen(1)
        ok = ok and all(grades(m(A, GA.gen(i), Ainv)) == [1] for i in range(6))
    V = m(E, E23)
    Vinv = GA.neg(V)
    ok = ok and m(V, Vinv) == ONE
    ok = ok and all(grades(m(V, GA.gen(i), Vinv)) == [1] for i in range(6))
    GA.check("(iii) R^W reverse(R^W) != 1 and R^W e2 R^W^-1 has a grade-3 part off pi Z; E e2e3 a versor; R_theta a rotor", ok)
    return ok
