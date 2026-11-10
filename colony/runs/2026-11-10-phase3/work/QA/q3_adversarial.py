"""QA adversarial test of Q3 (protraction identity d_a ^ calR(a ^ b) = 0). Independent of QB's scripts.
T(b) = sum_a gamma^a ^ calR(gamma_a ^ gamma_b) (trivector) on: (1) a generic non-diagonal polynomial coframe with the
torsion-free Omega; (2) the same coframe with Omega shifted by a position-dependent bivector field (torsion);
(3) Omega = 0 with a non-holonomic coframe (torsion, zero curvature): the converse fails."""
import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, gtg
S = gtg.S13
d = 4

def rows(X):
    t, x, y, z = X
    return [[1 + F(1, 3) * x + t * y, F(1, 5) * z * z, F(1, 7) * t, 0],
            [F(1, 2) * y, 1 - F(1, 4) * t + x * z, F(1, 9) * x * x, F(1, 3) * y],
            [0, F(1, 6) * t * t, 1 + F(1, 2) * z - x * y, F(1, 8) * t],
            [F(1, 4) * x * y, 0, F(1, 5) * t, 1 + F(1, 3) * y + z * z]]

x0 = [F(1, 2), F(-1, 3), F(1, 5), F(2, 7)]

def wedge3(v, B):
    """grade-3 part of v B for a vector v and bivector B."""
    p = gtg.m_mul(v, B, S)
    return {k: c for k, c in p.items() if len(k) == 3 and c}

def protraction(fld):
    Rc = fld.curvature()
    out = []
    for b in range(d):
        T = {}
        for a in range(d):
            if a == b:
                continue
            key = (a, b) if a < b else (b, a)
            sgn = 1 if a < b else -1
            recip = gtg.m_scal(F(S[a]), gtg.e(a))
            T = gtg.m_add(T, gtg.m_scal(sgn, wedge3(recip, Rc[key])))
        out.append({k: c for k, c in T.items() if c})
    return out

f1 = gtg.field_from_hbinv(rows, x0, S, order=1)
print("1 torsion-free:", f1.torsion_free(), " protraction zero:", all(t == {} for t in protraction(f1)),
      " curvature nonzero:", any(v for v in f1.curvature().values()))

# pair symmetry <A calR(B)> = <calR(A) B> on (1)
Rc = f1.curvature()
keys = list(Rc)
def sp(A, B):
    return gtg.m_mul(A, B, S).get((), F(0))
print("  pair symmetric:", all(sp({k1: F(1)}, Rc[k2]) == sp(Rc[k1], {k2: F(1)}) for k1 in keys for k2 in keys))

# (2) add torsion: Omega(e_mu) -> Omega(e_mu) + K_mu(x)
def with_torsion(kfun):
    X = [gtg.Jet.var(i, x0[i], d, 2) for i in range(d)]
    r = rows(X)
    TH = [[gtg._jc(r[mu][a], d) for mu in range(d)] for a in range(d)]
    base = gtg.Field(TH, None, S)
    Om = [gtg.m_add(base.Om[mu], kfun(X, mu)) for mu in range(d)]
    return gtg.Field(TH, None, S, Om=Om)

def generic(X, mu):
    t, x, y, z = X
    bl = gtg.bivector_blades(d)
    return {bl[(mu + j) % 6]: gtg._jc((j + 1) * x + (mu + 2) * t * z + F(1, 3 + j), d) for j in range(3)}

f2 = with_torsion(generic)
print("2 generic torsion: torsion-free", f2.torsion_free(), " protraction zero:", all(t == {} for t in protraction(f2)))

# totally antisymmetric (axial) contorsion with constant physical trivector: K(a) = a . S3, S3 constant
def axial(X, mu):
    S3 = {(1, 2, 3): F(1, 2), (0, 1, 2): F(1, 3)}
    # physical vector over e_mu is g_mu = hb^{-1}(e_mu); K(e_mu) = g_mu . S3
    r = rows(X)
    out = {}
    for a in range(d):
        p = gtg.m_mul(gtg.e(a), S3, S)
        dotp = {k: c for k, c in p.items() if len(k) == 2}
        for k, c in dotp.items():
            out[k] = out.get(k, 0) + gtg._jc(r[mu][a], d) * c
    return out
f3 = with_torsion(axial)
print("3 axial torsion (constant spin trivector): torsion-free", f3.torsion_free(), " protraction zero:",
      all(t == {} for t in protraction(f3)))

# (4) Omega = 0, same coframe: curvature zero, torsion nonzero
X = [gtg.Jet.var(i, x0[i], d, 2) for i in range(d)]
r = rows(X)
TH = [[gtg._jc(r[mu][a], d) for mu in range(d)] for a in range(d)]
f4 = gtg.Field(TH, None, S, Om=[{} for _ in range(d)])
print("4 Omega = 0: torsion-free", f4.torsion_free(), " protraction zero:", all(t == {} for t in protraction(f4)),
      " curvature zero:", not any(v for v in f4.curvature().values()))

# ---- independent test of QB's clause (ii): (1/2) C_R(g^mu) = D ^ Theta^mu - Theta^nu ^ D_nu g^mu
def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k and c}

def jgrade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}

def clause_ii(fld):
    HJ = fld.hb_matrix_jet()
    recip = [gtg.m_scal(F(S[a]), gtg.e(a)) for a in range(d)]
    co = [gtg.m_add(*[gtg.m_scal(HJ[mu][a], recip[a]) for a in range(d)]) for mu in range(d)]     # g^mu jets
    Dg = [[gtg.m_add(gtg.m_d(co[mu], lam), gtg.comm(fld.Om[lam], co[mu], S)) for mu in range(d)] for lam in range(d)]
    Theta = [gtg.m_add(*[jgrade(gtg.m_mul(co[lam], Dg[lam][mu], S), 2) for lam in range(d)]) for mu in range(d)]
    Rc = fld.curvature()
    def calR(a, b):
        if a == b:
            return {}
        return Rc[(a, b)] if a < b else gtg.m_neg(Rc[(b, a)])
    res = []
    for mu in range(d):
        c = gtg.m_val(co[mu])
        C = {}
        for a in range(d):
            for b in range(d):
                if a == b:
                    continue
                v = grade(gtg.m_mul(calR(a, b), c, S), 1)
                w = grade(gtg.m_mul(recip[a], v, S), 2)
                C = gtg.m_add(C, grade(gtg.m_mul(recip[b], w, S), 3))
        C = {k: x for k, x in C.items() if x}
        rhs = {}
        for lam in range(d):
            DT = gtg.m_add(gtg.m_d(Theta[mu], lam), gtg.comm(fld.Om[lam], Theta[mu], S))
            rhs = gtg.m_add(rhs, grade(gtg.m_mul(gtg.m_val(co[lam]), gtg.m_val(DT), S), 3))
            rhs = gtg.m_sub(rhs, grade(gtg.m_mul(gtg.m_val(Theta[lam]), gtg.m_val(Dg[lam][mu]), S), 3))
        rhs = {k: x for k, x in rhs.items() if x}
        half = {k: x / 2 for k, x in C.items()}
        res.append((half == rhs, half == gtg.m_neg(rhs) if rhs else None, bool(C)))
    return res
for name, f in (("generic torsion", f2), ("axial torsion", f3), ("Omega=0", f4), ("torsion-free", f1)):
    print("clause (ii)", name, clause_ii(f))
