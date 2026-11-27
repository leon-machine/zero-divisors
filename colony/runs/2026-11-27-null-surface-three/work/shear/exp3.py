import sys, time
sys.path.insert(0, 'colony/runs/2026-11-27-null-surface-three/work/shear')
from pw import *
x0 = (F(1, 2), F(1, 3), F(-1, 4), F(1, 5))
w1 = [[[F(3), F(2), F(1)], [F(5, 2), F(-1)]], [[F(5, 2), F(-1)], [F(-3), F(-2), F(-1)]]]
for order in (6, 8):
    eps = F(3, 2)
    w = [[[eps * c for c in w1[i][j]] for j in range(2)] for i in range(2)]
    t0 = time.time()
    W_ = Wave(w, [[0, 0], [0, 0]], x0, order)
    t1 = time.time()
    th = W_.theta()
    tb2 = W_.trB2()
    dth = W_.along(th)
    foc = dth + tb2
    print(order, "build", t1 - t0, "rest", time.time() - t1, jet_zero(foc, order - 1), "Q(K)", jet_zero(W_.QK(), order))
    # theta as a series in du: coefficient of t^k
    print([th.coeff((k, 0, 0, 0)) for k in range(order + 1)])
    print("depends only on u:", all(e[1] == 0 and e[2] == 0 for e in th.c))
