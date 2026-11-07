"""SA work: spin and statistics on a tower level Cl(N, N+2). Exact (Fractions, GA)."""
import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA

OK = True


def chk(label, ok):
    global OK
    OK &= bool(ok)
    print(("PASS " if ok else "FAIL ") + label)


def level(N):
    """kernel g1 = 0, g2 = 1 (square -1); plane k: e = 2 + 2k (+1), f = 3 + 2k (-1)."""
    s = tuple([-1, -1] + [1, -1] * N)
    mul = lambda x, y: GA.mul(x, y, s)
    J = mul(GA.gen(0), GA.gen(1))
    v = [GA.add(GA.scal(F(1, 2), GA.gen(2 + 2 * k)), GA.scal(F(1, 2), GA.gen(3 + 2 * k))) for k in range(N)]
    w = [GA.add(GA.scal(F(1, 2), GA.gen(2 + 2 * k)), GA.scal(F(-1, 2), GA.gen(3 + 2 * k))) for k in range(N)]
    n = [mul(v[k], w[k]) for k in range(N)]
    Gam = GA.sc(1)
    for k in range(N):
        Gam = mul(Gam, mul(GA.gen(2 + 2 * k), GA.gen(3 + 2 * k)))
    I = GA.sc(1)
    for i in range(len(s)):
        I = mul(I, GA.gen(i))
    return s, mul, J, v, w, n, Gam, I


def dag(x, s):
    out = {}
    for b, c in x.items():
        g = len(b)
        sg = (-1) ** (g * (g - 1) // 2)
        for i in b:
            if s[i] == -1:
                sg = -sg
        out[b] = sg * c
    return {b: c for b, c in out.items() if c != 0}


def comm(mul, x, y):
    return GA.sub(mul(x, y), mul(y, x))


def acomm(mul, x, y):
    return GA.add(mul(x, y), mul(y, x))


