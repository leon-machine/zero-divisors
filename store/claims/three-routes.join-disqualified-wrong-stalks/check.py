"""three-routes.join-disqualified-wrong-stalks: exact checks.

The U-ledger on a finite truncation of N = 2, 3, 4 points, one mode per point: Jordan-Wigner v_x as exact
integer matrices on 2^N states (CAR checked), v_x* the transpose, sigma_x = v_x* v_x - v_x v_x*, and
Ad sigma_x(X) = sigma_x X sigma_x (sigma_x^2 = 1).
(i) For y != x, Ad sigma_x fixes v_y and v_y*: every generator lies in the fixed algebra of some other point,
    so the join J(U) contains all of them; the normal-ordered monomials in the generators have rank 4^N
    (exact), so J(U) is the whole ledger and the two-ledger discrepancy against it (ledger / J) is zero.
    The pointwise fixed algebras have dimension 4^N / 2 each (sigma_x is diagonal, checked, so Ad sigma_x - 1
    multiplies the matrix unit E_ij by s_i s_j - 1 and the fixed algebra is spanned by the E_ij with s_i s_j = 1).
(ii) v_y is in J(U) but Ad sigma_y(v_y) = -v_y: J contains elements odd at y, for every y, so J is not
    contained in the pointwise even algebra (the stalk algebra A_y^+) at any point, while the meet of the
    fixed algebras (the sections even at every point) is the joint diagonal, of dimension 2^N.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

POINTS = [2, 3, 4]


def _zeros(d):
    return [[0] * d for _ in range(d)]


def _eye_i(d):
    return [[1 if i == j else 0 for j in range(d)] for i in range(d)]


def _imm(A, B):
    d = len(A)
    out = _zeros(d)
    for i in range(d):
        Ai = A[i]
        Oi = out[i]
        for t in range(d):
            a = Ai[t]
            if a:
                Bt = B[t]
                for j in range(d):
                    if Bt[j]:
                        Oi[j] += a * Bt[j]
    return out


def _iadd(*Ms):
    d = len(Ms[0])
    return [[sum(M[i][j] for M in Ms) for j in range(d)] for i in range(d)]


def _iscal(c, A):
    return [[c * x for x in row] for row in A]


def _itr(A):
    return [list(r) for r in zip(*A)]


def _comm(A, B):
    return _iadd(_imm(A, B), _iscal(-1, _imm(B, A)))


def _is_zero(A):
    return all(x == 0 for row in A for x in row)


def annihilators(nmodes):
    """Jordan-Wigner annihilators on 2^nmodes states; bit i of a basis index = occupation of mode i."""
    d = 2 ** nmodes
    out = []
    for i in range(nmodes):
        M = _zeros(d)
        for b in range(d):
            if b >> i & 1:
                M[b ^ (1 << i)][b] = (-1) ** bin(b & ((1 << i) - 1)).count("1")
        out.append(M)
    return out


def ledger(N):
    a = annihilators(N)
    ad = [_itr(x) for x in a]
    sig = [_iadd(_imm(ad[x], a[x]), _iscal(-1, _imm(a[x], ad[x]))) for x in range(N)]
    return a, ad, sig


def _ad(s, X):
    return _imm(s, _imm(X, s))


def _flat(X):
    return [F(x) for row in X for x in row]


def fixed_algebra_dim(s):
    """sigma is diagonal (checked), so Ad sigma - 1 multiplies the matrix unit E_ij by s_i s_j - 1:
    the fixed algebra is spanned by the E_ij with s_i s_j = 1."""
    d = len(s)
    diag = all(s[i][j] == 0 for i in range(d) for j in range(d) if i != j)
    return diag, sum(1 for i in range(d) for j in range(d) if s[i][i] * s[j][j] == 1)


def check_join_is_the_whole_ledger():
    ok = True
    for N in POINTS:
        a, ad, sig = ledger(N)
        d = 2 ** N
        ok = ok and all(_iadd(_imm(a[i], ad[j]), _imm(ad[j], a[i])) == (_eye_i(d) if i == j else _zeros(d))
                        for i in range(N) for j in range(N))
        ok = ok and all(_imm(s, s) == _eye_i(d) for s in sig)
        for x in range(N):
            for y in range(N):
                if x != y:
                    ok = ok and _ad(sig[x], a[y]) == a[y] and _ad(sig[x], ad[y]) == ad[y]
            diag, dim = fixed_algebra_dim(sig[x])
            ok = ok and diag and dim == d * d // 2
        monos = []
        for ex in product((0, 1), repeat=2 * N):
            M = _eye_i(d)
            for x in range(N):
                if ex[2 * x]:
                    M = _imm(M, ad[x])
                if ex[2 * x + 1]:
                    M = _imm(M, a[x])
            monos.append(_flat(M))
        ok = ok and GA.rank_of_vectors(monos) == 4 ** N
    _tp_rv = (ok); assert _tp_rv is not False, "check_join_is_the_whole_ledger"; return _tp_rv


def check_join_has_elements_odd_at_each_point():
    premise("three-routes.stalks-are-pointwise-metric-levels")
    ok = True
    for N in POINTS:
        a, ad, sig = ledger(N)
        d = 2 ** N
        for y in range(N):
            others = [x for x in range(N) if x != y]
            ok = ok and all(_ad(sig[x], a[y]) == a[y] for x in others)          # v_y in J
            ok = ok and _ad(sig[y], a[y]) == _iscal(-1, a[y])                  # odd at y
            ok = ok and fixed_algebra_dim(sig[y])[1] < 4 ** N
        meet = [(i, j) for i in range(d) for j in range(d)
                if all(sig[x][i][i] * sig[x][j][j] == 1 for x in range(N))]
        ok = ok and len(meet) == 2 ** N and all(i == j for i, j in meet)
    _tp_rv = (ok); assert _tp_rv is not False, "check_join_has_elements_odd_at_each_point"; return _tp_rv
