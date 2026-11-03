"""transport.existence-classification-type-c: exact checks.

Cl(p,q) in GA.py (p generators of square +1, then q of square -1), omega the volume element. For every
(p,q) with 1 <= n = p + q <= 7:
(1) The centre is computed blade by blade (a blade is central iff it commutes with every generator; the
    centre of a Clifford algebra is spanned by its central blades since conjugation by a generator is
    diagonal on blades). Its idempotents are solved for exactly: in span{1} they are 0, 1; in
    span{1, omega} with omega^2 = s, x = a + b omega is idempotent iff a^2 + s b^2 = a and 2ab = b, so a
    nontrivial one needs b != 0, a = 1/2 and s b^2 = 1/4, possible iff s > 0, then b = +-1/2. The
    computed criterion "nontrivial central idempotent exists" matches p - q = 1 mod 4 on all 35 (p,q).
(2) In those cases eps_+- = (1 +- omega)/2 are central idempotents, eps_+ eps_- = 0, eps_+ + eps_- = 1,
    the grade involution exchanges them, and conjugation by sample invertible elements (vectors and
    rotors) fixes each of them.
(3) The splitting: eps_+ A and eps_- A each have dimension 2^(n-1) and together span A (direct), each is a
    two-sided ideal (A eps_+ = eps_+ A), and the centre of eps_+ A is R eps_+ (computed), so each ideal
    has centre a field.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

GRID = [(p, n - p) for n in range(1, 8) for p in range(n + 1)]
ONE = GA.sc(1)


def vol(n):
    return {tuple(range(n)): F(1)}


def central_blades(S):
    n = len(S)
    return [b for b in GA.all_blades(n) if all(GA.commutes({b: F(1)}, GA.gen(i), S) for i in range(n))]


def nontrivial_central_idempotents(S):
    """Solve x^2 = x on the computed centre (dimension 1 or 2); return the nontrivial solutions."""
    cb = central_blades(S)
    if cb == [()]:
        return []
    assert len(cb) == 2
    w = {cb[1]: F(1)}
    s = GA.mul(w, w, S)[()]
    if s <= 0:
        return []
    b = F(1, 2)                      # s b^2 = 1/4 with s = 1
    if s * b * b != F(1, 4):
        return []
    return [GA.add(GA.sc(F(1, 2)), GA.scal(sg * b, w)) for sg in (1, -1)]


def rank(xs, n):
    bl = GA.all_blades(n)
    return GA.rank_of_vectors([[x.get(b, F(0)) for b in bl] for x in xs])


def check_type_c_iff_p_minus_q_one_mod_four():
    premise("transport.centre")
    premise("transport.sign")
    ok = len(GRID) == 35
    found = []
    for p, q in GRID:
        S = GA.sig(p, q)
        idem = nontrivial_central_idempotents(S)
        for e in idem:
            ok = ok and GA.eq(GA.mul(e, e, S), e) and not GA.is_zero(e) and not GA.eq(e, ONE)
        ok = ok and (len(idem) > 0) == ((p - q) % 4 == 1)
        if idem:
            found.append((p, q))
    ok = ok and found == [(1, 0), (0, 3), (2, 1), (1, 4), (3, 2), (5, 0), (0, 7), (2, 5), (4, 3), (6, 1)]
    _tp_rv = (ok); assert _tp_rv is not False, "check_type_c_iff_p_minus_q_one_mod_four"; return _tp_rv


def check_eps_pm_identities_and_exchange():
    premise("transport.centre")
    ok = True
    for p, q in GRID:
        if (p - q) % 4 != 1:
            continue
        S = GA.sig(p, q)
        n = p + q
        w = vol(n)
        ep = GA.scal(F(1, 2), GA.add(ONE, w))
        em = GA.scal(F(1, 2), GA.sub(ONE, w))
        ok = ok and GA.eq(GA.mul(ep, ep, S), ep) and GA.eq(GA.mul(em, em, S), em)
        ok = ok and GA.is_zero(GA.mul(ep, em, S)) and GA.eq(GA.add(ep, em), ONE)
        ok = ok and GA.eq(GA.grade_inv(ep), em) and GA.eq(GA.grade_inv(em), ep)
        ok = ok and all(GA.commutes(ep, GA.gen(i), S) for i in range(n))
        # conjugation by invertible elements: a vector of nonzero square and a rotor
        g = GA.add(GA.gen(0), GA.scal(2, GA.gen(n - 1))) if n > 1 else GA.gen(0)
        gg = GA.mul(g, g, S)[()]
        ginv = GA.scal(1 / gg, g)
        ok = ok and GA.eq(GA.mul(GA.mul(g, ep, S), ginv, S), ep)
        if n > 1:
            R = GA.add(GA.sc(F(3)), GA.mul(GA.gen(0), GA.gen(1), S))
            Rr = GA.reverse(R)
            nr = GA.mul(R, Rr, S)[()]
            ok = ok and GA.eq(GA.mul(GA.mul(R, ep, S), GA.scal(1 / nr, Rr), S), ep)
    _tp_rv = (ok); assert _tp_rv is not False, "check_eps_pm_identities_and_exchange"; return _tp_rv


def check_splitting_into_two_ideals():
    premise("transport.classification-real-clifford-algebras")
    ok = True
    for p, q in GRID:
        n = p + q
        if (p - q) % 4 != 1 or n > 5:
            continue
        S = GA.sig(p, q)
        w = vol(n)
        ep = GA.scal(F(1, 2), GA.add(ONE, w))
        em = GA.scal(F(1, 2), GA.sub(ONE, w))
        allb = [{b: F(1)} for b in GA.all_blades(n)]
        Ip = [GA.mul(ep, x, S) for x in allb]
        Im = [GA.mul(em, x, S) for x in allb]
        ok = ok and rank(Ip, n) == 2 ** (n - 1) and rank(Im, n) == 2 ** (n - 1)
        ok = ok and rank(Ip + Im, n) == 2 ** n
        ok = ok and all(GA.eq(GA.mul(ep, x, S), GA.mul(x, ep, S)) for x in allb)
        # centre of eps_+ A: z in eps_+ A commuting with every eps_+ e_i (solve on the span of Ip)
        bl = GA.all_blades(n)
        cols = []
        for x in Ip:
            row = []
            for i in range(n):
                c = GA.sub(GA.mul(x, GA.gen(i), S), GA.mul(GA.gen(i), x, S))
                row.extend(c.get(b, F(0)) for b in bl)
            cols.append(row)
        ker = GA.field_kernel([list(r) for r in zip(*cols)])
        cen = [GA.add(*[GA.scal(k[j], Ip[j]) for j in range(len(Ip)) if k[j]]) for k in ker]
        ok = ok and rank(cen, n) == 1 and rank(cen + [ep], n) == 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_splitting_into_two_ideals"; return _tp_rv
