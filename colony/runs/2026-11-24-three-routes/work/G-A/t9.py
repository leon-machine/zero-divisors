import time
from fractions import Fraction as F
from spin2 import *
exec(open('t6.py').read().split("t0 = time.time()")[0].replace("L = int(sys.argv[1])", "L = 9"))
t0 = time.time()
phi, deg = solve_poisson({x: -v/2 for x, v in rho.items()})
kap = T.einstein({(c, x): v for x, v in phi.items() for c in range(3)})
print(time.time()-t0)
for k in [(0, (7, 4, 4)), (5, (1, 2, 6))]:
    w = 1 if k[0] < 3 else 2
    De = T.ham({k: F(1)})
    t1 = time.time()
    u, dg = solve_poisson(De)
    # lam = (1/(4 w)) D^T u : value on f = (1/(4w)) sum_y u(y) (D f)(y)
    val = sum(u.get(y, 0) * v for y, v in rho.items()) / (4*w)
    print(k, "deg", dg, "time", time.time()-t1, "lam(f)", val, "kap", kap.get(k, 0), val == kap.get(k, 0))
