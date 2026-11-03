"""transport.group-null-rotations: exact checks of N_v = {R_u = 1 + v u : u in U}.

Setting, in each of the signatures (p,q) = (1,2), (2,1), (2,2), (1,3), (3,1), (2,3), (3,2), (1,4),
(4,1): generator 0 squares +1 and generator p squares -1; v = e_0 + e_p is null, w = (e_0 - e_p)/4 is
its hyperbolic partner (v w + w v = 1), and U = span of the remaining generators, the complement of
the hyperbolic plane. Sample vectors of U are fixed integer combinations (module level).

(1) R_u R_u' = R_{u+u'} for all ordered pairs of samples (so N_v is abelian), R_0 = 1 and
R_u R_{-u} = 1; injectivity: the products v e_k (e_k in U) are linearly independent, so u -> v u
and hence u -> R_u is injective on U; control: for u = v (orthogonal to v but outside U) R_v = 1.
(2) Each R_u is in Spin^0: it is even, R_u reverse(R_u) = 1, it maps every basis vector to a vector
under x -> R_u x R_u^-1, and t -> R_{tu} (t = 0, 1/3, 1/2, 1) is a path of such rotors from 1;
each R_u fixes v and shears w: R_u w R_u^-1 - w is nonzero.
(3) Levi equivariance: for g = a b (a, b non-null in U) and g = 1 + c e_i e_j (c = 1/2, 1/3), g is
invertible, even, fixes v, g u g^-1 lies in U with Q preserved, and g R_u g^-1 = R_{g u g^-1}.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = ((1, 2), (2, 1), (2, 2), (1, 3), (3, 1), (2, 3), (3, 2), (1, 4), (4, 1))
COEFFS = ((1, 0, 0), (0, 1, 0), (2, -1, 3), (-3, 5, 1), (1, 1, 1))


def setting(p, q):
    n = p + q
    sq = GA.sig(p, q)
    v = GA.add(GA.gen(0), GA.gen(p))
    w = GA.scal(F(1, 4), GA.sub(GA.gen(0), GA.gen(p)))
    ugens = [k for k in range(n) if k not in (0, p)]
    samples = []
    for c in COEFFS:
        u = GA.add(*[GA.scal(c[i], GA.gen(k)) for i, k in enumerate(ugens)])
        if u and u not in samples:
            samples.append(u)
    return n, sq, v, w, ugens, samples


def R(v, u, sq):
    return GA.add(GA.sc(1), GA.mul(v, u, sq))


def inv_versor(x, sq):
    """Inverse of an element with x reverse(x) a nonzero scalar."""
    r = GA.reverse(x)
    s = GA.mul(x, r, sq)
    assert set(s) <= {()} and s
    return GA.scal(1 / s[()], r)


def is_vector(x):
    return all(len(b) == 1 for b in x)


def check_group_law_and_injectivity():
    ok = True
    for p, q in SIGS:
        n, sq, v, w, ugens, samples = setting(p, q)
        ok = ok and GA.is_zero(GA.mul(v, v, sq)) and GA.is_zero(GA.mul(w, w, sq))
        ok = ok and GA.eq(GA.add(GA.mul(v, w, sq), GA.mul(w, v, sq)), GA.sc(1))
        ok = ok and len(ugens) == n - 2
        for u in samples:
            ok = ok and GA.dot(u, v, sq) == 0 and GA.dot(u, w, sq) == 0
            ok = ok and GA.eq(GA.mul(R(v, u, sq), R(v, GA.neg(u), sq), sq), GA.sc(1))
            for u2 in samples:
                lhs = GA.mul(R(v, u, sq), R(v, u2, sq), sq)
                ok = ok and GA.eq(lhs, R(v, GA.add(u, u2), sq))
                ok = ok and GA.eq(lhs, GA.mul(R(v, u2, sq), R(v, u, sq), sq))
        ok = ok and GA.eq(R(v, {}, sq), GA.sc(1))
        bl = GA.all_blades(n)
        prods = [GA.basis_vector_of(GA.mul(v, GA.gen(k), sq), bl) for k in ugens]
        ok = ok and GA.rank_of_vectors(prods) == n - 2
        ok = ok and GA.eq(R(v, v, sq), GA.sc(1))          # control: u = v is outside U
    GA.check("R_u R_u' = R_{u+u'}, abelian, R_{-u} inverse, u -> R_u injective on U, 9 signatures", ok)
    return ok


# Sample path parameters t for t -> R_{tu}; the path starts at t = 0.
T_PATH = (F(0), F(1, 3), F(1, 2), F(1))


def check_null_rotations_are_rotors_fixing_v():
    premise("transport.no-go-level-elements")
    ok = True
    for p, q in SIGS:
        n, sq, v, w, ugens, samples = setting(p, q)
        for u in samples:
            # the path starts at the identity
            ok = ok and GA.eq(R(v, GA.scal(T_PATH[0], u), sq), GA.sc(1))
            for t in T_PATH:
                Rt = R(v, GA.scal(t, u), sq)
                ok = ok and all(len(b) % 2 == 0 for b in Rt)
                ok = ok and GA.eq(GA.mul(Rt, GA.reverse(Rt), sq), GA.sc(1))
                Ri = GA.reverse(Rt)
                ok = ok and all(is_vector(GA.mul(GA.mul(Rt, GA.gen(k), sq), Ri, sq)) for k in range(n))
            Ru = R(v, u, sq)
            Ri = GA.reverse(Ru)
            ok = ok and GA.eq(GA.mul(GA.mul(Ru, v, sq), Ri, sq), v)
            shear = GA.sub(GA.mul(GA.mul(Ru, w, sq), Ri, sq), w)
            ok = ok and not GA.is_zero(shear) and is_vector(shear)
            # by hand, from v w + w v = 1, v^2 = 0 and u orthogonal to v, w: the shear is -u - Q(u) v
            Qu = GA.mul(u, u, sq).get((), F(0))
            ok = ok and GA.eq(shear, GA.sub(GA.neg(u), GA.scal(Qu, v)))
    GA.check("each R_u is an even rotor (R reverse(R) = 1) on a path from 1, fixes v, shears w", ok)
    return ok


def check_levi_equivariance():
    ok = True
    tested = 0
    for p, q in SIGS:
        n, sq, v, w, ugens, samples = setting(p, q)
        if len(ugens) < 2:
            continue
        i, j = ugens[0], ugens[1]
        a = GA.add(GA.scal(2, GA.gen(i)), GA.gen(j))
        b = GA.sub(GA.gen(i), GA.scal(3, GA.gen(ugens[-1])))
        gs = [GA.mul(a, b, sq),
              GA.add(GA.sc(1), GA.scal(F(1, 2), GA.mul(GA.gen(i), GA.gen(j), sq))),
              GA.add(GA.sc(1), GA.scal(F(1, 3), GA.mul(GA.gen(i), GA.gen(ugens[-1]), sq)))]
        for g in gs:
            if not g:
                continue
            gi = inv_versor(g, sq)
            ok = ok and GA.eq(GA.mul(g, gi, sq), GA.sc(1)) and all(len(bb) % 2 == 0 for bb in g)
            ok = ok and GA.eq(GA.mul(GA.mul(g, v, sq), gi, sq), v)
            for u in samples:
                gu = GA.mul(GA.mul(g, u, sq), gi, sq)
                ok = ok and is_vector(gu) and all(bb[0] in ugens for bb in gu)
                ok = ok and GA.dot(gu, gu, sq) == GA.dot(u, u, sq)
                lhs = GA.mul(GA.mul(g, R(v, u, sq), sq), gi, sq)
                ok = ok and GA.eq(lhs, R(v, gu, sq))
                tested += 1
    ok = ok and tested == 105
    GA.check("g R_u g^-1 = R_{g u g^-1} with g u g^-1 in U, Q preserved, g fixing v", ok)
    return ok
