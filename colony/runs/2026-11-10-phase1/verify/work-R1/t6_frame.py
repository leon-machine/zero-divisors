from fractions import Fraction as F
import random
from rcl import *
random.seed(3)
for sig in [(3, 0), (0, 3), (1, 3), (3, 1), (2, 2), (4, 1), (0, 5), (3, 3)]:
    A = Cl([1] * sig[0] + [-1] * sig[1]); N = 1 << A.n
    rnd = lambda: {random.randrange(N): F(random.randint(-5, 5)) for _ in range(5)}
    ok = all(A.dag(A.mul(x, y)) == A.mul(A.dag(y), A.dag(x)) for x, y in [(rnd(), rnd()) for _ in range(40)])
    ok2 = all(A.mul({b: F(1)}, A.dag({b: F(1)})) == one() for b in range(N))
    x = rnd(); ok3 = s0(A.mul(x, A.dag(x))) == sum(v * v for v in x.values())
    print(sig, "anti-automorphism:", ok, " blade*dagger=1:", ok2, " positive form:", ok3)
# frame dependence in Cl(1,1): boosted frame
A = Cl([1, -1]); e, f = A.gen(0), A.gen(1)
e2 = add(sc(F(5, 3), e), sc(F(4, 3), f)); f2 = add(sc(F(4, 3), e), sc(F(5, 3), f))
print("boosted frame: e'^2, f'^2, anticommute:", A.mul(e2, e2), A.mul(f2, f2), add(A.mul(e2, f2), A.mul(f2, e2)) == {})
print("e' self-adjoint for the dagger of frame (e,f)?", A.dag(e2) == e2, "  e'+ =", A.dag(e2))
# the 17/8 element is a unit vector of positive square = first vector of a boosted frame
a = add(sc(F(17, 8), e), sc(F(15, 8), f)); b = add(sc(F(15, 8), e), sc(F(17, 8), f))
print("A=(17/8)e+(15/8)f: A^2 =", A.mul(a, a), " partner b^2 =", A.mul(b, b), " anticommute:", add(A.mul(a, b), A.mul(b, a)) == {})
# dagger' of boosted frame: x -> expressed in primed blades; check rho=(1+e)/2 is not dagger'-self-adjoint and omega_rho(a a^dagger') etc.
# dagger'(e) : e = (17/8) a - (15/8) b  -> dagger' fixes a, negates b
ep = add(sc(F(17, 8), a), sc(F(-15, 8), b)); print("e = (17/8)A - (15/8)b:", ep == e)
edag = add(sc(F(17, 8), a), sc(F(15, 8), b)); print("dagger'(e) =", edag, " != e: the state (1+e)/2 of the old frame is not self-adjoint in the new one")
# value of x x^dagger' for x = 1 - A?? : in new frame A is an observable so (1 - A)(1 - A)^dagger' = 2 - 2A ; omega_rho = <(1+e)(.)>_0
rho = add(one(), e); x = sub(one(), a); xx = A.mul(x, x)
print("omega_rho((1-A)(1-A)^dagger') =", s0(A.mul(rho, xx)), " (negative: omega_rho violates (P) of the boosted frame)")
