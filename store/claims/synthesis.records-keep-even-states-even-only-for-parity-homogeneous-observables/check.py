"""synthesis.records-keep-even-states-even-only-for-parity-homogeneous-observables: exact checks.

Cl(l,l) of modes: e_k (square +1, index 2k), f_k (square -1, index 2k+1), p_k = f_k e_k; the dagger sends a blade
to its inverse; alpha is the grade involution (conjugation by the total parity). Record map of an observable a:
E_a(x) = (x + a x a)/2.
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
    return clean({b: (c if len(b) % 2 == 0 else -c) for b, c in x.items()})


def even(x):
    return clean({b: c for b, c in x.items() if len(b) % 2 == 0})


def odd(x):
    return clean({b: c for b, c in x.items() if len(b) % 2 == 1})


def modes(m):
    sq = tuple(s for _ in range(m) for s in (1, -1))
    e = [GA.gen(2 * k) for k in range(m)]
    f = [GA.gen(2 * k + 1) for k in range(m)]
    p = [prod(sq, f[k], e[k]) for k in range(m)]
    blades = [ONE] + [{tuple(c): F(1)} for r in range(1, 2 * m + 1) for c in combinations(range(2 * m), r)]
    return sq, e, f, p, blades


def is_obs(x, sq):
    return clean(dagger(x, sq)) == clean(x) and prod(sq, x, x) == ONE


def rec(sq, a, x):
    return lin((F(1, 2), x), (F(1, 2), prod(sq, a, x, a)))


def chsh(sq, a1, a2, b1, b2):
    return lin((1, prod(sq, a1, b1)), (1, prod(sq, a1, b2)), (1, prod(sq, a2, b1)), (-1, prod(sq, a2, b2)))


def check_record_map_commutes_with_parity_exactly_for_homogeneous_observables():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("singularity.descent-parity-average")
    premise("synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate")
    sq, e, f, p, blades = modes(2)
    gam = prod(sq, p[0], p[1])
    assert is_obs(gam, sq) and all(prod(sq, gam, b, gam) == par(b) for b in blades)
    # centre of the even subalgebra: blades commuting with every bivector blade
    biv = [b for b in blades if len(next(iter(b))) == 2]
    central = [next(iter(b)) for b in blades if all(GA.commutes(b, w, sq) for w in biv)]
    assert central == [(), (0, 1, 2, 3)]
    x1, z1, x2, z2 = e[0], p[0], prod(sq, e[1], p[0]), p[1]
    hom = [x1, z1, x2, z2, prod(sq, x1, x2), prod(sq, z1, z2), prod(sq, e[0], f[1]), prod(sq, f[0], e[1])]
    blk = lin((F(1, 2), prod(sq, lin((1, ONE), (1, p[1])), p[0])), (F(1, 2), prod(sq, lin((1, ONE), (-1, p[1])), e[0])))
    mix = [lin((F(3, 5), x1), (F(4, 5), z1)), lin((F(3, 5), x2), (F(4, 5), z2)), lin((F(5, 13), x1), (F(-12, 13), z1)), blk]
    sa_even = [b for b in blades if len(next(iter(b))) % 2 == 0 and clean(dagger(b, sq)) == b and b != ONE]
    states = [ONE] + [lin((1, ONE), (s, b)) for b in sa_even for s in (1, -1)]
    for rho in states:
        assert rho == ONE or rho == lin((F(1, 2), prod(sq, rho, rho)))  # 1 + s = (1 + s)^2 / 2
    odd_sa = [b for b in blades if len(next(iter(b))) % 2 == 1 and clean(dagger(b, sq)) == b]
    for a in hom + mix:
        assert is_obs(a, sq)
        # positivity and the two sectors
        pp, pm = lin((F(1, 2), ONE), (F(1, 2), a)), lin((F(1, 2), ONE), (F(-1, 2), a))
        for b in blades[:8]:
            assert rec(sq, a, b) == lin((1, prod(sq, pp, b, pp)), (1, prod(sq, pm, b, pm)))
        homog = par(a) == a or par(a) == GA.neg(a)
        commute = all(par(rec(sq, a, b)) == rec(sq, a, par(b)) for b in blades)
        keeps = all(s0(prod(sq, rho, rec(sq, a, y))) == 0 for rho in states for y in odd_sa)
        assert homog == commute == keeps
        assert homog == (a in hom)
    # one witness spelled out: the even state <(1 + p1)(1 + p2) x>_0 after a record of (3/5) X1 + (4/5) Z1
    rho = prod(sq, lin((1, ONE), (1, p[0])), lin((1, ONE), (1, p[1])))
    assert par(rho) == rho and s0(prod(sq, rho, rec(sq, mix[0], e[0]))) == F(12, 25)
    return True


def check_one_mode_per_party_at_homogeneous_settings_even_states_give_at_most_two():
    premise("tower.commuting-copies")
    premise("synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects")
    premise("synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate")
    sq, e, f, p, blades = modes(2)
    x1, z1, x2, z2 = e[0], p[0], prod(sq, e[1], p[0]), p[1]
    u, v = prod(sq, x1, x2), prod(sq, z1, z2)
    # self-adjoint blades of the two party algebras
    sa1 = [b for b in blades if set(next(iter(b))) <= {0, 1} and clean(dagger(b, sq)) == b]
    assert [next(iter(b)) for b in sa1] == [(), (0,), (0, 1)]
    setsa = [GA.scal(F(s), o) for o in (x1, z1) for s in (1, -1)]
    setsb = [GA.scal(F(s), o) for o in (x2, z2) for s in (1, -1)]
    worst = F(0)
    for a1, a2, b1, b2 in product(setsa, setsa, setsb, setsb):
        ec = even(chsh(sq, a1, a2, b1, b2))
        assert set(ec) <= {next(iter(u)), next(iter(v))}
        tot = sum(abs(c) for c in ec.values())
        assert tot <= 2
        worst = max(worst, tot)
    assert worst == 2
    for su, sv in product((1, -1), repeat=2):
        lhs = lin((2, ONE), (-su, u), (-sv, v))
        rhs = lin((F(1, 2), prod(sq, lin((1, ONE), (-su, u)), lin((1, ONE), (-su, u)))),
                  (F(1, 2), prod(sq, lin((1, ONE), (-sv, v)), lin((1, ONE), (-sv, v)))))
        assert lhs == rhs
    # contrast: a mixed setting of party 2, an even state, value 14/5, and the record that breaks evenness
    b1 = lin((F(3, 5), x2), (F(4, 5), z2))
    b2 = lin((F(4, 5), x2), (F(-3, 5), z2))
    assert is_obs(b1, sq) and is_obs(b2, sq)
    c = chsh(sq, x1, z1, b1, b2)
    rho = prod(sq, lin((1, ONE), (1, u)), lin((1, ONE), (1, v)))
    assert par(rho) == rho and rho == clean(GA.scal(F(1, 4), prod(sq, rho, rho))) and s0(rho) == 1
    assert s0(prod(sq, rho, c)) == F(14, 5)
    assert u == prod(sq, e[1], f[0])  # the element u of the cited clause
    y = prod(sq, x1, z2)
    assert odd(y) == y and s0(prod(sq, rho, y)) == 0
    assert s0(prod(sq, rho, rec(sq, b1, y))) == F(12, 25)
    return True


def check_two_modes_per_party_odd_homogeneous_observables_exceed_two_on_an_even_state():
    premise("tower.commuting-copies")
    premise("synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate")
    sq, e, f, p, blades = modes(4)
    g = prod(sq, p[0], p[1])
    a = (e[0], e[1])
    b = (prod(sq, e[2], g), prod(sq, e[3], g))
    for o in a + b:
        assert is_obs(o, sq) and par(o) == GA.neg(o) and len(o) == 1
    assert all(GA.commutes(x, y, sq) for x in a for y in b)
    assert GA.anticommutes(a[0], a[1], sq) and GA.anticommutes(b[0], b[1], sq)
    c = chsh(sq, *a, *b)
    k = GA.neg(prod(sq, a[0], a[1], b[0], b[1]))
    assert par(c) == c and par(k) == k and is_obs(k, sq)
    assert prod(sq, c, c) == lin((4, ONE), (4, k)) and prod(sq, k, c) == c
    r = F(1, 3)
    rho = prod(sq, lin((1, ONE), (1, k)), lin((1, ONE), (r, c)))
    assert par(rho) == rho and s0(rho) == 1 and s0(prod(sq, rho, c)) == F(8, 3) and 8 * r * r <= 1
    # rho is a positive multiple of the square of a self-adjoint element, so its functional satisfies (P)
    s, t = F(2, 3), F(1, 6)
    root = prod(sq, lin((1, ONE), (1, k)), lin((s, ONE), (t, c)))
    assert clean(dagger(root, sq)) == root
    assert prod(sq, root, root) == clean(GA.scal(F(4, 3), rho))
    # records of the four observables commute with the parity (all 256 blades)
    for o in a + b:
        assert all(par(rec(sq, o, y)) == rec(sq, o, par(y)) for y in blades)
    return True
