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


def check_double_squares_to_a_positive_form_and_is_split():
    premise("synthesis.wall-class-one-rung-obstruction")
    ok = True
    samples = [
        mat([[3]]), mat([[0]]), mat([[2, 1], [1, -3]]), mat([[1, 2], [2, 4]]), mat([[0, 0], [0, 0]]),
        mat([[1, 2, 0], [2, 1, 5], [0, 5, -7]]), mat([[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
        mat([[2, 0, 1, 0], [0, -1, 0, 3], [1, 0, 0, 0], [0, 3, 0, 5]]),
    ]
    count = 0
    for g in samples:
        n = len(g)
        g2 = GA.mat_mul(g, g)
        singular = sig(g)[2] > 0
        for b in (F(0), F(1), F(-2, 3), F(5, 7)):
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
    for x in [F(j, 3) for j in range(-9, 10)]:
        b = bump(x)
        h = mat([[x * x, b], [b, -1]])
        det = h[0][0] * h[1][1] - h[0][1] * h[1][0]
        ok = ok and det == -(x * x + b * b) and sig(h) == (1, 1, 0)
        if b == 0:
            ok = ok and GA.mat_eq(h, direct_sum(mat([[x * x]]), mat([[-1]])))
    # corank bound: a form vanishing on a plane (n = 2, r = 2) has no nondegenerate extension to rank 3
    fills = [(1, 2, 3, 4, 5), (0, 1, 1, 0, -2), (7, -3, 2, 2, 1), (1, 0, 0, 1, 9), (-4, 5, 6, -7, 0)]
    for (p, q, c1, c2, w) in fills:
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
