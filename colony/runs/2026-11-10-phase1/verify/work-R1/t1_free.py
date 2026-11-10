"""Certificate in the universal algebra: Q<A1,A2,B1,B2>/(Ai^2=1,Bj^2=1,AiBj=BjAi), dagger = word reversal.
Normal form: (reduced alternating word in A) x (reduced alternating word in B)."""
from fractions import Fraction as F
def red(w):
    out = []
    for ch in w:
        if out and out[-1] == ch: out.pop()
        else: out.append(ch)
    return tuple(out)
def mulw(m1, m2):
    return (red(m1[0] + m2[0]), red(m1[1] + m2[1]))
def mul(x, y):
    r = {}
    for a, ca in x.items():
        for b, cb in y.items():
            m = mulw(a, b); r[m] = r.get(m, 0) + ca * cb
    return {k: v for k, v in r.items() if v}
def add(*xs):
    r = {}
    for x in xs:
        for k, v in x.items(): r[k] = r.get(k, 0) + v
    return {k: v for k, v in r.items() if v}
def sc(c, x): return {k: F(c) * v for k, v in x.items()}
def dag(x): return {(a[::-1], b[::-1]): v for (a, b), v in x.items()}
E = {((), ()): F(1)}
A1 = {((1,), ()): F(1)}; A2 = {((2,), ()): F(1)}; B1 = {((), (1,)): F(1)}; B2 = {((), (2,)): F(1)}
C = add(mul(A1, add(B1, B2)), mul(A2, add(B1, sc(-1, B2))))
X = add(mul(A1, A2), sc(-1, mul(A2, A1))); Y = add(mul(B1, B2), sc(-1, mul(B2, B1)))
SA = add(mul(A1, A2), mul(A2, A1)); SB = add(mul(B1, B2), mul(B2, B1))
Z = add(X, sc(-1, Y))
C2 = mul(C, C)
print("C dagger = C:", dag(C) == C)
print("C^2 = 4 - XY:", C2 == add(sc(4, E), sc(-1, mul(X, Y))))
rhs = sc(F(1, 2), add(mul(dag(Z), Z), mul(SA, SA), mul(SB, SB)))
print("8 - C^2 = (Z+Z + SA^2 + SB^2)/2:", add(sc(8, E), sc(-1, C2)) == rhs)
print("X+X = 4 - SA^2:", mul(dag(X), X) == add(sc(4, E), sc(-1, mul(SA, SA))))
# sign-convention perturbations must fail
Zp = add(X, Y)
print("with Z = X + Y (should be False):", add(sc(8, E), sc(-1, C2)) == sc(F(1, 2), add(mul(dag(Zp), Zp), mul(SA, SA), mul(SB, SB))))
Cp = add(mul(A1, add(B1, B2)), mul(A2, add(B2, sc(-1, B1))))
print("C' = A1(B1+B2)+A2(B2-B1): C'^2 = 4 + XY:", mul(Cp, Cp) == add(sc(4, E), mul(X, Y)))
# three party: A+,A-
Ap = add(A1, A2); Am = add(A1, sc(-1, A2))
print("A+A- + A-A+ = 0:", add(mul(Ap, Am), mul(Am, Ap)) == {}, " A+^2 + A-^2 = 4:", add(mul(Ap, Ap), mul(Am, Am)) == sc(4, E))
print("C = A+B1 + A-B2:", C == add(mul(Ap, B1), mul(Am, B2)))
