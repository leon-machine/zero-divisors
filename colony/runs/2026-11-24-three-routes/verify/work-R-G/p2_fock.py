# Independent Fock computation for proposal 2 (ii),(iii). Exact integers.
import itertools, sys
from fractions import Fraction
from math import comb

def run(q, N, channels):
    levels = list(range(-N, N))
    modes = [(k, c) for c in channels for k in levels]
    idx = {m: i for i, m in enumerate(modes)}
    sea = frozenset(idx[(k, c)] for c in channels for k in levels if k < 0)
    def ann(i, st):
        out = {}
        for pat, a in st.items():
            if i in pat:
                sgn = (-1) ** sum(1 for j in pat if j < i)
                p2 = pat - {i}
                out[p2] = out.get(p2, 0) + sgn * a
        return out
    def cre(i, st):
        out = {}
        for pat, a in st.items():
            if i not in pat:
                sgn = (-1) ** sum(1 for j in pat if j < i)
                p2 = pat | {i}
                out[p2] = out.get(p2, 0) + sgn * a
        return out
    def add(a, b, c=1):
        r = dict(a)
        for k, v in b.items():
            r[k] = r.get(k, 0) + c * v
        return {k: v for k, v in r.items() if v != 0}
    # operator = list of (coef, [ops]) with ops applied right to left: ('c',i)/('a',i)
    def apply(op, st):
        res = {}
        for coef, word in op:
            s = st
            for kind, i in reversed(word):
                s = (cre if kind == 'c' else ann)(i, s)
                if not s: break
            if s: res = add(res, s, coef)
        return res
    def dag(op):
        return [(c, [('a' if k == 'c' else 'c', i) for k, i in reversed(w)]) for c, w in op]
    def mul(A, B):
        return [(a * b, wa + wb) for a, wa in A for b, wb in B]
    def rho(a, cp, cm):  # sum a*_{k,cp} a_{k+a,cm}
        return [(1, [('c', idx[(k, cp)]), ('a', idx[(k + a, cm)])]) for k in levels if k + a in levels]
    def ip(s, t):
        return sum(v * t.get(k, 0) for k, v in s.items())
    def comm_exp(op, st):  # <st,[op,op*]st>
        a = apply(dag(op), st); b = apply(op, st)
        return ip(a, a) - ip(b, b)
    return locals()

# two flavours: channels (+,1),(-,1),(+,2),(-,2)
for q in [2, 3, 4]:
    N = q + 2
    E = run(q, N, ['p1', 'm1', 'p2', 'm2'])
    X = []
    for a in range(1, q):
        X += E['mul'](E['rho'](a, 'p1', 'm1'), E['rho'](q - a, 'p2', 'm2'))
    Om = {E['sea']: 1}
    psi1 = E['apply'](E['dag'](E['rho'](2, 'p2', 'm2')), Om)
    psi2 = E['apply'](E['dag'](E['rho'](1, 'm2', 'p2')), Om)
    vals = [E['comm_exp'](X, s) for s in (Om, psi1, psi2)]
    norms = [E['ip'](s, s) for s in (Om, psi1, psi2)]
    rid = []
    for c in ['p1', 'm1', 'p2', 'm2']:
        rid += E['rho'](q, c, c)
    rv = [E['comm_exp'](rid, s) for s in (Om, psi1, psi2)]
    XdXd = E['apply'](E['dag'](X), E['apply'](E['dag'](X), Om))
    print('two-flavour q', q, 'raw <[X,X*]>', vals, 'norms', norms, 'normalised', [Fraction(v, n) for v, n in zip(vals, norms)],
          'XOm', E['apply'](X, Om) == {}, 'binom', comb(q + 1, 3), 'rho_q(id) comm', [Fraction(v, n) for v, n in zip(rv, norms)],
          '(X*)^2 Om zero', XdXd == {})
# one species
for q in [4, 5, 6, 7]:
    N = max(2, q - 2) + 1
    E = run(q, N, ['p', 'm'])
    lv = E['levels']; idx = E['idx']
    V = []
    for k1, k2 in itertools.combinations(lv, 2):
        for l1, l2 in itertools.combinations(lv, 2):
            if l1 + l2 - k1 - k2 == q:
                V.append(((k2 - k1) * (l2 - l1), [('c', idx[(k1, 'p')]), ('c', idx[(k2, 'p')]), ('a', idx[(l2, 'm')]), ('a', idx[(l1, 'm')])]))
    Om = {E['sea']: 1}
    print('one-species q', q, E['comm_exp'](V, Om), 'binom', comb(q + 3, 7), 'VOm zero', E['apply'](V, Om) == {})
