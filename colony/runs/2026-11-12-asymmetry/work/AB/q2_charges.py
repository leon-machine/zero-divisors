"""Q2: which abelian charges of the sixteen survive which stored terms. Exact (Fractions)."""
import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as F
from itertools import combinations
import GA

N = 5
STATES = [frozenset(c) for r in range(N + 1) for c in combinations(range(1, N + 1), r)]
EVEN = [S for S in STATES if len(S) % 2 == 0]
IDX = {S: i for i, S in enumerate(EVEN)}
NAMES = {(0, 0): "nu^c", (0, 2): "u^c", (1, 1): "Q", (1, 3): "L", (2, 0): "e^c", (2, 2): "d^c"}
SPECIES = ["Q", "u^c", "d^c", "L", "e^c", "nu^c"]

def jk(S): return len(S & {4, 5}), len(S & {1, 2, 3})
def sp(S): return NAMES[jk(S)]

def op1(kind, i, st):
    out = {}
    for S, a in st.items():
        if kind == "v" and i not in S: T = S | {i}
        elif kind == "w" and i in S: T = S - {i}
        else: continue
        sign = -1 if sum(1 for j in S if j < i) % 2 else 1
        out[T] = out.get(T, 0) + sign * a
    return out

def word(ops, st):
    for kind, i in reversed(ops):
        st = op1(kind, i, st)
    return {k: v for k, v in st.items() if v != 0}

def chi(S): return -(-1) ** len(S & {4, 5})
def bml(S): return 1 - F(2, 3) * jk(S)[1]
def nB(S): return (bml(S) + chi(S)) / 4
def nL(S): return (chi(S) - 3 * bml(S)) / 4
def Y(S): return F(len(S & {4, 5}) - 1, 2) + bml(S) / 2
def t3(S): return F((4 in S) - (5 in S), 2)
def lam(S): return (1 in S) - (2 in S)

# 1. commutant of su(3)+su(2)_L+u(1)_Y on the sixteen
def weight(S): return (lam(S), (2 in S) - (3 in S), t3(S), Y(S))
pairs = [(S, T) for S in EVEN for T in EVEN if weight(S) == weight(T)]
print("matrix units commuting with the SM Cartan:", len(pairs))
roots = [[("v", a), ("w", b)] for a in (1, 2, 3) for b in (1, 2, 3) if a != b] + [[("v", 4), ("w", 5)], [("v", 5), ("w", 4)]]
rows = []
for E in roots:
    Emat = {S: word(E, {S: F(1)}) for S in EVEN}
    # [M, E] = 0, M = sum m_(S,T) |S><T|
    for A in EVEN:
        for Bst in EVEN:
            row = [F(0)] * len(pairs)
            nz = False
            for c, (S, T) in enumerate(pairs):
                # (M E)_{A,B} = sum_T M_{A,T} E_{T,B};  (E M)_{A,B} = sum_S E_{A,S} M_{S,B}
                v = 0
                if S == A: v += Emat[Bst].get(T, 0)
                if T == Bst: v -= Emat[S].get(A, 0)
                if v: row[c] = F(v); nz = True
            if nz: rows.append(row)
ker = GA.field_kernel(rows)
print("dim commutant of SM algebra on the sixteen:", len(ker))
diag_only = all(all(v == 0 or pairs[c][0] == pairs[c][1] for c, v in enumerate(k)) for k in ker)
print("commutant diagonal in occupation basis:", diag_only)

# charges: x over 6 species, plus h (charge of the slot creators v_4,v_5; slot annihilators carry -h)
def Bform(S, T):
    if T != frozenset(range(1, 6)) - S: return 0
    lst = sorted(S) + sorted(T)
    inv = sum(1 for i in range(5) for j in range(i + 1, 5) if lst[i] > lst[j])
    return (-1) ** (len(S) * (len(S) - 1) // 2) * (-1) ** inv

def constraint_rows_dirac(two_doublets=False):
    rows = set()
    for kind in ("v", "w"):
        for i in (4, 5):
            for T in EVEN:
                img = word([(kind, i)], {T: F(1)})
                for U, c in img.items():
                    for S in EVEN:
                        if Bform(S, U) * c != 0:
                            r = [0] * 8
                            r[SPECIES.index(sp(S))] += 1
                            r[SPECIES.index(sp(T))] += 1
                            if kind == "v": r[6] += 1
                            else: r[7] += 1
                            rows.add(tuple(r))
    rows = [list(r) for r in rows]
    if not two_doublets:
        rows.append([0, 0, 0, 0, 0, 0, 1, 1])  # h_v + h_w = 0
    return rows

def majorana_rows():
    T5 = [("v", i) for i in (1, 2, 3, 4, 5)]
    rows = set()
    for T in EVEN:
        img = word(T5, {T: F(1)})
        for U, c in img.items():
            for S in EVEN:
                if Bform(S, U) * c != 0:
                    r = [0] * 8
                    r[SPECIES.index(sp(S))] += 1; r[SPECIES.index(sp(T))] += 1
                    rows.add(tuple(r))
    return [list(r) for r in rows]

def anomaly_rows():
    a2 = [0] * 8; a3 = [0] * 8
    for S in EVEN:
        a2[SPECIES.index(sp(S))] += 4 * t3(S) ** 2
        a3[SPECIES.index(sp(S))] += lam(S) ** 2
    return [a2], [a3]

def mixing_rows():
    """charge x is carried consistently by a slot-pair root vector E iff x(T)-x(S) is the same on every
    transition S->T of E; rows: differences of transition charges."""
    rows = []
    for a in (1, 2, 3):
        for i in (4, 5):
            for E in ([("v", a), ("v", i)], [("v", a), ("w", i)], [("w", a), ("v", i)], [("w", a), ("w", i)]):
                trans = []
                for S in EVEN:
                    for T in word(E, {S: F(1)}):
                        r = [0] * 8
                        r[SPECIES.index(sp(T))] += 1; r[SPECIES.index(sp(S))] -= 1
                        trans.append(r)
                for r in trans[1:]:
                    rows.append([x - y for x, y in zip(r, trans[0])])
    return rows

def vec(fn, h):
    d = {}
    for S in EVEN: d[sp(S)] = fn(S)
    return [F(d[s]) for s in SPECIES] + [F(h), F(-h)]

named = {"Y": vec(Y, F(1, 2)), "n_B": vec(nB, 0), "n_L": vec(nL, 0), "B-L": vec(bml, 0), "chi": vec(chi, 0),
         "one": vec(lambda S: 1, 0)}

def kern(rows):
    rows = [[F(x) for x in r] for r in rows]
    return GA.field_kernel(rows)

def inspan(v, basis):
    if not basis: return all(x == 0 for x in v)
    return GA.field_rank(basis + [v]) == GA.field_rank(basis)

D = constraint_rows_dirac()
M = majorana_rows()
A2, A3 = anomaly_rows()
X = mixing_rows()
print("Dirac rows:", sorted(set(map(tuple, D))))
print("Majorana rows:", M)
print("A2 row:", A2, " A3 row:", A3)
cases = {"Dirac": D, "Dirac+Majorana": D + M, "Dirac+A2": D + A2, "Dirac+A2+A3": D + A2 + A3,
         "Dirac+mixing": D + X, "Dirac+Majorana+A2": D + M + A2, "all": D + M + A2 + A3 + X,
         "Dirac(2 doublets)": constraint_rows_dirac(True), "Dirac(2 doublets)+A3": constraint_rows_dirac(True) + A3}
for name, rows in cases.items():
    K = kern(rows)
    print(f"{name}: dim {len(K)}; contains:", [n for n, v in named.items() if inspan(v, K)])
for n, v in named.items():
    a2 = sum(x * y for x, y in zip(A2[0], v)); a3 = sum(x * y for x, y in zip(A3[0], v))
    tr = sum(F(fn(S)) for S in EVEN for fn in [dict(Y=Y, n_B=nB, n_L=nL, chi=chi, one=lambda S: 1).get(n, bml)])
    print(n, "A2 =", a2, "A3 =", a3, "trace on sixteen =", tr)
