"""Lead 5, exact tests of kill conditions K5a and K5b. Run: python3 lead5.py

K5a. Signatures (p, q) of one dimension n and the residue p - q mod 8: which pairs of signatures share a residue,
     and by how many sign changes they differ. Algebra data of the stored table (std-algebra.periodicity) are
     functions of the residue and the dimension; the even subalgebra Cl^0(p,q) = Cl(p,q-1) = Cl(q,p-1) likewise.
K5b. N copies of the tautological line over RP^n are trivial when R^N carries a linear family g(x), x in R^(n+1),
     with g(x) invertible for x != 0 (then (x, v) -> g(x) v descends, since g(-x) = -g(x)). Such a family is
     x_0 + sum x_i J_i with n anticommuting maps J_i of square -1; built here exactly for n <= 8. Lower bound from
     the stored Whitney formula: (1 + x)^N != 1 in Z_2[x]/(x^(n+1)) forbids N copies from being stably trivial.
"""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', '..', 'lib'))
import GA

ok = True
# ---- K5a
for n in range(1, 13):
    sigs = [(p, n - p) for p in range(n + 1)]
    for (p, q) in sigs:
        for (p2, q2) in sigs:
            if (p - q) % 8 == (p2 - q2) % 8 and p != p2:
                ok &= ((p - p2) % 4 == 0)                       # equal residues: differ by a multiple of four signs
            if abs(p - p2) == 2:
                ok &= ((p - q) % 8 != (p2 - q2) % 8)            # two sign changes move the residue by four
            if abs(p - p2) == 1:
                ok &= (((p - q) - (p2 - q2)) % 8 in (2, 6))     # one sign change (a tame wall) moves it by two
coll4 = [((p, 4 - p), (p2, 4 - p2)) for p in range(5) for p2 in range(p) if (2 * p - 4) % 8 == (2 * p2 - 4) % 8]
print("dimension four, signatures with equal residue:", coll4)
ok &= (coll4 == [((4, 0), (0, 4))])
coll6 = [((p, 6 - p), (p2, 6 - p2)) for p in range(7) for p2 in range(p) if (2 * p - 6) % 8 == (2 * p2 - 6) % 8]
print("dimension six:", coll6)
ok &= (((6, 0), (2, 4)) in coll6)                               # the physical tower's floor (2,4) shares residue 6 with (6,0)

# ---- K5b
def kron(a, b):
    return [[x * y for x in ra for y in rb] for ra in a for rb in b]

I2 = [[F(1), F(0)], [F(0), F(1)]]
EPS = [[F(0), F(1)], [F(-1), F(0)]]
S1 = [[F(0), F(1)], [F(1), F(0)]]
S3 = [[F(1), F(0)], [F(0), F(-1)]]

def tensor(*ms):
    out = [[F(1)]]
    for m in ms:
        out = kron(out, m)
    return out

def anticommuting_structures(n):
    """n anticommuting antisymmetric maps of square -1, on R^N with N the Radon-Hurwitz dimension, n <= 8."""
    if n == 1:
        return [EPS]
    if n in (2, 3):
        return [tensor(EPS, I2), tensor(S1, EPS), tensor(S3, EPS)][:n]
    # seven on R^8 (octonion-type), an eighth needs R^16
    j8 = [tensor(I2, I2, EPS), tensor(I2, EPS, S1), tensor(EPS, I2, S3), tensor(EPS, S1, S1), tensor(EPS, S3, S1),
          tensor(S1, EPS, S3), tensor(S3, EPS, S3)]
    if n <= 7:
        return j8[:n]
    # n = 8 on R^16: J_i (x) s1 for the seven, and 1 (x) eps... must anticommute: use J_i (x) S1 and 1_8 (x) EPS
    return [kron(j, S1) for j in j8] + [kron(tensor(I2, I2, I2), EPS)]

def is_structure_set(js):
    N = len(js[0])
    ident = [[F(1) if i == j else F(0) for j in range(N)] for i in range(N)]
    good = True
    for i, a in enumerate(js):
        good &= GA.mat_eq(GA.mat_mul(a, a), [[-x for x in r] for r in ident])
        good &= GA.mat_eq([list(r) for r in zip(*a)], [[-x for x in r] for r in a])
        for b in js[i + 1:]:
            ab, ba = GA.mat_mul(a, b), GA.mat_mul(b, a)
            good &= all(ab[r][c] + ba[r][c] == 0 for r in range(N) for c in range(N))
    return good

def sw_lower_bound(n):
    """Least power of two N with (1 + x)^N = 1 in Z_2[x]/(x^(n+1))."""
    N = 1
    while True:
        coeffs = [1]
        for _ in range(N):
            new = [0] * (len(coeffs) + 1)
            for i, c in enumerate(coeffs):
                new[i] ^= c
                new[i + 1] ^= c
            coeffs = new[:n + 1]
        if all(c == 0 for c in coeffs[1:n + 1]):
            return N
        N *= 2

table = []
for n in range(1, 9):
    js = anticommuting_structures(n)
    good = is_structure_set(js)
    ok &= good
    N = len(js[0])
    lb = sw_lower_bound(n)
    table.append((n, N, lb))
    ok &= (N == lb)
print("n, copies trivialised by the Clifford family, least power of two allowed by the Whitney formula:")
for row in table:
    print("  RP^%d: %d, %d" % row)
ok &= (table[4] == (5, 8, 8)) and (table[7] == (8, 16, 16))
print("lead 5 tests:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
