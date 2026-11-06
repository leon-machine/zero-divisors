# Own route for proposal 1: blade-sign counts from the closed form, compared with the signature of the
# trace form x -> <x^2>_0 (diagonal in the blade basis, entries e_S^2) computed from the matrix model
# M_k(D) of the classification: R -> +k, C -> 0, H -> -2k (per simple summand).  Also Arf by majority,
# a GA cross-check of the closed form for n <= 6, and the Gauss sum via Gaussian integers.
from fractions import Fraction as F
from math import comb
import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA
def q_closed(k, neg): return (comb(k, 2) + neg) % 2
def gauss(p, q):
    return sum(comb(p, a) * comb(q, b) * (-1) ** q_closed(a + b, b) for a in range(p + 1) for b in range(q + 1))
def trace_sig(p, q):
    n = p + q; d = (p - q) % 8
    if d in (0, 2): k = 2 ** (n // 2); return k
    if d in (4, 6): k = 2 ** ((n - 2) // 2); return -2 * k
    if d == 1: k = 2 ** ((n - 1) // 2); return 2 * k
    if d == 5: k = 2 ** ((n - 3) // 2); return -2 * 2 * k
    return 0
def gi(p, q):  # (1 - i)(1 + i)^p (1 - i)^q in Gaussian integers, real part
    z = complex(1, -1) * complex(1, 1) ** p * complex(1, -1) ** q
    return round(z.real)
cnt = 0
for n in range(1, 15):
    for p in range(n + 1):
        q = n - p
        g = gauss(p, q)
        assert g == trace_sig(p, q) == gi(p, q), (p, q, g, trace_sig(p, q))
        cnt += 1
print("closed-form Gauss sum = trace-form signature = Gaussian-integer formula for", cnt, "signatures, n <= 14")
# GA cross-check of the closed form q(S) = C(|S|,2) + |S cap N| for n <= 6
for n in range(1, 7):
    for p in range(n + 1):
        S = GA.sig(p, n - p)
        for m in range(2 ** n):
            bl = tuple(i for i in range(n) if m >> i & 1)
            sq = GA.mul({bl: F(1)}, {bl: F(1)}, S)[()]
            neg = sum(1 for i in bl if i >= p)
            assert sq == (-1) ** q_closed(len(bl), neg)
print("GA squares agree with closed form, n <= 6")
# Arf by majority for even n vs the type
for n in range(2, 13, 2):
    for p in range(n + 1):
        q = n - p
        minus = sum(comb(p, a) * comb(q, b) for a in range(p + 1) for b in range(q + 1) if q_closed(a + b, b))
        arf = 1 if minus > 2 ** (n - 1) else 0
        assert arf == (1 if (p - q) % 8 in (4, 6) else 0)
print("Arf (majority) = 1 exactly for p - q = 4, 6 mod 8, even n <= 12")
