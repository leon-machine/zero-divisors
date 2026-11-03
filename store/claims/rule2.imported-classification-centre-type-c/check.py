"""rule2.imported-classification-centre-type-c: exact checks.

Every clause is tested on all signatures (p, q) with 1 <= n = p + q <= 8 (44 signatures):
  (1) n even: Cl(p,q) is semisimple (the trace form tau(xy), tau the scalar part, is diagonal in the
      blade basis with entries +-1; tau is 2^-n times the regular trace, which vanishes on
      nilpotents, so the radical lies in the kernel of the nondegenerate tau and is zero) and its
      centre is R (the commutator with e_i sends distinct blades to distinct blades, so the centre
      is spanned by the central blades, and only 1 is central); semisimple with centre a field
      means simple;
  (2) n odd: omega is central, omega^2 = (-1)^(n(n-1)/2) (-1)^q, the centre is span{1, omega},
      isomorphic to R + R (orthogonal idempotents (1 +- omega)/2) when omega^2 = +1 and to C
      (omega^2 = -1) otherwise;
  (3) central idempotents: (a + b omega)^2 = (a^2 + s b^2) + 2ab omega (s = omega^2, checked as a
      polynomial identity on a 3 x 3 grid of (a, b)), so the nontrivial ones solve 2ab = b,
      a^2 + s b^2 = a, b != 0, i.e. a = 1/2, b^2 = 1/(4s): real solutions exactly when s = +1 and n
      odd, i.e. p - q = 1 mod 4, and then exactly eps_+- = (1 +- omega)/2;
  (4) the grade involution exchanges eps_+ and eps_-, while every inner automorphism fixes them
      (they are central; tested also on explicit invertible u), so it is outer; each ideal
      eps_+- Cl(p,q) has dimension 2^(n-1) and centre R eps_+- (a field), hence is simple.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def sigs(nmax):
    return [(p, n - p) for n in range(1, nmax + 1) for p in range(n + 1)]


def central_blades(n, sq):
    return [b for b in GA.all_blades(n)
            if all(GA.commutes(GA.gen(i), {b: F(1)}, sq) for i in range(n))]


def semisimple(n, sq):
    blades = GA.all_blades(n)
    diag = all(GA.mul({b: F(1)}, {b: F(1)}, sq) in ({(): F(1)}, {(): F(-1)}) for b in blades)
    # tau(e_I e_J) = 0 for I != J: e_I e_J is a nonscalar blade
    off = all(() not in GA.mul({a: F(1)}, {b: F(1)}, sq) for a in blades for b in blades if a != b)
    return diag and off


def rank(elems, blades):
    rows = [[x.get(b, F(0)) for b in blades] for x in elems if x]
    return GA.field_rank(rows) if rows else 0


def check_even_simple_with_centre_r():
    premise("transport.centre")
    premise("transport.classification-real-clifford-algebras")
    ok = True
    count = 0
    for k in range(1, 5):
        n = 2 * k
        for p in range(n + 1):
            sq = GA.sig(p, n - p)
            ok = ok and central_blades(n, sq) == [()] and semisimple(n, sq)
            count += 1
    ok = ok and count == 24
    GA.check("n even: Cl(p,q) semisimple with centre R, hence simple (2 <= n <= 8)", ok)
    return ok


def check_odd_centre_and_square():
    premise("transport.centre")
    premise("transport.sign")
    ok = True
    count = 0
    nsplit = 0
    for p, q in sigs(8):
        n = p + q
        if n % 2 == 0:
            continue
        sq = GA.sig(p, q)
        omega = {tuple(range(n)): F(1)}
        ok = ok and central_blades(n, sq) == [(), tuple(range(n))]
        s = (-1) ** (n * (n - 1) // 2) * (-1) ** q
        ok = ok and GA.eq(GA.mul(omega, omega, sq), GA.sc(s))
        if s == 1:
            ep = GA.scal(F(1, 2), GA.add(GA.sc(1), omega))
            em = GA.scal(F(1, 2), GA.sub(GA.sc(1), omega))
            # R + R: two orthogonal idempotents spanning the centre
            ok = ok and GA.eq(GA.mul(ep, ep, sq), ep) and GA.is_zero(GA.mul(ep, em, sq))
            ok = ok and GA.eq(GA.add(ep, em), GA.sc(1))
            nsplit += 1
        else:
            # C: omega is a square root of -1, so a + b omega is invertible unless a = b = 0
            for a, b in ((1, 2), (-3, 1), (0, 5)):
                z = GA.add(GA.sc(a), GA.scal(b, omega))
                zb = GA.sub(GA.sc(a), GA.scal(b, omega))
                ok = ok and GA.eq(GA.mul(z, zb, sq), GA.sc(a * a + b * b))
        count += 1
    ok = ok and count == 20 and nsplit == 10
    GA.check("n odd: centre R[omega], R + R for omega^2 = +1 and C for -1 (1 <= n <= 7)", ok)
    return ok


def check_central_idempotents():
    premise("transport.existence-classification-type-c")
    ok = True
    count = 0
    have = 0
    for p, q in sigs(8):
        n = p + q
        sq = GA.sig(p, q)
        cb = central_blades(n, sq)
        nontrivial = []
        if len(cb) == 2:
            omega = {cb[1]: F(1)}
            s = GA.mul(omega, omega, sq)[()]
            # the polynomial identity behind the idempotent equations, on a 3 x 3 grid
            for a in (F(0), F(1, 2), F(-2)):
                for b in (F(1), F(-1, 3), F(3, 2)):
                    x = GA.add(GA.sc(a), GA.scal(b, omega))
                    want = GA.add(GA.sc(a * a + s * b * b), GA.scal(2 * a * b, omega))
                    ok = ok and GA.eq(GA.mul(x, x, sq), want)
            # b != 0 forces a = 1/2 and b^2 = 1/(4 s): a real b exists iff s > 0
            if s > 0:
                for b in (F(1, 2), F(-1, 2)):
                    e = GA.add(GA.sc(F(1, 2)), GA.scal(b, omega))
                    ok = ok and GA.eq(GA.mul(e, e, sq), e) and b * b * 4 * s == 1
                    nontrivial.append(e)
        ok = ok and (len(nontrivial) == 2) == ((p - q) % 4 == 1)
        have += len(nontrivial) == 2
        count += 1
    ok = ok and count == 44 and have == 10
    GA.check("nontrivial central idempotents exist iff p - q = 1 mod 4, and are (1 +- omega)/2", ok)
    return ok


def check_grade_involution_outer_and_ideals_simple():
    premise("transport.existence-classification-type-c")
    premise("transport.classification-real-clifford-algebras")
    ok = True
    count = 0
    for p, q in sigs(7):
        if (p - q) % 4 != 1:
            continue
        n = p + q
        sq = GA.sig(p, q)
        blades = GA.all_blades(n)
        omega = {tuple(range(n)): F(1)}
        ep = GA.scal(F(1, 2), GA.add(GA.sc(1), omega))
        em = GA.scal(F(1, 2), GA.sub(GA.sc(1), omega))
        ok = ok and GA.eq(GA.grade_inv(ep), em) and not GA.eq(ep, em)
        # inner automorphisms fix eps_+: explicit invertible u with inverse u^-1
        for i in range(n):
            u = GA.add(GA.sc(2), GA.gen(i))                  # (2 + e_i)(2 - e_i) = 4 - e_i^2
            ui = GA.scal(F(1, 4 - sq[i]), GA.sub(GA.sc(2), GA.gen(i)))
            ok = ok and GA.eq(GA.mul(u, ui, sq), GA.sc(1))
            ok = ok and GA.eq(GA.mul(GA.mul(u, ep, sq), ui, sq), ep)
        for sgn, e in ((1, ep), (-1, em)):
            ideal = [GA.mul(e, {b: F(1)}, sq) for b in blades]
            ok = ok and rank(ideal, blades) == 2 ** (n - 1)
            ok = ok and GA.eq(GA.mul(e, omega, sq), GA.scal(sgn, e))     # e omega = +- e
            # centre of the ideal: e Z = span{e, e omega} = R e
            ok = ok and rank([GA.mul(e, {b: F(1)}, sq) for b in central_blades(n, sq)], blades) == 1
        count += 1
    ok = ok and count == 10
    GA.check("grade involution exchanges eps_+- (outer); each ideal has centre R and is simple", ok)
    return ok
