"""Referee's own helpers (independent of the authors' check.py helpers).

Two independent routes:
  (G) lib/GA.py blades, generators ordered e_0..e_{n-1}, f_0..f_{n-1} (squares +1 then -1);
  (M) an explicit real matrix representation of Cl_Q(n,n) (Jordan-Wigner), sparse, over Fractions,
      in which the adjoint of (P) is the matrix transpose.
"""
import sys
from fractions import Fraction as F
from itertools import combinations, product
sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA

# ---------------- route (G) ----------------
def S(n):
    return tuple([1] * n + [-1] * n)

def E(j, n):
    return {(j,): F(1)}

def Fg(j, n):
    return {(n + j,): F(1)}

def V(j, n):
    return GA.scal(F(1, 2), GA.add(E(j, n), Fg(j, n)))

def W(j, n):
    return GA.scal(F(1, 2), GA.sub(E(j, n), Fg(j, n)))

def adj(x, n):
    """(P) adjoint: reverse, times (-1) per f generator."""
    out = {}
    for b, c in x.items():
        g = len(b)
        s = (-1) ** (g * (g - 1) // 2) * (-1) ** sum(1 for i in b if i >= n)
        out[b] = c * s
    return out

def M(*xs, n):
    out = {(): F(1)}
    for x in xs:
        out = GA.mul(out, x, S(n))
    return out

def scalar(x):
    return x.get((), F(0))

def blades_of(gens):
    return [tuple(c) for r in range(len(gens) + 1) for c in combinations(sorted(gens), r)]

def apply_vector_map(img, blade, n):
    """Image of a blade under the algebra automorphism determined by generator images img[i]."""
    out = {(): F(1)}
    for i in blade:
        out = GA.mul(out, img.get(i, {(i,): F(1)}), S(n))
    return out

def rank(rows):
    rows = [list(r) for r in rows if any(r)]
    if not rows:
        return 0
    ncol = len(rows[0])
    rk = 0
    for c in range(ncol):
        piv = None
        for i in range(rk, len(rows)):
            if rows[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        pr = rows[rk]
        for i in range(len(rows)):
            if i != rk and rows[i][c] != 0:
                q = rows[i][c] / pr[c]
                rows[i] = [a - q * b for a, b in zip(rows[i], pr)]
        rk += 1
        if rk == len(rows):
            break
    return rk

def is_psd(G):
    """Exact PSD test by symmetric elimination with diagonal pivoting (largest diagonal first)."""
    G = [list(r) for r in G]
    n = len(G)
    for i in range(n):
        for j in range(n):
            if G[i][j] != G[j][i]:
                raise ValueError("not symmetric")
    alive = list(range(n))
    while alive:
        k = max(alive, key=lambda i: G[i][i])
        d = G[k][k]
        if d < 0:
            return False
        if d == 0:
            # all remaining diagonals are 0: then all remaining entries must be 0
            return all(G[i][j] == 0 for i in alive for j in alive)
        alive.remove(k)
        for i in alive:
            if G[i][k] != 0:
                q = G[i][k] / d
                for j in alive:
                    G[i][j] -= q * G[k][j]
    return True

# ---------------- route (M): sparse matrices ----------------
class SM(object):
    """Sparse square matrix over Fractions: dict (row, col) -> value."""
    def __init__(self, d, dim):
        self.d = {k: v for k, v in d.items() if v != 0}
        self.dim = dim
    @staticmethod
    def eye(dim):
        return SM({(i, i): F(1) for i in range(dim)}, dim)
    def __add__(self, o):
        d = dict(self.d)
        for k, v in o.d.items():
            d[k] = d.get(k, F(0)) + v
        return SM(d, self.dim)
    def __sub__(self, o):
        return self + o.sc(-1)
    def sc(self, c):
        return SM({k: F(c) * v for k, v in self.d.items()}, self.dim)
    def __mul__(self, o):
        rows = {}
        for (i, j), v in o.d.items():
            rows.setdefault(i, []).append((j, v))
        d = {}
        for (i, k), a in self.d.items():
            for j, b in rows.get(k, []):
                d[(i, j)] = d.get((i, j), F(0)) + a * b
        return SM(d, self.dim)
    def T(self):
        return SM({(j, i): v for (i, j), v in self.d.items()}, self.dim)
    def tr(self):
        return sum((v for (i, j), v in self.d.items() if i == j), F(0))
    def __eq__(self, o):
        return (self - o).d == {}
    def apply(self, vec):
        out = {}
        for (i, j), v in self.d.items():
            if j in vec:
                out[i] = out.get(i, F(0)) + v * vec[j]
        return {k: v for k, v in out.items() if v != 0}

def jw(n):
    """Real JW representation of Cl(n,n) on (Q^2)^{(x)n}; basis index bit j = occupation-type label of rung j.
    e_j = Z..Z X I..I, f_j = Z..Z (iY) I..I with iY = [[0,1],[-1,0]]; transpose is the (P) adjoint."""
    dim = 2 ** n
    es, fs = [], []
    for j in range(n):
        de, df = {}, {}
        for col in range(dim):
            bits = [(col >> (n - 1 - k)) & 1 for k in range(n)]
            sgn = (-1) ** sum(bits[:j])
            row = col ^ (1 << (n - 1 - j))
            de[(row, col)] = F(sgn)
            # iY: |0> -> -|1>, |1> -> +|0>  (columns: iY e0 = (0,-1)^T, iY e1 = (1,0)^T)
            df[(row, col)] = F(sgn) * (F(-1) if bits[j] == 0 else F(1))
        es.append(SM(de, dim))
        fs.append(SM(df, dim))
    return es, fs
