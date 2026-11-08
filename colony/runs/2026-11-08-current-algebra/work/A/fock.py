"""Sparse exact Fock operators: states dict {int bitmask: Fraction}; mode i = bit i."""
from fractions import Fraction as F
import itertools

def popc(x):
    return bin(x).count("1")

def cre(i, st):
    out = {}
    b = 1 << i
    for S, c in st.items():
        if S & b: continue
        s = -1 if popc(S & (b - 1)) % 2 else 1
        T = S | b
        out[T] = out.get(T, 0) + s * c
    return {k: v for k, v in out.items() if v}

def ann(i, st):
    out = {}
    b = 1 << i
    for S, c in st.items():
        if not S & b: continue
        s = -1 if popc(S & (b - 1)) % 2 else 1
        T = S & ~b
        out[T] = out.get(T, 0) + s * c
    return {k: v for k, v in out.items() if v}

def add(*xs):
    out = {}
    for x in xs:
        for k, v in x.items():
            out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}

def scal(a, x):
    return {k: a * v for k, v in x.items() if a * v}

def bil(i, j, st):  # c*_i c_j
    return cre(i, ann(j, st))

class Win:
    def __init__(self, n, L):
        self.n, self.L = n, L
    def idx(self, x, k):
        return x * self.L + k
    def cur(self, M, m, st):
        """J(M)_m st = sum_{x,y} M[x][y] sum_k c*_{x,k} c_{y,k+m}"""
        out = {}
        for x in range(self.n):
            for y in range(self.n):
                a = M[x][y]
                if not a: continue
                for k in range(self.L):
                    if 0 <= k + m < self.L:
                        r = bil(self.idx(x, k), self.idx(y, k + m), st)
                        for s, c in r.items():
                            out[s] = out.get(s, 0) + a * c
        return {k: v for k, v in out.items() if v}
    def E(self, x, y):
        return [[1 if (a, b) == (x, y) else 0 for b in range(self.n)] for a in range(self.n)]
    def num(self, st, w):
        """sum_{x,k} w(k) n_{x,k}"""
        out = {}
        for S, c in st.items():
            v = sum(w(k) for x in range(self.n) for k in range(self.L) if S >> self.idx(x, k) & 1)
            if v: out[S] = out.get(S, 0) + v * c
        return out
