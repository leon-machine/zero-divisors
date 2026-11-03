"""synthesis.admissible-decay-does-not-control-tangential-derivatives: exact checks.

phi(y) = y/(1 + y^2): |phi| <= 1/2 (1 + y^2 - 2|y| = (1 - |y|)^2), phi'(y) = (1 - y^2)/(1 + y^2)^2, phi'(0) = 1.
At tau = 1/n^2, a_tau(x) = n^{-1} phi(n^4 x): sup |a_tau| = 1/(2n) (attained at x = 1/n^4), d/dx a_tau(0) = n^3.
The boost B = e0 e2 of Cl(1,3) squares to 1, so exp(sB) = c + sB with c^2 - s^2 = 1; at rational points of the
hyperbola B exp(sB) = s + cB has B-coefficient c >= 1, so ||d/dx T|| >= lambda n.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise


def phi(y):
    return y / (1 + y * y)


def check_tangential_derivative_not_controlled():
    premise("interior.transport-level-convergence-along-tangential-curves")
    # phi: bound and derivative
    num = GA.padd(GA.pmul(GA.pderiv([F(0), F(1)]), [F(1), F(0), F(1)]),
                  GA.pneg(GA.pmul([F(0), F(1)], GA.pderiv([F(1), F(0), F(1)]))))
    assert num == [F(1), F(0), F(-1)]                     # phi' numerator 1 - y^2, denominator (1+y^2)^2
    assert GA.peval(num, F(0)) == 1
    for k in range(-12, 13):
        y = F(k, 3)
        assert 2 * abs(phi(y)) <= 1 and (1 - abs(y)) ** 2 == 1 + y * y - 2 * abs(y)
    assert phi(F(1)) == F(1, 2) and phi(F(-1)) == F(-1, 2)
    # the family at tau = 1/n^2: a(x) = (1/n) phi(x / tau^2)
    for n in (2, 5, 10, 40):
        tau = F(1, n * n)
        a = lambda x: phi(x / (tau * tau)) / n
        assert a(tau * tau) == F(1, 2 * n)                # the sup, attained at x = tau^2
        assert all(2 * n * abs(a(F(j, 7 * n ** 4))) <= 1 for j in range(-30, 31))
        # coordinate derivative at 0: n^3 = tau^{-3/2}; exact difference quotient n^3/(1 + (h/tau^2)^2)
        for h in (F(1, 10 ** 12), F(1, 10 ** 15)):
            dq = a(h) / h
            assert dq == n ** 3 / (1 + (h / (tau * tau)) ** 2) and n ** 3 - dq < F(1, 10 ** 3)
        # ||E||/tau = sup/tau = n/2 = tau^{-1/2}/2: integrable (int_0^t0 tau^{-1/2}/2 = t0^{1/2})
        assert F(1, 2 * n) / tau == F(n, 2)
    # Hubble-normalised derivative tau^{1 - p_j} tau^{-3/2} = tau^{-1/2 - p_j}: exponent < 0 on the variety
    for p in (F(-1, 3), F(0), F(2, 3), F(1, 2), F(-2, 7)):
        assert F(-1, 2) - p <= F(-1, 6) or p < F(-1, 3)
    # the boost: B^2 = 1 and B (c + sB) = s + cB with c >= 1 on the unit hyperbola
    sq = (-1, 1, 1, 1)
    B = GA.mul(GA.gen(0), GA.gen(2), sq)
    assert GA.eq(GA.mul(B, B, sq), GA.sc(1))
    for c, s in ((F(5, 4), F(3, 4)), (F(13, 12), F(5, 12)), (F(1), F(0))):
        assert c * c - s * s == 1
        rot = GA.add(GA.sc(c), GA.scal(s, B))
        assert GA.eq(GA.mul(rot, GA.reverse(rot), sq), GA.sc(c * c - s * s))
        prod = GA.mul(B, rot, sq)
        assert GA.eq(prod, GA.add(GA.sc(s), GA.scal(c, B))) and prod[(0, 2)] >= 1
    return True
