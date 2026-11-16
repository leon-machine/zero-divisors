import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, gtg
from pert2 import build, split, Z, E1
k = F(3, 2); s0, c0 = F(3, 5), F(4, 5)
a_c = [F(2), F(3), F(5, 7), F(1, 3)]
a0 = a_c[0]; Hc = a_c[1] / a0
z = [F(0)] * 4
P = [F(7, 3), F(1, 2), F(-2, 5), F(1, 7)]
S = [F(5, 2), F(-1, 3), F(3, 4), F(2, 7)]
B = [F(1, 4), F(2, 3), F(-3, 5), F(1, 9)]
for name, (p, q, r) in {'phi': (P, z, z), 'psi': (z, S, z), 'b': (z, z, B)}.items():
    fld = build(a_c, p, q, r, k, s0, c0)
    print(name)
    for mu in range(4):
        print("  Omega(e_%d):" % mu, {bl: (str(split(c)[0]), str(split(c)[1])) for bl, c in fld.Om[mu].items() if split(c) != (0, 0)})
print("Hc", Hc, "k phi s", k * P[0] * s0, "psi' c", S[1] * c0, "k psi s", k * S[0] * s0, "Hc*phi c", Hc*P[0]*c0, "Hc psi c", Hc*S[0]*c0)
print("b: b' s", B[1]*s0, "Hc b s", Hc*B[0]*s0, "k b c", k*B[0]*c0)
