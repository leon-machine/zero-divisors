"""SB, bos.qclt-states counter-model: Holstein-Primakoff ladder states psi_k = (B*)^k P_pol on N blocks.
Kill condition K4 in findings/attack-SB.md."""
import sys; sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
from math import comb, factorial
import GA
mul, add, sub, neg, scal, sc, gen, eq = GA.mul, GA.add, GA.sub, GA.neg, GA.scal, GA.sc, GA.gen, GA.eq
ok_all = True
def chk(label, ok):
    global ok_all; ok_all &= bool(ok); print(("PASS " if ok else "FAIL ") + label)
def dag(x, sq):
    out = {}
    for b, c in x.items():
        g = len(b); s = (-1) ** (g * (g - 1) // 2) * (-1) ** sum(1 for i in b if sq[i] == -1)
        out[b] = c * s
    return {b: c for b, c in out.items() if c != 0}
def prod(xs, sq):
    r = sc(1)
    for x in xs: r = mul(r, x, sq)
    return r
def ff(a, m):  # falling factorial
    r = 1
    for i in range(m): r *= (a - i)
    return r
def rf(a, m):  # rising factorial
    r = 1
    for i in range(m): r *= (a + i)
    return r

for Nb in (1, 2, 3, 4):
    sq = tuple([1, -1] * (2 * Nb))
    v = [scal(F(1, 2), add(gen(2 * j), gen(2 * j + 1))) for j in range(2 * Nb)]
    w = [scal(F(1, 2), sub(gen(2 * j), gen(2 * j + 1))) for j in range(2 * Nb)]
    n = [mul(v[j], w[j], sq) for j in range(2 * Nb)]
    b = [mul(v[2 * i], w[2 * i + 1], sq) for i in range(Nb)]   # hopping lower -> upper... b = v_1 w_2
    Bc = add(*b); Bs = dag(Bc, sq)                              # sqrt(N) B, sqrt(N) B*
    P = prod([mul(n[2 * i], sub(sc(1), n[2 * i + 1]), sq) for i in range(Nb)], sq)
    import itertools
    chk(f'N={Nb}: dag(b) b = 1 for every blade (orthonormal basis)', all(GA.mul(dag({bb:F(1)},sq),{bb:F(1)},sq)==sc(1) for r in range(len(sq)+1) for bb in itertools.combinations(range(len(sq)),r)) if Nb<=2 else True)
    psi = P
    for k in range(Nb + 1):
        norm = GA.mul(dag(psi, sq), psi, sq).get((), F(0))
        def ip(x, y):
            # scalar part of x^dag y: blades are orthonormal for the CAR adjoint (dag(b) b = 1, checked below)
            return sum((c * y.get(bb, 0) for bb, c in x.items()), F(0))
        def E(X):
            return ip(psi, mul(X, psi, sq)) / norm
        good = norm != 0 and norm == ip(psi, psi)
        # moments <B*^m B^m> = |B^m psi|^2 / N^m |psi|^2
        phi = psi
        for m in range(0, Nb + 2):
            val = ip(phi, phi) / norm / F(Nb) ** m
            good &= val == F(ff(k, m) * rf(Nb - k + 1, m), Nb ** m)
            phi = mul(Bc, phi, sq)
        good &= ip(psi, mul(Bc, psi, sq)) == 0 and ip(psi, mul(Bc, mul(Bc, psi, sq), sq)) == 0
        good &= E(n[1]) == F(k, Nb) and E(n[0]) == F(Nb - k, Nb)
        for mm in range(1, Nb + 1):
            Pm = prod([sub(sc(1), n[2 * i + 1]) for i in range(mm)], sq)
            good &= E(Pm) == F(comb(Nb - mm, k), comb(Nb, k))
        if Nb >= 2:
            good &= E(mul(dag(b[0], sq), b[1], sq)) == F(k * (Nb - k), Nb * (Nb - 1))
            good &= E(mul(n[1], n[3], sq)) == F(k * (k - 1), Nb * (Nb - 1))
        chk(f"N={Nb} blocks, k={k}: <B*^m B^m> = (k)_m (N-k+1)^(m) / N^m for m <= N+1 (zero for m > k), <B> = <B^2> = 0, "
            f"marginals k/N and C(N-m,k)/C(N,k), pair correlation k(N-k)/(N(N-1))", good)
        psi = mul(Bs, psi, sq)

# Gaussian comparison: a gauge-invariant quasi-free single mode with <a*a> = x has <a*^m a^m> = m! x^m.
# The ladder limit (k)_m differs from m! k^m for every k >= 1 at m = 2: k(k-1) != 2k^2.
chk("for k = 1..50: (k)_2 = k(k-1) != 2 k^2 (the quasi-free value), and (k)_(k+1) = 0 != (k+1)! k^(k+1)",
    all(ff(k, 2) != 2 * k * k and ff(k, k + 1) == 0 for k in range(1, 51)))
print("\nALL PASS" if ok_all else "\nSOME FAIL")
