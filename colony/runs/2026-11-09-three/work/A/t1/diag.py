from fractions import Fraction as F
def bd(k, a, m):
    """boundary of g^a e_k: dict {(k-1, b): coeff}"""
    out = {}
    if k == 0: return out
    if k % 2 == 1:
        out[(k-1, (a+1) % m)] = out.get((k-1, (a+1) % m), 0) + 1
        out[(k-1, a)] = out.get((k-1, a), 0) - 1
    else:
        for c in range(m):
            out[(k-1, (a+c) % m)] = out.get((k-1, (a+c) % m), 0) + 1
    return {x: v for x, v in out.items() if v}
def add(A, B, s=1):
    C = dict(A)
    for x, v in B.items():
        C[x] = C.get(x, 0) + s*v
        if not C[x]: del C[x]
    return C
def delta(k, a, m, variant=0):
    """Delta(g^a e_k): dict {(p, a1, q, b1): coeff}"""
    out = {}
    for p in range(k+1):
        q = k - p
        if p % 2 == 0:
            terms = [(0, 0)]
        elif q % 2 == 0:
            terms = [(0, 1)]
        else:
            terms = [(i, j) for i in range(m) for j in range(i+1, m)]
        for (i, j) in terms:
            out[(p, (a+i) % m, q, (a+j) % m)] = 1
    return out
def bd2(T, m):
    out = {}
    for (p, a, q, b), v in T.items():
        for (pp, aa), c in bd(p, a, m).items():
            out = add(out, {(pp, aa, q, b): v*c})
        for (qq, bb), c in bd(q, b, m).items():
            out = add(out, {(p, a, qq, bb): v*c*(-1)**p})
    return out
def delta_of_chain(ch, m):
    out = {}
    for (k, a), c in ch.items():
        out = add(out, {x: c*v for x, v in delta(k, a, m).items()})
    return out
if __name__ == '__main__':
    for m in (2, 3, 4, 5):
        for k in range(0, 8):
            lhs = bd2(delta(k, 0, m), m); rhs = delta_of_chain(bd(k, 0, m), m)
            print(m, k, lhs == rhs)
