import sys, time
sys.path.insert(0, 'colony/runs/2026-11-27-null-surface-three/work/shear')
from pw import *
x0 = (F(1, 2), F(1, 3), F(-1, 4), F(1, 5))
w = [[[F(3), F(2), F(1)], [F(5, 2), F(-1)]], [[F(5, 2), F(-1)], [F(-3), F(-2), F(-1)]]]
W_ = Wave(w, [[0, 0], [0, 0]], x0, 1)
fld = W_.fld
t, x, y, z = W_.X
du = W_.du
wj = [[series_jet(w[i][j], du) for j in range(2)] for i in range(2)]
H = F(1, 2) * (wj[0][0] * x * x + 2 * wj[0][1] * x * y + wj[1][1] * y * y)
gradH = {(mu,): H.d(mu) * ETA[mu] for mu in range(D) if H.d(mu)}       # e^mu d_mu H
Nv = {(0,): F(1), (3,): F(1)}
B = gtg.wedge(gradH, Nv, S)
print("grad H ^ n :", gtg.m_val(B))
for mu in range(D):
    print(mu, "Om", gtg.m_val(fld.Om[mu]), " om", gtg.m_val(fld.om[mu]))
