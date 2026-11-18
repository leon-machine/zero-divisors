"""Sufficiency for a degeneration inside a ball: the rotation homotopy and two worked families, exact.

(1) For an orthogonal F of rank N the family
        Phi(c, s) = (F (+) 1) R (1 (+) F^T) R^T,   R = [[c, -s], [s, c]] (x) 1_N,   c^2 + s^2 = 1,
    is orthogonal, equals F (+) F^T at (c, s) = (1, 0) and the identity at (0, 1).
(2) Two copies of [[x, y], [y, -x]] on R^4 over the plane: the eigenbundles on a circle are trivial (frames
    quadratic in the half-angle functions, so polynomial in the point), and the form built from (1) on R^8, with
    the fixed exterior form +1 on four added directions, is nondegenerate of signature (6, 2) at every sample
    point, equals G (+) 1 outside the disc of radius 3 and is constant inside the disc of radius 1. A constant
    change of basis of the added directions gives a completion for another fixed form of the same signature.
(3) The family [[x^2 - y^2, 2xy], [2xy, y^2 - x^2]] (the line of w itself): eigenlines trivial, spanned by
    (x, y) and (-y, x); the positive line turns twice in the circle of lines; with one added positive direction
    the reflection along n = (-b y, b x, 1 - b) completes it with signature (2, 1).
(4) One copy of [[x, y], [y, -x]]: the unit eigenvector in the half-angle reverses after one turn (the stored
    obstruction of degree one), so no frame as in (2) exists for it.
(5) Rotors of the plane: cos b + sin b f1f2 induces the rotation through -2b. The loop of rotations through
    4 pi t (the winding-two family on a circle) has the closed lift b = -2 pi t; read as a rotation through b,
    that lift is the loop through -2 pi t, whose own lift b = pi t ends at the negative of its start.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

N_BLOCK = 4
# rational points (c, s) of the unit circle from tau = tan(angle/2); TAUS increases, the angle runs over (-pi, pi)
TAUS_POS = [F(0), F(1, 5), F(2, 5), F(3, 5), F(4, 5), F(1), F(5, 4), F(5, 3), F(5, 2), F(5)]
TAUS = [-t for t in reversed(TAUS_POS[1:])] + TAUS_POS
# radii: outside the ball (>= 3), the scaling collar [2, 3], the rotation collar [1, 2], the core (<= 1)
RADII = [F(0), F(1, 2), F(1), F(5, 4), F(3, 2), F(7, 4), F(2), F(9, 4), F(5, 2), F(3), F(7, 2), F(5)]
QUARTER_TAUS = [F(0), F(1, 4), F(1, 3), F(1, 2), F(2, 3), F(3, 4), F(1)]   # tan(t/2) for t in [0, pi/2]
R_OUT, R_MID, R_IN = F(3), F(2), F(1)
SAMPLE_ROTATIONS = [(F(3, 5), F(4, 5)), (F(5, 13), F(-12, 13)), (F(0), F(1)), (F(-7, 25), F(24, 25))]
GRID = [F(j, 2) for j in range(-6, 7)]
# an invertible constant change of basis of the four added directions, for another form of the same signature
LAMBDA = [[F(1), F(2), F(0), F(0)], [F(0), F(1), F(3), F(0)], [F(0), F(0), F(1), F(-1)], [F(1), F(0), F(0), F(1)]]
SQ2 = GA.sig(2, 0)
# half-turn parameters (a, b): the point ((a^2-b^2)/(a^2+b^2), 2ab/(a^2+b^2)) runs over the upper half circle
HALF_TURN = [(F(8 - j), F(j)) for j in range(9)]


def circ(tau):
    tau = F(tau)
    d = 1 + tau * tau
    return (1 - tau * tau) / d, 2 * tau / d


def ident(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def transpose(m):
    return [list(r) for r in zip(*m)]


def dsum(a, b):
    n, m = len(a), len(b)
    return [list(a[i]) + [F(0)] * m for i in range(n)] + [[F(0)] * n + list(b[i]) for i in range(m)]


def mm(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = GA.mat_mul(out, m)
    return out


def rot_blocks(c, s, n):
    """[[c, -s], [s, c]] (x) 1_n."""
    top = [[c if i == j else F(0) for j in range(n)] + [-s if i == j else F(0) for j in range(n)] for i in range(n)]
    bot = [[s if i == j else F(0) for j in range(n)] + [c if i == j else F(0) for j in range(n)] for i in range(n)]
    return top + bot


def phi(f, c, s):
    n = len(f)
    r = rot_blocks(c, s, n)
    return mm(dsum(f, ident(n)), r, dsum(ident(n), transpose(f)), transpose(r))


def frame_two_copies(c, s):
    """Columns u1, u2 (positive) and v1, v2 (negative) for two copies of [[x,y],[y,-x]] at the angle (c, s).

    With C, S the cosine and sine of half the angle: C^2 = (1+c)/2, S^2 = (1-c)/2, CS = s/2."""
    cc, ss, cs = (1 + c) / 2, (1 - c) / 2, s / 2
    u1 = [cc, cs, cs, ss]
    u2 = [-cs, -ss, cc, cs]
    v1 = [-cs, cc, -ss, cs]
    v2 = [ss, -cs, -cs, cc]
    return transpose([u1, u2, v1, v2])


def g_two_copies(x, y):
    return [[x, y, F(0), F(0)], [y, -x, F(0), F(0)], [F(0), F(0), x, y], [F(0), F(0), y, -x]]


D8 = [[(F(1) if i < 2 or i >= 4 else F(-1)) if i == j else F(0) for j in range(8)] for i in range(8)]
D4 = [[(F(1) if i < 2 else F(-1)) if i == j else F(0) for j in range(4)] for i in range(4)]


def completion(r, c, s):
    """The form on R^8 at radius r and angle (c, s)."""
    f = frame_two_copies(c, s)
    sigma = mm(f, D4, transpose(f))                       # the involution of G on the circle
    if r >= R_OUT:
        return dsum(g_two_copies(r * c, r * s), ident(N_BLOCK))
    if r >= R_MID:
        lam = R_OUT - r                                   # 0 at the sphere, 1 at radius 2
        scale = (1 - lam) * R_OUT + lam
        return dsum([[scale * a for a in row] for row in sigma], ident(N_BLOCK))
    if r >= R_IN:
        ct, st = circ(R_MID - r)                          # the angle t from 0 (r = 2) to pi/2 (r = 1)
        p = phi(f, ct, st)
        return mm(p, D8, transpose(p))
    return [list(row) for row in D8]


def check_rotation_homotopy_joins_f_plus_f_inverse_to_the_identity():
    ok = True
    frames = [frame_two_copies(*circ(t)) for t in TAUS[::3]]
    for (c, s) in SAMPLE_ROTATIONS:
        frames.append([[c, -s, F(0), F(0)], [s, c, F(0), F(0)], [F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(-1)]])
    for f in frames:
        ok = ok and GA.mat_eq(mm(transpose(f), f), ident(4))
        ok = ok and GA.mat_eq(phi(f, F(1), F(0)), dsum(f, transpose(f)))
        ok = ok and GA.mat_eq(phi(f, F(0), F(1)), ident(8))
        for tq in QUARTER_TAUS:
            c, s = circ(tq)
            p = phi(f, c, s)
            ok = ok and GA.mat_eq(mm(transpose(p), p), ident(8))
    ok = ok and circ(QUARTER_TAUS[0]) == (1, 0) and circ(QUARTER_TAUS[-1]) == (0, 1)
    GA.check("Phi = (F + 1) R (1 + F^T) R^T is orthogonal at seven angles of the quarter turn, equals F + F^T at "
             "angle 0 and the identity at the quarter turn, for eight orthogonal F of rank four", ok)
    return ok


def check_two_copies_of_the_plane_family_complete_with_a_fixed_form():
    premise("synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump")
    ok = True
    for t in TAUS:
        c, s = circ(t)
        f = frame_two_copies(c, s)
        ok = ok and GA.mat_eq(mm(transpose(f), f), ident(4))
        # the frame diagonalises G on the unit circle: G = F diag(1, 1, -1, -1) F^T
        ok = ok and GA.mat_eq(mm(f, D4, transpose(f)), g_two_copies(c, s))
        for r in RADII:
            h = completion(r, c, s)
            ok = ok and GA.mat_eq(h, transpose(h))
            ok = ok and GA.congruence_signature(h) == (6, 2, 0)
            if r >= R_OUT:
                ok = ok and GA.mat_eq(h, dsum(g_two_copies(r * c, r * s), ident(N_BLOCK)))
            if r <= R_IN:
                ok = ok and GA.mat_eq(h, D8)
        # the three seams: the pieces agree at radius 3, 2 and 1
        sigma = mm(f, D4, transpose(f))
        ok = ok and GA.mat_eq(completion(R_OUT, c, s), dsum([[R_OUT * a for a in row] for row in sigma], ident(4)))
        p0 = phi(f, F(1), F(0))
        ok = ok and GA.mat_eq(mm(p0, D8, transpose(p0)), dsum(sigma, ident(4)))
        ok = ok and GA.mat_eq(completion(R_MID, c, s), dsum(sigma, ident(4)))
        ok = ok and GA.mat_eq(completion(R_IN, c, s), D8)
    # another fixed form of the same signature: K0' = L^T L, completion (1 + L)^T h (1 + L)
    ok = ok and GA.mat_rank(LAMBDA) == 4
    k0p = mm(transpose(LAMBDA), LAMBDA)
    ok = ok and GA.congruence_signature(k0p) == (4, 0, 0) and not GA.mat_eq(k0p, ident(4))
    lam = dsum(ident(4), LAMBDA)
    for t in TAUS[::4]:
        c, s = circ(t)
        for r in RADII:
            hp = mm(transpose(lam), completion(r, c, s), lam)
            ok = ok and GA.congruence_signature(hp) == (6, 2, 0)
            if r >= R_OUT:
                ok = ok and GA.mat_eq(hp, dsum(g_two_copies(r * c, r * s), k0p))
    # the undeformed sum degenerates at the origin; the family has signature (2, 2) elsewhere
    ok = ok and GA.congruence_signature(dsum(g_two_copies(F(0), F(0)), ident(4))) == (4, 0, 4)
    ok = ok and all(GA.congruence_signature(g_two_copies(x, y)) == (2, 2, 0)
                    for x in GRID for y in GRID if (x, y) != (0, 0))
    GA.check("two copies of [[x,y],[y,-x]]: frames of both eigenbundles polynomial on the circle; the form built "
             "from the rotation homotopy on R^8 has signature (6,2) at 19 angles and 12 radii, is G + 1 outside "
             "radius 3, constant inside radius 1, and the pieces agree at the seams", ok)
    return ok


def quadrant(x, y):
    if x > 0 and y >= 0:
        return 0
    if x <= 0 and y > 0:
        return 1
    if x < 0 and y <= 0:
        return 2
    return 3


def turns(points):
    """Number of turns of a closed chain of nonzero plane vectors whose steps move less than a quadrant."""
    total = 0
    for (a, b) in zip(points, points[1:] + points[:1]):
        d = (quadrant(*b) - quadrant(*a)) % 4
        if d == 3:
            d = -1
        if d == 2:
            return None
        total += d
    return F(total, 4)


def bump(q):
    """0 for q <= 1, q - 1 on [1, 2], 1 for q >= 2 (q the squared radius)."""
    q = F(q)
    return F(0) if q <= 1 else (F(1) if q >= 2 else q - 1)


def winding_two_completion(x, y):
    q = x * x + y * y
    b = bump(q)
    n = [-b * y, b * x, 1 - b]
    nn = sum(a * a for a in n)
    refl = [[(F(1) if i == j else F(0)) - 2 * n[i] * n[j] / nn for j in range(3)] for i in range(3)]
    if q <= 2:
        return refl
    lam = F(1) if q >= 3 else q - 2                       # 0 at q = 2, 1 from q = 3 on
    scale = (1 - lam) + lam * q
    return [[refl[i][j] * (scale if (i < 2 and j < 2) else F(1)) for j in range(3)] for i in range(3)]


def check_winding_two_family_needs_one_added_direction():
    ok = True
    circle = [circ(t) for t in TAUS] + [(F(-1), F(0))]
    lines, doubled = [], []
    for (c, s) in circle:
        g = [[c * c - s * s, 2 * c * s], [2 * c * s, s * s - c * c]]
        # eigenvectors: w = (c, s) with value +1 and (-s, c) with value -1: both lines have global sections
        ok = ok and GA.mat_mul(g, [[c], [s]]) == [[c], [s]]
        ok = ok and GA.mat_mul(g, [[-s], [c]]) == [[s], [-c]]
        lines.append((c, s))
        doubled.append((c * c - s * s, 2 * c * s))       # the line of angle a is the point 2a of the circle of lines
    ok = ok and turns(lines) == 1 and turns(doubled) == 2
    for x in GRID:
        for y in GRID:
            q = x * x + y * y
            g = [[x * x - y * y, 2 * x * y], [2 * x * y, y * y - x * x]]
            ok = ok and GA.congruence_signature(g) == ((1, 1, 0) if q != 0 else (0, 0, 2))
            h = winding_two_completion(x, y)
            ok = ok and GA.mat_eq(h, transpose(h)) and GA.congruence_signature(h) == (2, 1, 0)
            if q >= 3:
                ok = ok and GA.mat_eq(h, dsum(g, [[F(1)]]))
            if q <= 1:
                ok = ok and h == [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(-1)]]
    GA.check("[[x^2-y^2, 2xy],[2xy, y^2-x^2]]: eigenlines spanned by (x,y) and (-y,x); the positive line turns "
             "twice in the circle of lines; with one added positive direction the reflection along "
             "(-b y, b x, 1-b) has signature (2,1) on a 13 by 13 grid and equals G + 1 outside radius^2 = 3", ok)
    return ok


def check_one_copy_has_no_frame():
    premise("synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump")
    ok = True
    # half-angle points (C, S); the angle point is (C^2 - S^2, 2CS); (C, S) and (-C, -S) give the same point
    for t in TAUS_POS:
        ch, sh = circ(t)
        c, s = ch * ch - sh * sh, 2 * ch * sh
        g = [[c, s], [s, -c]]
        ok = ok and GA.mat_mul(g, [[ch], [sh]]) == [[ch], [sh]]
        ok = ok and GA.mat_mul(g, [[-sh], [ch]]) == [[sh], [-ch]]
    # along the half turn of (C, S) from (1, 0) to (-1, 0) the angle point makes one full turn
    half = [circ(t) for t in TAUS_POS] + [(F(-1), F(0))]
    ok = ok and half[0] == (1, 0) and half[-1] == (-1, 0)
    full = [(ch * ch - sh * sh, 2 * ch * sh) for (ch, sh) in half]
    ok = ok and full[0] == full[-1] == (1, 0) and turns(full[:-1]) == 1
    GA.check("one copy of [[x,y],[y,-x]]: the unit positive eigenvector (C, S) in the half angle runs from (1,0) "
             "to (-1,0) while the point makes one full turn", ok)
    return ok


def unit_point(a, b):
    d = a * a + b * b
    return (a * a - b * b) / d, 2 * a * b / d


def plane_rotor(cb, sb):
    """cos b + sin b f1f2."""
    return GA.add(GA.sc(cb), GA.scal(sb, {(0, 1): F(1)}))


def rotation_of(r):
    """Matrix of v -> r v r~ on the plane, columns the images of f1, f2."""
    cols = []
    for i in range(2):
        img = GA.mul(GA.mul(r, GA.gen(i), SQ2), GA.reverse(r), SQ2)
        cols.append([img.get((0,), F(0)), img.get((1,), F(0))])
    return [[cols[0][0], cols[1][0]], [cols[0][1], cols[1][1]]]


def check_double_lift_of_the_winding_two_loop():
    premise("std-algebra.spin-double-cover")
    ok = True
    first, second = [], []
    for (a, b) in HALF_TURN:
        # (c1, s1): the angle pi t, t from 0 to 1; doubled once: 2 pi t; doubled twice: 4 pi t
        c1, s1 = unit_point(a, b)
        c2, s2 = c1 * c1 - s1 * s1, 2 * c1 * s1
        c4, s4 = c2 * c2 - s2 * s2, 2 * c2 * s2
        r = plane_rotor(c2, -s2)                              # b = -2 pi t
        ok = ok and GA.eq(GA.mul(r, GA.reverse(r), SQ2), GA.sc(1))
        ok = ok and rotation_of(r) == [[c4, -s4], [s4, c4]]  # the rotation through 4 pi t
        first.append(r)
        # j(r) is the rotation through -2 pi t; its lift is the rotor with b = pi t
        r2 = plane_rotor(c1, s1)
        ok = ok and rotation_of(r2) == [[c2, s2], [-s2, c2]]  # the rotation through -2 pi t
        second.append(r2)
    ok = ok and GA.eq(first[0], GA.sc(1)) and GA.eq(first[-1], GA.sc(1))           # the first lift closes
    ok = ok and GA.eq(second[0], GA.sc(1)) and GA.eq(second[-1], GA.sc(-1))        # the second does not
    ok = ok and GA.eq(first[4], GA.sc(-1))                                         # half way the first lift is -1
    GA.check("cos b + sin b f1f2 induces the rotation through -2b; the loop of rotations through 4 pi t lifts to "
             "the closed loop b = -2 pi t, and the rotation loop through -2 pi t lifts to b = pi t, ending at -1", ok)
    return ok
