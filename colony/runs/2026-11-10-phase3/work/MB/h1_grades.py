"""H1 probe: grades of psi e_t rev(psi) for psi in S = Cl^0(V) f, causal towers of dimension 3, 4, 5.
Exact (GA.py over Fractions). Question: is the vector projection in j(psi) = <psi e_t rev(psi)>_1 vacuous?"""
import sys, itertools
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA

def grades(x):
    return sorted({bin(b).count('1') if isinstance(b, int) else len(b) for b, c in x.items() if c != 0})

def run(p, q):
    n = p + q
    sq = GA.sig(p, q)
    t = 0 if p == 1 else p          # the single generator of the minority sign
    a = 1 if t == 0 else 0
    et, ea = GA.gen(t), GA.gen(a)
    f = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.mul(et, ea, sq)))
    blades = [b for b in GA.all_blades(n)]
    even = []
    for b in blades:
        x = {b: F(1)}
        if grades(x)[0] % 2 == 0:
            even.append(x)
    out = set(); s_vals = []
    k = 0
    for coeffs in itertools.product((-1, 0, 1, 2), repeat=4):
        k += 1
        psi = {}
        for i, e in enumerate(even):
            c = coeffs[i % 4] + (i // 4) * coeffs[(i + 1) % 4]
            psi = GA.add(psi, GA.scal(F(c), e))
        psi = GA.mul(psi, f, sq)
        y = GA.mul(GA.mul(psi, et, sq), GA.reverse(psi), sq)
        g = tuple(grades(y))
        out.add(g)
    return out

for sig in [(2, 1), (1, 2), (1, 3), (3, 1), (4, 1), (1, 4)]:
    print(sig, run(*sig))
