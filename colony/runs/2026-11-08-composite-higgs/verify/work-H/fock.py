"""Referee H: independent occupation-number (Jordan-Wigner) model of the two-species floor.
Modes 3b + i, i = 0 (psi_1), 1 (psi_2), 2 (chi). Bitmask states. Exploration with numpy; exact checks with Fractions."""
from fractions import Fraction as F
from itertools import combinations
import numpy as np


def cre(k, s):
    if s >> k & 1:
        return None
    sign = -1 if bin(s & ((1 << k) - 1)).count('1') % 2 else 1
    return sign, s | (1 << k)


def ann(k, s):
    if not s >> k & 1:
        return None
    sign = -1 if bin(s & ((1 << k) - 1)).count('1') % 2 else 1
    return sign, s & ~(1 << k)


def apply_word(word, s):
    """word = [(kind, mode)] applied right to left, kind 'c' or 'a'."""
    c = 1
    for kind, k in reversed(word):
        r = (cre if kind == 'c' else ann)(k, s)
        if r is None:
            return None
        c *= r[0]
        s = r[1]
    return c, s


def op_terms(nb, which):
    """list of (coef, word). S*S, B_a*B_a with S = sum_b a0 a1? use proposal convention:
    S = sum w1 w2 = sum a_0 a_1 ; S* = sum a_1^dag a_0^dag ; B_a = sum a_a a_2 ; B_a* = a_2^dag a_a^dag."""
    t = []
    if which == 'SS':
        for b in range(nb):
            for c in range(nb):
                t.append((1, [('c', 3*b+1), ('c', 3*b+0), ('a', 3*c+0), ('a', 3*c+1)]))
    if which in ('B0', 'B1'):
        a = int(which[1])
        for b in range(nb):
            for c in range(nb):
                t.append((1, [('c', 3*b+2), ('c', 3*b+a), ('a', 3*c+a), ('a', 3*c+2)]))
    return t


def basis(nb, nums):
    out = []
    for A in combinations(range(nb), nums[0]):
        for B in combinations(range(nb), nums[1]):
            for C in combinations(range(nb), nums[2]):
                s = 0
                for b in A: s |= 1 << (3*b)
                for b in B: s |= 1 << (3*b+1)
                for b in C: s |= 1 << (3*b+2)
                out.append(s)
    return sorted(out)


def matrix(nb, nums, Kp, Kc, GS, GD, exact=False):
    bs = basis(nb, nums)
    idx = {s: i for i, s in enumerate(bs)}
    n = len(bs)
    zero = F(0) if exact else 0.0
    M = [[zero] * n for _ in range(n)] if exact else np.zeros((n, n))
    terms = [(-GS, w) for _, w in op_terms(nb, 'SS')] + [(-GD, w) for _, w in op_terms(nb, 'B0')] + \
            [(-GD, w) for _, w in op_terms(nb, 'B1')]
    for j, s in enumerate(bs):
        kin = Kp * (nums[0] + nums[1]) + Kc * nums[2]
        if exact:
            M[j][j] += kin
        else:
            M[j, j] += kin
        for cf, w in terms:
            r = apply_word(w, s)
            if r is None:
                continue
            i = idx[r[1]]
            if exact:
                M[i][j] += cf * r[0]
            else:
                M[i, j] += cf * r[0]
    return bs, M


def inertia(A):
    """exact (pos, neg, zero) of a symmetric Fraction matrix via LDL with pivoting by symmetric swap
    (Sylvester); zero diagonal handled by 2x2 congruence."""
    A = [row[:] for row in A]
    n = len(A)
    pos = neg = zer = 0
    alive = list(range(n))
    while alive:
        piv = next((i for i in alive if A[i][i] != 0), None)
        if piv is None:
            pair = None
            for i in alive:
                for j in alive:
                    if j != i and A[i][j] != 0:
                        pair = (i, j)
                        break
                if pair:
                    break
            if pair is None:
                zer += len(alive)
                break
            i, j = pair
            # row/col i += row/col j
            for k in range(n):
                A[i][k] += A[j][k]
            for k in range(n):
                A[k][i] += A[k][j]
            continue
        d = A[piv][piv]
        if d > 0:
            pos += 1
        else:
            neg += 1
        alive.remove(piv)
        for i in alive:
            if A[i][piv] != 0:
                f = A[i][piv] / d
                for k in alive:
                    if A[piv][k] != 0:
                        A[i][k] -= f * A[piv][k]
    return pos, neg, zer
