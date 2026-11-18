import sys, time
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as F
import gtg
from gtg import Jet
from uring import U
from closed import even_parts
import even_extract as ee

z, s0, c0 = ee.z, ee.s0, ee.c0
r0, f, M = ee.r0, ee.f, ee.M
zero = U.const(0)
t0 = time.time()
n = nz = 0
for fn in range(4):
    for mono in ee.MONO:
        t = Jet.var(0, F(0), 4, 2)
        r = Jet.var(1, r0, 4, 2)
        fj = f(r)
        Z = Jet.const(0, 4)
        H = [Z, Z, Z, Z]
        H[fn] = Jet(1, None, 4, 2) * (t ** mono[0]) * ((r - r0) ** mono[1])
        parts = {k: gtg._val(v) if isinstance(v, Jet) else v for k, v in even_parts(H[0], H[1], H[2], H[3], r, fj, M).items()}
        parts = {k: (v if isinstance(v, U) else U.const(v)) for k, v in parts.items()}
        for ang in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            a, b, p2 = ang
            DP = p2 + (c0 / s0) * b
            pre = b / (2 * r0 * z)
            want = {
                (0, 0): a * parts["c00"] + DP * parts["d00"],
                (0, 1): a * parts["c01"] + DP * parts["d01"],
                (1, 0): -(a * parts["c01"] + DP * parts["d01"]),
                (0, 2): -pre * parts["c02"],
                (2, 0): pre * parts["c02"],
                (1, 2): pre * parts["c12"],
                (2, 1): pre * parts["c12"],
                (1, 1): a * parts["c11"] + DP * parts["d11"],
                (2, 2): a * parts["c22"] + DP * parts["dK"] + p2 * parts["cHH"],
                (3, 3): a * parts["c22"] + DP * parts["dK"] + (c0 / s0) * b * parts["cHH"],
            }
            got = ee.even_ricci(fn, mono, ang)
            for ab in set(got) | set(want):
                g, w = got.get(ab, zero), want.get(ab, zero)
                if not (g == w):
                    print("MISMATCH", fn, mono, ang, ab, g, w)
                n += 1
                nz += bool(g)
print("compared", n, "nonzero", nz, "time", time.time() - t0)
