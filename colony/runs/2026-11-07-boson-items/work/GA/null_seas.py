"""GA exploration: densities of null seas in higher dimension (window along the generator x transverse torus),
closed tori, and the kernel reflection (orientation of J). Exact arithmetic with lib/GA.py."""
import sys, itertools
sys.path.insert(0, '/home/claude/phys-graph/colony/runs/2026-11-07-boson-items/work/GA')
from tower_currents import Tower, chk, F, GA, mul, add, sub, neg, scal, sc, gen, eq
import tower_currents as tc

print("\nG. null seas: modes (k, t), k in 1..L along the generator, t in Z_T transverse momentum")
L, T = 4, 2
Tw = Tower(L * T, kernel=False)
idx = lambda k, t: (t % T) * L + (k - 1)
def rho(q, p):
    out = {}
    for k in range(1, L + 1):
        if 1 <= k + q <= L:
            for t in range(T): out = add(out, Tw.bil(idx(k, t), idx(k + q, t + p)))
    return out
def rhs(q, p, q2, p2):
    out = {}
    for k in range(1, L + 1):
        if 1 <= k + q <= L and 1 <= k + q + q2 <= L:
            for t in range(T): out = add(out, Tw.bil(idx(k, t), idx(k + q + q2, t + p + p2)))
    for l in range(1, L + 1):
        if 1 <= l + q2 <= L and 1 <= l + q2 + q <= L:
            for t in range(T): out = sub(out, Tw.bil(idx(l, t), idx(l + q + q2, t + p + p2)))
    return out
ok = all(eq(Tw.comm(rho(q, p), rho(q2, p2)), rhs(q, p, q2, p2))
         for q in range(-2, 3) for q2 in range(-2, 3) for p in range(T) for p2 in range(T))
chk(f"[rho_(q,p), rho_(q',p')] = difference of two window sums (edge operators), L={L}, T={T}", ok)
# graph seas: transverse line t filled up to h_t, with q <= h_t <= L - q
for hs in [(2, 2), (1, 3), (3, 1), (2, 3)]:
    qmax = min(min(h, L - h) for h in hs)
    occ = [0] * (L * T)
    for t in range(T):
        for k in range(1, hs[t] + 1): occ[idx(k, t)] = 1
    P = Tw.proj(occ)
    res = []
    for q in range(1, qmax + 1):
        for p in range(T):
            for p2 in range(T):
                X = Tw.comm(rho(q, p), rho(-q, p2))
                val = q * T if (p + p2) % T == 0 else 0
                res.append(eq(Tw.m(X, P), scal(val, P)))
            for q2 in range(-qmax, qmax + 1):
                if q2 != -q:
                    for p2 in range(T):
                        res.append(eq(Tw.m(Tw.comm(rho(q, p), rho(q2, p2)), P), {}))
    chk(f"  graph sea h_t = {hs}: [rho_(q,p), rho_(-q,p')] P = q T delta_(p+p') P; other commutators kill P (q <= {qmax})", all(res))

print("G2. closed torus (both directions periodic): densities commute exactly")
Lc = 3
Tc = Tower(Lc * T, kernel=False)
ic = lambda k, t: (t % T) * Lc + (k % Lc)
def rhoc(q, p):
    out = {}
    for k in range(Lc):
        for t in range(T): out = add(out, Tc.bil(ic(k, t), ic(k + q, t + p)))
    return out
chk("  [rho_q, rho_q'] = 0 for every q, q' on Z_3 x Z_2", all(GA.is_zero(Tc.comm(rhoc(q, p), rhoc(q2, p2)))
    for q in range(Lc) for q2 in range(Lc) for p in range(T) for p2 in range(T)))

print("\nK. kernel reflection kappa: g2 -> -g2 on a two-mode block (lower 0, upper 1)")
B = Tower(2)
def kappa(x):
    return {b: (-c if 1 in b else c) for b, c in x.items()}
S = B.bil(0, 1); Sd = B.dag(S)
phi = add(S, Sd)
pis = {s: scal(s, B.m(B.J, sub(Sd, S))) for s in (1, -1)}
cen = sub(B.num(0), B.num(1))
for s in (1, -1):
    chk(f"  sigma={s}: [phi, pi_sigma] = sigma 2 J (n_low - n_up)", eq(B.comm(phi, pis[s]), scal(2 * s, B.m(B.J, cen))))
chk("  kappa fixes every transport generator, kappa(J) = -J, kappa(pi_+) = pi_-",
    all(eq(kappa(gen(i)), gen(i)) for i in range(2, 6)) and eq(kappa(B.J), neg(B.J)) and eq(kappa(pis[1]), pis[-1]))
# flows Ad exp(sigma J H t) with H = n_up - n_low (rational angle): u_sigma = prod (1 + (z^{+-} - 1) n)
z = add(sc(F(3, 5)), scal(F(4, 5), B.J)); zb = B.dag(z)
def Uflow(s):
    zu, zl = (z, zb) if s == 1 else (zb, z)
    return B.m(add(sc(1), B.m(sub(zu, sc(1)), B.num(1))), add(sc(1), B.m(sub(zl, sc(1)), B.num(0))))
chk("  kappa(U_+) = U_-  (kappa maps the sigma flow to the -sigma flow)", eq(kappa(Uflow(1)), Uflow(-1)))
P = B.proj([1, 0])
chk("  the ground state of H (lower filled) is J-free and kappa-invariant", eq(kappa(P), P) and all(1 not in b for b in P))
# S annihilates the lower-filled state for both sigma: S P = 0; S^dag P != 0
chk("  S P = 0 and S^dag P != 0: the boson vacuum is the same J-free state for both orientations",
    GA.is_zero(B.m(S, P)) and not GA.is_zero(B.m(Sd, P)))
# omega(J X) = 0 for every transport X in a J-free state: the orientation is invisible to transport observables
vals = [B.omega(P, B.m(B.J, B.m(*[gen(i) for i in bl]) if bl else sc(1))) for r in range(5) for bl in itertools.combinations(range(2, 6), r)]
chk("  omega(J X) = 0 for every transport blade X (state J-free)", all(v == 0 for v in vals))
print("\nALL:", tc.OK)
