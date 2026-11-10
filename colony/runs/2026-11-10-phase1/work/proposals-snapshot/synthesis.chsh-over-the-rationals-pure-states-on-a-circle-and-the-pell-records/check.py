"""synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records: exact checks.

Cl_Q(2,2): generators e_1, f_1, e_2, f_2 (squares +1, -1, +1, -1), parities p_k = f_k e_k, adjoint = linear
extension of the blade inverse. Settings A1 = e_1, A2 = p_1, B1 = e_2 p_1, B2 = p_2 (mode 1 and the Klein-twisted
mode 2); C the CHSH element, K = e_1 f_2, I = B1 B2, Cq = C I the quarter-turned CHSH element.

(1) Cq is the CHSH element of (A2, -A1, B1, B2); C and Cq anticommute and have the same square 4(1 + K); the
    corner of the sector K = 1 is spanned by four independent elements; sample states have values in the disc.
(2) The states rho_u = (1 + uI) rho_0 (1 + uI)^dagger / (1 + u^2): pure, in the sector, with values
    (2(c_u - s_u), -2(c_u + s_u)) on the circle X^2 + Y^2 = 8, equal to the values of rho_0 on directions turned by the
    rational rotor R_u; rho_u = (1 + K)/4 + (X C + Y Cq)/16; parity.
(3) The denominator law 8 Q^2 - P^2 >= 4 for all fractions with Q up to a bound, equality exactly on the Pell
    sequence, the recursion, the records and the rational bracket of the distance to the bound.
"""
from fractions import Fraction as F
from functools import reduce

import GA
from tp_premise import premise

ONE = GA.sc(F(1))
SQ = (1, -1, 1, -1)
E = [GA.gen(0), GA.gen(2)]
FF = [GA.gen(1), GA.gen(3)]
QMAX = 400


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def isqrt(n):
    r = 0
    while (r + 1) * (r + 1) <= n:
        r += 1
    return r


def mul(*xs):
    return reduce(lambda a, b: GA.mul(a, b, SQ), xs)


def dagger(x):
    r = GA.reverse(x)
    return {b: (c if sum(1 for i in b if i % 2 == 1) % 2 == 0 else -c) for b, c in r.items()}


def s0(x):
    return x.get((), F(0))


def chsh(A1, A2, B1, B2):
    return GA.add(mul(A1, GA.add(B1, B2)), mul(A2, GA.sub(B1, B2)))


PAR = [mul(FF[k], E[k]) for k in range(len(E))]
A1, A2, B1, B2 = E[0], PAR[0], mul(E[1], PAR[0]), PAR[1]
C = chsh(A1, A2, B1, B2)
K = mul(E[0], FF[1])
IB = mul(B1, B2)
CQ = mul(C, IB)
PK = GA.scal(F(1, 2), GA.add(ONE, K))
RHO0 = GA.scal(F(1, 4), mul(GA.add(ONE, mul(A1, B1)), GA.sub(ONE, mul(A2, B2))))
BLADES = [{b: F(1)} for b in GA.all_blades(len(SQ))]
GAMMA = mul(PAR[0], PAR[1])


def value(rho, x):
    return s0(mul(rho, x)) / s0(rho)


def rho_of(u):
    y = GA.add(ONE, GA.scal(F(u), IB))
    return GA.scal(1 / (1 + F(u) * F(u)), mul(y, RHO0, dagger(y)))


def circle_point(u):
    # the rotor components (c_u, s_u)
    u = F(u)
    return (1 - u * u) / (1 + u * u), 2 * u / (1 + u * u)


def is_pure(rho):
    """Self-adjoint idempotent with rho x rho = 4 <rho x>_0 rho on every blade."""
    if not (GA.eq(dagger(rho), rho) and GA.eq(mul(rho, rho), rho)):
        return False
    return all(GA.eq(mul(rho, b, rho), GA.scal(F(4) * s0(mul(rho, b)), rho)) for b in BLADES)


def coefficient_rank(xs):
    keys = sorted({b for x in xs for b in x})
    return GA.mat_rank([[x.get(b, F(0)) for b in keys] for x in xs])


US = [F(0), F(-1, 2), F(-2, 5), F(-5, 12), F(1, 3), F(1), F(7, 4), F(-3), F(2, 9)]


# ------------------------------------------------------------------ (1)
def check_quarter_turned_chsh_elements_anticommute_and_values_lie_in_a_disc():
    premise("synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate")
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    assert GA.eq(CQ, chsh(A2, GA.neg(A1), B1, B2))
    assert GA.eq(mul(IB, IB), GA.scal(F(-1), ONE)) and GA.eq(dagger(IB), GA.scal(F(-1), IB))
    assert GA.commutes(IB, A1, SQ) and GA.commutes(IB, A2, SQ) and GA.commutes(IB, K, SQ)
    assert GA.anticommutes(C, IB, SQ) and GA.anticommutes(C, CQ, SQ)
    four_pk = GA.scal(F(4), GA.add(ONE, K))
    assert GA.eq(mul(C, C), four_pk) and GA.eq(mul(CQ, CQ), four_pk) and GA.eq(dagger(CQ), CQ)
    assert GA.eq(mul(K, C), C) and GA.eq(mul(K, CQ), CQ)
    # (x C + y Cq)^2 = 4 (x^2 + y^2)(1 + K), on one rational pair
    x, y = F(3, 7), F(-5, 2)
    L = GA.add(GA.scal(x, C), GA.scal(y, CQ))
    assert GA.eq(mul(L, L), GA.scal(F(4) * (x * x + y * y), GA.add(ONE, K)))
    # the corner P_K Cl P_K: the sixteen blades give a space of dimension 4 with basis P_K, C, I P_K, Cq
    corner = [mul(PK, b, PK) for b in BLADES]
    basis = [PK, C, mul(IB, PK), CQ]
    assert coefficient_rank(corner) == 4 and coefficient_rank(basis) == 4 and coefficient_rank(corner + basis) == 4
    # sample states: values in the disc X^2 + Y^2 <= 8
    ys = [GA.add(ONE, E[0]), GA.add(GA.scal(F(2), ONE), mul(E[0], E[1]), GA.scal(F(-1, 3), FF[0])),
          GA.add(FF[1], GA.scal(F(5, 2), mul(E[0], FF[0], E[1])), ONE), mul(GA.add(GA.scal(F(3), ONE), C), PK),
          mul(GA.add(GA.scal(F(2), ONE), CQ, C), PK)]
    worst = F(0)
    for yv in ys:
        rho = mul(yv, dagger(yv))
        r2 = value(rho, C) ** 2 + value(rho, CQ) ** 2
        assert r2 <= F(8)
        worst = max(worst, r2)
    assert worst == F(2304, 289)


# ------------------------------------------------------------------ (2)
def check_pure_states_of_the_sector_are_rational_points_of_the_circle_of_square_radius_eight():
    premise("synthesis.the-sign-is-the-rotor-at-infinity")
    premise("synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate")
    premise("synthesis.division-gives-the-rationals")
    assert is_pure(RHO0) and GA.eq(mul(K, RHO0), RHO0) and GA.commutes(GAMMA, RHO0, SQ)
    assert (value(RHO0, C), value(RHO0, CQ)) == (F(2), F(-2))
    assert GA.eq(RHO0, GA.add(GA.scal(F(1, 2), PK), GA.scal(F(1, 8), GA.sub(C, CQ))))
    even_points = []
    for u in US:
        rho = rho_of(u)
        c, s = circle_point(u)
        X, Y = value(rho, C), value(rho, CQ)
        assert is_pure(rho) and GA.eq(mul(K, rho), rho)
        assert (X, Y) == (F(2) * (c - s), F(-2) * (c + s)) and X * X + Y * Y == F(8)
        assert GA.eq(rho, GA.add(GA.scal(F(1, 2), PK), GA.scal(X / F(16), C), GA.scal(Y / F(16), CQ)))
        # the same value from the fixed state rho_0 and directions of party B turned by the rotor: y^{-1} b y = b R_u^{-1}, R_u = c - s I
        Rinv = GA.add(GA.scal(c, ONE), GA.scal(s, IB))
        y = GA.add(ONE, GA.scal(u, IB))
        yinv = GA.scal(1 / (1 + u * u), dagger(y))
        b1, b2 = mul(yinv, B1, y), mul(yinv, B2, y)
        assert GA.eq(b1, mul(B1, Rinv)) and GA.eq(b2, mul(B2, Rinv))
        assert GA.eq(b1, GA.add(GA.scal(c, B1), GA.scal(s, B2)))
        assert GA.eq(dagger(b1), b1) and GA.eq(mul(b1, b1), ONE) and GA.commutes(b1, A2, SQ)
        assert value(RHO0, chsh(A1, A2, b1, b2)) == X
        if GA.commutes(GAMMA, rho, SQ):
            even_points.append((u, X, Y))
    # among the sample, the states that commute with the total parity are those with X = -Y = 2 or -2
    assert even_points == [(F(0), F(2), F(-2))]
    rho_inf = mul(IB, RHO0, dagger(IB))
    assert is_pure(rho_inf) and (value(rho_inf, C), value(rho_inf, CQ)) == (F(-2), F(2))
    assert GA.commutes(GAMMA, rho_inf, SQ)
    # the stored pair state at equal weights (c s = -1/2, r = 0) is this point
    v = [GA.scal(F(1, 2), GA.add(E[k], FF[k])) for k in range(len(E))]
    w = [GA.scal(F(1, 2), GA.sub(E[k], FF[k])) for k in range(len(E))]
    pair = GA.add(GA.scal(F(1, 4), GA.add(ONE, GAMMA)), GA.scal(F(-1, 2), GA.add(mul(w[0], w[1]), mul(v[1], v[0]))))
    assert GA.eq(pair, rho_inf)
    # pinned values
    assert value(rho_of(F(-1, 2)), C) == F(14, 5) and value(rho_of(F(-2, 5)), C) == F(82, 29)
    assert value(rho_of(F(-5, 12)), C) == F(478, 169)
    # a general self-adjoint element of the corner s P_K + x C + y Cq is idempotent iff s = 1/2, 32(x^2 + y^2) = 1
    for (s, x, y, expect) in ((F(1, 2), F(1, 8), F(1, 8), True), (F(1, 2), F(7, 40), F(1, 40), True),
                              (F(1, 2), F(1, 8), F(0), False), (F(1, 3), F(1, 8), F(1, 8), False)):
        t = GA.add(GA.scal(s, PK), GA.scal(x, C), GA.scal(y, CQ))
        assert GA.eq(mul(t, t), t) == expect and (s == F(1, 2) and F(32) * (x * x + y * y) == F(1)) == expect


# ------------------------------------------------------------------ (3)
def pell_pairs(limit):
    out, x, q = [], 1, 1
    while q <= limit:
        out.append((x, q))
        x, q = 3 * x + 4 * q, 2 * x + 3 * q
    return out


def check_denominator_law_and_the_pell_records():
    premise("synthesis.division-gives-the-rationals")
    premise("synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate")
    equal = []
    for q in range(1, QMAX + 1):
        top = isqrt(8 * q * q)
        for p in range(0, top + 1):
            if gcd(p, q) != 1:
                continue
            gap = 8 * q * q - p * p
            assert gap >= 4
            if gap == 4:
                equal.append((p, q))
            if p % 2 == 1:
                assert gap >= 7
            if p % 4 == 0:
                assert gap >= 8
    # values of pure states of the sector: fractions P/Q in lowest terms with 8 Q^2 - P^2 a perfect square;
    # their running maxima by increasing denominator are the Pell values in this range (computed)
    best, running = F(0), []
    for q in range(1, QMAX + 1):
        for p in range(isqrt(8 * q * q), 0, -1):
            if gcd(p, q) == 1 and isqrt(8 * q * q - p * p) ** 2 == 8 * q * q - p * p:
                if F(p, q) > best:
                    best = F(p, q)
                    running.append((p, q))
                break
    assert running == [(2, 1), (14, 5), (82, 29), (478, 169)]
    # the Pell values are not the running maxima of all state values: 280/99 exceeds 82/29 below denominator 169
    assert F(82, 29) < F(280, 99) and F(280, 99) ** 2 < F(8) and F(8) * F(35, 99) ** 2 <= F(1)
    pairs = pell_pairs(QMAX)
    assert pairs == [(1, 1), (7, 5), (41, 29), (239, 169)]
    assert equal == [(2 * x, q) for x, q in pairs]
    for x, q in pell_pairs(10 ** 12):
        assert x * x - 2 * q * q == -1
        S = F(2 * x, q)
        assert F(8) - S * S == F(4, q * q)
        # the legs (x - 1)/2 and (x + 1)/2 with hypotenuse q, and the rational bracket of the distance to the bound
        a, b = (x - 1) // 2, (x + 1) // 2
        assert a * a + b * b == q * q and F(2) * (F(a, q) + F(b, q)) == S
        assert S * S < F(8) < (S + F(1, q * q)) ** 2
    # descent: every positive solution with q > 1 comes from a smaller one
    for x, q in pell_pairs(10 ** 12)[1:]:
        x0, q0 = 3 * x - 4 * q, 3 * q - 2 * x
        assert 0 < q0 < q and x0 > 0 and x0 * x0 - 2 * q0 * q0 == -1
    # the records as values of pure states: u_k = -b/(q + a)
    for (x, q), u in zip(pairs, (F(0), F(-1, 2), F(-2, 5), F(-5, 12))):
        a, b = (x - 1) // 2, (x + 1) // 2
        assert u in (F(-b, q + a), F(-a, q + b))
        assert value(rho_of(u), C) == F(2 * x, q)
