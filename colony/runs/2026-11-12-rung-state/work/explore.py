import sys, types, itertools, time
sys.path.insert(0, '/home/claude/phys-graph/lib')
sys.path.insert(0, '/home/claude/phys-graph/store/claims/synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight')
m = types.ModuleType("tp_premise"); m.premise = lambda i: None; sys.modules["tp_premise"] = m
from check import *
import GA

# ---- C1: integer states on one rung
S = sq(1)
B = blades(range(2))          # 1, e, f, ef
E, Fv = e(0), f(0); p = mul(Fv, E, S)
found = []
for a in (-1, 0, 1):
    for c in (-1, 0, 1):
        for b in (-1, 0, 1):
            vals = {(): F(1), (0,): F(a), (1,): F(c), (0, 1): F(-b)}     # omega(ef) = -omega(fe) = -b
            Om = lambda x, vals=vals: sum(cc * vals[k] for k, cc in x.items())
            if satisfies_p(Om, 1, S):
                on = mul(v(0), w(0), S)
                found.append((a, c, b, Om(on), Om(v(0)), Om(w(0))))
print("ladder-integer (P)-states (a=om(e), c=om(f), b=om(p), om(on), om(v), om(w)):")
for r in found: print("  ", r)
sw = [r for r in found if all(x.denominator == 1 for x in r[3:])]
print("of these, integer on the switch monomials:", [(r[0], r[1], r[2]) for r in sw])

# ---- C2: centre of the even subalgebra, l = 2
S2 = sq(2)
evenB = [b for b in blades(range(4)) if len(next(iter(b))) % 2 == 0]
biv = [mul(gen(a), gen(b), S2) for a, b in itertools.combinations(range(4), 2)]
# solve for even x commuting with all bivectors: linear system
keys = [next(iter(b)) for b in evenB]
rows = []
for Bv in biv:
    for i, b in enumerate(evenB):
        pass
import fractions
def comm(x, y): return sub(mul(x, y, S2), mul(y, x, S2))
# matrix of the map x -> (comm(x, B))_B
cols = []
allkeys = [next(iter(b)) for b in blades(range(4))]
for b in evenB:
    col = []
    for Bv in biv:
        cm = comm(b, Bv)
        col += [cm.get(k, F(0)) for k in allkeys]
    cols.append(col)
# rank
M = [list(r) for r in zip(*cols)]
def rank(M):
    M = [r[:] for r in M]; rk = 0; ncol = len(M[0])
    for c in range(ncol):
        piv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                fct = M[i][c] / M[rk][c]
                M[i] = [x - fct * y for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk
print("even subalgebra dim", len(evenB), "centre dim", len(evenB) - rank(M))

# ---- C3: rotor taking a string to weights 9/25, 16/25 (two rungs, one particle)
n1 = mul(v(0), w(0), S2); n2 = mul(v(1), w(1), S2)
P10 = mul(n1, sub(sc(1), n2), S2); P01 = mul(sub(sc(1), n1), n2, S2)
Pi1 = add(P10, P01)
h = sub(mul(v(0), w(1), S2), mul(v(1), w(0), S2))
print("h^2 == -Pi1:", mul(h, h, S2) == scal(-1, Pi1), " h dagger == -h:", dagger(h) == scal(-1, h))
c, s = F(3, 5), F(4, 5)
R = add(sub(sc(1), Pi1), scal(c, Pi1), scal(s, h))
print("R R^dag = 1:", mul(R, dagger(R), S2) == sc(1), " R even:", all(len(k) % 2 == 0 for k in R))
print("R reverse:", mul(R, GA.reverse(R), S2) == sc(1))
om = state(P10, S2)
om2 = lambda x: om(mul(mul(dagger(R), x, S2), R, S2))
print("weights after R on P10, P01:", om2(P10), om2(P01))
om3 = lambda x: om(mul(mul(R, x, S2), dagger(R), S2))
print("other convention:", om3(P10), om3(P01))
