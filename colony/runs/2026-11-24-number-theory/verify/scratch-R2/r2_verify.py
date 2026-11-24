"""Referee R2: independent exact re-verification of the finite steps of clause (iii).
Own quaternion code (Hamilton: B1=i, B2=j, B3=k, ij=k). Integers / Fractions only.
The certificate is parsed from proof-main.tex, not from check.py, then compared."""
import re, sys
from fractions import Fraction as Fr
from itertools import product, combinations
from math import gcd

CL = "/home/claude/zero-divisors/store/claims/synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear/"

def qm(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3,
            a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 + a2*b0 + a3*b1 - a1*b3,
            a0*b3 + a3*b0 + a1*b2 - a2*b1)
def cj(a): return (a[0], -a[1], -a[2], -a[3])
def nm(a): return sum(c*c for c in a)
def dot(a, b): return sum(x*y for x, y in zip(a, b))
def prim(v):
    g = 0
    for c in v: g = gcd(g, c)
    v = tuple(c//g for c in v)
    for c in v:
        if c: return v if c > 0 else tuple(-t for t in v)
# sanity of convention
I, J, K = (0,1,0,0), (0,0,1,0), (0,0,0,1)
assert qm(I, J) == K and qm(J, K) == I and qm(K, I) == J and qm(I, I) == (-1,0,0,0)

def Rmat(x):
    """Rotation n -> x n x^-1 on pure quaternions, as Fractions; columns images of i,j,k."""
    N = nm(x); cols = []
    for e in (I, J, K):
        y = qm(qm(x, e), cj(x)); assert y[0] == 0; cols.append([Fr(c, N) for c in y[1:]])
    return [[cols[c][r] for c in range(3)] for r in range(3)]

def rank(rows):
    rows = [list(map(Fr, r)) for r in rows]; rk = 0; ncol = len(rows[0]) if rows else 0
    for c in range(ncol):
        p = next((i for i in range(rk, len(rows)) if rows[i][c] != 0), None)
        if p is None: continue
        rows[rk], rows[p] = rows[p], rows[rk]
        for i in range(len(rows)):
            if i != rk and rows[i][c] != 0:
                f = rows[i][c] / rows[rk][c]
                rows[i] = [a - f*b for a, b in zip(rows[i], rows[rk])]
        rk += 1
    return rk

out = []
def ok(label, cond):
    out.append(("PASS " if cond else "FAIL ") + label); print(out[-1])
    if not cond: sys.exit(1)

# ---------------- Step 1
O = sorted({prim(v) for v in product((-1,0,1), repeat=4) if nm(v) in (1,2,4)})
ok("24 octahedral rays", len(O) == 24)
Os = set(O); idx = {r: i for i, r in enumerate(O)}
ok("O closed under product and conjugate (mod scalars)", all(prim(qm(a,b)) in Os for a in O for b in O) and all(prim(cj(a)) in Os for a in O))
biv = [r for r in O if r[0] == 0]
trip = [t for t in combinations(biv, 3) if all(dot(t[i], t[j]) == 0 for i in range(3) for j in range(i))]
ok("9 bivectors, 4 orthogonal triples", len(biv) == 9 and len(trip) == 4)
# triple closed: product of two = third up to scale
ok("each triple: a*b ~ c", all(prim(qm(t[0], t[1])) == t[2] or prim(qm(t[0], t[1])) == prim(t[2]) for t in trip))
frames = set()
for t in trip:
    for x in O:
        frames.add(tuple(sorted({prim(x)} | {prim(qm(n, x)) for n in t})))
ok("24 distinct 4-element frames inside O", len(frames) == 24 and all(len(f) == 4 for f in frames))
ok("they are orthogonal frames", all(dot(f[i], f[j]) == 0 for f in frames for i in range(4) for j in range(i)))
# also: ALL orthogonal frames among the 24 rays (not only cosets) -- are there more?
allfr = [f for f in combinations(O, 4) if all(dot(f[i], f[j]) == 0 for i in range(4) for j in range(i))]
ok("all orthogonal frames inside O are these 24 (count %d)" % len(allfr), set(allfr) == frames)
M = [[1 if r in f else 0 for r in O] for f in frames]
ok("rank of the 24 frame relations = 15", rank(M) == 15)
Rs = [[c for row in Rmat(x) for c in row] for x in O]
ok("R(O) spans 9-dim matrix space", rank(Rs) == 9)
ok("R kills each frame relation", all(all(sum(Rs[idx[r]][k] for r in f) == 0 for k in range(9)) for f in frames))
# dimension of W as image of Q[O]: 24 - 15 = 9 exactly matches
# ---------------- Step 2: parse certificate from the tex
tex = open(CL + "proof-main.tex").read()
cert_txt = tex[tex.index("The certificate of Step 2"):]
blocks = re.findall(r"\$q_\{F\} = (-?)\\tfrac\{(\d+)\}\{(\d+)\}\$ \((\d+) frames?\): (.*?)(?=\$q_\{F\}|The coefficients sum)", cert_txt, re.S)
cert = []
for sg, a, b, cnt, body in blocks:
    q = Fr(int(a), int(b)) * (-1 if sg else 1)
    fs = re.findall(r"\\\{(.*?)\\\}", body)
    ok("block q=%s has %s frames" % (q, cnt), len(fs) == int(cnt))
    for fstr in fs:
        vs = [tuple(int(t) for t in m.split(",")) for m in re.findall(r"\(([-\d, ]+)\)", fstr)]
        cert.append((q, tuple(vs)))
ok("34 frames parsed from tex", len(cert) == 34)
sys.path.insert(0, CL)
src = open(CL + "check.py").read()
ns = {}; exec(src[src.index("CERT = ["):src.index("TARGET =")], ns)
ck = sorted((Fr(n, d), tuple(fr)) for n, d, fr in ns["CERT"])
ok("tex certificate == check.py CERT", sorted(cert) == ck)
for q, f in cert:
    assert len(f) == 4 and all(prim(v) == v for v in f) and len(set(f)) == 4
ok("every certificate set is 4 distinct primitive vectors, pairwise orthogonal",
   all(dot(f[i], f[j]) == 0 for q, f in cert for i in range(4) for j in range(i)))
# frame = coset {x, a x, b x, ab x}: quotients by first member are pure, pairwise orthogonal, third ~ product
def is_coset(f):
    x = f[0]; u = [qm(v, cj(x)) for v in f[1:]]
    return all(t[0] == 0 for t in u) and all(dot(u[i], u[j]) == 0 for i in range(3) for j in range(i)) and prim(qm(u[0], u[1])) == prim(u[2])
ok("every certificate frame is a coset of a half-turn Klein group", all(is_coset(f) for q, f in cert))
tot = {}
for q, f in cert:
    for v in f: tot[v] = tot.get(v, 0) + q
tot = {v: c for v, c in tot.items() if c != 0}
ok("coefficient sum 2/5", sum(q for q, f in cert) == Fr(2, 5))
ok("target (2,1,0,0) has total 1", tot.get((2,1,0,0)) == 1)
rest = {v: c for v, c in tot.items() if v != (2,1,0,0)}
ok("all other nonzero totals are on O (18 of them)", set(rest) <= Os and len(rest) == 18)
allrays = {v for q, f in cert for v in f}
ok("rays outside O other than target occurring: %d (tex says 43)" % len(allrays - Os - {(2,1,0,0)}), len(allrays - Os - {(2,1,0,0)}) == 43)
listed = {Fr(1,2): [(0,0,0,1),(0,0,1,0)], Fr(1,5): [(0,1,0,-1),(0,1,0,1),(1,-1,0,0)],
          Fr(1,10): [(0,1,-1,0),(0,1,1,0),(1,-1,-1,1),(1,-1,1,-1)], Fr(-1,10): [(1,0,-1,0),(1,0,1,0),(1,1,-1,-1),(1,1,1,1)],
          Fr(-1,5): [(1,0,0,-1),(1,0,0,1),(1,1,-1,1),(1,1,0,0),(1,1,1,-1)]}
lst = {v: c for c, vs in listed.items() for v in vs}
ok("t_s values in the tex match the computed totals", lst == rest)
# Independent consequence: for EVERY quadratic form rho, value at target = (2/5) tr rho - sum t_s q(s)
def qv(rho, r): return Fr(sum(rho[i][j]*r[i]*r[j] for i in range(4) for j in range(4)), nm(r))
good = True
for i in range(4):
    for j in range(i, 4):
        rho = [[0]*4 for _ in range(4)]; rho[i][j] = rho[j][i] = 1
        tr = sum(rho[k][k] for k in range(4))
        good &= qv(rho, (2,1,0,0)) == Fr(2,5)*tr - sum(c*qv(rho, v) for v, c in rest.items())
ok("certificate consistent with all 10 quadratic forms", good)
# conjugates by O
six = {(2,1,0,0),(2,-1,0,0),(2,0,1,0),(2,0,-1,0),(2,0,0,1),(2,0,0,-1)}
conj = set()
for u in O:
    z = qm(qm(u, (2,1,0,0)), cj(u)); g = nm(u); assert all(c % g == 0 for c in z)
    conj.add(prim(tuple(c//g for c in z)))
ok("conjugates of 2+B1 by O are exactly the 6 rays 2 +- B_k", conj == {prim(s) for s in six})
# ---------------- Step 3
cnt = 0; good = True
for y in product(range(5), repeat=4):
    if nm(y) % 5 == 0:
        cnt += 1
        good &= any(all(c % 5 == 0 for c in qm(cj(p), y)) for p in six)
ok("mod-5 table: all %d classes of norm 0 mod 5 have a left divisor among the six" % cnt, good and cnt == 145)
def factor(y):
    fs = []
    while nm(y) > 1:
        for p in sorted(six):
            z = qm(cj(p), y)
            if all(c % 5 == 0 for c in z):
                fs.append(p); y = tuple(c//5 for c in z); break
        else: return None
    return fs, y
units = {(1,0,0,0),(-1,0,0,0),(0,1,0,0),(0,-1,0,0),(0,0,1,0),(0,0,-1,0),(0,0,0,1),(0,0,0,-1)}
good = True; n625 = 0
for y in product(range(-25, 26), repeat=4):
    if nm(y) == 625:
        n625 += 1; r = factor(y); good &= r is not None and r[1] in units and len(r[0]) == 4
ok("all %d integer quaternions of norm 625 factor into 4 of the six and a unit" % n625, good and n625 == 8*(1+5+25+125+625))
# ---------------- Step 4 on all integer bivectors with entries <= 8 (primitive), incl. norms divisible by 2, 5
def step4(n, k):
    N = nm((0,)+n); Np = N
    e = 0
    while Np % 5 == 0: Np //= 5; e += 1
    base = [2,0,0,0]; base[k] = 1; base = tuple(base)
    g = base; s = 1
    while g[k] % Np != 0:
        g = qm(g, base); s += 1
        if s > 10**5: return None
    if g[0] % 5 == 0 or g[k] % 5 == 0: return "alpha/beta divisible by 5"
    nq = (0,)+n
    Y = qm(qm(nq, g), cj(nq))     # = n g ~n = -N n g n^-1 ... times scalar
    # claimed integer representative: 5^e alpha - (beta/N') n B n
    B = [0,0,0,0]; B[k] = 1
    nBn = qm(qm(nq, tuple(B)), nq)
    y = tuple(5**e * (g[0] if i == 0 else 0) - (g[k]//Np) * nBn[i] for i in range(4))
    if prim(y) != prim(Y): return "class mismatch"
    if nm(y) != 5**(2*e+s): return "norm mismatch"
    r = factor(y)
    if r is None: return "factor fail"
    return s
bad = []; ns5 = ns2 = 0; tested = 0; maxs = 0
for n in product(range(-8, 9), repeat=3):
    if n == (0,0,0) or prim((0,)+n) != (0,)+n: continue
    N = nm((0,)+n); ns5 += N % 5 == 0; ns2 += N % 2 == 0; tested += 1
    for k in (1, 2):
        r = step4(n, k)
        if not isinstance(r, int): bad.append((n, k, r))
        else: maxs = max(maxs, r)
ok("Step 4 on %d primitive integer bivectors (|entries|<=8; %d with 5|N, %d with 2|N), axes B1,B2: all conjugates integer of norm 5^(2e+s) and factor (max s=%d)" % (tested, ns5, ns2, maxs), not bad)
open("/home/claude/zero-divisors/colony/runs/2026-11-24-number-theory/verify/scratch-R2/r2_verify.log", "w").write("\n".join(out) + "\n")
