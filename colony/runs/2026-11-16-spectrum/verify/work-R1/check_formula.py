from rad_modes import *
from fractions import Fraction as F
from math import factorial
# cos x, x sin x as series in y (x^2 = y^2/3)
cosx = L({2*n: F((-1)**n, factorial(2*n))/F(3)**n for n in range(N)})
xsinx = L({2*n+2: F((-1)**n, factorial(2*n+1))/F(3)**(n+1) for n in range(N)})
C1 = cosx + xsinx; C2 = 2*cosx + xsinx
for nm, P in [('g', Pg), ('d', Pd)]:
    S = slices(P)
    for sl in ['ue','fl','co','N']:
        s = S[sl]
        z = -1*s['psi']*C1 - F(1,4)*s['delta']*cosx - s['th']*Y.inv()*C2
        print(nm, sl, z.show(6))
