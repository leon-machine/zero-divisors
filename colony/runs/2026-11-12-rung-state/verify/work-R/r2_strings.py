"""Claim 1 (iii) by the matrix route, plus the finite-support lemma behind the infinite-tower remark."""
from myalg import *
m = 3
es, fs = jw(m)
dim = 2 ** m
I = SM.eye(dim)
half = F(1, 2)
v = [(es[j] + fs[j]).sc(half) for j in range(m)]
w = [(es[j] - fs[j]).sc(half) for j in range(m)]
on = [v[j] * w[j] for j in range(m)]
off = [w[j] * v[j] for j in range(m)]
strings = list(product((0, 1), repeat=m))
P = {}
for s in strings:
    x = I
    for j in range(m):
        x = x * (on[j] if s[j] else off[j])
    P[s] = x
ok = all(P[s] * P[s] == P[s] and P[s].T() == P[s] for s in strings)
ok &= all((P[s] * P[r]).d == {} for s in strings for r in strings if s != r)
tot = P[strings[0]]
for s in strings[1:]:
    tot = tot + P[s]
ok &= tot == I
ok &= all(P[s].tr() == 1 for s in strings)            # rank one each
print("8 rank-one orthogonal self-adjoint idempotents summing to 1:", ok)
# Volume element Gamma = prod f_j e_j : diagonal, sign (-1)^{|s|} times one overall sign
Gam = I
for j in range(m):
    Gam = Gam * fs[j] * es[j]
signs = {}
for s in strings:
    GP = Gam * P[s]
    signs[s] = 1 if GP == P[s] else (-1 if GP == P[s].sc(-1) else None)
print("Gamma P_s = sign * P_s:", signs)
print("sign = c * (-1)^|s| for one c:", len({signs[s] * (-1) ** sum(s) for s in strings}) == 1)
# Gamma commutes with all 15 bivectors (so with the even subalgebra, hence every rotor)
gens = es + fs
print("Gamma commutes with all bivectors:", all(Gam * (gens[a] * gens[b]) == (gens[a] * gens[b]) * Gam
                                             for a, b in combinations(range(2 * m), 2)))
# Rotor classes by brute force on a generating set of rotors: f_i f_j, e_i e_j, e_i f_j (i != j) and
# the rational rotations 3/5 + 4/5 e_i e_j etc. Orbit of P_000 among the string projectors.
rotors = []
for a, b in combinations(range(2 * m), 2):
    B = gens[a] * gens[b]
    for (c, s_) in ((F(0), F(1)), (F(3, 5), F(4, 5))):
        R = I.sc(c) + B.sc(s_)
        if R * R.T() == I:          # unitary for (P): these are the rotors we may use
            rotors.append(R)
reach = {(0, 0, 0)}
frontier = [(0, 0, 0)]
while frontier:
    s = frontier.pop()
    for R in rotors:
        img = R * P[s] * R.T()
        for r in strings:
            if img == P[r] and r not in reach:
                reach.add(r); frontier.append(r)
print(f"{len(rotors)} unitary rotors used; strings reached from 000 by conjugation:", sorted(reach))
# Finite-support lemma: every blade not involving rung j commutes with on_j and off_j, so no element of
# the algebra of the other rungs changes the value of rung j.
lem = True
for j in range(m):
    others = [k for k in range(2 * m) if k % m != j]
    for r in range(len(others) + 1):
        for c in combinations(others, r):
            x = I
            for g in c:
                x = x * gens[g]
            lem &= x * on[j] == on[j] * x
print("every element supported off rung j commutes with on_j (all j):", lem)
