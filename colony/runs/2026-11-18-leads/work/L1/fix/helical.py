import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
import tp_premise; tp_premise.configure("/home/claude/phys-graph/store")
sys.path.insert(0, "/home/claude/phys-graph/proposals/synthesis.tube-point-clause-fixes-no-observer-where-rotations-have-no-fixed-point")
import check as c
from fractions import Fraction as F
g = c.g
I = c.tractor(F(1, 2), 0, 0, 1)
W = c.lin((F(-1, 2), 1), (c.NO, c.NINF))
J = c.mul(c.e3, c.e4)
rot = c.stabiliser(I)
assert g.is_zero(c.comm(J, I)) and g.is_zero(c.comm(J, c.K))

def boost(X, hs):
    """the chart boost of rational half-rapidity parameter hs on a vector"""
    ch = (1 + hs * hs) / (1 - hs * hs); sh = 2 * hs / (1 - hs * hs)
    v = c.cv(X)
    v[0], v[1] = ch * v[0] + sh * v[1], sh * v[0] + ch * v[1]
    return c.vec(*v)

def rotJ(X, cs, sn):
    v = c.cv(X)
    v[2], v[3] = cs * v[2] - sn * v[3], sn * v[2] + cs * v[3]
    return c.vec(*v)

R1, R2 = (F(3, 5), F(4, 5)), (F(5, 13), F(12, 13))
R12 = (R1[0] * R2[0] - R1[1] * R2[1], R1[0] * R2[1] + R1[1] * R2[0])
ok = 0
for (s, cc) in c.RADII:
    for hs in c.BOOSTS:
        u, w = c.boost_pair(hs)
        for (n3, n4, nw) in c.SPHERE:
            n = c.lin((n3, n4, nw), (c.e3, c.e4, W))
            X = g.add(I, g.scal(cc, w), g.scal(s, n))
            # psi at eta: rotate by R1; boost by tau; psi^{-1} at eta + tau: rotate back by R1 R2
            Y = rotJ(boost(rotJ(X, *R1), F(1, 4)), R12[0], -R12[1])
            Z = rotJ(boost(X, F(1, 4)), R2[0], -R2[1])
            assert g.is_zero(g.sub(Y, Z)); ok += 1
print("conjugated boost = boost times rotation about J:", ok)
fixed = 0
for (s, cc) in c.RADII:
    if s == 0: continue
    for hs in c.BOOSTS:
        u, w = c.boost_pair(hs)
        for sign in (1, -1):
            X = g.add(I, g.scal(cc, w), g.scal(sign * s, W))
            assert c.ip(X, X) == 0 and g.is_zero(c.comm(J, X))
            assert not all(g.is_zero(c.comm(B, X)) for B in rot)
            rho = 2 * cc / (1 - sign * s)
            re, im, obs = c.tube_parts(0, 0, rho, hs)
            lam = c.ip(X, c.NINF)
            assert g.is_zero(g.sub(g.scal(1 / lam, X), c.X_of(obs)))
            assert c.fixes_tube(J, re, im) and not all(c.fixes_tube(B, re, im) for B in rot)
            fixed += 1
print("axis observers fixed by J with their tube points:", fixed, "rho values", sorted({2 * cc / (1 - sg * s) for (s, cc) in c.RADII if s for sg in (1, -1)}))
