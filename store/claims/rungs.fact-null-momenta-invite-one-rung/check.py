"""rungs.fact-null-momenta-invite-one-rung: exact checks.

Null momenta p = e0 + n (n a rational unit spatial vector) in R^(1,3) subset Cl(1,3) (e0^2 = +1).
(1) No equivariant element-level inverse. For two null momenta, and in Cl(1,3) itself, in its one-vector
    extensions Cl(1,4), Cl(2,3) and in the rung Cl(2,4): the null rotations R_w = 1 + p w/2 (w spacelike,
    w . p = 0; two such w) are rotors fixing p, and the linear system
        p s p = p,  R_w s R_w~ = s  (both w)
    for an unknown element s of the whole algebra has no solution (exact rank test: the augmented rank
    exceeds the coefficient rank), while p s p = p alone is solvable. So no pseudo-inverse of p is fixed by
    the stabiliser of p in Spin^0(1,3), in any of these algebras: p stays a zero divisor (p^2 = 0 there).
(2) One rung for all momenta. In Cl(2,4) (e+ at index 4 square +1, e- at 5 square -1, n0 = (e- - e+)/2,
    ninf = e- + e+) the lifts X(x) = n0 + x + Q(x) ninf/2 of six null momenta are all null; the lift of 0
    and the lifts of the first k momenta span min(k + 1, 5) dimensions (null lifts lie in span{n0, e0..e3}),
    so the six null lifts plus the lift of 0 span 5, and with one non-null point (which uses ninf) all 6:
    every momentum lifts into the same R^(2,4), which does not grow with n. Its adjoined plane has Gram
    signature (1,1). Minimality and uniqueness of the rung are imported, not tested.
(3) The transported reciprocal iota(a n0 + x + b ninf) = 2b n0 + x + (a/2) ninf preserves the quadric, is an
    involution, and sends every X(p^i) to p^i + ninf/2 (n0-coefficient 0: an ideal point), all six at once;
    on a non-null x it returns X(x/Q(x)) up to the scale Q(x).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S13 = GA.sig(1, 3)
MOMENTA = [(1, F(3, 5), F(4, 5), 0), (1, 0, 0, 1), (1, F(5, 13), 0, F(12, 13)),
           (1, F(-2, 3), F(1, 3), F(2, 3)), (1, 0, F(-1), 0), (1, F(2, 7), F(3, 7), F(-6, 7))]


def v(c):
    return {(i,): F(x) for i, x in enumerate(c) if x != 0}


def perp_spacelike(c):
    """Two independent spatial vectors orthogonal to n (cross products of n with basis vectors): spacelike and
    orthogonal to p = e0 + n."""
    n = c[1:]
    basis = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    ws = []
    for b in basis:
        cr = (n[1] * b[2] - n[2] * b[1], n[2] * b[0] - n[0] * b[2], n[0] * b[1] - n[1] * b[0])
        if any(x != 0 for x in cr) and len(ws) < 2:
            if not ws or GA.rank_of_vectors([list(ws[0]), list(cr)]) == 2:
                ws.append(cr)
    return [(0,) + w for w in ws]


def lin_system(S, nvars, p, Rs):
    blades = GA.all_blades(nvars)
    idx = {b: i for i, b in enumerate(blades)}
    N = len(blades)
    rows, rhs = [], []
    # p s p = p
    cols = [GA.mul(GA.mul(p, {b: F(1)}, S), p, S) for b in blades]
    for t in blades:
        rows.append([cols[j].get(t, F(0)) for j in range(N)])
        rhs.append(p.get(t, F(0)))
    base_rows = (rows[:], rhs[:])
    for (R, Rt) in Rs:
        cols = [GA.sub(GA.mul(GA.mul(R, {b: F(1)}, S), Rt, S), {b: F(1)}) for b in blades]
        for t in blades:
            rows.append([cols[j].get(t, F(0)) for j in range(N)])
            rhs.append(F(0))
    return base_rows, (rows, rhs), idx


def solvable(rows, rhs):
    aug = [r + [c] for r, c in zip(rows, rhs)]
    return GA.rank_of_vectors(aug) == GA.rank_of_vectors(rows)


def check_no_equivariant_pseudo_inverse_in_any_extension():
    premise("rungs.imported-totality-minimality-completion")
    ok = True
    for S in [S13, S13 + (-1,), S13 + (1,), S13 + (1, -1)]:      # Cl(1,3), Cl(1,4), Cl(2,3), Cl(2,4)
        n = len(S)
        for c in MOMENTA[:2]:
            p = v(c)
            ok = ok and GA.is_zero(GA.mul(p, p, S))
            Rs = []
            for w in perp_spacelike(c):
                wv = v(w)
                ok = ok and GA.dot(wv, p, S) == 0 and GA.mul(wv, wv, S)[()] < 0
                R = GA.add(GA.sc(1), GA.scal(F(1, 2), GA.mul(p, wv, S)))
                Rt = GA.reverse(R)
                ok = ok and GA.eq(GA.mul(R, Rt, S), GA.sc(1))
                ok = ok and GA.eq(GA.mul(GA.mul(R, p, S), Rt, S), p)
                ok = ok and not GA.eq(R, GA.sc(1))
                Rs.append((R, Rt))
            ok = ok and len(Rs) == 2
            base, full, _ = lin_system(S, n, p, Rs)
            ok = ok and solvable(*base) and not solvable(*full)
    _tp_rv = (ok); assert _tp_rv is not False, "check_no_equivariant_pseudo_inverse_in_any_extension"; return _tp_rv


S24 = (1, -1, -1, -1, 1, -1)
EP, EM = GA.gen(4), GA.gen(5)
N0 = GA.scal(F(1, 2), GA.sub(EM, EP))
NINF = GA.add(EM, EP)
# Non-null sample points for iota(X(x)) = Q(x) X(x/Q(x)).
NON_NULL_POINTS = [(2, 1, 0, 0), (1, 2, F(1, 3), 0), (F(1, 2), 0, 0, 3)]


def lift(c):
    x = v(c)
    Q = GA.mul(x, x, S13).get((), F(0))
    return GA.add(N0, x, GA.scal(Q / 2, NINF))


def iota(X):
    # X = a n0 + x + b ninf with n0 = (e- - e+)/2, ninf = e- + e+: e+ coeff = -a/2 + b, e- coeff = a/2 + b
    cp, cm = X.get((4,), F(0)), X.get((5,), F(0))
    a = cm - cp
    b = (cp + cm) / 2
    x = {k: c for k, c in X.items() if k not in ((4,), (5,))}
    return GA.add(GA.scal(2 * b, N0), x, GA.scal(a / 2, NINF))


def check_one_rung_for_all_momenta():
    premise("rungs.imported-totality-minimality-completion")
    ok = GA.congruence_signature([[S24[4], 0], [0, S24[5]]]) == (1, 1, 0)
    ok = ok and GA.is_zero(GA.mul(N0, N0, S24)) and GA.is_zero(GA.mul(NINF, NINF, S24))
    ok = ok and GA.dot(N0, NINF, S24) == -1
    blades = [(i,) for i in range(6)]
    lifts = [lift((0, 0, 0, 0))]
    for k, c in enumerate(MOMENTA):
        X = lift(c)
        ok = ok and GA.is_zero(GA.mul(X, X, S24))
        lifts.append(X)
        rk = GA.rank_of_vectors([[L.get(b, F(0)) for b in blades] for L in lifts])
        ok = ok and rk == min(k + 2, 5)
    lifts.append(lift((0, 1, 0, 0)))                       # one non-null point uses the ninf direction
    ok = ok and GA.rank_of_vectors([[L.get(b, F(0)) for b in blades] for L in lifts]) == 6
    _tp_rv = (ok); assert _tp_rv is not False, "check_one_rung_for_all_momenta"; return _tp_rv


def check_reciprocal_total_on_quadric():
    premise("rungs.imported-totality-minimality-completion")
    ok = True
    for c in MOMENTA:
        X = lift(c)
        Y = iota(X)
        ok = ok and GA.eq(Y, GA.add(v(c), GA.scal(F(1, 2), NINF)))
        ok = ok and GA.is_zero(GA.mul(Y, Y, S24)) and GA.eq(iota(Y), X)
        # ideal point: n0-coefficient 0, read as Y . ninf = 0 (n0 . ninf = -1, x . ninf = ninf . ninf = 0)
        ok = ok and GA.mul(Y, NINF, S24).get((), F(0)) == 0
    qs = []
    for c in NON_NULL_POINTS:
        x = v(c)
        Q = GA.mul(x, x, S13)[()]
        qs.append(Q)
        Y = iota(lift(c))
        ok = ok and GA.eq(Y, GA.scal(Q, lift(tuple(F(t) / Q for t in c))))
        ok = ok and GA.is_zero(GA.mul(Y, Y, S24)) and GA.eq(iota(Y), lift(c))
    # by hand: Q = 4 - 1 = 3, 1 - 4 - 1/9 = -28/9, 1/4 - 9 = -35/4 (the points are non-null)
    ok = ok and qs == [3, F(-28, 9), F(-35, 4)]
    _tp_rv = (ok); assert _tp_rv is not False, "check_reciprocal_total_on_quadric"; return _tp_rv
