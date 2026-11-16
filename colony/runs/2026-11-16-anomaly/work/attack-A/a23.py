"""A2/A3 scratch: equilibrium coefficient as a Gram ratio; B - L weights of the stored terms; mass forms."""
import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
from itertools import combinations
import GA

MODES = (1, 2, 3, 4, 5); PAIR, SLOT = (1, 2, 3), (4, 5)
STATES = [frozenset(c) for r in range(6) for c in combinations(MODES, r)]
EVEN = [S for S in STATES if len(S) % 2 == 0]
def jk(S): return len(S & set(SLOT)), len(S & set(PAIR))
def bml(S): return 1 - F(2, 3)*jk(S)[1]
def chi(S): return -(-1)**jk(S)[0]
def n_b(S): return (bml(S)+chi(S))/4
def n_l(S): return (chi(S)-3*bml(S))/4
def hyp(S): return F(jk(S)[0]-1, 2)+bml(S)/2
def t3(S): return F((4 in S)-(5 in S), 2)
def qem(S): return t3(S)+hyp(S)
def lam(S): return (1 in S)-(2 in S)
def lam2(S): return (2 in S)-(3 in S)
NAMES = {(0, 0): "nu^c", (0, 2): "u^c", (1, 1): "Q", (1, 3): "L", (2, 0): "e^c", (2, 2): "d^c"}
def word(ops, st):
    for kind, i in reversed(ops):
        out = {}
        for S, a in st.items():
            if kind == "v" and i not in S: T = S | {i}
            elif kind == "w" and i in S: T = S - {i}
            else: continue
            sign = -1 if sum(1 for j in S if j < i) % 2 else 1
            out[T] = out.get(T, 0)+sign*a
        st = out
    return {k: v for k, v in st.items() if v != 0}

for S in EVEN:
    print(sorted(S), NAMES[jk(S)], 'Y', hyp(S), 'T3', t3(S), 'Q', qem(S), 'B-L', bml(S), 'nB', n_b(S), 'nL', n_l(S))

PLASMA = [S for S in EVEN if jk(S) != (0, 0)]      # the fifteen: nu^c not in the plasma
def chiF(X, Xp, states=PLASMA): return sum(F(X(S))*F(Xp(S)) for S in states)

# ---- symmetric phase: Gram ratio with neutral charges T3, Y
def gram_ratio_sym(nf, nh):
    # charges as (function on states, doublet charge h, W charge)
    Y = (hyp, F(1, 2), 0); T3 = (t3, None, 1); BL = (bml, 0, 0); B = (n_b, 0, 0)
    def form(a, b):
        f = nf*chiF(a[0], b[0])
        # doublet: two components with (T3, Y) = (+-1/2, 1/2); boson weight 2
        def dq(c, comp):  # charge of doublet component
            if c is T3: return F(comp, 2)
            return c[1]
        f += 2*nh*sum(dq(a, s)*dq(b, s) for s in (1, -1))
        # W bosons: one complex field of T3 = 1, two helicities, boson weight 2
        f += 2*2*a[2]*b[2]
        return f
    V = [T3, Y, BL]
    # mu = BL + a*T3 + b*Y with form(T3, mu) = form(Y, mu) = 0
    M = [[form(T3, T3), form(T3, Y)], [form(Y, T3), form(Y, Y)]]
    rhs = [-form(T3, BL), -form(Y, BL)]
    detM = M[0][0]*M[1][1]-M[0][1]*M[1][0]
    a = (rhs[0]*M[1][1]-M[0][1]*rhs[1])/detM; b = (M[0][0]*rhs[1]-M[1][0]*rhs[0])/detM
    nB = form(B, BL)+a*form(B, T3)+b*form(B, Y)
    nBL = form(BL, BL)+a*form(BL, T3)+b*form(BL, Y)
    return nB/nBL, a, b, form(Y, Y), form(T3, T3), form(Y, BL), form(BL, BL), form(B, BL), form(B, Y)
def gram_ratio_broken(nf, nh):
    def form(a, b, qa, qb):
        f = nf*chiF(a, b)
        f += 2*(2+nh)*qa*qb      # W (two helicities) and nh charged scalars, each of charge 1, boson weight 2
        return f
    QQ = form(qem, qem, 1, 1); QBL = form(qem, bml, 1, 0); BLBL = form(bml, bml, 0, 0)
    BBL = form(n_b, bml, 0, 0); BQ = form(n_b, qem, 0, 1)
    return (BBL*QQ-BQ*QBL)/(BLBL*QQ-QBL*QBL), QQ
print(gram_ratio_sym(3, 1)); print(gram_ratio_sym(3, 2)); print(gram_ratio_broken(3, 1), gram_ratio_broken(3, 2))
ok = all(gram_ratio_sym(nf, nh)[0] == F(8*nf+4*nh, 22*nf+13*nh) for nf in range(1, 7) for nh in range(0, 7))
okb = all(gram_ratio_broken(nf, nh)[0] == F(8*nf+4*(nh+2), 24*nf+13*(nh+2)) for nf in range(1, 7) for nh in range(0, 7))
print('sym formula on grid', ok, ' broken formula on grid', okb)

# ---- the conserved space at state level, broken phase.
# unknowns: x_S for the 16 even states, h4v,h4w (neutral slot ops), h5v,h5w (charged slot ops), hW
def pairing(S, U):
    if U != frozenset(MODES)-S: return 0
    lst = sorted(S)+sorted(U)
    inv = sum(1 for a in range(5) for b in range(a+1, 5) if lst[a] > lst[b])
    return (-1)**(len(S)*(len(S)-1)//2)*(-1)**inv
IDX = {S: i for i, S in enumerate(EVEN)}
NV = 16+5
def rows_state_level(broken, with_sph=True, with_nu_c=True):
    rows = []
    # colour root vectors carry nothing
    for a in PAIR:
        for b in PAIR:
            if a != b:
                for S in EVEN:
                    for T in word([("v", a), ("w", b)], {S: F(1)}):
                        r = [0]*NV; r[IDX[T]] += 1; r[IDX[S]] -= 1; rows.append(r)
    # W: v4 w5 carries hW (index 20)
    for S in EVEN:
        for T in word([("v", 4), ("w", 5)], {S: F(1)}):
            r = [0]*NV; r[IDX[T]] += 1; r[IDX[S]] -= 1; r[20] -= 1; rows.append(r)
    # Dirac terms: x_S + x_T + h_a = 0
    for kind, i, col in (("v", 4, 16), ("w", 4, 17), ("v", 5, 18), ("w", 5, 19)):
        for T in EVEN:
            for U, c in word([(kind, i)], {T: F(1)}).items():
                for S in EVEN:
                    if pairing(S, U)*c != 0:
                        r = [0]*NV; r[IDX[S]] += 1; r[IDX[T]] += 1; r[col] += 1; rows.append(r)
    # one doublet and its conjugate: h(w_i) = -h(v_i); and the doublet is a weak doublet: h(v4) - h(v5) = +-hW
    rows.append([0]*16+[1, 1, 0, 0, 0]); rows.append([0]*16+[0, 0, 1, 1, 0])
    if broken:
        rows.append([0]*16+[0, 0, 1, 0, 0])       # neutral component condensed: h(v5) = 0
    if with_sph:
        r = [0]*NV
        for S in EVEN:
            if jk(S)[0] == 1: r[IDX[S]] += 1
        rows.append(r)
    return rows
def vecs(fn, h4, h5, hW): return [F(fn(S)) for S in EVEN]+[F(h4), -F(h4), F(h5), -F(h5), F(hW)]
for broken in (False, True):
    for sph in (False, True):
        ker = GA.field_kernel([[F(x) for x in r] for r in rows_state_level(broken, sph)])
        print('broken' if broken else 'symmetric', 'sphaleron' if sph else 'no sphaleron', 'dim conserved space', len(ker))
        for name, v in (('Y', vecs(hyp, F(1, 2), F(1, 2), 0)), ('T3', vecs(t3, F(1, 2), F(-1, 2), 1)), ('Q', vecs(qem, 1, 0, 1)),
                        ('B-L', vecs(bml, 0, 0, 0)), ('nB', vecs(n_b, 0, 0, 0)), ('nL', vecs(n_l, 0, 0, 0))):
            inside = GA.field_rank(ker+[v]) == GA.field_rank(ker)
            print('   ', name, 'in space:', inside)
