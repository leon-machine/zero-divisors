"""Exploration for the Higgs-sector BRST: doublets as even elements of Cl(3,0), s phi = -g rho(c) phi."""
import sys
import time
from fractions import Fraction as F
sys.path.insert(0, '/home/claude/phys-graph/lib')
import GA  # noqa: E402

E3 = GA.sig(3, 0)
QB = [(), (1, 2), (0, 2), (0, 1)]   # basis 1, e12, e02, e01 of the even part of Cl(3,0)


def blade(b):
    return {b: F(1)} if b else GA.sc(1)


def coords(x):
    return [x.get(b, F(0)) for b in QB]


def left(T):
    return [[coords(GA.mul(T, blade(QB[j]), E3))[i] for j in range(4)] for i in range(4)]


def right(T):
    return [[coords(GA.mul(blade(QB[j]), T, E3))[i] for j in range(4)] for i in range(4)]


half = lambda x: GA.scal(F(1, 2), x)
e12 = GA.mul(GA.gen(1), GA.gen(2), E3)
e20 = GA.mul(GA.gen(2), GA.gen(0), E3)
e01 = GA.mul(GA.gen(0), GA.gen(1), E3)
for T in (half(e12), half(e20), half(e01)):
    print(left(T))
print(right(e12))
