"""primer.classification-real-clifford-algebras: exact checks.

For every nondegenerate signature (p, q) with n = p + q <= 7 (36 signatures, every residue
d = p - q mod 8 at several dimensions) the Wedderburn type of Cl(p, q) is computed from exact
invariants and compared with the clock table:
  (a) semisimplicity: the trace form tau(xy) (scalar part) is diagonal in the blade basis with
      entries e_I^2 = +-1, so it is nondegenerate and the algebra is semisimple;
  (b) the centre: [e_i, e_I] is 0 or 2 e_i e_I, and distinct blades go to distinct blades, so the
      centre is spanned by the blades commuting with every generator; its square class omega^2
      decides R, C or R + R;
  (c) a primitive idempotent f = prod (1 + b_j)/2 over commuting blades b_j of square +1 (seeded
      with omega in the split case, so that f lies in one simple ideal), and its corner f A f,
      identified exactly as R (dimension 1), C (f and u with u^2 = -f) or H (f, u, v, uv with
      u^2 = v^2 = -f, uv = -vu); a corner that is a division algebra certifies that f is primitive;
  (d) k from 2^n = (number of summands) k^2 dim D, confirmed independently by dim(A f) = k dim D.
EXPORTS["clifford_type"] returns the computed type for reuse by the checks that import this table.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise  # noqa: F401  (no premises: the primer proves the table)


def _sq(p, q):
    return GA.sig(p, q)


def _blade_vec(x, blades):
    return [x.get(b, F(0)) for b in blades]


def _rank(elems, blades):
    rows = [_blade_vec(x, blades) for x in elems if x]
    return GA.field_rank(rows) if rows else 0


def _central_blades(n, sq):
    out = []
    for b in GA.all_blades(n):
        e = {b: F(1)}
        if all(GA.commutes(GA.gen(i), e, sq) for i in range(n)):
            out.append(b)
    return out


def _primitive_idempotent(n, sq, seed=None):
    f = GA.sc(1)
    chosen = []
    cands = ([seed] if seed is not None else []) + [b for b in GA.all_blades(n) if b]
    for b in cands:
        e = {b: F(1)}
        if not GA.eq(GA.mul(e, e, sq), GA.sc(1)):
            continue
        if not all(GA.commutes(e, c, sq) for c in chosen):
            continue
        g = GA.mul(f, GA.scal(F(1, 2), GA.add(GA.sc(1), e)), sq)
        if GA.is_zero(g) or GA.eq(g, f):
            continue
        f = g
        chosen.append(e)
    return f


def _corner_type(f, n, sq, blades):
    """Identify f A f exactly; returns (label, dimension) or (None, dim) if not a division algebra."""
    elems = []
    for b in blades:
        x = GA.mul(GA.mul(f, {b: F(1)}, sq), f, sq)
        if x and not any(GA.eq(x, y) or GA.eq(x, GA.neg(y)) for y in elems):
            elems.append(x)
    dim = _rank(elems, blades)
    negf = GA.neg(f)
    if dim == 1:
        return ("R", 1)
    if dim == 2:
        for u in elems:
            if GA.eq(GA.mul(u, u, sq), negf) and _rank([f, u], blades) == 2:
                return ("C", 2)
        return (None, 2)
    if dim == 4:
        imag = [u for u in elems if GA.eq(GA.mul(u, u, sq), negf)]
        for u in imag:
            for v in imag:
                uv = GA.mul(u, v, sq)
                if GA.eq(uv, GA.neg(GA.mul(v, u, sq))) and _rank([f, u, v, uv], blades) == 4:
                    return ("H", 4)
        return (None, 4)
    return (None, dim)


def clifford_type(p, q):
    """Exact Wedderburn type of Cl(p, q): dict with keys
    semisimple, centre ('R', 'C', 'R+R'), D ('R', 'C', 'H'), summands (1 or 2), k, left_ideal_dim."""
    n = p + q
    sq = _sq(p, q)
    blades = GA.all_blades(n)
    semisimple = all(GA.mul({b: F(1)}, {b: F(1)}, sq) in ({(): F(1)}, {(): F(-1)}) for b in blades)
    cb = _central_blades(n, sq)
    omega = tuple(range(n))
    seed = None
    if cb == [()]:
        centre = "R"
    elif n >= 1 and cb == [(), omega]:
        w2 = GA.mul({omega: F(1)}, {omega: F(1)}, sq)
        centre = "C" if GA.eq(w2, GA.sc(-1)) else "R+R"
        if centre == "R+R":
            seed = omega
    else:
        centre = None
    f = _primitive_idempotent(n, sq, seed)
    D, ddim = _corner_type(f, n, sq, blades)
    summands = 2 if centre == "R+R" else 1
    total = 2 ** n
    k = None
    if D is not None and total % (summands * ddim) == 0:
        k2 = total // (summands * ddim)
        r = 0
        while r * r < k2:
            r += 1
        k = r if r * r == k2 else None
    left = _rank([GA.mul({b: F(1)}, f, sq) for b in blades], blades)
    return {"semisimple": semisimple, "centre": centre, "D": D, "summands": summands, "k": k,
            "left_ideal_dim": left, "f": f}


EXPORTS = {"clifford_type": clifford_type}


def check_classification_table():
    # the clock table, d = p - q mod 8: (division algebra, number of simple summands)
    table = {0: ("R", 1), 1: ("R", 2), 2: ("R", 1), 3: ("C", 1),
             4: ("H", 1), 5: ("H", 2), 6: ("H", 1), 7: ("C", 1)}
    dimD = {"R": 1, "C": 2, "H": 4}
    ok = True
    count = 0
    seen = set()
    for n in range(0, 8):
        for p in range(n + 1):
            q = n - p
            t = clifford_type(p, q)
            D, s = table[(p - q) % 8]
            k = t["k"]
            ok = ok and t["semisimple"] and t["D"] == D and t["summands"] == s and k is not None
            ok = ok and s * k * k * dimD[D] == 2 ** n
            # Wedderburn: a primitive left ideal of Mat_k(D) has dimension k dim D
            ok = ok and t["left_ideal_dim"] == k * dimD[D]
            # simple exactly off p - q = 1 mod 4: centre a field there, R + R on it
            ok = ok and ((t["centre"] == "R+R") == ((p - q) % 4 == 1))
            want_centre = "R+R" if s == 2 else ("C" if D == "C" else "R")
            ok = ok and t["centre"] == want_centre
            count += 1
            seen.add((p - q) % 8)
    ok = ok and count == 36 and len(seen) == 8
    GA.check("Cl(p,q) has the clock-table Wedderburn type for all n <= 7", ok)
    return ok


def check_split_summands_isomorphic_and_simple():
    ok = True
    hits = 0
    for (p, q) in ((1, 0), (0, 3), (2, 1), (5, 0), (1, 4), (3, 2), (0, 7), (2, 5)):
        n = p + q
        sq = GA.sig(p, q)
        omega = {tuple(range(n)): F(1)}
        ep = GA.scal(F(1, 2), GA.add(GA.sc(1), omega))
        em = GA.scal(F(1, 2), GA.sub(GA.sc(1), omega))
        ok = ok and (p - q) % 4 == 1
        # central orthogonal idempotents summing to 1: the two ideals
        ok = ok and GA.eq(GA.mul(ep, ep, sq), ep) and GA.is_zero(GA.mul(ep, em, sq))
        ok = ok and GA.eq(GA.add(ep, em), GA.sc(1))
        ok = ok and all(GA.commutes(GA.gen(i), ep, sq) for i in range(n))
        # the grade involution (an automorphism) exchanges them, so the two ideals are isomorphic
        ok = ok and GA.eq(GA.grade_inv(ep), em)
        # each ideal has dimension 2^(n-1) and centre R eps (a field), so it is simple
        blades = GA.all_blades(n)
        ideal = [GA.mul(ep, {b: F(1)}, sq) for b in blades]
        ok = ok and _rank(ideal, blades) == 2 ** (n - 1)
        cz = [GA.mul(ep, {b: F(1)}, sq) for b in _central_blades(n, sq)]
        ok = ok and len(cz) == 2 and _rank(cz, blades) == 1
        hits += 1
    ok = ok and hits == 8
    GA.check("in the split signatures the two simple summands are exchanged by the grade involution", ok)
    return ok
