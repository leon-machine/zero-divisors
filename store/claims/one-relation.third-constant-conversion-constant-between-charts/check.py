"""one-relation.third-constant-conversion-constant-between-charts: exact checks (ported and widened
from the T16 c-placement block; GA.py and Fractions only).

(i)   Finiteness is nondegeneracy and mixing: Q_c/c^2 = diag(1, -1/c^2, -1/c^2, -1/c^2) has signature
      (1,3) for every finite sample c; at c = infinity it is diag(1,0,0,0), rank one with radical the
      simultaneity hyperplane (dimension 3). A diagonal nondegenerate form has a nonzero null vector
      iff pq != 0: e_i + e_j for mixed forms, and for definite forms Q(x) != 0 on every nonzero grid
      point (all signatures with n <= 4).
(ii)  One number (Fact one-relation.imported-witts-extension-theorem): three distinct hyperbolic planes
      of (1,3) spanned by rational null pairs with n.m = -1 all have orthogonal complements of
      signature (0,2), so Witt's theorem makes them conjugate.
(iii) Witt chart against metric chart in Cl(1,1): f_+- = (e0 +- e1)/2 are null with f+.f- = 1/2; at
      lam = e^eta = mu^2 (mu = 2, 3, 1/2) the rotor R = cosh(eta/2) - sinh(eta/2) e0e1 has R R~ = 1,
      R f+ R~ = lam f+, R f- R~ = f-/lam, R e0 R~ = cosh(eta) e0 + sinh(eta) e1, and the coordinate
      velocity tanh(eta) = (lam^2 - 1)/(lam^2 + 1).
(iv)  The arrow: the number of components of {Q > 0} is computed by a union-find over rational grid
      points of {Q > 0} joined by exactly certified Q-positive segments: 2 when p = 1 (separated by the
      sign of x_0), 1 when p >= 2, 0 when p = 0; some sign-definite cone splits iff min(p, q) = 1.
(Cone) With Fact one-relation.imported-null-cone-determines-form-zeemans: for 1 <= p, q <= 3 the
      symmetric forms vanishing on a spanning family of rational null vectors form a space of
      dimension one, so the cone fixes Q up to scale.
(Units) The exponent matrix of (c, hbar, G) over (L, T, M) has determinant -2; no monomial in hbar and
      G alone has the dimension of L, T or M; the Planck exponents solve exactly.
"""
from fractions import Fraction as F
from itertools import permutations, product

import GA
from pyutil import get_or_set
from tp_premise import premise

GRID = [F(-2), F(-1), F(0), F(1), F(2)]
C_VALUES = [1, 10, 1000]
MU = [F(2), F(3), F(1, 2)]
NULL_PAIRS = [
    ([F(1), F(1), F(0), F(0)], [F(-1, 2), F(1, 2), F(0), F(0)]),
    ([F(5), F(3), F(4), F(0)], [F(-1, 10), F(3, 50), F(4, 50), F(0)]),
    ([F(13), F(3), F(4), F(12)], [F(-1, 26), F(3, 338), F(4, 338), F(12, 338)]),
]
UNIT_ROWS = [[1, -1, 0], [2, -1, 1], [3, -2, -1]]      # c, hbar, G over (L, T, M)


def Bform(p, q):
    sq = GA.sig(p, q)
    return lambda x, y: sum(F(s) * F(a) * F(b) for s, a, b in zip(sq, x, y))


def segment_positive(u, v, B):
    d = [F(b) - F(a) for a, b in zip(u, v)]
    a2, b1, c0 = B(d, d), 2 * B(u, d), B(u, u)
    vals = [c0, a2 + b1 + c0]
    if a2 > 0:
        t = -b1 / (2 * a2)
        if 0 < t < 1:
            vals.append(a2 * t * t + b1 * t + c0)
    return min(vals) > 0


def components(p, q, limit=40):
    n = p + q
    B = Bform(p, q)
    nodes = []
    for x in product(GRID, repeat=n):
        if B(x, x) > 0:
            nodes.append(tuple(x))
            if len(nodes) >= limit:
                break
    extra = [tuple(list(x[:p]) + [F(0)] * q) for x in nodes]
    for k in range(min(n, 2)):
        for s in (1, -1):
            e = [F(0)] * n
            e[k] = F(s)
            extra.append(tuple(e))
    for x in extra:
        if B(x, x) > 0 and x not in nodes:
            nodes.append(x)
    parent = list(range(len(nodes)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if find(i) != find(j) and segment_positive(nodes[i], nodes[j], B):
                parent[find(i)] = find(j)
    classes = {}
    for i, x in enumerate(nodes):
        get_or_set(classes, find(i), set()).add((x[0] > 0) - (x[0] < 0))
    return len(classes), list(classes.values())


def det3(M):
    (a, b, c), (d, e, f), (g, h, i) = [[F(x) for x in r] for r in M]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def diag(vals):
    n = len(vals)
    return [[F(vals[i]) if i == j else F(0) for j in range(n)] for i in range(n)]


def check_finite_ratio_iff_nondegenerate_and_mixed():
    ok = True
    for c in C_VALUES:
        k = F(1, c * c)
        ok = ok and GA.congruence_signature(diag([1, -k, -k, -k])) == (1, 3, 0)
    ok = ok and GA.congruence_signature(diag([1, 0, 0, 0])) == (1, 0, 3)
    for n in range(2, 5):
        for p in range(n + 1):
            q = n - p
            B = Bform(p, q)
            has_null = any(B(x, x) == 0 for x in product(GRID, repeat=n) if any(x))
            ok = ok and has_null == (p * q != 0)
            if p * q:
                e = [F(0)] * n
                e[0], e[p] = F(1), F(1)
                ok = ok and B(e, e) == 0
    GA.check("Q_c/c^2 -> t^2 (rank 1) as c -> infinity; a nonzero null vector exists iff pq != 0 (n <= 4)", ok)
    return ok


def check_one_number_by_witt():
    premise("one-relation.imported-witts-extension-theorem")
    ok = True
    B = Bform(1, 3)
    sq = GA.sig(1, 3)
    sigs = []
    for nv, mv in NULL_PAIRS:
        ok = ok and B(nv, nv) == 0 and B(mv, mv) == 0 and B(nv, mv) == -1
        rows = [[F(s) * x for s, x in zip(sq, v)] for v in (nv, mv)]
        kern = GA.field_kernel(rows)
        ok = ok and len(kern) == 2
        sigs.append(GA.congruence_signature([[B(u, v) for v in kern] for u in kern]))
    ok = ok and sigs == [(0, 2, 0)] * 3
    spans = [GA.mat_rank([a[0], a[1], b[0], b[1]]) for i, a in enumerate(NULL_PAIRS) for b in NULL_PAIRS[i + 1:]]
    ok = ok and all(r >= 3 for r in spans) and len(spans) == 3
    GA.check("three distinct hyperbolic planes of (1,3) have complements of one signature (0,2): conjugate by Witt", ok)
    return ok


def check_witt_rescaling_is_the_boost():
    ok = True
    sq = GA.sig(1, 1)
    e0, e1 = GA.gen(0), GA.gen(1)
    one = GA.sc(1)

    def mm(*xs):
        out = xs[0]
        for x in xs[1:]:
            out = GA.mul(out, x, sq)
        return out

    fp = GA.scal(F(1, 2), GA.add(e0, e1))
    fm = GA.scal(F(1, 2), GA.sub(e0, e1))
    ok = ok and GA.is_zero(mm(fp, fp)) and GA.is_zero(mm(fm, fm)) and GA.dot(fp, fm, sq) == F(1, 2)
    Bv = mm(e0, e1)
    ok = ok and GA.eq(mm(Bv, Bv), one)
    for mu in MU:
        lam = mu * mu
        chh, shh = (mu + 1 / mu) / 2, (mu - 1 / mu) / 2
        ch, sh = (lam + 1 / lam) / 2, (lam - 1 / lam) / 2
        R = GA.sub(GA.scal(chh, one), GA.scal(shh, Bv))
        Rt = GA.reverse(R)
        ok = ok and GA.eq(mm(R, Rt), one)
        ok = ok and GA.eq(mm(R, fp, Rt), GA.scal(lam, fp)) and GA.eq(mm(R, fm, Rt), GA.scal(1 / lam, fm))
        ok = ok and GA.eq(mm(R, e0, Rt), GA.add(GA.scal(ch, e0), GA.scal(sh, e1)))
        ok = ok and sh / ch == (lam * lam - 1) / (lam * lam + 1)
    ok = ok and (lambda lam: ((lam - 1 / lam) / (lam + 1 / lam)))(F(4)) == F(15, 17)
    GA.check("the Witt rescaling f+ -> lam f+, f- -> f-/lam is the boost rotor of rapidity log lam", ok)
    return ok


# Sample signatures (p, q) for the component count, and for the arrow iff min(p, q) = 1 criterion.
COUNT_SIGNATURES = [(1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (3, 1), (0, 3), (0, 2)]
IFF_SIGNATURES = ((1, 3), (3, 1), (2, 2), (1, 1), (2, 1))


def check_time_orientation_iff_min_p_q_is_one():
    ok = True
    for (p, q) in COUNT_SIGNATURES:
        # {Q > 0} has the components of S^(p-1): none for p = 0, two for p = 1, one for p >= 2
        want = 0 if p == 0 else (2 if p == 1 else 1)
        c, signs = components(p, q)
        ok = ok and c == want
        if signs:
            # both time signs occur; the classes are sign-pure exactly when there are two of them
            ok = ok and {1, -1} <= set.union(*signs)
            ok = ok and all(len(s) == 1 for s in signs) == (want == 2)
    for p, q in IFF_SIGNATURES:
        cp, cm = components(p, q)[0], components(q, p)[0]
        ok = ok and ((cp == 2 or cm == 2) == (min(p, q) == 1))
    GA.check("{Q > 0} has 2 components for p = 1, 1 for p >= 2, 0 for p = 0; an arrow iff min(p,q) = 1", ok)
    return ok


def check_cone_determines_the_form():
    premise("one-relation.imported-null-cone-determines-form-zeemans")
    ok = True
    for p in range(1, 4):
        for q in range(1, 4):
            n = p + q
            pos, neg = range(p), range(p, n)
            out = []

            def vec(d):
                v = [F(0)] * n
                for i, c in d.items():
                    v[i] += F(c)
                return v

            for i in pos:
                for j in neg:
                    out += [vec({i: 1, j: 1}), vec({i: 1, j: -1})]
            for i, k in permutations(pos, 2):
                for j in neg:
                    out += [vec({i: 3, k: 4, j: 5}), vec({i: 3, k: 4, j: -5})]
            for j, l in permutations(neg, 2):
                for i in pos:
                    out += [vec({i: 5, j: 3, l: 4}), vec({i: 5, j: 3, l: -4})]
            B = Bform(p, q)
            ok = ok and all(B(v, v) == 0 for v in out)
            idx = [(i, j) for i in range(n) for j in range(i, n)]
            rows = [[v[i] * v[j] * (1 if i == j else 2) for (i, j) in idx] for v in out]
            ok = ok and len(idx) - GA.mat_rank(rows) == 1
    GA.check("for 1 <= p, q <= 3 the forms vanishing on the null cone are the multiples of Q", ok)
    return ok


def check_three_constants_fix_three_units():
    ok = det3(UNIT_ROWS) == -2
    hg = UNIT_ROWS[1:]
    ok = ok and all(GA.mat_rank(GA.frac_matrix(hg + [row])) == 3 for row in ([1, 0, 0], [0, 1, 0], [0, 0, 1]))

    def solve(rhs):
        MT = [[F(UNIT_ROWS[j][i]) for j in range(3)] for i in range(3)]
        D = det3(MT)
        sol = []
        for k in range(3):
            Mk = [row[:] for row in MT]
            for r in range(3):
                Mk[r][k] = F(rhs[r])
            sol.append(det3(Mk) / D)
        return sol

    ok = ok and solve([1, 0, 0]) == [F(-3, 2), F(1, 2), F(1, 2)]
    ok = ok and solve([0, 1, 0]) == [F(-5, 2), F(1, 2), F(1, 2)]
    ok = ok and solve([0, 0, 1]) == [F(1, 2), F(1, 2), F(-1, 2)]
    GA.check("det of the (c, hbar, G) exponent matrix is -2; hbar and G alone fix no base unit; Planck units", ok)
    return ok
