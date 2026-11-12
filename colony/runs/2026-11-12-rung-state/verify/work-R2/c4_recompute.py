"""Referee R2: independent recomputation for claim 4, plus the counterexample found in amended claim 1.

Explicit matrices (mx.py). Adjoint = transpose (real matrices; e symmetric, f antisymmetric checked).
"""
import sys
from fractions import Fraction as F
from itertools import product, combinations
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from mx import Alg, mul, add, sc, dag, mprod, apply, ip, vadd, vsc, is_even_op

OK = True


def report(name, cond):
    global OK
    OK = OK and cond
    print(("PASS " if cond else "FAIL ") + name)


def tr(A, m):
    return sum(v for (i, j), v in A.items() if i == j) / F(2 ** m)


def gens(G):
    out = []
    for j in range(G.m):
        out += [G.e[j], G.f[j]]
    return out


def blades(G):
    g = gens(G)
    res = []
    for r in range(len(g) + 1):
        for idx in combinations(range(len(g)), r):
            M = G.I
            for i in idx:
                M = mul(M, g[i])
            res.append((idx, M))
    return res


def signflip(idx, which):
    return (-1) ** sum(1 for i in idx if i in which)


# ---------------------------------------------------------------- claim 1, sigma_e alone, l = 1
G = Alg(2)        # rung 0 = A_1 (old), rung 1 = new plane (e = gen index 2, f = gen index 3)
report("adjoint = transpose: e symmetric, f antisymmetric", all(dag(G.e[j]) == G.e[j] and dag(G.f[j]) == sc(-1, G.f[j]) for j in range(2)))
X = mul(G.e[0], G.f[1])
report("X = e_0 f_new is self-adjoint with X^2 = 1", dag(X) == X and mul(X, X) == G.I)
rho = sc(F(1, 4), add(G.I, X))          # (1/2) * projection (1+X)/2, trace-normalised to 1 on C^4... (tr/4 = 1/4)
P = sc(F(1, 2), add(G.I, X))
report("(1+X)/2 is a projection, so Omega(x) = tr(P x)/tr(P) is a state under (P)", mul(P, P) == P and dag(P) == P)
def Omega(M):
    return tr(mul(P, M), 2) / tr(P, 2)
def Omega_half(idx):
    return F(1) if idx == () else F(0) if any(i >= 2 for i in idx) else None
B = blades(G)
restr = all(Omega(M) == (F(1) if idx == () else F(0)) for idx, M in B if all(i < 2 for i in idx))
report("Omega restricts to the tracial state omega on A_1 (blades of rung 0)", restr)
inv_e = all(Omega(M) == signflip(idx, {2}) * Omega(M) for idx, M in B)
inv_f = all(Omega(M) == signflip(idx, {3}) * Omega(M) for idx, M in B)
report("Omega is invariant under sigma_e (e_new -> -e_new), which exchanges on and off", inv_e)
on_new = mul(G.v[1], G.w[1])
report("Omega(on_new) = 1/2", Omega(on_new) == F(1, 2))
report("Omega != Omega_1/2: Omega(e_0 f_new) = 1 (Omega_1/2 vanishes there)", Omega(X) == 1)
report("Omega is not sigma_f-invariant (so the full group is needed, not 'exchange + a sign change moving e')", not inv_f)
# sigma_f alone (the claim's own case) exchanges on and off too:
sf_on = None
# on = v w with v = (e+f)/2; sigma_f: v -> (e-f)/2 = w
vf = sc(F(1, 2), add(G.e[1], sc(-1, G.f[1])))
report("sigma_f maps v to w, hence on to off (it DOES exchange on with off)", vf == G.w[1])

# ---------------------------------------------------------------- claim 4 (i): G2 odd conjugation, sign changes
G = Alg(3)
strings = list(product((0, 1), repeat=3))
def sproj(G, s):
    M = G.I
    for j, b in enumerate(s):
        M = mul(M, G.on[j] if b else G.off[j])
    return M
SP = {s: sproj(G, s) for s in strings}
g = gens(G)
e0 = G.e[0]
odd_flips_rest = all(mprod(e0, g[i], e0) == sc(-1, g[i]) for i in range(2, 6))
report("conjugation by the odd unitary e_0 negates every generator of the other rungs (an infinite sign change on the tower)", odd_flips_rest)
report("... and fixes every on_j, j != 0 (so no string value beyond rung 0 changes)", all(mprod(e0, G.on[j], e0) == G.on[j] for j in (1, 2)))
report("conjugation by e_j flips string value j", all(mprod(G.e[j], SP[s], G.e[j]) == SP[tuple(b ^ (i == j) for i, b in enumerate(s))] for j in range(3) for s in strings))

# rung permutations: the fermionic swap of rungs 0,1 as an automorphism defined on generators
# (e_0,f_0) <-> (e_1,f_1). Check it preserves the relations and the adjoint (images satisfy the same
# Clifford relations and the same adjoint rule), and permutes string values.
img = {0: G.e[1], 1: G.f[1], 2: G.e[0], 3: G.f[0], 4: G.e[2], 5: G.f[2]}
cliff = all(add(mul(img[i], img[j]), mul(img[j], img[i])) == (sc(2 * (1 if i % 2 == 0 else -1), G.I) if i == j else {})
            for i in range(6) for j in range(6))
adjok = all(dag(img[i]) == (img[i] if i % 2 == 0 else sc(-1, img[i])) for i in range(6))
report("the swap of two rungs is a dagger-commuting automorphism (relations and adjoint preserved)", cliff and adjok)

# ---------------------------------------------------------------- claim 4 (iii): four even atoms on two rungs
G = Alg(2)
P0 = mul(G.off[0], G.off[1])
v1v2 = mul(G.v[0], G.v[1])
ys = [mul(add(G.I, v1v2), P0), mul(add(G.I, sc(-1, v1v2)), P0), mul(add(G.v[0], G.v[1]), P0), mul(add(G.v[0], sc(-1, G.v[1])), P0)]
atoms = [sc(F(1, 2), mul(y, dag(y))) for y in ys]
ok = all(mul(A, A) == A and dag(A) == A and is_even_op(A, 2) and tr(A, 2) == F(1, 4) for A in atoms)
ok = ok and all(mul(atoms[i], atoms[j]) == {} for i in range(4) for j in range(4) if i != j) and add(*atoms) == G.I
report("claim 4 (iii): four even, orthogonal atoms of trace 1/4, sum 1 (own matrices)", ok)

# ---------------------------------------------------------------- claim 4 (iv): a rule built from VALUES of elements
# System rungs 0,1 (alternatives phi_0 = quantum on 0, phi_1 = on 1); data rungs 2..n+1, a string s.
# Rule: outcome 1 iff omega(Y) < omega(on_0), Y = sum_k 2^-k on_(1+k): both are values of elements of A in
# the joint state psi (x) s.
n = 4
G = Alg(2 + n)
Y = add(*[sc(F(1, 2 ** k), G.on[1 + k]) for k in range(1, n + 1)])
dirs = [(F(1), F(0)), (F(0), F(1)), (F(3, 5), F(4, 5)), (F(4, 5), F(3, 5)), (F(5, 13), F(12, 13)), (F(8, 17), F(15, 17)), (F(-3, 5), F(4, 5))]
freq = {}
nonconst = False
for a, b in dirs:
    wins = 0
    for s in product((0, 1), repeat=n):
        occ = [2 + k for k in range(n) if s[k]]
        psi = vadd(vsc(a, G.ket([0] + occ)), vsc(b, G.ket([1] + occ)))
        vY = ip(psi, apply(Y, psi))
        v0 = ip(psi, apply(G.on[0], psi))
        wins += 1 if vY < v0 else 0
    freq[(a, b)] = F(wins, 2 ** n)
for a, b in dirs:
    print(f"   psi = ({a}, {b}): Born weight {a*a}, frequency of outcome 1 over the 16 data strings {freq[(a, b)]}")
dep = len(set(freq.values())) > 1
close = all(abs(freq[(a, b)] - a * a) <= F(1, 2 ** n) for a, b in dirs)
report("a rule comparing VALUES of two elements of A (on_0 and Y) has state-dependent odds within 2^-n of Born", dep and close)
# for one fixed data string the outcome, as a function of psi, is two-valued and not constant (so it is no quadratic form)
s = (0, 1, 0, 1)
occ = [2 + k for k in range(n) if s[k]]
outs = []
for a, b in dirs:
    psi = vadd(vsc(a, G.ket([0] + occ)), vsc(b, G.ket([1] + occ)))
    outs.append(1 if ip(psi, apply(Y, psi)) < ip(psi, apply(G.on[0], psi)) else 0)
report(f"for fixed data the outcome is a non-constant 0/1 function of psi ({outs}), as (iv) forbids for a single value", len(set(outs)) == 2)

# exact limit: read-until-decided is the same comparison, read digit by digit (values of on_(1+k) against the
# binary digits of the value of on_0); probability exactly p, closed form over one period
p = F(9, 25)
digits, x = [], p
for _ in range(20):
    x *= 2
    d = int(x >= 1)
    digits.append(d)
    x -= d
period_ok = (x == p)
P_first = sum(F(d, 2 ** (k + 1)) for k, d in enumerate(digits)) / (1 - F(1, 2 ** 20))
order2 = next(k for k in range(1, 30) if pow(2, k, 25) == 1)
report(f"(v): 9/25 has binary period {order2} (order of 2 mod 25), probability of outcome 1 = {P_first}", period_ok and order2 == 20 and P_first == p)
# mean number of reads: sum_{k>=0} P(T > k) = sum 2^-k = 2; check truncation formula exactly for n = 20
E20 = sum(F(1, 2 ** k) for k in range(20))
report("(v): truncated mean sum_{k<20} 2^-k = 2 - 2^-19", E20 == 2 - F(1, 2 ** 19))

print("ALL PASS" if OK else "SOME FAIL")
