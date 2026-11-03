"""transport.classification-idempotent-orbits: exact checks on Cl(1,1) = Mat_2(R), Cl(2,2) = Mat_4(R),
Cl(1,2) = Mat_2(C), Cl(1,3) = Mat_2(H) (simple) and Cl(2,1) = Mat_2(R) + Mat_2(R) (split).

Idempotents: products of choices from {1, P_i, 1 - P_i} over the hyperbolic pairs (e_i, e_j) of the
signature (P_i = v v*, v = (e_i + e_j)/2, v* = (e_i - e_j)/2), times {1, eps_+, eps_-} in the split
case (eps_+- = (1 +- omega)/2), and the non-coordinate idempotents e + e a (1 - e) for a sample a.
Rank: dim_R(eA) = rank(e) m dim_R D with m, D from the classification (rank pair via eps_+- eA in the
split case).
(1) For every ordered pair of idempotents (e, e') of each algebra the linear space {g : g e = e' g}
is computed; it contains an invertible element (found among fixed combinations of a kernel basis and
verified invertible by the rank of x -> g x) exactly when the rank data agree. When they differ no
conjugator can exist, since dim(g e g^{-1} A) = dim(eA).
(2) Hence e ~ 1 - e exactly for balanced e (rank m/2, componentwise in the split case); checked
directly for every idempotent.
(3) An idempotent is central iff conjugation by every unit fixes it; the basis blades are units that
span A (the units-span fact), so this is iff it commutes with every blade. Checked for every
idempotent: the singleton orbits are exactly the central idempotents (0, 1, and eps_+- and their
complements in the split case), and every non-central one is moved by some blade.
"""
from fractions import Fraction as F
from itertools import product
import GA
from tp_premise import premise

# (p, q, hyperbolic pairs (index of square +1, index of square -1))
ALGEBRAS = [(1, 1, [(0, 1)]), (2, 2, [(0, 2), (1, 3)]), (1, 2, [(0, 1)]), (1, 3, [(0, 1)]), (2, 1, [(0, 2)])]
DIM_D = {0: 1, 1: 1, 2: 1, 3: 2, 4: 4, 5: 4, 6: 4, 7: 2}


def classify(p, q):
    """(split, m, dim D) from the classification table and dim Cl = 2^n."""
    d = (p - q) % 8
    split = d in (1, 5)
    dD = DIM_D[d]
    comp = 2 ** (p + q) // (2 if split else 1)
    m = [k for k in range(1, 17) if k * k * dD == comp]
    return split, m[0], dD


def rank(xs, n):
    bl = GA.all_blades(n)
    return GA.rank_of_vectors([[x.get(b, F(0)) for b in bl] for x in xs])


def right_ideal_dim(e, sq, n):
    return rank([GA.mul(e, {b: F(1)}, sq) for b in GA.all_blades(n)], n)


def idempotents(p, q, pairs):
    sq = GA.sig(p, q)
    n = p + q
    Ps = []
    for (i, j) in pairs:
        v = GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(j)))
        vs = GA.scal(F(1, 2), GA.sub(GA.gen(i), GA.gen(j)))
        P = GA.mul(v, vs, sq)
        Ps.append([GA.sc(1), P, GA.sub(GA.sc(1), P)])
    split = n % 2 == 1 and GA.eq(GA.mul({tuple(range(n)): F(1)}, {tuple(range(n)): F(1)}, sq), GA.sc(1))
    cent = [GA.sc(1)]
    if split:
        om = {tuple(range(n)): F(1)}
        cent += [GA.scal(F(1, 2), GA.add(GA.sc(1), om)), GA.scal(F(1, 2), GA.sub(GA.sc(1), om))]
    out = [{}]
    for c in cent:
        for choice in product(*Ps):
            e = c
            for x in choice:
                e = GA.mul(e, x, sq)
            out.append(e)
    # non-coordinate idempotents e + e a (1 - e)
    a = {b: F(len(b) + 1, 2) for b in GA.all_blades(n)}
    extra = []
    for e in out[2:4]:
        extra.append(GA.add(e, GA.mul(GA.mul(e, a, sq), GA.sub(GA.sc(1), e), sq)))
    uniq = []
    for e in out + extra:
        if not any(GA.eq(e, u) for u in uniq):
            uniq.append(e)
    return sq, n, uniq


def rank_data(e, sq, n, split, m, dD):
    if not split:
        r = right_ideal_dim(e, sq, n)
        assert r % (m * dD) == 0
        return (r // (m * dD),)
    om = {tuple(range(n)): F(1)}
    ep = GA.scal(F(1, 2), GA.add(GA.sc(1), om))
    em = GA.scal(F(1, 2), GA.sub(GA.sc(1), om))
    return tuple(right_ideal_dim(GA.mul(c, e, sq), sq, n) // (m * dD) for c in (ep, em))


def find_conjugator(e, e2, sq, n):
    bl = GA.all_blades(n)
    cols = []
    for b in bl:
        x = {b: F(1)}
        d = GA.sub(GA.mul(x, e, sq), GA.mul(e2, x, sq))
        cols.append([d.get(c, F(0)) for c in bl])
    rows = [list(r) for r in zip(*cols)]
    ker = GA.field_kernel(rows)
    for t in (2, 3, 5, 7, 11):
        coeff = [F(t) ** k for k in range(len(ker))]
        g = {}
        for c, kv in zip(coeff, ker):
            g = GA.add(g, {bl[j]: c * kv[j] for j in range(len(bl)) if kv[j] != 0})
        if g and right_ideal_dim(g, sq, n) == 2 ** n:
            return g
    return None


def check_orbits_are_rank_classes():
    premise("transport.classification-real-clifford-algebras")
    ok = True
    pairs_tested = 0
    for p, q, hp in ALGEBRAS:
        split, m, dD = classify(p, q)
        sq, n, ids = idempotents(p, q, hp)
        ok = ok and all(GA.eq(GA.mul(e, e, sq), e) for e in ids)
        data = [rank_data(e, sq, n, split, m, dD) for e in ids]
        for i, e in enumerate(ids):
            for j, e2 in enumerate(ids):
                g = find_conjugator(e, e2, sq, n)
                found = g is not None
                if found:
                    # verify: g invertible and g e = e' g
                    ok = ok and GA.eq(GA.mul(g, e, sq), GA.mul(e2, g, sq))
                ok = ok and found == (data[i] == data[j])
                pairs_tested += 1
    # the algebras' (split, m, dim D)
    ok = ok and [classify(p, q) for p, q, _ in ALGEBRAS] == [(False, 2, 1), (False, 4, 1), (False, 2, 2),
                                                             (False, 2, 4), (True, 2, 1)]
    ok = ok and pairs_tested > 100
    GA.check("idempotents are conjugate iff their rank data agree (simple and split cases)", ok)
    return ok


def check_complement_conjugate_iff_balanced():
    premise("transport.classification-real-clifford-algebras")
    ok = True
    balanced_seen = 0
    for p, q, hp in ALGEBRAS:
        split, m, dD = classify(p, q)
        sq, n, ids = idempotents(p, q, hp)
        for e in ids:
            c = GA.sub(GA.sc(1), e)
            rd = rank_data(e, sq, n, split, m, dD)
            rc = rank_data(c, sq, n, split, m, dD)
            ok = ok and (len(rd) == len(rc) and all(a + b == m for a, b in zip(rd, rc)))
            balanced = all(2 * a == m for a in rd)
            ok = ok and (find_conjugator(e, c, sq, n) is not None) == balanced
            balanced_seen += balanced
    ok = ok and balanced_seen >= 5
    GA.check("e and 1 - e are conjugate iff rank e = m - rank e (componentwise when split)", ok)
    return ok


def check_central_iff_singleton_orbit():
    premise("transport.units-span")
    ok = True
    central_count = {}
    for p, q, hp in ALGEBRAS:
        sq, n, ids = idempotents(p, q, hp)
        units = []
        for b in GA.all_blades(n):
            x = {b: F(1)}
            s = GA.mul(x, GA.reverse(x), sq)
            ok = ok and list(s) == [()] and s[()] != 0
            units.append((x, GA.scal(1 / s[()], GA.reverse(x))))
        ok = ok and rank([u for u, _ in units], n) == 2 ** n
        cnt = 0
        for e in ids:
            fixed = all(GA.eq(GA.mul(GA.mul(u, e, sq), ui, sq), e) for u, ui in units)
            central = all(GA.commutes(e, GA.gen(i), sq) for i in range(n))
            ok = ok and fixed == central
            cnt += central
        central_count[(p, q)] = cnt
    ok = ok and central_count == {(1, 1): 2, (2, 2): 2, (1, 2): 2, (1, 3): 2, (2, 1): 4}
    GA.check("an idempotent is central iff no unit moves it; the split case has the extra central pair", ok)
    return ok
