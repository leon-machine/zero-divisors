import sys, time
sys.path.insert(0, '.')
from explore7 import setup, Hf, Htot
from fock import add, scal, cre, ann
from fractions import Fraction as F
# failing vector near the edge
W, Om, facs = setup(4, 2)
for x in range(16):
    psi = cre(W.idx(x, 3), ann(W.idx(x, 1), Om))
    out = []
    for fac in facs:
        X = fac[1][0]
        m = -1
        Xp = W.cur(X, m, psi)
        lhs = add(Hf(W, fac, Xp), scal(-1, W.cur(X, m, Hf(W, fac, psi))))
        out.append(not add(lhs, scal(m, Xp)))
    print(x, out)
t = time.time()
W, Om, facs = setup(12, 6)
Z = W.E(0, 7)
psi = W.cur(Z, -1, Om)
for fac in facs:
    X = fac[1][0]
    for m in (1, -1):
        Xp = W.cur(X, m, psi)
        lhs = add(Hf(W, fac, Xp), scal(-1, W.cur(X, m, Hf(W, fac, psi))))
        print(fac[0], m, not add(lhs, scal(m, Xp)), round(time.time() - t, 1))
