# exact: Dirac channel coupling W = s*lam/r, s = sqrt(f), f = 1 - 2M/r, r = 2M/(1 - s^2); dW/dr_* = f dW/dr.
from fractions import Fraction as F
M, lam = F(1), F(3, 2)          # lam = j + 1/2 at j = 1
def V(s, sign):
    r = 2 * M / (1 - s * s)
    dsdr = M / (r * r * s)
    dWdr = lam * (dsdr / r - s / (r * r))
    return lam * lam * s * s / (r * r) + sign * s * s * dWdr
def Vscalar(s, l=1, mu=F(0)):
    r = 2 * M / (1 - s * s); f = s * s
    return f * (F(l * (l + 1)) / (r * r) + 2 * M / r ** 3 + mu * mu)
for s in [F(1, 10), F(1, 100), F(1, 1000), F(1, 10000)]:
    print(s, "V+/s", V(s, 1) / s, "V-/s", V(s, -1) / s, "Vscalar/s^2", Vscalar(s) / (s * s), "massive", Vscalar(s, 1, F(1, 2)) / (s * s))
print("predicted lim V+-/s = +-lam/(8M^2) =", lam / (8 * M * M))
