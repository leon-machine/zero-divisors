from bbl import *
from itertools import combinations, product
# --- sym(PAP) = kP in several algebras
def blades(n): return [GA.sc(F(1))] + [ {tuple(c): F(1)} for r in range(1, n+1) for c in combinations(range(n), r)]
def rank(vs, keys):
    return GA.mat_rank([[v.get(k, F(0)) for k in keys] for v in vs]) if vs else 0
def test(sq, P, name):
    n = len(sq); B = blades(n); keys = [tuple(b.keys())[0] for b in B]
    assert clean(prod(sq, P, P)) == clean(P) and clean(dagger(P, sq)) == clean(P)
    pap = [clean(prod(sq, P, b, P)) for b in B]
    sym = [lin((1, y), (1, dagger(y, sq))) for y in pap]
    print(name, 'dim PAP', rank(pap, keys), 'dim sym(PAP)', rank(sym, keys), 'trace P', s0(P))
e0, e1, e2 = GA.gen(0), GA.gen(1), GA.gen(2)
test((1, -1), lin((F(1,2), ONE), (F(1,2), e0)), 'Cl(1,1) (1+e)/2')
test((1, 1), lin((F(1,2), ONE), (F(1,2), e0)), 'Cl(2,0)')
test((-1, -1), ONE, 'Cl(0,2) P=1')
test((1, 1, 1), lin((F(1,2), ONE), (F(1,2), e0)), 'Cl(3,0)')
test((-1, -1, -1), lin((F(1,2), ONE), (F(1,2), GA.mul(GA.mul(e0, e1, (-1,-1,-1)), e2, (-1,-1,-1)))), 'Cl(0,3) (1+I)/2')
test((1,1,1,1), lin((F(1,2), ONE), (F(1,2), e0)), 'Cl(4,0) (1+e1)/2')
sq, e, f, p = modes(2)
P0 = prod(sq, lin((F(1,2), ONE), (F(1,2), p[0])), lin((F(1,2), ONE), (F(1,2), p[1])))
test(sq, P0, 'Cl(2,2) (1+p1)(1+p2)/4')
test((1,-1,-1,-1), lin((F(1,2), ONE), (F(1,2), e0)), 'Cl(1,3) (1+g0)/2')
test((1,-1,-1,-1), lin((F(1,2), ONE), (F(1,2), GA.mul(GA.gen(1), e0, (1,-1,-1,-1)))), 'Cl(1,3) (1+g1g0)/2')
# --- (i) no reality
sq1 = (1, -1); e, f = GA.gen(0), GA.gen(1); p = GA.mul(f, e, sq1)
P = lin((F(1,2), ONE), (F(1,2), e))
om = lambda x: 2 * s0(prod(sq1, P, x)) + 3 * s0(prod(sq1, f, x))
B = blades(2)
print('no reality: om(1), om(P), om(f), born(f):', om(ONE), om(P), om(f), 2 * s0(prod(sq1, P, f)))
# positivity: form om(x x^dag) on general x = sum c_b b equals that of om_P: check Gram matrices agree on symmetric part
G = [[om(prod(sq1, a, dagger(b, sq1))) + om(prod(sq1, b, dagger(a, sq1))) for b in B] for a in B]
G0 = [[4 * s0(prod(sq1, P, a, dagger(b, sq1))) + 0 * 1 for b in B] for a in B]
G0 = [[2 * s0(prod(sq1, P, a, dagger(b, sq1))) + 2 * s0(prod(sq1, P, b, dagger(a, sq1))) for b in B] for a in B]
print('quadratic form equal to Born one:', G == G0)
# --- (ii) boosted idempotent
A = lin((F(5,4), e), (F(3,4), f)); Pb = lin((F(1,2), ONE), (F(1,2), A))
print('boost: A^2=1', clean(prod(sq1, A, A)) == ONE, 'Pb idem', clean(prod(sq1, Pb, Pb)) == Pb, 'sa', clean(dagger(Pb, sq1)) == Pb)
for z in (F(3,5), F(0), F(-3,5)):
    rho = lin((1, ONE), (F(4,5), e), (z, p))
    w = lambda x: s0(prod(sq1, rho, x))
    print(' z', z, 'omega(Pb)=', w(Pb), 'omega(p)=', w(p), 'det-type 1-x^2-z^2 =', 1 - F(16,25) - z*z)
rho = lin((1, ONE), (1, e)); print(' state (1+e): weight of Pb', s0(prod(sq1, rho, Pb)), 'of 1-Pb', s0(prod(sq1, rho, GA.sub(ONE, Pb))))
# --- Gleason size 2
g = lambda x, z: 1 if (z > 0 or (z == 0 and x > 0)) else 0
pts = [(F(1), F(0)), (F(0), F(1)), (F(3,5), F(4,5)), (F(-3,5), F(4,5)), (F(5,13), F(-12,13))]
print('frame fn additive:', all(g(x, z) + g(-x, -z) == 1 for x, z in pts))
print('linear extension from E(e),E(p) predicts on (3/5,4/5):', F(1,2) * (1 + F(3,5) * (2*g(1,0)-1) + F(4,5) * (2*g(0,1)-1)), 'actual', g(F(3,5), F(4,5)))
