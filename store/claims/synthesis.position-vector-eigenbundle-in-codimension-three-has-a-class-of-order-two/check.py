"""The position vector on the least module of Cl(3,0): clutching function and rotor lift, exact.

The least module is the left ideal S = Cl(3,0) p, p = (1 + e3)/2, of dimension four, with the product
<psi~ phi>_0 (scalar part); multiplication by a vector x on the left is symmetric for it and squares to Q(x).
Over the unit sphere the positive eigenbundle is G_+ = { (x, psi) : x psi = psi } = pi(x) S, pi(x) = (1 + x)/2.

(1) Generators: e1, e2, e3 act on S by symmetric anticommuting maps of square one; g(x)^2 = Q(x).
(2) Frames: pi(x) p, pi(x) e1e2 p are orthogonal of square (1 + x3)/4 each (a frame where x3 > -1);
    pi(x) e1 p, pi(x) e2 p are orthogonal of square (1 - x3)/4 each (a frame where x3 < 1).
(3) Clutching: at x = (c, s, 0) the second frame is the first turned by the angle of x:
    pi e1 p = c pi p - s pi e1e2 p,  pi e2 p = s pi p + c pi e1e2 p.  One full turn round the equator.
(4) Rotor lift: in Cl(2 + N, 0) the rotor R = cos(a/2) + sin(a/2) f1f2 turns the frame (f1, f2) as in (3),
    R f1 R~ = c f1 - s f2, R f2 R~ = s f1 + c f2, and fixes the other directions; along the turn it runs from 1
    to -1. For k planes turned together it ends at (-1)^k.
(5) Two copies: the least module of Cl(4,0), the ideal T = Cl(4,0) p4, p4 = (1 + e1e2e3e4)/2, of dimension eight,
    is S p4 + S e1 p4 under Cl(3,0), two orthogonal copies of S (the product halved), and e4 is a fourth symmetric
    anticommuting generator: (x + b e4)^2 = Q(x) + b^2.
(6) On S itself no fourth symmetric map anticommutes with e1, e2, e3.
(7) For the lifting clause (L): in Cl(n,0), n = 1..6, the only even blade commuting with every basis vector is
    the scalar, and no odd blade anticommutes with every basis vector (conjugation by a basis vector is diagonal
    on blades, so this decides it for all elements); the plane rotor is a product of two unit vectors.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ3 = GA.sig(3, 0)
SQ4 = GA.sig(4, 0)
N_EXTRA = 3                      # trivial directions added in the rotor check
SQF = GA.sig(2 + N_EXTRA, 0)     # fibre algebra of the stabilised bundle
SQK = GA.sig(6, 0)               # three planes, for k = 1, 2, 3 copies

# rational points of the circle, (c, s) with c^2 + s^2 = 1, from (a, b): c = (a^2-b^2)/(a^2+b^2), s = 2ab/(a^2+b^2)
CIRCLE_SEEDS = [(1, 0), (2, 1), (1, 1), (1, 2), (0, 1), (-1, 2), (-1, 1), (-2, 1), (3, 2), (-3, 5), (5, -1), (1, -3)]
# rational points of the sphere from (u, v): x = (2u, 2v, u^2+v^2-1)/(u^2+v^2+1), and the two poles
SPHERE_SEEDS = [(0, 0), (1, 0), (0, 1), (1, 1), (2, -1), (F(1, 2), F(1, 3)), (-3, 2), (F(-2, 5), 4), (7, 7)]
# the turn in N_STEPS + 1 points: half-angle parameters (1 - j/N_STEPS, j/N_STEPS)
N_STEPS = 12
SAMPLE_VECTORS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (2, -1, 3), (F(1, 2), F(2, 3), -5), (0, 0, 0), (-4, 4, 1)]
SAMPLE_COUPLINGS = [F(0), F(1), F(-2, 3), F(5, 7)]
CENTRE_DIMENSIONS = [1, 2, 3, 4, 5, 6]


def circle_point(a, b):
    a, b = F(a), F(b)
    d = a * a + b * b
    return (a * a - b * b) / d, 2 * a * b / d


def sphere_point(u, v):
    u, v = F(u), F(v)
    d = u * u + v * v + 1
    return 2 * u / d, 2 * v / d, (u * u + v * v - 1) / d


def vec(x, n=3):
    out = {}
    for i in range(n):
        if i < len(x) and x[i] != 0:
            out[(i,)] = F(x[i])
    return out


def blade(*idx):
    return {tuple(idx): F(1)}


def pair(a, b, squares):
    """<a~ b>_0."""
    return GA.mul(GA.reverse(a), b, squares).get((), F(0))


P3 = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.gen(2)))                    # p = (1 + e3)/2
IDEAL3 = [P3, GA.mul(GA.gen(0), P3, SQ3), GA.mul(GA.gen(1), P3, SQ3), GA.mul(blade(0, 1), P3, SQ3)]
BLADES3 = GA.all_blades(3)
BLADES4 = GA.all_blades(4)


def coords(psi, basis, blades):
    """Coordinates of psi in a list of independent multivectors (exact solve), or None."""
    rows = [GA.basis_vector_of(b, blades) for b in basis]
    target = GA.basis_vector_of(psi, blades)
    n = len(basis)
    # solve sum_j c_j rows[j] = target by elimination on the transposed system
    m = [[rows[j][i] for j in range(n)] + [target[i]] for i in range(len(blades))]
    piv_cols, r = [], 0
    for col in range(n):
        piv = next((i for i in range(r, len(m)) if m[i][col] != 0), None)
        if piv is None:
            return None
        m[r], m[piv] = m[piv], m[r]
        pv = m[r][col]
        m[r] = [a / pv for a in m[r]]
        for i in range(len(m)):
            if i != r and m[i][col] != 0:
                f = m[i][col]
                m[i] = [a - f * b for a, b in zip(m[i], m[r])]
        piv_cols.append(col)
        r += 1
    if any(row[n] != 0 for row in m[r:]):
        return None
    return [m[i][n] for i in range(n)]


def left_matrix(a, basis, blades, squares):
    """Matrix of psi -> a psi on the span of basis (columns are images)."""
    cols = [coords(GA.mul(a, b, squares), basis, blades) for b in basis]
    if any(c is None for c in cols):
        return None
    n = len(basis)
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def gram(basis, squares):
    return [[pair(a, b, squares) for b in basis] for a in basis]


def is_symmetric_for(m, g):
    """m^T g = g m."""
    n = len(m)
    mt = [[m[j][i] for j in range(n)] for i in range(n)]
    return GA.mat_eq(GA.mat_mul(mt, g), GA.mat_mul(g, m))


def check_least_module_and_symmetric_generators():
    premise("std-algebra.periodicity")
    ok = True
    # p is an idempotent and the ideal has dimension four, half of Cl(3,0)
    ok = ok and GA.eq(GA.mul(P3, P3, SQ3), P3)
    ok = ok and GA.rank_of_vectors([GA.basis_vector_of(b, BLADES3) for b in IDEAL3]) == 4
    ok = ok and len(BLADES3) == 8
    g = gram(IDEAL3, SQ3)
    ok = ok and GA.congruence_signature(g) == (4, 0, 0)
    mats = [left_matrix(GA.gen(i), IDEAL3, BLADES3, SQ3) for i in range(3)]
    ok = ok and all(m is not None for m in mats)
    ident = [[F(1) if i == j else F(0) for j in range(4)] for i in range(4)]
    zero = [[F(0)] * 4 for _ in range(4)]
    for i in range(3):
        ok = ok and is_symmetric_for(mats[i], g)
        ok = ok and GA.mat_eq(GA.mat_mul(mats[i], mats[i]), ident)
        for j in range(i + 1, 3):
            ac = [[a + b for a, b in zip(r1, r2)] for r1, r2 in
                  zip(GA.mat_mul(mats[i], mats[j]), GA.mat_mul(mats[j], mats[i]))]
            ok = ok and GA.mat_eq(ac, zero)
    # g(x)^2 = Q(x) on the module, for sample vectors: degenerate exactly at x = 0
    for x in SAMPLE_VECTORS:
        xv = vec(x)
        q = sum(F(c) * F(c) for c in x)
        for b in IDEAL3:
            ok = ok and GA.eq(GA.mul(xv, GA.mul(xv, b, SQ3), SQ3), GA.scal(q, b))
        m = left_matrix(xv, IDEAL3, BLADES3, SQ3) if xv else zero
        gm = GA.mat_mul(g, m)
        sig = GA.congruence_signature(gm)
        ok = ok and (sig == (2, 2, 0) if q != 0 else sig == (0, 0, 4))
    GA.check("the ideal Cl(3,0)(1+e3)/2 has dimension four; e1, e2, e3 act on it by symmetric anticommuting maps of "
             "square one; g(x)^2 = Q(x), the form of g(x) has signature (2,2) for x != 0 and vanishes at x = 0", ok)
    return ok


def frames(x):
    """North and south frames of the positive eigenbundle at the unit vector x."""
    pi = GA.scal(F(1, 2), GA.add(GA.sc(1), vec(x)))
    north = [GA.mul(pi, IDEAL3[0], SQ3), GA.mul(pi, IDEAL3[3], SQ3)]
    south = [GA.mul(pi, IDEAL3[1], SQ3), GA.mul(pi, IDEAL3[2], SQ3)]
    return pi, north, south


def check_hemisphere_frames_of_the_positive_eigenbundle():
    ok = True
    pts = [sphere_point(u, v) for (u, v) in SPHERE_SEEDS] + [(F(0), F(0), F(1))]
    for x in pts:
        ok = ok and sum(c * c for c in x) == 1
        pi, north, south = frames(x)
        xv = vec(x)
        for f in north + south:
            ok = ok and GA.eq(GA.mul(xv, f, SQ3), f)              # in the +1 eigenspace
        gn, gs = gram(north, SQ3), gram(south, SQ3)
        ok = ok and gn == [[(1 + x[2]) / 4, F(0)], [F(0), (1 + x[2]) / 4]]
        ok = ok and gs == [[(1 - x[2]) / 4, F(0)], [F(0), (1 - x[2]) / 4]]
        # the eigenspace has dimension two
        allf = [GA.mul(pi, b, SQ3) for b in IDEAL3]
        ok = ok and GA.rank_of_vectors([GA.basis_vector_of(f, BLADES3) for f in allf]) == 2
    # the poles: the north frame vanishes at the south pole only, the south frame at the north pole only
    south_pole, north_pole = (F(0), F(0), F(-1)), (F(0), F(0), F(1))
    ok = ok and all(GA.is_zero(f) for f in frames(south_pole)[1])
    ok = ok and all(GA.is_zero(f) for f in frames(north_pole)[2])
    ok = ok and not any(GA.is_zero(f) for f in frames(north_pole)[1])
    GA.check("pi(x) p, pi(x) e1e2 p are orthogonal of square (1+x3)/4 and pi(x) e1 p, pi(x) e2 p orthogonal of "
             "square (1-x3)/4 at ten rational points of the sphere; the eigenspace has dimension two", ok)
    return ok


def check_clutching_function_is_one_full_turn():
    ok = True
    turned = []
    for (a, b) in CIRCLE_SEEDS:
        c, s = circle_point(a, b)
        ok = ok and c * c + s * s == 1
        pi, north, south = frames((c, s, F(0)))
        # south_j = sum_i north_i gamma_ij with gamma = [[c, s], [-s, c]]
        ok = ok and GA.eq(south[0], GA.add(GA.scal(c, north[0]), GA.scal(-s, north[1])))
        ok = ok and GA.eq(south[1], GA.add(GA.scal(s, north[0]), GA.scal(c, north[1])))
        turned.append((c, s))
    # the angle of gamma is the angle of x: the points visit all four open quadrants and the axes
    quad = {(c > 0, s > 0) for (c, s) in turned if c != 0 and s != 0}
    ok = ok and len(quad) == 4 and (F(1), F(0)) in turned and (F(-1), F(0)) in turned
    # the turn is not a turn of the frame through twice the angle: at x = (0, 1, 0) gamma = [[0, 1], [-1, 0]]
    c, s = circle_point(1, 1)
    pi, north, south = frames((c, s, F(0)))
    ok = ok and (c, s) == (0, 1) and GA.eq(south[0], GA.neg(north[1])) and GA.eq(south[1], north[0])
    GA.check("on the equator x = (c, s, 0) the south frame is the north frame turned by the angle of x, "
             "gamma = [[c, s], [-s, c]], at twelve rational points in all four quadrants: one full turn", ok)
    return ok


def plane_rotor(ch, sh, i, j):
    """cos(a/2) + sin(a/2) f_i f_j."""
    return GA.add(GA.sc(ch), GA.scal(sh, blade(i, j)))


def check_rotor_lift_of_the_full_turn_ends_at_minus_one():
    premise("std-algebra.spin-double-cover")
    ok = True
    path = []
    for j in range(N_STEPS + 1):
        a, b = F(N_STEPS - j, N_STEPS), F(j, N_STEPS)
        ch, sh = circle_point(a, b)                    # half angle t/2 from 0 to pi
        c, s = ch * ch - sh * sh, 2 * ch * sh           # the angle t from 0 to 2 pi
        r = plane_rotor(ch, sh, 0, 1)
        ok = ok and GA.eq(GA.mul(r, GA.reverse(r), SQF), GA.sc(1))
        # R f_j R~ = sum_i f_i gamma_ij with gamma = [[c, s], [-s, c]], the clutching function; the rest fixed
        img = [GA.mul(GA.mul(r, GA.gen(i), SQF), GA.reverse(r), SQF) for i in range(2 + N_EXTRA)]
        ok = ok and GA.eq(img[0], GA.add(GA.scal(c, GA.gen(0)), GA.scal(-s, GA.gen(1))))
        ok = ok and GA.eq(img[1], GA.add(GA.scal(s, GA.gen(0)), GA.scal(c, GA.gen(1))))
        ok = ok and all(GA.eq(img[i], GA.gen(i)) for i in range(2, 2 + N_EXTRA))
        path.append((c, s, r))
    # the loop of rotations is closed, its lift is not: it runs from 1 to -1
    ok = ok and path[0][:2] == (1, 0) and path[-1][:2] == (1, 0)
    ok = ok and GA.eq(path[0][2], GA.sc(1)) and GA.eq(path[-1][2], GA.sc(-1))
    # consecutive lifts are the nearer of the two preimages: <R_j~ R_{j+1}>_0 > 0
    ok = ok and all(pair(path[j][2], path[j + 1][2], SQF) > 0 for j in range(N_STEPS))
    # k planes turned together (k copies of the module): the lift ends at (-1)^k
    for k in (1, 2, 3):
        ends = []
        for (a, b) in [(1, 0), (0, 1)]:
            ch, sh = circle_point(a, b)
            r = GA.sc(1)
            for q in range(k):
                r = GA.mul(r, plane_rotor(ch, sh, 2 * q, 2 * q + 1), SQK)
            ends.append(r)
        ok = ok and GA.eq(ends[0], GA.sc(1)) and GA.eq(ends[1], GA.sc((-1) ** k))
    GA.check("the rotor cos(a/2) + sin(a/2) f1f2 turns the frame plane by the clutching angle and fixes three "
             "added directions; along the full turn it runs from 1 to -1 in thirteen steps, each the nearer "
             "preimage; for k planes turned together it ends at (-1)^k, k = 1, 2, 3", ok)
    return ok


def check_two_copies_carry_a_fourth_generator():
    premise("std-algebra.periodicity")
    premise("synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump")
    ok = True
    omega = blade(0, 1, 2, 3)
    ok = ok and GA.eq(GA.mul(omega, omega, SQ4), GA.sc(1))
    p4 = GA.scal(F(1, 2), GA.add(GA.sc(1), omega))
    ok = ok and GA.eq(GA.mul(p4, p4, SQ4), p4)
    cand = [GA.mul({b: F(1)}, p4, SQ4) for b in BLADES4]
    vecs = [GA.basis_vector_of(c, BLADES4) for c in cand]
    ok = ok and GA.rank_of_vectors(vecs) == 8
    basis, rows = [], []
    for c, v in zip(cand, vecs):
        if GA.rank_of_vectors(rows + [v]) == len(rows) + 1:
            basis.append(c)
            rows.append(v)
    ok = ok and len(basis) == 8
    g = gram(basis, SQ4)
    ok = ok and GA.congruence_signature(g) == (8, 0, 0)
    mats = [left_matrix(GA.gen(i), basis, BLADES4, SQ4) for i in range(4)]
    ident = [[F(1) if i == j else F(0) for j in range(8)] for i in range(8)]
    zero = [[F(0)] * 8 for _ in range(8)]
    for i in range(4):
        ok = ok and mats[i] is not None and is_symmetric_for(mats[i], g)
        ok = ok and GA.mat_eq(GA.mat_mul(mats[i], mats[i]), ident)
        for j in range(i + 1, 4):
            ac = [[a + b for a, b in zip(r1, r2)] for r1, r2 in
                  zip(GA.mat_mul(mats[i], mats[j]), GA.mat_mul(mats[j], mats[i]))]
            ok = ok and GA.mat_eq(ac, zero)
    # under Cl(3,0) it is two copies of S: s -> s p4 and s -> s e1 p4 are module maps (right multiplications),
    # each injective and a multiple of an isometry, with orthogonal images that span the ideal
    lift3 = [{k: v for k, v in b.items()} for b in IDEAL3]
    copy1 = [GA.mul(b, p4, SQ4) for b in lift3]
    copy2 = [GA.mul(GA.mul(b, GA.gen(0), SQ4), p4, SQ4) for b in lift3]
    g3 = gram(IDEAL3, SQ3)
    half = [[x / 2 for x in row] for row in g3]
    ok = ok and gram(copy1, SQ4) == half and gram(copy2, SQ4) == half
    ok = ok and all(pair(a, b, SQ4) == 0 for a in copy1 for b in copy2)
    ok = ok and GA.rank_of_vectors([GA.basis_vector_of(c, BLADES4) for c in copy1 + copy2]) == 8
    for i in range(3):
        for b3, c1, c2 in zip(IDEAL3, copy1, copy2):
            eb = GA.mul(GA.gen(i), b3, SQ3)
            ok = ok and GA.eq(GA.mul(GA.gen(i), c1, SQ4), GA.mul(eb, p4, SQ4))
            ok = ok and GA.eq(GA.mul(GA.gen(i), c2, SQ4), GA.mul(GA.mul(eb, GA.gen(0), SQ4), p4, SQ4))
    for x in SAMPLE_VECTORS:
        for bcoup in SAMPLE_COUPLINGS:
            y = GA.add(vec(x, 4), GA.scal(bcoup, GA.gen(3)))
            q = sum(F(c) * F(c) for c in x) + bcoup * bcoup
            for b in basis[:3]:
                ok = ok and GA.eq(GA.mul(y, GA.mul(y, b, SQ4), SQ4), GA.scal(q, b))
            if y:
                m = left_matrix(y, basis, BLADES4, SQ4)
                sig = GA.congruence_signature(GA.mat_mul(g, m))
                ok = ok and sig == (4, 4, 0)
    GA.check("the ideal Cl(4,0)(1+e1e2e3e4)/2 has dimension eight and is two orthogonal copies of the least module "
             "of Cl(3,0); e1..e4 act by symmetric anticommuting maps of square one; (x + b e4)^2 = Q(x) + b^2 and "
             "the form has signature (4,4) unless x = 0 and b = 0", ok)
    return ok


def check_no_fourth_generator_on_the_least_module():
    premise("synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump")
    ok = True
    g = gram(IDEAL3, SQ3)
    mats = [left_matrix(GA.gen(i), IDEAL3, BLADES3, SQ3) for i in range(3)]
    n = 4
    # unknown X (16 entries); equations X E_i + E_i X = 0 (i = 1, 2, 3) and X^T g - g X = 0
    rows = []
    for m in mats:
        for i in range(n):
            for j in range(n):
                row = [F(0)] * (n * n)
                for k in range(n):
                    row[i * n + k] += m[k][j]          # (X m)_ij
                    row[k * n + j] += m[i][k]          # (m X)_ij
                rows.append(row)
    for i in range(n):
        for j in range(n):
            row = [F(0)] * (n * n)
            for k in range(n):
                row[k * n + i] += g[k][j]              # (X^T g)_ij
                row[k * n + j] -= g[i][k]              # (g X)_ij
            rows.append(row)
    ok = ok and GA.rank_of_vectors(rows) == n * n      # only X = 0
    # without the symmetry condition the anticommuting maps form a plane (the antisymmetric ones)
    ok = ok and GA.rank_of_vectors(rows[:3 * n * n]) == n * n - 2
    GA.check("on the least module of Cl(3,0) no nonzero symmetric map anticommutes with e1, e2, e3 "
             "(the anticommuting maps form a plane of antisymmetric ones)", ok)
    return ok


def check_elements_commuting_or_anticommuting_with_every_vector():
    premise("primer.centre")
    premise("std-algebra.spin-double-cover")
    ok = True
    for n in CENTRE_DIMENSIONS:
        squares = GA.sig(n, 0)
        even_central, odd_anti = [], []
        for b in GA.all_blades(n):
            x = {b: F(1)}
            signs = []
            for i in range(n):
                xe, ex = GA.mul(x, GA.gen(i), squares), GA.mul(GA.gen(i), x, squares)
                # conjugation by a basis vector is diagonal on blades: e x = +- x e
                ok = ok and (GA.eq(xe, ex) or GA.eq(xe, GA.neg(ex)))
                signs.append(1 if GA.eq(xe, ex) else -1)
            if len(b) % 2 == 0 and all(sg == 1 for sg in signs):
                even_central.append(b)
            if len(b) % 2 == 1 and all(sg == -1 for sg in signs):
                odd_anti.append(b)
        ok = ok and even_central == [()] and odd_anti == []
    # the plane rotor is a product of two unit vectors: cos(a/2) + sin(a/2) f1f2 = f1 (cos(a/2) f1 + sin(a/2) f2)
    for (a, b) in CIRCLE_SEEDS:
        ch, sh = circle_point(a, b)
        u = GA.add(GA.scal(ch, GA.gen(0)), GA.scal(sh, GA.gen(1)))
        ok = ok and GA.eq(GA.mul(u, u, SQF), GA.sc(1))
        ok = ok and GA.eq(GA.mul(GA.gen(0), u, SQF), plane_rotor(ch, sh, 0, 1))
    GA.check("in Cl(n,0), n = 1..6: conjugation by a basis vector is diagonal on blades, the only even blade "
             "commuting with every basis vector is the scalar and no odd blade anticommutes with all of them; "
             "the plane rotor is a product of two unit vectors", ok)
    return ok
