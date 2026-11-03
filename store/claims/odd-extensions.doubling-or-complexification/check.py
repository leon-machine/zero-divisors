"""odd-extensions.doubling-or-complexification: exact checks, over every signature (p,q) of odd
dimension n = 3 and n = 5 (and n = 1 for (ii) and (i)), with e_n the last generator and
omega' = e_1 ... e_{n-1}.

(i) omega^2 = +1 (computed, and equal to the premise's (-1)^(n(n-1)/2 + q)): P_+- = (1 +- omega)/2 are
central, idempotent, orthogonal, nonzero and sum to 1; x -> P_+- x is injective on Cl^0 (rank
2^(n-1)) and P_+- Cl = P_+- Cl^0 (same span), so each ideal is a copy of Cl^0. The sign of the
action of e_n is P_+- e_n = +-s P_+- omega' with s = e_n^2 = omega'^2: e_n acts as omega' on one
summand and as -omega' on the other (which summand gets +omega' is fixed by s; see the report).
(ii) omega^2 = -1: omega is central and odd, Cl^0 + omega Cl^0 spans Cl (dimension 2^n) with
Cl^0 meeting omega Cl^0 in 0, and (a + omega b)(c + omega d) = (ac - bd) + omega(ad + bc) on sample
elements: Cl = Cl^0 (x) C with omega as i.
(iii) Cl^0(p,q+1) = Cl(p,q) and Cl^0(p+1,q) = Cl(q,p): the e_i e_n square to -e_i^2 e_n^2 and
anticommute, and generate the whole even subalgebra (span 2^(n-1)).
"""
from fractions import Fraction as F
from itertools import combinations
import GA
from tp_premise import premise


def blade(idx):
    return {tuple(idx): F(1)} if idx else GA.sc(1)


def rank(xs, n):
    bl = GA.all_blades(n)
    return GA.rank_of_vectors([[x.get(b, F(0)) for b in bl] for x in xs])


def scalar_square(x, sq):
    y = GA.mul(x, x, sq)
    assert set(y) <= {()}
    return y.get((), F(0))


def odd_sigs(ns=(1, 3, 5)):
    for n in ns:
        for q in range(n + 1):
            yield n, n - q, q, GA.sig(n - q, q)


def check_omega_plus_one_doubling():
    premise("odd-extensions.volume-element-odd-dimension")
    ok = True
    cases = 0
    for n, p, q, sq in odd_sigs():
        om = blade(range(n))
        w2 = scalar_square(om, sq)
        ok = ok and w2 == (-1) ** ((n * (n - 1) // 2 + q) % 2)
        ok = ok and all(GA.commutes(om, GA.gen(i), sq) for i in range(n))
        if w2 != 1:
            continue
        cases += 1
        bl = GA.all_blades(n)
        full = [{b: F(1)} for b in bl]
        even = [{b: F(1)} for b in bl if len(b) % 2 == 0]
        Pp = GA.scal(F(1, 2), GA.add(GA.sc(1), om))
        Pm = GA.scal(F(1, 2), GA.sub(GA.sc(1), om))
        ok = ok and GA.eq(GA.mul(Pp, Pp, sq), Pp) and GA.eq(GA.mul(Pm, Pm, sq), Pm)
        ok = ok and GA.is_zero(GA.mul(Pp, Pm, sq)) and GA.eq(GA.add(Pp, Pm), GA.sc(1))
        ok = ok and all(GA.commutes(P, GA.gen(i), sq) for P in (Pp, Pm) for i in range(n))
        for P in (Pp, Pm):
            ideal = [GA.mul(P, x, sq) for x in full]
            img0 = [GA.mul(P, x, sq) for x in even]
            r = rank(ideal, n)
            ok = ok and r == 2 ** (n - 1) and rank(img0, n) == 2 ** (n - 1) and rank(ideal + img0, n) == r
        # the sign pairing for e_n
        en = GA.gen(n - 1)
        wp = blade(range(n - 1))
        s = sq[n - 1]
        ok = ok and scalar_square(wp, sq) == s and scalar_square(en, sq) == s
        ok = ok and GA.eq(GA.mul(Pp, en, sq), GA.scal(s, GA.mul(Pp, wp, sq)))
        ok = ok and GA.eq(GA.mul(Pm, en, sq), GA.scal(-s, GA.mul(Pm, wp, sq)))
        ok = ok and not GA.eq(GA.mul(Pp, en, sq), GA.mul(Pm, en, sq))
    # omega^2 = +1 at q = 0 (n = 1), q = 1, 3 (n = 3) and q = 0, 2, 4 (n = 5)
    ok = ok and cases == 6
    GA.check("omega^2 = +1: Cl = P+ Cl^0 + P- Cl^0 and e_n acts as +s omega', -s omega' on the two ideals", ok)
    return ok


def check_omega_minus_one_complexification():
    premise("odd-extensions.volume-element-odd-dimension")
    ok = True
    cases = 0
    for n, p, q, sq in odd_sigs():
        om = blade(range(n))
        w2 = scalar_square(om, sq)
        ok = ok and w2 == (-1) ** ((n * (n - 1) // 2 + q) % 2)
        if w2 != -1:
            continue
        cases += 1
        ok = ok and all(GA.commutes(om, GA.gen(i), sq) for i in range(n))
        bl = GA.all_blades(n)
        even = [{b: F(1)} for b in bl if len(b) % 2 == 0]
        wev = [GA.mul(om, x, sq) for x in even]
        ok = ok and rank(even, n) == 2 ** (n - 1) and rank(even + wev, n) == 2 ** n
        ok = ok and all(len(b) % 2 == 1 for x in wev for b in x)
        # complex multiplication on samples of Cl^0
        a = GA.add(GA.sc(2), {b: F(1, 3) for b in bl if len(b) == 2})
        b_ = GA.add(GA.sc(-1), {b: F(len(b) + 1) for b in bl if len(b) % 2 == 0 and b})
        c = GA.add(GA.sc(F(1, 2)), {bl[-1 if n == 1 else 4]: F(1)} if n > 1 else {})
        d = {b: F(2) for b in bl if len(b) == 2} or GA.sc(5)
        lhs = GA.mul(GA.add(a, GA.mul(om, b_, sq)), GA.add(c, GA.mul(om, d, sq)), sq)
        rhs = GA.add(GA.sub(GA.mul(a, c, sq), GA.mul(b_, d, sq)),
                     GA.mul(om, GA.add(GA.mul(a, d, sq), GA.mul(b_, c, sq)), sq))
        ok = ok and GA.eq(lhs, rhs)
    ok = ok and cases == 6
    GA.check("omega^2 = -1: Cl = Cl^0 + omega Cl^0 = Cl^0 (x) C with omega as i", ok)
    return ok


def check_even_subalgebra_identities():
    ok = True
    for n, p, q, sq in odd_sigs((3, 5)):
        en_sq = sq[n - 1]
        T = [GA.mul(GA.gen(i), GA.gen(n - 1), sq) for i in range(n - 1)]
        ok = ok and all(scalar_square(T[i], sq) == -sq[i] * en_sq for i in range(n - 1))
        ok = ok and all(GA.anticommutes(T[i], T[j], sq) for i in range(n - 1) for j in range(i + 1, n - 1))
        prods = []
        for k in range(n):
            for S in combinations(range(n - 1), k):
                x = GA.sc(1)
                for i in S:
                    x = GA.mul(x, T[i], sq)
                prods.append(x)
        ok = ok and rank(prods, n) == 2 ** (n - 1) and all(len(b) % 2 == 0 for x in prods for b in x)
        # target signature: Cl(p', q') of the shadow when e_n^2 = -1, Cl(q', p') when +1
        shadow = sq[:n - 1]
        tgt = shadow if en_sq == -1 else tuple(-s for s in shadow)
        ok = ok and tuple(scalar_square(t, sq) for t in T) == tgt
    GA.check("Cl^0(p,q+1) = Cl(p,q) and Cl^0(p+1,q) = Cl(q,p) via e_i e_n, all odd n = 3, 5", ok)
    return ok
