"""Exact fermion Fock space on a finite set of modes (sparse vectors, integer or Fraction coefficients).
A state is {occupation bitmask: coefficient}. Modes are indexed 0..n-1 in a fixed order; the sign of a
creation or annihilation is (-1)^(number of occupied modes of lower index)."""
from fractions import Fraction as F


def _sign(mask, i):
    return -1 if bin(mask & ((1 << i) - 1)).count('1') % 2 else 1


def cr(i, st):
    out = {}
    for m, c in st.items():
        if not (m >> i) & 1:
            out[m | (1 << i)] = c * _sign(m, i)
    return out


def an(i, st):
    out = {}
    for m, c in st.items():
        if (m >> i) & 1:
            out[m & ~(1 << i)] = c * _sign(m, i)
    return out


def add(a, b, s=1):
    out = dict(a)
    for m, c in b.items():
        v = out.get(m, 0) + s * c
        if v == 0:
            out.pop(m, None)
        else:
            out[m] = v
    return out


def scal(x, a):
    return {m: x * c for m, c in a.items() if x * c != 0}


def ip(a, b):
    return sum(c * b.get(m, 0) for m, c in a.items())


def apply(op, st):
    """op: list of (coefficient, [(kind, mode), ...]) with the word applied right to left."""
    out = {}
    for coef, word in op:
        cur = st
        for kind, i in reversed(word):
            cur = cr(i, cur) if kind == 'c' else an(i, cur)
            if not cur:
                break
        if cur:
            out = add(out, scal(coef, cur))
    return out


def dagger(op):
    return [(coef, [('a' if k == 'c' else 'c', i) for k, i in reversed(word)]) for coef, word in op]
