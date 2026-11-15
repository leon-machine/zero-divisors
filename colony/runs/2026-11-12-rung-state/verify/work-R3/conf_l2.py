"""Confirmation pass: sigma_e-alone counterexample at l = 2 (claim 1 technical level 'one or more old rungs')."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r3_recompute import *
sig = (1, -1, 1, -1, 1, -1)          # old rungs 0,1 (gens 0..3), new rung gens 4 (e), 5 (f)
u = cmul(g(0), g(5), sig)
rho = csc(F(1, 2), cadd(one(), u))
Om = tr_state(rho, sig)
B = all_blades(6)
ok = cmul(u, u, sig) == one() and cdag(u) == u and cmul(rho, rho, sig) == rho
ok = ok and psd([[Om(cmul({a: F(1)}, cdag({b: F(1)}), sig)) for b in B] for a in B])
ok = ok and all(Om(sflip({b: F(1)}, {4})) == Om({b: F(1)}) for b in B)
ok = ok and all(Om({b: F(1)}) == (1 if b == () else 0) for b in all_blades(4))
v = csc(F(1, 2), cadd(g(4), g(5))); w = csc(F(1, 2), cadd(g(4), csc(-1, g(5))))
ok = ok and Om(cmul(v, w, sig)) == F(1, 2) and Om(u) == 1
# claim 3 new check numbers: c=0, N=1, on_{a_1}: 0 vs 16/25 (own Fock)
P = psi_N(1, F(0), F(1)); x = lambda q: fnum(4, q)
A = branch_A({0, 1}, 2, F(0), F(1)); Bv = branch_B(2)
ok3 = fip(P, x(P)) == 0 and F(9, 25) * fip(A, x(A)) + F(16, 25) * fip(Bv, x(Bv)) == F(16, 25)
# claim 4 (v) with system on rungs 1,2 (own Fock, rung index = label), data on rungs 3..7: rule = sign of value of Y - on_1
ok4 = True
for a, b in ((F(3, 5), F(4, 5)), (F(5, 13), F(12, 13))):
    n = 5; first = 0
    for bits in product((0, 1), repeat=n):
        base = {0: F(1)}
        for k in range(n):
            if bits[k]: base = fcre(3 + k, base)
        q = fadd(fsc(a, fcre(1, base)), fsc(b, fcre(2, base)))
        val = sum(F(1, 2 ** (k + 1)) * fip(q, fnum(3 + k, q)) for k in range(n)) - fip(q, fnum(1, q))
        first += val < 0
    ok4 = ok4 and F(first, 2 ** n) == F(ceil(a * a * 2 ** n), 2 ** n)
print("claim1 l=2 sigma_e counterexample:", ok)
print("claim3 on_{a_1} 0 vs 16/25:", ok3)
print("claim4 (v) rungs 1,2, sign of Y - on_1:", ok4)
