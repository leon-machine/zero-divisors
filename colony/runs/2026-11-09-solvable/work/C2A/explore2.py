import time
from fractions import Fraction as F
from band import *

def comm_op(A, Bop, v):
    return vadd(A(Bop(v)), vsc(-1, Bop(A(v))))

t=time.time()
fd = factor_data()
for d in fd: print(d[0], d[3], d[4], 2*F(d[4])/(2+d[3]))
B = Band(NC)
Om = {frozenset(): F(1)}
X = fd[0][1][0]
v1 = B.J(fd[1][1][0], -1, Om)   # su2 excitation
v2 = {frozenset([(0, 3)]): F(1)}  # one particle in channel 3
v3 = B.j(5, 9, -2, Om)
vecs = [Om, v1, v2, v3]
print("setup", time.time()-t)
res = {}
for (name, Bs, Ds, lam, dim) in fd:
    c = 2*F(dim)/(2+lam)
    L = lambda nn, v, Bs=Bs, Ds=Ds, lam=lam: B.sug(Bs, Ds, lam, nn, v)
    bad = 0
    for v in vecs:
        for m in range(-2, 3):
            for nn in range(-2, 3):
                if m >= nn: continue
                lhs = vadd(L(m, L(nn, v)), vsc(-1, L(nn, L(m, v))))
                rhs = vsc(m-nn, L(m+nn, v))
                if m+nn == 0: rhs = vadd(rhs, vsc(c*F(m**3-m,12), v))
                if vadd(lhs, vsc(-1, rhs)): bad += 1
    print(name, "vir bad", bad, time.time()-t)
