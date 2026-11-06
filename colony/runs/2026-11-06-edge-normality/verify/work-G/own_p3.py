# Own route for proposal 3.
from fractions import Fraction as F
from math import comb, factorial, sin, tan, cos, pi
import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA
# (a) N commuting square-zero steps with nonzero product already in Cl(N,N) (Jordan-Wigner-twisted null vectors)
for N in (2, 3):
    S = GA.sig(N, N)
    v = [GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(N + i))) for i in range(N)]
    w = [GA.scal(F(1, 2), GA.sub(GA.gen(i), GA.gen(N + i))) for i in range(N)]
    par = [GA.sub(GA.mul(v[j], w[j], S), GA.mul(w[j], v[j], S)) for j in range(N)]   # 1 - 2 w_j v_j
    bs = []
    for i in range(N):
        b = v[i]
        for j in range(i):
            b = GA.mul(b, par[j], S)
        bs.append(b)
    for b in bs: assert GA.is_zero(GA.mul(b, b, S))
    for b in bs:
        for c in bs: assert GA.commutes(b, c, S)
    prod = GA.sc(1); top = GA.sc(1)
    for b in bs:
        prod = GA.mul(prod, GA.add(GA.sc(1), b), S); top = GA.mul(top, b, S)
    assert not GA.is_zero(top)
    eps = GA.add(*bs); expo = {}; pw = GA.sc(1)
    for k in range(N + 1):
        if k: pw = GA.mul(pw, eps, S)
        expo = GA.add(expo, GA.scal(F(1, factorial(k)), pw))
    assert GA.is_zero(GA.mul(pw, eps, S)) and GA.eq(prod, expo)
    print(f"Cl({N},{N}): {N} commuting square-zero steps, product nonzero, prod(1+b) = exp(sum b)")
# (b) Archimedes numerics by an independent float route (illustration, not evidence)
for k in range(1, 7):
    n = 2 ** (k + 1)
    L, U = n * sin(pi / n), n * tan(pi / n)
    if k == 1: assert abs(L * L - 8) < 1e-12 and abs(U - 4) < 1e-12
print("k=6: L, U =", round(128 * sin(pi / 128), 5), round(128 * tan(pi / 128), 5),
      " 4^6 (U-L) =", round(4096 * 128 * (tan(pi / 128) - sin(pi / 128)), 4), " pi^3/8 =", round(pi ** 3 / 8, 4))
# (c) tan coefficients: odd denominators to degree 61, and the closed form v_2 = s_2(n) - 1 >= 0
N = 61
sinc = [F(0)] * (N + 1); cosc = [F(0)] * (N + 1)
for k in range(N + 1):
    if k % 2: sinc[k] = F((-1) ** ((k - 1) // 2), factorial(k))
    else: cosc[k] = F((-1) ** (k // 2), factorial(k))
inv = [F(0)] * (N + 1); inv[0] = 1 / cosc[0]
for m in range(1, N + 1):
    inv[m] = -sum(cosc[j] * inv[m - j] for j in range(1, m + 1)) / cosc[0]
tanc = [sum(sinc[j] * inv[m - j] for j in range(m + 1)) for m in range(N + 1)]
def v2(x):
    x = F(x); a, b, v = x.numerator, x.denominator, 0
    while a % 2 == 0: a //= 2; v += 1
    while b % 2 == 0: b //= 2; v -= 1
    return v
for m in range(1, N + 1, 2):
    n = (m + 1) // 2
    assert tanc[m].denominator % 2 == 1
    assert v2(tanc[m]) == bin(n).count("1") - 1, (m, v2(tanc[m]))
print("tan coefficients odd-denominator through degree", N, "; v_2 of the x^(2n-1) coefficient = s_2(n) - 1")
d21 = tanc[21].denominator
print("deg-21 denominator", d21, "== 3^9 5^4 7^3 11 13 17 19:", d21 == 3**9 * 5**4 * 7**3 * 11 * 13 * 17 * 19)
