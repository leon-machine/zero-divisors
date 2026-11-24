# float exploration only (not evidence): the thermal test along the ground conic
from math import exp, pi, sqrt
def G(delta, lam):
    s = 0.0
    for k in range(0, 60):
        for a in (k + delta, k + 1 - delta):
            x = lam * a
            if x < 700:
                s += a / (exp(x) + 1.0)
    return s
def T(delta):
    r2 = 1 - 12 * (delta - 0.5) ** 2
    r = sqrt(r2)
    return -r2 / 24 + G(delta, 2 * pi / r)
dmin = 0.5 - 1 / sqrt(12)
print("dmin", dmin)
import sys
prev = None
N = 4000
zeros = []
vals = []
for i in range(1, N + 1):
    d = dmin + (0.5 - dmin) * i / N
    t = T(d)
    vals.append((d, t))
    if prev is not None and (prev[1] < 0) != (t < 0):
        zeros.append((prev[0], d))
    prev = (d, t)
print("sign changes", zeros)
for d in (0.22, 0.23, 0.24, 0.245, 0.25, 0.255, 0.27, 0.29, 0.31, 0.33, 1/3, 0.34, 0.36, 0.4, 0.45, 0.48, 0.5):
    print(d, T(d))
# extremes between zeros
import itertools
def ext(lo, hi):
    seg = [v for v in vals if lo < v[0] < hi]
    return min(seg, key=lambda v: v[1]), max(seg, key=lambda v: v[1])
print(ext(dmin, 0.25)); print(ext(0.25, 1/3)); print(ext(1/3, 0.5))
h = 1e-4
for d in (0.25, 1/3):
    print("slope", d, (T(d + h) - T(d - h)) / (2 * h))
print("curv at 1/2", (T(0.5 - 2*h) - 2 * T(0.5 - h) + T(0.5)) / h**2, (T(0.5-0.01))/(0.01**2)*2, (T(0.45))/(0.05**2)*2)
print("---- second derivative and slope profile (floats)")
def d1(d, h=1e-5): return (T(d + h) - T(d - h)) / (2 * h)
def d2(d, h=1e-4): return (T(d + h) - 2 * T(d) + T(d - h)) / h**2
for d in (0.2146, 0.22, 0.23, 0.24, 0.246, 0.25, 0.254, 0.26, 0.28, 0.3, 0.32, 0.3233, 1/3, 0.3433, 0.36, 0.386, 0.4, 0.42, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.4999):
    print(round(d, 4), "T=%.3e" % T(d), "T'=%.4e" % d1(d), "T''=%.4e" % d2(d))
