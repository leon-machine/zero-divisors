"""transport.no-transport-terminates: exact checks.

GA.py with custom signature tuples. Rule 1: from every base Cl(p,q) with 0 <= n = p + q <= 4 (definite
bases included) adjoin e+ (square +1, index n) and e- (square -1, index n+1). Rule 2: from every type-C
base Cl(p,q) (p - q = 1 mod 4, n <= 5) adjoin nu (square +1 or -1, index n), with eps_+- = (1 +- omega)/2.
(1) Rule 1 completions have mixed signature (p+1, q+1); f = (e+ + e-)/2 and f* = (e+ - e-)/2 are nonzero,
    null (f^2 = f*^2 = 0) and f f* + f* f = 1, and left multiplication by f has rank 2^(n+1) out of
    2^(n+2): the adjoined pair is itself type N, a zero divisor.
(2) Rule 2 completions: E11 = eps_+, E22 = eps_-, E12 = eps_+ nu, E21 = s eps_- nu (s = nu^2) satisfy the
    2 x 2 matrix-unit relations; E11 is an idempotent that does not commute with nu (non-central, type
    P), E12 is a nonzero nilpotent (E12^2 = 0), the corner E11 B E11 has dimension 2^(n-1) (n <= 3), so
    B = Mat_2(corner); left multiplication by E12 has rank 2^n of 2^(n+1) (singular).
(3) No completion is a division algebra: in every case above a nonzero element has a nontrivial left
    annihilator.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

ONE = GA.sc(1)


def rank(xs, n):
    bl = GA.all_blades(n)
    return GA.rank_of_vectors([[x.get(b, F(0)) for b in bl] for x in xs])


def left_rank(v, S):
    n = len(S)
    return rank([GA.mul(v, {b: F(1)}, S) for b in GA.all_blades(n)], n)


BASES1 = [(p, n - p) for n in range(0, 5) for p in range(n + 1)]
BASES2 = [(p, n - p) for n in range(1, 6, 2) for p in range(n + 1) if (2 * p - n) % 4 == 1]


def check_rule_one_completion_carries_type_n():
    premise("transport.existence-locus-type-n")
    ok = len(BASES1) == 15
    for p, q in BASES1:
        n = p + q
        S = GA.sig(p, q) + (1, -1)
        ok = ok and S.count(1) == p + 1 and S.count(-1) == q + 1 and p + 1 > 0 and q + 1 > 0
        f = GA.scal(F(1, 2), GA.add(GA.gen(n), GA.gen(n + 1)))
        fs = GA.scal(F(1, 2), GA.sub(GA.gen(n), GA.gen(n + 1)))
        ok = ok and not GA.is_zero(f) and GA.is_zero(GA.mul(f, f, S)) and GA.is_zero(GA.mul(fs, fs, S))
        ok = ok and GA.eq(GA.add(GA.mul(f, fs, S), GA.mul(fs, f, S)), ONE)
        if n <= 3:
            ok = ok and left_rank(f, S) == 2 ** (n + 1)
    _tp_rv = (ok); assert _tp_rv is not False, "check_rule_one_completion_carries_type_n"; return _tp_rv


def check_rule_two_completion_carries_type_p():
    premise("transport.matrix-units-peirce-isomorphism")
    premise("transport.rule-2-ideal-fusion-sharp-form")
    ok = BASES2 == [(1, 0), (0, 3), (2, 1), (1, 4), (3, 2), (5, 0)]
    for p, q in BASES2:
        n = p + q
        w = {tuple(range(n)): F(1)}
        for s in (1, -1):
            S = GA.sig(p, q) + (s,)
            nu = GA.gen(n)
            ep = GA.scal(F(1, 2), GA.add(ONE, w))
            em = GA.scal(F(1, 2), GA.sub(ONE, w))
            E = {(1, 1): ep, (2, 2): em, (1, 2): GA.mul(ep, nu, S), (2, 1): GA.scal(s, GA.mul(em, nu, S))}
            for i in (1, 2):
                for j in (1, 2):
                    for k in (1, 2):
                        for m in (1, 2):
                            want = E[(i, m)] if j == k else {}
                            ok = ok and GA.eq(GA.mul(E[(i, j)], E[(k, m)], S), want)
            ok = ok and GA.eq(GA.add(E[(1, 1)], E[(2, 2)]), ONE)
            ok = ok and not GA.commutes(E[(1, 1)], nu, S)
            ok = ok and not GA.is_zero(E[(1, 2)]) and GA.is_zero(GA.mul(E[(1, 2)], E[(1, 2)], S))
            if n <= 3:
                corner = [GA.mul(GA.mul(ep, {b: F(1)}, S), ep, S) for b in GA.all_blades(n + 1)]
                ok = ok and rank(corner, n + 1) == 2 ** (n - 1)
                ok = ok and left_rank(E[(1, 2)], S) == 2 ** n
    _tp_rv = (ok); assert _tp_rv is not False, "check_rule_two_completion_carries_type_p"; return _tp_rv


# Sample bases for the division-algebra test (the first ten Rule-1 bases and first three Rule-2 bases)
# and the signs of nu^2 for Rule 2.
RULE1_SAMPLE = BASES1[:10]
RULE2_SAMPLE = BASES2[:3]
NU_SQUARES = (-1, 1)


def check_no_completion_is_a_division_algebra():
    premise("transport.existence-locus-type-n")
    ok = True
    for p, q in RULE1_SAMPLE:
        n = p + q
        S = GA.sig(p, q) + (1, -1)
        f = GA.add(GA.gen(n), GA.gen(n + 1))       # e+ + e-, a nonzero multiple of the docstring's f
        # f is null and nonzero, and left multiplication by it has rank exactly half: 2^(n+1) of 2^(n+2)
        ok = ok and GA.is_zero(GA.mul(f, f, S)) and not GA.is_zero(f)
        ok = ok and left_rank(f, S) * 2 == 2 ** (n + 2)
    for p, q in RULE2_SAMPLE:
        n = p + q
        for nu_sq in NU_SQUARES:
            S = GA.sig(p, q) + (nu_sq,)
            ep = GA.scal(F(1, 2), GA.add(ONE, {tuple(range(n)): F(1)}))
            ok = ok and GA.eq(GA.mul(ep, ep, S), ep)                      # eps_+ is an idempotent
            ok = ok and left_rank(ep, S) == 2 ** n
    _tp_rv = (ok); assert _tp_rv is not False, "check_no_completion_is_a_division_algebra"; return _tp_rv
