"""Referee R2: independent recomputation for claim 3 (records of unbounded length).

Own route: explicit sparse matrices (mx.py, MSB / higher-label Jordan-Wigner), elements expanded in the
Clifford blade basis {1, e, f, fe} per rung (the author used 1, v, w, vw on the Fock side).
"""
import random
import sys
from fractions import Fraction as F
from itertools import product
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from mx import Alg, mul, add, sc, dag, mprod, apply, ip, vadd, vsc, is_even_op

AL, BE = F(3, 5), F(4, 5)
OK = True


def report(name, cond):
    global OK
    OK = OK and cond
    print(("PASS " if cond else "FAIL ") + name)


def pair(j):
    return 2 + 2 * j, 3 + 2 * j


def setup(N, c, s):
    m = 2 + 2 * N
    G = Alg(m)
    R, U = [], []
    for j in range(N):
        a, b = pair(j)
        Pi = add(mul(G.on[a], G.off[b]), mul(G.off[a], G.on[b]))
        h = add(mul(G.v[a], G.w[b]), sc(-1, mul(G.v[b], G.w[a])))
        Rj = add(G.I, sc(-1, Pi), sc(c, Pi), sc(s, h))
        R.append(Rj)
        U.append(add(G.off[0], mul(G.on[0], Rj)))
    base = G.vac()
    for j in reversed(range(N)):
        base = apply(G.v[pair(j)[0]], base)
    A0 = apply(G.v[0], base)
    B = apply(G.v[1], base)
    return G, R, U, A0, B


def AK(G, R, A0, K):
    x = A0
    for j in K:
        x = apply(R[j], x)
    return x


def blade_op(G, rung, t):
    # t in 0..3 : 1, e, f, fe on that rung
    return [G.I, G.e[rung], G.f[rung], mul(G.f[rung], G.e[rung])][t]


def interference_vec(x_on, A, B):
    return AL * BE * (ip(A, x_on(B)) + ip(B, x_on(A)))


def word_applier(G, rungs, word):
    ops = [blade_op(G, r, t) for r, t in zip(rungs, word) if t]
    def f(vec):
        for M in reversed(ops):
            vec = apply(M, vec)
            if not vec:
                break
        return vec
    return f


# ---- (i) the factor, full blade basis for N = 2 and N = 3, every proper K, two values of c
for N in (2, 3):
    for c, s in ((F(3, 5), F(4, 5)), (F(0), F(1)), (F(-5, 13), F(12, 13))):
        G, R, U, A0, B = setup(N, c, s)
        # unitarity of U_j and R_j
        report(f"N={N} c={c}: R_j, U_j unitary and even",
               all(mul(Rj, dag(Rj)) == G.I and is_even_op(Rj, G.m) for Rj in R) and
               all(mul(Uj, dag(Uj)) == G.I for Uj in U))
        # Psi_N = 3/5 A_N + 4/5 B as defined via the couplings
        psi0 = vadd(vsc(AL, A0), vsc(BE, B))
        psiN = psi0
        for Uj in U:
            psiN = apply(Uj, psiN)
        AN = AK(G, R, A0, range(N))
        report(f"N={N} c={c}: U_(N-1)..U_0 Psi_0 = 3/5 A_N + 4/5 B", psiN == vadd(vsc(AL, AN), vsc(BE, B)))
        total = nonzero = odd_nonzero_pairs = 0
        good = True
        for mask in range(2 ** N - 1):
            K = [j for j in range(N) if (mask >> j) & 1]
            rungs = [0, 1] + [r for j in K for r in pair(j)]
            AKv = AK(G, R, A0, K)
            fac = c ** (N - len(K))
            for word in product(range(4), repeat=len(rungs)):
                xa = word_applier(G, rungs, word)
                lhs = interference_vec(xa, AN, B)
                rhs = fac * interference_vec(xa, AKv, B)
                total += 1
                if interference_vec(xa, AKv, B) != 0:
                    nonzero += 1
                good = good and lhs == rhs
        report(f"N={N} c={c}: I_N(x) = c^(N-k) I_K(x) on all {total} blade-basis elements ({nonzero} with I_K != 0)", good)

# ---- (i) random integer combinations of blades, with odd parts and system-record hops, interleaved K
random.seed(20261112)
N = 3
c, s = F(3, 5), F(4, 5)
G, R, U, A0, B = setup(N, c, s)
AN = AK(G, R, A0, range(N))
good = True
for K in ([1], [0, 2], [2], [1, 2]):
    rungs = [0, 1] + [r for j in K for r in pair(j)]
    AKv = AK(G, R, A0, K)
    for trial in range(60):
        terms = [(random.randint(-3, 3), tuple(random.randrange(4) for _ in rungs)) for _ in range(6)]
        # add an explicit hop between the system and a record rung of K
        a = pair(K[0])[0]
        def xa(vec, terms=terms):
            out = {}
            for coef, word in terms:
                out = vadd(out, vsc(coef, word_applier(G, rungs, word)(vec)))
            out = vadd(out, apply(mul(G.v[0], G.w[a]), vec), vsc(2, apply(mul(G.v[a], G.w[1]), vec)))
            return out
        good = good and interference_vec(xa, AN, B) == c ** (N - len(K)) * interference_vec(xa, AKv, B)
report("N=3: factor holds for 240 random elements (both parities, hops system<->record, interleaved K)", good)

# the hypothesis matters: elements touching an uncoupled pair violate the factor
K = [0]
rungs_bad = [0, 1] + list(pair(0)) + list(pair(1))
AKv = AK(G, R, A0, K)
viol = 0
for word in product(range(4), repeat=len(rungs_bad)):
    xa = word_applier(G, rungs_bad, word)
    if interference_vec(xa, AN, B) != c ** (N - 1) * interference_vec(xa, AKv, B):
        viol += 1
report(f"hypothesis is not idle: {viol} blade elements touching uncoupled pair 1 violate the factor with K={{0}}", viol > 0)

# I_K does not depend on how many spectator pairs carry a quantum (used silently in (iii))
vals = []
for Nn in (1, 2, 3):
    Gn, Rn, Un, A0n, Bn = setup(Nn, c, s)
    AK0 = AK(Gn, Rn, A0n, [0])
    rungs = [0, 1, 2, 3]
    vals.append([interference_vec(word_applier(Gn, rungs, w), AK0, Bn) for w in product(range(4), repeat=4)])
report("I_K(x) for K={0} is the same with N = 1, 2, 3 spectator-filled pairs", vals[0] == vals[1] == vals[2])

# ---- (ii) and the off-by-one in the c = 0 sentence of (iii)
for c, s in ((F(3, 5), F(4, 5)), (F(0), F(1))):
    for N in (1, 2, 3):
        G, R, U, A0, B = setup(N, c, s)
        Ut = mprod(*reversed(U)) if N > 1 else U[0]
        O0 = add(mul(G.v[0], G.w[1]), mul(G.v[1], G.w[0]))
        ON = mprod(Ut, O0, dag(Ut))
        AN = AK(G, R, A0, range(N))
        psi = vadd(vsc(AL, AN), vsc(BE, B))
        O2 = mul(ON, ON)
        cond = (dag(ON) == ON and mul(O2, O2) == O2 and is_even_op(ON, G.m)
                and ip(psi, apply(ON, psi)) == F(24, 25)
                and ip(AN, apply(ON, AN)) == 0 and ip(B, apply(ON, B)) == 0)
        report(f"(ii) c={c} N={N}: O_N even, self-adjoint, O_N^2 idempotent, value 24/25, branch values 0", cond)
# the largest pair O_N involves is N-1 < N; for c = 0 the claim says omega_N(x) is then the mixture value
G, R, U, A0, B = setup(1, F(0), F(1))
O0 = add(mul(G.v[0], G.w[1]), mul(G.v[1], G.w[0]))
O1 = mprod(U[0], O0, dag(U[0]))
AN = AK(G, R, A0, [0])
psi = vadd(vsc(AL, AN), vsc(BE, B))
mix = F(9, 25) * ip(AN, apply(O1, AN)) + F(16, 25) * ip(B, apply(O1, B))
print(f"   c=0, N=1, x=O_1 (largest pair involved: 0): omega_N(x) = {ip(psi, apply(O1, psi))}, mixture value = {mix}")
report("COUNTEREXAMPLE to (iii) last sentence: N exceeds the largest pair x involves, yet omega_N(x) != mixture",
       ip(psi, apply(O1, psi)) != mix)

# ---- (iv) one-particle symbols of the two branches, computed from the vectors; Wick check
N = 3
for c, s in ((F(3, 5), F(4, 5)), (F(5, 13), F(12, 13))):
    G, R, U, A0, B = setup(N, c, s)
    AN = AK(G, R, A0, range(N))
    m = G.m
    def symbol(x):
        return [[ip(x, apply(mul(G.v[j], G.w[i]), x)) for j in range(m)] for i in range(m)]  # S_ij = omega(a_j^dag a_i)
    SA, SB = symbol(AN), symbol(B)
    def matmul(X, Y):
        return [[sum(X[i][k] * Y[k][j] for k in range(m)) for j in range(m)] for i in range(m)]
    proj = matmul(SA, SA) == SA and matmul(SB, SB) == SB
    hs2 = sum((SA[i][j] - SB[i][j]) ** 2 for i in range(m) for j in range(m))
    # Wick (quasi-free) check on all 4-point functions omega(a_i^dag a_j^dag a_k a_l)
    wick = True
    for i, j, k, l in product(range(m), repeat=4):
        val = ip(AN, apply(mprod(G.v[i], G.v[j], G.w[k], G.w[l]), AN))
        pred = SA[l][i] * SA[k][j] - SA[k][i] * SA[l][j]
        wick = wick and val == pred
    report(f"(iv) c={c}: both branch symbols are projections, branch A is quasi-free (all {m**4} 4-point functions)", proj and wick)
    report(f"(iv) c={c}: ||S_A - S_B||_HS^2 = {hs2} = 2 (system) + 2 s^2 N = {2 + 2 * s * s * N}", hs2 == 2 + 2 * s * s * N)

print("ALL PASS" if OK else "SOME FAIL (see above; the counterexample line is expected to PASS as a found counterexample)")
