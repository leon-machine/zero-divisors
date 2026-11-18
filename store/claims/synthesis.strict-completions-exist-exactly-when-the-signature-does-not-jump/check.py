"""Strict completions and the signature jump: exact checks.

A strict completion of a family G of symmetric forms is h = G (+) K outside a neighbourhood U of the set where G
degenerates, with one signature of K there.

(1) The double  h_D = [[g, b], [b, -g]]  (frame orthonormal for an auxiliary metric, b a scalar): its square is
    (g^2 + b^2) on each copy, it has signature (n, n) wherever g is invertible or b is nonzero, it is G (+) (-G)
    where b = 0, and it degenerates where g is singular and b = 0.
(2) Counter-models, one for each tameness clause: x^2 (second order), diag(x, -x) (corank two), x^2 + y^2 and
    [[x, y], [y, -x]] (degenerate at a point). The signature of G is constant off the degeneration set, the double
    is nondegenerate at every sample point with a bump b, and K = -G has one signature outside the bump.
(3) x id in rank four: signatures (4,0) and (0,4), equal residues modulo 8, exterior totals of every G (+) K differ;
    a strict sample completion degenerates at x = +-1 exactly; the double stays nondegenerate and is not strict.
(4) x^2 with one added negative direction; a point of corank r needs r added directions.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def mat(rows):
    return [[F(x) for x in r] for r in rows]


def block(g, b):
    """[[g, b 1], [b 1, -g]] for a symmetric matrix g and a scalar b."""
    n = len(g)
    top = [list(g[i]) + [b if i == j else F(0) for j in range(n)] for i in range(n)]
    bot = [[b if i == j else F(0) for j in range(n)] + [-x for x in g[i]] for i in range(n)]
    return top + bot


def direct_sum(a, k):
    n, m = len(a), len(k)
    return [list(a[i]) + [F(0)] * m for i in range(n)] + [[F(0)] * n + list(k[i]) for i in range(m)]


def sig(m):
    return GA.congruence_signature(m)


def bump(x):
    """1 on [-1, 1], linear to 0 at +-2, 0 beyond."""
    ax = abs(F(x))
    if ax <= 1:
        return F(1)
    if ax >= 2:
        return F(0)
    return 2 - ax


SAMPLE_FORMS = [
    mat([[3]]), mat([[0]]), mat([[2, 1], [1, -3]]), mat([[1, 2], [2, 4]]), mat([[0, 0], [0, 0]]),
    mat([[1, 2, 0], [2, 1, 5], [0, 5, -7]]), mat([[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
    mat([[2, 0, 1, 0], [0, -1, 0, 3], [1, 0, 0, 0], [0, 3, 0, 5]]),
]
SAMPLE_COUPLINGS = (F(0), F(1), F(-2, 3), F(5, 7))
THIRDS = [F(j, 3) for j in range(-9, 10)]
QUARTERS = [F(j, 4) for j in range(-12, 13)]
RANK_THREE_FILLS = [(1, 2, 3), (1, 1, -2), (2, 2, 1), (0, 1, 9), (6, -7, 0)]


def check_double_squares_to_a_positive_form_and_is_split():
    premise("synthesis.wall-class-one-rung-obstruction")
    ok = True
    count = 0
    for g in SAMPLE_FORMS:
        n = len(g)
        g2 = GA.mat_mul(g, g)
        singular = sig(g)[2] > 0
        for b in SAMPLE_COUPLINGS:
            h = block(g, b)
            h2 = GA.mat_mul(h, h)
            want = [[g2[i][j] + (b * b if i == j else 0) for j in range(n)] for i in range(n)]
            ok = ok and GA.mat_eq(h2, direct_sum(want, want))
            s = sig(h)
            if b != 0 or not singular:
                ok = ok and s == (n, n, 0)
            else:
                ok = ok and s[2] == 2 * sig(g)[2] and s[2] > 0
            if b == 0:
                ok = ok and GA.mat_eq(h, direct_sum(g, [[-x for x in row] for row in g]))
            count += 1
    ok = ok and count == 32
    # explicit values: g = [[2, 1], [1, -3]] at b = 5/7, and the singular g = [[1, 2], [2, 4]] at b = 0
    h = block(mat([[2, 1], [1, -3]]), F(5, 7))
    h2 = GA.mat_mul(h, h)
    ok = ok and h2[0][0] == 5 + F(25, 49) and h2[0][1] == -1 and h2[1][1] == 10 + F(25, 49) and h2[0][2] == 0
    ok = ok and h2[2][2] == 5 + F(25, 49) and h2[3][3] == 10 + F(25, 49)
    ok = ok and sig(block(mat([[1, 2], [2, 4]]), F(0))) == (1, 1, 2)
    ok = ok and sig(block(mat([[1, 2], [2, 4]]), F(1, 9))) == (2, 2, 0)
    ok = ok and sig(block(mat([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), F(0))) == (1, 1, 4)
    GA.check("the double squares to (g^2 + b^2) on each copy, is split of signature (n,n) unless g is singular "
             "and b = 0, and is G (+) (-G) at b = 0 (8 forms, 4 couplings)", ok)
    return ok


def check_counter_models_for_each_tameness_clause():
    premise("synthesis.wall-class-one-rung-obstruction")
    ok = True
    line = [F(k, 4) for k in range(-12, 13)]
    # (a) x^2: corank one at 0, signature (1,0) on both sides
    # (b) diag(x, -x): corank two at 0, signature (1,1) on both sides
    models_1d = {
        "a": (lambda x: mat([[x * x]]), (1, 0, 0), 1),
        "b": (lambda x: mat([[x, 0], [0, -x]]), (1, 1, 0), 2),
    }
    for name, (gf, s_off, corank) in models_1d.items():
        n = len(gf(F(1)))
        for x in line:
            g = gf(x)
            ok = ok and (sig(g) == s_off if x != 0 else sig(g)[2] == corank)
            ok = ok and sig(block(g, bump(x))) == (n, n, 0)
        # strictness: K = -G has one signature at the exterior sample points, on both sides
        ext = [sig([[-v for v in row] for row in gf(x)]) for x in (F(-3), F(-5, 2), F(5, 2), F(3))]
        ok = ok and len(set(ext)) == 1 and ext[0] == (s_off[1], s_off[0], 0)
    # (c) x^2 + y^2 on a line and [[x, y], [y, -x]]: degenerate at the origin only
    plane = [(F(i, 2), F(j, 2)) for i in range(-6, 7) for j in range(-6, 7)]
    models_2d = {
        "c1": (lambda x, y: mat([[x * x + y * y]]), (1, 0, 0), 1),
        "c2": (lambda x, y: mat([[x, y], [y, -x]]), (1, 1, 0), 2),
    }
    for name, (gf, s_off, corank) in models_2d.items():
        n = len(gf(F(1), F(0)))
        for (x, y) in plane:
            g = gf(x, y)
            origin = (x == 0 and y == 0)
            ok = ok and (sig(g)[2] == corank if origin else sig(g) == s_off)
            b = max(bump(x), F(0)) * max(bump(y), F(0))
            ok = ok and (b > 0 if origin else True)
            ok = ok and sig(block(g, b)) == (n, n, 0)
    # control: without the coupling the double degenerates on the degeneration set
    ok = ok and sig(block(mat([[0]]), F(0)))[2] == 2 and sig(block(mat([[0, 0], [0, 0]]), F(0)))[2] == 4
    GA.check("x^2, diag(x,-x), x^2+y^2 and [[x,y],[y,-x]]: one signature off the degeneration set, the coupled "
             "double nondegenerate of signature (n,n) at every sample point, K = -G of one exterior signature", ok)
    return ok


def check_signature_jump_obstructs_with_matched_clocks():
    premise("sheaf.conservation-degeneracy-absolute-form")
    premise("std-algebra.periodicity")
    ok = True
    gid = lambda x: [[F(x) if i == j else F(0) for j in range(4)] for i in range(4)]
    s_plus, s_minus = sig(gid(3)), sig(gid(-3))
    ok = ok and s_plus == (4, 0, 0) and s_minus == (0, 4, 0)
    ok = ok and (s_plus[0] - s_plus[1] - (s_minus[0] - s_minus[1])) % 8 == 0
    # exterior totals of G (+) K differ for every one signature of K (here all K of rank up to 4)
    for kp in range(0, 5):
        for kq in range(0, 5 - kp):
            k = [[(F(1) if i < kp else F(-1)) if i == j else F(0) for j in range(kp + kq)] for i in range(kp + kq)]
            tp, tm = sig(direct_sum(gid(3), k)), sig(direct_sum(gid(-3), k))
            ok = ok and tp == (4 + kp, kq, 0) and tm == (kp, 4 + kq, 0) and tp != tm
    # a strict sample: K = diag(1,1,-1,-1), coupling bump(x) * identity; it degenerates exactly at x = +-1
    k = [[(F(1) if i < 2 else F(-1)) if i == j else F(0) for j in range(4)] for i in range(4)]

    def strict(x):
        b = bump(x)
        top = [gid(x)[i] + [b if i == j else F(0) for j in range(4)] for i in range(4)]
        bot = [[b if i == j else F(0) for j in range(4)] + k[i] for i in range(4)]
        return top + bot

    zeros = [x for x in [F(j, 4) for j in range(-12, 13)] if sig(strict(x))[2] > 0]
    ok = ok and zeros == [F(-1), F(1)] and sig(strict(F(1)))[2] == 2 and sig(strict(F(-1)))[2] == 2
    ok = ok and sig(strict(F(3))) == (6, 2, 0) and sig(strict(F(-3))) == (2, 6, 0)
    ok = ok and sig(strict(F(0))) == (4, 4, 0)
    # the double is nondegenerate at every sample point, and its K = -G changes signature: not strict
    ok = ok and all(sig(block(gid(x), bump(x))) == (4, 4, 0) for x in [F(j, 4) for j in range(-12, 13)])
    ok = ok and sig(gid(-3)) != sig(gid(3))
    GA.check("x id in rank four: signatures (4,0) and (0,4) with equal residues modulo 8; exterior totals of "
             "G (+) K differ for each of the 15 signatures of K; a strict sample degenerates at x = +-1 "
             "(corank 2 each); the double is nondegenerate but its K changes signature", ok)
    return ok


def check_one_added_direction_and_the_corank_bound():
    premise("odd-extensions.imported-minimal-completion-degenerate-algebra-rule")
    ok = True
    for x in THIRDS:
        b = bump(x)
        h = mat([[x * x, b], [b, -1]])
        det = h[0][0] * h[1][1] - h[0][1] * h[1][0]
        ok = ok and det == -(x * x + b * b) and sig(h) == (1, 1, 0)
        if b == 0:
            ok = ok and GA.mat_eq(h, direct_sum(mat([[x * x]]), mat([[-1]])))
    h = mat([[F(4, 9), 1], [1, -1]])                       # x = 2/3, b = 1
    ok = ok and h[0][0] * h[1][1] - h[0][1] * h[1][0] == F(-13, 9) and bump(F(2, 3)) == 1
    h = mat([[F(25, 9), F(1, 3)], [F(1, 3), -1]])          # x = 5/3, b = 1/3
    ok = ok and h[0][0] * h[1][1] - h[0][1] * h[1][0] == F(-26, 9) and bump(F(5, 3)) == F(1, 3)
    ok = ok and bump(F(7, 3)) == 0 and sig(mat([[F(49, 9), 0], [0, -1]])) == (1, 1, 0)
    # the place of the degeneration is set by K: G = x with K = +1 degenerates at x = 1, with K = -1 at x = -1
    grid = QUARTERS
    ok = ok and [x for x in grid if sig(mat([[x, bump(x)], [bump(x), 1]]))[2] > 0] == [F(1)]
    ok = ok and [x for x in grid if sig(mat([[x, bump(x)], [bump(x), -1]]))[2] > 0] == [F(-1)]
    ok = ok and [x for x in grid if sig(mat([[x, 0], [0, 1]]))[2] > 0] == [F(0)]
    # the sharper count: G = diag(1, 0) (p, q, r) = (1, 0, 1) inside a nondegenerate rank-three form has (2, 1)
    ok = ok and sig(mat([[1, 0, 0], [0, 0, 1], [0, 1, 5]])) == (2, 1, 0)
    # corank bound: a form vanishing on a plane (n = 2, r = 2) has no nondegenerate extension to rank 3
    for (c1, c2, w) in RANK_THREE_FILLS:
        h3 = mat([[0, 0, c1], [0, 0, c2], [c1, c2, w]])
        ok = ok and sig(h3)[2] >= 1
    # rank n + r = 4 is reached, with r = 2 directions of each sign
    h4 = mat([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]])
    ok = ok and sig(h4) == (2, 2, 0)
    # corank one inside rank two (n = 2, r = 1): rank 3 suffices and has one direction of each sign at least
    h3 = mat([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    ok = ok and sig(h3) == (2, 1, 0) and min(sig(h3)[0], sig(h3)[1]) >= 1
    GA.check("x^2 with one added negative direction has determinant -(x^2 + b^2) and signature (1,1); a form "
             "vanishing on a plane has no nondegenerate extension to rank 3 and one of signature (2,2) in rank 4", ok)
    return ok


# ---------------------------------------------------------------------------------------------------------
# model completions (a constant exterior model), the eigenline around a point, Clifford families
# ---------------------------------------------------------------------------------------------------------
def check_constant_model_for_corank_two_and_the_twisted_eigenline():
    premise("sheaf.conservation-degeneracy-absolute-form")
    ok = True
    # diag(x, -x) with the constant model K0 = diag(1, -1) and coupling b [[1, 1], [1, -1]]
    for x in [F(j, 4) for j in range(-12, 13)]:
        b = bump(x)
        h = mat([[x, 0, b, b], [0, -x, b, -b], [b, b, 1, 0], [b, -b, 0, -1]])
        if x != 0 or b != 0:
            ok = ok and sig(h) == (2, 2, 0)
        if b == 0:
            ok = ok and GA.mat_eq(h, direct_sum(mat([[x, 0], [0, -x]]), mat([[1, 0], [0, -1]])))
        # det h = x^2 + 4 b^4: its Schur complement G - b^2 C K0^-1 C^T = [[x, -2b^2], [-2b^2, -x]]
        schur = mat([[x, -2 * b * b], [-2 * b * b, -x]])
        ok = ok and schur[0][0] * schur[1][1] - schur[0][1] * schur[1][0] == -(x * x + 4 * b ** 4)
    # the same coupling with the identity in place of [[1,1],[1,-1]] degenerates at x = b^2 (here x = 1)
    hbad = mat([[1, 0, 1, 0], [0, -1, 0, 1], [1, 0, 1, 0], [0, 1, 0, -1]])
    ok = ok and sig(hbad)[2] == 2
    # G = [[x, y], [y, -x]] on the unit circle, half-angle parametrisation (c, s): G = [[c^2-s^2, 2cs], [2cs, s^2-c^2]]
    # positive eigenvector (c, s), negative eigenvector (-s, c); half a turn of (c, s) is a whole turn of G
    half = [(F(1), F(0)), (F(4, 5), F(3, 5)), (F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(0), F(1)),
            (F(-5, 13), F(12, 13)), (F(-3, 5), F(4, 5)), (F(-4, 5), F(3, 5)), (F(-1), F(0))]
    for (c, s) in half:
        g = mat([[c * c - s * s, 2 * c * s], [2 * c * s, s * s - c * c]])
        ok = ok and c * c + s * s == 1
        ok = ok and [g[0][0] * c + g[0][1] * s, g[1][0] * c + g[1][1] * s] == [c, s]
        ok = ok and [g[0][0] * (-s) + g[0][1] * c, g[1][0] * (-s) + g[1][1] * c] == [s, -c]
    # continuity along the half turn: consecutive eigenvectors have positive inner product, the last is minus the first
    ok = ok and all(half[i][0] * half[i + 1][0] + half[i][1] * half[i + 1][1] > 0 for i in range(len(half) - 1))
    ok = ok and half[-1] == (-half[0][0], -half[0][1])
    g0 = mat([[1, 0], [0, -1]])
    ok = ok and mat([[half[0][0] ** 2 - half[0][1] ** 2, 0], [0, half[0][1] ** 2 - half[0][0] ** 2]]) == g0
    ok = ok and mat([[half[-1][0] ** 2 - half[-1][1] ** 2, 0], [0, half[-1][1] ** 2 - half[-1][0] ** 2]]) == g0
    GA.check("diag(x,-x) with the constant model diag(1,-1): Schur determinant -(x^2 + 4b^4), signature (2,2) at "
             "every sample point; around the origin the positive eigenvector of [[x,y],[y,-x]] is (c,s) at half "
             "angle and returns to its negative after one turn, as does the negative one", ok)
    return ok


def kron(a, b):
    return [[a[i][j] * b[k][m] for j in range(len(a)) for m in range(len(b))]
            for i in range(len(a)) for k in range(len(b))]


def symmetric_anticommutant_dim(gens, n):
    """Dimension of the space of symmetric X with X E + E X = 0 for every E in gens."""
    basis = []
    for i in range(n):
        for j in range(i, n):
            X = [[F(0)] * n for _ in range(n)]
            X[i][j] = F(1)
            X[j][i] = F(1)
            basis.append(X)
    rows = []
    for X in basis:
        row = []
        for E in gens:
            A = GA.mat_mul(X, E)
            B = GA.mat_mul(E, X)
            row += [A[i][j] + B[i][j] for i in range(n) for j in range(n)]
        rows.append(row)
    return len(basis) - GA.mat_rank(rows)


def check_clifford_multiplication_families_and_the_added_generator():
    premise("std-algebra.periodicity")
    ok = True
    one = mat([[1, 0], [0, 1]])
    sz = mat([[1, 0], [0, -1]])
    sx = mat([[0, 1], [1, 0]])
    ep = mat([[0, 1], [-1, 0]])
    fam = {
        1: ([mat([[1]])], 1),
        2: ([sz, sx], 2),
        3: ([kron(sz, one), kron(sx, one), kron(ep, ep)], 4),
        4: ([kron(kron(sz, one), one), kron(kron(sx, one), one), kron(kron(ep, ep), one), kron(kron(ep, sx), ep)], 8),
    }
    extra = kron(kron(ep, sz), ep)                 # a fifth generator on the module of dimension eight
    for m, (gens, n) in fam.items():
        ident = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
        for a, Ea in enumerate(gens):
            ok = ok and GA.mat_eq(Ea, [list(r) for r in zip(*Ea)])                 # symmetric
            ok = ok and GA.mat_eq(GA.mat_mul(Ea, Ea), ident)                       # squares to one
            for Eb in gens[a + 1:]:
                s = GA.mat_mul(Ea, Eb)
                t = GA.mat_mul(Eb, Ea)
                ok = ok and all(s[i][j] + t[i][j] == 0 for i in range(n) for j in range(n))
        # the family g(x) = sum x_i E_i squares to |x|^2 and has signature (n/2, n/2) off the origin for m >= 2
        x = [F(2), F(-1), F(3), F(1, 2)][:m]
        g = [[sum(x[i] * gens[i][r][c] for i in range(m)) for c in range(n)] for r in range(n)]
        q = sum(v * v for v in x)
        ok = ok and GA.mat_eq(GA.mat_mul(g, g), [[q if i == j else F(0) for j in range(n)] for i in range(n)])
        if m >= 2:
            ok = ok and sig(g) == (n // 2, n // 2, 0)
        # symmetric maps anticommuting with every generator: none for m = 1, 2, 3 on the minimal module
        dim = symmetric_anticommutant_dim(gens, n)
        ok = ok and dim == {1: 0, 2: 0, 3: 0, 4: 1}[m]
    # m = 4: the fifth generator is symmetric, squares to one, anticommutes with the four, and g + b E5 squares to |x|^2 + b^2
    gens, n = fam[4]
    ident = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    ok = ok and GA.mat_eq(extra, [list(r) for r in zip(*extra)]) and GA.mat_eq(GA.mat_mul(extra, extra), ident)
    for E in gens:
        s = GA.mat_mul(E, extra)
        t = GA.mat_mul(extra, E)
        ok = ok and all(s[i][j] + t[i][j] == 0 for i in range(n) for j in range(n))
    for (x, b) in [((F(0), F(0), F(0), F(0)), F(1)), ((F(1), F(2), F(0), F(-1)), F(1, 2)), ((F(3), F(0), F(1), F(1)), F(0))]:
        h = [[sum(x[i] * gens[i][r][c] for i in range(4)) + b * extra[r][c] for c in range(n)] for r in range(n)]
        q = sum(v * v for v in x) + b * b
        ok = ok and GA.mat_eq(GA.mat_mul(h, h), [[q if i == j else F(0) for j in range(n)] for i in range(n)])
        ok = ok and sig(h) == (4, 4, 0)
    # minimal module dimensions of Cl(m,0), m = 1..10, from the classification: equal consecutive dimensions at 4, 6, 7, 8
    dims = {1: 1, 2: 2, 3: 4, 4: 8, 5: 8, 6: 16, 7: 16, 8: 16, 9: 16, 10: 32}
    ok = ok and [m for m in range(1, 10) if dims[m] == dims[m + 1]] == [4, 6, 7, 8]
    ok = ok and all(dims[m] == fam[m][1] for m in fam)
    GA.check("multiplication by the position vector on the minimal module of Cl(m,0), m = 1..4: symmetric generators, "
             "g^2 = |x|^2; no further symmetric anticommuting generator for m = 1, 2, 3 and one for m = 4, where "
             "g + b E5 squares to |x|^2 + b^2 on the same module", ok)
    return ok
