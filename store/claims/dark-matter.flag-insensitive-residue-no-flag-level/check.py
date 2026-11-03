"""dark-matter.flag-insensitive-residue-no-flag-level: exact checks.

(a) Witt transitivity, constructively over Q, in every nondefinite P3 representative ((1,3), (3,1),
(2,2), (2,1), (1,2), (4,1), (1,4)): target hyperbolic pairs (u, u'), Q(u) = Q(u') = 0, <u,u'> = 1, are
built independently of any isometry (u by stereographic projection of the null cone from the standard
null vector u0 along a direction d; u' from u and an auxiliary w). Products of at most four reflections
r_a(x) = x - 2<x,a>/Q(a) a are then found that carry the standard pair (u0, u0') to (u, u'); the
composite is checked to preserve the Gram matrix on the basis and to hit both vectors. The reflection in
u - u' exchanges the two null lines of the plane. Hence transitivity on hyperbolic planes and on the
null lines within them, in every nondefinite residue alike.
(b) The paper's witnesses: in (1,3) the rotation e1 -> e2, e2 -> -e1 is an isometry fixing e0 and
carrying span(e0, e1) to span(e0, e2) and R(e0 + e1) to R(e0 + e2); in (2,2) two totally isotropic
planes are exchanged by e3 <-> e4, the three isotropy equations have Jacobian rank 3 in four chart
unknowns (exact central differences of quadratics), and a hyperbolic plane stays hyperbolic under
chart steps of 1/5.
(c) Definite r = 4 ((4,0), (0,4)): the Gram matrix is definite (signature (4,0) or (0,4)), so no null
vector and no hyperbolic plane; but the complexified conformal ambient (5,1) has a three-dimensional
totally isotropic subspace (Gaussian rationals, rank 3 over Q(i)), the descent's flag.
The claim has no declared premises, so no premise() calls.
"""
from fractions import Fraction as F
import GA

REPS = [(1, 3), (3, 1), (2, 2), (2, 1), (1, 2), (4, 1), (1, 4)]
# generic sample directions (the claim holds for all of them)
DIRS = [[2, -1, 3, 1, 5], [1, 4, -2, 3, -1], [-3, 2, 1, -1, 2]]
AUX = [[1, 2, 0, -1, 3], [3, -1, 2, 2, -2], [0, 1, 1, 5, 1]]


def ip(sq, a, b):
    return sum(F(sq[k]) * a[k] * b[k] for k in range(len(sq)))


def refl(sq, a):
    Qa = ip(sq, a, a)
    return lambda x: [x[k] - 2 * ip(sq, x, a) / Qa * a[k] for k in range(len(sq))]


def standard_pair(sq):
    i = sq.index(1)
    j = sq.index(-1)
    n = len(sq)
    u0 = [F(1) if k in (i, j) else F(0) for k in range(n)]
    u0p = [F(1, 2) if k == i else (F(-1, 2) if k == j else F(0)) for k in range(n)]
    return u0, u0p


def null_from(sq, u0, d):
    t = -2 * ip(sq, u0, d) / ip(sq, d, d)
    return [u0[k] + t * d[k] for k in range(len(sq))]


def partner(sq, u, w):
    c = ip(sq, u, w)
    x = [w[k] - ip(sq, w, w) / (2 * c) * u[k] for k in range(len(sq))]
    return [xk / c for xk in x]


def compose(fs):
    def g(x):
        for f in fs:
            x = f(x)
        return x
    return g


def move_null(sq, x, y, helpers):
    """Reflections (list) carrying the null vector x to the null vector y."""
    if ip(sq, x, y) != 0:
        return [refl(sq, [x[k] - y[k] for k in range(len(sq))])]
    for z in helpers:
        if ip(sq, x, z) != 0 and ip(sq, z, y) != 0:
            return [refl(sq, [x[k] - z[k] for k in range(len(sq))]), refl(sq, [z[k] - y[k] for k in range(len(sq))])]
    return None


def check_witt_transitivity_on_hyperbolic_pairs():
    ok = True
    count = 0
    for p, q in REPS:
        sq = GA.sig(p, q)
        n = p + q
        u0, u0p = standard_pair(sq)
        ok = ok and ip(sq, u0, u0) == 0 and ip(sq, u0p, u0p) == 0 and ip(sq, u0, u0p) == 1
        for d, w in zip(DIRS, AUX):
            d, w = [F(x) for x in d[:n]], [F(x) for x in w[:n]]
            if ip(sq, d, d) == 0 or ip(sq, u0, d) == 0:
                continue
            u = null_from(sq, u0, d)
            if ip(sq, u, w) == 0:
                continue
            up = partner(sq, u, w)
            ok = ok and ip(sq, u, u) == 0 and ip(sq, up, up) == 0 and ip(sq, u, up) == 1
            helpers = [null_from(sq, u0, [F(x) for x in h[:n]]) for h in DIRS + AUX
                       if ip(sq, [F(x) for x in h[:n]], [F(x) for x in h[:n]]) != 0]
            step1 = move_null(sq, u0, u, helpers)
            ok = ok and step1 is not None
            g1 = compose(step1)
            v = g1(u0p)
            ok = ok and g1(u0) == u and ip(sq, u, v) == 1
            if ip(sq, v, up) != 0:
                step2 = [refl(sq, [v[k] - up[k] for k in range(n)])]
            else:
                zs = [partner(sq, u, [F(x) for x in h[:n]]) for h in AUX + DIRS
                      if ip(sq, u, [F(x) for x in h[:n]]) != 0]
                z = next(z for z in zs if ip(sq, v, z) != 0 and ip(sq, z, up) != 0)
                step2 = [refl(sq, [v[k] - z[k] for k in range(n)]), refl(sq, [z[k] - up[k] for k in range(n)])]
            g = compose(step1 + step2)
            E = [[F(int(i == j)) for j in range(n)] for i in range(n)]
            ok = ok and g(u0) == u and g(u0p) == up
            ok = ok and all(ip(sq, g(a), g(b)) == ip(sq, a, b) for a in E for b in E)
            swap = refl(sq, [u[k] - up[k] for k in range(n)])
            ok = ok and swap(u) == up and swap(up) == u
            count += 1
    ok = ok and count == 21
    GA.check("prop:flaggable: in all 7 nondefinite P3 representatives, 3 independent hyperbolic pairs each are "
             "reached from the standard pair by reflections (21 cases), and their null lines exchanged", ok)
    return ok


def check_paper_witnesses_13_and_22():
    G13 = (1, -1, -1, -1)
    E = [[F(int(i == j)) for j in range(4)] for i in range(4)]

    def rot(v):
        return [v[0], -v[2], v[1], v[3]]
    ok = all(ip(G13, rot(a), rot(b)) == ip(G13, a, b) for a in E for b in E)
    ok = ok and rot(E[0]) == E[0] and rot(E[1]) == E[2]
    n1 = [F(1), F(1), F(0), F(0)]
    ok = ok and ip(G13, n1, n1) == 0 and rot(n1) == [F(1), F(0), F(1), F(0)]
    G22 = (1, 1, -1, -1)
    P1 = ([F(1), 0, F(1), 0], [0, F(1), 0, F(1)])
    P2 = ([F(1), 0, 0, F(1)], [0, F(1), F(1), 0])

    def iso(pl):
        a, b = pl
        return ip(G22, a, a) == 0 and ip(G22, b, b) == 0 and ip(G22, a, b) == 0
    sw = lambda v: [v[0], v[1], v[3], v[2]]
    ok = ok and iso(P1) and iso(P2)
    ok = ok and GA.rank_of_vectors([sw(P1[0]), sw(P1[1]), list(P2[0]), list(P2[1])]) == 2

    def chart(m):
        return ([F(1), F(0), 1 + m[0], m[1]], [F(0), F(1), m[2], 1 + m[3]])

    def eqs(m):
        a, b = chart(m)
        return [ip(G22, a, a), ip(G22, b, b), ip(G22, a, b)]
    h = F(1, 3)
    cols = []
    for j in range(4):
        mp = [F(0)] * 4
        mm = [F(0)] * 4
        mp[j] += h
        mm[j] -= h
        cols.append([(x - y) / (2 * h) for x, y in zip(eqs(mp), eqs(mm))])
    J = [[cols[j][i] for j in range(4)] for i in range(3)]
    ok = ok and eqs([F(0)] * 4) == [0, 0, 0] and GA.rank_of_vectors(J) == 3 and 4 - GA.rank_of_vectors(J) == 1

    def gdet(pl):
        a, b = pl
        return ip(G22, a, a) * ip(G22, b, b) - ip(G22, a, b) ** 2
    H = [F(1), F(0), F(0), F(-1)]
    ok = ok and gdet(chart(H)) < 0
    ok = ok and all(gdet(chart([H[k] + F(1, 5) * s * F(int(k == j)) for k in range(4)])) < 0
                    for j in range(4) for s in (1, -1))
    GA.check("prop:flaggable: the (1,3) rotation witness; in (2,2) exchanged isotropic planes, Jacobian rank 3 "
             "(one-parameter family), hyperbolic planes open", ok)
    return ok


def check_definite_residue_has_flag_but_no_plane():
    ok = True
    for p, q in ((4, 0), (0, 4)):
        sq = GA.sig(p, q)
        G = [[F(sq[i]) if i == j else F(0) for j in range(4)] for i in range(4)]
        ok = ok and tuple(GA.congruence_signature(G)) == (p, q, 0)
    # complexified conformal ambient of (4,0): (5,1); a 3-dim totally isotropic subspace over Q(i)
    sq = (1, 1, 1, 1, 1, -1)
    i_ = GA.QI_I
    one, zero = GA.qi(1), GA.qi(0)
    W = [[one, i_, zero, zero, zero, zero], [zero, zero, one, i_, zero, zero], [zero, zero, zero, zero, one, one]]
    bil = lambda a, b: sum((a[k] * b[k] * sq[k] for k in range(6)), GA.qi(0))
    ok = ok and all(bil(a, b) == 0 for a in W for b in W) and GA.field_rank(W) == 3
    # and no larger one: a 4th vector orthogonal to W lies in W + (its own) ... dim W^perp = 6 - 3
    rows = [[a[k] * sq[k] for k in range(6)] for a in W]
    ok = ok and 6 - GA.field_rank(rows) == 3
    GA.check("r = 4: (4,0), (0,4) definite (no null vector, no hyperbolic plane); complexified (5,1) carries a "
             "3-dimensional totally isotropic subspace, W^perp of dimension 3", ok)
    return ok
