"""synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state: exact checks.

Cl(l,l) of modes: e_k (square +1, index 2k), f_k (square -1, index 2k+1), p_k = f_k e_k. The dagger sends a blade
to its inverse. Twisted one-mode configuration A1 = p_1, A2 = e_1, B1 = p_2, B2 = e_2 p_1 (integer blades).

The box functional <(1 + C) x>_0: value 4 on C, non-negative no-signalling probabilities at every setting pair,
non-negative inside each setting pair, negative on (C - t)(C - t)^dagger and on (A1(B1+B2) - 2)^2, inertia
(12, 4, 0); positivity on C - t and 1 - K suffices for the bound 8.
"""
from fractions import Fraction as F
from itertools import combinations

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
    premise("tower.commuting-copies")
    premise("synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate")
    sq, e, f, p = modes(2)
    a = (p[0], e[0])
    b = (p[1], prod(sq, e[1], p[0]))
    for o in a + b:
        assert is_obs(o, sq) and all(c in (1, -1) for c in o.values())
    c = chsh(sq, a[0], a[1], b[0], b[1])
    assert len(c) == 4 and all(v in (1, -1) for v in c.values()) and () not in c
    m = GA.add(ONE, c)
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
    # an element using two setting pairs with a shared setting
    h = prod(sq, a[0], GA.add(b[0], b[1]))
    hm = GA.sub(h, GA.sc(F(2)))
    assert dagger(h, sq) == h and prod(sq, h, h) == GA.sc(F(2)) and lam(prod(sq, hm, dagger(hm, sq))) == -2
    # non-negative inside each setting pair: x = sum of x_ab E_ab
    for i in range(2):
        for j in range(2):
            x = GA.add(GA.sc(F(3)), GA.scal(F(-5), a[i]), GA.scal(F(2), b[j]), GA.scal(F(7), prod(sq, a[i], b[j])))
            assert lam(prod(sq, x, dagger(x, sq))) >= 0
    # inertia of the form lam(x y^dagger) on the sixteen blades
    blades = [bb for n in range(5) for bb in combinations(range(4), n)]
    gram = [[lam(prod(sq, {s: F(1)}, dagger({t: F(1)}, sq))) for t in blades] for s in blades]
    assert all(gram[i][j] == gram[j][i] for i in range(16) for j in range(16))
    assert GA.congruence_signature(gram) == (12, 4, 0)
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
