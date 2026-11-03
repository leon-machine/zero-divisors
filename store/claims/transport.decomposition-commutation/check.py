"""transport.decomposition-commutation: exact checks.

A = Cl(V, Q) on generators e_0..e_{n-1} (degenerate V included), nu = e_n adjoined orthogonally with
nu^2 = gamma in {+1, -1, 0}, B_gamma = Cl(V + <nu>).
(1) B_gamma = A + A nu: the blades of A together with the blades of A times nu are linearly
    independent and span B_gamma (rank 2^(n+1) = 2^n + 2^n), for gamma = 0 as well.
(2) nu a = a^ nu for every blade of A and for sample non-homogeneous a, with a^ the grade
    involution; controls: nu a = a nu fails for odd a, and the product nu a is not a nu.
(3) For gamma = +-1, nu is invertible with nu^{-1} = gamma nu; for gamma = 0, nu^2 = 0 so nu is
    not invertible.
No premises (blade count and anticommutation).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise  # noqa: F401  (no store premises)

BASES = [(1, 0, 0), (0, 1, 0), (2, 0, 0), (1, 1, 0), (0, 2, 0), (2, 1, 0), (1, 2, 0), (1, 3, 0),
         (3, 1, 0), (2, 0, 1), (1, 1, 1), (3, 0, 1), (2, 2, 0)]
GAMMAS = (1, -1, 0)
SAMPLE_A = [{(): F(2), (0,): F(1), (0, 1): F(-3)}, {(0,): F(1, 2), (1,): F(5), (0, 1): F(1)},
            {(): F(1), (0, 1): F(7)}]


def _sq(p, q, r, g):
    return GA.sig(p, q, r) + (g,)


def check_direct_sum_decomposition():
    ok = True
    for (p, q, r) in BASES:
        n = p + q + r
        for g in GAMMAS:
            sq = _sq(p, q, r, g)
            blades_B = GA.all_blades(n + 1)
            nu = GA.gen(n)
            part_A = [{b: F(1)} for b in GA.all_blades(n)]
            part_Anu = [GA.mul({b: F(1)}, nu, sq) for b in GA.all_blades(n)]
            rows = [GA.basis_vector_of(x, blades_B) for x in part_A + part_Anu]
            ok = ok and GA.rank_of_vectors(rows) == 2 ** (n + 1)
            ok = ok and GA.rank_of_vectors(rows[:len(part_A)]) == 2 ** n
            ok = ok and GA.rank_of_vectors(rows[len(part_A):]) == 2 ** n
    GA.check("B_gamma = A + A nu (rank 2^(n+1)) for 13 base spaces and gamma = +1, -1, 0", ok)
    return ok


def check_commutation_by_grade_involution():
    ok = True
    for (p, q, r) in BASES:
        n = p + q + r
        for g in GAMMAS:
            sq = _sq(p, q, r, g)
            nu = GA.gen(n)
            odd_seen = False
            for b in GA.all_blades(n):
                a = {b: F(1)}
                lhs = GA.mul(nu, a, sq)
                rhs = GA.mul(GA.grade_inv(a), nu, sq)
                ok = ok and GA.eq(lhs, rhs)
                if len(b) % 2 == 1:
                    odd_seen = True
                    ok = ok and GA.eq(lhs, GA.scal(-1, GA.mul(a, nu, sq)))   # odd blade: sign -1
                    ok = ok and not GA.eq(lhs, GA.mul(a, nu, sq))
            ok = ok and odd_seen
            if n >= 2:
                for a in SAMPLE_A:
                    ok = ok and GA.eq(GA.mul(nu, a, sq), GA.mul(GA.grade_inv(a), nu, sq))
    GA.check("nu a = a^ nu on every blade and on sample elements, gamma = +1, -1, 0", ok)
    return ok


def check_inverse_is_gamma_nu():
    ok = True
    for (p, q, r) in BASES:
        n = p + q + r
        for g in (1, -1):
            sq = _sq(p, q, r, g)
            nu = GA.gen(n)
            inv = GA.scal(g, nu)
            ok = ok and GA.eq(GA.mul(nu, inv, sq), GA.sc(1)) and GA.eq(GA.mul(inv, nu, sq), GA.sc(1))
            ok = ok and GA.eq(GA.mul(nu, nu, sq), GA.sc(g))
        sq0 = _sq(p, q, r, 0)
        nu = GA.gen(n)
        ok = ok and GA.is_zero(GA.mul(nu, nu, sq0))     # gamma = 0: nu^2 = 0, nu not invertible
    GA.check("nu^{-1} = gamma nu for gamma = +-1; nu^2 = 0 for gamma = 0", ok)
    return ok
