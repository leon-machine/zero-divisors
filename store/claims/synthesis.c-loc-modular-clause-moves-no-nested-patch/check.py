"""synthesis.c-loc-modular-clause-moves-no-nested-patch: exact checks.

Gaussian rationals are pairs of Fractions. (1) On a two-mode window (Jordan-Wigner 4 x 4 matrices) a boost
step that multiplies each mode by a unit Gaussian-rational phase z^{w_j}, z = (3 + 4i)/5, weights (1, 2),
satisfies the CAR, acts by phases on the generators and preserves the window: the point-spectrum flow of the
Definition. (2) z is not a root of unity (z^n != 1 for 1 <= n <= 200; the proof gives the general argument),
yet the flow recurs: |z^61 - 1|^2 < 1/1000 and |z^122 - 1|^2 < 1/250, so the window flow comes back
arbitrarily close to the identity without being periodic. (3) Contrast: the bilateral shift, the model of a
dilation with Lebesgue spectrum, never recurs (|S^n e_0 - e_0|^2 = 2 for every n >= 1) and maps the closed
span of e_k, k >= 0, properly into itself; this is the behaviour the geometric reading needs and the
point-spectrum flow cannot have.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise


def c(a, b=0):
    return (F(a), F(b))


def cadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def cmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def cconj(x):
    return (x[0], -x[1])


def cpow(x, n):
    r = c(1)
    for _ in range(n):
        r = cmul(r, x)
    return r


def zeros(n):
    return [[c(0) for _ in range(n)] for _ in range(n)]


def mm(A, B):
    n = len(A)
    out = zeros(n)
    for i in range(n):
        for k in range(n):
            if A[i][k] != c(0):
                for j in range(n):
                    out[i][j] = cadd(out[i][j], cmul(A[i][k], B[k][j]))
    return out


def madd(A, B):
    return [[cadd(A[i][j], B[i][j]) for j in range(len(A))] for i in range(len(A))]


def mscal(s, A):
    return [[cmul(s, A[i][j]) for j in range(len(A))] for i in range(len(A))]


def dag(A):
    n = len(A)
    return [[cconj(A[j][i]) for j in range(n)] for i in range(n)]


def eye(n):
    out = zeros(n)
    for i in range(n):
        out[i][i] = c(1)
    return out


def kron(A, B):
    na, nb = len(A), len(B)
    out = zeros(na * nb)
    for i in range(na):
        for j in range(na):
            for k in range(nb):
                for m in range(nb):
                    out[i * nb + k][j * nb + m] = cmul(A[i][j], B[k][m])
    return out


def window():
    lower = [[c(0), c(1)], [c(0), c(0)]]       # |1> -> |0>
    parity = [[c(1), c(0)], [c(0), c(-1)]]
    a1 = kron(lower, eye(2))
    a2 = kron(parity, lower)
    return a1, a2


def check_window_flow_acts_by_phases():
    premise("synthesis.point-spectrum-boost-admits-no-half-sided-translations")
    a1, a2 = window()
    modes = [a1, a2]
    for i in range(2):
        for j in range(2):
            ac = madd(mm(modes[i], dag(modes[j])), mm(dag(modes[j]), modes[i]))
            GA.check("CAR {a_%d, a_%d*}" % (i, j), ac == (eye(4) if i == j else zeros(4)))
            aa = madd(mm(modes[i], modes[j]), mm(modes[j], modes[i]))
            GA.check("CAR {a_%d, a_%d}" % (i, j), aa == zeros(4))
    z = (F(3, 5), F(4, 5))
    GA.check("|z| = 1", cmul(z, cconj(z)) == c(1))
    weights = (1, 2)
    # basis index 2 n1 + n2, occupation (n1, n2); U = diag z^{w1 n1 + w2 n2}
    U = zeros(4)
    for n1 in range(2):
        for n2 in range(2):
            U[2 * n1 + n2][2 * n1 + n2] = cpow(z, weights[0] * n1 + weights[1] * n2)
    GA.check("U unitary", mm(U, dag(U)) == eye(4))
    for j, a in enumerate(modes):
        ta = mm(mm(U, a), dag(U))
        GA.check("tau(a_%d) = conj(z)^w a_%d" % (j, j), ta == mscal(cpow(cconj(z), weights[j]), a))
    return True


def check_recurrence_without_period():
    premise("synthesis.point-spectrum-boost-admits-no-half-sided-translations")
    z = (F(3, 5), F(4, 5))
    # z = (2 + i)/(2 - i): numerator and denominator are non-associate Gaussian primes
    GA.check("z = (2+i)/(2-i)", cmul(z, c(2, -1)) == c(2, 1))
    p = c(1)
    hits = []
    for n in range(1, 201):
        p = cmul(p, z)
        GA.check("z^%d != 1" % n, p != c(1))
        d2 = 2 - 2 * p[0]                      # |z^n - 1|^2 for |z| = 1
        if d2 < F(1, 1000):
            hits.append(n)
    GA.check("first close return at n = 61", hits[:1] == [61])
    d61 = 2 - 2 * cpow(z, 61)[0]
    d122 = 2 - 2 * cpow(z, 122)[0]
    GA.check("|z^61 - 1|^2 < 1/1000", d61 < F(1, 1000))
    GA.check("|z^122 - 1|^2 < 1/250", d122 < F(1, 250))
    # with integer weights w the phase z^{w n} returns too: |z^{2n} - 1| <= 2 |z^n - 1|
    GA.check("weight 2 returns with weight 1", 2 - 2 * cpow(z, 2 * 61)[0] <= 4 * d61)
    return True


def check_shift_contrast():
    premise("synthesis.point-spectrum-boost-admits-no-half-sided-translations")
    # vectors in l^2(Z) as finite dicts k -> coefficient; S e_k = e_{k+1}
    def shift(v, n):
        return {k + n: x for k, x in v.items()}

    def norm2(v):
        return sum(x * x for x in v.values())

    def sub(v, w):
        out = dict(v)
        for k, x in w.items():
            out[k] = out.get(k, 0) - x
        return {k: x for k, x in out.items() if x != 0}

    e0 = {0: F(1)}
    for n in range(1, 50):
        GA.check("no return of the shift at n = %d" % n, norm2(sub(shift(e0, n), e0)) == 2)
    # S maps span{e_k : k >= 0} onto span{e_k : k >= 1}, a proper closed subspace: e_0 is orthogonal to it
    image_supports = {min(shift({k: F(1)}, 1)) for k in range(0, 40)}
    GA.check("image misses e_0", 0 not in image_supports and min(image_supports) == 1)
    return True
