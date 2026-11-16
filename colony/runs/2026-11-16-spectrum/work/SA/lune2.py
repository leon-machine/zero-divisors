from fractions import Fraction as F
from lune import inner, pint, lune, w_energy_weyl, w_number_weyl, w_number_scalar
def blocked(k):
    """int over p with |p + k| <= 1 of ((r2 - r1)/2)^2 (1 - cos)/2 d^3p/(2 pi) = (1/k) int (r2-r1)^2 (k^2 - (r1-r2)^2)/16 dr1 dr2"""
    k = F(k)
    # weight polynomial in (r1, r2): (r2 - r1)^2 (k^2 - (r1 - r2)^2)/16
    w = {}
    sq = {(2, 0): F(1), (1, 1): F(-2), (0, 2): F(1)}
    for (a, b), c in sq.items():
        w[(a, b)] = w.get((a, b), 0) + c * k * k / 16
        for (d, e), f in sq.items():
            w[(a + d, b + e)] = w.get((a + d, b + e), 0) - c * f / 16
    # integrate over r1 first: swap roles: inner integrates over the second index; so transpose
    wt = {(b, a): c for (a, b), c in w.items()}          # now first index r2, second r1
    I1 = inner(wt, [k, F(-1)], [k, F(1)])                # r2 in [0, k]: r1 from k - r2 to k + r2
    I2 = inner(wt, [-k, F(1)], [k, F(1)])                # r2 in [k, 1]: r1 from r2 - k to r2 + k
    return (pint(I1, F(0), k) + pint(I2, k, F(1))) / k
def fit(fn, nodes):
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
print("blocked poly:", fit(blocked, nodes))
print("lune E weyl:", fit(lambda x: lune(w_energy_weyl(x), x), nodes))
tot = lambda x: lune(w_energy_weyl(x), x) - blocked(x)
print("total:", fit(tot, nodes))
print("k=1:", tot(F(1)), lune(w_energy_weyl(1), 1), blocked(F(1)))
