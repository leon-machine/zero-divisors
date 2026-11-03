"""angle.within-supplied-class-spectrum-condition-selects: exact checks.

Supplied-class generators (Theorem singularity.class-relative-no-go-no-supplied: ultralocal, so polynomials in
the number operators) on nu = 2 and 3 fermionic modes, Jordan-Wigner basis on bitmasks.
(i) For fixed sample polynomials sum_S c_S prod_{k in S} N_k (module level), the operator built from the N_k is
    diagonal in the number basis; when the minimum is unique (at least three such generators, counted), the
    ground state is the number basis state at the minimum; for every cut (every nonempty proper subset of the
    modes) its state factorises (omega(AB) = omega(A) omega(B) for the number projectors on the two sides), its
    marginal on each mode is a rank-one idempotent diag(1, 0) or diag(0, 1), it is an eigenvector of every N_k and
    of sample boost generators sum_k w_k (N_k - 1/2); and for a single-mode side the marginal is Gibbs at no
    finite beta: diag(1, q)/(1 + q) = diag(1, 0) forces q = 0 and diag(0, 1) has no solution.
(ii) H = (N0 - N1)^2 = N0 + N1 - 2 N0 N1 on the pair has eigenvalues 0, 0, 1, 1 on |00>, |11>, |10>, |01>; its
    kernel is two-dimensional, spanned by |00> and |11>, and contains the thermofield pair 4/5|00> + 3/5|11>
    (mixed marginal diag(16/25, 9/25)) and the product state |00> alike.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
import fock
from tp_premise import premise

# sample supplied generators: {subset of modes: coefficient}
GENS2 = [{(0,): 3, (1,): 5, (0, 1): -9}, {(0,): -2, (1,): 1, (0, 1): 4}, {(0,): 2, (1,): 2, (0, 1): -4}]
GENS3 = [{(0,): 2, (1,): -3, (2,): 1, (0, 2): 4, (0, 1, 2): -1},
         {(0,): 1, (1,): 1, (2,): 1, (0, 1): -1, (1, 2): -1}, {(1,): -4, (0, 1): 3, (2,): 2}]
WEIGHTS = [F(1), F(3, 2), F(-2, 5)]


def number_op(nu, k):
    return fock.to_dense(fock.num(k, nu), 1 << nu)


mm = GA.mat_mul                         # dense matrix product


def madd(a, b, c=1):
    n = len(a)
    return [[a[i][j] + F(c) * b[i][j] for j in range(n)] for i in range(n)]


def build(nu, poly):
    d = 1 << nu
    H = [[F(0)] * d for _ in range(d)]
    for S, coef in poly.items():
        P = [[F(1) if i == j else F(0) for j in range(d)] for i in range(d)]
        for k in S:
            P = mm(P, number_op(nu, k))
        H = madd(H, P, coef)
    return H


def mv(a, v):
    return [sum(a[i][k] * v[k] for k in range(len(v))) for i in range(len(a))]


def expect(v, op):
    w = mv(op, v)
    return sum(v[i] * w[i] for i in range(len(v)))


def check_unique_ground_state_is_a_product_number_state():
    premise("singularity.class-relative-no-go-no-supplied")
    ok = True
    unique = 0
    for nu, gens in ((2, GENS2), (3, GENS3)):
        d = 1 << nu
        Ns = [number_op(nu, k) for k in range(nu)]
        for poly in gens:
            H = build(nu, poly)
            ok = ok and all(H[i][j] == 0 for i in range(d) for j in range(d) if i != j)
            diag = [H[i][i] for i in range(d)]
            low = min(diag)
            if diag.count(low) != 1:
                continue
            unique += 1
            g = diag.index(low)
            v = [F(1) if i == g else F(0) for i in range(d)]
            ok = ok and mv(H, v) == [low * x for x in v]
            # eigenvector of every N_k and of the boost generators
            for k in range(nu):
                nk = expect(v, Ns[k])
                ok = ok and mv(Ns[k], v) == [nk * x for x in v] and nk in (0, 1)
                # single-mode marginal diag(1 - nk, nk): a rank-one idempotent
                m = (1 - nk, nk)
                ok = ok and m[0] * m[1] == 0 and m[0] + m[1] == 1
                # Gibbs diag(1, q)/(1 + q) at no finite beta: q/(1+q) = nk needs q = 0 or has no solution
                if nk == 0:
                    ok = ok and all(qq / (1 + qq) != 0 for qq in (F(1, 9), F(1), F(7)))
                else:
                    ok = ok and all(1 / (1 + qq) != 0 for qq in (F(1, 9), F(1), F(7)))
            K = [[F(0)] * d for _ in range(d)]
            for k in range(nu):
                K = madd(K, madd(Ns[k], [[F(1, 2) if i == j else F(0) for j in range(d)] for i in range(d)], -1),
                         WEIGHTS[k])
            kv = expect(v, K)
            ok = ok and mv(K, v) == [kv * x for x in v]
            # product across every cut: number projectors factorise
            for size in range(1, nu):
                for left in combinations(range(nu), size):
                    right = [k for k in range(nu) if k not in left]
                    PL = build(nu, {tuple(left): 1})
                    PR = build(nu, {tuple(right): 1})
                    ok = ok and expect(v, mm(PL, PR)) == expect(v, PL) * expect(v, PR)
    _tp_rv = (ok and unique == 5); assert _tp_rv is not False, "check_unique_ground_state_is_a_product_number_state"; return _tp_rv


def check_degenerate_ground_space_selects_nothing():
    H = build(2, {(0,): 1, (1,): 1, (0, 1): -2})
    ok = [H[i][i] for i in range(4)] == [F(0), F(1), F(1), F(0)]       # |00>, |10>, |01>, |11>
    ker = GA.field_kernel(H)
    ok = ok and len(ker) == 2
    tfd = [F(4, 5), F(0), F(0), F(3, 5)]
    prod = [F(1), F(0), F(0), F(0)]
    ok = ok and mv(H, tfd) == [F(0)] * 4 and mv(H, prod) == [F(0)] * 4
    ok = ok and GA.field_rank(ker + [tfd]) == 2 and GA.field_rank(ker + [prod]) == 2
    n0 = expect(tfd, number_op(2, 0))
    ok = ok and (1 - n0, n0) == (F(16, 25), F(9, 25)) and expect(prod, number_op(2, 0)) == 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_degenerate_ground_space_selects_nothing"; return _tp_rv
