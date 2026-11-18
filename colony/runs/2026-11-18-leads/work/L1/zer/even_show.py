import pickle
from fractions import Fraction as F
res = pickle.load(open("even_raw.pkl", "rb"))
NAMES = ["H0", "H1", "H2", "K"]
ANG = ["P", "P'", "P''"]
def show(n, d):
    # group by trig monomial
    groups = {}
    for (i, j, k), x in n.items():
        groups.setdefault((j, k), {})[i] = x
    parts = []
    for (j, k), co in sorted(groups.items()):
        poly = " + ".join("%s z^%d" % (x, i) for i, x in sorted(co.items()))
        parts.append("[s^%d c^%d](%s)" % (j, k, poly))
    return " + ".join(parts) + "  / z^%d (1-z^2)^%d s^%d" % d
for ab in sorted({k[0] for k in res}):
    print("== component gamma_%d of R1(gamma_%d)" % ab)
    for key in sorted(k for k in res if k[0] == ab):
        _, fn, mono, ai = key
        n, d = res[key]
        print("   d_t^%d d_r^%d %s * %s : %s" % (mono[0], mono[1], NAMES[fn], ANG[ai], show(n, d)))
