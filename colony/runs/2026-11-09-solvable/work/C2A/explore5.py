import time
from fractions import Fraction as F
from band import *
t=time.time()
B = Band(NC)
fd = factor_data()
su = []; 
for x in range(NC):
    for y in range(NC):
        if x != y: su.append([(x, y, F(1))])
for x in range(NC-1):
    su.append([(x,x,F(1)),(x+1,x+1,F(-1))])
dense = []
for M in su:
    D = zero(NC)
    for (i,j,a) in M: D[i][j] += a
    dense.append(D)
print(len(su), time.time()-t)
# dual: off-diagonal E_xy dual E_yx; Cartan part dual via inverse gram
Dl = dual(dense); print("dual", time.time()-t)
lam = lam_of(dense, Dl, dense[0]); print("lam", lam, time.time()-t)
Bs, Ds = [sparse(M) for M in dense], [sparse(M) for M in Dl]
N = fd[3]
Om = {frozenset(): F(1)}
v2 = {frozenset([(0, 3)]): F(1)}
for v in (Om, v2):
    for nn in (-2, -1, 1, 2):
        s = vadd(B.sug(Bs, Ds, lam, nn, v), B.sug(N[1], N[2], N[3], nn, v))
        print(nn, not vadd(s, vsc(-1, B.Lfree(nn, v))), time.time()-t)
