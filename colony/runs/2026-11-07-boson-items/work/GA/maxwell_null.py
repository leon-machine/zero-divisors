"""STA Maxwell on a null plane: symplectic current, null flux in the gauge n.A = 0, null energy, duality = transverse
rotation on null data. Exact polynomial multivector fields over Fractions with lib/GA.py."""
import sys, itertools
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
SQ = (1, -1, -1, -1)
mul = lambda x, y: GA.mul(x, y, SQ)
add, sub, neg, scal, sc, gen, eq = GA.add, GA.sub, GA.neg, GA.scal, GA.sc, GA.gen, GA.eq
OK = True
def chk(label, ok):
    global OK; OK &= bool(ok); print(("PASS " if ok else "FAIL ") + label)
def grade(x, k): return {b: c for b, c in x.items() if len(b) == k}
g = [gen(i) for i in range(4)]
I4 = mul(mul(g[0], g[1]), mul(g[2], g[3]))
def vdot(a, b): return grade(mul(a, b), 0).get((), F(0))

# polynomial multivector fields: dict exps(4-tuple) -> multivector
def padd(*fs):
    out = {}
    for f in fs:
        for e, mv in f.items():
            out[e] = add(out.get(e, {}), mv)
    return {e: mv for e, mv in out.items() if mv}
def pmul(f, h):
    out = {}
    for e1, m1 in f.items():
        for e2, m2 in h.items():
            e = tuple(a + b for a, b in zip(e1, e2))
            out[e] = add(out.get(e, {}), mul(m1, m2))
    return {e: mv for e, mv in out.items() if mv}
def pconst(mv): return {(0, 0, 0, 0): mv} if mv else {}
def pgrade(f, k): return {e: grade(mv, k) for e, mv in f.items() if grade(mv, k)}
def pd(f, mu):
    out = {}
    for e, mv in f.items():
        if e[mu]:
            e2 = list(e); e2[mu] -= 1
            out[tuple(e2)] = add(out.get(tuple(e2), {}), scal(e[mu], mv))
    return {e: mv for e, mv in out.items() if mv}
def nabla(f):   # vector derivative: sum_mu gamma^mu d_mu, gamma^mu = gamma_mu / Q(gamma_mu)
    return padd(*[pmul(pconst(scal(F(1, SQ[mu]), g[mu])), pd(f, mu)) for mu in range(4)])
def pdn(f, n):  # directional derivative n . nabla = sum_mu n_mu d_mu, n = sum n_mu gamma_mu (components)
    return padd(*[{e: scal(n.get((mu,), 0), mv) for e, mv in pd(f, mu).items()} for mu in range(4) if n.get((mu,), 0)])
def peval(f, x):
    out = {}
    for e, mv in f.items():
        c = F(1)
        for xi, ei in zip(x, e): c *= F(xi) ** ei
        out = add(out, scal(c, mv))
    return out

# deterministic polynomial vector potentials of degree <= 2
def poly_vec(seed):
    out = {}
    mons = [e for e in itertools.product(range(3), repeat=4) if sum(e) <= 2]
    for j, e in enumerate(mons):
        mv = {}
        for mu in range(4):
            c = F(((seed * 7 + j * 3 + mu * 5) % 11) - 5, 1 + (j + mu + seed) % 3)
            if c: mv = add(mv, scal(c, g[mu]))
        if mv: out[e] = mv
    return out
A1, A2 = poly_vec(1), poly_vec(2)
F1, F2 = pgrade(nabla(A1), 2), pgrade(nabla(A2), 2)
om = padd(pgrade(pmul(F1, A2), 1), {e: neg(m) for e, m in pgrade(pmul(F2, A1), 1).items()})
div_om = pgrade(nabla(om), 0)
dF1, dF2 = pgrade(nabla(F1), 1), pgrade(nabla(F2), 1)
rhs = padd(pgrade(pmul(dF1, A2), 0), {e: neg(m) for e, m in pgrade(pmul(dF2, A1), 0).items()})
chk("1. div(F1.A2 - F2.A1) = (div F1).A2 - (div F2).A1 for generic polynomial A1, A2 (F.A = <F A>_1)",
    padd(div_om, {e: neg(m) for e, m in rhs.items()}) == {})
chk("   the identity is not empty: div F1 != 0 for these test fields", dF1 != {})

# null plane with generators along n = g0 + g3, second null m = g0 - g3, transverse g1, g2
n = add(g[0], g[3]); mn = sub(g[0], g[3])
def gauge_vec(seed):
    """A = a n + A1 g1 + A2 g2 with polynomial a, A1, A2: n.A = 0 identically."""
    base = poly_vec(seed)
    out = {}
    for e, mv in base.items():
        a = mv.get((0,), F(0)); x1 = mv.get((1,), F(0)); x2 = mv.get((2,), F(0))
        out[e] = add(scal(a, n), scal(x1, g[1]), scal(x2, g[2]))
    return {e: mv for e, mv in out.items() if mv}
B1, B2 = gauge_vec(3), gauge_vec(4)
chk("2. gauge fields satisfy n.A = 0 identically", all(vdot(n, mv) == 0 for f in (B1, B2) for mv in f.values()))
G1, G2 = pgrade(nabla(B1), 2), pgrade(nabla(B2), 2)
omg = padd(pgrade(pmul(G1, B2), 1), {e: neg(m) for e, m in pgrade(pmul(G2, B1), 1).items()})
flux = pgrade(pmul(pconst(n), omg), 0)
def perp(f): return {e: grade(add(scal(mv.get((1,), 0), g[1]), scal(mv.get((2,), 0), g[2])), 1) for e, mv in f.items() if mv.get((1,), 0) or mv.get((2,), 0)}
tr = padd(pgrade(pmul(perp(pdn(B1, n)), perp(B2)), 0), {e: neg(m) for e, m in pgrade(pmul(perp(pdn(B2, n)), perp(B1)), 0).items()})
chk("   null flux n.omega = d_n A1perp . A2perp - d_n A2perp . A1perp identically (no n-component, no transverse derivative)",
    padd(flux, {e: neg(m) for e, m in tr.items()}) == {})
nF = pgrade(pmul(pconst(n), G1), 1)
chk("   n.F = d_n A identically in this gauge", padd(nF, {e: neg(m) for e, m in pdn(B1, n).items()}) == {})

# gauge invariance of the transverse null data (n.F)perp under A -> A + grad chi
chi = {(1, 1, 0, 0): sc(3), (0, 2, 1, 0): sc(-2), (2, 0, 0, 1): sc(5), (0, 0, 1, 1): sc(1)}
Ach = padd(A1, pgrade(nabla(chi), 1))
chk("3. F and so (n.F)perp are gauge invariant: grad ^ grad chi = 0", pgrade(nabla(Ach), 2) == F1)

# algebraic identities for a generic constant bivector F
Fb = {}
for j, b in enumerate(itertools.combinations(range(4), 2)):
    Fb[b] = F((j * 5 + 3) % 7 - 3, 1 + j % 2)
Fb = {b: c for b, c in Fb.items() if c}
nFb = grade(mul(n, Fb), 1)
Tn = scal(F(-1, 2), mul(mul(Fb, n), Fb))   # T(n) = -1/2 F n F
Eperp = add(scal(nFb.get((1,), 0), g[1]), scal(nFb.get((2,), 0), g[2]))
chk("4. n.(n.F) = 0, so n.F = alpha n + Eperp (no m-component)", vdot(n, nFb) == 0 and
    eq(nFb, add(scal(F(1, 2) * vdot(mn, nFb), n), Eperp)))
chk("   null energy n.T(n) = -Eperp^2 = |Eperp|^2 >= 0 (depends on the transverse null data only)",
    vdot(n, Tn) == -vdot(Eperp, Eperp) and -vdot(Eperp, Eperp) > 0)

# duality on null data: for f = n ^ a (a transverse), I4 f = f J' with J' = g1 g2 acting by a 90-degree rotation
J = mul(g[1], g[2])
for a in (g[1], g[2], add(scal(3, g[1]), scal(-2, g[2]))):
    f = grade(mul(n, a), 2)
    ra = grade(mul(a, J), 1)  # a J = a turned by a quarter turn within the transverse plane
    chk(f"5. I4 (n^a) = (n^a) J = n^(a J) for transverse a = {a}: duality is the transverse quarter turn on null data",
        eq(mul(I4, f), mul(f, J)) and eq(mul(f, J), grade(mul(n, ra), 2)) and eq(mul(J, f), neg(mul(f, J))))
# rotation about the generator R = (3 + 4 J)/5-type rotor on the null data: E -> R E R~ = E (R~)^2
R = add(sc(F(2, 1)), scal(F(1, 1), J))  # unnormalised rotor (2 + J); R R~ = 5
Rt = GA.reverse(R)
E = add(scal(3, g[1]), scal(-2, g[2]))
eps = mul(g[1], E)  # g1 E in span{1, J}
chk("6. eps = g1 Eperp lies in span{1, J}", all(b in [(), (1, 2)] for b in eps))
lhs = mul(g[1], mul(mul(R, E), Rt))
chk("   rotating Eperp about the generator multiplies eps = g1 Eperp by (R~)^2 (a phase in span{1, J}; helicity +-1)",
    eq(lhs, mul(eps, mul(Rt, Rt))))
print("\nALL:", OK)
