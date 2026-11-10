import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as F
from itertools import product
import GA

# basis 0..5 <-> e3..e8 ; f_k = 2k, j f_k = 2k+1
def jmap(m):  # j as signed perm
    return (m + 1, 1) if m % 2 == 0 else (m - 1, -1)

def from_complex(u):
    # u: 3x3 entries in {0, 1, -1, 'i', '-i'} as (a, b) pairs
    img = {}
    for l in range(3):
        col = {}
        for k in range(3):
            a, b = u[k][l]
            if a: col[2 * k] = a
            if b: col[2 * k + 1] = b
        assert len(col) == 1
        (m, s), = col.items()
        img[2 * l] = (m, s)
        jm, js = jmap(m)
        img[2 * l + 1] = (jm, js * s)
    return tuple(img[m] for m in range(6))

def compose(g, h):  # g after h
    out = []
    for m in range(6):
        n, s = h[m]
        n2, s2 = g[n]
        out.append((n2, s * s2))
    return tuple(out)

Z, O, M, I, MI = (0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)
gens = [from_complex([[I, Z, Z], [Z, MI, Z], [Z, Z, O]]),
        from_complex([[O, Z, Z], [Z, I, Z], [Z, Z, MI]]),
        from_complex([[Z, Z, O], [O, Z, Z], [Z, O, Z]]),
        from_complex([[Z, O, Z], [O, Z, Z], [Z, Z, M]])]
ident = tuple((m, 1) for m in range(6))
G = {ident}
frontier = [ident]
while frontier:
    new = []
    for g in frontier:
        for h in gens:
            k = compose(h, g)
            if k not in G:
                G.add(k); new.append(k)
    frontier = new
G = sorted(G)
print("order", len(G))

def tens_inv(d):
    seen = {}
    vecs = []
    for t in product(range(6), repeat=d):
        if t in seen: continue
        orb = {}
        ok = True
        for g in G:
            s = 1
            img = []
            for a in t:
                n, sg = g[a]; img.append(n); s *= sg
            img = tuple(img)
            if img in orb and orb[img] != s: ok = False
            orb[img] = s
        for k in orb: seen[k] = True
        if ok:
            vecs.append(orb)
    return vecs

def trace_count(d):
    return sum(F(sum(1 for m in range(6) if g[m] == (m, 1)) - sum(1 for m in range(6) if g[m] == (m, -1))) ** d for g in G) / len(G)

for d in range(1, 6):
    v = tens_inv(d)
    print(d, len(v), trace_count(d))

# ---- su(3) from GA: bivectors of e3..e8 commuting with J and with Re Omega
S9 = (1,) * 9
def e(*idx):
    r = GA.sc(1)
    for i in idx: r = GA.mul(r, GA.gen(i), S9)
    return r
J = GA.add(e(3, 4), e(5, 6), e(7, 8))
ReO = GA.add(e(3, 5, 7), GA.scal(-1, e(3, 6, 8)), GA.scal(-1, e(4, 5, 8)), GA.scal(-1, e(4, 6, 7)))
ImO = GA.add(e(4, 5, 7), e(3, 6, 7), e(3, 5, 8), GA.scal(-1, e(4, 6, 8)))
pairs = [(a, b) for a in range(3, 9) for b in range(a + 1, 9)]
def comm(x, y): return GA.sub(GA.mul(x, y, S9), GA.mul(y, x, S9))
# linear conditions on coefficients c_ab
rows = {}
for k, (a, b) in enumerate(pairs):
    for tgt in (J, ReO):
        c = comm(e(a, b), tgt)
        for blade, val in c.items():
            rows.setdefault((id(tgt), blade), [F(0)] * 15)[k] += val
Mx = list(rows.values())
ker = GA.field_kernel(Mx)
print("dim su3", len(ker))
su3 = [GA.add(*[GA.scal(v[k], e(*pairs[k])) for k in range(15) if v[k]]) for v in ker]
for B in su3: print(B)
def vec_action(B):
    # X(v) = (vB - Bv)/2 on e3..e8 -> 6x6 matrix
    Mt = [[F(0)] * 6 for _ in range(6)]
    for m in range(6):
        v = GA.gen(m + 3)
        w = GA.scal(F(1, 2), GA.sub(GA.mul(v, B, S9), GA.mul(B, v, S9)))
        for blade, val in w.items():
            assert len(blade) == 1
            Mt[blade[0] - 3][m] = val
    return Mt
X = [vec_action(B) for B in su3]

def apply_der(Xm, vec, d):
    out = {}
    for t, c in vec.items():
        for pos in range(d):
            a = t[pos]
            for n in range(6):
                x = Xm[n][a]
                if x:
                    t2 = t[:pos] + (n,) + t[pos + 1:]
                    out[t2] = out.get(t2, 0) + c * x
    return {k: v for k, v in out.items() if v}

def su3_inv_dim(d):
    vs = tens_inv(d)
    rowsd = {}
    for j, v in enumerate(vs):
        for gi, Xm in enumerate(X):
            for t, c in apply_der(Xm, v, d).items():
                rowsd.setdefault((gi, t), [F(0)] * len(vs))[j] += c
    if not rowsd: return len(vs), len(vs)
    k = GA.field_kernel(list(rowsd.values()))
    return len(vs), len(k)
for d in range(1, 6):
    print("d", d, su3_inv_dim(d))
