"""singularity.rate-rigidity-temperature-not-algebra-intrinsic: exact checks.

Single-mode algebra A = Mat_2(C), K = diag(0, 1), alpha_t = Ad(e^{itK}); every *-automorphism is Ad_U, U
unitary. omega_beta has density diag(1, x)/(1 + x), x = e^{-beta}, so omega_{-beta} has x -> 1/x.
theta = Ad_U intertwines alpha_t with alpha_{ct} iff U K U^{-1} = cK + d for a scalar d.
(1) Commuting (c = 1): the solutions U of U K = (K + d) U contain an invertible matrix only for d = 0, and
    then form the diagonal matrices (kernel computed); every diagonal unitary over Q(i) tested fixes omega_beta at
    x = 9/16 and 16/9.
(2) Reversing (c = -1): U K = (-K + d) U has invertible solutions only for d = 1, the anti-diagonal matrices;
    for anti-diagonal unitaries over Q(i), omega_beta o theta = omega_{-beta}.
(3) Reparametrisation: the KMS system for the flow of cK at inverse temperature b, whose Boltzmann matrix is
    diag(1, e^{-cb}), is solved for an unknown density: (K, beta) and (2K, beta/2) give the same solution,
    (2K, beta) a different one (x -> x^2), at x = 9/16, 16/9 (x^(1/2) = 3/4, 4/3 rational).
(4) Intertwiners exist only for c = +-1: the spectrum condition {0, 1} = {d, c + d} has exactly the
    solutions (c, d) = (1, 0), (-1, 1), and for c in {2, 1/2, -3, 3/2} (with d = (1 - c)/2 from the trace)
    the solutions of U K = (cK + d) U are all singular; the Gibbs map x -> omega is injective on samples,
    so the orbit of omega_beta under intertwining automorphisms is {omega_beta, omega_{-beta}}.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI
ZERO, ONE = QI(0), QI(1)
XS = (F(9, 16), F(16, 9))


def q(x):
    return x if isinstance(x, QI) else QI(x)


mm = GA.field_mat_mul


def dag(A):
    return [[q(A[j][i]).conj() for j in range(2)] for i in range(2)]


def meq(A, B):
    return all(q(A[i][j]) == q(B[i][j]) for i in range(2) for j in range(2))


def gibbs(x):
    return [[QI(1 / (1 + x)), ZERO], [ZERO, QI(x / (1 + x))]]


K = [[F(0), F(0)], [F(0), F(1)]]


def intertwiner_space(c, d):
    """Kernel of U -> U K - (cK + d) U on 2 x 2 matrices (unknowns u00, u01, u10, u11)."""
    rows = []
    T = [[c * K[i][j] + (d if i == j else 0) for j in range(2)] for i in range(2)]
    for i in range(2):
        for j in range(2):
            row = [F(0)] * 4
            for t in range(2):
                row[2 * i + t] += K[t][j]
                row[2 * t + j] -= T[i][t]
            rows.append(row)
    return GA.field_kernel(rows)


COMBOS = [(F(1), F(0)), (F(0), F(1)), (F(1), F(1)), (F(1), F(2)), (F(2), F(-3))]


def has_invertible(ker):
    """Whether the span of the kernel contains an invertible matrix (det is a quadratic form in the
    coefficients; it vanishes identically iff it vanishes at these five points for a span of dim <= 2)."""
    for a, b in COMBOS:
        v = [a * ker[0][t] + (b * ker[1][t] if len(ker) > 1 else 0) for t in range(4)] if ker else [0] * 4
        if v[0] * v[3] - v[1] * v[2] != 0:
            return True
    return False


def state_after(U, rho):
    """Density of omega o Ad_U: omega(U A U*) = tr(rho U A U*) = tr(U* rho U A)."""
    return mm(mm(dag(U), rho), U)


DIAG_U = [[[QI(F(3, 5), F(4, 5)), ZERO], [ZERO, QI(F(5, 13), F(-12, 13))]],
          [[ONE, ZERO], [ZERO, QI(0, 1)]]]
ANTI_U = [[[ZERO, QI(F(8, 17), F(15, 17))], [QI(F(3, 5), F(-4, 5)), ZERO]],
          [[ZERO, ONE], [ONE, ZERO]]]


def check_commuting_automorphisms_fix_gibbs():
    premise("singularity.kms-uniqueness-factor")
    ker = intertwiner_space(1, 0)
    ok = len(ker) == 2 and all(v[1] == 0 and v[2] == 0 for v in ker)
    ok = ok and has_invertible(ker)
    ok = ok and all(not has_invertible(intertwiner_space(1, d)) for d in (F(1), F(-1), F(1, 2)))
    for U in DIAG_U:
        ok = ok and meq(mm(U, dag(U)), [[ONE, ZERO], [ZERO, ONE]])
        for x in XS:
            ok = ok and meq(state_after(U, gibbs(x)), gibbs(x))
    _tp_rv = (ok); assert _tp_rv is not False, "check_commuting_automorphisms_fix_gibbs"; return _tp_rv


def check_reversing_automorphisms_flip_beta():
    premise("singularity.kms-uniqueness-factor")
    ker = intertwiner_space(-1, 1)
    ok = len(ker) == 2 and all(v[0] == 0 and v[3] == 0 for v in ker)
    ok = ok and has_invertible(ker)
    ok = ok and all(not has_invertible(intertwiner_space(-1, d)) for d in (F(0), F(2), F(-1)))
    for U in ANTI_U:
        ok = ok and meq(mm(U, dag(U)), [[ONE, ZERO], [ZERO, ONE]])
        for x in XS:
            ok = ok and meq(state_after(U, gibbs(x)), gibbs(1 / x))
            ok = ok and not meq(state_after(U, gibbs(x)), gibbs(x))
    _tp_rv = (ok); assert _tp_rv is not False, "check_reversing_automorphisms_flip_beta"; return _tp_rv


def kms_solution(y):
    """Unknown density r (4 entries) with omega(E_ab) = r_ba; KMS for Boltzmann matrix diag(1, y)."""
    w = [F(1), y]
    rows = []
    for s1 in range(2):
        for t1 in range(2):
            for s2 in range(2):
                for t2 in range(2):
                    c = [F(0)] * 4
                    if t1 == s2:
                        c[2 * t2 + s1] += 1
                    if t2 == s1:
                        c[2 * t1 + s2] -= w[s1] / w[t1]
                    if any(c):
                        rows.append(c)
    ker = GA.field_kernel(rows)
    v = ker[0]
    t = v[0] + v[3]
    return len(ker), [x / t for x in v]


def check_reparametrisation_rescales_beta():
    premise("singularity.kms-uniqueness-factor")
    ok = True
    for x, rt in ((F(9, 16), F(3, 4)), (F(16, 9), F(4, 3))):
        ok = ok and rt * rt == x
        n1, s1 = kms_solution(x)                  # (K, beta): e^{-beta}
        n2, s2 = kms_solution((rt * rt))          # (2K, beta/2): e^{-2 (beta/2)} = (x^(1/2))^2
        n3, s3 = kms_solution(x * x)              # (2K, beta): e^{-2 beta}
        n4, s4 = kms_solution(rt)                 # (K, beta/2)
        ok = ok and (n1, n2, n3, n4) == (1, 1, 1, 1)
        ok = ok and s1 == s2 and s1 != s3 and s1 != s4
        ok = ok and s1 == [1 / (1 + x), F(0), F(0), x / (1 + x)]
    _tp_rv = (ok); assert _tp_rv is not False, "check_reparametrisation_rescales_beta"; return _tp_rv


def check_only_orientation_flip_intertwines():
    premise("singularity.kms-uniqueness-factor")
    # spectrum {d, c + d} = {0, 1}: trace c + 2d = 1 and det d (c + d) = 0
    sols = []
    for d in (F(0),):                              # case d = 0
        sols.append((1 - 2 * d, d))
    # case c + d = 0: then 1 = c + 2d = d, c = -1
    sols.append((F(-1), F(1)))
    ok = all(c + 2 * d == 1 and d * (c + d) == 0 for c, d in sols) and sols == [(1, 0), (-1, 1)]
    for c in (F(2), F(1, 2), F(-3), F(3, 2)):
        d = (1 - c) / 2
        ok = ok and d * (c + d) != 0 and not has_invertible(intertwiner_space(c, d))
    for (c, d) in sols:
        ok = ok and has_invertible(intertwiner_space(c, d))
    states = [gibbs(x) for x in (F(1, 3), F(9, 16), F(1), F(16, 9), F(3))]
    ok = ok and all(not meq(states[i], states[j]) for i in range(5) for j in range(i + 1, 5))
    _tp_rv = (ok); assert _tp_rv is not False, "check_only_orientation_flip_intertwines"; return _tp_rv
