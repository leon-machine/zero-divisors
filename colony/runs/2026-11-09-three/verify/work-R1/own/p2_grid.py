# Referee extension: clause (1) over a BASIS of second-order jets of (h0,h1) and of S-data, on a 3 angle x 2 L grid,
# as identities of rational functions of z = sqrt f. Uses the proposal's own lin_ricci.
import sys, os, time
LAB='/home/claude/phys-graph'
sys.path.insert(0, LAB+'/lib'); sys.path.insert(0, LAB+'/proposals/synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional')
import tp_premise; tp_premise.configure(LAB+'/store')
from fractions import Fraction as F
import GA, gtg
from gtg import Jet
from GA import RF
import check as C
def case(M, r0, w, s0, c0, L, mono, which, a, b):
    f = gtg.f_static(M)
    fld = gtg.static_field(r0, s0, c0, f, order=1, sqrt_f=w)
    t = Jet.var(0, F(0), 4, 2); r = Jet.var(1, r0, 4, 2)
    sn, cs = gtg.sincos(2, s0, c0, 4, 2)
    fj = f(r); sf = fj.pw(F(1, 2), w)
    m = (t ** mono[0]) * ((r - r0) ** mono[1]) if mono != (0,0) else Jet.const(1,4) + 0*t
    Zr = 0*t
    h0, h1 = (m, Zr) if which == 0 else (Zr, m)
    S = C.angular(sn, cs, L, a, b, 1, 2)
    Z = Jet.const(0, 4)
    TH1 = [[Z] * 4 for _ in range(4)]
    TH1[0][3] = h0 * S / sf
    TH1[1][3] = -h1 * S * sf
    ric = [{k: gtg._val(v) for k, v in x.items() if gtg._val(v)} for x in C.lin_ricci(fld, TH1)]
    Et, Er, Eth = [x.v for x in C.odd_equations(h0, h1, fj, r, M, L)]
    pre = -a / (2 * r0 * s0 * w)
    ang = (b - 2 * (c0 / s0) * a) / (2 * r0 * r0 * s0)
    want = {(0,): pre * Et, (1,): pre * Er, (2,): ang * Eth}
    zero = 0 * pre
    ok = all(ric[3].get(k, zero) == want[k] for k in want) and set(ric[3]) <= set(want)
    ok &= ric[0].get((3,), zero) == -want[(0,)] and set(ric[0]) <= {(3,)}
    ok &= ric[1].get((3,), zero) == want[(1,)] and set(ric[1]) <= {(3,)}
    ok &= ric[2].get((3,), zero) == want[(2,)] and set(ric[2]) <= {(3,)}
    return ok
z = C.K(RF.var())
monos = [(i, j) for i in range(3) for j in range(3 - i)]
angles = [(F(3,5),F(4,5)), (F(5,13),F(12,13)), (F(15,17),F(-8,17))]
t0=time.time(); n=0; bad=[]
for (s0,c0) in angles:
    for L in (F(7,2), F(6)):
        for M in (F(1),):
            for mono in monos:
                for which in (0,1):
                    for (a,b) in ((F(1),F(0)),(F(0),F(1))):
                        n+=1
                        if not case(M, 2*M/(1-z*z), z, s0, c0, L, mono, which, a, b): bad.append((s0,L,mono,which,a,b))
    print('angle',s0,'done',n,round(time.time()-t0,1),flush=True)
print('cases',n,'failures',bad)
