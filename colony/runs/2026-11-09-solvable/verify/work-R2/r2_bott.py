"""R2 independent check for the Bott-shifted model: does Premise U (U3) hold at the shifted odd towers?

For a causal tower (p,q), conformal space hatV = (p+1, q+1), n = p + q:
  b = complex Witt index floor((n+2)/2) (the stored pair count, dark-tower-matter.pairs and
      synthesis.gauge-algebra-by-tower), real Witt index min(p,q) + 1 = 2;
  F = constituent field = division ring of Cl^0(hatV) = Cl(p+1, q), by residue r + 1 mod 8
      (0,1,2 -> R; 3,7 -> C; 4,5,6 -> H), which reproduces the stored table of dark-tower-matter.constituents-field.
U3: every complex unit that builds a pair lies in F. If b > 2 a unit is needed; F = R supplies none.
Also: GA computation of the conformal pseudoscalar (square, centrality) at (2,1), (10,1), (4,1), (12,1),
and the unit-ball ratios by an independent rational enclosure of pi (Machin series).
"""
import sys
from fractions import Fraction as F

sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA  # noqa: E402


def field(r):
    return {0: "R", 1: "R", 2: "R", 3: "C", 7: "C", 4: "H", 5: "H", 6: "H"}[(r + 1) % 8]


stored = {6: "C", 2: "C", 1: "R", 7: "R", 3: "H", 5: "H", 0: "R", 4: "H"}
print("field rule reproduces stored table:", all(field(r) == stored[r] for r in stored))

print("\nodd residues, causal members up to n = 21:")
for r in (1, 7, 3, 5):
    rows = []
    for p in range(1, 22):
        for q in range(1, 22):
            if min(p, q) != 1 or p + q > 21 or (p - q) % 8 != r:
                continue
            n = p + q
            b = (n + 2) // 2
            real = min(p, q) + 1
            Fd = field(r)
            ok = (b == real) or Fd in ("C", "H")
            rows.append((n, (p, q), b, real, Fd, ok))
    rows.sort()
    for row in rows:
        n, s, b, real, Fd, ok = row
        print(f"  r={r} {s} n={n} pairs b={b} real={real} field={Fd} U3 {'holds' if ok else 'FAILS'}")


def pseudo(p, q):
    sq = tuple([1] * p + [-1] * q)
    top = tuple(range(p + q))
    c, rest = GA.blade_mul(top, top, sq)
    assert rest == ()
    w = {top: F(1)}
    central = all(GA.commutes(w, GA.gen(i), sq) for i in range(p + q))
    return c, central


print("\nconformal pseudoscalars (square, central):")
for s in ((2, 1), (10, 1), (4, 1), (12, 1), (1, 2), (1, 10), (1, 4), (1, 12)):
    print(f"  tower {s}: Cl{(s[0] + 1, s[1] + 1)} omega^2 = {pseudo(s[0] + 1, s[1] + 1)}")


# pi enclosure by Machin: pi = 16 atan(1/5) - 4 atan(1/239), alternating series bounds
def atan_bounds(x, terms):
    s, lo, hi = F(0), None, None
    for k in range(terms):
        s += F((-1) ** k) * x ** (2 * k + 1) / (2 * k + 1)
    t = x ** (2 * terms + 1) / (2 * terms + 1)
    return (s - t, s + t)


a = atan_bounds(F(1, 5), 12)
b_ = atan_bounds(F(1, 239), 6)
pi_lo, pi_hi = 16 * a[0] - 4 * b_[1], 16 * a[1] - 4 * b_[0]
print(f"\npi in ({float(pi_lo):.15f}, {float(pi_hi):.15f})")


def ratio_L(pi):
    return 1 + F(8, 3) + F(16, 3) / pi


def ratio_8(pi):
    return 1 + F(320) / pi ** 4 + F(1920) / pi ** 5


print("M_L ratio in", float(ratio_L(pi_hi)), float(ratio_L(pi_lo)))
print("M_8 ratio in", float(ratio_8(pi_hi)), float(ratio_8(pi_lo)))
# a model shifting only residues 3, 5 (the U3-compatible part)
r35 = lambda pi: 1 + F(8, 3) + F(1920) / pi ** 5
print("M_8' (only residues 3, 5 shifted) ratio in", float(r35(pi_hi)), float(r35(pi_lo)))
# ball volumes check V3/V_D
