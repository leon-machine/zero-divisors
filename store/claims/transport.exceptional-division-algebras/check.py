"""transport.exceptional-division-algebras: exact checks.

For every signature (p, q) with n = p + q <= 6 (28 signatures), in GA.py:
  (1) Witnesses. A blade u with u^2 = +1, u != 1 gives the zero divisors 1 + u, 1 - u
      ((1 + u)(1 - u) = 0). Two anticommuting blades a, b with a^2 = +1, b^2 = -1 give the nonzero
      nilpotent a + b ((a + b)^2 = 0). The blade search finds a zero divisor exactly off
      {(0,0), (0,1), (0,2)} and a nilpotent exactly off {(0,0), (0,1), (0,2), (1,0), (0,3)}.
  (2) Absence. For the five exceptional algebras, with the central idempotents eps (1, or
      (1 +- omega)/2 for (1,0) and (0,3)) and an involution x -> x' fixing eps (Clifford conjugation,
      or reversion for (1,0)): on each summand eps A the symmetrised products eps(b_i b_j' + b_j b_i')
      are multiples of eps with a positive definite diagonal Gram. So eps x x' = N(x) eps with N
      positive definite, each eps A is a division algebra, and a nonzero element has no nilpotent
      or zero-divisor component inside a summand. Summand dimensions and quaternion relations
      identify R, C, H, R + R, H + H.
  (3) Against the classification (premise transport.classification-real-clifford-algebras): the
      eight-entry d-table gives (D, number of summands s) and k from s k^2 dim D = 2^n; the computed
      verdicts are "no zero divisors iff s = 1 and k = 1" and "no nilpotents iff k = 1".
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = [(p, n - p) for n in range(0, 7) for p in range(n + 1)]
EXCEPTIONAL = {(0, 0): ("R", 1), (0, 1): ("C", 2), (0, 2): ("H", 4), (1, 0): ("R+R", 1), (0, 3): ("H+H", 4)}


def blade_square(b, sq):
    s, rest = GA.blade_mul(b, b, sq)
    return s


def zd_witness(p, q):
    n = p + q
    sq = GA.sig(p, q)
    for b in GA.all_blades(n):
        if b and blade_square(b, sq) == 1:
            u = {b: F(1)}
            return GA.add(GA.sc(1), u), GA.sub(GA.sc(1), u)
    return None


def nilpotent_witness(p, q):
    n = p + q
    sq = GA.sig(p, q)
    bl = [b for b in GA.all_blades(n) if b]
    plus = [b for b in bl if blade_square(b, sq) == 1]
    minus = [b for b in bl if blade_square(b, sq) == -1]
    for a in plus:
        for c in minus:
            if GA.anticommutes({a: F(1)}, {c: F(1)}, sq):
                return GA.add({a: F(1)}, {c: F(1)})
    return None


def clifford_conj(x):
    return GA.grade_inv(GA.reverse(x))


def summand_norm_ok(p, q, eps, invol):
    """eps A is a division algebra: eps(b_i b_j' + b_j b_i') in R eps, Gram positive definite diagonal."""
    n = p + q
    sq = GA.sig(p, q)
    basis = []
    for b in GA.all_blades(n):
        x = GA.mul(eps, {b: F(1)}, sq)
        rows = [[y.get(c, F(0)) for c in GA.all_blades(n)] for y in basis + [x]]
        if GA.field_rank(rows) == len(basis) + 1:
            basis.append(x)
    gram = []
    for x in basis:
        row = []
        for y in basis:
            s = GA.add(GA.mul(x, invol(y), sq), GA.mul(y, invol(x), sq))
            # s must be a multiple of eps
            c = None
            for blade, val in eps.items():
                c = s.get(blade, F(0)) / val
                break
            if not GA.eq(s, GA.scal(c, eps)):
                return None
            row.append(c)
        gram.append(row)
    diag_pos = all(gram[i][i] > 0 for i in range(len(gram)))
    offdiag = all(gram[i][j] == 0 for i in range(len(gram)) for j in range(len(gram)) if i != j)
    return len(basis) if (diag_pos and offdiag) else None


def summands(p, q):
    n = p + q
    if (p, q) in ((1, 0), (0, 3)):
        w = {tuple(range(n)): F(1)}
        return [GA.scal(F(1, 2), GA.add(GA.sc(1), w)), GA.scal(F(1, 2), GA.sub(GA.sc(1), w))]
    return [GA.sc(1)]


def check_witnesses_exist_exactly_off_the_exceptional_lists():
    ok = True
    zd_free, nil_free = [], []
    for p, q in SIGS:
        sq = GA.sig(p, q)
        zd = zd_witness(p, q)
        if zd is None:
            zd_free.append((p, q))
        else:
            ok = ok and GA.is_zero(GA.mul(zd[0], zd[1], sq)) and zd[0] and zd[1]
        nil = nilpotent_witness(p, q)
        if nil is None:
            nil_free.append((p, q))
        else:
            ok = ok and GA.is_zero(GA.mul(nil, nil, sq)) and not GA.is_zero(nil)
    ok = ok and sorted(zd_free) == [(0, 0), (0, 1), (0, 2)]
    ok = ok and sorted(nil_free) == [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0)]
    GA.check("zero-divisor and nilpotent witnesses exist exactly off the two exceptional lists (n <= 6)", ok)
    return ok


def check_exceptional_algebras_are_sums_of_division_algebras():
    ok = True
    for (p, q), (name, dim) in EXCEPTIONAL.items():
        sq = GA.sig(p, q)
        invol = GA.reverse if (p, q) == (1, 0) else clifford_conj
        eps_list = summands(p, q)
        tot = GA.add(*eps_list)
        ok = ok and GA.eq(tot, GA.sc(1))
        for e in eps_list:
            ok = ok and GA.eq(GA.mul(e, e, sq), e)
            ok = ok and all(GA.commutes(GA.gen(i), e, sq) for i in range(p + q))
            ok = ok and summand_norm_ok(p, q, e, invol) == dim
        if len(eps_list) == 2:
            ok = ok and GA.is_zero(GA.mul(eps_list[0], eps_list[1], sq))
    # the quaternion relations in Cl(0,2) and on eps_+ Cl(0,3)
    for p, q, eps in ((0, 2, GA.sc(1)), (0, 3, summands(0, 3)[0])):
        sq = GA.sig(p, q)
        i_, j_ = GA.mul(eps, GA.gen(0), sq), GA.mul(eps, GA.gen(1), sq)
        k_ = GA.mul(i_, j_, sq)
        for x in (i_, j_, k_):
            ok = ok and GA.eq(GA.mul(x, x, sq), GA.neg(eps))
        ok = ok and GA.eq(GA.mul(j_, i_, sq), GA.neg(k_))
    # C: Cl(0,1) is commutative with e^2 = -1
    ok = ok and GA.eq(GA.mul(GA.gen(0), GA.gen(0), GA.sig(0, 1)), GA.sc(-1))
    GA.check("the five exceptional algebras are R, C, H, R+R, H+H: positive norm forms on each summand", ok)
    return ok


def check_verdicts_match_the_classification_table():
    premise("transport.classification-real-clifford-algebras")
    table = [("R", 1), ("R", 2), ("R", 1), ("C", 1), ("H", 1), ("H", 2), ("H", 1), ("C", 1)]
    dimD = {"R": 1, "C": 2, "H": 4}
    ok = True
    for p, q in SIGS:
        n = p + q
        D, s = table[(p - q) % 8]
        k2 = 2 ** n // (s * dimD[D])
        k = 1
        while k * k < k2:
            k += 1
        ok = ok and k * k == k2
        ok = ok and ((zd_witness(p, q) is None) == (s == 1 and k == 1))
        ok = ok and ((nilpotent_witness(p, q) is None) == (k == 1))
    GA.check("no zero divisors iff Cl = D (k = 1, one summand); no nilpotents iff k = 1, per the d-table", ok)
    return ok
