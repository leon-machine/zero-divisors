"""synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state: exact checks.

Cl(l,l) of modes: e_k (square +1, index 2k), f_k (square -1, index 2k+1), p_k = f_k e_k. The dagger sends a blade
to its inverse. Twisted one-mode configuration A1 = p_1, A2 = e_1, B1 = p_2, B2 = e_2 p_1 (integer blades).

(1) the box functional <(1 + C) x>_0: value 4 on C, non-negative no-signalling probabilities at every setting
    pair, and negative on (C - t)(C - t)^dagger; positivity on C - t and 1 - K alone gives the bound 8;
(2) a configuration with C^2 = 8 on a block and A1 A2 + A2 A1 = 1 - p_3, not zero.
"""
from fractions import Fraction as F

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


def prod(sq, *xs):
    r = ONE
    for x in xs:
        r = GA.mul(r, x, sq)
    return r


def comm(x, y, sq):
    return GA.sub(GA.mul(x, y, sq), GA.mul(y, x, sq))


def acomm(x, y, sq):
    return GA.add(GA.mul(x, y, sq), GA.mul(y, x, sq))


def chsh(sq, a1, a2, b1, b2):
    return GA.add(prod(sq, a1, b1), prod(sq, a1, b2), prod(sq, a2, b1), GA.neg(prod(sq, a2, b2)))


def s0(x):
    return x.get((), F(0))


def modes(m):
    sq = tuple(s for _ in range(m) for s in (1, -1))
    e = [GA.gen(2 * k) for k in range(m)]
    f = [GA.gen(2 * k + 1) for k in range(m)]
    p = [GA.mul(f[k], e[k], sq) for k in range(m)]
    return sq, e, f, p


def is_obs(x, sq):
    return dagger(x, sq) == x and prod(sq, x, x) == ONE


def check_box_functional_has_value_four_and_fails_positivity_only_across_settings():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product")
    sq, e, f, p = modes(2)
    a = (p[0], e[0])
    b = (p[1], prod(sq, e[1], p[0]))
    for o in a + b:
        assert is_obs(o, sq) and all(c in (1, -1) for c in o.values())
    c = chsh(sq, a[0], a[1], b[0], b[1])
    assert len(c) == 4 and all(v in (1, -1) for v in c.values()) and () not in c
    m = GA.add(ONE, GA.scal(F(1, 2), c))
    lam = lambda x: s0(prod(sq, m, x))
    assert dagger(m, sq) == m and lam(ONE) == 1 and lam(c) == 4
    assert [lam(prod(sq, a[i], b[j])) for i in range(2) for j in range(2)] == [1, 1, 1, -1]
    assert [lam(o) for o in a + b] == [0, 0, 0, 0]
    # joint probabilities of the outcomes at each setting pair, and the marginals
    for i in range(2):
        for j in range(2):
            probs = {}
            for sa in (1, -1):
                for sb in (1, -1):
                    pa = GA.scal(F(1, 2), GA.add(ONE, GA.scal(sa, a[i])))
                    pb = GA.scal(F(1, 2), GA.add(ONE, GA.scal(sb, b[j])))
                    assert prod(sq, pa, pa) == pa and GA.commutes(pa, pb, sq)
                    probs[(sa, sb)] = lam(prod(sq, pa, pb))
            assert sorted(probs.values()) == [0, 0, F(1, 2), F(1, 2)]
            assert probs[(1, 1)] + probs[(1, -1)] == F(1, 2) == probs[(1, 1)] + probs[(-1, 1)]
    # positivity fails on the CHSH element shifted by a scalar
    k = GA.neg(prod(sq, a[0], a[1], b[0], b[1]))
    assert prod(sq, c, c) == GA.add(GA.sc(F(4)), GA.scal(F(4), k)) and lam(k) == 0
    vals = []
    for t in range(9):
        x = GA.sub(c, GA.sc(F(t)))
        vals.append(lam(prod(sq, x, dagger(x, sq))))
        assert vals[-1] == t * t - 8 * t + 4
    assert vals == [4, -3, -8, -11, -12, -11, -8, -3, 4]
    y = GA.sub(ONE, k)
    assert lam(prod(sq, y, dagger(y, sq))) == 2
    # the tracial state and a state with value above 2 satisfy both positivity conditions
    for r in (F(0), F(1, 3), F(239, 676)):
        rho = prod(sq, GA.add(ONE, k), GA.add(ONE, GA.scal(r, c)))
        phi = lambda z: s0(prod(sq, rho, z))
        assert phi(ONE) == 1 and phi(c) == 8 * r
        for t in (F(0), F(2), F(14, 5), F(4)):
            x = GA.sub(c, GA.sc(t))
            assert phi(prod(sq, x, x)) == 8 - 16 * r * t + t * t >= 0
        assert phi(prod(sq, y, y)) == 0
    return True


def check_square_eight_on_a_state_with_nonzero_anticommutator():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product")
    sq, e, f, p = modes(3)
    plus = GA.scal(F(1, 2), GA.add(ONE, p[2]))
    minus = GA.scal(F(1, 2), GA.sub(ONE, p[2]))
    a1 = p[0]
    a2 = GA.add(prod(sq, e[0], plus), prod(sq, p[0], minus))
    b1, b2 = p[1], prod(sq, e[1], p[0])
    for o in (a1, a2, b1, b2):
        assert is_obs(o, sq)
    for a in (a1, a2):
        for b in (b1, b2):
            assert GA.commutes(a, b, sq)
    assert acomm(a1, a2, sq) == GA.sub(ONE, p[2]) == GA.scal(F(2), minus)
    assert not GA.is_zero(acomm(a1, a2, sq)) and GA.anticommutes(b1, b2, sq)
    c = chsh(sq, a1, a2, b1, b2)
    k = GA.neg(prod(sq, p[0], e[0], b1, b2))
    c2 = prod(sq, c, c)
    assert c2 == GA.add(GA.sc(F(4)), GA.scal(F(4), prod(sq, k, plus)))
    proj = prod(sq, GA.add(ONE, k), GA.add(ONE, p[2]))
    assert prod(sq, proj, proj) == GA.scal(F(4), proj) and prod(sq, proj, c2) == GA.scal(F(8), proj)
    for r in (F(1, 3), F(239, 676)):
        rho = prod(sq, proj, GA.add(ONE, GA.scal(r, c)))
        phi = lambda z: s0(prod(sq, rho, z))
        assert dagger(rho, sq) == rho and phi(ONE) == 1 and phi(c2) == 8 and phi(c) == 8 * r
        ac = acomm(a1, a2, sq)
        assert phi(prod(sq, ac, ac)) == 0
    return True
