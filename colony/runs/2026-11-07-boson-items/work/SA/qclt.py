"""SA work: central limit of fluctuation states on N blocks of a tower level, exact cumulants."""
import sys, itertools
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
sys.path.insert(0, '/home/claude/phys-graph/colony/runs/2026-11-07-boson-items/work/SA')
from galib import level, dag, comm, acomm, chk
import galib

OK = True


def partitions(lst):
    if not lst:
        yield []
        return
    first, rest = lst[0], lst[1:]
    for p in partitions(rest):
        yield [[first]] + p
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]


def fact(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def setup(NB):
    N = 2 * NB
    s, mul, J, v, w, n, Gam, I = level(N)
    m = N

    def omega(rho, X):
        """span{1,J}-valued state: 2^m (<rho X>_0 - J <J rho X>_0), returned as (re, jm)."""
        y = mul(rho, X)
        return (2 ** m * y.get((), F(0)), -(2 ** m) * mul(J, y).get((), F(0)))
    return s, mul, J, v, w, n, omega


def copy(x, blk):
    return {tuple(i if i < 2 else i + 4 * blk for i in bl): c for bl, c in x.items()}


def cmul(a, b):
    # (a0 + a1 J)(b0 + b1 J)
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cumulant(mom, k):
    """classical cumulant from ordered moments mom(tuple of indices)."""
    tot = (F(0), F(0))
    for p in partitions(list(range(k))):
        term = (F((-1) ** (len(p) - 1) * fact(len(p) - 1)), F(0))
        for B in p:
            term = cmul(term, mom(tuple(sorted(B))))
        tot = (tot[0] + term[0], tot[1] + term[1])
    return tot


results = {}
MAIN = __name__ == "__main__"
for NB in ((1, 2, 3) if MAIN else ()):
    s, mul, J, v, w, n, omega = setup(NB)
    # block state: occupations (p1, p2) on every block
    p1, p2 = F(3, 4), F(1, 5)
    rho = GA.sc(1)
    for blk in range(NB):
        for j, p in ((0, p1), (1, p2)):
            nk = n[2 * blk + j]
            rho = mul(rho, GA.add(GA.scal(p, nk), GA.scal(1 - p, GA.sub(GA.sc(1), nk))))
    b = mul(v[0], w[1])
    c = mul(w[0], w[1])
    phi = GA.add(b, dag(b, s))
    pi = mul(J, GA.sub(dag(b, s), b))
    chi = GA.add(c, dag(c, s))
    xs = {'phi': phi, 'pi': pi, 'n0': n[0], 'chi': chi, 'mix': GA.add(phi, GA.scal(2, mul(n[0], n[1])))}
    # centre with the single-block state value (real for these self-adjoint elements)
    _, _, _, _, _, _, om1 = setup(1)
    rho1 = mul(GA.add(GA.scal(p1, n[0]), GA.scal(1 - p1, GA.sub(GA.sc(1), n[0]))),
               GA.add(GA.scal(p2, n[1]), GA.scal(1 - p2, GA.sub(GA.sc(1), n[1]))))
    S = {}
    for name, x in xs.items():
        mval = om1(rho1, x)
        assert mval[1] == 0
        y = GA.sub(x, GA.sc(mval[0]))
        S[name] = GA.add(*[copy(y, blk) for blk in range(NB)])
    for seq in (('phi', 'pi'), ('phi', 'pi', 'phi'), ('n0', 'n0', 'n0'), ('phi', 'pi', 'pi', 'phi'), ('mix', 'chi', 'pi'),
                ('mix', 'mix', 'mix', 'mix')):
        ops = [S[a] for a in seq]

        def mom(idx, ops=ops):
            X = GA.sc(1)
            for i in idx:
                X = mul(X, ops[i])
            return omega(rho, X)
        kap = cumulant(mom, len(seq))
        results[(NB, seq)] = kap
        print(NB, seq, 'cumulant', kap)

for seq in (set(k[1] for k in results) if MAIN else ()):
    k1 = results[(1, seq)]
    ok = all(results[(NB, seq)] == (NB * k1[0], NB * k1[1]) for NB in (2, 3))
    chk(f"cumulant additivity kappa_N = N kappa_1 for {seq}: kappa_1 = {k1}", ok)
print("ALL", galib.OK)
