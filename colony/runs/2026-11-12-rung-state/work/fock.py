"""Fock module of the ladder pairs (Chevalley action): v_j by wedge, w_j by contraction.
Vectors: dict {sorted tuple of occupied rungs: Fraction}. Words: tuple of ('v'|'w', j), applied right to left."""
from fractions import Fraction as F
import random

def vadd(*xs):
    out = {}
    for x in xs:
        for k, c in x.items():
            out[k] = out.get(k, F(0)) + c
    return {k: c for k, c in out.items() if c != 0}

def vscal(c, x):
    return {k: F(c) * cc for k, cc in x.items()} if c != 0 else {}

def ap_v(j, x):
    out = {}
    for S, c in x.items():
        if j in S: continue
        sgn = -1 if sum(1 for i in S if i < j) % 2 else 1
        T = tuple(sorted(S + (j,)))
        out[T] = out.get(T, F(0)) + sgn * c
    return {k: c for k, c in out.items() if c != 0}

def ap_w(j, x):
    out = {}
    for S, c in x.items():
        if j not in S: continue
        sgn = -1 if sum(1 for i in S if i < j) % 2 else 1
        T = tuple(i for i in S if i != j)
        out[T] = out.get(T, F(0)) + sgn * c
    return {k: c for k, c in out.items() if c != 0}

def ap_word(word, x):
    for (t, j) in reversed(word):
        x = ap_v(j, x) if t == 'v' else ap_w(j, x)
        if not x: break
    return x

def ap(el, x):
    """el: dict {word: coefficient}."""
    return vadd(*[vscal(c, ap_word(wd, x)) for wd, c in el.items()])

def ip(x, y):
    return sum(c * y.get(k, F(0)) for k, c in x.items())

def emul(a, b):
    out = {}
    for wa, ca in a.items():
        for wb, cb in b.items():
            out[wa + wb] = out.get(wa + wb, F(0)) + ca * cb
    return {k: c for k, c in out.items() if c != 0}

def eadd(*xs):
    out = {}
    for x in xs:
        for k, c in x.items():
            out[k] = out.get(k, F(0)) + c
    return {k: c for k, c in out.items() if c != 0}

def escal(c, a):
    return {k: F(c) * cc for k, cc in a.items()} if c != 0 else {}

def edag(a):
    return {tuple(('w' if t == 'v' else 'v', j) for (t, j) in reversed(wd)): c for wd, c in a.items()}

ONE = {(): F(1)}
def V(j): return {(('v', j),): F(1)}
def W(j): return {(('w', j),): F(1)}
def ON(j): return emul(V(j), W(j))
def OFF(j): return emul(W(j), V(j))
