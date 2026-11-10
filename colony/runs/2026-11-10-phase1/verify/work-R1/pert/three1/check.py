"""synthesis.three-party-trade-off-of-chsh-values-and-the-local-value-two: exact checks.

Modes of Cl_Q(3,3): e_k (square +1), f_k (square -1), p_k = f_k e_k; adjoint = linear extension of the blade
inverse. Party A: directions of mode 1 (e_1, p_1); party B: mode 2 twisted by p_1 (e_2 p_1, p_2); party D: mode 3
twisted by p_1 p_2 (e_3 p_1 p_2, p_3).

(1) Diagonals: for observables A1, A2 the sum and the difference anticommute, their squares add to 4, and
    C = (A1 + A2) B1 + (A1 - A2) B2; the two mixed products used in the proof anticommute.
(2) The trade-off w(C_AB)^2 + w(C_AD)^2 <= 8 on rational states and directions, with equality cases.
(3) Commuting directions: C^2 = 4 and the values on the minimal idempotents of the parity subalgebra are 2, -2.
(4) The stored pair state: the value 402/145 and the bound it leaves for a third party.
"""
from fractions import Fraction as F
from functools import reduce
from itertools import product

import GA
from tp_premise import premise

ONE = GA.sc(F(1))
M3 = 3
SQ = tuple(s for _ in range(M3) for s in (1, -1))
E = [GA.gen(2 * k) for k in range(M3)]
FF = [GA.gen(2 * k + 1) for k in range(M3)]


def mul(*xs):
    return reduce(lambda a, b: GA.mul(a, b, SQ), xs)


def dagger(x):
    r = GA.reverse(x)
    return {b: (c if sum(1 for i in b if i % 2 == 1) % 2 == 0 else -c) for b, c in r.items()}


def s0(x):
    return x.get((), F(0))


PAR = [mul(FF[k], E[k]) for k in range(M3)]
XA, ZA = E[0], PAR[0]
XB, ZB = mul(E[1], PAR[0]), PAR[1]
XD, ZD = mul(E[2], PAR[0], PAR[1]), PAR[2]
PTS = [(F(1), F(0)), (F(0), F(1)), (F(3, 5), F(4, 5)), (F(-5, 13), F(12, 13)), (F(20, 29), F(21, 29))]


def lin(c, x, s, y):
    return GA.add(GA.scal(F(c), x), GA.scal(F(s), y))


def direction(pt, X, Z):
    return lin(pt[0], X, pt[1], Z)


def chsh(A1, A2, B1, B2):
    return GA.add(mul(A1, GA.add(B1, B2)), mul(A2, GA.sub(B1, B2)))


def is_observable(x):
    return GA.eq(dagger(x), x) and GA.eq(mul(x, x), ONE)


def value(rho, x):
    return s0(mul(rho, x)) / s0(rho)


def anti(x, y):
    return GA.is_zero(GA.add(mul(x, y), mul(y, x)))


# ------------------------------------------------------------------ (1)
def check_sum_and_difference_of_two_observables_anticommute():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product")
    # the three parties commute pairwise (nested twists) and each party's two blades anticommute
    for (x, z) in ((XA, ZA), (XB, ZB), (XD, ZD)):
        assert is_observable(x) and is_observable(z) and anti(x, z)
    for u in (XA, ZA):
        for w in (XB, ZB, XD, ZD):
            assert GA.commutes(u, w, SQ)
    for u in (XB, ZB):
        for w in (XD, ZD):
            assert GA.commutes(u, w, SQ)
    # without the second twist factor mode 3 does not commute with party B
    assert GA.anticommutes(mul(E[2], PAR[0]), XB, SQ)
    pairs = [(direction(a, XA, ZA), direction(b, XA, ZA)) for a in PTS for b in PTS]
    count = 0
    for A1, A2 in pairs:
        assert is_observable(A1) and is_observable(A2)
        Ap, Am = GA.add(A1, A2), GA.sub(A1, A2)
        assert anti(Ap, Am)
        assert GA.eq(GA.add(mul(Ap, Ap), mul(Am, Am)), GA.scal(F(4), ONE))
        B1, B2, D2 = direction(PTS[2], XB, ZB), ZB, direction(PTS[3], XD, ZD)
        assert GA.eq(chsh(A1, A2, B1, B2), GA.add(mul(Ap, B1), mul(Am, B2)))
        U, V = mul(Ap, B1), mul(Am, D2)
        assert anti(U, V) and GA.eq(dagger(U), U) and GA.eq(dagger(V), V)
        lam, mu = F(2, 3), F(-7, 5)
        H = GA.add(GA.scal(lam, U), GA.scal(mu, V))
        assert GA.eq(mul(H, H), GA.add(GA.scal(lam * lam, mul(Ap, Ap)), GA.scal(mu * mu, mul(Am, Am))))
        count += 1
    assert count == 25


# ------------------------------------------------------------------ (2)
def sample_states():
    ys = [GA.add(ONE, E[0]),
          GA.add(GA.scal(F(2), ONE), mul(E[0], E[1]), GA.scal(F(-1, 3), FF[2])),
          GA.add(FF[1], GA.scal(F(5, 2), mul(E[0], FF[0], E[2])), ONE, mul(E[1], E[2])),
          GA.add(mul(XA, XB), mul(ZA, ZD), GA.scal(F(3), ONE), GA.scal(F(1, 2), mul(XA, XD)))]
    rhos = [mul(y, dagger(y)) for y in ys]
    # stabiliser states: A1 B1 = A1 D1 = 1 with a third generator
    ghz = mul(GA.add(ONE, mul(XA, XB)), GA.add(ONE, mul(XA, XD)), GA.add(ONE, mul(ZA, ZB, ZD)))
    rhos.append(ghz)
    # a pair state of A and B near the bound, times a state of mode 3
    IB = mul(XB, ZB)
    y = GA.add(ONE, GA.scal(F(-1, 2), IB))
    bell = mul(GA.add(ONE, mul(XA, XB)), GA.sub(ONE, mul(ZA, ZB)))
    rhos.append(mul(y, bell, dagger(y), GA.add(ONE, PAR[2])))
    rhos.append(GA.add(rhos[0], rhos[3]))
    return rhos, ghz


def check_two_chsh_values_sharing_a_party_have_squares_summing_to_at_most_eight():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("synthesis.division-gives-the-rationals")
    premise("synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product")
    rhos, ghz = sample_states()
    for rho in rhos:
        assert GA.eq(dagger(rho), rho) and s0(rho) > 0
    settings = list(product(PTS[:3], PTS[1:4], PTS[:2], PTS[2:4], PTS[1:3], PTS[3:]))
    assert len(settings) == 144
    worst, n = F(0), 0
    for a1, a2, b1, b2, d1, d2 in settings[::7]:
        A1, A2 = direction(a1, XA, ZA), direction(a2, XA, ZA)
        CAB = chsh(A1, A2, direction(b1, XB, ZB), direction(b2, XB, ZB))
        CAD = chsh(A1, A2, direction(d1, XD, ZD), direction(d2, XD, ZD))
        for rho in rhos:
            t = value(rho, CAB) ** 2 + value(rho, CAD) ** 2
            assert t <= F(8)
            worst = max(worst, t)
            n += 1
    assert n == 147 and worst == F(1296, 169)
    # equality: the stabiliser state with B1 = B2 and D1 = D2 gives (2, 2)
    CAB, CAD = chsh(XA, ZA, XB, XB), chsh(XA, ZA, XD, XD)
    assert (value(ghz, CAB), value(ghz, CAD)) == (F(2), F(2))
    assert value(ghz, CAB) ** 2 + value(ghz, CAD) ** 2 == F(8)
    # near the corner: the pair state at u = -1/2 has value 14/5 with B and leaves at most 4/25 for D
    near = rhos[5]
    CAB = chsh(XA, ZA, XB, ZB)
    assert value(near, CAB) == F(14, 5) and F(8) - F(14, 5) ** 2 == F(4, 25)
    for d1, d2 in product(PTS, repeat=2):
        CAD = chsh(XA, ZA, direction(d1, XD, ZD), direction(d2, XD, ZD))
        assert value(near, CAD) ** 2 <= F(0)


# ------------------------------------------------------------------ (3)
def check_commuting_directions_give_square_four_and_values_two():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    # one party's directions commute (equal or opposite): C^2 = 4 whatever the other party does
    for b1, b2 in product(PTS, repeat=2):
        for sgn in (F(1), F(-1)):
            Cc = chsh(ZA, GA.scal(sgn, ZA), direction(b1, XB, ZB), direction(b2, XB, ZB))
            assert GA.eq(mul(Cc, Cc), GA.scal(F(4), ONE))
    # the commutative subalgebra of the parities p_1, p_2: four minimal idempotents, C = 2 or -2 on each
    idem = [GA.scal(F(1, 4), mul(GA.add(ONE, GA.scal(F(s1), PAR[0])), GA.add(ONE, GA.scal(F(s2), PAR[1]))))
            for s1 in (1, -1) for s2 in (1, -1)]
    assert all(GA.eq(mul(q, q), q) for q in idem) and GA.eq(reduce(GA.add, idem), ONE)
    choices_a = [ONE, GA.neg(ONE), PAR[0], GA.neg(PAR[0])]
    choices_b = [ONE, GA.neg(ONE), PAR[1], GA.neg(PAR[1])]
    seen = set()
    for A1, A2 in product(choices_a, repeat=2):
        for B1, B2 in product(choices_b, repeat=2):
            Cc = chsh(A1, A2, B1, B2)
            assert GA.eq(mul(Cc, Cc), GA.scal(F(4), ONE))
            for q in idem:
                val = value(q, Cc)
                assert GA.eq(mul(Cc, q), GA.scal(val, q))
                seen.add(val)
    assert seen == {F(2), F(-2)}


# ------------------------------------------------------------------ (4)
def check_pair_state_value_and_what_it_leaves_a_third_party():
    premise("synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product")
    c, s = F(3, 5), F(4, 5)
    r = c * c - s * s
    v = [GA.scal(F(1, 2), GA.add(E[k], FF[k])) for k in range(M3)]
    w = [GA.scal(F(1, 2), GA.sub(E[k], FF[k])) for k in range(M3)]
    pair = GA.add(GA.scal(F(1, 4), mul(GA.add(ONE, mul(PAR[0], PAR[1])), GA.add(ONE, GA.scal(r, PAR[0])))),
                  GA.scal(c * s, GA.add(mul(w[0], w[1]), mul(v[1], v[0]))))
    assert GA.eq(mul(pair, pair), pair) and GA.eq(dagger(pair), pair)
    # correlations of the pair state: diag(2cs, 1) in the directions (e, p) of the two parties
    T = [[value(pair, mul(a, b)) for b in (XB, ZB)] for a in (XA, ZA)]
    assert T == [[F(24, 25), F(0)], [F(0), F(1)]]
    # each correlation is alpha + beta r + gamma cs; three weight pairs with independent (1, r, cs) fix the form
    rows = []
    for cc, ss in ((F(3, 5), F(4, 5)), (F(20, 29), F(21, 29)), (F(5, 13), F(12, 13))):
        st = GA.add(GA.scal(F(1, 4), mul(GA.add(ONE, mul(PAR[0], PAR[1])), GA.add(ONE, GA.scal(cc * cc - ss * ss, PAR[0])))),
                    GA.scal(cc * ss, GA.add(mul(w[0], w[1]), mul(v[1], v[0]))))
        assert [[value(st, mul(a, b)) for b in (XB, ZB)] for a in (XA, ZA)] == [[F(2) * cc * ss, F(0)], [F(0), F(1)]]
        rows.append([F(1), cc * cc - ss * ss, cc * ss])
    assert GA.mat_rank(rows) == 3
    x, z = F(20, 29), F(21, 29)
    S = value(pair, chsh(ZA, XA, lin(z, ZB, x, XB), lin(z, ZB, -x, XB)))
    assert S == F(2) * (z + F(24, 25) * x) == F(402, 145)
    # squared values: 4(1 + 4 c^2 s^2) = 4804/625 is not reached by this rational choice
    assert S * S < F(4) * (1 + 4 * c * c * s * s) == F(4804, 625)
    # with any state of mode 3 adjoined, a third party D is left with squared value at most 8 - S^2
    rho = mul(pair, GA.add(ONE, lin(F(3, 5), E[2], F(4, 5), PAR[2])))
    assert value(rho, chsh(ZA, XA, lin(z, ZB, x, XB), lin(z, ZB, -x, XB))) == S
    left = F(8) - S * S
    assert left == F(6596, 21025)
    best = F(0)
    for d1, d2 in product(PTS, repeat=2):
        for (P1, P2) in ((ZA, XA), (XA, ZA)):
            t = value(rho, chsh(P1, P2, direction(d1, XD, ZD), direction(d2, XD, ZD))) ** 2
            assert t <= left
            best = max(best, t)
    assert best <= F(4) * r * r + (F(4804, 625) - S * S) and F(4) * r * r == F(196, 625)
