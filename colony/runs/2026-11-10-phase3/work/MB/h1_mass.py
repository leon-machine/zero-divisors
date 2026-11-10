"""H1 probe 2: in dimension five, psi e_t rev(psi) = j + s I_5. Compare m^2 = Q(e_t) Q(j) with s^2 (exact)."""
import sys, itertools
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA

def run(p, q):
    n = p + q; sq = GA.sig(p, q)
    t = 0 if p == 1 else p; a = 1 if t == 0 else 0
    et, ea = GA.gen(t), GA.gen(a)
    f = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.mul(et, ea, sq)))
    even = [{b: F(1)} for b in GA.all_blades(n) if len(b) % 2 == 0]
    I = {tuple(range(n)): F(1)}
    I2 = GA.mul(I, I, sq)[()]
    Qt = sq[t]
    rows = set()
    for coeffs in itertools.product((-1, 0, 1, 2), repeat=4):
        psi = {}
        for i, e in enumerate(even):
            psi = GA.add(psi, GA.scal(F(coeffs[i % 4] + (i // 4) * coeffs[(i + 1) % 4]), e))
        psi = GA.mul(psi, f, sq)
        y = GA.mul(GA.mul(psi, et, sq), GA.reverse(psi), sq)
        j = {b: c for b, c in y.items() if len(b) == 1}
        s = y.get(tuple(range(n)), F(0))
        Qj = GA.mul(j, j, sq).get((), F(0))
        m2 = Qt * Qj
        rows.add((m2, s * s))
    ratios = {m2 / s2 for m2, s2 in rows if s2 != 0}
    zero_ok = all(m2 == 0 for m2, s2 in rows if s2 == 0)
    return I2, Qt, ratios, zero_ok, len(rows)

for sig in [(4, 1), (1, 4)]:
    print(sig, run(*sig))
