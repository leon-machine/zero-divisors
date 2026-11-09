import time
from fractions import Fraction as F
from band import *

def vir_defect(Lop, m, nn, c, v):
    a = Lop(m, Lop(nn, v)); b = Lop(nn, Lop(m, v))
    lhs = vadd(a, vsc(-1, b))
    rhs = vsc(m - nn, Lop(m + nn, v))
    if m + nn == 0:
        rhs = vadd(rhs, vsc(c * F(m**3 - m, 12), v))
    return vadd(lhs, vsc(-1, rhs))

t=time.time()
B = Band(2)
Om = {frozenset(): F(1)}
ph = B.j(0, 1, -1, Om)
ch = {frozenset([(0, 0)]): F(1)}
vecs = [Om, ph, ch, vadd(B.j(1,1,-2,Om), B.j(0,1,-1,ch))]
bad = 0
for v in vecs:
    for m in range(-3, 4):
        for nn in range(-3, 4):
            d = vir_defect(B.Lfree, m, nn, 2, v)
            if d: bad += 1
print("free 2ch bad", bad, time.time()-t)
# u(2) sugawara vs free
E = [[(0,0,F(1))],[(0,1,F(1))],[(1,0,F(1))],[(1,1,F(1))]]
Ed = [[(0,0,F(1))],[(1,0,F(1))],[(0,1,F(1))],[(1,1,F(1))]]
# su2 part + N part: u(2)_1 sug with lam: for gl(2) basis E_xy, dual E_yx; Casimir of gl(2) ad: lam = 2n=4 on su part, 0 on N; need split
su2 = [[(0,1,F(1))],[(1,0,F(1))],[(0,0,F(1)),(1,1,F(-1))]]
su2d = [[(1,0,F(1))],[(0,1,F(1))],[(0,0,F(1,2)),(1,1,F(-1,2))]]
Nn = [[(0,0,F(1)),(1,1,F(1))]]; Nd=[[(0,0,F(1,2)),(1,1,F(1,2))]]
bad=0
for v in vecs:
    for nn in range(-3,4):
        s = vadd(B.sug(su2,su2d,F(4),nn,v), B.sug(Nn,Nd,F(0),nn,v))
        if vadd(s, vsc(-1,B.Lfree(nn,v))): bad+=1
print("u2 sug = free bad", bad, time.time()-t)
