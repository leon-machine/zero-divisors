"""transport.odd-lorentzian-dimension-exactly-one-real: exact checks, odd n = 3, 5, 7, 9, 11.

(1) For each odd n and each real form, Cl(1,n-1) (time generator square +1, the other n-1 square -1)
and Cl(n-1,1), the centre is computed blade-wise (conjugation by a generator sends a blade to +-
itself, so the centre is spanned by the central blades) and is span{1, omega}. omega^2 decides the
type: +1 gives nonzero complementary central idempotents (1 +- omega)/2 (type C); -1 makes the
centre a copy of C (complex type). The computed table: Cl(1,n-1) is type C exactly for n = 5, 9 and
Cl(n-1,1) exactly for n = 3, 7, 11, so exactly one form is type C in every odd n.
(2) The table agrees with the commuting-square theorem's rule, applied as the proof applies it: an
even-dimensional Cl(a,b) has its type-C extension by a generator of square -1 iff a - b = 2 mod 4
and by one of square +1 iff a - b = 0 mod 4; Cl(1,n-1) extends Cl(1,n-2) by a square -1 generator
and Cl(n-1,1) extends Cl(n-2,1) by a square +1 generator. The extensions are built in GA and their
omega^2 recomputed.
(3) Complexification, modelled exactly as pairs (a, b) = a + i b: e_k -> i e_k on the generators of
square -1 turns the relations of Cl(p,q) into those of Cl(n,0), for both forms, and the products of
the images are one per blade (independent); omega' = omega or i omega has square +1, is central, and
(1 +- omega')/2 are nonzero orthogonal central idempotents summing to 1, for every odd n <= 11.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

NS = (3, 5, 7, 9, 11)


def form(n, time_plus):
    return GA.sig(1, n - 1) if time_plus else GA.sig(n - 1, 1)


def central_blades(sq):
    n = len(sq)
    return [b for b in GA.all_blades(n)
            if all(GA.commutes({b: F(1)}, GA.gen(i), sq) for i in range(n))]


def omega_sq(sq):
    n = len(sq)
    w = {tuple(range(n)): F(1)}
    return GA.mul(w, w, sq).get((), F(0))


def is_type_c(sq):
    """Type C read off the algebra: omega^2 = +1 and (1 +- omega)/2 are nonzero central idempotents."""
    n = len(sq)
    w = {tuple(range(n)): F(1)}
    if omega_sq(sq) != 1:
        return False
    ep = GA.scal(F(1, 2), GA.add(GA.sc(1), w))
    em = GA.scal(F(1, 2), GA.sub(GA.sc(1), w))
    return (GA.eq(GA.mul(ep, ep, sq), ep) and GA.eq(GA.mul(em, em, sq), em)
            and GA.is_zero(GA.mul(ep, em, sq)) and not GA.is_zero(ep) and not GA.is_zero(em))


def check_exactly_one_real_form_is_type_c():
    ok = True
    plus_c, minus_c = [], []
    for n in NS:
        for time_plus in (True, False):
            sq = form(n, time_plus)
            ok = ok and central_blades(sq) == [(), tuple(range(n))]
            if is_type_c(sq):
                (plus_c if time_plus else minus_c).append(n)
            else:
                # complex type: omega^2 = -1, so the centre span{1, omega} is a copy of C
                ok = ok and omega_sq(sq) == -1
        ok = ok and ((n in plus_c) != (n in minus_c))
    ok = ok and plus_c == [5, 9] and minus_c == [3, 7, 11]
    ok = ok and all(n % 4 == 1 for n in plus_c) and all(n % 4 == 3 for n in minus_c)
    GA.check("odd n <= 11: Cl(1,n-1) type C iff n = 1 mod 4, Cl(n-1,1) iff n = 3 mod 4, other complex", ok)
    return ok


def check_agrees_with_commuting_square_rule():
    premise("transport.where-obstruction-lies-commuting-square")
    ok = True
    for n in NS:
        # Cl(1,n-1) = Cl(1,n-2) + generator of square -1; Cl(n-1,1) = Cl(n-2,1) + generator of square +1
        for (a, b), gamma, time_plus in (((1, n - 2), -1, True), ((n - 2, 1), 1, False)):
            ext = GA.sig(a, b) + (gamma,)
            rule = ((a - b) % 4 == 2) if gamma == -1 else ((a - b) % 4 == 0)
            ok = ok and sorted(ext) == sorted(form(n, time_plus))
            ok = ok and is_type_c(ext) == rule and is_type_c(form(n, time_plus)) == rule
    GA.check("the type table matches the commuting-square rule on the even base algebras", ok)
    return ok


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


def check_common_complexification_is_split():
    ok = True
    for n in NS:
        for time_plus in (True, False):
            sq = form(n, time_plus)
            img = [({}, GA.gen(k)) if sq[k] == -1 else (GA.gen(k), {}) for k in range(n)]
            ok = ok and all(ceq(cmul(img[k], img[k], sq), creal(1)) for k in range(n))
            ok = ok and all(ceq(cadd(cmul(img[j], img[k], sq), cmul(img[k], img[j], sq)), ({}, {}))
                            for j in range(n) for k in range(j + 1, n))
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
            w = {tuple(range(n)): F(1)}
            wp = (w, {}) if omega_sq(sq) == 1 else ({}, w)
            ok = ok and ceq(cmul(wp, wp, sq), creal(1))
            ok = ok and all(ceq(cmul(wp, (GA.gen(i), {}), sq), cmul((GA.gen(i), {}), wp, sq))
                            for i in range(n))
            ep = (GA.scal(F(1, 2), GA.add(GA.sc(1), wp[0])), GA.scal(F(1, 2), wp[1]))
            em = (GA.scal(F(1, 2), GA.sub(GA.sc(1), wp[0])), GA.scal(F(-1, 2), wp[1]))
            ok = ok and ceq(cmul(ep, ep, sq), ep) and ceq(cmul(em, em, sq), em)
            ok = ok and ceq(cmul(ep, em, sq), ({}, {})) and ceq(cadd(ep, em), creal(1))
            ok = ok and not ceq(ep, ({}, {})) and not ceq(em, ({}, {}))
    GA.check("both real forms complexify to Cl(n,0) (x) C, split by (1 +- omega')/2, odd n <= 11", ok)
    return ok
