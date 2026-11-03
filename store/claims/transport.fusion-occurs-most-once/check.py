"""transport.fusion-occurs-most-once: exact checks.

Residue d = p - q mod 8. Type C is detected in GA, not read from a table: Cl(p,q) is type C iff its
volume element omega is central with omega^2 = +1 (computed blade-exactly; for even n omega anticommutes
with the generators and the centre is R).
(1) For every (p,q) with 1 <= n <= 10: type C (computed) holds exactly when d = 1 mod 4. Rule 1
    (p,q) -> (p+1,q+1) keeps d; Rule 2 on a type-C algebra, (p,q) -> (p+1,q) or (p,q+1), moves d by +-1,
    taking residue 1 into {0, 2} and residue 5 into {4, 6}, and the image is never type C (computed).
(2) Every transport history of length <= 6 from every start with n <= 4 (Rule 2 allowed only where type
    C is computed): at most one Rule-2 step; the residue is constant after it; histories with exactly one
    Rule-2 step exist exactly from the type-C starts (1,0), (2,1), (0,3); the number of histories is
    counted (one per length from the other 12 starts, 2j + 1 at length j from each type-C start).
(3) Rule 1 is matrix amplification: in Cl(p+1,q+1) the twisted generators e_i E (E = e+ e-) satisfy the
    relations of Cl(p,q), commute with e+ and e- (which generate Cl(1,1) = Mat_2(R), with matrix units
    built from the null pair), and the products span all 2^(n+2) blades, for every (p,q) with n <= 4.
    Physical lineage: Cl(1+k,3+k), k <= 2, has residue 6 and centre R (blade-wise), so Rule 2 never fires.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

STARTS = [(p, n - p) for n in range(1, 5) for p in range(n + 1)]


def omega(n):
    return {tuple(range(n)): F(1)}


def type_c(p, q):
    n = p + q
    S = GA.sig(p, q)
    w = omega(n)
    central = all(GA.commutes(w, GA.gen(i), S) for i in range(n))
    return central and GA.eq(GA.mul(w, w, S), GA.sc(1))


def central_blades(p, q):
    n = p + q
    S = GA.sig(p, q)
    return [b for b in GA.all_blades(n)
            if all(GA.commutes({b: F(1)}, GA.gen(i), S) for i in range(n))]


def check_residues_and_type_c_sites():
    premise("transport.existence-classification-type-c")
    premise("transport.rule-1-morita-trivial")
    ok = True
    sites = []
    for n in range(1, 11):
        for p in range(n + 1):
            q = n - p
            d = (p - q) % 8
            tc = type_c(p, q)
            ok = ok and tc == (d % 4 == 1)
            if tc:
                sites.append(d)
                images = {(p + 1 - q) % 8, (p - q - 1) % 8}
                ok = ok and images == ({0, 2} if d == 1 else {4, 6})
                ok = ok and not type_c(p + 1, q) and not type_c(p, q + 1)
            ok = ok and (p + 1 - (q + 1)) % 8 == d
    ok = ok and sorted(set(sites)) == [1, 5] and len(sites) == 15
    _tp_rv = (ok); assert _tp_rv is not False, "check_residues_and_type_c_sites"; return _tp_rv


def check_histories_fuse_at_most_once():
    premise("transport.existence-classification-type-c")
    ok = True
    fused_starts = set()
    nhist = 0
    for start in STARTS:
        frontier = [(start, 0, None)]          # (signature, number of Rule-2 steps, residue after it)
        for _ in range(6):
            nxt = []
            for (sg, k, dfix) in frontier:
                p, q = sg
                moves = [((p + 1, q + 1), 0)]
                if type_c(p, q):
                    moves += [((p + 1, q), 1), ((p, q + 1), 1)]
                for (s2, r2) in moves:
                    k2 = k + r2
                    d2 = (s2[0] - s2[1]) % 8
                    ok = ok and k2 <= 1
                    if dfix is not None:
                        ok = ok and d2 == dfix
                    nxt.append((s2, k2, d2 if k2 == 1 else None))
                    if k2 == 1:
                        fused_starts.add(start)
            frontier = nxt
            nhist += len(frontier)
    ok = ok and sorted(fused_starts) == [(0, 3), (1, 0), (2, 1)]
    # three type-C starts each give 3 histories of length 1, 5 of length 2, ... (2j + 1 at length j)
    ok = ok and nhist == (len(STARTS) - 3) * 6 + 3 * sum(2 * j + 1 for j in range(1, 7))
    _tp_rv = (ok); assert _tp_rv is not False, "check_histories_fuse_at_most_once"; return _tp_rv


def check_rule_one_amplification_and_lineage():
    premise("transport.rule-1-morita-trivial")
    premise("transport.classification-real-clifford-algebras")
    ok = True
    for (p, q) in STARTS:
        n = p + q
        S = GA.sig(p, q) + (1, -1)
        ep, em = GA.gen(n), GA.gen(n + 1)
        E = GA.mul(ep, em, S)
        tw = [GA.mul(GA.gen(i), E, S) for i in range(n)]
        for i in range(n):
            ok = ok and GA.eq(GA.mul(tw[i], tw[i], S), GA.sc(S[i]))
            ok = ok and GA.commutes(tw[i], ep, S) and GA.commutes(tw[i], em, S)
            for j in range(i + 1, n):
                ok = ok and GA.anticommutes(tw[i], tw[j], S)
        # Cl(1,1) = Mat_2(R): null pair f, f*, idempotent f* f, matrix units
        f = GA.scal(F(1, 2), GA.add(ep, em))
        fs = GA.scal(F(1, 2), GA.sub(ep, em))
        ok = ok and GA.is_zero(GA.mul(f, f, S)) and GA.is_zero(GA.mul(fs, fs, S))
        ok = ok and GA.eq(GA.add(GA.mul(f, fs, S), GA.mul(fs, f, S)), GA.sc(1))
        # spanning: products of twisted blades with {1, e+, e-, e+e-} span 2^(n+2)
        vecs = []
        allb = GA.all_blades(n + 2)
        for b in GA.all_blades(n):
            x = GA.sc(1)
            for i in b:
                x = GA.mul(x, tw[i], S)
            for y in (GA.sc(1), ep, em, E):
                z = GA.mul(x, y, S)
                vecs.append([z.get(c, F(0)) for c in allb])
        ok = ok and GA.rank_of_vectors(vecs) == 2 ** (n + 2)
    for k in range(3):
        p, q = 1 + k, 3 + k
        ok = ok and (p - q) % 8 == 6 and central_blades(p, q) == [()] and not type_c(p, q)
    _tp_rv = (ok); assert _tp_rv is not False, "check_rule_one_amplification_and_lineage"; return _tp_rv
