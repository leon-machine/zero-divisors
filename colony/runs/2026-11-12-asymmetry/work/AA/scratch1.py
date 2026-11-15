import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
from itertools import combinations
import GA
SQ = GA.sig(5, 5)
def mul(*xs):
    r = xs[0]
    for x in xs[1:]:
        r = GA.mul(r, x, SQ)
    return r
def comm(a, b): return GA.sub(mul(a, b), mul(b, a))
e = [GA.gen(i) for i in range(5)]; f = [GA.gen(5 + i) for i in range(5)]
v = [GA.scal(F(1, 2), GA.add(e[i], f[i])) for i in range(5)]
w = [GA.scal(F(1, 2), GA.sub(e[i], f[i])) for i in range(5)]
one = GA.sc(1)
n = [mul(v[i], w[i]) for i in range(5)]
def X(x):  # f_i -> -f_i
    return {b: c * (-1) ** sum(1 for i in b if i >= 5) for b, c in x.items()}
def dag(x): return X(GA.reverse(x))
# switch relations
for i in range(5):
    assert mul(v[i], v[i]) == {} and mul(w[i], w[i]) == {}
    for j in range(5):
        ac = GA.add(mul(v[i], w[j]), mul(w[j], v[i]))
        assert ac == (one if i == j else {})
    assert GA.eq(X(v[i]), w[i]) and GA.eq(X(w[i]), v[i])
# inner: u = e1..e5
u = mul(*e); uinv = GA.scal(1 / mul(u, u)[()], u)
print('u^2', mul(u, u))
for x in v + w:
    assert GA.eq(mul(u, x, uinv), X(x))
print('X = Ad(e1..e5) ok')
k = GA.add(n[0], n[1], n[2]); j = GA.add(n[3], n[4])
BL = GA.sub(one, GA.scal(F(2, 3), k))
par = lambda idx: mul(*[GA.sub(one, GA.scal(2, n[i])) for i in idx])
P3 = par([0, 1, 2]); Gam = par(range(5)); chi = GA.neg(par([3, 4]))
assert GA.eq(mul(chi, Gam), GA.neg(P3))
nB = GA.scal(F(1, 4), GA.sub(BL, P3)); nL = GA.scal(F(1, 4), GA.sub(GA.neg(P3), GA.scal(3, BL)))
print('nB grades', sorted({len(b) for b in nB}), nB)
print('nL grades', sorted({len(b) for b in nL}))
Y = GA.add(GA.scal(F(1, 2), GA.sub(j, one)), GA.scal(F(1, 2), BL))
T = mul(*v); Td = mul(*reversed(w))
for name, q in [('nB', nB), ('nL', nL), ('BL', BL), ('Y', Y)]:
    print(name, 'X-odd', GA.eq(X(q), GA.neg(q)))
print('X chi = chi', GA.eq(X(chi), chi), 'X Gam = -Gam', GA.eq(X(Gam), GA.neg(Gam)), 'X P3 = -P3', GA.eq(X(P3), GA.neg(P3)))
print('X(T) == Td', GA.eq(X(T), Td), 'X(T) == rev T', GA.eq(X(T), GA.reverse(T)), 'dag T == Td', GA.eq(dag(T), Td))
print('[nB,T]=0', comm(nB, T) == {}, '[BL,T]=-2T', GA.eq(comm(BL, T), GA.scal(-2, T)), '[nL,T]=2T', GA.eq(comm(nL, T), GA.scal(2, T)), '[Y,T]', comm(Y, T) == {})
# bivectors of so(10): gamma_m gamma_n
gens = e + f
biv = [mul(gens[a], gens[b]) for a, b in combinations(range(10), 2)]
blades = sorted({b for q in [nB] for x in biv for b in comm(q, x)} | {()})
def cent_dim(q, basis):
    imgs = [comm(q, x) for x in basis]
    bl = sorted({b for im in imgs for b in im})
    rk = GA.rank_of_vectors([[im.get(b, F(0)) for b in bl] for im in imgs]) if bl else 0
    return len(basis) - rk
for name, q in [('nB', nB), ('nL', nL), ('BL', BL), ('k', k), ('P3', P3), ('chi', chi), ('Y', Y), ('N', GA.add(k, j))]:
    print('dim of bivectors commuting with', name, '=', cent_dim(q, biv))
# typed generators
pairs = [0, 1, 2]; slots = [3, 4]
u3 = [mul(v[a], w[b]) for a in pairs for b in pairs if a != b] + [GA.sub(n[a], GA.scal(F(1, 2), one)) for a in pairs]
lq = [mul(v[a], v[b]) for a, b in combinations(pairs, 2)] + [mul(w[a], w[b]) for a, b in combinations(pairs, 2)]
so4 = [mul(v[3], w[4]), mul(v[4], w[3]), mul(v[3], v[4]), mul(w[4], w[3]), GA.sub(n[3], GA.scal(F(1, 2), one)), GA.sub(n[4], GA.scal(F(1, 2), one))]
mix = [mul(x[s], y[a]) for s in slots for a in pairs for x in (v, w) for y in (v, w)]
print(len(u3), len(lq), len(so4), len(mix))
print('u3,so4 commute with nB:', all(comm(nB, x) == {} for x in u3 + so4))
print('lq: none commutes with nB', all(comm(nB, x) != {} for x in lq), ' commute with P3', all(comm(P3, x) == {} for x in lq),
      ' [nB,x]=1/4[BL,x]', all(GA.eq(comm(nB, x), GA.scal(F(1, 4), comm(BL, x))) for x in lq))
print('mix: none commutes with nB', all(comm(nB, x) != {} for x in mix), ' anticommute with P3', all(GA.add(mul(P3, x), mul(x, P3)) == {} for x in mix), 'and chi', all(GA.add(mul(chi, x), mul(x, chi)) == {} for x in mix))
for x in mix[:4] + lq[:1] + lq[3:4]:
    cb = comm(nB, x); cl = comm(nL, x); ck = comm(k, x)
    r = lambda c: None if c == {} else next(iter(c.values())) / x[next(iter(c))]
    print('shift k', r(ck), 'nB', r(cb), 'nL', r(cl), 'prop', all(GA.eq(c, GA.scal(r(c), x)) for c in (cb, cl, ck) if c))
# vectors
print('slot vectors commute with nB', all(comm(nB, x) == {} for s in slots for x in (v[s], w[s])), '; pair vectors do not', all(comm(nB, x) != {} for a in pairs for x in (v[a], w[a])))
# J lift
Jb = GA.scal(F(1, 2), GA.add(*[mul(e[a], f[a]) for a in pairs]))
print('k-3/2 = -1/2 sum e f', GA.eq(GA.sub(k, GA.scal(F(3, 2), one)), GA.neg(Jb)), ' BL = (1/3) sum e_a f_a', GA.eq(BL, GA.scal(F(2, 3), Jb)))
# adjoint
print('dag = X o reverse: v<->w', all(GA.eq(dag(v[i]), w[i]) for i in range(5)))
# omega and vacuum
h = [GA.sub(mul(w[i], v[i]), mul(v[i], w[i])) for i in range(5)]
for m in range(1, 6):
    om = mul(*h[:m]); print(m, 'X omega = ', '+' if GA.eq(X(om), om) else '-' if GA.eq(X(om), GA.neg(om)) else '?')
