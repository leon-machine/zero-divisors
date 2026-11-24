"""Scratch: the steps of the induction on the support, P2, and the CHSH element."""
import sys
sys.path.insert(0, '/home/claude/leon-machine/zero-divisors/lib')
from fractions import Fraction as F
from itertools import combinations, product
import GA

# ---- quaternions as rotors of Cl(3,0)
SQ3 = (1, 1, 1)
B = [GA.mul(GA.gen(2), GA.gen(1), SQ3), GA.mul(GA.gen(0), GA.gen(2), SQ3), GA.mul(GA.gen(1), GA.gen(0), SQ3)]
def rotor(r):
    return GA.add(GA.sc(F(r[0])), *[GA.scal(F(r[k + 1]), B[k]) for k in range(3)])
def coords(x):
    return (x.get((), F(0)), x.get((1, 2), F(0)) * -1, x.get((0, 2), F(0)), x.get((0, 1), F(0)) * -1)
# check coords convention
for k in range(4):
    r = [0, 0, 0, 0]; r[k] = 1
    assert coords(rotor(r)) == tuple(F(c) for c in r), (k, rotor(r))
def qmul(r, s):
    return coords(GA.mul(rotor(r), rotor(s), SQ3))
def qinv(r):
    n = sum(c * c for c in r)
    return (r[0] / n, -r[1] / n, -r[2] / n, -r[3] / n)
def norm(r):
    return sum(F(c) * F(c) for c in r)

def primes_of(n):
    out = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            out.append(d); n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out
MEMO = {}
def four_prime(p):
    """rational quaternion of norm p, by the induction of the proof"""
    if p in MEMO:
        return MEMO[p]
    if p == 2:
        MEMO[p] = (F(1), F(1), F(0), F(0)); return MEMO[p]
    h = (p - 1) // 2
    sq = {(a * a) % p: a for a in range(h + 1)}
    for b in range(h + 1):
        t = (-1 - b * b) % p
        if t in sq:
            a = sq[t]; break
    m = (a * a + b * b + 1) // p
    assert 1 <= m < p and m * p == a * a + b * b + 1
    q = (F(a), F(b), F(1), F(0))
    q = qmul(q, qinv(four_int(m)))
    assert norm(q) == p
    MEMO[p] = q
    return q
def four_int(n):
    q = (F(1), F(0), F(0), F(0))
    for p in primes_of(n):
        q = qmul(q, four_prime(p))
    assert norm(q) == n
    return q
def four_rat(x):
    x = F(x)
    q = four_int(x.numerator * x.denominator)
    return tuple(c / x.denominator for c in q)
for n in range(1, 400):
    four_int(n)
print('four squares over Q for 1..399 ok; e.g. 7 ->', four_int(7), ' 23 ->', four_int(23))

# ---- reflection step
def dotp(a, b):
    return sum(x * y for x, y in zip(a, b))
def reflect(m, x):
    c = 2 * dotp(m, x) / dotp(m, m)
    return tuple(xi - c * mi for xi, mi in zip(x, m))
def embed(r):
    """r of full support in Q^n, n >= 5: W = R(span e_0..e_3) contains r"""
    n = len(r)
    q = four_rat(dotp(r, r))
    s = tuple(q) + (F(0),) * (n - 4)
    m = tuple(a - b for a, b in zip(r, s))
    basis = []
    for i in range(4):
        e = tuple(F(1) if j == i else F(0) for j in range(n))
        basis.append(reflect(m, e) if any(m) else e)
    return s, basis
def rank(rows):
    return GA.mat_rank([list(x) for x in rows])
def solve(rows, target):
    # solve sum c_k rows[k] = target over Q ; return c or None
    A = [list(col) for col in zip(*rows)]
    n = len(rows)
    Mx = [A[i] + [target[i]] for i in range(len(A))]
    piv = []
    r0 = 0
    for c in range(n):
        p = next((i for i in range(r0, len(Mx)) if Mx[i][c] != 0), None)
        if p is None: continue
        Mx[r0], Mx[p] = Mx[p], Mx[r0]
        pv = Mx[r0][c]
        Mx[r0] = [x / pv for x in Mx[r0]]
        for i in range(len(Mx)):
            if i != r0 and Mx[i][c] != 0:
                f = Mx[i][c]
                Mx[i] = [x - f * y for x, y in zip(Mx[i], Mx[r0])]
        piv.append(c); r0 += 1
    if any(all(x == 0 for x in row[:-1]) and row[-1] != 0 for row in Mx):
        return None
    sol = [F(0)] * n
    for i, c in enumerate(piv):
        sol[c] = Mx[i][-1]
    return sol
def quad_eval(c):
    return [c[a] * c[b] for a in range(4) for b in range(a, 4)]
samples = [(1, 1, 1, 1, 1), (1, 2, 3, 4, 5), (1, 1, 1, 1, 1, 1, 1, 1), (3, -1, 2, 5, 1, 1, -2, 7), (1, 2, 3, 4, 5, 6), (2, 1, 1, 1, 1, 1, 3)]
for r in samples:
    r = tuple(F(c) for c in r)
    n = len(r)
    s, W = embed(r)
    # W orthonormal (isometric image of the coordinate four-space)
    assert all(dotp(W[i], W[j]) == (1 if i == j else 0) for i in range(4) for j in range(4))
    cr = [dotp(r, W[i]) for i in range(4)]
    assert tuple(sum(cr[i] * W[i][k] for i in range(4)) for k in range(n)) == r
    assert tuple(cr) == tuple(s[:4])
    # hyperplanes x_k = 0 inside W : linear forms l_k(c) = sum_i c_i W[i][k]
    forms = [tuple(W[i][k] for i in range(4)) for k in range(n)]
    assert all(any(f) for f in forms)
    classes = []
    for f in forms:
        if not any(rank([f, g]) == 1 for g in classes):
            classes.append(f)
    # vectors of W in the hyperplanes: kernel bases
    evs = []
    for f in classes:
        ker = GA.field_kernel([list(f)]) if hasattr(GA, 'field_kernel') else None
        ker = [tuple(F(x) for x in kv) for kv in ker]
        assert len(ker) == 3 and all(dotp(f, kv) == 0 for kv in ker)
        vecs = list(ker) + [tuple(a + b for a, b in zip(ker[i], ker[j])) for i, j in combinations(range(3), 2)]
        evs += [quad_eval(c) for c in vecs]
    rk = rank(evs)
    sol = solve(evs, quad_eval(cr))
    print('r =', [int(c) for c in r], ' s =', [str(c) for c in s[:4]], ' distinct hyperplanes', len(classes), ' rank of evaluations', rk, ' r in span:', sol is not None)

# ---- P2: the pair e_1, (0,1,1,1,2,0,0,0)
res = sorted({(a * a + b * b + c * c) % 8 for a in range(8) for b in range(8) for c in range(8)})
print('sums of three squares mod 8:', res)
print('a^2+b^2+c^2 = 0 mod 4 forces all even:', all((a % 2 == 0 and b % 2 == 0 and c % 2 == 0) for a in range(4) for b in range(4) for c in range(4) if (a * a + b * b + c * c) % 4 == 0))
bound = 40
hits = [(m, a, b, c) for m in range(1, bound) for a in range(0, 3 * bound) for b in range(a, 3 * bound) for c in range(b, 3 * bound) if a * a + b * b + c * c == 7 * m * m]
print('7 m^2 = a^2+b^2+c^2 with m <', bound, ':', hits[:3])
# Lagrange identity: Q(x)Q(y) - (x.y)^2 = norm of the bivector part of y x~
import itertools
ok = True
for x, y in [((1, 2, 3, 4), (0, 1, -1, 5)), ((2, 0, 1, 1), (3, 1, 4, 1)), ((1, 0, 0, 0), (0, 1, 1, 1))]:
    xr = (x[0], -x[1], -x[2], -x[3])
    z = qmul(y, xr)
    ok &= (norm(x) * norm(y) - dotp(x, y) ** 2 == z[1] ** 2 + z[2] ** 2 + z[3] ** 2) and z[0] == dotp(x, y)
print('Lagrange identity (det of a pair in Q^4 is a sum of three squares):', ok)
