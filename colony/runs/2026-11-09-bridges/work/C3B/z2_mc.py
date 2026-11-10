# scratch sanity only (floats): sector mean entropy against the closed form
import numpy as np
from fractions import Fraction as F
import math
rng = np.random.default_rng(1)
def sector_entropy(m, n, N=20000):
    # sector = (m/2 x n/2) + (m/2 x n/2)
    tot = 0.0
    for _ in range(N):
        z = rng.normal(size=(2, m//2, n//2)) + 1j*rng.normal(size=(2, m//2, n//2))
        z /= np.sqrt((abs(z)**2).sum())
        S = 0.0
        for blk in z:
            ev = np.linalg.svd(blk, compute_uv=False)**2
            ev = ev[ev > 1e-300]
            S -= (ev*np.log(ev)).sum()
        tot += S
    return tot/N
def closed(m, n):
    return sum(F(1, k) for k in range(n//2+1, m*n//2+1)) - F(m-2, 2*n)
def page(m, n):
    return sum(F(1, k) for k in range(n+1, m*n+1)) - F(m-1, 2*n)
for m, n in ((2,2),(2,4),(4,4),(4,8),(8,8)):
    c = closed(m,n); p = page(m,n)
    print(m, n, "MC", round(sector_entropy(m,n),4), "closed", c, float(c), "page", float(p), "diff", p and (c-p), "bounds", F(1,2*m*n), float(c-p), F(1,2*(m*n+1))+F(1,2*n*(n+1)))
