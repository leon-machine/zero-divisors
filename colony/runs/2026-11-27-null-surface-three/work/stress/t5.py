# plane wave along nbar: h = f+(nbar.x) eps+ + fx(nbar.x) epsx ; full G2 in three parametrisations
import time
from engine import *
from sol import *
from t4 import EPSP, EPSX, pairm, NB, NV

def wave(X, jp, jx):
    """profiles with prescribed 2-jets (f, f', f'') at phi0 plus cubic terms"""
    t, x, y, z = X
    phi = t + z                      # nbar.x
    phi0 = X0[0] + X0[3]
    u = phi - phi0
    fp = u * 0 + jp[0] + u * jp[1] + u * u * F(jp[2], 2) + u * u * u * F(1, 7)
    fx = u * 0 + jx[0] + u * jx[1] + u * u * F(jx[2], 2) - u * u * u * F(1, 5)
    return madd([[EPSP[m][k] * fp for k in range(D)] for m in range(D)], [[EPSX[m][k] * fx for k in range(D)] for m in range(D)])

X = labels(X0, 2)
jp, jx = (F(2, 3), F(-1, 2), F(3, 4)), (F(1, 5), F(2, 7), F(-1, 3))
h = wave(X, jp, jx)
H1 = mscal(F(-1, 2), h)
kk = const_mat(outer_map(NB, NB))        # a -> (a.nbar) nbar
hp2 = 2 * (jp[1] ** 2 + jx[1] ** 2)       # <h', h'>
hh2 = 2 * 2 * (jp[1] ** 2 + jp[0] * jp[2] + jx[1] ** 2 + jx[0] * jx[2])   # <h,h>'' = 2 (f^2)'' summed = 4 (f'^2 + f f'')
for name, c2, coef in (("hb", None, F(1, 2)), ("s", F(1), F(-1, 2)), ("exp", F(1, 2), F(0))):
    t0 = time.time()
    H2 = None if c2 is None else mscal(c2, mmul(H1, H1))
    G1, G2, _ = einstein_orders(H1, H2)
    want = mscal(F(1, 4) * (hp2 + coef * hh2), mval(kk))
    print(name, "G1=0", all(not x for r in G1 for x in r), "G2 = 1/4 (<h',h'> + c <h,h>'') (a.k) k:",
          mval(G2) == mval(want), time.time() - t0)
