"""H1 probe 3: dimension of the space of spin-equivariant quadratic maps S -> V (and S -> scalars),
causal towers of dimension 3, 4, 5. Exact linear algebra over Q."""
import sys, time
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA

def setup(p, q):
    n = p + q; sq = GA.sig(p, q)
    t = 0 if p == 1 else p; a = 1 if t == 0 else 0
    et, ea = GA.gen(t), GA.gen(a)
    f = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.mul(et, ea, sq)))
    blades = GA.all_blades(n)
    idx = {b: i for i, b in enumerate(blades)}
    def vec(x):
        v = [F(0)] * len(blades)
        for b, c in x.items():
            v[idx[b]] = c
        return v
    # basis of S = Cl^0 f
    basis = []
    for b in blades:
        if len(b) % 2 == 0:
            x = GA.mul({b: F(1)}, f, sq)
            if GA.mat_rank([vec(y) for y in basis] + [vec(x)]) > len(basis):
                basis.append(x)
    return n, sq, et, f, blades, vec, basis

def coords(x, basis, vec):
    """coordinates of x in the span of basis (exact solve)."""
    cols = [vec(b) for b in basis]
    m = len(cols); N = len(cols[0])
    A = [[cols[j][i] for j in range(m)] + [vec(x)[i]] for i in range(N)]
    # gaussian elimination
    r = 0; piv = []
    for c in range(m):
        pr = next((i for i in range(r, N) if A[i][c] != 0), None)
        if pr is None: continue
        A[r], A[pr] = A[pr], A[r]
        A[r] = [v / A[r][c] for v in A[r]]
        for i in range(N):
            if i != r and A[i][c] != 0:
                A[i] = [u - A[i][c] * v for u, v in zip(A[i], A[r])]
        piv.append(c); r += 1
    assert all(A[i][m] == 0 for i in range(r, N)), "not in span"
    out = [F(0)] * m
    for i, c in enumerate(piv): out[c] = A[i][m]
    return out

def nullity(rows, ncols):
    return ncols - GA.mat_rank(rows) if rows else ncols

def run(p, q):
    n, sq, et, f, blades, vec, basis = setup(p, q)
    d = len(basis)
    biv = [{b: F(1)} for b in blades if len(b) == 2]
    Bm = []
    for B in biv:
        cols = [coords(GA.mul(B, e, sq), basis, vec) for e in basis]   # cols[i][l]
        Bm.append(cols)
    ad = []
    for B in biv:
        cols = []
        for m in range(n):
            c = GA.sub(GA.mul(B, GA.gen(m), sq), GA.mul(GA.gen(m), B, sq))
            cols.append([c.get((k,), F(0)) for k in range(n)])
        ad.append(cols)                                                # ad[B][m][k]
    pairs = [(i, j) for i in range(d) for j in range(i, d)]
    pid = {pr: x for x, pr in enumerate(pairs)}
    def P(i, j): return pid[(i, j) if i <= j else (j, i)]
    # vector-valued
    nun = len(pairs) * n
    rows = []
    for bi in range(len(biv)):
        for (i, j) in pairs:
            for k in range(n):
                row = [F(0)] * nun
                for l in range(d):
                    if Bm[bi][i][l] != 0: row[P(l, j) * n + k] += Bm[bi][i][l]
                    if Bm[bi][j][l] != 0: row[P(i, l) * n + k] += Bm[bi][j][l]
                for m in range(n):
                    if ad[bi][m][k] != 0: row[P(i, j) * n + m] -= ad[bi][m][k]
                if any(row): rows.append(row)
    nv = nullity(rows, nun)
    # scalar-valued
    rows = []
    for bi in range(len(biv)):
        for (i, j) in pairs:
            row = [F(0)] * len(pairs)
            for l in range(d):
                if Bm[bi][i][l] != 0: row[P(l, j)] += Bm[bi][i][l]
                if Bm[bi][j][l] != 0: row[P(i, l)] += Bm[bi][j][l]
            if any(row): rows.append(row)
    ns = nullity(rows, len(pairs))
    return d, nv, ns

for sg in [(2, 1), (1, 2), (1, 3), (3, 1), (4, 1), (1, 4)]:
    t0 = time.time(); print(sg, 'dim S, dim equivariant quadratic S->V, dim invariant quadratic S->R:', run(*sg), round(time.time() - t0, 1), 's', flush=True)
