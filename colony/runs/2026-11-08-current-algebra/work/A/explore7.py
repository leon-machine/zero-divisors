import sys, time
sys.path.insert(0, '.')
from embed import *
from explore4 import inv, gram
from fock import Win, add, scal
from fractions import Fraction as F

def setup(L, s):
    W = Win(16, L)
    Om = {sum(1 << W.idx(x, k) for x in range(16) for k in range(s)): F(1)}
    facs = []
    for name, B5, lam in (('su2', su2, F(1)), ('su3', su3, F(3, 2)), ('Y', [Y5], F(0))):
        B16 = [rep(X) for X in B5]
        Gi = inv(gram(B16))
        facs.append((name, B16, Gi, lam))
    one = [[F(int(i == j)) for j in range(16)] for i in range(16)]
    facs.append(('N', [one], [[F(1, 16)]], F(0)))
    return W, Om, facs

def Hf(W, fac, st):
    name, B16, Gi, lam = fac
    out = {}
    for q in range(0, W.L):
        for a in range(len(B16)):
            inner = W.cur(B16[a], q, st)
            if not inner: continue
            for b in range(len(B16)):
                if Gi[a][b]:
                    out = add(out, scal(Gi[a][b] * (2 if q else 1), W.cur(B16[b], -q, inner)))
    return scal(1 / (2 + lam), out)

def Htot(W, st):
    return W.num(st, lambda k: k + F(1, 2))

for L, s in ((4, 2), (6, 3), (8, 4)):
    W, Om, facs = setup(L, s)
    Z = W.E(0, 7)
    psis = [('Omega', Om), ('J(E07)_-1 Omega', W.cur(Z, -1, Om))]
    t = time.time()
    for pname, psi in psis:
        res = []
        for fac in facs:
            X = fac[1][0]
            for m in (1, -1):
                Xp = W.cur(X, m, psi)
                lhs = add(Hf(W, fac, Xp), scal(-1, W.cur(X, m, Hf(W, fac, psi))))
                ok1 = not add(lhs, scal(m, Xp))
                # coset: H - sum_f H_f
                def Hc(st):
                    out = Htot(W, st)
                    for f in facs:
                        out = add(out, scal(-1, Hf(W, f, st)))
                    return out
                cc = add(Hc(Xp), scal(-1, W.cur(X, m, Hc(psi))))
                res.append((fac[0], m, ok1, not cc))
        print(L, s, pname, res, round(time.time() - t, 1))
