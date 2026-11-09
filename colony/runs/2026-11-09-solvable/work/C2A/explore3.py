import time
from fractions import Fraction as F
from band import *
t=time.time()
fd = factor_data()
B = Band(NC)
Om = {frozenset(): F(1)}
v1 = B.J(fd[1][1][0], -1, Om)
v2 = {frozenset([(0, 3)]): F(1)}
v3 = B.j(5, 9, -2, Om)
vecs = [Om, v1, v2, v3]
def Lf(i, nn, v):
    d = fd[i]; return B.sug(d[1], d[2], d[3], nn, v)
def Lc(nn, v):
    out = B.Lfree(nn, v)
    for i in range(4): out = vadd(out, vsc(-1, Lf(i, nn, v)))
    return out
cc = 16 - sum(2*F(d[4])/(2+d[3]) for d in fd)
print("cc", cc)
bad=0
for v in vecs:
    for m in range(-2,3):
        for nn in range(-2,3):
            if m >= nn: continue
            lhs = vadd(Lc(m, Lc(nn, v)), vsc(-1, Lc(nn, Lc(m, v))))
            rhs = vsc(m-nn, Lc(m+nn, v))
            if m+nn == 0: rhs = vadd(rhs, vsc(cc*F(m**3-m,12), v))
            if vadd(lhs, vsc(-1, rhs)): bad += 1
print("coset vir bad", bad, time.time()-t)
bad=0
for v in vecs[:3]:
    for m in (-2,-1,1,2):
        for nn in (-1,0,1):
            for i in range(4):
                X = fd[i][1][0]
                d = vadd(Lc(m, B.J(X, nn, v)), vsc(-1, B.J(X, nn, Lc(m, v))))
                if d: bad+=1
print("coset-current bad", bad, time.time()-t)
bad=0
for v in vecs[:2]:
    for m in (-2,1):
        for nn in (-1,2):
            for i in range(4):
                d = vadd(Lc(m, Lf(i, nn, v)), vsc(-1, Lf(i, nn, Lc(m, v))))
                if d: bad+=1
                for k in range(4):
                    if k==i: continue
                    d = vadd(Lf(k, m, Lf(i, nn, v)), vsc(-1, Lf(i, nn, Lf(k, m, v))))
                    if d: bad+=1
print("coset-Lf, Lf-Lf' bad", bad, time.time()-t)
# norms on Omega
for i in range(4):
    w = Lf(i, -2, Om); print(fd[i][0], sum(c*c for c in w.values()))
w = Lc(-2, Om); print("coset", sum(c*c for c in w.values()))
w = Lc(-3, Om); print("coset L-3 norm", sum(c*c for c in w.values()), "expect", cc*2)
