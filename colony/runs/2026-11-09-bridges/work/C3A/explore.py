"""Scratch: Sq^2 of the fibre class on M = (S^{K} x S^3)/Z_m by cup-1 in the product cell model. Mod-2 chains are
frozensets (symmetric difference); integer cochains dicts."""
import sys, itertools
from fractions import Fraction as Fr

def bd(k, a, m):                       # mod 2 boundary of g^a e_k in C_m: list of cells
    if k == 0: return []
    if k % 2: return [(k-1, (a+1) % m), (k-1, a)]
    return [(k-1, (a+c) % m) for c in range(m)]

def bdZ(k, a, m):
    if k == 0: return {}
    if k % 2: return {(k-1, (a+1) % m): 1, (k-1, a): -1}
    return {(k-1, (a+c) % m): 1 for c in range(m)}

def closure(k, a, m, top):
    """cells of the closure of g^a e_k"""
    out = {(k, a)}
    if k % 2:
        out |= {(k-1, a), (k-1, (a+1) % m)}
        low = k - 1
    else:
        low = k
    for j in range(low):
        for c in range(m): out.add((j, c))
    return out

def delta(k, a, m):                    # stored diagonal, mod 2: set of (p,a,q,b)
    out = set()
    for p in range(k+1):
        q = k - p
        if p % 2 == 0: terms = [(0, 0)]
        elif q % 2 == 0: terms = [(0, 1)]
        else: terms = [(i, j) for i in range(m) for j in range(i+1, m)]
        for (i, j) in terms: out ^= {(p, (a+i) % m, q, (a+j) % m)}
    return out

def xor_into(S, items):
    for x in items:
        if x in S: S.remove(x)
        else: S.add(x)

def bd_t(T, m):                        # boundary on C_m (x) C_m mod 2
    out = set()
    for (p, a, q, b) in T:
        xor_into(out, [(pp, aa, q, b) for (pp, aa) in bd(p, a, m)])
        xor_into(out, [(p, a, qq, bb) for (qq, bb) in bd(q, b, m)])
    return out

def swap(T): return {(q, b, p, a) for (p, a, q, b) in T}
def shift(T, s, m): return {(p, (a+s) % m, q, (b+s) % m) for (p, a, q, b) in T}

def solve_f2(rows, rhs, order=None):
    """rows: list of sets of unknown indices (equations), rhs: list of bits. returns a solution set or None."""
    piv = {}
    for r, b in zip(rows, rhs):
        r = set(r); b = b
        while r:
            key = (max(r) if order == 'max' else min(r))
            if key in piv:
                pr, pb = piv[key]; r ^= pr; b ^= pb
            else:
                piv[key] = (r, b); break
        else:
            if b: return None
    # back substitution: free vars 0
    sol = {}
    keys = sorted(piv, reverse=(order != 'max'))
    for key in keys:
        r, b = piv[key]
        v = b
        for x in r:
            if x != key and sol.get(x, 0): v ^= 1
        sol[key] = v
    return {k for k, v in sol.items() if v}

def higher_diag(m, top, order=None):
    """Delta_1(e_k) for k <= top: equivariant, carried by closed cells, bd H + H bd = Delta + swap Delta."""
    H = {}
    for k in range(top+1):
        cl = closure(k, 0, m, top)
        unknowns = [(p, a, q, b) for (p, a) in sorted(cl) for (q, b) in sorted(cl) if p + q == k + 1]
        target = delta(k, 0, m) ^ swap(delta(k, 0, m))
        for (kk, aa) in bd(k, 0, m):
            xor_into(target, shift(H[kk], aa, m))
        idx = {}
        eqs = {}
        for i, u in enumerate(unknowns):
            for t in bd_t({u}, m):
                eqs.setdefault(t, set()).add(i)
        keys = sorted(set(eqs) | target)
        rows = [eqs.get(t, set()) for t in keys]
        rhs = [1 if t in target else 0 for t in keys]
        sol = solve_f2(rows, rhs, order)
        assert sol is not None, ('no carried solution', m, k)
        H[k] = {unknowns[i] for i in sol}
        assert bd_t(H[k], m) == target
    return H

def int_kernel(Mx, n):
    """basis of the integer kernel of the matrix (rows = equations) by unimodular column operations."""
    A = [list(r) for r in Mx]; U = [[int(i == j) for j in range(n)] for i in range(n)]
    col = 0
    for r in range(len(A)):
        while True:
            nz = [j for j in range(col, n) if A[r][j]]
            if len(nz) <= 1: break
            j0 = min(nz, key=lambda j: abs(A[r][j]))
            for j in nz:
                if j == j0: continue
                f = A[r][j] // A[r][j0]
                for i in range(len(A)): A[i][j] -= f * A[i][j0]
                for i in range(n): U[i][j] -= f * U[i][j0]
        nz = [j for j in range(col, n) if A[r][j]]
        if nz:
            j = nz[0]
            for i in range(len(A)): A[i][j], A[i][col] = A[i][col], A[i][j]
            for i in range(n): U[i][j], U[i][col] = U[i][col], U[i][j]
            col += 1
    return [tuple(U[i][j] for i in range(n)) for j in range(col, n)]

# ---- product complex P = C_m (x) C_2, cells (k,a,q,b), g: a+1, b+1
def pbd(c, m):
    k, a, q, b = c
    return [(kk, aa, q, b) for (kk, aa) in bd(k, a, m)] + [(k, a, qq, bb) for (qq, bb) in bd(q, b, 2)]
def pbdZ(c, m):
    k, a, q, b = c
    out = {}
    for (kk, aa), v in bdZ(k, a, m).items(): out[(kk, aa, q, b)] = out.get((kk, aa, q, b), 0) + v
    for (qq, bb), v in bdZ(q, b, 2).items(): out[(k, a, qq, bb)] = out.get((k, a, qq, bb), 0) + v * (-1) ** k
    return out
def rep(c, m):                         # orbit representative with a = 0
    k, a, q, b = c
    return (k, 0, q, (b - a) % 2)
def ptbd(T, m):
    out = set()
    for (c1, c2) in T:
        xor_into(out, [(x, c2) for x in pbd(c1, m)])
        xor_into(out, [(c1, x) for x in pbd(c2, m)])
    return out

def run(m, K, variant=0, order=None, verbose=True):
    HC = higher_diag(m, K, order); HD = higher_diag(2, 3, order)
    DC = {k: delta(k, 0, m) for k in range(K+1)}; DD = {q: delta(q, 0, 2) for q in range(4)}
    def prod(TC, TD):                  # (C(x)C) x (D(x)D) -> P(x)P
        return {((p, a, r, c), (q, b, s, d)) for (p, a, q, b) in TC for (r, c, s, d) in TD}
    def HP(k, q):                      # on cell (k,0,q,0)
        out = set()
        if variant == 0:
            xor_into(out, prod(HC[k], swap(DD[q]))); xor_into(out, prod(DC[k], HD[q]))
        else:
            xor_into(out, prod(HC[k], DD[q])); xor_into(out, prod(swap(DC[k]), HD[q]))
        return out
    def DP(k, q): return prod(DC[k], DD[q])
    def pshift(T, s): return {((k, (a+s) % m, q, (b+s) % 2), (k2, (a2+s) % m, q2, (b2+s) % 2)) for ((k, a, q, b), (k2, a2, q2, b2)) in T}
    def pswap(T): return {(y, x) for (x, y) in T}
    def HPcell(c):
        k, a, q, b = c
        assert (b - a) % 2 == 0 or True
        # cell (k,a,q,b) = g^a (k,0,q,b-a); need H on (k,0,q,1) too: use Z2 equivariance of D-part: shift D by 1 only
        T = HP(k, q)
        bb = (b - a) % 2
        if bb: T = {((k1, a1, q1, (b1+1) % 2), (k2, a2, q2, (b2+1) % 2)) for ((k1, a1, q1, b1), (k2, a2, q2, b2)) in T}
        return pshift(T, a)
    def DPcell(c):
        k, a, q, b = c
        T = DP(k, q); bb = (b - a) % 2
        if bb: T = {((k1, a1, q1, (b1+1) % 2), (k2, a2, q2, (b2+1) % 2)) for ((k1, a1, q1, b1), (k2, a2, q2, b2)) in T}
        return pshift(T, a)
    # verify homotopy identity on all orbit reps of dim <= 5
    for k in range(K+1):
        for q in range(4):
            if k + q > 5: continue
            for b in (0, 1):
                c = (k, 0, q, b)
                lhs = ptbd(HPcell(c), m)
                for x in pbd(c, m): xor_into(lhs, HPcell(x))
                rhs = DPcell(c) ^ pswap(DPcell(c))
                assert lhs == rhs, ('homotopy fails', c)
                # chain map
                l2 = ptbd(DPcell(c), m); r2 = set()
                for x in pbd(c, m): xor_into(r2, DPcell(x))
                assert l2 == r2
    # integral invariant cochains of degree n: values on reps (k,0,q,b)
    def reps(n): return [(k, 0, n-k, b) for k in range(K+1) if 0 <= n-k <= 3 for b in (0, 1)]
    def cob_matrix(n):                 # rows: reps(n+1), cols: reps(n)
        R = reps(n); S = reps(n+1); col = {r: i for i, r in enumerate(R)}
        Mx = [[0]*len(R) for _ in S]
        for i, c in enumerate(S):
            for x, v in pbdZ(c, m).items(): Mx[i][col[rep(x, m)]] += v
        return Mx, R, S
    M3, R3, S4 = cob_matrix(3)
    M2, R2, _ = cob_matrix(2)
    basis = int_kernel(M3, len(R3))
    cocycles = [tuple(sum(c*b[i] for c, b in zip(cs, basis)) for i in range(len(R3)))
                for cs in itertools.product(range(-2, 3), repeat=len(basis))]
    assert all(sum(r[i]*v[i] for i in range(len(v))) == 0 for r in M3 for v in cocycles)
    if verbose: print('kernel basis', basis)
    fib = lambda v: v[R3.index((0, 0, 3, 0))] + v[R3.index((0, 0, 3, 1))]
    fibs = sorted({abs(fib(v)) for v in cocycles})
    if verbose: print('m', m, 'K', K, 'integral 3-cocycles in box', len(cocycles), 'fibre values', fibs)
    # mod 2 machinery in degree 5
    R5 = reps(5); R4 = reps(4)
    def sq(theta):                     # theta: dict rep->int ; returns set of reps(5) where cup-1 square is odd
        a = {r for r, v in theta.items() if v % 2}
        out = set()
        for c in R5:
            n = sum(1 for (x, y) in HPcell(c) if rep(x, m) in a and rep(y, m) in a)
            if n % 2: out.add(c)
        return out
    cob4 = []                          # coboundaries of the basis 4-cochains, as sets of reps(5)
    for r in R4:
        cob4.append({c for c in R5 if sum(1 for x in pbd(c, m) if rep(x, m) == r) % 2})
    def in_span(target, gens):
        gens = [set(g) for g in gens]; t = set(target)
        piv = {}
        for g in gens:
            g = set(g)
            while g:
                key = min(g)
                if key in piv: g ^= piv[key]
                else: piv[key] = g; break
        while t:
            key = min(t)
            if key in piv: t ^= piv[key]
            else: return False
        return True
    pstar = {c for c in R5 if c[2] == 0}            # p^* eps_5
    res = {}
    for v in cocycles:
        if abs(fib(v)) != (fibs[1] if len(fibs) > 1 else 0) or fib(v) <= 0: continue
        th = dict(zip(R3, v)); s2 = sq(th)
        key = (in_span(s2, cob4), in_span(s2 ^ pstar, cob4))
        res[key] = res.get(key, 0) + 1
        ex = (v, sorted(s2))
    if verbose:
        print('  (sq ~ 0, sq ~ p^*eps5) counts over theta with minimal fibre value:', res)
        print('  p^*eps5 a coboundary mod 2:', in_span(pstar, cob4), ' example theta', dict(zip(R3, ex[0])) if res else None, 'sq support', ex[1] if res else None)
    return res

if __name__ == '__main__':
    for (m, K) in ((4, 5), (8, 5), (2, 5), (4, 3), (12, 5), (16, 5), (6, 5), (4, 7)):
        for variant in (0, 1)[:1 if m > 8 else 2]:
            for order in (None, 'max')[:1 if m > 8 else 2]:
                run(m, K, variant, order)
