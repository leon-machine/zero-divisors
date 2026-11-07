"""GA exploration: two-channel (u(2)) currents on a generator window, helicity, flip currents, null seas.
Exact arithmetic (Fractions) with lib/GA.py. Exploration script, not the proposal check."""
import sys, itertools
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
mul, add, sub, neg, scal, sc, gen, eq = GA.mul, GA.add, GA.sub, GA.neg, GA.scal, GA.sc, GA.gen, GA.eq
OK = True
def chk(label, ok):
    global OK; OK &= bool(ok); print(("PASS " if ok else "FAIL ") + label)

class Tower:
    """kernel g1,g2 (square -1) at 0,1; mode p on plane (e,f) = (2+2p, 3+2p), squares (+1,-1)."""
    def __init__(self, nmodes, kernel=True):
        self.k = 2 if kernel else 0
        self.sq = tuple(([-1, -1] if kernel else []) + [1, -1] * nmodes)
        self.n = nmodes
        self.c = []; self.cd = []
        for p in range(nmodes):
            e, f = gen(self.k + 2 * p), gen(self.k + 2 * p + 1)
            self.c.append(scal(F(1, 2), sub(e, f)))   # annihilator w
            self.cd.append(scal(F(1, 2), add(e, f)))  # creator v
        self.J = mul(gen(0), gen(1), self.sq) if kernel else None
    def m(self, *xs):
        out = sc(1)
        for x in xs: out = mul(out, x, self.sq)
        return out
    def num(self, p): return self.m(self.cd[p], self.c[p])
    def bil(self, p, q): return self.m(self.cd[p], self.c[q])
    def comm(self, x, y): return sub(self.m(x, y), self.m(y, x))
    def dag(self, x):
        out = {}
        for b, c in x.items():
            g = len(b); s = (-1) ** (g * (g - 1) // 2) * (-1) ** sum(1 for i in b if self.sq[i] == -1)
            out[b] = c * s
        return {b: c for b, c in out.items() if c != 0}
    def proj(self, occ):
        """rank-one projector of the product state with occupations occ[p] in {0,1}."""
        P = sc(1)
        for p, o in enumerate(occ):
            P = self.m(P, self.num(p) if o else sub(sc(1), self.num(p)))
        return P
    def scal_part(self, x, y):
        """<x y>_0 without forming the product."""
        s = F(0)
        for b, c in x.items():
            d = y.get(b)
            if d is not None:
                sg, bb = GA.blade_mul(b, b, self.sq)
                s += c * d * sg
        return s
    def omega(self, P, X):
        # state with rank-one projector P on the transport planes; trace normalisation over transport planes
        return (2 ** self.n) * self.scal_part(P, X)

# ---------------------------------------------------------------- A, B: u(2) currents on a window
print("A. u(2) currents J^{ab}_m on a window of L levels, two channels: exact commutator with edge terms")
L = 3
T = Tower(2 * L)
idx = lambda a, k: a * L + (k - 1)          # channel a in {0,1}, level k in 1..L
W = range(1, L + 1)
def Jc(a, b, m):
    out = {}
    for k in W:
        if 1 <= k + m <= L: out = add(out, T.bil(idx(a, k), idx(b, k + m)))
    return out
def rhs(a, b, c, d, m, n):
    out = {}
    if b == c:
        for k in W:
            if all(1 <= x <= L for x in (k + m, k + m + n)): out = add(out, T.bil(idx(a, k), idx(d, k + m + n)))
    if a == d:
        for l in W:
            if all(1 <= x <= L for x in (l + n, l + n + m)): out = sub(out, T.bil(idx(c, l), idx(b, l + n + m)))
    return out
allok = True
for a, b, c, d in itertools.product((0, 1), repeat=4):
    for m in range(-2, 3):
        for n in range(-2, 3):
            if not eq(T.comm(Jc(a, b, m), Jc(c, d, n)), rhs(a, b, c, d, m, n)): allok = False
chk("[J^ab_m, J^cd_n] = delta_bc sum_{k,k+m,k+m+n in W} - delta_ad sum_{l,l+n,l+n+m in W}, all a,b,c,d, |m|,|n|<=2", allok)

print("B. edge-clean values (bottom h levels of each channel filled)")
h = 1
occ = [1 if k <= h else 0 for a in (0, 1) for k in W]
P = T.proj(occ)
for (a, b) in [(0, 0), (1, 1), (0, 1), (1, 0)]:
    X = T.comm(Jc(a, b, 1), Jc(b, a, -1))
    chk(f"  [J^{a}{b}_1, J^{b}{a}_-1] P = 1 P (central value m = 1 for diagonal and flip currents)", eq(T.m(X, P), P))
# flip-current commutator for m+n = -1: 2 J^3_{-1} (plus edges); its vacuum norm
X = T.comm(Jc(0, 1, 0), Jc(1, 0, -1))
Y = sub(Jc(0, 0, -1), Jc(1, 1, -1))
chk("  [J^{+-}_0, J^{-+}_-1] = J^{++}_-1 - J^{--}_-1 = 2 J^3_-1 exactly at L=3", eq(X, Y))
nrm = T.omega(P, T.m(T.dag(X), X))
chk(f"  vacuum norm^2 of [J^+_0, J^-_-1] Omega = {nrm} (canonical value 0; expected 2|m+n| = 2)", nrm == 2)
dens = T.omega(P, T.m(T.dag(Jc(0, 0, -1)), Jc(0, 0, -1)))
chk(f"  density: ||rho_-1 Omega||^2 = {dens} = central value 1", dens == 1)

# ---------------------------------------------------------------- D: helicity under the transverse rotation
print("D. transverse rotation U = prod_k (1 + (z_eps - 1) n_{eps,k}), z_+ = (3 + 4J)/5, z_- = conj")
z = {0: add(sc(F(3, 5)), scal(F(4, 5), T.J)), 1: add(sc(F(3, 5)), scal(F(-4, 5), T.J))}
U = sc(1); Ui = sc(1)
for a in (0, 1):
    for k in W:
        nn = T.num(idx(a, k))
        U = T.m(U, add(sc(1), T.m(sub(z[a], sc(1)), nn)))
        Ui = T.m(Ui, add(sc(1), T.m(sub(T.dag(z[a]), sc(1)), nn)))
chk("  U unitary for the CAR adjoint, U^dag = U^-1", eq(T.m(U, Ui), sc(1)) and eq(T.dag(U), Ui))
Ad = lambda X: T.m(U, X, Ui)
z2 = T.m(z[0], z[0])
chk("  densities rho_+-_1 invariant (helicity 0)", eq(Ad(Jc(0, 0, 1)), Jc(0, 0, 1)) and eq(Ad(Jc(1, 1, 1)), Jc(1, 1, 1)))
chk("  flip current J^{+-}_1 -> z_+^2 J^{+-}_1, z_+^2 = (-7 + 24 J)/25 (helicity 1); J^{-+} -> conj",
    eq(Ad(Jc(0, 1, 1)), T.m(z2, Jc(0, 1, 1))) and eq(Ad(Jc(1, 0, 1)), T.m(T.dag(z2), Jc(1, 0, 1))))

print("\nALL:", OK)
