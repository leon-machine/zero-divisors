import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
import tp_premise; tp_premise.configure("/home/claude/phys-graph/store")
sys.path.insert(0, "/home/claude/phys-graph/proposals/synthesis.tube-point-clause-on-black-hole-fields-empty-for-the-horizon-flow-and-reading-dependent")
import check as c
from fractions import Fraction as F
g = c.g
J = c.mul(c.e3, c.e4)
for lam in (3, 12, F(4, 3)):
    I = c.tractor(F(lam) / 6, 0, 0, 1)
    for cc in (F(1), F(3, 7), F(-2)):
        KJ = g.add(c.K, g.scal(cc, J))
        rows = [c.cv(c.comm(B, I)) + c.bv(c.comm(B, KJ)) for B in c.BIV]
        dim = len(c.BIV) - c.rank(rows)
        sym = len(c.BIV) - c.rank([c.cv(c.comm(B, I)) for B in c.BIV])
        assert g.is_zero(c.comm(J, I)) and g.is_zero(c.comm(c.K, I))
        print("Lambda", lam, "c", cc, "symmetry algebra dim", sym, "centraliser of K + cJ dim", dim)
# a K + B fixes no compatible tube point
I = c.tractor(F(1, 2), 0, 0, 1)
rot = c.stabiliser(I)
n = 0
for (x3, x4) in c.FEET:
    for rho in c.RHOS:
        for s in c.BOOSTS:
            re, im, obs = c.tube_parts(x3, x4, rho, s)
            for B in rot + [c.lin(m, c.TRANSVERSE) for m in c.MIXES]:
                for a in (F(1), F(-1, 3), F(5)):
                    assert not c.fixes_tube(g.add(g.scal(a, c.K), B), re, im); n += 1
print("a K + B fixes none:", n)
