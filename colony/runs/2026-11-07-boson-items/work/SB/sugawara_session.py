"""SB, bos.dynamics: is the window kinetic energy H0 = sum_j j n_j a quadratic form in the density modes
plus a function of the number?  Exact linear algebra over the blades of Cl(M, M). Kill condition K5."""
import sys; sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
mul, add, sub, neg, scal, sc, gen, eq = GA.mul, GA.add, GA.sub, GA.neg, GA.scal, GA.sc, GA.gen, GA.eq
def dag(x, sq):
    out = {}
    for b, c in x.items():
        g = len(b); s = (-1) ** (g * (g - 1) // 2) * (-1) ** sum(1 for i in b if sq[i] == -1)
        out[b] = c * s
    return {b: c for b, c in out.items() if c != 0}
def solve(cols, target):
    """least structure: Gaussian elimination for sum_i x_i cols[i] = target; returns x or None."""
    keys = sorted(set(k for c in cols for k in c) | set(target))
    A = [[c.get(k, F(0)) for c in cols] + [target.get(k, F(0))] for k in keys]
    n = len(cols); r = 0; piv = []
    for c in range(n):
        p = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        A[r] = [x / A[r][c] for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                A[i] = [a - A[i][c] * b for a, b in zip(A[i], A[r])]
        piv.append(c); r += 1
    if any(all(A[i][j] == 0 for j in range(n)) and A[i][n] != 0 for i in range(len(A))): return None
    x = [F(0)] * n
    for i, c in enumerate(piv): x[c] = A[i][n]
    return x

for M in range(2, 7):
    sq = tuple([1, -1] * M)
    v = [scal(F(1, 2), add(gen(2 * j), gen(2 * j + 1))) for j in range(M)]
    w = [scal(F(1, 2), sub(gen(2 * j), gen(2 * j + 1))) for j in range(M)]
    n = [mul(v[j], w[j], sq) for j in range(M)]
    H0 = add(*[scal(F(j), n[j]) for j in range(M)])
    Nn = add(*n)
    rho = {q: add(*[mul(v[k], w[k + q], sq) for k in range(M - q)]) for q in range(1, M)}
    cols, names = [], []
    for q in range(1, M):
        cols.append(mul(dag(rho[q], sq), rho[q], sq)); names.append(f"rho{q}* rho{q}")
        cols.append(mul(rho[q], dag(rho[q], sq), sq)); names.append(f"rho{q} rho{q}*")
    Np = sc(1)
    for d in range(M + 1):
        cols.append(Np); names.append(f"N^{d}"); Np = mul(Np, Nn, sq)
    x = solve(cols, H0)
    print(f"M={M}: H0 in span(rho_q* rho_q, rho_q rho_q*, N^d)? ", "NO" if x is None else
          "YES " + ", ".join(f"{nm}:{c}" for nm, c in zip(names, x) if c != 0))
    # Linear dispersion: [H0, rho_q] = -q rho_q exactly on every window
    print(f"   [H0, rho_q] = -q rho_q for all q:", all(eq(sub(mul(H0, rho[q], sq), mul(rho[q], H0, sq)), scal(F(-q), rho[q])) for q in rho))

print("\nNormal-ordered (Sugawara) form: span(rho_q* rho_q, N^d) only")
for M in range(2, 8):
    sq = tuple([1, -1] * M)
    v = [scal(F(1, 2), add(gen(2 * j), gen(2 * j + 1))) for j in range(M)]
    w = [scal(F(1, 2), sub(gen(2 * j), gen(2 * j + 1))) for j in range(M)]
    n = [mul(v[j], w[j], sq) for j in range(M)]
    H0 = add(*[scal(F(j), n[j]) for j in range(M)])
    Nn = add(*n)
    rho = {q: add(*[mul(v[k], w[k + q], sq) for k in range(M - q)]) for q in range(1, M)}
    cols, names = [], []
    for q in range(1, M):
        cols.append(mul(dag(rho[q], sq), rho[q], sq)); names.append(f"rho{q}* rho{q}")
    Np = sc(1)
    for d in range(M + 1):
        cols.append(Np); names.append(f"N^{d}"); Np = mul(Np, Nn, sq)
    x = solve(cols, H0)
    print(f"M={M}:", "NO" if x is None else "YES " + ", ".join(f"{nm}:{c}" for nm, c in zip(names, x) if c != 0))
    S = add(*[mul(dag(rho[q], sq), rho[q], sq) for q in rho])
    D = sub(sub(H0, S), scal(F(1, 2), sub(mul(Nn, Nn, sq), Nn)))
    print("   defect D = H0 - sum rho* rho - N(N-1)/2: number of blades", len(D))
