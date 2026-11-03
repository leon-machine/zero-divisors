"""synthesis.unit-boost-residue-needs-nonpositive-exponent: exact checks.

Cl(1,3), e0^2 = +1, e1..e3 square -1; B_i = e0 e_i; B_w = sum_i p_i B_i (the residue of the Kasner pole in the
GTG sign is -B_w, with the same square).
  (1) B_w^2 = sum_i p_i^2 exactly (the B_i square to +1 and anticommute pairwise), at Kasner-circle
      points (value 1) and at Kasner-disk points (value < 1);
  (2) on the rational parametrisation of the Kasner circle, p(u) = (-u, 1 + u, u(1 + u))/(1 + u + u^2),
      sum p = sum p^2 = 1 and min p_i < 0 for u > 0 (the first entry), and every circle point with a
      vanishing entry is a permutation of (1, 0, 0);
  (3) on the grid p = (a, b, c)/N, a + b + c = N, all entries positive (N = 12, all such triples),
      sum p^2 < 1, with the maximum 17/24 pinned (at (10, 1, 1)/12);
  (4) the Einstein-scalar relations at leading order on the Kasner ansatz with phi = q log tau, in the
      convention of the Kasner-wall Proposition (tau^2 R_00 = sum p^2 - sum p, tau^2 R_ii = -p_i(sum p - 1),
      de Sitter Ric = Lambda g, so R_ab = -8 pi G d_a phi d_b phi): with k := 8 pi G q^2, sum p = 1 and
      sum p^2 = 1 - k, so B_w^2 = 1 - k; the stiff isotropic point (1/3, 1/3, 1/3) has k = 2/3.
"""
from fractions import Fraction as F
import GA
from GA import mul, add, gen, sig, scal
from tp_premise import premise

SQ = sig(1, 3)


def bw(p):
    out = {}
    for i in range(3):
        out = add(out, scal(p[i], mul(gen(0), gen(i + 1), SQ)))
    return out


def sq(p):
    return sum(x * x for x in p)


def circle(u):
    d = 1 + u + u * u
    return (F(-u) / d, F(1 + u) / d, F(u * (1 + u)) / d)


def check_residue_square_is_sum_of_squares():
    premise("dark-energy.frozen-point-datum-kasner-wall")
    for p in (circle(F(2)), circle(F(1, 3)), (F(1, 3), F(1, 3), F(1, 3)), (F(1, 2), F(1, 4), F(1, 4))):
        B = bw(p)
        assert mul(B, B, SQ) == {(): sq(p)}
    assert circle(F(2)) == (F(-2, 7), F(3, 7), F(6, 7))
    assert sq((F(1, 2), F(1, 4), F(1, 4))) == F(3, 8)
    return True


def check_circle_has_nonpositive_entry():
    premise("dark-energy.forcing-half-schwarzschild-wall-residue-sense")
    for u in (F(1, 5), F(1, 2), F(1), F(2), F(7, 3), F(10)):
        p = circle(u)
        assert sum(p) == 1 and sq(p) == 1
        assert min(p) < 0 and p[0] < 0
    assert circle(F(1)) == (F(-1, 3), F(2, 3), F(2, 3))
    assert circle(F(1, 2)) == (F(-2, 7), F(6, 7), F(3, 7))
    # a circle point with an entry 0: the other two satisfy b + c = 1, b^2 + c^2 = 1, so b c = 0
    hits = []
    for b in range(-12, 13):
        bb = F(b, 12)
        cc = 1 - bb
        if bb * bb + cc * cc == 1:
            assert bb * cc == 0
            hits.append(bb)
    assert hits == [F(0), F(1)]
    return True


def check_positive_exponents_not_unit():
    premise("dark-energy.frozen-point-datum-kasner-wall")
    N = 12
    best = F(0)
    count = 0
    for a in range(1, N):
        for b in range(1, N - a):
            c = N - a - b
            p = (F(a, N), F(b, N), F(c, N))
            s = sq(p)
            assert s < 1
            assert 1 - s == 2 * (p[0] * p[1] + p[0] * p[2] + p[1] * p[2])
            best = max(best, s)
            count += 1
    assert count == 55 and best == F(17, 24)
    return True


def check_scalar_kasner_relations():
    premise("dark-energy.frozen-point-datum-kasner-wall")
    premise("synthesis.diagonal-kasner-momentum-constraint")
    for p in ((F(1, 3), F(1, 3), F(1, 3)), (F(1, 2), F(1, 4), F(1, 4)), circle(F(3))):
        S1, S2 = sum(p), sq(p)
        assert S1 == 1
        R00 = S2 - S1                      # tau^2 R_00 on the ansatz
        Rii = [-x * (S1 - 1) for x in p]   # tau^2 R_ii
        k = -R00                           # R_00 = -8 pi G (d_tau phi)^2, (d_tau phi)^2 = q^2 / tau^2
        assert all(r == 0 for r in Rii)
        assert k >= 0 and S2 == 1 - k
        B = bw(p)
        assert mul(B, B, SQ) == {(): 1 - k}
    assert -(sq((F(1, 3), F(1, 3), F(1, 3))) - 1) == F(2, 3)
    return True
