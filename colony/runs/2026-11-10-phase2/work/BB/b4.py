from bbl import *
from itertools import combinations
def blades(n): return [ONE] + [{tuple(c): F(1)} for r in range(1, n+1) for c in combinations(range(n), r)]
sq, e, f, p = modes(2); B = blades(4)
X1, Z1, X2, Z2 = e[0], p[0], prod(sq, e[1], p[0]), p[1]
U, V = prod(sq, X1, X2), prod(sq, Z1, Z2); K = prod(sq, e[0], f[1])
print('U,V obs:', is_obs(U, sq), is_obs(V, sq), 'commute', GA.commutes(U, V, sq), 'UV =', clean(prod(sq, U, V)), 'K', K, 'U even', not odd(U))
Mp = lin((1, ONE), (-1, U), (-1, V), (1, prod(sq, U, V))); Mm = lin((1, ONE), (-1, U), (-1, V), (-1, prod(sq, U, V)))
lp = lambda x: s0(prod(sq, Mp, x)); lm = lambda x: s0(prod(sq, Mm, x))
Ps = GA.scal(F(1,4), Mp); print('Ps idempotent s.a. trace', clean(prod(sq, Ps, Ps)) == Ps, clean(dagger(Ps, sq)) == Ps, s0(Ps))
loc = [prod(sq, a, b) for a in (ONE, X1, Z1) for b in (ONE, X2, Z2)]
print('agree on the 9 local products:', all(lp(x) == lm(x) for x in loc), 'differ on blades:', [tuple(b.keys())[0] for b in B if lp(b) != lm(b)])
Ppp = prod(sq, lin((F(1,2), ONE), (F(1,2), U)), lin((F(1,2), ONE), (F(1,2), V)))
print('lm(weight of U=V=+1) =', lm(Ppp), 'lp =', lp(Ppp), 'lm real:', all(lm(dagger(b, sq)) == lm(b) for b in B), 'lm even:', all(lm(par(b)) == lm(b) for b in B))
T = lambda l: [[l(prod(sq, a, b)) for b in (X2, Z2)] for a in (X1, Z1)]
print('T(lp)', T(lp), 'T(lm)', T(lm), 'marginals', [lm(x) for x in (X1, Z1, X2, Z2)])
C = chsh(sq, X1, Z1, X2, Z2); box = lambda x: s0(prod(sq, GA.add(ONE, C), x))
print('T(box)', T(box))
a = X1; b = lin((F(-3,5), X2), (F(-4,5), Z2))
print('box weight of (a=+1,b=+1) at b=-(3/5,4/5):', box(prod(sq, lin((F(1,2), ONE), (F(1,2), a)), lin((F(1,2), ONE), (F(1,2), b)))))
# record map and parity
Ea = lambda a, x: lin((F(1,2), x), (F(1,2), prod(sq, a, x, a)))
def keeps_even(a):
    return all(not even(Ea(a, y)) for y in B if odd(y))   # E(E_a(y)) = 0 for odd y
mixed = lin((F(3,5), X1), (F(4,5), Z1)); mixedB = lin((F(3,5), X2), (F(4,5), Z2))
print('keeps even: X1', keeps_even(X1), 'Z1', keeps_even(Z1), 'X2', keeps_even(X2), 'Z2', keeps_even(Z2), 'mixed A', keeps_even(mixed), 'mixed B', keeps_even(mixedB), 'U', keeps_even(U))
rho = prod(sq, lin((1, ONE), (1, p[0])), lin((1, ONE), (1, p[1]))); om = lambda x: s0(prod(sq, rho, x))
print('even state (1+p1)(1+p2): om o E_mixed (e1) =', om(Ea(mixed, e[0])))
# even state above 2 with a mixed setting of B
B1 = lin((F(3,5), X2), (F(4,5), Z2)); B2 = lin((F(4,5), X2), (F(-3,5), Z2))
C2 = chsh(sq, X1, Z1, B1, B2); Ce = even(C2); print('E(C) =', Ce)
for s in (1, -1):
    for t in (1, -1):
        r = prod(sq, lin((1, ONE), (s, U)), lin((1, ONE), (t, V))); print('  even state', s, t, 'value', s0(prod(sq, r, C2)), 'even', not odd(r))
# homogeneous: E(C) = U - V ; 2 - (U - V) = ((1-U)^2 + (1+V)^2)/2
print('E(C) homogeneous:', even(C), ' certificate:', lin((2, ONE), (-1, even(C))) == lin((F(1,2), prod(sq, GA.sub(ONE, U), GA.sub(ONE, U))), (F(1,2), prod(sq, GA.add(ONE, V), GA.add(ONE, V)))))
# all self-adjoint elements of mode-1 algebra of square 1, homogeneous
print('s.a. basis of mode 1 algebra:', [tuple(b.keys())[0] for b in blades(4) if set(tuple(b.keys())[0]) <= {0, 1} and clean(dagger(b, sq)) == b])
# E_N: mode-wise average
EN = lambda x: clean({b: c for b, c in x.items() if all((2*k in b) == (2*k+1 in b) for k in range(2))})
print('E_N of box density:', EN(GA.add(ONE, C)), ' E_N of Mm:', EN(Mm))
