"""R3 referee: independent tests of imports 1b, 1c, 1d (exact where possible, mpmath for continuation)."""
from fractions import Fraction as Fr
from math import gcd, isqrt
import mpmath as mp

mp.mp.dps = 30


def squarefree(n):
    n = abs(n)
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p += 1
    return True


def fundamental(D):
    if D in (0, 1):
        return False
    if D % 4 == 1:
        return squarefree(D)
    if D % 4 == 0:
        d = D // 4
        return d % 4 in (2, 3) and squarefree(d)
    return False


def jacobi(a, n):  # n odd positive
    a %= n
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


def kron(D, m):
    """Kronecker symbol (D/m), m >= 1."""
    if m == 0:
        return 0
    r = 1
    while m % 2 == 0:
        m //= 2
        if D % 2 == 0:
            return 0
        r *= 1 if D % 8 in (1, 7) else -1
    return r * jacobi(D, m)


def B2(x):
    return x * x - x + Fr(1, 6)


def L0(D):
    f = abs(D)
    return sum(kron(D, a) * (Fr(1, 2) - Fr(a, f)) for a in range(1, f + 1))


def Lm1(D):
    f = abs(D)
    return -Fr(f, 2) * sum(kron(D, a) * B2(Fr(a, f)) for a in range(1, f + 1))


def h_reduced(D):
    h = 0
    a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a:
                continue
            if b < 0 and (a == c):
                continue
            h += 1
        a += 1
    return h


def w(D):
    # count unit solutions directly
    cnt = 0
    for x in range(-3, 4):
        for y in range(-3, 4):
            if D % 2:
                v = x * x + x * y + (1 - D) // 4 * y * y
            else:
                v = x * x - D // 4 * y * y
            if v == 1:
                cnt += 1
    return cnt


def sigma(n):
    return sum(d for d in range(1, n + 1) if n % d == 0)


def divsum(D):
    s = 0
    for b in range(-isqrt(D), isqrt(D) + 1):
        if b * b < D and (b - D) % 2 == 0:
            s += sigma((D - b * b) // 4)
    return -Fr(s, 5)


out = []
# (c): class number formula at 0
neg = [D for D in range(-3, -2001, -1) if fundamental(D)]
bad = [D for D in neg if L0(D) != Fr(2 * h_reduced(D), w(D))]
out.append(f"(c) fundamental D in [-2000,-3]: {len(neg)} tested, failures {bad[:5]}")
# kronecker period |D| and parity
badp = [D for D in neg[:80] if any(kron(D, m) != kron(D, m + abs(D)) for m in range(1, 3 * abs(D))) or kron(D, abs(D) - 1) != -1]
out.append(f"(c) period |D| and chi(-1)=-1 failures: {badp}")
# non-fundamental counter-check: D = -12 (h of primitive forms 1, w 2, but L0 of kron(-12,.) ?)
for D in (-12, -16, -27, -28):
    out.append(f"   non-fundamental D={D}: L0={L0(D)}, 2h_red/w={Fr(2*h_reduced(D), w(D))}")
# (d): divisor sum
pos = [D for D in range(2, 3001) if fundamental(D)]
badd = [D for D in pos if Lm1(D) != divsum(D)]
out.append(f"(d) fundamental D in [2,3000]: {len(pos)} tested, failures {badd[:5]}")
out.append(f"   D=5,8,12,13: {[Lm1(D) for D in (5,8,12,13)]}")
for D in (12*4, 20, 45):
    out.append(f"   non-fundamental D={D}: Lm1={Lm1(D)}, divsum={divsum(D)}")
# (b): Hurwitz values by mpmath continuation
for a in (Fr(1, 3), Fr(1, 2), Fr(3, 4), Fr(1)):
    A = mp.mpf(a.numerator) / a.denominator
    z0 = mp.zeta(0, A); z1 = mp.zeta(-1, A)
    out.append(f"(b) a={a}: zeta(0,a)={mp.nstr(z0,15)} vs {float(Fr(1,2)-a)}; zeta(-1,a)={mp.nstr(z1,15)} vs {float(-B2(a)/2)}")
# (b)(iii) at s=0,-1 against mpmath's dirichlet()
for D in (-4, -23, 5, 12):
    f = abs(D)
    chi = [kron(D, a) for a in range(f)]
    out.append(f"(b)(iii) D={D}: mp L(0)={mp.nstr(mp.dirichlet(0, chi),15)} vs {float(L0(D))}; L(-1)={mp.nstr(mp.dirichlet(-1, chi),15)} vs {float(Lm1(D))}")
# (b)(iv): removing Euler factor at p=2 from chi_{5}: chi' agrees off 2, vanishes at evens; period 10
D = 5
chi = [kron(D, a) for a in range(5)]
chip = [kron(D, a) if a % 2 else 0 for a in range(10)]
for s in (0, -1, mp.mpf('0.5'), 2):
    lhs = mp.dirichlet(s, chip)
    rhs = mp.dirichlet(s, chi) * (1 - kron(D, 2) * mp.power(2, -s))
    out.append(f"(b)(iv) s={s}: {mp.nstr(lhs,15)} vs {mp.nstr(rhs,15)}")
# principal character: "for all s" includes s=1 pole
out.append("(b)(iv) note: for chi principal, L has a pole at s=1; the identity holds for s != 1")
print("\n".join(out))
