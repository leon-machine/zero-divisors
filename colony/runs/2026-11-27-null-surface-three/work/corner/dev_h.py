from dev import *
from fractions import Fraction as F
globals().update({k: v for k, v in vars(ck).items() if not k.startswith("__")})
t = X[0]
h, k = sample_gauge_field(29, 2, 5), sample_gauge_field(53, 2, 5)
w1 = pomega(boost_variation(h), k); w2 = pomega(h, boost_variation(k)); w0 = pomega(h, k)
nd = lambda w: w[0] - w[3]
print("gauge fields: n.omega(Lh,k) + n.omega(h,Lk) = d_lam(lam n.omega(h,k)) on N:", on_N(nd(w1) + nd(w2) - dn(t * nd(w0))) == {})
# generic fields, generic gauge
h, k = sample_field(3), sample_field(4)
w1 = pomega(boost_variation(h), k); w2 = pomega(h, boost_variation(k)); w0 = pomega(h, k)
d = nd(w1) + nd(w2) - dn(t * nd(w0))
print("generic:", on_N(d) == {})
# full covariance: omega(Lh,k)+omega(h,Lk) = L_xi omega (vector Lie derivative) 
xi = XIB
Lw = [jsum(xi[a] * w0[m].d(a) - w0[a] * xi[m].d(a) for a in range(D)) for m in range(D)]
print("covariance of omega:", vzero(vadd(vadd(w1, w2), Lw, -1)))
# n.(L omega) = xi.grad(n.w) - (w.grad xi).n ; on N..
