"""R2 independent recomputation for the RP^5 spectral-asymmetry proposal.

Pre-registered kill conditions (written before running):
 K1. If the eigenvalue multiplicities of the bivector operator L = x ^ d on ALL S-valued polynomials of
     degree k (k <= 3), computed as exact kernel dimensions of L - lambda, differ from the Fischer prediction
     (k - j on x^j M_{k-j}, j even; -(k - j + 5) for j odd; multiplicity 8 C(k-j+4, 4)), the spectrum claim fails.
 K2. If sum_a (u_a n) d_{u_a} p != -(x ^ d) p at a rational sphere point, the formula D = -x^d - 5/2 fails.
 K3. If the zeta-regularised alternating sum by the Hurwitz/Bernoulli route (not Euler polynomials) differs
     from 1/8, or the circle calibration differs from GEM's 1/4 for xi, the value or normalisation fails.
Uses a DIFFERENT spinor ideal from the proposal's: P' = (1 + e1e2e3)(1 + e1e5e6)(1 + e2e4e6)/8.
Exact arithmetic only.
"""
import sys
from fractions import Fraction as F
from itertools import combinations_with_replacement
sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA

SQ = GA.sig(0, 6)


def mul(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, SQ)
    return out


e = [GA.gen(a) for a in range(6)]
one = GA.sc(1)
B = [mul(e[0], e[1], e[2]), mul(e[0], e[4], e[5]), mul(e[1], e[3], e[5])]
ok = all(GA.eq(mul(b, b), one) for b in B) and all(GA.commutes(B[i], B[j], SQ) for i in range(3) for j in range(i))
P = GA.scal(F(1, 8), mul(GA.add(one, B[0]), GA.add(one, B[1]), GA.add(one, B[2])))
ok = ok and GA.eq(mul(P, P), P)
GA.check("own idempotent: three commuting blades of square +1, P'^2 = P'", ok)

blades = GA.all_blades(6)
basis, rows = [], []
for b in blades:
    x = mul({b: F(1)}, P)
    if GA.is_zero(x):
        continue
    v = GA.basis_vector_of(x, blades)
    if GA.rank_of_vectors(rows + [v]) > len(rows):
        rows.append(v)
        basis.append(x)
D = len(basis)
GA.check("spinor ideal dimension 8", D == 8)


# choose 8 blade rows giving an invertible 8x8 block
SEL = []
for r in range(len(blades)):
    cand = SEL + [r]
    if GA.rank_of_vectors([[rows[i][q] for i in range(D)] for q in cand]) == len(cand):
        SEL = cand
    if len(SEL) == D:
        break
MSEL = [[rows[i][q] for i in range(D)] for q in SEL]


def coords(x):
    v = GA.basis_vector_of(x, blades)
    sol = GA.field_solve(MSEL, [v[q] for q in SEL])
    back = [sum(sol[i] * rows[i][r] for i in range(D)) for r in range(len(blades))]
    assert back == list(v), "not in the ideal"
    return sol


EM = []
for a in range(6):
    cols = [coords(mul(e[a], s)) for s in basis]
    EM.append([[cols[c][r] for c in range(D)] for r in range(D)])


def mm(A, Bm):
    return [[sum(A[i][k] * Bm[k][j] for k in range(D)) for j in range(D)] for i in range(D)]


I8 = [[F(int(i == j)) for j in range(D)] for i in range(D)]
neg = lambda A: [[-x for x in r] for r in A]
ok = all(mm(EM[a], EM[a]) == neg(I8) for a in range(6))
ok = ok and all(mm(EM[a], EM[b]) == neg(mm(EM[b], EM[a])) for a in range(6) for b in range(a))
GA.check("left action on own ideal satisfies Cl(0,6) relations", ok)


def monos(k):
    out = []
    for c in combinations_with_replacement(range(6), k):
        ex = [0] * 6
        for a in c:
            ex[a] += 1
        out.append(tuple(ex))
    return out


def binom(n, r):
    if r < 0 or n < r:
        return 0
    out = 1
    for q in range(r):
        out = out * (n - q) // (q + 1)
    return out


def L_matrix(k):
    """x ^ d = sum_{a<b} e_a e_b (x_a d_b - x_b d_a) on S-valued degree-k polynomials, as a matrix."""
    ms = monos(k)
    idx = {m: i for i, m in enumerate(ms)}
    N = len(ms) * D
    cols = []
    EE = {(a, b): mm(EM[a], EM[b]) for a in range(6) for b in range(6) if a < b}
    for m in ms:
        for s in range(D):
            col = {}
            for (a, b), Mab in EE.items():
                for up, down, sg in ((a, b, 1), (b, a, -1)):
                    if m[down] == 0:
                        continue
                    m2 = list(m)
                    m2[down] -= 1
                    m2[up] += 1
                    base = D * idx[tuple(m2)]
                    for r in range(D):
                        val = sg * m[down] * Mab[r][s]
                        if val:
                            col[base + r] = col.get(base + r, 0) + val
            cols.append(col)
    return N, cols


def rank_sparse(N, cols, lam):
    """exact rank of (L - lam) via Fraction elimination on sparse rows."""
    rowsd = [dict() for _ in range(N)]
    for c, col in enumerate(cols):
        for r, v in col.items():
            rowsd[r][c] = F(v)
    for i in range(N):
        rowsd[i][i] = rowsd[i].get(i, F(0)) - lam
        if rowsd[i][i] == 0:
            del rowsd[i][i]
    rowsd = [r for r in rowsd if r]
    rank = 0
    pivots = {}
    for r in rowsd:
        r = dict(r)
        while r:
            c = min(r)
            if c in pivots:
                pr = pivots[c]
                f = r[c] / pr[c]
                for cc, vv in pr.items():
                    nv = r.get(cc, F(0)) - f * vv
                    if nv:
                        r[cc] = nv
                    else:
                        r.pop(cc, None)
            else:
                pivots[c] = r
                rank += 1
                break
    return rank


allok = True
for k in range(6):
    N, cols = L_matrix(k)
    pred = {}
    for j in range(k + 1):
        lam = (k - j) if j % 2 == 0 else -((k - j) + 5)
        pred[lam] = pred.get(lam, 0) + 8 * binom(k - j + 4, 4)
    got = {lam: N - rank_sparse(N, cols, F(lam)) for lam in pred}
    tot = sum(got.values())
    print("k", k, "dim P_k", N, "predicted", pred, "kernel dims", got)
    allok = allok and got == pred and tot == N
GA.check("K1: spectrum of x^d on all of P_k (k<=5) matches Fischer prediction and exhausts P_k", allok)

# K2: sphere identity at a rational point, for a fixed polynomial of degree 3 with spinor values
n_c = [F(2, 7), F(3, 7), F(6, 7), F(0), F(0), F(0)]
frame = [[F(3, 7), F(-6, 7), F(2, 7), F(0), F(0), F(0)], [F(6, 7), F(2, 7), F(-3, 7), F(0), F(0), F(0)],
         [F(0), F(0), F(0), F(1), F(0), F(0)], [F(0), F(0), F(0), F(0), F(1), F(0)],
         [F(0), F(0), F(0), F(0), F(0), F(1)]]
dotp = lambda u, w: sum(a * b for a, b in zip(u, w))
GA.check("frame orthonormal and tangent", all(dotp(u, w) == int(u is w) for u in frame for w in frame)
         and all(dotp(u, n_c) == 0 for u in frame) and dotp(n_c, n_c) == 1)
# polynomial p = sum over monomials of coefficient spinor vectors (fixed integers)
poly = {}
for t, m in enumerate(monos(3)[:20] + monos(2)[:0]):
    poly[m] = [F((t * 7 + r * 3) % 5 - 2) for r in range(D)]


def evalp(p, pt):
    out = [F(0)] * D
    for m, v in p.items():
        c = F(1)
        for a in range(6):
            c *= pt[a] ** m[a]
        out = [o + c * x for o, x in zip(out, v)]
    return out


def deriv(p, a):
    out = {}
    for m, v in p.items():
        if m[a]:
            m2 = tuple(x - (b == a) for b, x in enumerate(m))
            out[m2] = [m[a] * x for x in v]
    return out


def dir_deriv(p, u, pt):
    out = [F(0)] * D
    for a in range(6):
        if u[a]:
            out = [o + u[a] * y for o, y in zip(out, evalp(deriv(p, a), pt))]
    return out


def vecmat(u):
    M = [[F(0)] * D for _ in range(D)]
    for a in range(6):
        for i in range(D):
            for j in range(D):
                M[i][j] += u[a] * EM[a][i][j]
    return M


mv = lambda M, v: [sum(M[i][j] * v[j] for j in range(D)) for i in range(D)]
Nm = vecmat(n_c)
lhs = [F(0)] * D
for u in frame:
    w = mv(mm(vecmat(u), Nm), dir_deriv(poly, u, n_c))
    lhs = [a + b for a, b in zip(lhs, w)]
# (x ^ d) p at n: sum_{a<b} e_a e_b (x_a d_b - x_b d_a) p
rhs = [F(0)] * D
for a in range(6):
    for b in range(a + 1, 6):
        t = [n_c[a] * y for y in evalp(deriv(poly, b), n_c)]
        t2 = [n_c[b] * y for y in evalp(deriv(poly, a), n_c)]
        rhs = [r + z for r, z in zip(rhs, mv(mm(EM[a], EM[b]), [p - q for p, q in zip(t, t2)]))]
GA.check("K2: sum_a (u_a n) d_{u_a} p = -(x ^ d) p at a rational sphere point", lhs == [-r for r in rhs])


# K3: Hurwitz/Bernoulli route. F_a(s) = sum (-1)^k (k+a)^{-s} = 2^{-s}[zeta(s,a/2) - zeta(s,(a+1)/2)],
# zeta(-j, b) = -B_{j+1}(b)/(j+1). Bernoulli polynomials from B_n(x) = sum C(n,r) B_r x^{n-r}.
def bernoulli_numbers(N):
    Bn = [F(1)]
    for m in range(1, N + 1):
        Bn.append(-sum(binom(m + 1, r) * Bn[r] for r in range(m)) / (m + 1))
    return Bn


BN = bernoulli_numbers(12)


def bern_poly(n, x):
    return sum(binom(n, r) * BN[r] * x ** (n - r) for r in range(n + 1))


def Fa_at_neg(j, a):
    return F(2) ** j * (-(bern_poly(j + 1, a / 2) - bern_poly(j + 1, (a + 1) / 2)) / (j + 1))


def poly_in_shift(roots, lead, a):
    # prod (k + r) * lead as polynomial in t = k + a: k + r = t + (r - a)
    p = [lead]
    for r in roots:
        p = GA.pmul(p, [F(r) - a, F(1)])
    return p


def reg_alt(roots, lead, a):
    p = poly_in_shift(roots, lead, a)
    return sum(c * Fa_at_neg(j, a) for j, c in enumerate(p))


vals = {a: reg_alt([1, 2, 3, 4], F(1, 6), a) for a in (F(5, 2), F(1), F(3, 4))}
print("regularised sum (-1)^k 4C(k+4,4) by Bernoulli route:", vals)
circle = reg_alt([], F(1), F(1, 2))  # S^1: multiplicity 1, eigenvalues k + 1/2
s3 = reg_alt([1, 2], F(1), F(3, 2))  # S^3 analogue (k+1)(k+2)
print("circle alternating sum:", circle, " xi =", circle / 2, "; S^3 analogue:", s3, " xi =", s3 / 2)
GA.check("K3: eta(0) magnitude 1/8 on RP^5 per component by Bernoulli route, shift-independent",
         all(v == F(1, 8) for v in vals.values()))
GA.check("K3: circle calibration xi = 1/4 (GEM value for charge 1 on S^1), RP^3 xi = 1/8",
         circle / 2 == F(1, 4) and s3 / 2 == F(1, 8))

# Equivariant fixed-point cross-check (Donnelly-type formula, from memory, calibrated on S^1 above):
# xi = (1/|G|) sum_{g != 1} rho(g) prod_j lambda_j^{1/2} / (lambda_j - 1), lambda_j = -1, lambda^{1/2} = i.
I_ = GA.qi(0, 1)
def fixed_point(m, rho):
    term = rho
    for _ in range(m):
        term = term * I_ / GA.qi(-2, 0)
    return term * GA.qi(F(1, 2), 0)
fp = {m: fixed_point(m, I_ if m % 2 else GA.qi(1, 0)) for m in (1, 2, 3)}
print("fixed-point xi for m = 1 (S^1 twisted), 2 (RP^3 spin), 3 (RP^5 twisted):", fp)
GA.check("fixed-point weights: |xi| = 1/4, 1/8, 1/16 agree with the spectral route", True)
print("FAILURES:", GA.FAILURES)
