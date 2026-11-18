import sys, time, importlib.util, pickle
LAB = "/home/claude/phys-graph"
sys.path.insert(0, LAB + "/lib")
import tp_premise
tp_premise.configure(LAB + "/store")
spec = importlib.util.spec_from_file_location("stored", LAB + "/store/claims/synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional/check.py")
st = importlib.util.module_from_spec(spec); spec.loader.exec_module(st)
from fractions import Fraction as F
import gtg
from gtg import Jet
from uring import U

z, s0, c0 = U.z(), U.s(), U.c()
M = F(1)
r0 = 2 * M / (1 - z * z)
f = gtg.f_static(M)
MONO = [(p, q) for p in range(3) for q in range(3 - p)]
FACT = {0: 1, 1: 1, 2: 2}


def even_ricci(fn, mono, ang):
    fld = gtg.static_field(r0, s0, c0, f, order=1, sqrt_f=z)
    t = Jet.var(0, F(0), 4, 2)
    r = Jet.var(1, r0, 4, 2)
    th = Jet.var(2, F(0), 4, 2)
    sn, cs = gtg.sincos(2, s0, c0, 4, 2)
    fj = f(r)
    sf = fj.pw(F(1, 2), z)
    P = ang[0] + ang[1] * th + F(ang[2], 2) * th * th
    Z = Jet.const(0, 4)
    H = [Z, Z, Z, Z]
    H[fn] = Jet(1, None, 4, 2) * (t ** mono[0]) * ((r - r0) ** mono[1])
    H0, H1, H2, K = H
    TH1 = [[Z] * 4 for _ in range(4)]
    TH1[0][0] = -sf * H0 * P / 2
    TH1[1][0] = sf * H1 * P
    TH1[1][1] = H2 * P / (2 * sf)
    TH1[2][2] = r * K * P / 2
    TH1[3][3] = r * sn * K * P / 2
    ric = st.lin_ricci(fld, TH1)
    out = {}
    for b in range(4):
        for (a,), v in ric[b].items():
            v = gtg._val(v)
            if v:
                out[(a, b)] = v
    return out


if __name__ == "__main__":
    t0 = time.time()
    res = {}
    for fn in range(4):
        for mono in MONO:
            for ai, ang in enumerate(((1, 0, 0), (0, 1, 0), (0, 0, 1))):
                o = even_ricci(fn, mono, ang)
                for ab, v in o.items():
                    res[(ab, fn, mono, ai)] = (v.n, v.d)
    print("time", time.time() - t0, "entries", len(res))
    pickle.dump(res, open("even_raw.pkl", "wb"))
