"""Referee R2: own exact sparse-matrix helpers (independent of lib/fock.py and of the author's code).

Convention chosen to differ from lib/fock.py: MSB basis index (mode 0 most significant) and the
Jordan-Wigner string over the modes with HIGHER label: a_k^dag |n> = (-1)^(n_{k+1}+...+n_{m-1}) |n + e_k>.
Matrices are dicts {(row, col): Fraction}. Everything exact.
"""
from fractions import Fraction as F


def bit(s, k, m):
    return (s >> (m - 1 - k)) & 1


def cre(k, m):
    M = {}
    for s in range(2 ** m):
        if bit(s, k, m) == 0:
            sign = (-1) ** sum(bit(s, i, m) for i in range(k + 1, m))
            M[(s | (1 << (m - 1 - k)), s)] = F(sign)
    return M


def dag(A):
    return {(j, i): c for (i, j), c in A.items()}   # rational entries


def mul(A, B):
    rows = {}
    for (i, j), c in B.items():
        rows.setdefault(i, []).append((j, c))
    out = {}
    for (i, k), a in A.items():
        for (j, b) in rows.get(k, ()):
            out[(i, j)] = out.get((i, j), F(0)) + a * b
    return {k: v for k, v in out.items() if v != 0}


def add(*As):
    out = {}
    for A in As:
        for k, v in A.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def sc(c, A):
    c = F(c)
    return {k: c * v for k, v in A.items()} if c != 0 else {}


def eye(m):
    return {(s, s): F(1) for s in range(2 ** m)}


def mprod(*As):
    out = As[0]
    for A in As[1:]:
        out = mul(out, A)
    return out


def apply(A, x):
    out = {}
    for (i, j), c in A.items():
        if j in x:
            out[i] = out.get(i, F(0)) + c * x[j]
    return {k: v for k, v in out.items() if v != 0}


def ip(x, y):
    return sum(c * y.get(k, F(0)) for k, c in x.items())


def vadd(*xs):
    out = {}
    for x in xs:
        for k, v in x.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def vsc(c, x):
    c = F(c)
    return {k: c * v for k, v in x.items()} if c != 0 else {}


class Alg:
    """v_j, w_j, e_j = v_j + w_j, f_j = v_j - w_j on m rungs (e^2 = 1, f^2 = -1, e^dag = e, f^dag = -f)."""

    def __init__(self, m):
        self.m = m
        self.v = [cre(k, m) for k in range(m)]
        self.w = [dag(x) for x in self.v]
        self.e = [add(a, b) for a, b in zip(self.v, self.w)]
        self.f = [add(a, sc(-1, b)) for a, b in zip(self.v, self.w)]
        self.I = eye(m)
        self.on = [mul(a, b) for a, b in zip(self.v, self.w)]
        self.off = [mul(b, a) for a, b in zip(self.v, self.w)]

    def vac(self):
        return {0: F(1)}

    def ket(self, occ):
        """Occupation basis vector with occupied set occ (no sign convention issues: a basis vector)."""
        s = 0
        for k in occ:
            s |= 1 << (self.m - 1 - k)
        return {s: F(1)}


def is_even_op(A, m):
    return all(bin(i).count("1") % 2 == bin(j).count("1") % 2 for (i, j) in A)
