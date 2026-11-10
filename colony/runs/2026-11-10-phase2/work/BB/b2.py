from bbl import *
from itertools import combinations
def blades(n): return [ONE] + [{tuple(c): F(1)} for r in range(1, n+1) for c in combinations(range(n), r)]
def study(sq, a, b, Gam, name, full=True):
    n = len(sq); print('==', name)
    assert all(is_obs(o, sq) for o in a + b)
    assert all(GA.commutes(x, y, sq) for x in a for y in b)
    c = chsh(sq, *a, *b); K = GA.neg(prod(sq, a[0], a[1], b[0], b[1]))
    m = GA.add(ONE, c); lam = lambda x: s0(prod(sq, m, x))
    print(' parities A,B:', ['o' if odd(x) else 'e' for x in a + b], 'C even:', not odd(c), 'lam(C)=', lam(c), 'lam(1)=', lam(ONE))
    # tables
    okt = True
    for i in range(2):
        for j in range(2):
            ps = [lam(prod(sq, lin((F(1,2), ONE), (F(s,2), a[i])), lin((F(1,2), ONE), (F(t,2), b[j])))) for s in (1,-1) for t in (1,-1)]
            okt &= all(x >= 0 for x in ps) and sum(ps) == 1
            if i == 0 and j == 0: print('  table(1,1):', ps)
    print(' tables nonneg, normalised:', okt, 'marginals lam(Ai),lam(Bj):', [lam(x) for x in a + b])
    x = GA.sub(c, ONE); print(' lam((C-1)(C-1)^dag) =', lam(prod(sq, x, dagger(x, sq))))
    # parity average
    cev = even(c); mE = GA.add(ONE, cev)
    y = prod(sq, GA.sub(c, ONE)) if False else None
    print(' C_even terms', len(cev), ' <(1+C_ev)C_ev> =', s0(prod(sq, mE, cev)))
    if odd(c):
        u = [ {k: v} for k, v in cev.items()]
        yy = prod(sq, GA.sub(ONE, u[0]), GA.sub(ONE, u[1]))  # try sign combos
        best = min(s0(prod(sq, mE, z, dagger(z, sq))) for z in [prod(sq, GA.add(ONE, GA.scal(F(s), u[0])), GA.add(ONE, GA.scal(F(t), u[1]))) for s in (1,-1) for t in (1,-1)])
        print(' min over 4 sign elements of lamE(z z^dag):', best)
    # record maps
    if full:
        B = blades(n)
        for i in range(2):
            for j in range(2):
                Rs = [prod(sq, lin((F(1,2), ONE), (F(s,2), a[i])), lin((F(1,2), ONE), (F(t,2), b[j]))) for s in (1,-1) for t in (1,-1)]
                sg = lam(prod(sq, a[i], b[j])); tgt = GA.add(ONE, GA.scal(sg, prod(sq, a[i], b[j])))
                ok = all(sum(lam(prod(sq, R, x, R)) for R in Rs) == s0(prod(sq, tgt, x)) for x in B)
                print('  record of context', i+1, j+1, ': lam o E_R = <(1 + %s A B) x>_0 on all blades:' % sg, ok)
        ok = all(F(1,2) * (lam(x) + lam(prod(sq, K, x, K))) == lam(x) for x in B)
        print('  coarse record of K leaves lam unchanged on all blades:', ok, ' K even:', not odd(K))
        ok = all(lam(par(x)) == lam(x) for x in B); print('  lam even (lam o alpha = lam):', ok)
sq, e, f, p = modes(2)
study(sq, (e[0], p[0]), (prod(sq, e[1], p[0]), p[1]), None, 'Cl(2,2) one mode per party, twisted (phase 1 model)')
sq, e, f, p = modes(4)
study(sq, (p[0], prod(sq, e[0], f[1])), (p[2], prod(sq, e[2], f[3])), None, 'Cl(4,4) two modes per party, even observables')
G = prod(sq, p[0], p[1])
study(sq, (e[0], e[1]), (prod(sq, e[2], G), prod(sq, e[3], G)), None, 'Cl(4,4) two modes per party, odd homogeneous observables')
