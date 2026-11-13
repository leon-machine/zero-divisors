"""Claim 2 recomputed by the matrix route (and the centre by route G), plus two extensions:
 - a parity-ODD but homogeneous record coupling (not tested by the author),
 - the store's composite mode-wise descent (pinching onto the joint-number-diagonal algebra) and the
   corner read-out D(x) = PxP, applied to the author's record example."""
from myalg import *
half = F(1, 2)

# (i) one rung: states under (P) with integer values on 1, e, f, fe.  Matrix route: omega(x) = tr(rho x),
# rho a rational 2x2 matrix fixed by omega on the 4 blades; (P) <=> rho symmetric PSD, trace 1 (proved
# below for 2x2: Gram matrix omega(x y^T) = tr(rho x y^T) PSD for all x,y <=> rho PSD; reality <=> rho = rho^T).
es, fs = jw(1)
I2 = SM.eye(2)
e, f = es[0], fs[0]
blades1 = [I2, e, f, f * e]
def basis_mats(dim):
    return [SM({(i, j): F(1)}, dim) for i in range(dim) for j in range(dim)]
found = []
for a, c, b in product(range(-2, 3), repeat=3):
    vals = [F(1), F(a), F(c), F(b)]
    # solve rho from tr(rho B_k) = vals_k: rho = sum_k vals_k B_k^T / 2 (the B_k are orthogonal for tr(X Y^T))
    rho = SM({}, 2)
    for B, val in zip(blades1, vals):
        rho = rho + B.T().sc(val / 2)
    assert all((rho * B).tr() == val for B, val in zip(blades1, vals))
    Om = lambda X: (rho * X).tr()
    bm = basis_mats(2)
    G = [[Om(X * Y.T()) for Y in bm] for X in bm]
    real = all(Om(X.T()) == Om(X) for X in bm)
    if real and is_psd(G):
        vv = (e + f).sc(half)
        found.append((a, c, b, Om(vv * (e - f).sc(half)), Om(vv)))
print("(i) integer (a,c,b) in {-2..2}^3 passing (P):", [(r[0], r[1], r[2]) for r in found])
print("    weights on 'on':", sorted(r[3] for r in found))
print("    also integer on v (switch form):", [(r[0], r[2], r[3]) for r in found if r[3].denominator == 1 and r[4].denominator == 1])

# (ii) centre of the even subalgebra of Cl(n,n), n = 2, 3, 4 (route G, own linear algebra)
for n in (2, 3, 4):
    allb = blades_of(range(2 * n))
    evb = [b for b in allb if len(b) % 2 == 0]
    gensb = [(a, b) for a, b in combinations(range(2 * n), 2)]
    # rows: for each bivector B and each output blade, sum_x c_x [x,B]_blade = 0
    cols = []
    out_index = {b: i for i, b in enumerate(evb)}
    eqs = {}
    for xi, x in enumerate(evb):
        for B in gensb:
            com = GA.sub(GA.mul({x: F(1)}, {B: F(1)}, S(n)), GA.mul({B: F(1)}, {x: F(1)}, S(n)))
            for bb, c in com.items():
                eqs.setdefault((B, bb), {})[xi] = c
    rows = [[row.get(i, F(0)) for i in range(len(evb))] for row in eqs.values()]
    print(f"(ii) centre of even subalgebra of Cl({n},{n}): dim = {len(evb) - rank(rows)} (even dim {len(evb)})")

# (ii) the record example, 4 rungs, matrix route. Rungs 0,1 system (one quantum), 2,3 record.
n = 4
es, fs = jw(n)
dim = 2 ** n
I = SM.eye(dim)
v = [(es[j] + fs[j]).sc(half) for j in range(n)]
w = [(es[j] - fs[j]).sc(half) for j in range(n)]
on = [v[j] * w[j] for j in range(n)]
off = [w[j] * v[j] for j in range(n)]
P0 = I
for j in range(n):
    P0 = P0 * off[j]
y = (v[0].sc(F(3, 5)) + v[1].sc(F(4, 5))) * v[2] * P0
rho = y * y.T()
print("    rho idempotent, trace 1:", rho * rho == rho, rho.tr())
X = (I - (on[2] - on[3]) * (on[2] - on[3])) + v[2] * w[3] + v[3] * w[2]
U = off[0] + on[0] * X
print("    X^2 = 1, X sym:", X * X == I, X.T() == X, "; U orthogonal:", U * U.T() == I)
rho2 = U * rho * U.T()
st = lambda R, x: (R * x).tr() / R.tr()
Ra = off[2] * on[3]; Rb = on[2] * off[3]
print("    record weights (rung 3, rung 2):", st(rho2, Ra), st(rho2, Rb),
      "; correlations:", st(rho2, Ra * on[0]), st(rho2, Rb * on[1]))
Gam = I
for j in range(n):
    Gam = Gam * fs[j] * es[j]
print("    Gamma on both branches:", Gam * (Ra * rho2) == Ra * rho2, Gam * (Rb * rho2) == Rb * rho2,
      "(same sign:", (Gam * (Ra * rho2) == Ra * rho2) == (Gam * (Rb * rho2) == Rb * rho2), ")")
T = v[0] * w[1] * v[3] * w[2]
O = T + T.T()
blk = Ra * rho2 * Ra + Rb * rho2 * Rb
print("    interference observable value:", st(rho2, O), "; after removing interference:", st(blk, O))

# Extension 1: an ODD homogeneous record coupling U_odd = off_0 e_3 + on_0 e_2: unitary, odd, and it
# still leaves both branches in one sector (each branch's parity flips together).
Uo = off[0] * es[3] + on[0] * es[2]
y1 = (v[0].sc(F(3, 5)) + v[1].sc(F(4, 5))) * P0          # system only, records empty
r1 = y1 * y1.T()
r1b = Uo * r1 * Uo.T()
br_a = on[0] * r1b * on[0]; br_b = on[1] * r1b * on[1]
print("(ii+) odd coupling: orthogonal", Uo * Uo.T() == I,
      "; record weights", st(r1b, on[2] * off[3]), st(r1b, off[2] * on[3]),
      "; Gamma sign branch a / b:", 1 if Gam * br_a == br_a else -1, 1 if Gam * br_b == br_b else -1,
      "; initial sign:", 1 if Gam * r1 == r1 else -1)
T2 = v[0] * w[1] * v[2] * w[3]
O2 = T2 + T2.T()
print("      even observable sees interference after the odd coupling:", st(r1b, O2))

# (iii) rotor on two rungs: weights 9/25, 16/25 (matrix route, 2 rungs)
es2, fs2 = jw(2)
I4 = SM.eye(4)
v2 = [(es2[j] + fs2[j]).sc(half) for j in range(2)]
w2 = [(es2[j] - fs2[j]).sc(half) for j in range(2)]
n1, n2 = v2[0] * w2[0], v2[1] * w2[1]
P10 = n1 * (I4 - n2); P01 = (I4 - n1) * n2
Pi1 = P10 + P01
h = v2[0] * w2[1] - v2[1] * w2[0]
R = (I4 - Pi1) + Pi1.sc(F(3, 5)) + h.sc(F(4, 5))
print("(iii) R orthogonal:", R * R.T() == I4, "; weights from string (1,0):",
      [((R * P10 * R.T()) * Ps).tr() for Ps in (P10, P01)])

# Extension 2: the store's composite mode-wise descent  E_comp(x) = prod_j (x -> (x + p_j x p_j)/2),
# p_j = on_j - off_j, which is the pinching onto the joint-number-diagonal algebra, applied to the
# author's state after the record (rho2) and before it (rho).
p = [on[j] - off[j] for j in range(n)]
def Ecomp(x):
    for j in range(n):
        x = (x + p[j] * x * p[j]).sc(half)
    return x
print("(E1) composite descent: rho2 -> diagonal in strings:", Ecomp(rho2) == blk,
      "; O after descent:", st(Ecomp(rho2), O), "; record weights kept:", st(Ecomp(rho2), Ra), st(Ecomp(rho2), Rb))
H = v[0] * w[1] + v[1] * w[0]
print("     but applied BEFORE any record it also kills the system's own interference: <hop> before",
      st(rho, H), "after descent", st(Ecomp(rho), H))
# corner read-out D(x) = P x P with P = on_3 (record 'quantum on rung 3'), renormalised: Lueders conditioning
Pc = on[3]
cond = Pc * rho2 * Pc
print("     corner read-out on P = on_3: unnormalised weight", cond.tr(),
      "; conditional weight of system rung 0:", st(cond, on[0]), " (always this branch: the corner is fixed by P)")
