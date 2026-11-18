"""Cross-link: (P) on the matter algebra Cl(1,1) of the lattice model and the commutator [J, O].
Cl(3,1) here: e1 (+), e2 (-) the matter pair; e3, e4 (+,+) only to supply a unit I = e3 e4 commuting with the pair."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', '..', 'lib'))
from fractions import Fraction as F
import GA
SQ = (1, -1, 1, 1)
ONE = GA.sc(F(1))
def clean(x): return {b: c for b, c in x.items() if c != 0}
def prod(*xs):
    r = ONE
    for x in xs: r = GA.mul(r, x, SQ)
    return clean(r)
def dsign(b):
    g = len(b); s = (-1) ** (g * (g - 1) // 2)
    for i in b: s *= SQ[i]
    return s
def dagger(x): return {b: c * dsign(b) for b, c in x.items()}
def lin(*t):
    r = {}
    for c, x in t: r = GA.add(r, GA.scal(F(c), x))
    return clean(r)
e1, e2, e3, e4 = (GA.gen(i) for i in range(4))
v = lin((F(1, 2), e1), (F(1, 2), e2)); w = lin((F(1, 2), e1), (F(-1, 2), e2))
P1, P2 = prod(v, w), prod(w, v)
I = prod(e3, e4)
ok = True
for (p, q) in [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(1), F(0))]:
    for (c1, c2) in [(F(1), F(0)), (F(2), F(-3)), (F(7, 2), F(7, 2))]:
        U = lin((p, ONE), (q, e2)); Ui = lin((p, ONE), (-q, e2))
        assert prod(U, Ui) == ONE and clean(dagger(U)) == Ui
        J = lin((c1, P1), (c2, P2)); O = prod(Ui, P1, U)
        assert clean(dagger(J)) == J and clean(dagger(O)) == O and prod(O, O) == O
        comm = clean(GA.sub(prod(J, O), prod(O, J)))
        assert comm == clean(GA.scal((c1 - c2) * p * q, e2))
        assert clean(dagger(comm)) == clean(GA.neg(comm))
        sa = prod(I, comm)                      # self-adjoint
        assert clean(dagger(sa)) == sa
assert clean(dagger(e2)) == clean(GA.neg(e2)) and prod(I, I) == clean(GA.neg(ONE)) and clean(dagger(I)) == clean(GA.neg(I))
assert prod(I, e1) == prod(e1, I) and prod(I, e2) == prod(e2, I)
K = prod(I, e2)
assert prod(K, K) == ONE and clean(dagger(K)) == K
for s in (1, -1):
    E = lin((F(1, 2), ONE), (F(s, 2), K))
    assert prod(E, E) == E and clean(dagger(E)) == E
# states of (P) on Cl(1,1): omega(x) = <rho x>_0-type with rho = (1 + a e1 + b e1e2)/1, a^2 + b^2 <= 1; value of e2 is 0
def s0(x): return x.get((), F(0))
for a, b in [(F(0), F(0)), (F(3, 5), F(4, 5)), (F(1, 2), F(-1, 3))]:
    rho = lin((1, ONE), (a, e1), (b, prod(e1, e2)))
    val = lambda x: s0(prod(rho, x))
    assert val(e2) == 0 and val(ONE) == 1
    for x in [ONE, e1, e2, prod(e1, e2), lin((1, e1), (2, e2)), lin((1, ONE), (-1, prod(e1, e2)), (3, e2))]:
        assert val(prod(x, dagger(x))) >= 0
# sharp state on E_+ of the extended algebra: value of K is 1 (bound attained)
print("cross-link computation: all assertions hold")
