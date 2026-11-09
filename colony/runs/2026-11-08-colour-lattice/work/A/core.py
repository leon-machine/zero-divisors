"""Exploration core for the colour rotor lattice (attacker A)."""
import sys, time
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
from itertools import combinations, product
import GA

E9 = GA.sig(9, 0)
IDX = tuple(range(3, 9))
EVEN = [b for k in (0, 2, 4, 6) for b in combinations(IDX, k)]
POS = {b: i for i, b in enumerate(EVEN)}
TAB = []
for a in EVEN:
    row = []
    for b in EVEN:
        s, c = GA.blade_mul(a, b, E9)
        row.append((int(s), POS[c]))
    TAB.append(row)


def m(x, y):
    out = [F(0)] * 32
    for i, a in enumerate(x):
        if a:
            row = TAB[i]
            for j, b in enumerate(y):
                if b:
                    s, k = row[j]
                    out[k] += s * a * b
    return tuple(out)


def arr(mv):
    a = [F(0)] * 32
    for b, c in mv.items():
        a[POS[b]] += c
    return tuple(a)


def mv(x):
    return {EVEN[i]: c for i, c in enumerate(x) if c}


def rev(x):
    return tuple(c if len(EVEN[i]) % 4 == 0 else -c for i, c in enumerate(x))


def add(*xs):
    return tuple(sum(c) for c in zip(*xs))


def sca(c, x):
    return tuple(c * v for v in x)


def bv(i, j):
    return arr(GA.mul(GA.gen(i), GA.gen(j), E9))


ONE = arr(GA.sc(1))
I6 = arr({IDX: F(1)})
P34, P56, P78 = bv(3, 4), bv(5, 6), bv(7, 8)
J = add(P34, P56, P78)
HALF = F(1, 2)
E = ONE
for p in (P34, P56, P78):
    E = m(E, sca(HALF, add(ONE, m(I6, p))))


def vec_action(R):
    """matrix M with M[a][b] = e_a . (R e_b R~)"""
    Rm, Rr = mv(R), mv(rev(R))
    cols = []
    for k in IDX:
        y = GA.mul(GA.mul(Rm, GA.gen(k), E9), Rr, E9)
        assert all(len(b) == 1 for b in y)
        cols.append([y.get((t,), F(0)) for t in IDX])
    return tuple(tuple(cols[b][a] for b in range(6)) for a in range(6))


def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(6)) for j in range(6)) for i in range(6))


def S(a, b, c, d):
    x = GA.sub(GA.gen(a), GA.gen(b))
    y = GA.sub(GA.gen(c), GA.gen(d))
    return arr(GA.scal(HALF, GA.mul(x, y, E9)))


def lift(R):
    RE = m(R, E)
    if RE == E:
        return R
    assert RE == sca(-1, E)
    return sca(-1, R)


GENS = [lift(sca(HALF, m(add(ONE, sca(-1, P34)), add(ONE, P56)))),
        lift(sca(HALF, m(add(ONE, sca(-1, P56)), add(ONE, P78)))),
        lift(m(S(5, 7, 6, 8), S(3, 5, 4, 6))),
        lift(m(S(3, 5, 4, 6), P78))]


def closure(gens):
    elems = {ONE: None}
    frontier = [ONE]
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = m(x, g)
                if y not in elems:
                    elems[y] = None
                    new.append(y)
        frontier = new
    return list(elems)


if __name__ == '__main__':
    t0 = time.time()
    G = closure(GENS)
    print('order', len(G), time.time() - t0)
    print('all RE=E', all(m(R, E) == E for R in G), '-1 in G', sca(-1, ONE) in G)
    Ms = [vec_action(R) for R in G]
    print('vec actions', time.time() - t0)
    tr = [sum(M[i][i] for i in range(6)) for M in Ms]
    for k in range(1, 7):
        print('deg', k, 'inv dim', sum(F(x) ** k for x in tr) / len(G))
    # character relation
    ok = all(4 * R[0] - 1 == F(t, 2) for R, t in zip(G, tr))
    print('Re chi = 4<R>_0 - 1:', ok)
    Jm = vec_action  # placeholder
    # J matrix: J_ab = e_a . (e_b . J)  -> use M for v -> v.J  : e3 -> e4
    Jmat = [[F(0)] * 6 for _ in range(6)]
    for b, k in enumerate(IDX):
        y = GA.mul(GA.gen(k), mv(J), E9)  # e_k J = e_k . J + e_k ^ J
        for a, t in enumerate(IDX):
            Jmat[a][b] = y.get((t,), F(0))
    print('J matrix', Jmat)
    imag = [-HALF * sum(sum(Jmat[i][k] * M[k][i] for k in range(6)) for i in range(6)) for M in Ms]
    c6 = [R[POS[IDX]] for R in G]
    print('Im chi vs 4 c6:', set((im, 4 * c) for im, c in zip(imag, c6)) if len(G) < 0 else
          all(im == 4 * c for im, c in zip(imag, c6)), all(im == -4 * c for im, c in zip(imag, c6)))
    # real span of matrices
    rows = [[M[i][j] for i in range(6) for j in range(6)] for M in Ms]
    print('real span dim', GA.field_rank(rows))
    print('avg rotor == E', tuple(sum(R[i] for R in G) / len(G) for i in range(32)) == E)
    print(time.time() - t0)
