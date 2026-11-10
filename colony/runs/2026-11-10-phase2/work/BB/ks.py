from bbl import *
from itertools import product, combinations
sq, e, f, p = modes(2)
v = [lin((F(1,2), e[j]), (F(1,2), f[j])) for j in range(2)]   # creation
w = [lin((F(1,2), e[j]), (F(-1,2), f[j])) for j in range(2)]  # annihilation = v^dagger
assert all(clean(dagger(v[j], sq)) == w[j] for j in range(2))
P0 = prod(sq, w[0], v[0], w[1], v[1])
s = [P0, prod(sq, v[0], P0), prod(sq, v[1], P0), prod(sq, v[0], v[1], P0)]
E = [[clean(prod(sq, s[i], dagger(s[j], sq))) for j in range(4)] for i in range(4)]
ok = all(clean(prod(sq, E[i][j], E[k][l])) == (E[i][l] if j == k else {}) for i in range(4) for j in range(4) for k in range(4) for l in range(4))
print('matrix units', ok, 'sum Eii = 1', lin(*[(1, E[i][i]) for i in range(4)]) == ONE, 'dagger', all(clean(dagger(E[i][j], sq)) == E[j][i] for i in range(4) for j in range(4)))
bases = [[(0,0,0,1),(0,0,1,0),(1,1,0,0),(1,-1,0,0)],[(0,0,0,1),(0,1,0,0),(1,0,1,0),(1,0,-1,0)],
 [(1,-1,1,-1),(1,-1,-1,1),(1,1,0,0),(0,0,1,1)],[(1,-1,1,-1),(1,1,1,1),(1,0,-1,0),(0,1,0,-1)],
 [(0,0,1,0),(0,1,0,0),(1,0,0,1),(1,0,0,-1)],[(1,-1,-1,1),(1,1,1,1),(1,0,0,-1),(0,1,-1,0)],
 [(1,1,-1,1),(1,1,1,-1),(1,-1,0,0),(0,0,1,1)],[(1,1,-1,1),(-1,1,1,1),(1,0,1,0),(0,1,0,-1)],
 [(1,1,1,-1),(-1,1,1,1),(1,0,0,1),(0,1,-1,0)]]
rays = sorted(set(r for b in bases for r in b)); print('rays', len(rays))
def proj(r):
    n = sum(x*x for x in r)
    return lin(*[(F(r[i]*r[j], n), E[i][j]) for i in range(4) for j in range(4)])
Pr = {r: proj(r) for r in rays}
print('idempotent, s.a.:', all(clean(prod(sq, Pr[r], Pr[r])) == Pr[r] and clean(dagger(Pr[r], sq)) == Pr[r] and s0(Pr[r]) == F(1,4) for r in rays))
print('contexts resolve 1:', all(lin(*[(1, Pr[r]) for r in b]) == ONE for b in bases), 'orth:', all(clean(prod(sq, Pr[a], Pr[b2])) == {} for b in bases for a in b for b2 in b if a != b2))
print('each ray in exactly two contexts:', all(sum(r in b for b in bases) == 2 for r in rays))
idx = {r: i for i, r in enumerate(rays)}; cnt = 0
for bits in range(1 << 18):
    if all(sum((bits >> idx[r]) & 1 for r in b) == 1 for b in bases): cnt += 1
print('0/1 assignments:', cnt)
print('sample idempotent coefficients:', Pr[(1,1,1,1)])
# Mermin-Peres square in blades
X1, Z1, X2, Z2 = e[0], p[0], prod(sq, e[1], p[0]), p[1]
sqr = [[X1, X2, prod(sq, X1, X2)], [Z2, Z1, prod(sq, Z1, Z2)], [prod(sq, X1, Z2), prod(sq, Z1, X2), None]]
sqr[2][2] = prod(sq, sqr[0][2], sqr[1][2])
print('all observables, blades up to sign:', all(is_obs(x, sq) and len(clean(x)) == 1 for row in sqr for x in row))
print('rows commute:', all(GA.commutes(r[i], r[j], sq) for r in sqr for i in range(3) for j in range(3)), 'cols commute:', all(GA.commutes(sqr[i][c], sqr[j][c], sq) for c in range(3) for i in range(3) for j in range(3)))
print('row products', [clean(prod(sq, *r)) for r in sqr], 'col products', [clean(prod(sq, sqr[0][c], sqr[1][c], sqr[2][c])) for c in range(3)])
print('parities of the nine:', [[ 'e' if not odd(x) else 'o' for x in r] for r in sqr])
