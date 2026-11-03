"""singularity.p-reduced-metric-level-reading-many: exact checks on N = 1, 2, 3 boundary modes.

The modes are built by Jordan-Wigner, v_k = Z x ... x Z x E_12 x 1 x ... x 1, as 2^N x 2^N rational
matrices; sigma_k = v_k* v_k - v_k v_k* is computed from them (the strings cancel: sigma_k is
single-site), and the mode-wise descent is the premise's parity average E_k(x) = (x + sigma_k x
sigma_k)/2.
(1) The E_k commute pairwise, are idempotent, and their composite in every order (all permutations
of the N modes) is the joint pinching E_N (keep the diagonal of the joint number basis), on all 4^N
matrix units, hence on every element.
(2) The Ad(sigma_k)-fixed subalgebra, computed as the kernel of Ad(sigma_k) - id, has dimension 4^N/2;
every matrix unit is an eigenvector of Ad(sigma_k) with eigenvalue +-1 and sigma_k is an invertible
element of the fixed algebra, which is the bimodularity step of the uniqueness argument
(sigma F(x) sigma = -F(x) forces F(x) = 0 on the odd part). range(E_k) is the fixed algebra.
(3) range(E_N) is the intersection of the mode-wise ranges, the joint-number-diagonal algebra of
dimension 2^N, while the total-parity-even algebra has dimension 4^N/2: equal at N = 1, strictly
larger for N >= 2.
The antecedent (the choice of the sheaf assembly) is a choice, not a computation, and is not checked.
"""
from fractions import Fraction as F
from itertools import permutations

import GA
import fock
from tp_premise import premise


def bit(b, k, n):
    return (b >> (n - 1 - k)) & 1


def lower(n, k):
    return fock.to_dense(fock.ann(k, n, fock.MSB), 2 ** n)


def mm(A, B):
    D = len(A)
    out = [[F(0)] * D for _ in range(D)]
    for i in range(D):
        for t in range(D):
            a = A[i][t]
            if a:
                for j in range(D):
                    if B[t][j]:
                        out[i][j] += a * B[t][j]
    return out


def tp(A):
    return [list(r) for r in zip(*A)]


def sigmas(n):
    out = []
    for k in range(n):
        v = lower(n, k)
        vs = tp(v)
        a, b = mm(vs, v), mm(v, vs)
        out.append([[a[i][j] - b[i][j] for j in range(2 ** n)] for i in range(2 ** n)])
    return out


def Ek(s, x):
    sxs = mm(mm(s, x), s)
    return [[(x[i][j] + sxs[i][j]) / 2 for j in range(len(x))] for i in range(len(x))]


def unit(D, b, c):
    M = [[F(0)] * D for _ in range(D)]
    M[b][c] = F(1)
    return M


def flat(M):
    return [x for r in M for x in r]


popcount = fock.popcount


def check_modewise_descents_commute_and_compose_to_joint_pinching():
    premise("singularity.descent-parity-average")
    perms = 0
    for n in (2, 3):
        D = 2 ** n
        S = sigmas(n)
        # single-site: sigma_k is diagonal with entry (-1)^{1 - b_k} (strings cancel)
        for k in range(n):
            assert S[k] == [[F(2 * bit(b, k, n) - 1) if b == c else F(0) for c in range(D)] for b in range(D)]
        for b in range(D):
            for c in range(D):
                x = unit(D, b, c)
                target = x if b == c else [[F(0)] * D for _ in range(D)]
                for k in range(n):
                    assert Ek(S[k], Ek(S[k], x)) == Ek(S[k], x)
                    for j in range(n):
                        assert Ek(S[j], Ek(S[k], x)) == Ek(S[k], Ek(S[j], x))
                for order in permutations(range(n)):
                    y = x
                    for k in order:
                        y = Ek(S[k], y)
                    assert y == target
                    perms += 1
    assert perms == 16 * 2 + 64 * 6, perms


def check_fixed_subalgebra_dimension_and_uniqueness_step():
    premise("singularity.descent-parity-average")
    for n in (1, 2, 3):
        D = 2 ** n
        S = sigmas(n)
        units = [(b, c) for b in range(D) for c in range(D)]
        for k in range(n):
            # matrix of Ad(sigma_k) - id on the matrix units
            cols = [flat(mm(mm(S[k], unit(D, b, c)), S[k])) for (b, c) in units]
            A = [[cols[j][i] - (1 if i == j else 0) for j in range(D * D)] for i in range(D * D)]
            fix = GA.field_kernel(A)
            assert len(fix) == D * D // 2
            # every matrix unit is a +-1 eigenvector, half of each
            signs = [cols[j][j] for j in range(D * D)]
            assert all(cols[j] == [signs[j] if i == j else 0 for i in range(D * D)] for j in range(D * D))
            assert signs.count(F(1)) == signs.count(F(-1)) == D * D // 2
            # sigma_k lies in the fixed algebra and is invertible (sigma_k^2 = 1)
            assert GA.field_rank(fix + [flat(S[k])]) == D * D // 2
            assert mm(S[k], S[k]) == [[F(1) if i == j else F(0) for j in range(D)] for i in range(D)]
            # range(E_k) is the fixed algebra
            rng = [flat(Ek(S[k], unit(D, b, c))) for (b, c) in units]
            assert GA.field_rank(rng) == D * D // 2 and GA.field_rank(rng + fix) == D * D // 2


def check_meet_is_joint_diagonal_smaller_than_parity_even():
    premise("singularity.descent-parity-average")
    dims = {}
    for n in (1, 2, 3):
        D = 2 ** n
        S = sigmas(n)
        units = [(b, c) for b in range(D) for c in range(D)]
        rows = []
        for k in range(n):
            cols = [flat(mm(mm(S[k], unit(D, b, c)), S[k])) for (b, c) in units]
            rows += [[cols[j][i] - (1 if i == j else 0) for j in range(D * D)] for i in range(D * D)]
        meet = GA.field_kernel(rows)
        diag = [flat(unit(D, b, b)) for b in range(D)]
        # range(E_N): images of all matrix units under the composite of the mode-wise descents
        pinch_range = []
        for (b, c) in units:
            y = unit(D, b, c)
            for k in range(n):
                y = Ek(S[k], y)
            pinch_range.append(flat(y))
        assert len(meet) == D and GA.field_rank(meet + diag) == D
        assert GA.field_rank(pinch_range) == D and GA.field_rank(meet + pinch_range) == D
        parity_even = sum(1 for (b, c) in units if (popcount(b) + popcount(c)) % 2 == 0)
        dims[n] = (len(meet), parity_even)
    assert dims == {1: (2, 2), 2: (4, 8), 3: (8, 32)}, dims
