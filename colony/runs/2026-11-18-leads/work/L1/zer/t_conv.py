import sys, time
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as F
from sym import A, LF, substitute
from closed import even_parts

r, lam, w = A.var(0), A.var(1), A.var(2)
M = F(1)
f = (r - 2) / r
L = 2 * lam + 2
den = lam * r + 3
V = f * (2 * lam * lam * (lam + 1) * r ** 3 + 6 * lam * lam * r * r + 18 * lam * r + 18) / (r ** 3 * den * den)

def Dstar(u):
    return f * u.d(1)

def zer(u):
    return u.d(0).d(0) - Dstar(Dstar(u)) + V * u

def radial(H0, H1, H2, K):
    p = even_parts(H0, H1, H2, K, r, f, M)
    return dict(E1=p["c00"] - L * p["d00"], E2=p["c01"] - L * p["d01"], E3=p["c02"], E4=p["c12"],
                E5=p["c11"] - L * p["d11"], E6=H0 - H2, E7=p["c22"] - L * p["dK"])

def moncrief(H2, K):
    return r * (K + (f * r / den) * (H2 - r * K.d(1)))

Psi = LF.sym("Psi")
Zs = LF.sym("Z")
# reconstruction (candidate)
Kr = (lam * (lam + 1) * r * r + 3 * lam * r + 6) / (r * r * den) * Psi + f * Psi.d(1)
Hr = (-(lam * lam * (lam + 1) * r ** 3 + 3 * lam * lam * r * r + 9 * lam * r + 9) / (r * r * den * den) * Psi
      + (lam * r * r - lam * r + 3) / (r * den) * Psi.d(1) + (r - 2) * Psi.d(1).d(1))
H1r = r * Psi.d(0).d(1) + (lam * r * r - 3 * lam * r - 3) / ((r - 2) * den) * Psi.d(0)

# rule: Psi_tt = D*D* Psi - V Psi + Z
base = Dstar(Dstar(Psi)) - V * Psi + Zs
def rule(s):
    name, p, q = s
    if name == "Psi" and p >= 2:
        x = base
        for _ in range(p - 2):
            x = x.d(0)
        for _ in range(q):
            x = x.d(1)
        return x
    return None

t0 = time.time()
eqs = radial(Hr, H1r, Hr, Kr)
for k, e in sorted(eqs.items()):
    red = substitute(e, rule)
    psi_part = {s: x for s, x in red.c.items() if s[0] == "Psi"}
    z_part = {s: x for s, x in red.c.items() if s[0] == "Z"}
    print(k, "Psi-remainder:", sorted(psi_part), " Z-part:", {s: (x.n, x.d) for s, x in z_part.items()})
mm = substitute(moncrief(Hr, Kr) - Psi, rule)
print("Moncrief - Psi:", {s: (x.n, x.d) for s, x in mm.c.items()})
print("time", time.time() - t0)
