import sys, os, importlib.util, time
LAB = "/home/claude/zero-divisors"
sys.path.insert(0, os.path.join(LAB, "lib"))
import tp_premise, GA
tp_premise.configure(os.path.join(LAB, "store"))
spec = importlib.util.spec_from_file_location("ck", "check.py")
ck = importlib.util.module_from_spec(spec); spec.loader.exec_module(ck)
globals().update({k: v for k, v in vars(ck).items() if not k.startswith("__")})
from fractions import Fraction as F
PRIME = 1000003
def rank_mod(rows, p):
    piv, r = {}, 0
    for row in rows:
        row = {j: c % p for j, c in row.items() if c % p}
        while row:
            j = min(row)
            if j in piv:
                c = row[j]
                for k, v in piv[j].items():
                    nv = (row.get(k, 0) - c * v) % p
                    if nv: row[k] = nv
                    else: row.pop(k, None)
            else:
                inv = pow(row[j], p - 2, p)
                piv[j] = {k: (v * inv) % p for k, v in row.items()}
                r += 1
                break
    return r
t0 = time.time()
# scalar form F(u, v; h; xi; p) = (u ^ v) . K(h, xi, p): coefficients on (blade pair a<b, sym pair c<=d, e, f)
blades = [(a, b) for a in range(D) for b in range(a + 1, D)]
prs = [(a, b) for a in range(D) for b in range(a, D)]
index, basis = {}, []
for bl in blades:
    for P in prs:
        for e in range(D):
            for f in range(D):
                index[(bl, P, e, f)] = len(basis); basis.append((bl, P, e, f))
print(len(basis))
def canon(t6):
    a, b = t6[0], t6[1]
    if a == b: return None, 0
    sgn = 1
    if a > b: a, b = b, a; sgn = -1
    return ((a, b), tuple(sorted(t6[2:4])), t6[4], t6[5]), sgn
rows = []
for mu in range(D):
    for nu in range(mu + 1, D):
        G = mul(E[mu], E[nu], S)
        Xm = []
        for a in range(D):
            img = g1(scal(F(1, 2), sub(mul(G, E[a], S), mul(E[a], G, S))))
            Xm.append([F(ETA[b]) * dot(img, E[b]) for b in range(D)])
        for I in basis:
            t6 = [I[0][0], I[0][1], I[1][0], I[1][1], I[2], I[3]]
            row = {}
            for slot in range(6):
                for b in range(D):
                    c = Xm[t6[slot]][b]
                    if c:
                        t = list(t6); t[slot] = b
                        key, sgn = canon(t)
                        if key is None: continue
                        j = index[key]
                        row[j] = row.get(j, 0) + sgn * int(c)
            row = {j: c for j, c in row.items() if c}
            if row: rows.append(row)
print(len(rows), time.time() - t0)
print("nullity", len(basis) - rank_mod(rows, PRIME), time.time() - t0)
