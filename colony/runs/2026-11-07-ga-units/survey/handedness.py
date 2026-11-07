#!/usr/bin/env python3
"""Is the (N+) sign eta the doublet handedness under i = I4?  Exact, GA.py."""
import sys
from fractions import Fraction as F
from itertools import product
sys.path.insert(0, '/home/claude/phys-graph/lib')
import GA

SQ = GA.sig(1, 3)            # g0^2 = +1, g1^2 = g2^2 = g3^2 = -1
def g(i): return GA.gen(i)
def m(*xs):
    r = GA.sc(1)
    for x in xs: r = GA.mul(r, x, SQ)
    return r
g0, g1, g2, g3 = g(0), g(1), g(2), g(3)
I4 = m(g0, g1, g2, g3)
sig1, sig3 = m(g1, g0), m(g3, g0)
Isig3 = m(I4, sig3)
BL = GA.all_blades(4)
EVEN = [b for b in BL if len(b) % 2 == 0]
NE = len(EVEN)

def vec(x):           # coordinates on the even basis
    return [x.get(b, F(0)) for b in EVEN]
def unvec(v):
    return {b: c for b, c in zip(EVEN, v) if c != 0}
def blade(b): return {tuple(b): F(1)}
def opmat(f):        # matrix of a real-linear map on Cl+
    cols = [vec(f(blade(b))) for b in EVEN]
    return [[cols[j][i] for j in range(NE)] for i in range(NE)]
def L(a): return lambda x: GA.mul(a, x, SQ)
def R(b): return lambda x: GA.mul(x, b, SQ)
def comp(f, h): return lambda x: f(h(x))
def apply(M, v): return [sum(M[i][j] * v[j] for j in range(NE)) for i in range(NE)]
def mm(A, B): return GA.mat_mul(A, B)
def meq(A, B): return GA.mat_eq(A, B)
def mneg(A): return [[-c for c in r] for r in A]
def ident(): return [[F(1) if i == j else F(0) for j in range(NE)] for i in range(NE)]

def nullspace(M):
    """Basis of {v : M v = 0} over Q (Gaussian elimination)."""
    A = [r[:] for r in M]; rows, cols = len(A), len(A[0]); piv = []; r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if A[i][c] != 0), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        A[r] = [x / A[r][c] for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                A[i] = [a - A[i][c] * b for a, b in zip(A[i], A[r])]
        piv.append(c); r += 1
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        v = [F(0)] * cols; v[f] = F(1)
        for i, c in enumerate(piv): v[c] = -A[i][f]
        basis.append(v)
    return basis

def S(k):             # S_k = {psi even : k psi = 0}; k psi is odd, so use all coordinates
    cols = [[GA.mul(k, blade(b), SQ).get(c, F(0)) for c in BL] for b in EVEN]
    M = [[cols[j][i] for j in range(NE)] for i in range(len(BL))]
    return nullspace(M)

def rotate(k, Rt):    # R k R~ / (R R~), rational Cayley rotor
    nrm = GA.mul(Rt, GA.reverse(Rt), SQ).get((), F(0))
    return GA.scal(F(1) / nrm, m(Rt, k, GA.reverse(Rt)))

def spatial_dir(k):   # n = spatial part of k relative to g0, as a vector
    return {b: c for b, c in k.items() if b != (0,)}

def is_future(k): return k.get((0,), F(0)) > 0

ks = [GA.add(g0, g3), GA.add(g0, g1), GA.add(g0, GA.neg(g2))]
for (a, bb, t) in [((1, 3), None, F(1, 2)), ((2, 3), None, F(2, 3)), ((1, 2), None, F(3, 5))]:
    Rt = GA.add(GA.sc(1), GA.scal(t, m(g(a[0]), g(a[1]))))
    ks.append(rotate(GA.add(g0, g3), Rt))
# a boosted null vector (boost rotor in the g0 g3 plane, rational): k' = lambda (g0 + g3)
ks.append(GA.scal(F(5, 3), GA.add(g0, g3)))

Gam = comp(L(I4), R(Isig3))
GamM = opmat(Gam)
LI = opmat(L(I4)); RH = opmat(R(Isig3))

# --- F3: L_I4 = -Gamma R_{I sigma3} on all of Cl+, Gamma^2 = 1
GA.check("F3 Gamma^2 = 1", meq(mm(GamM, GamM), ident()))
GA.check("F3 L_I4 = -Gamma R_Isig3", meq(LI, mneg(mm(GamM, RH))))

def restrict_eq(Aop, Bop, basis):
    return all(apply(Aop, v) == apply(Bop, v) for v in basis)

# --- F1: on S_k, L_B = 1 and L_J = -L_I4, with B the boost bivector of k and J = -I4 B
for k in ks:
    n = spatial_dir(k); n0 = k[(0,)]
    nh = GA.scal(F(1) / n0, n)                       # unit spatial direction (k null)
    B = m(nh, g0)                                    # boost bivector n g0, B^2 = 1
    J = GA.neg(m(I4, B))
    Sk = S(k)
    GA.check("F1 dim S_k = 4", len(Sk) == 4)
    GA.check("F1 L_B = 1 on S_k", restrict_eq(opmat(L(B)), ident(), Sk))
    GA.check("F1 L_J = -L_I4 on S_k", restrict_eq(opmat(L(J)), mneg(LI), Sk))

# --- F5: commutant of the left Lorentz action is the right multiplications; all commute with L_I4
gens = [opmat(L(m(g(i), g(j)))) for i in range(4) for j in range(i + 1, 4)]
rowsys = []
for G in gens:                                       # T G - G T = 0, unknowns T_ij row-major
    for i in range(NE):
        for j in range(NE):
            row = [F(0)] * (NE * NE)
            for l in range(NE):
                row[i * NE + l] += G[l][j]
                row[l * NE + j] -= G[i][l]
            rowsys.append(row)
comm = nullspace(rowsys)
GA.check("F5 commutant has dimension 8 (right multiplications)", len(comm) == 8)
ok = True
for v in comm:
    T = [v[i * NE:(i + 1) * NE] for i in range(NE)]
    ok = ok and meq(mm(T, LI), mm(LI, T))
GA.check("F5 every Lorentz-covariant map is I4-linear", ok)

# --- bits of a mode (k future, s, psi0 in S_k, psi0 a Gamma eigenvector)
def bits(k, s, psi0):
    u = [[s * c for c in r] for r in LI]               # the mode's frequency unit s L_I4
    n = spatial_dir(k); nh = GA.scal(F(1) / k[(0,)], n)
    I3 = m(g1, g2, g3)                                  # fixed spatial orientation of the reference frame
    Jn = m(I3, nh)                                      # rotation bivector about nh (right-hand rule)
    v = vec(psi0)
    LJv = apply(opmat(L(Jn)), v); uv = apply(u, v)
    h = 1 if LJv == uv else (-1 if LJv == [-c for c in uv] else 0)
    Rv = apply(RH, v)
    q = 1 if Rv == uv else (-1 if Rv == [-c for c in uv] else 0)
    Gv = apply(GamM, v)
    gm = 1 if Gv == v else (-1 if Gv == [-c for c in v] else 0)
    return s, h, q, gm

def gamma_eigvecs(k):
    Sk = S(k); out = {}
    for gm in (1, -1):
        P = [[(ident()[i][j] + gm * GamM[i][j]) / 2 for j in range(NE)] for i in range(NE)]
        vs = [apply(P, v) for v in Sk]
        vs = [v for v in vs if any(c != 0 for c in v)]
        out[gm] = unvec(vs[0])
    return out

# lock: h s and q s Gamma are constant over all modes
lock_hs, lock_q = set(), set()
for k in ks:
    for gm, psi0 in gamma_eigvecs(k).items():
        for s in (1, -1):
            s_, h, q, gm_ = bits(k, s, psi0)
            GA.check("bits defined", h != 0 and q != 0 and gm_ == gm)
            lock_hs.add(h * s); lock_q.add(q * s * gm)
GA.check("LOCK helicity times frequency sign is one constant (I4 B = J)", len(lock_hs) == 1)
GA.check("LOCK charge sign = -Gamma * s (from F3)", lock_q == {-1})
print("h*s =", lock_hs, " q*s*Gamma =", lock_q)

# --- discrete symmetries psi(x) -> a psi(Lambda^{-1} x) b
def refl_P(x): return m(g0, x, g0)
def refl_T(x): return GA.neg(m(g0, x, g0))
def refl_PT(x): return GA.neg(x)
LAMS = {'id': lambda x: x, 'P': refl_P, 'T': refl_T, 'PT': refl_PT}

def image(a, b, lamname, k, s, psi0):
    """Image of exp(-s I k.x) psi0: returns (k', s', psi0') with k' future."""
    lam = LAMS[lamname]
    kp = lam(k)                                          # theta = k . Lambda^{-1} x = (Lambda k) . x
    sp = s * (-1 if len(next(iter(a))) % 2 else 1)       # odd a anticommutes with I4
    psi = GA.mul(GA.mul(a, psi0, SQ), b, SQ)
    if not is_future(kp):
        kp = GA.neg(kp); sp = -sp
    return kp, sp, psi

results = {}
for lamname in LAMS:
    for ab in product(BL, BL):
        a, b = blade(ab[0]), blade(ab[1])
        if (len(ab[0]) + len(ab[1])) % 2: continue      # must map even to even
        good = True; rec = []
        for k in ks:
            for gm, psi0 in gamma_eigvecs(k).items():
                for s in (1, -1):
                    kp, sp, psi = image(a, b, lamname, k, s, psi0)
                    if not GA.is_zero(GA.mul(kp, psi, SQ)): good = False; break
                    s0, h0, q0, g0b = bits(k, s, psi0)
                    s1, h1, q1, g1b = bits(kp, sp, psi)
                    if 0 in (h1, q1, g1b): good = False; break
                    rec.append((s0 * s1, h0 * q0 * h1 * q1, g0b * g1b))
                if not good: break
            if not good: break
        if good:
            flips = set(rec)
            if len(flips) == 1:
                results.setdefault(lamname, set()).add((ab, flips.pop()))
            else:
                results.setdefault(lamname + '-inconsistent', set()).add(ab)

print("\nSymmetry classes: (eta flips?, chi flips?, Gamma flips?)  -1 = flips")
summary = {}
for lamname, recs in results.items():
    if lamname.endswith('inconsistent'):
        print(lamname, len(recs)); continue
    for ab, f in recs:
        summary.setdefault((lamname, f), []).append(ab)
for (lamname, f), abs_ in sorted(summary.items()):
    print(f"Lambda={lamname:3s} eta:{f[0]:+d} chi:{f[1]:+d} Gamma:{f[2]:+d}  ({len(abs_)} maps, e.g. a={abs_[0][0]} b={abs_[0][1]})")

sep = [(ln, f) for (ln, f) in summary if f[0] != f[1]]
print("\nsymmetries separating eta from chi:", sep)
named = {'P (a=b=g0)': ('P', ((0,), (0,))), 'C_H (b=sigma1)': ('id', ((), (0, 1)))}
for nm, (ln, ab) in named.items():
    hit = [f for (l2, f), lst in summary.items() if l2 == ln and ab in lst]
    print(nm, hit)
print("failures:", GA.FAILURES)
