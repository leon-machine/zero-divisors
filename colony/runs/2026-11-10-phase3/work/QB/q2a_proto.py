import sys, time, itertools
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
SQ = GA.sig(1, 3)
G = [GA.gen(i) for i in range(4)]
GUP = [GA.scal(SQ[i], G[i]) for i in range(4)]
BIV = [(i, j) for i in range(4) for j in range(i + 1, 4)]
def mul(x, y): return GA.mul(x, y, SQ)
def comm(x, y): return GA.scal(F(1, 2), GA.sub(mul(x, y), mul(y, x)))
def grade(x, k): return {b: c for b, c in x.items() if len(b) == k and c != 0}

def rep_matrix(J, blades):
    """matrix of M -> J x M on the span of the given blades: cols[j] = {i: coeff}"""
    cols = []
    for b in blades:
        im = comm(J, {b: F(1)})
        cols.append({blades.index(k): c for k, c in im.items() if c != 0})
    return cols

VB = [(i,) for i in range(4)]
GENS = [{(0, 1): F(1)}, {(1, 2): F(1)}, {(2, 3): F(1)}]

def tensor_generator_rows(J, slots):
    """rows of the derivation J acting on the tensor product of the slots (each slot a blade list): one row
    (dict index->coeff) per output basis element"""
    mats = [rep_matrix(J, s) for s in slots]
    dims = [len(s) for s in slots]
    rows = {}
    for idx in itertools.product(*[range(n) for n in dims]):
        col = flat(idx, dims)
        for k, m in enumerate(mats):
            for i, c in m[idx[k]].items():
                out = list(idx); out[k] = i
                r = flat(tuple(out), dims)
                rows.setdefault(r, {})
                rows[r][col] = rows[r].get(col, F(0)) + c
    return list(rows.values())

def flat(idx, dims):
    n = 0
    for i, d in zip(idx, dims):
        n = n * d + i
    return n

def rank(rows):
    piv = {}
    r = 0
    for row in rows:
        row = {k: v for k, v in row.items() if v != 0}
        while row:
            k = min(row)
            if k in piv:
                p = piv[k]
                f = row[k]
                for kk, vv in p.items():
                    nv = row.get(kk, F(0)) - f * vv
                    if nv == 0:
                        row.pop(kk, None)
                    else:
                        row[kk] = nv
            else:
                f = row[k]
                piv[k] = {kk: vv / f for kk, vv in row.items()}
                r += 1
                break
    return r

def invariants(slots, extra=()):
    rows = []
    for J in GENS:
        rows += tensor_generator_rows(J, slots)
    rows += list(extra)
    n = 1
    for s in slots: n *= len(s)
    return n - rank(rows)

t = time.time()
print('V3', invariants([VB, VB, VB]), 'V4', invariants([VB] * 4), time.time() - t)
print('L2 V V', invariants([BIV, VB, VB]), time.time() - t)
# End(L2) as L2 (value) x L2 (argument, reciprocal basis)
slots = [BIV, BIV, VB, VB]
dims = [6, 6, 4, 4]
def bsq(b): return SQ[b[0]] * SQ[b[1]]      # (e_i e_j)^2 = -sq_i sq_j ; <B_i B_i> = -sq sq
# tensor w = sum w[i,j] B_i (x) B^j  <-> M(B_j) = sum_i w[i,j] B_i ; reciprocal B^j = B_j / <B_j B_j>
# symmetric: <B_k M(B_j)> = <M(B_k) B_j>  -> w[k,j] n_k = w[j,k] n_j with n_k = <B_k B_k>
def nrm(b): return mul({b: F(1)}, {b: F(1)}).get((), F(0))
def sym_constraints():
    out = []
    for i in range(6):
        for j in range(i + 1, 6):
            for p in range(4):
                for q in range(4):
                    out.append({flat((i, j, p, q), dims): F(1), flat((j, i, p, q), dims): F(-1)})
    return out
def protraction_constraints():
    # T(b) = sum_a g^a ^ M(g_a ^ g_b), M(B_j) = sum_i w[i,j] B_i
    out = []
    for b in range(4):
        acc = {}   # trivector blade -> {(i,j): coeff}
        for a in range(4):
            if a == b: continue
            key = (a, b) if a < b else (b, a); s = 1 if a < b else -1
            j = BIV.index(key)
            for i in range(6):
                t = grade(mul(GUP[a], {BIV[i]: F(1)}), 3)
                for bl, c in t.items():
                    acc.setdefault(bl, {})
                    acc[bl][(i, j)] = acc[bl].get((i, j), F(0)) + s * c * nrm(BIV[j])
        for bl, d in acc.items():
            for p in range(4):
                for q in range(4):
                    out.append({flat((i, j, p, q), dims): c for (i, j), c in d.items()})
    return out
print('End', invariants(slots), time.time() - t)
print('Sym', invariants(slots, sym_constraints()), time.time() - t)
print('Prot', invariants(slots, protraction_constraints()), time.time() - t)
