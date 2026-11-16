"""scratch: exact particle-hole structure factors of a filled ball (k_F = 1) by bipolar integration.
d^3p = (2 pi / k) r1 r2 dr1 dr2, r1 = |p|, r2 = |p + k|, |r1 - r2| <= k <= r1 + r2.  Results in units of 2 pi."""
from fractions import Fraction as F

def padd(p, q):
    n = max(len(p), len(q)); o = [F(0)] * n
    for i, c in enumerate(p): o[i] += c
    for i, c in enumerate(q): o[i] += c
    return o
def pmul(p, q):
    o = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            o[i + j] += a * b
    return o
def ppow(p, n):
    o = [F(1)]
    for _ in range(n): o = pmul(o, p)
    return o
def pint(p, lo, hi):
    return sum(c * (hi ** (i + 1) - lo ** (i + 1)) / (i + 1) for i, c in enumerate(p))

def inner(poly2, lo, hi):
    """integrate sum c r1^i r2^j over r2 from lo(r1) to hi(r1) (lo, hi polynomials in r1): polynomial in r1"""
    out = [F(0)]
    for (i, j), c in poly2.items():
        t = padd(ppow(hi, j + 1), [-x for x in ppow(lo, j + 1)])
        t = [x * c / (j + 1) for x in t]
        out = padd(out, [F(0)] * i + t)
    return out

def lune(weight, k):
    """int over p in ball, p + k outside, of weight(r1, r2) d^3p / (2 pi), for 0 < k <= 2; weight includes r1 r2 / k"""
    k = F(k)
    one = [F(1)]
    if k <= 1:
        I = inner(weight, one, [k, F(1)])            # r2 from 1 to r1 + k
        return pint(I, 1 - k, F(1)) / k
    I1 = inner(weight, [k, F(-1)], [k, F(1)])        # r1 in [0, k-1]: r2 from k - r1 to k + r1
    I2 = inner(weight, one, [k, F(1)])               # r1 in [k-1, 1]
    return (pint(I1, F(0), k - 1) + pint(I2, k - 1, F(1))) / k

def w_number_scalar(): return {(1, 1): F(1)}
def w_number_weyl(k):   # r1 r2 (1 + cos)/2, cos = (r1^2 + r2^2 - k^2)/(2 r1 r2)
    k = F(k); return {(1, 1): F(1, 2), (2, 0): F(1, 4), (0, 2): F(1, 4), (0, 0): -k * k / 4}
def w_energy_scalar():  # r1 r2 ((r1 + r2)/2)^2
    return {(3, 1): F(1, 4), (2, 2): F(1, 2), (1, 3): F(1, 4)}
def w_energy_weyl(k):   # ((r1+r2)/2)^2 * [r1 r2/2 + (r1^2 + r2^2 - k^2)/4]
    k = F(k)
    base = {(2, 0): F(1, 4), (1, 1): F(1, 2), (0, 2): F(1, 4)}
    fac = {(1, 1): F(1, 2), (2, 0): F(1, 4), (0, 2): F(1, 4), (0, 0): -k * k / 4}
    out = {}
    for (a, b), c in base.items():
        for (d, e), f in fac.items():
            out[(a + d, b + e)] = out.get((a + d, b + e), 0) + c * f
    return out

if __name__ == "__main__":
    for k in (F(1, 10), F(1, 2), F(1), F(3, 2), F(2)):
        vol = F(2, 3)   # ball volume / (2 pi) = (4 pi/3)/(2 pi)
        SN = lune(w_number_scalar(), k) / vol
        print("k", k, "S_N scalar", SN, "formula", F(3, 4) * k - k ** 3 / 16)
        print("   S_N weyl", lune(w_number_weyl(k), k) / vol)
        print("   E scalar", lune(w_energy_scalar(), k), " E weyl", lune(w_energy_weyl(k), k))
    # fit polynomials in k for k <= 1 by Lagrange on rational nodes
    def fit(fn, nodes):
        # solve Vandermonde exactly
        n = len(nodes)
        M = [[x ** j for j in range(n)] + [fn(x)] for x in nodes]
        for c in range(n):
            p = next(r for r in range(c, n) if M[r][c] != 0)
            M[c], M[p] = M[p], M[c]
            M[c] = [x / M[c][c] for x in M[c]]
            for r in range(n):
                if r != c and M[r][c] != 0:
                    f = M[r][c]; M[r] = [x - f * y for x, y in zip(M[r], M[c])]
        return [M[i][n] for i in range(n)]
    nodes = [F(i, 12) for i in range(1, 10)]
    print("E scalar poly (k<=1):", fit(lambda x: lune(w_energy_scalar(), x), nodes))
    print("E weyl poly (k<=1):", fit(lambda x: lune(w_energy_weyl(x), x), nodes))
    print("N weyl poly (k<=1):", fit(lambda x: lune(w_number_weyl(x), x), nodes))
    nodes2 = [1 + F(i, 12) for i in range(1, 10)]
    print("E scalar poly (1<k<=2):", fit(lambda x: lune(w_energy_scalar(), x), nodes2))
    print("E weyl poly (1<k<=2):", fit(lambda x: lune(w_energy_weyl(x), x), nodes2))
    print("N weyl poly (1<k<=2):", fit(lambda x: lune(w_number_weyl(x), x), nodes2))
