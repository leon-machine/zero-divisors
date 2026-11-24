"""synthesis.additive-weights-on-the-rational-projectors-are-linear-in-every-size-from-four: exact checks.

Three algebras are used.  Cl(3,3) of three modes: e_k (square +1, index 2k), f_k (square -1, index 2k+1); the
dagger sends a blade to its inverse.  Cl(n,0) for n = 5..8: a vector of Q^n is a vector of the algebra and the
reflection in u is x -> -u x u^{-1}.  Cl(3,0): its even subalgebra, as in the two-mode theorem.  Everything is
integer or Fraction arithmetic.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

ONE = GA.sc(F(1))


def int_sqrt(n):
    x = 0
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


def four_squares(n):
    a = int_sqrt(n)
    while a >= 0:
        r1 = n - a * a
        b = min(a, int_sqrt(r1))
        while b >= 0:
            r2 = r1 - b * b
            c = min(b, int_sqrt(r2))
            while c >= 0:
                r3 = r2 - c * c
                d = int_sqrt(r3)
                if d * d == r3 and d <= c:
                    return (a, b, c, d)
                c -= 1
            b -= 1
        a -= 1
    return None


def vec(r):
    out = {}
    for i, c in enumerate(r):
        if c != 0:
            out[(i,)] = F(c)
    return out


def comps(x, n):
    return [x.get((i,), F(0)) for i in range(n)]


def dot(a, b):
    return sum(F(x) * F(y) for x, y in zip(a, b))


def reflect(u, x, n):
    """-u x u^{-1} in Cl(n,0), for vectors given by components."""
    sq = GA.sig(n, 0)
    U = vec(u)
    uu = dot(u, u)
    y = GA.scal(F(-1) / uu, GA.mul(GA.mul(U, vec(x), sq), U, sq))
    assert all(len(b) == 1 for b in y)
    return comps(y, n)


def support(r):
    return [i for i, c in enumerate(r) if c != 0]


# sample vectors of clause (ii): supports of size 5 to 8; several squares r.r of the kind 4^a(8b+7) times a square,
# and the vector of eight ones, for which r.r - r_j^2 = 7 for every j
SAMPLES = [
    (1, 1, 1, 1, 1),
    (1, 1, 1, 2, 3),
    (2, 1, 1, 1, 0, 3),
    (1, 2, 3, 4, 5, 6),
    (1, 1, 1, 1, 1, 1, 1),
    (3, -1, 2, 5, 1, 0, 4),
    (1, 1, 1, 1, 1, 1, 1, 1),
    (F(1, 2), 1, F(-2, 3), 3, 1, F(5, 7), 2, 1),
    (0, 2, 0, 1, 1, 3, 1, 1),
    (5, 4, 3, 2, 1, 1, 2, 3),
]


def construction(r):
    """The data of the induction step for a vector r with support of size at least 5."""
    n = len(r)
    S = support(r)
    T = S[:4]
    rr = dot(r, r)
    q = four_squares(rr.numerator * rr.denominator)
    rp = [F(0)] * n
    for t, c in zip(T, q):
        rp[t] = F(c, rr.denominator)
    u = [F(a) - b for a, b in zip(r, rp)]
    return n, S, T, rp, u


def check_three_modes_are_the_rational_matrices_of_size_eight_and_the_adjoint_is_the_transpose():
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    sq = (1, -1, 1, -1, 1, -1)
    half = F(1, 2)
    e = [GA.gen(2 * k) for k in range(3)]
    f = [GA.gen(2 * k + 1) for k in range(3)]
    v = [GA.scal(half, GA.add(e[k], f[k])) for k in range(3)]
    w = [GA.scal(half, GA.sub(e[k], f[k])) for k in range(3)]

    def dag(x):
        out = {}
        for b, c in x.items():
            s, bb = GA.blade_mul(b, b, sq)
            out[b] = c * s                # b b = s (a sign), so the inverse of the blade b is s b
        return out

    ok = True
    ok = ok and all(GA.eq(dag(v[k]), w[k]) for k in range(3))
    P0 = ONE
    for k in range(3):
        P0 = GA.mul(P0, GA.mul(w[k], v[k], sq), sq)
    s = []
    for mask in range(8):
        x = P0
        for k in (2, 1, 0):
            if mask >> k & 1:
                x = GA.mul(v[k], x, sq)
        s.append(x)
    # s_I^dagger s_J = delta_IJ P0
    for i in range(8):
        for j in range(8):
            g = GA.mul(dag(s[i]), s[j], sq)
            ok = ok and GA.eq(g, P0 if i == j else {})

    def mat(x):
        M = [[F(0)] * 8 for _ in range(8)]
        for i in range(8):
            for j in range(8):
                g = GA.mul(GA.mul(dag(s[i]), x, sq), s[j], sq)
                if g:
                    c = g.get((), F(0)) / P0[()]
                    if not GA.eq(g, GA.scal(c, P0)):
                        return None
                    M[i][j] = c
        return M

    gens = e + f
    mats = [mat(g) for g in gens]
    ok = ok and all(m is not None for m in mats)
    # generators of square +1 are symmetric matrices, of square -1 antisymmetric: the adjoint is the transpose
    for k in range(3):
        me, mf = mat(e[k]), mat(f[k])
        ok = ok and all(me[i][j] == me[j][i] for i in range(8) for j in range(8))
        ok = ok and all(mf[i][j] == -mf[j][i] for i in range(8) for j in range(8))
    # the 64 blades map to 64 independent matrices
    rows = []
    for b in GA.all_blades(6):
        m = mat({b: F(1)})
        ok = ok and m is not None
        rows.append([m[i][j] for i in range(8) for j in range(8)])
    ok = ok and GA.mat_rank(rows) == 64
    GA.check("Cl(3,3): s_I^dagger s_J = delta P0, e_k symmetric, f_k antisymmetric, 64 blades of rank 64", ok)
    return ok


def check_a_reflection_carries_a_coordinate_four_space_onto_one_through_the_vector():
    premise("std-algebra.reflection")
    premise("synthesis.positive-rationals-are-the-squares-of-the-even-subalgebra-of-cl-three")
    ok, count = True, 0
    for r in SAMPLES:
        n, S, T, rp, u = construction(r)
        ok = ok and len(S) >= 5 and dot(rp, rp) == dot(r, r) and any(c != 0 for c in u)
        ok = ok and support(rp) == [t for t in T if rp[t] != 0]
        # the reflection sends r' to r and is an isometry on the coordinate four-space of T
        ok = ok and reflect(u, rp, n) == [F(c) for c in r]
        img = []
        for t in T:
            x = [F(0)] * n
            x[t] = F(1)
            img.append(reflect(u, x, n))
        ok = ok and all(dot(img[a], img[b]) == (1 if a == b else 0) for a in range(4) for b in range(4))
        # every image has support inside the support of r
        ok = ok and all(set(support(y)) <= set(S) for y in img)
        count += 1
    ok = ok and count == 10
    GA.check("ten vectors: r' in a coordinate four-space with r'.r' = r.r, -u r' u^-1 = r, isometry, supports", ok)
    return ok


def check_vectors_of_smaller_support_fill_at_least_three_hyperplanes_and_force_a_quadratic_form_to_vanish():
    premise("std-algebra.reflection")
    ok, count = True, 0
    mons = [(a, b) for a in range(4) for b in range(a, 4)]
    for r in SAMPLES:
        n, S, T, rp, u = construction(r)
        img = []
        for t in T:
            x = [F(0)] * n
            x[t] = F(1)
            img.append(reflect(u, x, n))
        # coordinate functionals of the image, as rows on Q^4: one for each index of the support
        funcs = {i: tuple(img[a][i] for a in range(4)) for i in S}
        ok = ok and all(any(c != 0 for c in fn) for fn in funcs.values())
        ok = ok and GA.mat_rank([list(fn) for fn in funcs.values()]) == 4
        # the kernel of the functional of an index t of T: the image there has support smaller than that of r;
        # the common kernel of the functionals outside T: the image is the vector itself, of support at most 4
        hyper = [[funcs[t]] for t in T]
        outside = [funcs[i] for i in S if i not in T]
        ok = ok and GA.mat_rank([list(fn) for fn in outside]) == 1
        hyper.append([outside[0]])
        # pairwise distinct kernels: at least three
        distinct = []
        for h in hyper:
            if all(GA.mat_rank([list(h[0]), list(d[0])]) == 2 for d in distinct):
                distinct.append(h)
        ok = ok and len(distinct) >= 3
        # quadratic forms on Q^4 vanishing on three of the hyperplanes: only zero
        pts = []
        for h in distinct[:3]:
            fn = h[0]
            piv = next(i for i in range(4) if fn[i] != 0)
            basis = []
            for i in range(4):
                if i == piv:
                    continue
                x = [F(0)] * 4
                x[i] = F(1)
                x[piv] = -fn[i] / fn[piv]
                basis.append(x)
            ok = ok and all(dot(fn, x) == 0 for x in basis)
            for a in range(3):
                pts.append(basis[a])
                for b in range(a + 1, 3):
                    pts.append([p + q for p, q in zip(basis[a], basis[b])])
        ok = ok and len(pts) == 18
        ok = ok and GA.mat_rank([[x[a] * x[b] for a, b in mons] for x in pts]) == 10
        # the supports: on the kernel of the functional of t the image misses t; on the last kernel it lies in Q^T
        for t in T:
            fn = funcs[t]
            piv = next(i for i in range(4) if fn[i] != 0)
            for i in range(4):
                if i == piv:
                    continue
                x = [F(0)] * 4
                x[i] = F(1)
                x[piv] = -fn[i] / fn[piv]
                y = [sum(x[a] * img[a][j] for a in range(4)) for j in range(n)]
                ok = ok and y[t] == 0 and set(support(y)) <= set(S) - {t}
        fn = outside[0]
        piv = next(i for i in range(4) if fn[i] != 0)
        for i in range(4):
            if i == piv:
                continue
            x = [F(0)] * 4
            x[i] = F(1)
            x[piv] = -fn[i] / fn[piv]
            y = [sum(x[a] * img[a][j] for a in range(4)) for j in range(n)]
            ok = ok and set(support(y)) <= set(T)
        count += 1
    ok = ok and count == 10
    GA.check("ten vectors: five nonzero functionals of rank 4, three distinct kernels, 18 points of rank 10", ok)
    return ok


def check_two_rational_vectors_need_not_lie_in_a_four_space_similar_to_the_standard_one():
    premise("std-algebra.quaternions")
    premise("synthesis.positive-rationals-are-the-squares-of-the-even-subalgebra-of-cl-three")
    ok = True
    # the pair of the counterexample, in Cl(5,0): the bivector u ^ w has squared size 7
    sq = GA.sig(5, 0)
    U, W = vec((1, 0, 0, 0, 0)), vec((0, 1, 1, 1, 2))
    UW = GA.mul(U, W, sq)
    biv = {b: c for b, c in UW.items() if len(b) == 2}
    size = GA.mul(biv, GA.reverse(biv), sq)
    ok = ok and set(size) == {()} and size[()] == 7
    ok = ok and UW.get((), F(0)) == 0
    # in the even subalgebra of Cl(3,0): |x|^2 |y|^2 - (x.y)^2 is the sum of the three squared bivector
    # components of x y~
    sq3 = (1, 1, 1)
    B = [GA.mul(GA.gen(2), GA.gen(1), sq3), GA.mul(GA.gen(0), GA.gen(2), sq3), GA.mul(GA.gen(1), GA.gen(0), sq3)]

    def ev(x):
        out = GA.sc(F(x[0]))
        for k in range(3):
            out = GA.add(out, GA.scal(F(x[k + 1]), B[k]))
        return out

    samples = [(1, 2, 3, 4), (2, -1, 0, 5), (F(1, 2), F(1, 3), -2, 1), (0, 1, 1, 1), (1, 1, 1, 2), (3, 1, -4, 1)]
    cnt = 0
    for x in samples:
        for y in samples:
            Z = GA.mul(ev(x), GA.reverse(ev(y)), sq3)
            z0 = Z.get((), F(0))
            zb = [Z.get(b, F(0)) for b in ((1, 2), (0, 2), (0, 1))]
            ok = ok and z0 == dot(x, y)
            ok = ok and dot(x, x) * dot(y, y) - z0 * z0 == sum(c * c for c in zb)
            cnt += 1
    ok = ok and cnt == 36
    # 7 is not a sum of three squares of rationals with denominator up to 12 (the general statement is the premise)
    hit = False
    for d in range(1, 13):
        t = 7 * d * d
        for a in range(int_sqrt(t) + 1):
            for b in range(a, int_sqrt(t - a * a) + 1):
                c2 = t - a * a - b * b
                c = int_sqrt(c2)
                if c * c == c2:
                    hit = True
    ok = ok and not hit
    GA.check("the pair e_1, e_2 + e_3 + e_4 + 2 e_5 has |u ^ w|^2 = 7; the three-square identity on 36 pairs", ok)
    return ok


def check_linear_weights_sum_to_the_trace_on_a_reflected_frame_and_are_recovered_from_their_values():
    ok = True
    n = 6
    # a symmetric rho with entries of both signs; the weight of a ray is rho(r,r)/(r.r)
    rho = [[F((3 * i + 5 * j + i * j) % 7 - 3) for j in range(n)] for i in range(n)]
    rho = [[(rho[i][j] + rho[j][i]) / 2 for j in range(n)] for i in range(n)]
    tr = sum(rho[i][i] for i in range(n))

    def weight(r):
        return sum(rho[i][j] * r[i] * r[j] for i in range(n) for j in range(n)) / dot(r, r)

    # an orthogonal frame of Q^6 that is not a coordinate frame: reflect the coordinate frame in a vector
    u = (1, 2, 0, -1, 3, 1)
    frame = []
    for i in range(n):
        x = [F(0)] * n
        x[i] = F(1)
        frame.append(reflect(u, x, n))
    ok = ok and all(dot(frame[a], frame[b]) == (1 if a == b else 0) for a in range(n) for b in range(n))
    ok = ok and sum(weight(x) for x in frame) == tr
    # rescaling a ray does not change its weight
    ok = ok and weight([3 * c for c in frame[0]]) == weight(frame[0])
    # the values on e_i and e_i + e_j recover rho
    for i, j in combinations(range(n), 2):
        ei = [F(int(k == i)) for k in range(n)]
        ej = [F(int(k == j)) for k in range(n)]
        s = [a + b for a, b in zip(ei, ej)]
        ok = ok and (weight(s) * 2 - weight(ei) - weight(ej)) / 2 == rho[i][j]
    GA.check("a linear weight on Q^6 sums to the trace on a reflected frame and is recovered from 21 values", ok)
    return ok


def check_one_mode_admits_a_non_negative_additive_weight_that_is_not_linear():
    ok = True

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def weight(a, b):
        g = gcd(a, b)
        a, b = a // g, b // g
        if a % 2 and b % 2:
            return F(1, 2)
        return F(1) if a % 2 else F(0)

    # every frame {(a, b), (-b, a)} of Q^2 has total weight 1
    count = 0
    for a in range(-9, 10):
        for b in range(-9, 10):
            if (a, b) == (0, 0):
                continue
            ok = ok and weight(a, b) + weight(-b, a) == 1 and weight(a, b) == weight(-a, -b)
            count += 1
    ok = ok and count == 360
    # the only symmetric form with the values at (1,0), (0,1), (1,1) is diag(1, 0); it gives 1/5 at (1, 2)
    rho12 = (2 * weight(1, 1) - weight(1, 0) - weight(0, 1)) / 2
    ok = ok and rho12 == 0
    ok = ok and (weight(1, 0) * 1 + 2 * rho12 * 2 + weight(0, 1) * 4) / 5 == F(1, 5) and weight(1, 2) == 1
    GA.check("on the rays of Q^2 the parity weight sums to 1 on 360 frames and is not a quadratic form", ok)
    return ok
