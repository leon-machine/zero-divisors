"""transport.cohomological-form-no-go: exact checks.

Setting as in the torsor proposition (GA.py): V = R^{p,q} mixed, v = (e_0 + e_p)/2, w0 = (e_0 - e_p)/2,
U = span of the other generators of V, an extension V' adding generators of square +1, -1 or 0, and
R_u = 1 + v u. The class label of a pseudo-inverse is the Cl(U')-slot of its expansion in
{1, v, w0, v w0} x blades(U').
(1) Trivial coefficients: the translation part of R_u on classes does not depend on the class (linear
    part trivial), so coboundaries g -> g.b - b vanish; the cocycle theta(R_u) = u is additive
    (theta(R_u R_u') = u + u') and nonzero for every nonzero u in U, n >= 3.
(2) The vanishing locus: no pseudo-inverse is fixed by N_v. For every case (n = 3, 4, and extensions,
    degenerate included) the joint linear system {v s v = v, R_u s R_u^-1 = s for the sampled u} is
    inconsistent (rank of the augmented matrix exceeds the rank); adding further constraints (a Levi
    rotor) keeps it inconsistent. For n = 2 (Cl(1,1), U = 0, N_v trivial) the system v s v = v is
    consistent and w0 is a pseudo-inverse, in Cl(1,1) and in its extensions: the hyperbolic atom.
(3) Levi equivariance: rotors g of the even subalgebra of Cl(U) fix v, and g R_u g^-1 = R_{g u g^-1}, so
    theta(g R_u g^-1) = g theta(R_u) g^-1.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

CASES = [(1, 2, ()), (2, 1, ()), (2, 2, ()), (1, 3, ()), (3, 1, ()),
         (1, 2, (0,)), (2, 1, (1, -1)), (1, 3, (1,)), (2, 2, (-1,))]
ATOM = [(1, 1, ()), (1, 1, (1,)), (1, 1, (0, -1))]
U_COEFFS = [[1], [2, 1], [1, 1]]
ALPHA = [((), 2), ((0,), -1), ((0, 1), 3)]


def setup(p, q, extra):
    n = p + q
    sq = GA.sig(p, q) + tuple(extra)
    m = n + len(extra)
    v = GA.scal(F(1, 2), GA.add(GA.gen(0), GA.gen(p)))
    w0 = GA.scal(F(1, 2), GA.sub(GA.gen(0), GA.gen(p)))
    ugens = [i for i in range(n) if i not in (0, p)]
    uprime = [i for i in range(m) if i not in (0, p)]
    return sq, m, v, w0, ugens, uprime


def m3(x, y, z, sq):
    return GA.mul(GA.mul(x, y, sq), z, sq)


def co(x, blades):
    return [x.get(b, F(0)) for b in blades]


def us_of(ugens):
    return [GA.add(*[GA.scal(c, GA.gen(i)) for c, i in zip(uc, ugens) if c]) for uc in U_COEFFS if len(uc) <= len(ugens)]


def levi_rotor(ugens, sq):
    """A rational rotor in the plane of the first two generators of U (rotation or boost)."""
    B = GA.mul(GA.gen(ugens[0]), GA.gen(ugens[1]), sq)
    a, b = (F(3, 5), F(4, 5)) if GA.mul(B, B, sq)[()] == -1 else (F(5, 3), F(4, 3))
    return GA.add(GA.sc(a), GA.scal(b, B))


def lin(fn, blades):
    cols = [co(fn({b: F(1)}), blades) for b in blades]
    return [[cols[j][i] for j in range(len(blades))] for i in range(len(blades))]


def consistent(rows, rhs):
    return GA.field_rank(rows) == GA.field_rank([rows[i] + [rhs[i]] for i in range(len(rows))])


def cl_slot(x, sq, v, w0, uprime, blades):
    ub = [tuple(uprime[i] for i in b) for b in GA.all_blades(len(uprime))]
    h = [GA.sc(1), v, w0, GA.mul(v, w0, sq)]
    basis = [GA.mul(hh, {b: F(1)}, sq) for hh in h for b in ub]
    M = [[basis[j].get(b, F(0)) for j in range(len(basis))] for b in blades]
    c = GA.field_solve(M, co(x, blades))
    return {ub[i]: c[i] for i in range(len(ub)) if c[i]}


def elem(spec, uprime):
    out = {}
    for b, c in spec:
        if all(i < len(uprime) for i in b):
            out = GA.add(out, {tuple(uprime[i] for i in b): F(c)})
    return out


def check_trivial_coefficients_and_tautological_class():
    premise("transport.pseudo-inverse-torsor")
    premise("transport.group-null-rotations")
    ok = True
    for p, q, extra in CASES[:5]:
        sq, m, v, w0, ugens, uprime = setup(p, q, extra)
        blades = GA.all_blades(m)
        bases = [GA.add(w0, elem(ALPHA, uprime)), GA.add(w0, elem([((), -5)], uprime))]
        for u in us_of(ugens):
            R = GA.add(GA.sc(1), GA.mul(v, u, sq))
            Ri = GA.sub(GA.sc(1), GA.mul(v, u, sq))
            shifts = []
            for s in bases:
                shifts.append(GA.sub(cl_slot(m3(R, s, Ri, sq), sq, v, w0, uprime, blades),
                                     cl_slot(s, sq, v, w0, uprime, blades)))
            ok = ok and GA.eq(shifts[0], shifts[1]) and GA.eq(shifts[0], GA.neg(u)) and not GA.is_zero(u)
            for u2 in us_of(ugens):
                R2 = GA.add(GA.sc(1), GA.mul(v, u2, sq))
                R12 = GA.mul(R, R2, sq)
                R12i = GA.sub(GA.sc(1), GA.mul(v, GA.add(u, u2), sq))
                th = GA.sub(cl_slot(bases[0], sq, v, w0, uprime, blades),
                            cl_slot(m3(R12, bases[0], R12i, sq), sq, v, w0, uprime, blades))
                ok = ok and GA.eq(th, GA.add(u, u2))
    _tp_rv = (ok); assert _tp_rv is not False, "check_trivial_coefficients_and_tautological_class"; return _tp_rv


def check_class_vanishes_exactly_at_the_atom():
    premise("transport.pseudo-inverse-torsor")
    ok = True
    levi_cases = 0
    for p, q, extra in CASES:
        sq, m, v, w0, ugens, uprime = setup(p, q, extra)
        blades = GA.all_blades(m)
        zeros = [F(0)] * len(blades)
        rows = lin(lambda s: m3(v, s, v, sq), blades)
        rhs = co(v, blades)
        # pseudo-inverses exist (v s v = v alone is consistent): the inconsistency below comes from N_v
        ok = ok and consistent(rows, rhs)
        for u in us_of(ugens):
            R = GA.add(GA.sc(1), GA.mul(v, u, sq))
            Ri = GA.sub(GA.sc(1), GA.mul(v, u, sq))
            # R_u is in N_v: (v u)^2 = 0 gives R_u R_u^-1 = 1, and R_u fixes v
            ok = ok and GA.eq(GA.mul(R, Ri, sq), GA.sc(1)) and GA.eq(m3(R, v, Ri, sq), v)
            C = lin(lambda s: GA.sub(m3(R, s, Ri, sq), s), blades)
            ok = ok and consistent(C, zeros)          # each fixed-point condition alone is satisfiable
            rows = rows + C
            rhs = rhs + zeros
        ok = ok and not consistent(rows, rhs)
        if len(ugens) >= 2:
            levi_cases += 1
            g = levi_rotor(ugens, sq)
            gi = GA.reverse(g)
            C = lin(lambda s: GA.sub(m3(g, s, gi, sq), s), blades)
            ok = ok and GA.eq(GA.mul(g, gi, sq), GA.sc(1))
            ok = ok and not consistent(rows + C, rhs + zeros)
    # by hand: dim U = n - 2 >= 2 exactly for the five cases with n = 4
    ok = ok and levi_cases == 5
    for p, q, extra in ATOM:
        sq, m, v, w0, ugens, uprime = setup(p, q, extra)
        blades = GA.all_blades(m)
        ok = ok and ugens == [] and GA.eq(m3(v, w0, v, sq), v)
        ok = ok and consistent(lin(lambda s: m3(v, s, v, sq), blades), co(v, blades))
    _tp_rv = (ok); assert _tp_rv is not False, "check_class_vanishes_exactly_at_the_atom"; return _tp_rv


def check_levi_equivariance():
    premise("transport.group-null-rotations")
    ok = True
    count = 0
    for p, q, extra in CASES:
        sq, m, v, w0, ugens, uprime = setup(p, q, extra)
        if len(ugens) < 2:
            continue
        g = levi_rotor(ugens, sq)
        gi = GA.reverse(g)
        ok = ok and GA.eq(GA.mul(g, gi, sq), GA.sc(1))
        ok = ok and GA.eq(m3(g, v, gi, sq), v)
        for u in us_of(ugens):
            gu = m3(g, u, gi, sq)
            ok = ok and all(len(bl) == 1 and bl[0] in ugens for bl in gu)
            R = GA.add(GA.sc(1), GA.mul(v, u, sq))
            ok = ok and GA.eq(m3(g, R, gi, sq), GA.add(GA.sc(1), GA.mul(v, gu, sq)))
            count += 1
    ok = ok and count == 15
    _tp_rv = (ok); assert _tp_rv is not False, "check_levi_equivariance"; return _tp_rv
