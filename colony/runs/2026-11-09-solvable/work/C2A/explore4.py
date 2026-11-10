import time
from fractions import Fraction as F
from band import *
t=time.time()
fd = factor_data()
B = Band(NC)
so = []
one = [[F(int(i == j)) for j in range(NC)] for i in range(NC)]
for a in range(NM):
    for b in range(NM):
        M = rep(e5(a,b))
        if a == b: M = lin((1, M), (F(-1,2), one))
        so.append(M)
for a in range(NM):
    for b in range(a+1, NM):
        so.append(rep(e5(a,b), "cc")); so.append(rep(e5(a,b), "aa"))
print(len(so), all(tr(M)==0 for M in so))
D = dual(so)
lam = lam_of(so, D, so[3])
print("lam so10", lam, 2*F(45)/(2+lam))
Bs, Ds = [sparse(M) for M in so], [sparse(M) for M in D]
Om = {frozenset(): F(1)}
v2 = {frozenset([(0, 3)]): F(1)}
v3 = B.j(5, 9, -2, Om)
N = fd[3]
bad = 0
for v in (Om, v2, v3):
    for nn in range(-2, 3):
        s = vadd(B.sug(Bs, Ds, lam, nn, v), B.sug(N[1], N[2], N[3], nn, v))
        if vadd(s, vsc(-1, B.Lfree(nn, v))): bad += 1
print("Lfree = Lso10 + LN bad", bad, time.time()-t)
