"""mass.mass-weight-dictionary: exact checks in GA (tractors as Clifford vectors), ported from legacy
verify_T11.py Part A (thm:dictionary) and recast in GA.

For dimension n the tractor space is built in GA with signature (1, n-1) on the spacetime generators
0..n-1 and two more generators e+ (square +1), e- (square -1); n0 = (e+ + e-)/2, ninf = e+ - e-, so
Q(ninf) = Q(n0) = 0, ninf . n0 = 1, and a tractor (sigma, mu, rho) is sigma ninf + mu + rho n0 (for
n = 4 this is Cl(2,4), the store's tractor algebra). The Thomas operator of the premise,
D sigma = (w(n+2w-2) sigma, (n+2w-2) grad sigma, -(Box sigma - w J sigma)), is linear in the formal
data (sigma, grad sigma, Box sigma); the check builds the three tractor coefficients of D sigma, pairs
each with the frozen point I = ninf + (J/n) n0 by GA.dot, and reads m^2 off the Klein-Gordon equation:
I . D sigma = a Box sigma + b sigma (+ 0 grad sigma) = 0 means (Box + b/a) sigma = 0, m^2 = b/a.
  (1) m^2 = -w(w+n-1) Q(I) on a 144-point grid (w, n, J), with Q(I) = 2J/n computed in GA; the
      gradient slot always pairs to zero; the opposite sign fails wherever m^2 != 0.
  (2) n = 4, J = 2 Lambda/3: Q(I) = Lambda/3 = H^2 and m^2 = -w(w+3) Lambda/3, at three Lambda;
      consistency of the premise: (1/n) D 1 at w = 1 is the frozen point (1, 0, J/n).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

WS = [F(1), F(-2), F(3, 2), F(7, 3), F(10), F(-1), F(-3), F(0), F(-1, 2)]
NS = [3, 4, 5, 6]
JS = [F(1), F(-2, 3), F(5, 7), F(2)]
LAMS = [F(3), F(-6, 5), F(1, 7)]
_ALG = {}


def algebra(n):
    if n not in _ALG:
        S = tuple([1] + [-1] * (n - 1) + [1, -1])
        E = [GA.gen(i) for i in range(n + 2)]
        n0 = GA.scal(F(1, 2), GA.add(E[n], E[n + 1]))
        ninf = GA.sub(E[n], E[n + 1])
        grad = GA.add(*[GA.scal(F(k + 2), E[k]) for k in range(n)])      # a sample gradient vector
        _ALG[n] = (S, ninf, n0, grad)
    return _ALG[n]


def pairing(w, n, J):
    """(a, b, c): I . D sigma = a Box sigma + b sigma + c (grad-sample) with I = ninf + (J/n) n0."""
    S, ninf, n0, grad = algebra(n)
    I = GA.add(ninf, GA.scal(J / n, n0))
    d_sigma = GA.add(GA.scal(w * (n + 2 * w - 2), ninf), GA.scal(w * J, n0))
    d_box = GA.scal(-1, n0)
    d_grad = GA.scal(n + 2 * w - 2, grad)
    return GA.dot(I, d_box, S), GA.dot(I, d_sigma, S), GA.dot(I, d_grad, S), GA.dot(I, I, S)


def check_mass_is_minus_w_w_plus_n_minus_one_times_norm():
    premise("mass.imported-thomas-operator")
    premise("mass.imported-frozen-point-tractor-connection")
    ok_minus, ok_plus, nonzero = True, True, 0
    for w in WS:
        for n in NS:
            for J in JS:
                a, b, c, QI = pairing(w, n, J)
                ok_minus = ok_minus and a == -1 and c == 0 and QI == 2 * J / n
                m2 = b / a
                ok_minus = ok_minus and m2 == -w * (w + n - 1) * QI
                if m2 != 0:
                    nonzero += 1
                    ok_plus = ok_plus and m2 != w * (w + n - 1) * QI
    ok = ok_minus and ok_plus and nonzero == 120      # 144 less w = 0 (16) and w = 1 - n (n = 3, 4: 8)
    # hand value: w = 1, n = 4, J = 2: Q(I) = 1, m^2 = -1*4*1 = -4
    a, b, c, QI = pairing(F(1), 4, F(2))
    ok = ok and QI == 1 and b / a == -4
    GA.check("m^2 = -w(w+n-1) Q(I) read off I . D sigma = 0", ok)
    assert ok


def check_four_dimensions_in_lambda_and_frozen_point():
    premise("mass.imported-thomas-operator")
    premise("mass.imported-frozen-point-tractor-connection")
    ok = True
    for lam in LAMS:
        J = 2 * lam / 3
        for w in WS:
            a, b, c, QI = pairing(w, 4, J)
            ok = ok and QI == lam / 3 and b / a == -w * (w + 3) * lam / 3
    # the constant density 1 at w = 1: (1/n) D 1 = (1, 0, J/n), the frozen point itself
    for n in NS:
        S, ninf, n0, grad = algebra(n)
        for J in JS:
            D1 = GA.add(GA.scal(F(1) * (n + 2 - 2), ninf), GA.scal(J, n0))
            ok = ok and GA.eq(GA.scal(F(1, n), D1), GA.add(ninf, GA.scal(J / n, n0)))
    # hand value: the conformally coupled w = -1 at Lambda = 3 has m^2 = 2 = 2 H^2
    a, b, c, QI = pairing(F(-1), 4, F(2))
    ok = ok and b / a == 2 and QI == 1
    GA.check("n = 4: m^2 = -w(w+3) Lambda/3 = -w(w+3) H^2", ok)
    assert ok
