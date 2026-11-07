"""Referee G: an independent exact Fock-space route (not the tower/GA route of the checks).
Coefficients are numbers a + bJ in span{1, J}, J^2 = -1, stored as pairs of Fractions (J central).
States: dict  frozenset(occupied modes) -> number. Modes are hashable labels with a fixed total order."""
from fractions import Fraction as F

def nadd(x, y): return (x[0] + y[0], x[1] + y[1])
def nmul(x, y): return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def nconj(x): return (x[0], -x[1])
def nabs2(x): return x[0] * x[0] + x[1] * x[1]
ZERO, ONE = (F(0), F(0)), (F(1), F(0))
def num(a, b=0): return (F(a), F(b))

class Fock:
    def __init__(self, modes):
        self.modes = list(modes)
        self.idx = {m: i for i, m in enumerate(self.modes)}
    def _sign(self, occ, i):
        return -1 if sum(1 for j in occ if self.idx[j] < i) % 2 else 1
    def cdag(self, m, st):
        i = self.idx[m]; out = {}
        for occ, c in st.items():
            if m in occ: continue
            s = self._sign(occ, i)
            k = occ | {m}
            out[k] = nadd(out.get(k, ZERO), (c[0] * s, c[1] * s))
        return {k: v for k, v in out.items() if v != ZERO}
    def c(self, m, st):
        i = self.idx[m]; out = {}
        for occ, cc in st.items():
            if m not in occ: continue
            s = self._sign(occ, i)
            k = occ - {m}
            out[k] = nadd(out.get(k, ZERO), (cc[0] * s, cc[1] * s))
        return {k: v for k, v in out.items() if v != ZERO}

def sadd(*sts):
    out = {}
    for st in sts:
        for k, v in st.items():
            out[k] = nadd(out.get(k, ZERO), v)
    return {k: v for k, v in out.items() if v != ZERO}
def sscale(z, st): return {k: nmul(z, v) for k, v in st.items() if nmul(z, v) != ZERO}
def sneg(st): return sscale(num(-1), st)
def norm2(st): return sum(nabs2(v) for v in st.values())
def inner(a, b): # <a, b>, conjugate-linear in a
    s = ZERO
    for k, v in a.items():
        if k in b: s = nadd(s, nmul(nconj(v), b[k]))
    return s

class Bilinear:
    """Operator sum_t z_t c*_{x_t} c_{y_t}."""
    def __init__(self, fock, terms): self.f, self.terms = fock, [t for t in terms if t[0] != ZERO]
    def __call__(self, st):
        return sadd(*[sscale(z, self.f.cdag(x, self.f.c(y, st))) for z, x, y in self.terms]) if self.terms else {}
    def adj(self): return Bilinear(self.f, [(nconj(z), y, x) for z, x, y in self.terms])

def comm(A, B, st): return sadd(A(B(st)), sneg(B(A(st))))
