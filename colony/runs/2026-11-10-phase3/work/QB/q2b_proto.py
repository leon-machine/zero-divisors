import sys, time
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, gtg
from gtg import Jet
D4 = 4
SQ = gtg.S13

def coef(seed, k, m=11):
    return F(((seed * 7919 + k * 104729) % m) - m // 2)

def gen_poly(seed, k0, order, scale, d=D4, const=F(0)):
    """generic polynomial jet of the given order about 0; returns (jet, next k)"""
    X = [Jet.var(i, F(0), d, order) for i in range(d)]
    j = Jet.const(const, d) + X[0] * 0
    k = k0
    import itertools
    for deg in range(1, order + 1):
        for combo in itertools.combinations_with_replacement(range(d), deg):
            t = Jet.const(coef(seed, k) * scale, d); k += 1
            for i in combo:
                t = t * X[i]
            j = j + t
    return j, k

def sample_field(seed, order=3):
    TH = []; k = 0
    for a in range(D4):
        row = []
        for mu in range(D4):
            j, k = gen_poly(seed, k, order, F(1, 4), const=(F(1) if a == mu else F(0)) + coef(seed, 1000 + 4 * a + mu) / 8)
            row.append(j)
        TH.append(row)
    return gtg.Field(TH, None, SQ), TH

class Calc(object):
    def __init__(self, fld):
        self.f = fld
        HJ = fld.hb_matrix_jet()
        self.HJ = HJ
        self.gup = [gtg.m_add(*[gtg.m_scal(HJ[mu][a] * SQ[a], GA.gen(a)) for a in range(D4)]) for mu in range(D4)]
        self.Rc = fld.curvature()
    def Dmu(self, mu, M):
        return gtg.m_add(gtg.m_d(M, mu), gtg.comm(self.f.Om[mu], M, SQ))
    def grad(self, chi):
        return gtg.m_add(*[gtg.m_scal(chi.d(mu), self.gup[mu]) for mu in range(D4)])
    def div(self, A):
        out = 0
        for mu in range(D4):
            out = out + gtg.vdot(self.gup[mu], self.Dmu(mu, A), SQ)
        return out
    def curl(self, A):
        return gtg.m_add(*[gtg.outer(self.gup[mu], self.Dmu(mu, A), SQ) for mu in range(D4)])
    def divB(self, B):
        return gtg.m_add(*[gtg.inner_vb(self.gup[mu], self.Dmu(mu, B), SQ) for mu in range(D4)])
    def along(self, a, M):
        """(gamma_a . D) M"""
        return gtg.m_add(*[gtg.m_scal(self.HJ[mu][a], self.Dmu(mu, M)) for mu in range(D4)])
    def along_vec(self, v, M):
        return gtg.m_add(*[gtg.m_scal(v.get((a,), F(0)) * SQ[a] * SQ[a], self.along(a, M)) for a in range(D4) if v.get((a,))])
    def rough(self, A):
        out = {}
        for a in range(D4):
            t = self.along(a, self.along(a, A))
            ga = {(a,): Jet.const(F(1), D4)}
            v = self.along(a, ga)                       # (gamma_a . D) gamma_a = Omega(hb gamma_a) x gamma_a
            t = gtg.m_sub(t, self.along_vec(v, A))
            out = gtg.m_add(out, gtg.m_scal(SQ[a], t))
        return out

t0 = time.time()
rows = []
for seed in (1, 2):
    fld, TH = sample_field(seed)
    print('field', seed, fld.torsion_free(), time.time() - t0)
    C = Calc(fld)
    # generic vector field
    A = {}
    k = 5000
    for a in range(D4):
        j, k = gen_poly(seed + 10, k, 2, F(1, 2), const=coef(seed, 77 + a))
        A[(a,)] = j
    lhs = gtg.m_val(gtg.m_add(C.divB(C.curl(A)), gtg.m_neg(C.rough(A)), C.grad(C.div(A))))
    ricA = gtg.ricci(C.Rc, gtg.m_val(A), SQ)
    print(' weitz', lhs == ricA, lhs == gtg.m_neg(ricA), lhs, ricA)
    for cs in (3, 4):
        chi, _ = gen_poly(seed * 10 + cs, 9000, 3, F(1, 2))
        g = C.grad(chi)
        print(' curl grad', gtg.m_val(C.curl(g)))
        v1 = gtg.m_val(C.rough(g)); v2 = gtg.m_val(C.grad(C.div(g))); v3 = gtg.m_val(g)
        v4 = gtg.m_scal(gtg.ricci_scalar(C.Rc, SQ), v3); v5 = gtg.ricci(C.Rc, v3, SQ)
        for a in range(D4):
            rows.append([v.get((a,), F(0)) for v in (v1, v2, v3, v4, v5)])
    print(time.time() - t0)
print(GA.mat_rank(rows) if hasattr(GA, 'mat_rank') else None)
ker = GA.field_kernel(rows)
print(ker)
