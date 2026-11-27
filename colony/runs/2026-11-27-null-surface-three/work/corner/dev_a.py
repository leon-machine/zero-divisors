from dev import *
from fractions import Fraction as F
t0 = time.time()
coef = (F(1), F(-1), F(1), F(-1, 2))
pts = ck.quadratic_points()
count = nonzero = 0; ok = True
for H in ck.sym_units():
    cache = {}
    for xi in ck.E:
        for pc, qc in pts:
            p, q = ck.vec(pc), ck.vec(qc)
            if pc not in cache:
                cache[pc] = ck.einstein(H, p)
            lhs = ck.omega(H, p, ck.outer(q, xi), q)
            rhs = ck.add(ck.scal(2, ck.apply(cache[pc], xi)), ck.vdotB(ck.add(p, q), ck.potential_symbol(H, p, xi, q, coef)))
            ok = ok and GA.eq(lhs, rhs)
            count += 1; nonzero += 0 if GA.is_zero(lhs) else 1
print(ok, count, nonzero, time.time() - t0)
