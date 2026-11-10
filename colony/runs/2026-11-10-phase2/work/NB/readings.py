"""NB scratch: invariant forms on the Fock module of Cl(k,k) inside GA.py, and counts under each reading."""
import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
from itertools import combinations
import GA

def setup(k):
    SQ = tuple([1]*k + [-1]*k)
    e = [GA.gen(j) for j in range(k)]; f = [GA.gen(k+j) for j in range(k)]
    v = [GA.scal(F(1,2), GA.add(e[j], f[j])) for j in range(k)]
    w = [GA.scal(F(1,2), GA.sub(e[j], f[j])) for j in range(k)]
    P = GA.sc(1)
    for j in range(k):
        P = GA.mul(P, GA.mul(w[j], v[j], SQ), SQ)
    return SQ, e, f, v, w, P

def states(k, v, P, SQ):
    out = []
    for r in range(k+1):
        for S in combinations(range(k), r):
            x = P
            for j in reversed(S):
                x = GA.mul(v[j], x, SQ)
            out.append((S, x))
    return out

def conj(x):
    return GA.reverse(GA.grade_inv(x))

def gram(k, tau):
    SQ, e, f, v, w, P = setup(k)
    st = states(k, v, P, SQ)
    # reference element Omega = tau(top state) * vacuum  (spans tau(P) Cl P)
    top = st[-1][1]
    Om = GA.mul(tau(top), P, SQ)
    assert Om != {}
    b0 = next(iter(Om)); c0 = Om[b0]
    M = []
    for S, x in st:
        row = []
        for T, y in st:
            z = GA.mul(tau(x), y, SQ)
            if z == {}:
                row.append(F(0))
            else:
                lam = z[b0] / c0
                assert GA.eq(z, GA.scal(lam, Om))
                row.append(lam)
        M.append(row)
    return st, M

for k in range(1, 5):
    for name, tau in (('reverse', GA.reverse), ('conj', conj)):
        st, M = gram(k, tau)
        n = len(M)
        sym = all(M[i][j] == M[j][i] for i in range(n) for j in range(n))
        asym = all(M[i][j] == -M[j][i] for i in range(n) for j in range(n))
        rk = GA.mat_rank(M)
        info = ''
        if sym:
            info = 'signature %s' % (GA.congruence_signature(M),)
        # parity pairing
        ee = any(M[i][j] != 0 for i in range(n) for j in range(n) if len(st[i][0]) % 2 == 0 and len(st[j][0]) % 2 == 0)
        eo = any(M[i][j] != 0 for i in range(n) for j in range(n) if len(st[i][0]) % 2 != len(st[j][0]) % 2)
        print(k, name, 'dim', n, 'rank', rk, 'sym' if sym else ('antisym' if asym else 'neither'), info, 'even-even' if ee else '', 'even-odd' if eo else '')
