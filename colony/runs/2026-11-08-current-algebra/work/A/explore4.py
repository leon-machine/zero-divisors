import sys
sys.path.insert(0, '.')
from embed import *
from fractions import Fraction as F

def gram(basis16):
    return [[tr(mm(A, B)) for B in basis16] for A in basis16]

def inv(G):
    k = len(G)
    A = [row[:] + [F(int(i == j)) for j in range(k)] for i, row in enumerate(G)]
    for c in range(k):
        p = next(r for r in range(c, k) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(k):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [row[k:] for row in A]

for name, B5 in (('su2', su2), ('su3', su3), ('Y', [Y5])):
    B16 = [rep(X) for X in B5]
    G16 = gram(B16)
    G5 = [[tr(mm(A, B)) for B in B5] for A in B5]
    ratio = set(G16[i][j] / G5[i][j] for i in range(len(B5)) for j in range(len(B5)) if G5[i][j])
    zero_ok = all(G16[i][j] == 0 for i in range(len(B5)) for j in range(len(B5)) if G5[i][j] == 0)
    # lambda: sum_a ad(X^a) ad(X_a) on X_0 in 5-dim (rep-independent)
    Gi = inv(G16)
    dual = [[[sum(Gi[a][b] * B5[b][i][j] for b in range(len(B5))) for j in range(5)] for i in range(5)] for a in range(len(B5))]
    if len(B5) > 1:
        Z = B5[0]
        acc = [[F(0)] * 5 for _ in range(5)]
        for a in range(len(B5)):
            t = comm(dual[a], comm(B5[a], Z))
            acc = [[acc[i][j] + t[i][j] for j in range(5)] for i in range(5)]
        lam = set(acc[i][j] / Z[i][j] for i in range(5) for j in range(5) if Z[i][j])
    else:
        lam = {0}
    print(name, 'tr16/tr5', ratio, zero_ok, 'lambda', lam, 'trace', [tr(M) for M in B16])
B = [rep(X) for X in su2 + su3 + [Y5]]
print('cross traces zero', all(tr(mm(rep(X), rep(Yy))) == 0 for X in su2 for Yy in su3 + [Y5]) and all(tr(mm(rep(X), rep(Y5))) == 0 for X in su3))
Yd = [rep(Y5)[i][i] for i in range(16)]
print('Y diag', Yd, 'trY2', sum(y*y for y in Yd), 'trY3', sum(y**3 for y in Yd))
