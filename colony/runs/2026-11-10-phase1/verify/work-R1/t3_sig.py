from fractions import Fraction as F
from itertools import combinations
from rcl import *
def anal(p, q):
    n = p + q; A = Cl([1] * p + [-1] * q); N = 1 << n
    sgn = lambda a, b: A.bmul(a, b)[0]
    comm = lambda a, b: sgn(a, b) == sgn(b, a)
    sa = [b for b in range(1, N) if sgn(b, b) == 1]          # self-adjoint non-scalar blades
    # blade CHSH configuration search: A1,A2 anticommute, B1,B2 anticommute, cross commute
    found = None
    for a1, a2 in combinations(sa, 2):
        if comm(a1, a2): continue
        cands = [b for b in sa if comm(b, a1) and comm(b, a2)]
        for b1, b2 in combinations(cands, 2):
            if not comm(b1, b2): found = (a1, a2, b1, b2); break
        if found: break
    J = N - 1
    central = (n % 2 == 1) and sgn(J, J) == 1
    # frame: sa blades modulo J
    if central:
        F_ = [b for b in sa if b != J and b < (b ^ J)] if True else None
        # choose representatives: one of {b, b^J}; both are s.a. when J central s.a.
        F_ = sorted({min(b, b ^ J) for b in sa if b != J})
    else:
        F_ = sa
    pairwise_anti = all(not comm(a, b) for a, b in combinations(F_, 2))
    prods = [a ^ b for a, b in combinations(F_, 2)]
    if central:
        cls = lambda b: min(b, b ^ J)
        allc = [cls(b) for b in [0] + F_ + prods]
    else:
        allc = [0] + F_ + prods
    indep = len(set(allc)) == len(allc)
    return len(sa), central, len(F_), pairwise_anti, indep, found
def matsize(p, q):
    n = p + q; d = (p - q) % 8
    dimD = {0: 1, 1: 1, 2: 1, 3: 2, 4: 4, 5: 4, 6: 4, 7: 2}[d]; two = 2 if d in (1, 5) else 1
    k2 = (1 << n) // (dimD * two); k = int(round(k2 ** .5)); assert k * k == k2
    return k
excl = []
for n in range(1, 8):
    for p in range(n, -1, -1):
        q = n - p
        nsa, central, fs, anti, indep, found = anal(p, q)
        k = matsize(p, q)
        frame_ok = anti and indep
        tag = "EXCLUDED" if found is None else "config"
        if found is None: excl.append((p, q))
        print((p, q), "k=%d" % k, "sa blades=%d" % nsa, "J central s.a.=%s" % central, "|F|=%d" % fs, "frame anticommuting+independent=%s" % frame_ok, tag, found if found else "")
        assert (found is None) == (k <= 2), (p, q)
        assert (found is None) <= frame_ok
print("excluded:", excl, len(excl))
