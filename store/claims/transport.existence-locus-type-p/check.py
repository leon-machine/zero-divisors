"""transport.existence-locus-type-p: exact checks.

(1) For every signature with n = p + q <= 6: a non-central idempotent exists exactly off
    {(0,0), (0,1), (0,2), (1,0), (0,3)}. Existence by a blade u with u^2 = +1 that fails to commute
    with some generator: e = (1 + u)/2 is idempotent and non-central (both computed). Absence on the
    five: by Proposition transport.exceptional-division-algebras the algebra is a sum of at most two
    division algebras, so every idempotent is a sum of the central projectors eps; the check lists
    those sums and confirms they are idempotent and central, and that no blade with square +1 is
    non-central there. The verdict is compared with "k >= 2" read from the d-table of
    transport.classification-real-clifford-algebras (the matrix unit E_11 exists iff k >= 2).
(2) The concrete form: for invertible orthogonal vectors a, b (non-basis samples) in mixed
    signatures, (ab)^2 = -a^2 b^2; when a^2 b^2 = -1 the element (1 + ab)/2 is a non-central
    idempotent, and when a^2 b^2 = +1 (two spacelike factors) (ab)^2 = -1 and no idempotent arises.
    In negative-definite signature with q >= 4, u = e1e2e3e4 has u^2 = +1 and is non-central.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = [(p, n - p) for n in range(0, 7) for p in range(n + 1)]
# orthogonal pairs (p, q, a, b) as coordinate lists, a . b = 0 by construction
PAIRS = [
    (1, 1, [2, 1], [1, 2]),
    (1, 3, [5, 0, 4, 0], [4, 0, 5, 0]),
    (1, 3, [0, 1, 2, 0], [0, 2, -1, 0]),
    (2, 2, [1, 0, 2, 0], [2, 0, 1, 0]),
    (3, 1, [1, 1, 0, 0], [1, -1, 0, 2]),
    (2, 1, [3, 4, 0], [0, 0, 1]),
    (2, 1, [1, 0, 0], [0, 1, 0]),
]


def vec(c):
    return GA.add(*[GA.scal(x, GA.gen(i)) for i, x in enumerate(c) if x])


def central(x, n, sq):
    return all(GA.commutes(GA.gen(i), x, sq) for i in range(n))


def noncentral_idempotent(p, q):
    n = p + q
    sq = GA.sig(p, q)
    for b in GA.all_blades(n):
        if not b:
            continue
        u = {b: F(1)}
        if GA.eq(GA.mul(u, u, sq), GA.sc(1)) and not central(u, n, sq):
            return GA.scal(F(1, 2), GA.add(GA.sc(1), u))
    return None


def check_noncentral_idempotent_exactly_off_the_five():
    premise("transport.classification-real-clifford-algebras")
    table = [("R", 1), ("R", 2), ("R", 1), ("C", 1), ("H", 1), ("H", 2), ("H", 1), ("C", 1)]
    dimD = {"R": 1, "C": 2, "H": 4}
    ok = True
    missing = []
    for p, q in SIGS:
        n = p + q
        sq = GA.sig(p, q)
        e = noncentral_idempotent(p, q)
        if e is None:
            missing.append((p, q))
        else:
            ok = ok and GA.eq(GA.mul(e, e, sq), e) and not central(e, n, sq)
        D, s = table[(p - q) % 8]
        k2 = 2 ** n // (s * dimD[D])
        ok = ok and ((e is None) == (k2 == 1))
    ok = ok and sorted(missing) == [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0)]
    GA.check("a non-central idempotent exists exactly off the five, iff k >= 2 in the d-table (n <= 6)", ok)
    return ok


def check_idempotents_of_the_five_are_central():
    premise("transport.exceptional-division-algebras")
    ok = True
    for p, q in ((0, 0), (0, 1), (0, 2), (1, 0), (0, 3)):
        n = p + q
        sq = GA.sig(p, q)
        if (p, q) in ((1, 0), (0, 3)):
            w = {tuple(range(n)): F(1)}
            eps = [GA.scal(F(1, 2), GA.add(GA.sc(1), w)), GA.scal(F(1, 2), GA.sub(GA.sc(1), w))]
            combos = [{}, eps[0], eps[1], GA.add(eps[0], eps[1])]
        else:
            combos = [{}, GA.sc(1)]
        for e in combos:
            ok = ok and GA.eq(GA.mul(e, e, sq), e) and central(e, n, sq)
        ok = ok and len(combos) == (4 if (p, q) in ((1, 0), (0, 3)) else 2)
    GA.check("in the five exceptional algebras the idempotents (sums of the eps) are all central", ok)
    return ok


def check_orthogonal_vector_pair_gives_type_p():
    ok = True
    for p, q, ac, bc in PAIRS:
        n = p + q
        sq = GA.sig(p, q)
        a, b = vec(ac), vec(bc)
        ok = ok and GA.dot(a, b, sq) == 0
        a2, b2 = GA.dot(a, a, sq), GA.dot(b, b, sq)
        ab = GA.mul(a, b, sq)
        ok = ok and GA.eq(GA.mul(ab, ab, sq), GA.sc(-a2 * b2))
        if a2 * b2 < 0:
            # normalise u = ab / sqrt(-a2 b2): pick samples with -a2 b2 a perfect square
            r = -a2 * b2
            root = next(F(k) for k in range(1, 200) if F(k) * F(k) == r)
            u = GA.scal(1 / root, ab)
            e = GA.scal(F(1, 2), GA.add(GA.sc(1), u))
            ok = ok and GA.eq(GA.mul(u, u, sq), GA.sc(1))
            ok = ok and GA.eq(GA.mul(e, e, sq), e) and not central(e, n, sq)
        else:
            ok = ok and GA.mul(ab, ab, sq).get((), F(0)) < 0
    # the sign rule on the samples: five mixed pairs (a^2 b^2 < 0), two same-sign pairs
    signs = [GA.dot(vec(a), vec(a), GA.sig(p, q)) * GA.dot(vec(b), vec(b), GA.sig(p, q)) < 0
             for p, q, a, b in PAIRS]
    ok = ok and signs.count(True) == 5
    # negative definite, q >= 4: u = e1e2e3e4
    for q in (4, 5, 6):
        sq = GA.sig(0, q)
        u = {(0, 1, 2, 3): F(1)}
        ok = ok and GA.eq(GA.mul(u, u, sq), GA.sc(1)) and not central(u, q, sq)
    GA.check("orthogonal a, b with a^2 b^2 < 0 give the non-central idempotent (1 + ab/|ab|)/2", ok)
    return ok
