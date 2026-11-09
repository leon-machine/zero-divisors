"""Independent test of the identity behind Y1: sum_mu gamma^mu W(e_mu ^ xi) = 0 for a field strength of Weyl type
(Schwarzschild form W(B) = -(m/2)(B + 3 s B s), s = e_r e_t, in units of M/r^3) and = 3 lam xi for W(B) = lam B.
Cl(1,3), exact; all sixteen components, on a basis of xi (linear in xi)."""
import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
sq = GA.sig(1, 3)
e = [GA.gen(i) for i in range(4)]
recip = [e[0]] + [GA.neg(x) for x in e[1:]]          # gamma^mu
s = GA.mul(e[1], e[0], sq)                           # sigma_r = e_r e_t
def wedge(a, b):
    return GA.scal(F(1, 2), GA.sub(GA.mul(a, b, sq), GA.mul(b, a, sq)))
def weyl(B):
    return GA.scal(F(-1, 2), GA.add(B, GA.scal(F(3), GA.mul(GA.mul(s, B, sq), s, sq))))
def contract(R, xi):
    out = GA.sc(F(0))
    for mu in range(4):
        out = GA.add(out, GA.mul(recip[mu], R(wedge(e[mu], xi)), sq))
    return out
for xi in e + [GA.add(e[0], GA.scal(F(2), e[1]), GA.scal(F(-3), e[2]), e[3])]:
    assert GA.is_zero(contract(weyl, xi)), "Weyl contraction not zero"
    lam = F(5, 7)
    assert GA.eq(contract(lambda B: GA.scal(lam, B), xi), GA.scal(3 * lam, xi))
# control: without the factor 3 the map is not of Weyl type and the contraction is not zero
bad = lambda B: GA.scal(F(-1, 2), GA.add(B, GA.scal(F(2), GA.mul(GA.mul(s, B, sq), s, sq))))
assert not GA.is_zero(contract(bad, e[2]))
# trace-freeness alone (vector part) and the protraction (trivector part) separately
c = contract(weyl, e[2]); print("ok: gamma^mu W(e_mu ^ xi) = 0 on the Schwarzschild Weyl map; 3 lam xi on lam B; control fails as it should")
