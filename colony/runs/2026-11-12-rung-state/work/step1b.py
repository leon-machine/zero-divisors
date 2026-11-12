import sys, random, itertools
sys.path.insert(0, '.'); sys.path.insert(0, '/home/claude/phys-graph/lib')
from fock import *
from step1 import model, interference
import GA
random.seed(7)
al, be = F(3, 5), F(4, 5)

# --- tie the module to GA.py: n = 2, e_j = v_j + w_j, f_j = v_j - w_j
def basis(n):
    return [tuple(sorted(S)) for r in range(n + 1) for S in itertools.combinations(range(n), r)]
def gen_el(i):          # GA generator index i: e_j at 2j, f_j at 2j+1
    j = i // 2
    return eadd(V(j), W(j)) if i % 2 == 0 else eadd(V(j), escal(-1, W(j)))
def blade_el(b):
    el = ONE
    for i in b: el = emul(el, gen_el(i))
    return el
n = 2; sq = (1, -1, 1, -1)
blades = [tuple(c) for r in range(5) for c in itertools.combinations(range(4), r)]
ok = True
for b1 in blades:
    for b2 in blades:
        prod = GA.mul({b1: F(1)}, {b2: F(1)}, sq)          # GA product, a multiple of one blade
        lhs_el = emul(blade_el(b1), blade_el(b2))
        for S in basis(n):
            x = {S: F(1)}
            lhs = ap(lhs_el, x)
            rhs = vadd(*[vscal(c, ap(blade_el(b), x)) for b, c in prod.items()]) if prod else {}
            ok = ok and lhs == rhs
# faithfulness: the 16 blades act as linearly independent operators (matrix of 16 x 16 entries, rank 16)
rows = []
for b in blades:
    row = []
    for S in basis(n):
        img = ap(blade_el(b), {S: F(1)})
        row += [img.get(T, F(0)) for T in basis(n)]
    rows.append(row)
def rank(M):
    M = [r[:] for r in M]; rk = 0
    for c in range(len(M[0])):
        piv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                q = M[i][c] / M[rk][c]; M[i] = [x - q * y for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk
print("module agrees with GA.py products on Cl(2,2):", ok, " rank of the 16 blades:", rank(rows))
# adjoint: <x, a y> = <a^dag x, y>
okd = True
for b in blades:
    a = blade_el(b)
    for S in basis(n):
        for T in basis(n):
            okd = okd and ip({S: F(1)}, ap(a, {T: F(1)})) == ip(ap(edag(a), {S: F(1)}), {T: F(1)})
print("dagger is the Fock adjoint:", okd)

# --- the model built by hand equals the unitaries applied to the initial vector (N = 2)
def U_el(j, c, s):
    a, b = 2 + 2 * j, 3 + 2 * j
    P10 = emul(ON(a), OFF(b)); P01 = emul(OFF(a), ON(b)); Pi = eadd(P10, P01)
    h = eadd(emul(V(a), W(b)), escal(-1, emul(V(b), W(a))))
    R = eadd(ONE, escal(-1, Pi), escal(c, Pi), escal(s, h))
    return eadd(OFF(0), emul(ON(0), R)), R, h, Pi
for (c, s) in ((F(3, 5), F(4, 5)), (F(0), F(1))):
    N = 2
    vac = {(): F(1)}
    psi = vadd(vscal(al, ap_v(0, vac)), vscal(be, ap_v(1, vac)))
    for j in range(N): psi = ap_v(2 + 2 * j, psi)
    # note the order: build Psi0 = (al v0 + be v1) v2 v4 |vac> with v2, v4 applied first
    psi0 = {(): F(1)}
    for j in reversed(range(N)): psi0 = ap_v(2 + 2 * j, psi0)
    psi0 = vadd(vscal(al, ap_v(0, psi0)), vscal(be, ap_v(1, psi0)))
    out = psi0
    for j in range(N):
        U, R, h, Pi = U_el(j, c, s)
        out = ap(U, out)
    A, B = model(N, c, s, set(range(N)))
    hand = vadd(vscal(al, A), vscal(be, B))
    # unitarity of U on the whole module
    allb = [tuple(sorted(S)) for r in range(7) for S in itertools.combinations(range(6), r)]
    U, R, h, Pi = U_el(0, c, s)
    uni = all(ap(emul(edag(U), U), {S: F(1)}) == {S: F(1)} for S in allb)
    print("c =", c, " hand-built == +-unitaries applied:", out == hand, out == vscal(-1, hand), " U unitary:", uni, " norm:", ip(out, out))
