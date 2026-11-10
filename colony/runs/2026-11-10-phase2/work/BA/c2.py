from ba import *
def modes(m):
    sq = tuple(s for _ in range(m) for s in (1, -1))
    e = [GA.gen(2 * k) for k in range(m)]; f = [GA.gen(2 * k + 1) for k in range(m)]
    p = [GA.mul(f[k], e[k], sq) for k in range(m)]
    return sq, e, f, p
def lin(*terms):
    r = {}
    for c, x in terms: r = GA.add(r, GA.scal(F(c), x))
    return clean(r)
# --- one mode: positivity needed
sq, e, f, p = modes(1)
P = lin((F(1,2), ONE), (F(1,2), p[0]))
N = GA.sub(ONE, P)
for t in (F(1), F(1,3)):
    m = lin((1, ONE), (1, p[0]), (t, e[0]))
    lam = lambda x: s0(prod(sq, m, x))
    assert dag(m, sq) == m and lam(ONE) == 1 and lam(P) == 1 and lam(e[0]) == t
    y = lin((1, N), (-t, prod(sq, e[0], N)))   # try
    best = None
    for a in range(-3, 4):
        for b in range(-3, 4):
            for c in range(-3, 4):
                for d in range(-3, 4):
                    y = lin((a, ONE), (b, e[0]), (c, f[0]), (d, p[0]))
                    v = lam(prod(sq, y, dag(y, sq)))
                    if best is None or v < best[0]: best = (v, (a, b, c, d))
    print('one mode, t=', t, 'min lam(yy+) on small integers', best)
# reality needed
mu = lambda x: s0(prod(sq, P, x)) * 2 + s0(prod(sq, f[0], x))
print('no reality: mu(1), mu(P), mu(f), omega_P(f)', mu(ONE), mu(P), mu(f[0]), 2 * s0(prod(sq, P, f[0])))
import random
random.seed(3)
def rnd(n, sq, lo=-3, hi=3):
    return clean({b: F(random.randint(lo, hi)) for b in GA.all_blades(n)})
ok = True
for _ in range(50):
    y = rnd(2, sq); yy = prod(sq, y, dag(y, sq)); ok = ok and mu(yy) >= 0
print('mu nonneg on yy+ (50 samples):', ok)
# --- two modes: vacuum orbit, rational weights
sq, e, f, p = modes(2)
P0 = clean(prod(sq, lin((F(1,2), ONE), (F(1,2), p[0])), lin((F(1,2), ONE), (F(1,2), p[1]))))
v = [lin((F(1,2), e[k]), (F(1,2), f[k])) for k in range(2)]
w = [lin((F(1,2), e[k]), (F(-1,2), f[k])) for k in range(2)]
assert all(clean(prod(sq, v[k], P0)) == {} for k in range(2)), 'v kills vacuum'
assert dag(v[0], sq) == w[0]
tr = lambda x: s0(x)
def atom(x):
    y = clean(prod(sq, x, P0, dag(x, sq)))
    lamb = tr(prod(sq, P0, dag(x, sq), x)) / tr(P0)
    return GA.scal(1 / lamb, y), lamb
for _ in range(5):
    x = rnd(4, sq); Px, l1 = atom(x)
    assert dag(Px, sq) == Px and clean(prod(sq, Px, Px)) == clean(Px) and tr(Px) == tr(P0)
    for _ in range(3):
        y = rnd(4, sq)
        assert clean(GA.sub(prod(sq, Px, y, Px), GA.scal(tr(prod(sq, Px, y)) / tr(Px), Px))) == {}
    x2 = rnd(4, sq); Q, l2 = atom(x2)
    wgt = tr(prod(sq, Px, Q)) / tr(Px)
    # amplitude form: P0 x+ x2 P0 = c P0 ; weight = c c' /(l1 l2)
    c = tr(prod(sq, P0, dag(x, sq), x2)) / tr(P0); c2 = tr(prod(sq, P0, dag(x2, sq), x)) / tr(P0)
    assert wgt == c * c2 / (l1 * l2) and c == c2 and 0 <= wgt <= 1
    print('weight', wgt, 'norms', l1, l2, 'overlap', c)
# --- even state exceeding 2 with one mode per party and mixed-parity directions
G = prod(sq, p[0], p[1])
Eav = lambda x: clean(GA.scal(F(1,2), GA.add(x, prod(sq, G, x, G))))
a1, a2 = e[0], p[0]
e2t = prod(sq, e[1], p[0])
b1 = lin((F(3,5), e2t), (F(4,5), p[1])); b2 = lin((F(4,5), e2t), (F(-3,5), p[1]))
for o in (a1, a2, b1, b2): assert dag(o, sq) == o and clean(prod(sq, o, o)) == ONE
for a in (a1, a2):
    for b in (b1, b2): assert GA.commutes(a, b, sq)
C = clean(GA.add(prod(sq, a1, b1), prod(sq, a1, b2), prod(sq, a2, b1), GA.neg(prod(sq, a2, b2))))
EC = Eav(C); print('C =', C); print('E(C) =', EC)
Cav = clean(GA.add(prod(sq, Eav(a1), Eav(b1)), prod(sq, Eav(a1), Eav(b2)), prod(sq, Eav(a2), Eav(b1)), GA.neg(prod(sq, Eav(a2), Eav(b2)))))
print('CHSH of averaged directions =', Cav)
u = prod(sq, e[1], f[0]); print('u=', u, 'u^2', prod(sq,u,u), 'sa', dag(u,sq)==u)
for su in (1, -1):
    for sg in (1, -1):
        R = clean(prod(sq, lin((F(1,4), ONE), (F(su,4), u)), lin((1, ONE), (sg, G))))
        assert dag(R, sq) == R and clean(prod(sq, R, R)) == R and Eav(R) == R
        print(su, sg, 'even atom? tr', tr(R), 'value of C', tr(prod(sq, R, C)) / tr(R), 'corner', corner_dims(sq, R))
# --- boost keeps null pair lines, changes split
sq1, e_, f_, p_ = modes(1)
v1 = lin((F(1,2), e_[0]), (F(1,2), f_[0])); w1 = lin((F(1,2), e_[0]), (F(-1,2), f_[0]))
t = F(4)
ep = clean(GA.add(GA.scal(t, v1), GA.scal(1/t, w1))); fp = clean(GA.sub(GA.scal(t, v1), GA.scal(1/t, w1)))
print('boosted e,f:', ep, fp, 'squares', prod(sq1, ep, ep), prod(sq1, fp, fp), 'anticommute', GA.anticommutes(ep, fp, sq1), 'parity same', clean(prod(sq1, fp, ep)) == p_[0])
