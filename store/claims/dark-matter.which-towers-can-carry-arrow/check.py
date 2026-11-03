"""dark-matter.which-towers-can-carry-arrow: exact checks.

(a) Who carries: every signature of an odd residue is odd-dimensional (p - q and p + q have one
parity), so by the flag-bit theorem no odd residue is oriented, on any window. The even residues'
P3 representatives (census of towers-are-residues) are all four-dimensional, so oriented
(n = 0 mod 4); among them min(p,q) = 1 exactly at r = 6, 2, r = 4 has no time ((4,0), (0,4)) and
r = 0 has two ((2,2)). Oriented and causal: {2, 6}.
(b) The fork (2,2), in GA.py: the ambient R^(3,3) has omega^2 = +1 (no complex unit in its centre); a
primitive idempotent f of the even subalgebra Cl^0(3,3), built greedily from commuting even blades of
square +1, has Cl^0 f of real dimension 4 and corner f Cl^0 f = R (one-dimensional), the real
four-component spinors; three mutually orthogonal null vectors e_i + e_(3+i) span U with
dim U^perp = 6 - 3 (three pairs, the maximum). Cl^0(2,2): its pseudoscalar is central in it with square
+1, splitting it into two four-dimensional ideals (the two SL(2,R) factors).
(c) Mass begins at two: with a small exact polynomial ring, det(pi1 pt1^T) = 0 identically and
det(pi1 pt1^T + pi2 pt2^T) = <pi1 pi2><pt1 pt2> as a polynomial identity in the eight coordinates.
The Standard-Model gauge algebra on the fork (standard-model.four-dimensions-forces-converse) is cited,
not computed: no premise() call for it.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SIGS = [(p, q) for p in range(11) for q in range(11) if 1 <= p + q <= 10]

# --- a minimal multivariate polynomial ring over Q: {exponent tuple: Fraction} ---
NV = 8


def var(i):
    e = [0] * NV
    e[i] = 1
    return {tuple(e): F(1)}


def padd(a, b, s=1):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + s * v
    return {k: v for k, v in out.items() if v != 0}


def pmul(a, b):
    out = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            k = tuple(x + y for x, y in zip(k1, k2))
            out[k] = out.get(k, F(0)) + v1 * v2
    return {k: v for k, v in out.items() if v != 0}


def even_corner(p, q):
    n = p + q
    sq = GA.sig(p, q)
    ev = [b for b in GA.all_blades(n) if len(b) % 2 == 0]

    def co(x):
        return [x.get(b, F(0)) for b in ev]

    def dim_left(f):
        return GA.rank_of_vectors([co(GA.mul({b: F(1)}, f, sq)) for b in ev])
    f, dim, chosen = GA.sc(1), len(ev), []
    for b in ev:
        if b and GA.mul({b: F(1)}, {b: F(1)}, sq) == {(): F(1)} and \
                all(GA.commutes({b: F(1)}, {c: F(1)}, sq) for c in chosen):
            f2 = GA.mul(f, GA.scal(F(1, 2), GA.add(GA.sc(1), {b: F(1)})), sq)
            d2 = dim_left(f2)
            if 0 < d2 < dim:
                f, dim, chosen = f2, d2, chosen + [b]
    corner = GA.rank_of_vectors([co(GA.mul(GA.mul(f, {b: F(1)}, sq), f, sq)) for b in ev])
    return f, dim, corner


def check_oriented_and_causal_towers():
    premise("dark-matter.flag-bit-exists-exactly-tower-dimension")
    premise("dark-matter.towers-are-residues-single-clock-filter")
    ok = all(((p - q) % 2) == ((p + q) % 2) for p, q in SIGS)
    odd_dims = {r: {p + q for p, q in SIGS if (p - q) % 8 == r} for r in (1, 3, 5, 7)}
    ok = ok and all(all(d % 2 == 1 for d in ds) for ds in odd_dims.values())
    p3 = {r: sorted(s for s in SIGS if sum(s) == 4 and (s[0] - s[1]) % 8 == r) for r in (0, 2, 4, 6)}
    oriented = sorted(r for r in p3 if all((p + q) % 4 == 0 for p, q in p3[r]))
    times = {r: sorted({min(p, q) for p, q in p3[r]}) for r in p3}
    ok = ok and oriented == [0, 2, 4, 6] and times == {0: [2], 2: [1], 4: [0], 6: [1]}
    both = sorted(r for r in oriented if 1 in times[r])
    ok = ok and both == [2, 6]
    GA.check("cor:whocarries: odd residues odd-dimensional (never oriented); even P3 representatives "
             "four-dimensional; oriented and causal exactly {2, 6}", ok)
    return ok


def check_fork_conformal_spinors_are_real():
    sq = GA.sig(3, 3)
    om = {tuple(range(6)): F(1)}
    ok = GA.eq(GA.mul(om, om, sq), GA.sc(1))
    f, dim, corner = even_corner(3, 3)
    ok = ok and GA.eq(GA.mul(f, f, sq), f) and dim == 4 and corner == 1
    # three mutually orthogonal null vectors, and U^perp of dimension 3
    us = [[F(1) if k in (i, 3 + i) else F(0) for k in range(6)] for i in range(3)]
    ip = lambda a, b: sum(F(sq[k]) * a[k] * b[k] for k in range(6))
    ok = ok and all(ip(a, b) == 0 for a in us for b in us)
    perp = 6 - GA.rank_of_vectors([[F(sq[k]) * u[k] for k in range(6)] for u in us])
    ok = ok and perp == 3
    # Cl^0(2,2): the pseudoscalar is central in the even part and squares to +1
    sq22 = GA.sig(2, 2)
    om4 = {(0, 1, 2, 3): F(1)}
    ev = [b for b in GA.all_blades(4) if len(b) % 2 == 0]
    ok = ok and GA.eq(GA.mul(om4, om4, sq22), GA.sc(1))
    ok = ok and all(GA.commutes(om4, {b: F(1)}, sq22) for b in ev)
    for s in (1, -1):
        P = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.scal(s, om4)))
        ok = ok and GA.rank_of_vectors([[GA.mul(P, {b: F(1)}, sq22).get(c, F(0)) for c in ev] for b in ev]) == 4
    GA.check("fork: Cl(3,3) has omega^2 = +1; Cl^0(3,3) f has dimension 4 with corner R; three pairs; Cl^0(2,2) "
             "splits into two four-dimensional ideals", ok)
    return ok


def check_mass_begins_at_two_on_the_fork():
    p1 = [var(0), var(1)]
    t1 = [var(2), var(3)]
    p2 = [var(4), var(5)]
    t2 = [var(6), var(7)]

    def det2(M):
        return padd(pmul(M[0][0], M[1][1]), pmul(M[0][1], M[1][0]), -1)

    def outer(a, b):
        return [[pmul(a[i], b[j]) for j in range(2)] for i in range(2)]
    single = det2(outer(p1, t1))
    O1, O2 = outer(p1, t1), outer(p2, t2)
    two = det2([[padd(O1[i][j], O2[i][j]) for j in range(2)] for i in range(2)])
    br = pmul(padd(pmul(p1[0], p2[1]), pmul(p1[1], p2[0]), -1), padd(pmul(t1[0], t2[1]), pmul(t1[1], t2[0]), -1))
    ok = single == {} and padd(two, br, -1) == {} and len(two) == 4
    GA.check("cor:whocarries: det(pi pt^T) = 0 and det(pi1 pt1^T + pi2 pt2^T) = <pi1 pi2><pt1 pt2> "
             "(polynomial identity)", ok)
    return ok
