"""rule2.odd-lorentzian-dimension-exactly-one-real: exact checks, odd n = 3, 5, 7, 9, 11.

(1) For each odd n the centre of Cl(1,n-1) and of Cl(n-1,1) is spanned by the blades 1 and omega
(computed blade by blade: conjugation by a generator sends each blade to +- itself, so the centre is
spanned by the central blades). Type C (central idempotents (1 +- omega)/2, both nonzero) holds iff
omega^2 = +1, and the computed omega^2 gives: Cl(1,n-1) type C iff n = 1 mod 4, Cl(n-1,1) type C iff
n = 3 mod 4, the other form with omega^2 = -1 (centre C, complex type). This agrees with the
commuting-square theorem (a): Cl(1,n-1) is the timelike extension of Cl(0,n-1), obstructed iff
0 - (n-1) = 0 mod 4; Cl(n-1,1) is the spacelike extension of Cl(n-1,0), obstructed iff n-1 = 2 mod 4.
(2) Complexification, modelled exactly as pairs (a, b) = a + i b over Cl: e_k -> i e_k maps the
generators of Cl(1,n-1) to anticommuting elements of square -e_k^2, the relations of Cl(n-1,1), and
the images' products i^|S| e_S are independent: the two real forms have the same complexification.
In it omega' = omega or i omega has square +1 and is central, and (1 +- omega')/2 are nonzero
complementary central idempotents, for every odd n.
"""
from fractions import Fraction as F
from itertools import combinations
import GA
from tp_premise import premise

NS = (3, 5, 7, 9, 11)


def lor(n, time_plus):
    return GA.sig(1, n - 1) if time_plus else GA.sig(n - 1, 1)


def central_blades(sq):
    n = len(sq)
    return [b for b in GA.all_blades(n)
            if all(GA.commutes({b: F(1)}, GA.gen(i), sq) for i in range(n))]


def omega_sq(sq):
    n = len(sq)
    om = {tuple(range(n)): F(1)}
    return GA.mul(om, om, sq)[()]


def check_real_forms_alternate():
    premise("rule2.where-obstruction-sits-commuting-square")
    ok = True
    table = {}
    for n in NS:
        row = []
        for time_plus in (True, False):
            sq = lor(n, time_plus)
            ok = ok and central_blades(sq) == [(), tuple(range(n))]
            w2 = omega_sq(sq)
            typeC = w2 == 1
            if typeC:
                om = {tuple(range(n)): F(1)}
                ep = GA.scal(F(1, 2), GA.add(GA.sc(1), om))
                em = GA.scal(F(1, 2), GA.sub(GA.sc(1), om))
                ok = ok and GA.eq(GA.mul(ep, ep, sq), ep) and GA.is_zero(GA.mul(ep, em, sq))
                ok = ok and not GA.is_zero(ep) and not GA.is_zero(em)
            else:
                ok = ok and w2 == -1
            row.append(typeC)
        table[n] = tuple(row)
        # the commuting-square theorem's prediction from the even base algebra
        pred_plus = (0 - (n - 1)) % 4 == 0
        pred_minus = ((n - 1) - 0) % 4 == 2
        ok = ok and table[n] == (pred_plus, pred_minus)
        ok = ok and table[n] == (n % 4 == 1, n % 4 == 3)
    ok = ok and table[5] == (True, False) and table[3] == (False, True) and table[11] == (False, True)
    GA.check("odd Lorentzian n <= 11: exactly one real form is type C, Cl(1,n-1) iff n = 1 mod 4", ok)
    return ok


# complexified algebra: elements are pairs (re, im) of multivectors
def cmul(x, y, sq):
    a, b = x
    c, d = y
    return (GA.sub(GA.mul(a, c, sq), GA.mul(b, d, sq)), GA.add(GA.mul(a, d, sq), GA.mul(b, c, sq)))


def cadd(x, y):
    return (GA.add(x[0], y[0]), GA.add(x[1], y[1]))


def ceq(x, y):
    return GA.eq(x[0], y[0]) and GA.eq(x[1], y[1])


def creal(c):
    return (GA.sc(c), {})


def check_same_complexification_split():
    ok = True
    for n in NS:
        sq = lor(n, True)
        img = [({}, GA.gen(k)) for k in range(n)]          # i e_k
        target = lor(n, False)
        # Cl(n-1,1) puts its square -1 generator last; i e_k squares to -e_k^2
        ok = ok and all(ceq(cmul(img[k], img[k], sq), creal(-sq[k])) for k in range(n))
        ok = ok and sorted(-s for s in sq) == sorted(target)
        ok = ok and all(ceq(cadd(cmul(img[j], img[k], sq), cmul(img[k], img[j], sq)), ({}, {}))
                        for j in range(n) for k in range(j + 1, n))
        # products of images: i^|S| e_S, one per blade, independent (a monomial in a distinct blade)
        if n <= 5:
            seen = set()
            for k in range(n + 1):
                for S in combinations(range(n), k):
                    x = creal(1)
                    for i in S:
                        x = cmul(x, img[i], sq)
                    keys = set(x[0]) | set(x[1])
                    ok = ok and keys == {S}
                    seen |= keys
            ok = ok and len(seen) == 2 ** n
        # omega' = omega or i omega with square +1, central; (1 +- omega')/2 idempotents
        for s in (lor(n, True), lor(n, False)):
            om = {tuple(range(n)): F(1)}
            w2 = omega_sq(s)
            omp = (om, {}) if w2 == 1 else ({}, om)
            ok = ok and ceq(cmul(omp, omp, s), creal(1))
            ok = ok and all(ceq(cmul(omp, (GA.gen(i), {}), s), cmul((GA.gen(i), {}), omp, s)) for i in range(n))
            ep = (GA.scal(F(1, 2), GA.add(GA.sc(1), omp[0])), GA.scal(F(1, 2), omp[1]))
            em = (GA.scal(F(1, 2), GA.sub(GA.sc(1), omp[0])), GA.scal(F(-1, 2), omp[1]))
            ok = ok and ceq(cmul(ep, ep, s), ep) and ceq(cmul(em, em, s), em)
            ok = ok and ceq(cmul(ep, em, s), ({}, {})) and ceq(cadd(ep, em), creal(1))
            ok = ok and not ceq(ep, ({}, {})) and not ceq(em, ({}, {}))
    GA.check("both real forms complexify to one algebra, split by (1 +- omega')/2, every odd n <= 11", ok)
    return ok
