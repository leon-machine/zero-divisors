"""Referee P: does J a(f) J = (-1)^{n0} Gamma a*(W f) hold when the particle number r differs from n0?
Case 1 + 2 modes, r = 2: phi1 = (3/5) e0 + (4i/5) e1, phi2 = e2 (a filled complement mode).
Work on the cyclic subspace K = M Omega (4-dim inside 8-dim), exact Gaussian rationals."""
import sys, importlib.util
LAB = "/home/claude/phys-graph"
sys.path.insert(0, LAB + "/lib")
import tp_premise, GA
tp_premise.configure(LAB + "/store")
src = LAB + "/proposals/synthesis.modular-data-on-a-generator-fix-neither-the-translation-lift-nor-the-sign-of-i/check.py"
spec = importlib.util.spec_from_file_location("c2", src); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
import fock
from fractions import Fraction as F
QI = GA.QI; I = GA.QI_I; Z0 = QI(0); ONE = QI(1)

def run(orb, block, comp, W, sigma):
    M = len(block) + len(comp); d = 2 ** M
    a = [m.dense(fock.ann(k, M), d) for k in range(M)]; ad = [m.mdag(x) for x in a]
    Om = m.slater(orb, M)
    per = [[m.eye(d), a[k], ad[k], m.mmul(ad[k], a[k])] for k in block]
    mons = [m.eye(d)]
    for opts in per:
        mons = [m.mmul(x, o) for x in mons for o in opts]
    Gam = m.dense(fock.parity(M), d)
    def ad_of(vec):
        A = [[Z0] * d for _ in range(d)]
        for l, c in enumerate(vec):
            A = m.madd(A, m.msc(c, ad[comp[l]]))
        return A
    phi_a = [m.msc(sigma, m.mmul(Gam, ad_of([W[l][j] for l in range(len(comp))]))) for j in range(len(block))]
    phi_ad = [m.mdag(x) for x in phi_a]
    phis = [[m.eye(d), phi_a[j], phi_ad[j], m.mmul(phi_ad[j], phi_a[j])] for j in range(len(block))]
    images = [m.eye(d)]
    for opts in phis:
        images = [m.mmul(x, o) for x in images for o in opts]
    n = len(mons)
    basis = [m.apply(x, Om) for x in mons]                 # x_i Omega
    adj = [m.apply(m.mdag(x), Om) for x in mons]           # x_i^* Omega
    img = [m.apply(x, Om) for x in images]                 # phi(x_i) Omega
    # coordinates in the basis: pick n independent rows
    import itertools
    B = [[basis[j][i] for j in range(n)] for i in range(d)]
    rows = None
    for cand in itertools.combinations(range(d), n):
        if m.det([B[i] for i in cand]) != Z0:
            rows = cand; break
    Bsq = [B[i] for i in rows]
    def coords(v):
        c = GA.field_solve(Bsq, [v[i] for i in rows])
        rec = [sum((B[i][j] * c[j] for j in range(n)), Z0) for i in range(d)]
        assert rec == v, "vector not in the cyclic subspace"
        return c
    Sm = [coords(v) for v in adj]   # column j: S(basis_j) coordinates (S antilinear: S sum c_j b_j = sum conj(c_j) S b_j)
    Jm = [coords(v) for v in img]
    Sm = [[Sm[j][i] for j in range(n)] for i in range(n)]
    Jm = [[Jm[j][i] for j in range(n)] for i in range(n)]
    # antilinear maps as A K; J_c S = Jm conj(Sm) (linear)
    D = m.mmul(Jm, m.mconj(Sm))
    G = [[sum((m.cj(basis[i][k]) * basis[j][k] for k in range(d)), Z0) for j in range(n)] for i in range(n)]
    GD = m.mmul(G, D)
    herm = m.meq(GD, m.mdag(GD))
    minors = [m.det([r[:k] for r in GD[:k]]) for k in range(1, n + 1)]
    pos = herm and all(x.im == 0 and x.re > 0 for x in minors)
    # J_c antiunitary on K: <Jx, Jy> = conj<x, y>: Jm^dag G Jm = conj(G)
    anti = m.meq(m.mmul(m.mmul(m.mdag(Jm), G), Jm), m.mconj(G))
    return herm, pos, anti

orb = [[QI(F(3, 5)), QI(0, F(4, 5)), Z0], [Z0, Z0, ONE]]
for s in (F(-1), F(1)):
    print("1+2 modes, r = 2, sigma =", s, "-> (J_c S Hermitian, positive, J_c antiunitary) =", run(orb, [0], [1, 2], [[I], [Z0]], s))
orb1 = [[QI(F(3, 5)), QI(0, F(4, 5)), Z0]]
for s in (F(-1), F(1)):
    print("1+2 modes, r = 1, sigma =", s, "->", run(orb1, [0], [1, 2], [[I], [Z0]], s))
