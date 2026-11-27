import sys, time
sys.path.insert(0, 'colony/runs/2026-11-27-null-surface-three/work/shear')
from pw import *
x0 = (F(1, 2), F(1, 3), F(-1, 4), F(1, 5))
w = [[[F(3), F(2), F(1)], [F(5, 2), F(-1)]], [[F(5, 2), F(-1)], [F(-3), F(-2), F(-1)]]]
S0 = [[F(2, 3), F(-1, 5)], [F(-1, 5), F(3, 7)]]
t0 = time.time()
order = 3
W_ = Wave(w, S0, x0, order)
print("built", time.time() - t0)
qk = W_.QK()
print("Q(K) order", qk.order, "zero to order", [jet_zero(qk, o) for o in range(0, order + 2)])
print("K value", gtg.m_val(W_.K))
print("k (background) value", [x.v for x in W_.k], " n.k =", sum(NLOW[m] * W_.k[m].v for m in range(D)))
th = W_.theta()
print("theta", th.v, "tr S", W_.Sj[0][0].v + W_.Sj[1][1].v, "theta jet order", th.order)
print("theta - trS zero:", [jet_zero(th - W_.Sj[0][0] - W_.Sj[1][1], o) for o in range(order + 1)])
tb2 = W_.trB2()
S2 = sum((W_.Sj[i][j] * W_.Sj[j][i] for i in range(2) for j in range(2)), ZJ)
print("trB2 - trS2 zero:", [jet_zero(tb2 - S2, o) for o in range(order + 1)])
dth = W_.along(th)
trw = series_jet(w[0][0], W_.du) + series_jet(w[1][1], W_.du)
foc = dth + tb2 - trw
print("focusing residual zero:", [jet_zero(foc, o) for o in range(order)], " trw", trw.v)
x1, x2 = W_.connecting()
print("lie zero:", [[jet_zero(c, order - 1) for c in W_.lie(x)] for x in (x1, x2)])
print("tangent:", [sum((x[mu] * W_.phi.d(mu) for mu in range(D)), ZJ).v for x in (x1, x2)])
r4 = W_.rho4()
detE = W_.Ej[0][0] * W_.Ej[1][1] - W_.Ej[0][1] * W_.Ej[1][0]
print("rho4 - detE^2 zero:", [jet_zero(r4 - detE * detE, o) for o in range(order + 1)], r4.v)
print("d rho4 = 2 theta rho4:", [jet_zero(W_.along(r4) - 2 * th * r4, o) for o in range(order)])
print("time", time.time() - t0)
