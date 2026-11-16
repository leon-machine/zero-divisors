"""R2 independent recomputation for the order-four-walls proposal.

Pre-registered kill conditions:
 K4. J^2 != (-1)^(m+q) for some Cl(p,q), p+q = 2m <= 10 (GA computation), or J fails to anticommute with a vector.
 K5. Stiefel-Whitney: if w_2(RP^n) = x^2 with w_1 = 0 is not exactly n = 1 mod 4, or w_2(T RP^n + 2L) = 0 not
     exactly n = 1 mod 4 (n odd), or L^5(4) admits a class a with a^2 = w_2, the class statements fail.
 K6. With the textbook Standard Model charges of the 16 (my own table, not the proposal's occupation-state
     weights), if some torus involution reverses a number of states other than 0 or 8, or reverses the neutral
     singlet, or the number of patterns is not 16, clause (vi) fails.
"""
import sys
from fractions import Fraction as F
from itertools import product
sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA

# K4
ok = True
for n in (2, 4, 6, 8, 10):
    m = n // 2
    for q in range(n + 1):
        sq = GA.sig(n - q, q)
        J = {tuple(range(n)): F(1)}
        J2 = GA.mul(J, J, sq)
        ok = ok and GA.eq(J2, GA.sc((-1) ** (m + q)))
        ok = ok and all(GA.anticommutes(J, GA.gen(i), sq) for i in range(n))
GA.check("K4: pseudoscalar of Cl(p,q), p+q=2m<=10, squares to (-1)^(m+q) and anticommutes with vectors", ok)
# jump: Cl(6,2), J6 j = -J51 E with J51 = e1..e5 f1, E = e6 f2
s62 = GA.sig(6, 2)
J6, j = {(0, 1, 2, 3, 4, 5): F(1)}, {(6, 7): F(1)}
J51, E = {(0, 1, 2, 3, 4, 6): F(1)}, {(5, 7): F(1)}
ok = GA.eq(GA.mul(J51, E, s62), GA.neg(GA.mul(J6, j, s62))) and GA.eq(GA.mul(E, E, s62), GA.sc(1))
ok = ok and GA.eq(GA.mul(J51, J51, s62), GA.sc(1)) and GA.eq(GA.mul(J6, J6, s62), GA.sc(-1))
GA.check("K4: in Cl(6,2), J_{5,1} E = -J_{6,0} j; squares +1, +1, -1", ok)


# K5: total classes as polynomials over Z_2 truncated at degree n
def binom(a, b):
    if b < 0 or a < b:
        return 0
    out = 1
    for t in range(b):
        out = out * (a - t) // (t + 1)
    return out


twist, spin = [], []
for n in range(2, 22):
    w1, w2 = (n + 1) % 2, binom(n + 1, 2) % 2
    ext1, ext2 = (n + 3) % 2, binom(n + 3, 2) % 2           # T + 2L, w(L) = 1 + x
    if w1 == 0 and w2 == 0:
        spin.append(n)
    if ext1 == 0 and ext2 == 0 and not (w1 == 0 and w2 == 0):
        twist.append(n)
print("RP^n spin:", spin, " RP^n with Spin-Z4 (T+2L spin) but not spin:", twist)
ok = spin == [n for n in range(2, 22) if n % 4 == 3] and twist == [n for n in range(2, 22) if n % 4 == 1]
GA.check("K5: RP^n spin iff n = 3 mod 4; order-four structure with tautological line (not spin) iff n = 1 mod 4", ok)
# sides on RP^(2m-1): w(pL) w(qL); class w2(E+) + w2(E-) for a flat side
ok = all((binom(p, 2) + binom(q, 2)) % 2 == ((p + q) // 2 + q) % 2 for p in range(13) for q in range(13)
         if (p + q) % 2 == 0)
GA.check("K5: C(p,2) + C(q,2) = m + q mod 2 for p + q = 2m", ok)
# lens L^(2k+1)(4): H^*(Z_2) = Lambda[x] (x) Z_2[u]; w(T + R) = (1 + u)^(k+1); a in {0, x}, a^2 = 0.
res = {}
for k in range(1, 8):
    w2 = (k + 1) % 2   # coefficient of u
    res[k] = ("spin" if w2 == 0 else "not spin; no a with a^2 = w2")
print("lens spaces L^(2k+1)(4):", res)
GA.check("K5: L^5(4) (k = 2) is not spin and has no Spin-Z4 structure", res[2].startswith("not spin"))

# K6: textbook SM charges of one generation (left-handed Weyl fields), hypercharge Y with Q = T3 + Y.
# colour weights for a triplet: (1,0), (-1,1), (0,-1) in the basis (h1, h2) of fundamental weights; antitriplet negated.
trip = [(1, 0), (-1, 1), (0, -1)]
states = []
for c in trip:
    for t3 in (F(1, 2), F(-1, 2)):
        states.append(("Q", c, t3, F(1, 6)))
for c in trip:
    states.append(("uc", (-c[0], -c[1]), F(0), F(-2, 3)))
    states.append(("dc", (-c[0], -c[1]), F(0), F(1, 3)))
for t3 in (F(1, 2), F(-1, 2)):
    states.append(("L", (0, 0), t3, F(-1, 2)))
states.append(("ec", (0, 0), F(0), F(1)))
states.append(("nuc", (0, 0), F(0), F(0)))
assert len(states) == 16
# sanity: anomaly sums
GA.check("charges: sum Y = 0, sum Y^3 = 0 on the sixteen", sum(s[3] for s in states) == 0 and sum(s[3] ** 3 for s in states) == 0)
den = 12
patterns = set()
for a, b, c1, c2 in product(range(den), range(2 * den), range(den), range(den)):
    # element exp(2 pi i (a/den * 6Y + b/(2 den) * 2T3 + c1/den h1 + c2/den h2))
    ph = []
    good = True
    for s in states:
        x = F(a, den) * 6 * s[3] + F(b, 2 * den) * 2 * s[2] + F(c1, den) * s[1][0] + F(c2, den) * s[1][1]
        if (2 * x).denominator != 1:
            good = False
            break
        ph.append(int(2 * x) % 2)
    if good:
        patterns.add(tuple(ph))
flips = sorted(sum(p) for p in patterns)
nu = [i for i, s in enumerate(states) if s[0] == "nuc"][0]
print("number of sign patterns:", len(patterns), " flipped counts:", sorted(set(flips)), flips.count(0), flips.count(8))
ok = len(patterns) == 16 and set(flips) == {0, 8} and all(p[nu] == 0 for p in patterns)
GA.check("K6: torus involutions of the SM group on the sixteen: 16 patterns, each reverses 0 or 8, none the singlet", ok)
c16 = sorted(set(-16 + 2 * f for f in flips)); c15 = sorted(set(-15 + 2 * f for f in flips))
print("signed counts of omega g: sixteen", c16, " fifteen", c15)
gcd_diff = 0
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


for x in c16:
    gcd_diff = gcd(gcd_diff, x - c16[0])
print("gcd of differences of the counts on sixteen (maximal modulus of well-definedness):", gcd_diff)
GA.check("K6: counts mod 16: 0 on sixteen, 1 on fifteen; 16 is the largest modulus for which the count is a class function",
         all(x % 16 == 0 for x in c16) and all(x % 16 == 1 for x in c15) and gcd_diff == 16)
GA.check("three fifteen-component generations: -45 = 3 mod 16 and 3 = 3 mod 16", (-45) % 16 == 3 and 3 % 16 == 3)
print("FAILURES:", GA.FAILURES)
