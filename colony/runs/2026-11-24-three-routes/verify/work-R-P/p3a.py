"""synthesis.local-records-give-the-chsh-bound-without-positivity-and-reversal-on-one-party-keeps-them: exact checks.

Cl(l,l) of l modes: e_k (square +1, index 2k), f_k (square -1, index 2k+1), p_k = f_k e_k; the dagger sends a blade
to its inverse.  Commuting copies of the two-by-two matrices, one per mode: X_j = e_j p_1 ... p_{j-1}, Z_j = p_j,
Y_j = X_j Z_j (the twisted generators of the commuting-copies result).  Party 1 holds the first m modes, party 2 the
rest.  The reversal on party 2 multiplies a monomial by -1 for each factor Y_j with j a mode of party 2.
Everything is Fraction arithmetic.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise


def setup(n):
    sq = tuple([1, -1] * n)
    one = GA.sc(F(1))

    def pr(*xs):
        r = one
        for x in xs:
            r = GA.mul(r, x, sq)
        return r
    e = [GA.gen(2 * k) for k in range(n)]
    f = [GA.gen(2 * k + 1) for k in range(n)]
    p = [pr(f[k], e[k]) for k in range(n)]
    xs, zs, ys = [], [], []
    for j in range(n):
        x = e[j]
        for i in range(j):
            x = pr(x, p[i])
        xs.append(x)
        zs.append(p[j])
        ys.append(pr(x, p[j]))
    return sq, one, pr, e, f, p, xs, zs, ys


def dag(x, sq):
    out = {}
    for b, c in x.items():
        g = len(b)
        s = (-1) ** (g * (g - 1) // 2)
        for i in b:
            s *= sq[i]
        out[b] = c * s
    return out


def s0(x):
    return x.get((), F(0))


def lin(*terms):
    r = {}
    for c, x in terms:
        r = GA.add(r, GA.scal(F(c), x))
    return r


def mono(word, one, pr, xs, zs, ys):
    r = one
    for j, w in enumerate(word):
        if w:
            r = pr(r, (xs, zs, ys)[w - 1][j])
    return r


def monomials(n, one, pr, xs, zs, ys):
    return {wd: mono(wd, one, pr, xs, zs, ys) for wd in product(range(4), repeat=n)}


def reversal(x, monos, second):
    out = {}
    for wd, m in monos.items():
        (b, c), = m.items()
        if b in x:
            out[b] = x[b] * (-1) ** sum(1 for j in second if wd[j] == 3)
    return out


def unit(s):
    s = F(s)
    return ((1 - s * s) / (1 + s * s), 2 * s / (1 + s * s))


CONFIGS = [(0, 1, 0, 1), (F(1, 2), 2, F(-1, 3), 3), (F(2, 3), F(-5, 4), 1, F(1, 7))]
TS = [0, 1, -1, F(3, 2), F(7, 5), F(-2, 3)]
VALUES = [F(14, 5), F(-2), F(4), F(17, 6), F(3)]
ALBE = (F(2, 3), F(-5, 7), F(1, 2))


def four_squares(pr, one, a0, a1, b0, b1, t):
    """the four elements s^2 F of the certificate, and the element C."""
    t = F(t)
    sm, df = GA.add(a0, a1), GA.sub(a0, a1)
    out = []
    for s_, b, sg in ((sm, b0, 1), (sm, b0, -1), (df, b1, 1), (df, b1, -1)):
        s = lin((1, s_), (-sg * t, one))
        proj = lin((F(1, 2), one), (F(sg, 2), b))
        out.append((s, proj, pr(s, s, proj)))
    return out, GA.add(pr(sm, b0), pr(df, b1))


def check_certificate_and_bound_from_values_of_one_party_given_the_other_partys_outcomes():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("tower.commuting-copies")
    sq, one, pr, e, f, p, xs, zs, ys = setup(2)
    # (i) the identity, at three configurations of directions and at five values of t; each term is y y^dagger
    for sa, sb, sc_, sd in CONFIGS:
        (x, z), (x2, z2), (x3, z3), (x4, z4) = unit(sa), unit(sb), unit(sc_), unit(sd)
        a0, a1 = lin((x, xs[0]), (z, zs[0])), lin((x2, xs[0]), (z2, zs[0]))
        b0, b1 = lin((x3, xs[1]), (z3, zs[1])), lin((x4, xs[1]), (z4, zs[1]))
        for t in TS:
            terms, c = four_squares(pr, one, a0, a1, b0, b1, t)
            total = GA.add(*[y for _, _, y in terms])
            assert GA.eq(total, lin((4 + 2 * F(t) ** 2, one), (-2 * F(t), c)))
            for s, proj, y in terms:
                yy = pr(s, proj)
                assert GA.eq(pr(yy, dag(yy, sq)), y)
                assert GA.eq(pr(proj, proj), proj) and GA.eq(dag(proj, sq), proj)
    # the same identity on four modes, two per party, with observables that neither commute nor anticommute
    sq4, one4, pr4, e4, f4, p4, x4s, z4s, y4s = setup(4)
    a0, a1 = pr4(x4s[0], x4s[1]), lin((F(3, 5), z4s[0]), (F(4, 5), pr4(x4s[0], x4s[1])))
    b0, b1 = lin((F(3, 5), pr4(x4s[2], x4s[3])), (F(4, 5), z4s[2])), z4s[3]
    for o in (a0, a1, b0, b1):
        assert GA.eq(pr4(o, o), one4) and GA.eq(dag(o, sq4), o)
    assert not GA.commutes(a0, a1, sq4) and not GA.anticommutes(a0, a1, sq4)
    for t in TS:
        terms, c = four_squares(pr4, one4, a0, a1, b0, b1, t)
        assert GA.eq(GA.add(*[y for _, _, y in terms]), lin((4 + 2 * F(t) ** 2, one4), (-2 * F(t), c)))
    # (ii) the bound: at t = v/2 the left side has value 4 - v^2/2, for any value v of C
    for v in VALUES:
        t = v / 2
        assert 4 + 2 * t * t - 2 * t * v == 4 - v * v / 2
        assert (v * v <= 8) == (4 + 2 * t * t - 2 * t * v >= 0)
    # the box functional <(1 + C_0) x>_0: value 4 on C_0, and each of the four squares has value -1/2 at t = 1
    a0, a1, b0, b1 = xs[0], zs[0], xs[1], zs[1]
    terms, c0 = four_squares(pr, one, a0, a1, b0, b1, 1)
    box = GA.add(one, c0)
    assert s0(pr(box, c0)) == 4
    assert [s0(pr(box, y)) for _, _, y in terms] == [F(-1, 2)] * 4
    # one mode per party: s^2 is a non-negative combination of the two outcome projectors of a direction
    al, be, (x, z) = ALBE[0], ALBE[1], unit(ALBE[2])
    d = lin((x, xs[0]), (z, zs[0]))
    s = lin((al, one), (be, d))
    assert GA.eq(pr(s, s), lin(((al + be) ** 2 / 2, GA.add(one, d)), ((al - be) ** 2 / 2, GA.sub(one, d))))


def check_weights_of_records_of_one_party_of_two_modes_give_the_bound():
    premise("synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear")
    premise("tower.commuting-copies")
    # three modes: party 1 holds modes 1, 2 (its algebra is that of two modes), party 2 holds mode 3
    sq, one, pr, e, f, p, xs, zs, ys = setup(3)
    a0 = zs[0]
    a1 = pr(xs[0], lin((F(3, 5), zs[1]), (F(4, 5), xs[1])))
    b0, b1 = lin((F(4, 5), zs[2]), (F(3, 5), xs[2])), lin((F(3, 5), zs[2]), (F(-4, 5), xs[2]))
    for o in (a0, a1, b0, b1):
        assert GA.eq(pr(o, o), one) and GA.eq(dag(o, sq), o)
    for a in (e[0], f[0], e[1], f[1]):
        assert GA.commutes(a, b0, sq) and GA.commutes(a, b1, sq)
    # a density that is not a state: the reversal on party 2 of a state of modes 1 and 3, times a state of mode 2
    dens = pr(lin((1, one), (-1, pr(xs[0], xs[2])), (-1, pr(zs[0], zs[2])), (-1, pr(ys[0], ys[2]))),
              lin((1, one), (F(3, 5), zs[1]), (F(4, 5), xs[1])))
    assert s0(dens) == 1
    bad = GA.scal(F(1, 4), pr(lin((1, one), (1, pr(xs[0], xs[2]))), lin((1, one), (1, pr(zs[0], zs[2])))))
    assert GA.eq(pr(bad, bad), bad) and GA.eq(dag(bad, sq), bad) and s0(pr(dens, bad)) == F(-1, 2)

    def mu(pa, pb):          # weight of the product of a projector of party 1 and an outcome of party 2
        return s0(pr(dens, pa, pb))

    def pj(o, sg):
        return lin((F(1, 2), one), (F(sg, 2), o))
    corr = {}
    for i, a in enumerate((a0, a1)):
        for j, b in enumerate((b0, b1)):
            w = {(sa, sb): mu(pj(a, sa), pj(b, sb)) for sa in (1, -1) for sb in (1, -1)}
            assert all(val >= 0 for val in w.values()) and sum(w.values()) == 1
            corr[(i, j)] = sum(sa * sb * val for (sa, sb), val in w.items())
    value = corr[(0, 0)] + corr[(0, 1)] + corr[(1, 0)] - corr[(1, 1)]
    assert value * value < 8 and value == F(-14, 5)
    # the conditional functionals of party 1 are non-negative on hermitian squares of its algebra (16 blades)
    blades1 = [{b: F(1)} for b in GA.all_blades(4)]
    for b in (b0, b1):
        for sg in (1, -1):
            gram = [[s0(pr(dens, u, dag(w_, sq), pj(b, sg))) for w_ in blades1] for u in blades1]
            assert GA.congruence_signature(gram)[1] == 0
    # the four values that the bound uses, written with the weights' linear extensions, sum to 4 + 2t^2 - 2t value
    for t in [1, F(7, 5), value / 2]:
        terms, c = four_squares(pr, one, a0, a1, b0, b1, t)
        vals = [s0(pr(dens, y)) for _, _, y in terms]
        assert all(val >= 0 for val in vals)
        assert sum(vals) == 4 + 2 * F(t) ** 2 - 2 * F(t) * value


def check_reversal_on_one_party_is_well_defined_and_fixes_products_of_local_observables():
    premise("tower.commuting-copies")
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    sq, one, pr, e, f, p, xs, zs, ys = setup(4)
    monos = monomials(4, one, pr, xs, zs, ys)
    # the 256 products (monomial of party 1)(monomial of party 2) are signed blades, each blade once
    assert all(len(m) == 1 and abs(list(m.values())[0]) == 1 for m in monos.values())
    assert len({list(m.keys())[0] for m in monos.values()}) == 256
    # party 2's algebra is generated by the generators twisted by party 1's parity, and commutes with party 1
    gam = pr(p[0], p[1])
    tw = [pr(gam, v) for v in (e[2], f[2], e[3], f[3])]
    for a in (e[0], f[0], e[1], f[1]):
        assert all(GA.commutes(a, b, sq) for b in tw)
    z2 = pr(tw[1], tw[0])
    assert GA.eq(xs[2], tw[0]) or GA.eq(xs[2], GA.neg(tw[0]))
    assert GA.eq(zs[2], z2) or GA.eq(zs[2], GA.neg(z2))
    assert GA.eq(xs[3], pr(tw[2], z2)) or GA.eq(xs[3], GA.neg(pr(tw[2], z2)))
    # the adjoint of a monomial is (-1)^(number of Y) times it; the reversal uses the Y of party 2 only
    for wd, m in monos.items():
        assert GA.eq(dag(m, sq), GA.scal((-1) ** sum(1 for w in wd if w == 3), m))
    second = [2, 3]
    sample = lin((F(2, 3), monos[(1, 3, 3, 0)]), (F(-1, 5), monos[(3, 0, 2, 3)]), (4, monos[(0, 2, 3, 3)]), (1, monos[(2, 2, 1, 0)]))
    rs = reversal(sample, monos, second)
    assert GA.eq(rs, lin((F(-2, 3), monos[(1, 3, 3, 0)]), (F(1, 5), monos[(3, 0, 2, 3)]), (4, monos[(0, 2, 3, 3)]), (1, monos[(2, 2, 1, 0)])))
    assert GA.eq(reversal(rs, monos, second), sample)
    assert GA.eq(reversal(dag(sample, sq), monos, second), dag(rs, sq))
    # products of self-adjoint monomials of the two parties (10 times 10) are fixed
    sa1 = [monos[(a, b, 0, 0)] for a in range(4) for b in range(4) if ((a == 3) + (b == 3)) % 2 == 0]
    sa2 = [monos[(0, 0, a, b)] for a in range(4) for b in range(4) if ((a == 3) + (b == 3)) % 2 == 0]
    assert len(sa1) == 10 and len(sa2) == 10
    assert all(GA.eq(reversal(pr(a, b), monos, second), pr(a, b)) for a in sa1 for b in sa2)
    # a product with an anti-self-adjoint factor of party 2 is negated; module property for party 1, and for a
    # self-adjoint element of party 2 acting on both sides
    y = pr(monos[(1, 0, 0, 0)], monos[(0, 0, 3, 1)])
    assert GA.eq(reversal(y, monos, second), GA.neg(y))
    a_l, a_r = lin((1, monos[(1, 3, 0, 0)]), (2, one)), monos[(2, 1, 0, 0)]
    assert GA.eq(reversal(pr(a_l, sample, a_r), monos, second), pr(a_l, rs, a_r))
    b_s = lin((F(3, 5), monos[(0, 0, 1, 1)]), (F(4, 5), monos[(0, 0, 2, 0)]))
    assert GA.eq(dag(b_s, sq), b_s)
    assert GA.eq(reversal(pr(b_s, sample, b_s), monos, second), pr(b_s, rs, b_s))


def check_reversal_of_the_two_mode_state_and_two_copies_select_the_end_points():
    premise("tower.commuting-copies")
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    sq, one, pr, e, f, p, xs, zs, ys = setup(2)
    u, v, k = pr(xs[0], xs[1]), pr(zs[0], zs[1]), pr(e[0], f[1])
    assert GA.eq(k, GA.neg(pr(ys[0], ys[1]))) and GA.eq(pr(u, v), GA.neg(k))
    monos = monomials(2, one, pr, xs, zs, ys)

    def dens(c):
        return lin((1, one), (-1, u), (-1, v), (c, k))
    for c in [F(-1), F(0), F(1), F(1, 2), F(3)]:
        assert GA.eq(reversal(dens(c), monos, [1]), dens(-c))
    w = [s0(pr(dens(1), GA.scal(F(1, 4), pr(lin((1, one), (su, u)), lin((1, one), (sv, v))))))
         for su, sv in ((1, 1), (1, -1), (-1, 1), (-1, -1))]
    assert w == [F(-1, 2), F(1, 2), F(1, 2), F(1, 2)]
    blades = [{b: F(1)} for b in GA.all_blades(4)]
    gram = [[s0(pr(dens(1), a, dag(b, sq))) for b in blades] for a in blades]
    assert GA.congruence_signature(gram) == (12, 4, 0)
    gram = [[s0(pr(dens(-1), a, dag(b, sq))) for b in blades] for a in blades]
    assert GA.congruence_signature(gram) == (4, 0, 12)
    # two copies: modes 1, 2 with party 1 and 3, 4 with party 2; copy one is the pair (1, 3), copy two (2, 4)
    sq4, one4, pr4, e4, f4, p4, x4, z4, y4 = setup(4)
    monos4 = monomials(4, one4, pr4, x4, z4, y4)

    def pair(a, b, c):
        return lin((1, one4), (-1, pr4(x4[a], x4[b])), (-1, pr4(z4[a], z4[b])), (-c, pr4(y4[a], y4[b])))

    def lam(c, w1, w2):
        return {(0, 0): F(1), (1, 1): F(-1), (2, 2): F(-1), (3, 3): -F(c)}.get((w1, w2), F(0))

    def bell(a, b, s, t):
        return GA.scal(F(1, 4), pr4(lin((1, one4), (s, pr4(x4[a], x4[b]))), lin((1, one4), (t, pr4(z4[a], z4[b])))))
    for c in [F(-1), F(1), F(1, 2), F(3)]:
        r = pr4(pair(0, 2, c), pair(1, 3, c))
        for wd in monos4:
            m02 = mono((wd[0], 0, wd[2], 0), one4, pr4, x4, z4, y4)
            m13 = mono((0, wd[1], 0, wd[3]), one4, pr4, x4, z4, y4)
            assert s0(pr4(r, m02, m13)) == lam(c, wd[0], wd[2]) * lam(c, wd[1], wd[3])
        for s, t, s2, t2 in product((1, -1), repeat=4):
            pa, pb = bell(0, 1, s, t), bell(2, 3, s2, t2)
            assert s0(pr4(r, pa, pb)) == F(1, 16) * (1 + s * s2 + t * t2 + s * s2 * t * t2 * c)
        assert GA.eq(reversal(r, monos4, [2, 3]), pr4(pair(0, 2, -c), pair(1, 3, -c)))
    pa, pb = bell(0, 1, 1, 1), bell(2, 3, -1, -1)
    assert GA.eq(pr4(pa, pb, pa, pb), pr4(pa, pb)) and GA.eq(dag(pr4(pa, pb), sq4), pr4(pa, pb))
    assert s0(pr4(pr4(pair(0, 2, F(1, 2)), pair(1, 3, F(1, 2))), pa, pb)) == F(-3, 64)
    assert s0(pr4(pr4(pair(0, 2, 3), pair(1, 3, 3)), bell(0, 1, 1, 1), bell(2, 3, 1, -1))) == F(-1, 2)
    rp, rm = pr4(pair(0, 2, 1), pair(1, 3, 1)), pr4(pair(0, 2, -1), pair(1, 3, -1))
    assert GA.eq(pr4(rm, rm), GA.scal(16, rm)) and GA.eq(dag(rm, sq4), rm)
    sa1 = [monos4[(a, b, 0, 0)] for a in range(4) for b in range(4) if ((a == 3) + (b == 3)) % 2 == 0]
    sa2 = [monos4[(0, 0, a, b)] for a in range(4) for b in range(4) if ((a == 3) + (b == 3)) % 2 == 0]
    assert all(s0(pr4(rp, a, b)) == s0(pr4(rm, a, b)) for a in sa1 for b in sa2)
    assert s0(pr4(rp, bell(0, 2, 1, 1))) == F(-1, 2)


def check_one_unitary_between_the_parties_exposes_the_reversed_functional():
    premise("synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear")
    premise("std-algebra.quaternions")
    sq, one, pr, e, f, p, xs, zs, ys = setup(2)
    u_, v_, k = pr(xs[0], xs[1]), pr(zs[0], zs[1]), pr(e[0], f[1])
    un = lin((F(1, 2), one), (F(1, 2), zs[1]), (F(1, 2), xs[0]), (F(-1, 2), pr(xs[0], zs[1])))
    assert GA.eq(pr(un, dag(un, sq)), one) and GA.eq(dag(un, sq), un)
    local = GA.scal(F(1, 4), pr(lin((1, one), (1, zs[0])), lin((1, one), (1, xs[1]))))
    joint = GA.scal(F(1, 4), pr(lin((1, one), (1, u_)), lin((1, one), (1, v_))))
    assert GA.eq(pr(un, local, dag(un, sq)), joint)
    rev = lin((1, one), (-1, u_), (-1, v_), (1, k))
    state = lin((1, one), (-1, u_), (-1, v_), (-1, k))
    assert s0(pr(rev, local)) == F(1, 4) and s0(pr(state, local)) == F(1, 4)
    assert s0(pr(rev, un, local, dag(un, sq))) == F(-1, 2) and s0(pr(state, un, local, dag(un, sq))) == 0
    # the two facts behind the orbit: a reflection carries a vector to any other of the same norm, and the norm of
    # rational rotors (quaternions) is multiplicative, which carries the vectors of square norm to any norm class
    for r, r2 in [((1, 0, 1, 0), (1, 0, 0, 1)), ((3, 4, 0, 0), (0, 0, 5, 0)), ((1, 2, 3, 4), (5, 2, 1, 0))]:
        assert sum(x * x for x in r) == sum(x * x for x in r2)
        d = [F(x - y) for x, y in zip(r, r2)]
        dd = sum(x * x for x in d)
        img = [F(x) - 2 * dj * sum(di * F(xi) for di, xi in zip(d, r)) / dd for x, dj in zip(r, d)]
        assert img == [F(x) for x in r2]
    sq3 = (1, 1, 1)
    b1, b2, b3 = {(1, 2): F(-1)}, {(0, 2): F(1)}, {(0, 1): F(-1)}

    def rot(c):
        return lin((c[0], GA.sc(F(1))), (c[1], b1), (c[2], b2), (c[3], b3))
    assert GA.eq(GA.mul(b1, b2, sq3), b3) and GA.eq(GA.mul(b1, b1, sq3), GA.sc(F(-1)))
    for q0, y in [((1, 0, 0, 1), (F(3, 5), F(4, 5), 0, 0)), ((2, 1, 1, 1), (F(1, 3), F(2, 3), F(2, 3), 0))]:
        prod_ = GA.mul(rot(q0), rot(y), sq3)
        nrm = sum(c * c for c in prod_.values())
        assert nrm == sum(x * x for x in q0) * sum(F(x) * F(x) for x in y)
        assert sum(F(x) * F(x) for x in y) == 1


def check_field_theory_unit_makes_the_separating_blade_a_product_of_local_observables():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    # spacetime generators (indices 0..3, squares +1, -1, -1, -1) and two modes (indices 4..7)
    sq = (1, -1, -1, -1, 1, -1, 1, -1)
    one = GA.sc(F(1))

    def pr(*xs):
        r = one
        for x in xs:
            r = GA.mul(r, x, sq)
        return r
    i4 = pr(GA.gen(0), GA.gen(1), GA.gen(2), GA.gen(3))
    e1, f1, e2, f2 = GA.gen(4), GA.gen(5), GA.gen(6), GA.gen(7)
    p1, p2 = pr(f1, e1), pr(f2, e2)
    x1, z1, x2, z2 = e1, p1, pr(e2, p1), p2
    y1, y2 = pr(x1, z1), pr(x2, z2)
    k = pr(e1, f2)
    assert GA.eq(pr(i4, i4), GA.sc(F(-1))) and GA.eq(dag(i4, sq), GA.neg(i4))
    assert all(GA.commutes(i4, g, sq) for g in (e1, f1, e2, f2))
    assert all(GA.anticommutes(i4, GA.gen(j), sq) for j in range(4))
    l1, l2 = pr(i4, y1), pr(i4, y2)
    for l in (l1, l2):
        assert GA.eq(dag(l, sq), l) and GA.eq(pr(l, l), one)
    assert GA.commutes(l1, l2, sq) and GA.eq(pr(l1, l2), k)
    assert GA.eq(dag(y1, sq), GA.neg(y1)) and GA.eq(dag(y2, sq), GA.neg(y2))
    assert all(GA.commutes(l1, g, sq) for g in (x2, z2)) and all(GA.commutes(l2, g, sq) for g in (x1, z1))
