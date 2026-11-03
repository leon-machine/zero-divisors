"""primer.twisted-adjoint-action: exact checks.

(1) For versors g (products of one, two and three invertible vectors, rational, in Cl(1,3), Cl(2,1),
Cl(0,3) and Cl(2,2)), tau_g(x) = g x g^{-1} (g even) or g xhat g^{-1} (g odd) is multiplicative on
every pair of basis blades, and on vectors it equals the twisted adjoint ghat x g^{-1}, which is a
vector and preserves the quadratic form (Gram matrix of the images equals that of the basis).
(2) For an invertible vector u: Ad_u(x) = -u x u^{-1} = x - 2 (x.u / Q(u)) u, on every basis vector
and on sample vectors, with Ad_u(u) = -u and Ad_u fixing u^perp (a reflection).
(3) Kernel: in every nondegenerate signature with n <= 4 the solutions g of ghat x = x g for all
vectors x form the line R.1 (computed as a kernel); with the Pin normalisation g ghat~ = +-1 this
is {+1, -1}. In odd n the central omega is not in it (omega-hat e_i != e_i omega), which is why the
twist is used.
(4) Surjectivity onto O(p,q), sampled (Cartan-Dieudonne is cited, not checked): the rotation of
the Euclidean plane with cos = 3/5, sin = 4/5 and the boost of the (1,1) plane with cosh = 5/3,
sinh = 4/3 are Ad of the product of two reflections, u2 u1 with u1 = e0 and u2 = 2 e0 + e1.
"""
from fractions import Fraction as F
import GA

SIGS = [GA.sig(1, 3), GA.sig(2, 1), GA.sig(0, 3), GA.sig(2, 2)]
# sample reflection axes u (coefficients, truncated to the dimension n), used by check_vector_is_reflection
REFLECTION_AXES = ([1, 0, 0, 0], [2, 1, 0, 0], [1, -1, 1, 2], [0, 3, 1, 1])
# a sample non-basis vector x (truncated to n) on which Ad_u is compared with the reflection formula
SAMPLE_X = [3, -2, 1, 5]
# signature of the by-hand example u = 2 e0 + e1 in check_vector_is_reflection
EXAMPLE_SIG = GA.sig(1, 3)


def vec(cs):
    return {(i,): F(c) for i, c in enumerate(cs) if c != 0}


def inverse_versor(g, sq):
    """g^{-1} = reverse(g) / (g reverse(g)) for a versor (g reverse(g) is a nonzero scalar)."""
    nrm = GA.mul(g, GA.reverse(g), sq)
    assert list(nrm.keys()) == [()]
    return GA.scal(1 / nrm[()], GA.reverse(g))


def versors(sq):
    n = len(sq)
    cands = [vec([1 if j == i else 0 for j in range(n)]) for i in range(n)]
    cands += [vec([2, 1, 0, 0][:n]), vec([1, 0, 3, 0][:n]), vec([1, -1, 1, 2][:n])]
    us = [u for u in cands if GA.mul(u, u, sq).get((), F(0)) != 0]
    out = [(us[0], 1), (us[-1], 1), (GA.mul(us[-1], us[-2], sq), 0),
           (GA.mul(GA.mul(us[-1], us[-2], sq), us[0], sq), 1)]
    return out


def tau(g, par, ginv, x, sq):
    y = GA.grade_inv(x) if par else x
    return GA.mul(GA.mul(g, y, sq), ginv, sq)


def check_tau_is_automorphism_and_twisted_adjoint():
    ok = True
    count = 0
    for sq in SIGS:
        n = len(sq)
        bl = [{b: F(1)} for b in GA.all_blades(n)]
        for g, par in versors(sq):
            ginv = inverse_versor(g, sq)
            ok = ok and GA.eq(GA.mul(g, ginv, sq), GA.sc(1))
            for a in bl:
                for b in bl:
                    ok = ok and GA.eq(tau(g, par, ginv, GA.mul(a, b, sq), sq),
                                      GA.mul(tau(g, par, ginv, a, sq), tau(g, par, ginv, b, sq), sq))
                    count += 1
            imgs = []
            for i in range(n):
                x = GA.gen(i)
                adg = GA.mul(GA.mul(GA.grade_inv(g), x, sq), ginv, sq)
                ok = ok and GA.eq(tau(g, par, ginv, x, sq), adg)
                ok = ok and all(len(b) == 1 for b in adg)
                imgs.append(adg)
            gram = [[GA.dot(imgs[i], imgs[j], sq) for j in range(n)] for i in range(n)]
            ok = ok and all(gram[i][j] == (sq[i] if i == j else 0) for i in range(n) for j in range(n))
    ok = ok and count == 4 * (2 * 256 + 2 * 64)
    GA.check("tau_g is multiplicative on all blade pairs and equals the twisted adjoint isometry on vectors", ok)
    return ok


def check_vector_is_reflection():
    ok = True
    for sq in SIGS:
        n = len(sq)
        for cs in REFLECTION_AXES:
            u = vec(cs[:n])
            Q = GA.mul(u, u, sq).get(())
            if not Q:
                continue
            uinv = GA.scal(1 / Q, u)
            for x in [GA.gen(i) for i in range(n)] + [vec(SAMPLE_X[:n])]:
                lhs = GA.neg(GA.mul(GA.mul(u, x, sq), uinv, sq))
                rhs = GA.sub(x, GA.scal(2 * GA.dot(x, u, sq) / Q, u))
                ok = ok and GA.eq(lhs, rhs)
            # Ad_u(u) = -u; and a vector orthogonal to u is fixed
            ok = ok and GA.eq(GA.neg(GA.mul(GA.mul(u, u, sq), uinv, sq)), GA.neg(u))
            for i in range(n):
                y = GA.sub(GA.scal(Q, GA.gen(i)), GA.scal(GA.dot(GA.gen(i), u, sq), u))
                ok = ok and GA.dot(y, u, sq) == 0
                ok = ok and GA.eq(GA.neg(GA.mul(GA.mul(u, y, sq), uinv, sq)), y)
    # explicit value: in Cl(1,3), u = 2 e0 + e1 (Q = 3), Ad_u(e0) = e0 - (4/3) u = -(5/3) e0 - (4/3) e1
    sq = EXAMPLE_SIG
    u = vec([2, 1])
    val = GA.neg(GA.mul(GA.mul(u, GA.gen(0), sq), GA.scal(F(1, 3), u), sq))
    ok = ok and GA.eq(val, vec([F(-5, 3), F(-4, 3)]))
    GA.check("Ad_u = -u x u^{-1} = x - 2 (x.u/Q(u)) u, the reflection in u^perp", ok)
    return ok


def check_kernel_is_plus_minus_one():
    ok = True
    for n in range(1, 5):
        for p in range(n + 1):
            sq = GA.sig(p, n - p)
            bl = GA.all_blades(n)
            # linear map g -> (ghat e_i - e_i g)_i on the 2^n coefficients of g
            cols = []
            for b in bl:
                g = {b: F(1)}
                col = []
                for i in range(n):
                    d = GA.sub(GA.mul(GA.grade_inv(g), GA.gen(i), sq), GA.mul(GA.gen(i), g, sq))
                    col.extend(d.get(c, F(0)) for c in bl)
                cols.append(col)
            rows = [list(r) for r in zip(*cols)]
            ker = GA.field_kernel(rows)
            ok = ok and len(ker) == 1 and all(ker[0][j] == 0 for j in range(1, 2 ** n)) and ker[0][0] != 0
            if n % 2 == 1:
                om = {tuple(range(n)): F(1)}
                ok = ok and GA.commutes(om, GA.gen(0), sq)
                ok = ok and not GA.eq(GA.mul(GA.grade_inv(om), GA.gen(0), sq), GA.mul(GA.gen(0), om, sq))
    # Pin normalisation on the kernel line: lambda^2 = 1 has exactly the roots +-1 among rationals
    roots = [F(a, b) for a in range(-3, 4) for b in range(1, 4) if F(a, b) ** 2 == 1]
    ok = ok and sorted(set(roots)) == [F(-1), F(1)]
    GA.check("the kernel of g -> Ad_g is R.1 (hence {+-1} in Pin) for every signature n <= 4", ok)
    return ok


def apply_matrix(g, sq):
    ginv = inverse_versor(g, sq)
    n = len(sq)
    return [[GA.mul(GA.mul(GA.grade_inv(g), GA.gen(j), sq), ginv, sq).get((i,), F(0))
             for j in range(n)] for i in range(n)]


def check_surjectivity_samples():
    ok = True
    # Euclidean plane: reflections in e0 then in 2 e0 + e1 give the rotation by 2 atan(1/2)
    sq = GA.sig(2, 0)
    g = GA.mul(vec([2, 1]), vec([1, 0]), sq)
    ok = ok and apply_matrix(g, sq) == [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
    # (1,1) plane: the same pair gives the boost with cosh 5/3, sinh 4/3
    sq = GA.sig(1, 1)
    g = GA.mul(vec([2, 1]), vec([1, 0]), sq)
    ok = ok and apply_matrix(g, sq) == [[F(5, 3), F(4, 3)], [F(4, 3), F(5, 3)]]
    # and a single reflection has determinant -1, the product of two determinant +1
    sq = GA.sig(1, 1)
    M1 = apply_matrix(vec([2, 1]), sq)
    ok = ok and M1[0][0] * M1[1][1] - M1[0][1] * M1[1][0] == -1
    GA.check("sampled rotation and boost are twisted adjoints of two-reflection versors", ok)
    return ok
