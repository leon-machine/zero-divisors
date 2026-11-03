"""families.why-kinematic-attacks-had-fail: exact checks, ported from legacy verify_T13.py
(prop:covariance) and widened (the Lambda exponent of H, Laurent sums, the principal series in Q(i)).

Monomials in (Lambda, M_P, m, kappa) are exponent tuples of Fractions; H = (Lambda/3)^(1/2) (constants
dropped), N = M_P/H. The rescaling Lambda -> kappa^2 Lambda at fixed M_P and m multiplies a monomial by
kappa^(2 x Lambda-exponent); its kappa-weight is computed by applying the substitution.
  (1) Im(-3/2 + i nu) = nu with m^2/H^2 = -w(w+3) = nu^2 + 9/4, so Im w = m/H at leading order;
      as monomials Im w = m/H = N (m/M_P).
  (2) Weights: H has weight 1, N weight -1, m/M_P weight 0 (the premise), Im w weight -1; mass ratios
      have weight 0.
  (3) The covariance f(N/kappa) = f(N)/kappa: for a Laurent sum f = sum c_a N^a it holds iff only a = 1
      occurs (monomial comparison over 6 exponents and 5 sums), and exactly at rational sample points;
      Zel'dovich-Weinberg m_h^3 = M_P^2 H is m_h/M_P = N^(-1/3) (exponents), the hadronic Im w = N^(2/3)
      is the same relation, and both have kappa-weight 1/3 != 0 = weight of m/M_P: no kinematic theorem.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

LAM, MP, M, KAP = (F(1), F(0), F(0), F(0)), (F(0), F(1), F(0), F(0)), (F(0), F(0), F(1), F(0)), (F(0), F(0), F(0), F(1))
EXPONENTS = [F(1, 3), F(2, 3), F(1), F(2), F(-1, 3), F(0)]
SUMS = [{F(1): F(3)}, {F(1): F(2), F(2): F(1)}, {F(2, 3): F(1)}, {F(1): F(1), F(-1, 3): F(5)}, {F(0): F(7)}]
NK = [(F(7, 3), F(2)), (F(5), F(1, 3)), (F(2, 9), F(4))]


def mmul(a, b):
    return tuple(x + y for x, y in zip(a, b))


def mpow(a, k):
    return tuple(k * x for x in a)


def rescale(mono):
    """Lambda -> kappa^2 Lambda: a monomial Lambda^l ... picks up kappa^(2 l)."""
    return mono[:3] + (mono[3] + 2 * mono[0],)


def weight(mono):
    return rescale(mono)[3] - mono[3]


H = mpow(LAM, F(1, 2))
N = mmul(MP, mpow(H, -1))
RATIO = mmul(M, mpow(MP, -1))
IMW = mmul(M, mpow(H, -1))


def check_imaginary_weight_is_mass_in_hubble_units():
    premise("families.imported-dictionary-exact-join")
    ok = True
    for nu in (F(1), F(7, 2), F(1000)):
        w = GA.qi(F(-3, 2), nu)
        x2 = (-(w * (w + GA.qi(3)))).re                  # m^2/H^2 read off the dictionary
        ok = ok and w.im == nu and x2 == nu * nu + F(9, 4)
    # hand value: nu = 1000 gives m^2/H^2 = 1000002.25, so Im w H/m = 1000/sqrt(1000002.25) -> 1
    ok = ok and (-(GA.qi(F(-3, 2), 1000) * GA.qi(F(3, 2), 1000))).re == F(4000009, 4)
    ok = ok and mmul(N, RATIO) == IMW
    GA.check("Im w = m/H = N (m/M_P)", ok)
    assert ok


def check_rescaling_weights():
    premise("standard-model.trichotomy-what-kind-number")
    ok = weight(H) == 1 and weight(N) == -1 and weight(RATIO) == 0 and weight(IMW) == -1
    ok = ok and rescale(N) == mmul(N, mpow(KAP, -1)) and rescale(RATIO) == RATIO
    ok = ok and weight(mmul(M, mpow(M, -1))) == 0 and weight(mmul(mpow(M, 2), mpow(MP, -2))) == 0
    GA.check("N -> N/kappa, m/M_P invariant, Im w -> Im w/kappa", ok)
    assert ok


def check_covariance_forces_linear():
    premise("standard-model.trichotomy-what-kind-number")
    ok = True
    # monomials in (N, kappa): f(N/kappa) has N^a kappa^-a, f(N)/kappa has N^a kappa^-1
    for a in EXPONENTS:
        ok = ok and (((a, -a)) == ((a, F(-1)))) == (a == 1)
    for f in SUMS:
        lhs = {(a, -a): c for a, c in f.items()}
        rhs = {(a, F(-1)): c for a, c in f.items()}
        ok = ok and (lhs == rhs) == (set(f) == {F(1)})
    for n, k in NK:
        for a in range(-1, 4):
            ok = ok and (((n / k) ** a == n ** a / k) == (a == 1))
    # Zel'dovich-Weinberg: m^3 M_P^-2 H^-1 = 1  <=>  (m/M_P)^3 = H/M_P = N^-1
    zw = mmul(mmul(mpow(M, 3), mpow(MP, -2)), mpow(H, -1))
    ok = ok and mpow(RATIO, 3) == mmul(zw, mpow(N, -1)) and weight(zw) == -1
    # hadronic Im w = N^(2/3) is m/M_P = N^(-1/3); its right side has weight 1/3, the left 0
    ok = ok and mmul(IMW, mpow(N, F(-2, 3))) == mmul(RATIO, mpow(N, F(1, 3)))
    ok = ok and weight(mpow(N, F(-1, 3))) == F(1, 3) and weight(RATIO) == 0
    GA.check("covariance forces f linear; N^(2/3) and N^(-1/3) cannot be kinematic", ok)
    assert ok
