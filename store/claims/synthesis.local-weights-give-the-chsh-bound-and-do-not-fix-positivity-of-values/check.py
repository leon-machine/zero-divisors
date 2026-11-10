"""synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values: exact checks.

Cl(2,2) of two modes: e_k (square +1, index 2k), f_k (square -1, index 2k+1), p_k = f_k e_k; the dagger sends a
blade to its inverse. X1 = e_1, Z1 = p_1, X2 = e_2 p_1, Z2 = p_2; U = X1 X2, V = Z1 Z2, K = e_1 f_2 = -U V.
Functionals lam_c(x) = <(1 - U - V + c K) x>_0 and the box <(1 + C) x>_0.
"""
from fractions import Fraction as F
from itertools import combinations, product

import GA
from tp_premise import premise

ONE = GA.sc(F(1))


def dsign(b, sq):
    g = len(b)
    s = (-1) ** (g * (g - 1) // 2)
    for i in b:
        s *= sq[i]
    return s


def dagger(x, sq):
    return {b: c * dsign(b, sq) for b, c in x.items()}


def clean(x):
    return {b: c for b, c in x.items() if c != 0}


def prod(sq, *xs):
    r = ONE
    for x in xs:
        r = GA.mul(r, x, sq)
    return clean(r)


def lin(*terms):
    r = {}
    for c, x in terms:
        r = GA.add(r, GA.scal(F(c), x))
    return clean(r)


def s0(x):
    return x.get((), F(0))


def par(x):
    return {b: (c if len(b) % 2 == 0 else -c) for b, c in x.items()}


def setup():
    sq = (1, -1, 1, -1)
    e = [GA.gen(0), GA.gen(2)]
    f = [GA.gen(1), GA.gen(3)]
    p = [prod(sq, f[k], e[k]) for k in range(2)]
    x1, z1, x2, z2 = e[0], p[0], prod(sq, e[1], p[0]), p[1]
    u, v, k = prod(sq, x1, x2), prod(sq, z1, z2), prod(sq, e[0], f[1])
    blades = [ONE] + [{tuple(c): F(1)} for r in range(1, 5) for c in combinations(range(4), r)]
    return sq, p, x1, z1, x2, z2, u, v, k, blades


def chsh(sq, a1, a2, b1, b2):
    return lin((1, prod(sq, a1, b1)), (1, prod(sq, a1, b2)), (1, prod(sq, a2, b1)), (-1, prod(sq, a2, b2)))


def unit(s):
    """Rational point of the unit circle with parameter s."""
    s = F(s)
    return ((1 - s * s) / (1 + s * s), 2 * s / (1 + s * s))


PARAMS = [F(0), F(1), F(-1), F(1, 2), F(-1, 2), F(2), F(-3), F(1, 3), F(2, 3), F(-5, 4)]


def is_obs(x, sq):
    return clean(dagger(x, sq)) == clean(x) and prod(sq, x, x) == ONE


def check_local_weights_bound_values_and_the_box_fails_them():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("tower.commuting-copies")
    premise("synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate")
    premise("synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state")
    sq, p, x1, z1, x2, z2, u, v, k, blades = setup()
    dirs = [unit(s) for s in PARAMS] + [(-c, -d) for c, d in (unit(s) for s in PARAMS)]
    da = [lin((c, x1), (d, z1)) for c, d in dirs]
    db = [lin((c, x2), (d, z2)) for c, d in dirs]
    assert all(is_obs(a, sq) for a in da + db)
    assert all(GA.commutes(a, b, sq) for a in (x1, z1) for b in (x2, z2))
    half = F(1, 2)
    w = lambda a, b: prod(sq, lin((half, ONE), (half, a)), lin((half, ONE), (half, b)))
    # a weight element is y y^dagger with y itself, and the two sums of opposite weights
    for a, b in ((da[3], db[7]), (x1, z2), (da[9], db[2])):
        y = w(a, b)
        assert prod(sq, y, dagger(y, sq)) == y
        na, nb = GA.neg(a), GA.neg(b)
        assert lin((1, w(a, b)), (1, w(na, nb))) == lin((half, ONE), (half, prod(sq, a, b)))
        assert lin((1, w(a, nb)), (1, w(na, b))) == lin((half, ONE), (-half, prod(sq, a, b)))
    # the box: value 4, matrix T with a unit pair of value 7/5, weight -1/10
    c = chsh(sq, x1, z1, x2, z2)
    box = lambda x: s0(prod(sq, lin((1, ONE), (1, c)), x))
    assert box(ONE) == 1 and box(c) == 4
    assert [box(prod(sq, a, b)) for a in (x1, z1) for b in (x2, z2)] == [1, 1, 1, -1]
    bb = lin((F(3, 5), x2), (F(4, 5), z2))
    assert is_obs(bb, sq) and box(prod(sq, x1, bb)) == F(7, 5)
    assert box(w(x1, GA.neg(bb))) == F(-1, 10) and box(w(GA.neg(x1), bb)) == F(-1, 10)
    assert box(w(x1, bb)) == F(6, 10)
    # lam_c: weights (1 - xi.eta)/4 >= 0 and CHSH values of square below 8, the same for every c
    for cc in (F(-1), F(0), F(1), F(3)):
        m = lin((1, ONE), (-1, u), (-1, v), (cc, k))
        lam = lambda x: s0(prod(sq, m, x))
        assert lam(ONE) == 1
        for (i, a), (j, b) in product(enumerate(da), enumerate(db)):
            wt = lam(w(a, b))
            assert wt == (1 - dirs[i][0] * dirs[j][0] - dirs[i][1] * dirs[j][1]) / 4 and wt >= 0
        best = F(0)
        for i1, i2, j1, j2 in product(range(0, 20, 3), repeat=4):
            val = lam(chsh(sq, da[i1], da[i2], db[j1], db[j2]))
            assert val * val < 8
            best = max(best, val)
        assert best == F(14, 5)
    return True


def check_local_values_do_not_fix_positivity():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional")
    premise("tower.commuting-copies")
    sq, p, x1, z1, x2, z2, u, v, k, blades = setup()
    assert is_obs(u, sq) and is_obs(v, sq) and is_obs(k, sq) and GA.commutes(u, v, sq)
    assert prod(sq, u, v) == GA.neg(k)
    y1, y2 = prod(sq, x1, z1), prod(sq, x2, z2)
    assert k == GA.neg(prod(sq, y1, y2)) and y1 == GA.neg(GA.gen(1)) and y2 == GA.neg(prod(sq, GA.gen(3), p[0]))
    assert clean(dagger(y1, sq)) == GA.neg(y1) and clean(dagger(y2, sq)) == GA.neg(y2)
    loc = [prod(sq, a, b) for a in (ONE, x1, z1) for b in (ONE, x2, z2)]
    keys = set()
    for y in loc:
        assert len(y) == 1
        keys.add(next(iter(y)))
    assert len(keys) == 9 and next(iter(k)) not in keys
    ps = lin((F(1, 4), ONE), (F(-1, 4), u), (F(-1, 4), v), (F(1, 4), prod(sq, u, v)))
    assert prod(sq, ps, ps) == ps and clean(dagger(ps, sq)) == ps and s0(ps) == F(1, 4)
    assert all(prod(sq, ps, b, ps) == clean(GA.scal(4 * s0(prod(sq, ps, b)), ps)) for b in blades)
    quarter = F(1, 4)
    tab = lambda lam, su, sv: lam(prod(sq, lin((F(1, 2), ONE), (F(su, 2), u)), lin((F(1, 2), ONE), (F(sv, 2), v))))
    ref = None
    for cc in (F(-1), F(0), F(1), F(3), F(-2)):
        m = lin((1, ONE), (-1, u), (-1, v), (cc, k))
        lam = lambda x: s0(prod(sq, m, x))
        vals = [lam(y) for y in loc]
        ref = vals if ref is None else ref
        assert vals == ref == [1, 0, 0, 0, -1, 0, 0, 0, -1]
        assert all(lam(dagger(b, sq)) == lam(b) and lam(par(b)) == lam(b) for b in blades)
        assert lam(k) == cc and lam(ps) == (3 - cc) / 4
        t = {(su, sv): tab(lam, su, sv) for su in (1, -1) for sv in (1, -1)}
        assert t[(1, 1)] == -(1 + cc) * quarter and t[(1, -1)] == (1 + cc) * quarter
        assert t[(-1, 1)] == (1 + cc) * quarter and t[(-1, -1)] == (3 - cc) * quarter
        assert (min(t.values()) >= 0) == (cc == -1)
        if cc == -1:
            assert m == clean(GA.scal(F(4), ps))
    return True


def check_descents_mode_wise_gives_positivity_total_parity_does_not():
    premise("singularity.descent-parity-average")
    premise("singularity.p-reduced-metric-level-reading-many")
    premise("synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects")
    premise("synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state")
    sq, p, x1, z1, x2, z2, u, v, k, blades = setup()
    gam = prod(sq, p[0], p[1])
    assert gam == v
    grp = [ONE, p[0], p[1], gam]
    pis = [prod(sq, lin((F(1, 2), ONE), (F(n1, 2), p[0])), lin((F(1, 2), ONE), (F(n2, 2), p[1])))
           for n1 in (1, -1) for n2 in (1, -1)]
    en = lambda x: clean(GA.scal(F(1, 4), GA.add(*[prod(sq, g, x, g) for g in grp])))
    for b in blades:
        assert en(b) == lin(*[(4 * s0(prod(sq, q, b)), q) for q in pis])
        assert en(b) == lin(*[(1, prod(sq, q, b, q)) for q in pis])
    c = chsh(sq, x1, z1, x2, z2)
    dens = [lin((1, ONE), (1, c))] + [lin((1, ONE), (-1, u), (-1, v), (cc, k)) for cc in (F(-1), F(0), F(1), F(3))]
    target = lin((1, ONE), (-1, v))
    for m in dens:
        assert en(m) == target
        assert [s0(prod(sq, m, q)) for q in pis] == [0, F(1, 2), F(1, 2), 0]
    assert target == lin((F(1, 2), prod(sq, lin((1, ONE), (-1, v)), lin((1, ONE), (-1, v)))))
    # total parity average: lam_c unchanged; the box becomes <(1 + U - V) x>_0, negative on y y^dagger
    ev = lambda x: clean(GA.scal(F(1, 2), GA.add(x, prod(sq, gam, x, gam))))
    for m in dens[1:]:
        assert ev(m) == m
    mb = ev(dens[0])
    assert mb == lin((1, ONE), (1, u), (-1, v))
    y = prod(sq, lin((F(1, 2), ONE), (F(-1, 2), u)), lin((F(1, 2), ONE), (F(1, 2), v)))
    assert prod(sq, y, dagger(y, sq)) == y and s0(prod(sq, mb, y)) == F(-1, 4)
    return True
