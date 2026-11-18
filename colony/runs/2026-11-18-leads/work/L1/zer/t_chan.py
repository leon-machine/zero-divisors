import sys, time
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as F
from sym import A, LF, substitute
from closed import even_parts
from t_conv import r, lam, w, M, f, L, den, V, Dstar, zer, radial, moncrief

Ks, Hs, H1s = LF.sym("K"), LF.sym("H"), LF.sym("H1")
rhsK = -((r - 3) / (r * r * f)) * Ks + Hs / r - (L / (2 * r * r * w)) * H1s.d(0)
rhsH = rhsK + (H1s.d(0) - (2 / (r * r)) * Hs) / f
rhsH1 = (Hs.d(0) + Ks.d(0)) / f - (2 / (r * r * f)) * H1s
RHS = {"K": rhsK, "H": rhsH, "H1": rhsH1}

def rule(s):
    name, p, q = s
    if name not in RHS:
        return None
    if p >= 2:
        return LF({(name, p - 2, q): -w})
    if q >= 1:
        x = RHS[name]
        for _ in range(p):
            x = x.d(0)
        for _ in range(q - 1):
            x = x.d(1)
        return x
    return None

def red(x):
    return substitute(x, rule)

def show(x):
    return {s: (y.n, y.d) for s, y in sorted(x.c.items())}

def proportional(x, y):
    """x = mu y for some mu in the fraction field (cross products vanish); returns True/False."""
    keys = sorted(set(x.c) | set(y.c))
    z0 = A.const(0)
    for i in keys:
        for j in keys:
            if (x.c.get(i, z0) * y.c.get(j, z0) - x.c.get(j, z0) * y.c.get(i, z0)).n:
                return False
    return True

t0 = time.time()
eqs = radial(Hs, H1s, Hs, Ks)
R = {k: red(e) for k, e in eqs.items()}
for k in sorted(R):
    print(k, sorted(R[k].c))
Fc = R["E7"]
print("F =", show(Fc))
for k in ("E1", "E5", "E7"):
    print(k, "prop to F:", proportional(R[k], Fc), "nonzero:", bool(R[k]))
Ft = red(Fc.d(0))
Fr = red(Fc.d(1))
print("dF/dr symbols:", sorted(Fr.c), " prop to F:", proportional(Fr, Fc))
Psi = moncrief(Hs, Ks)
zr = red(zer(Psi))
print("Zerilli[Psi] reduced symbols:", sorted(zr.c), "prop to F:", proportional(zr, Fc), "zero:", not zr)
# reconstruction against the field
def rec(Phi):
    Kr = (lam * (lam + 1) * r * r + 3 * lam * r + 6) / (r * r * den) * Phi + f * Phi.d(1)
    Hr = (-(lam * lam * (lam + 1) * r ** 3 + 3 * lam * lam * r * r + 9 * lam * r + 9) / (r * r * den * den) * Phi
          + (lam * r * r - lam * r + 3) / (r * den) * Phi.d(1) + (r - 2) * Phi.d(1).d(1))
    H1r = r * Phi.d(0).d(1) + (lam * r * r - 3 * lam * r - 3) / ((r - 2) * den) * Phi.d(0)
    return Kr, Hr, H1r
Kr, Hr, H1r = rec(Psi)
dK = red((lam + 1) * Ks - Kr)
dH = red((lam + 1) * Hs - Hr)
dH1 = red((lam + 1) * H1s - H1r)
print("K diff:", sorted(dK.c), proportional(dK, Fc), not dK)
print("H diff:", sorted(dH.c), proportional(dH, Fc), not dH)
print("H1 diff:", sorted(dH1.c), proportional(dH1, Ft), not dH1)
print("Ft", sorted(Ft.c))
print("time", time.time() - t0)
