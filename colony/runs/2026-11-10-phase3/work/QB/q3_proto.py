import sys, time
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, gtg
from gtg import Jet

def poly_field(seed, d=4, sq=None, torsion=None):
    sq = gtg.lorentz_sig(d) if sq is None else sq
    X = [Jet.var(i, F(0), d, 2) for i in range(d)]
    # deterministic small integers
    def c(k):
        return F(((seed * 7919 + k * 104729) % 11) - 5, 1 + (seed + k) % 3)
    TH = []
    k = 0
    for a in range(d):
        row = []
        for mu in range(d):
            j = Jet.const(F(1) if a == mu else F(0), d) + X[0] * 0
            j = j + F(c(k), 4) ; k += 1
            for i in range(d):
                j = j + X[i] * F(c(k), 3); k += 1
                for l in range(i, d):
                    j = j + X[i] * X[l] * F(c(k), 2); k += 1
            row.append(j)
        TH.append(row)
    return gtg.Field(TH, None, sq), TH, sq

def protraction(fld):
    d, sq = fld.d, fld.sq
    Rc = fld.curvature()
    out = []
    for b in range(d):
        T = {}
        for a in range(d):
            if a == b: continue
            key = (a, b) if a < b else (b, a)
            s = 1 if a < b else -1
            T = gtg.m_add(T, gtg.outer(gtg.er(a, sq), gtg.m_scal(s, Rc[key]), sq))
        out.append(T)
    return out, Rc

t = time.time()
for seed in (1, 2):
    fld, TH, sq = poly_field(seed)
    print('torsion free', fld.torsion_free(), 'det ok')
    T, Rc = protraction(fld)
    print(seed, [len(x) for x in T], sum(len(v) for v in Rc.values()), time.time() - t)
    # control: perturb Om
    Om = [dict(x) for x in fld.Om]
    X = [Jet.var(i, F(0), 4, 2) for i in range(4)]
    Om[1] = gtg.m_add(Om[1], {(0, 2): X[3] * F(1, 2) + F(1, 3)})
    f2 = gtg.Field(TH, None, sq, Om=Om)
    T2, _ = protraction(f2)
    print('control torsion free', f2.torsion_free(), [len(x) for x in T2])
