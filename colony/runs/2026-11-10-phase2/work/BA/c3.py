from ba import *
import time
def modes(m):
    sq = tuple(s for _ in range(m) for s in (1, -1))
    e = [GA.gen(2 * k) for k in range(m)]; f = [GA.gen(2 * k + 1) for k in range(m)]
    p = [clean(GA.mul(f[k], e[k], sq)) for k in range(m)]
    return sq, e, f, p
def lin(*terms):
    r = {}
    for c, x in terms: r = GA.add(r, GA.scal(F(c), x))
    return clean(r)
def frame(m, A, Ainv):
    """generators of the split adapted to the null pairs, for A in GL_m acting on W (columns), A^-T on W'."""
    sq, e, f, p = modes(m)
    v = [lin((F(1,2), e[k]), (F(1,2), f[k])) for k in range(m)]
    w = [lin((F(1,2), e[k]), (F(-1,2), f[k])) for k in range(m)]
    vn = [lin(*[(A[i][j], v[i]) for i in range(m)]) for j in range(m)]
    wn = [lin(*[(Ainv[j][i], w[i]) for i in range(m)]) for j in range(m)]
    en = [clean(GA.add(vn[j], wn[j])) for j in range(m)]; fn = [clean(GA.sub(vn[j], wn[j])) for j in range(m)]
    return sq, en, fn
def refl(m, A, Ainv):
    """images of the old generators under the reflection (+1 on span e', -1 on span f')."""
    sq, en, fn = frame(m, A, Ainv)
    gens = [GA.gen(i) for i in range(2 * m)]
    out = []
    for g in gens:
        r = {}
        for j in range(m):
            ce = s0(prod(sq, g, en[j])) ; r = GA.add(r, GA.scal(ce, en[j]))          # (g . e') e' / (e'^2 = 1)
            cf = s0(prod(sq, g, fn[j])) ; r = GA.add(r, GA.scal(cf, fn[j]))          # -(g.f')/(f'^2=-1) f' = +(g.f') f'
        out.append(clean(r))
    return sq, out
def dag_split(sq, images, x):
    r = {}
    for b, c in x.items():
        y = ONE
        for i in reversed(b): y = GA.mul(y, images[i], sq)
        r = GA.add(r, GA.scal(c, y))
    return clean(r)
def common_real_functionals(m, mats):
    sq = tuple(s for _ in range(m) for s in (1, -1))
    blades = GA.all_blades(2 * m); rows = []
    for A, Ainv in mats:
        _, images = refl(m, A, Ainv)
        for b in blades:
            d = clean(GA.sub(blade(b), dag_split(sq, images, blade(b))))
            if d: rows.append([d.get(bb, F(0)) for bb in blades])
    return len(blades) - GA.rank_of_vectors(rows), GA.field_kernel(rows) if rows else None
I1 = ([[F(1)]], [[F(1)]]); T4 = ([[F(4)]], [[F(1,4)]])
# sanity: identity split reproduces the blade inverse; t = 4 reproduces the boosted frame
sq, im = refl(1, *I1); print('identity images', im)
sq, en, fn = frame(1, *T4); print('t=4 frame', en, fn)
print('l=1: dims', common_real_functionals(1, [I1])[0], common_real_functionals(1, [I1, T4])[0])
def inv2(A):
    a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]; det = a * d - b * c
    return [[d / det, -b / det], [-c / det, a / det]]
M2 = [[[F(1), F(0)], [F(0), F(1)]], [[F(2), F(0)], [F(0), F(1)]], [[F(1), F(0)], [F(0), F(3)]], [[F(1), F(1)], [F(0), F(1)]], [[F(1), F(0)], [F(1), F(1)]]]
mats2 = [(A, inv2(A)) for A in M2]
for n in range(1, 6):
    t = time.time(); d, ker = common_real_functionals(2, mats2[:n]); print('l=2, first', n, 'splits: dim', d, round(time.time() - t, 2))
sq, e, f, p = modes(2); blades = GA.all_blades(4)
for kv in ker: print({b: c for b, c in zip(blades, kv) if c})
# B3 finite facts: pair state coherence between record sectors, and e2 swaps the record sectors
v = [lin((F(1,2), e[k]), (F(1,2), f[k])) for k in range(2)]; w = [lin((F(1,2), e[k]), (F(-1,2), f[k])) for k in range(2)]
c, s = F(3,5), F(4,5); r = c*c - s*s
rho = clean(GA.add(prod(sq, lin((F(1,4), ONE), (F(1,4), prod(sq, p[0], p[1]))), lin((1, ONE), (r, p[0]))), GA.scal(c*s, GA.add(prod(sq, w[0], w[1]), prod(sq, v[1], v[0])))))
print('rho projector', clean(prod(sq, rho, rho)) == rho, dag(rho, sq) == rho, 'tr', s0(rho))
Rp = lin((F(1,2), ONE), (F(1,2), p[1])); Rm = lin((F(1,2), ONE), (F(-1,2), p[1]))
x = clean(GA.add(prod(sq, w[0], w[1]), prod(sq, v[1], v[0])))
print('value on R+ x R- :', 4 * s0(prod(sq, rho, Rp, x, Rm)), ' on R- x R+:', 4 * s0(prod(sq, rho, Rm, x, Rp)))
print('e2 swaps sectors', clean(prod(sq, e[1], Rp, e[1])) == Rm)
