"""families.imported-grade-three-direction-between-families: exact checks of the module part.

Computable part: the first sentence (grade three, couplings, moduli ratio 3, the family-diagonal statement).
The fits of the Standard-Model paper (the tuning of one part in 50 to several thousand, the registered route)
stand at record level and are not recomputed; standard-model.fits-record-level is therefore not touched.
The five-mode module, the invariant pairing B and GA's Cl(5,5) model of the ten (e_{2m} = v_m + w_m,
e_{2m+1} = w_m - v_m) are rebuilt here as in families.doublet-direction-module-georgi-jarlskog-clebsch.
(1) w_4 (B - L) and v_4 (B - L) are pure grade three (the 120 by the grade dictionary, applied, not recomputed);
    their forms couple exactly (L, e^c), (Q, d^c), respectively (L, nu^c), (Q, u^c), antisymmetrically, with one
    entry magnitude per pair and lepton : quark = 3.
(2) Tensored with a sample antisymmetric family matrix, the form is symmetric, zero on the family diagonal and
    nonzero on every off-diagonal family block; a symmetric family matrix gives a non-symmetric form (control).
"""
from fractions import Fraction as F

import GA
from pyutil import get_or_set
import fock
from tp_premise import premise

FAM_A = [[F(0), F(3), F(-1, 2)], [F(-3), F(0), F(4, 5)], [F(1, 2), F(-4, 5), F(0)]]
FAM_S = [[F(2), F(3), F(-1, 2)], [F(3), F(0), F(4, 5)], [F(-1, 2), F(4, 5), F(1)]]

# ---------------------------------------------------------------------------
# module construction (generic; nothing here is asserted)
# ---------------------------------------------------------------------------
NM = 5
DIM = 32
PAIRS = (0, 1, 2)
SLOTS = (3, 4)
SPECIES = {(0, 0): "nuc", (2, 0): "uc", (1, 1): "Q", (3, 1): "L", (0, 2): "ec", (2, 2): "dc"}  # (N_W, N_R)


def nw(s):
    return sum(1 for m in PAIRS if s >> m & 1)


def nr(s):
    return sum(1 for m in SLOTS if s >> m & 1)


def ntot(s):
    return nw(s) + nr(s)


def species(s):
    return SPECIES.get((nw(s), nr(s)))


def create(m):
    return fock.cre(m, NM)


def diag(fn):
    return fock.diag(fn, DIM)


# sparse exact operators from lib/fock.py (LSB order; comm and acomm are not halved); tr is the TRANSPOSE
tr = fock.transpose
mm, madd, msc, msub = fock.mm, fock.madd, fock.msc, fock.msub
comm, acomm, meq = fock.comm, fock.acomm, fock.meq


ONE = fock.eye(DIM)
V = [create(m) for m in range(NM)]
W = [tr(v) for v in V]
NUM = [fock.num(m, NM) for m in range(NM)]
SIXTEEN = [s for s in range(DIM) if ntot(s) % 2 == 0]


def complement(s):
    return (DIM - 1) ^ s


def eps_sign(s):
    seq = [m for m in range(NM) if s >> m & 1] + [m for m in range(NM) if not s >> m & 1]
    return (-1) ** sum(1 for i in range(NM) for j in range(i + 1, NM) if seq[i] > seq[j])


def bcoef(s):
    k = bin(s).count("1")
    return F((-1) ** (k * (k - 1) // 2) * eps_sign(s))


def form(T):
    """Y_T(e_s, e_t) = B(e_s, T e_t) for s, t in the sixteen."""
    out = {}
    for s in SIXTEEN:
        for t in SIXTEEN:
            x = T.get((complement(s), t))
            if x:
                out[(s, t)] = bcoef(s) * x
    return out


def ftr(f):
    return {(t, s): x for (s, t), x in f.items()}


def fadd(*fs):
    return madd(*fs)


def sym(f):
    return msc(F(1, 2), madd(f, ftr(f)))


def clebsch(f):
    out = {}
    for (s, t), x in f.items():
        get_or_set(out, tuple(sorted((species(s), species(t)))), set()).add(x)
    return out


def op_weight(H, X):
    """c with [H, X] = c X, or None."""
    Y = comm(H, X)
    k = next(iter(X))
    c = Y.get(k, 0) / X[k]
    return c if meq(Y, msc(c, X)) else None


BL = diag(lambda s: 1 - F(2, 3) * nw(s))
CHI = diag(lambda s: -(-1) ** nr(s))
NW = diag(nw)
HYP = diag(lambda s: F(nr(s), 2) - F(nw(s), 3))
T3 = msc(F(1, 2), msub(NUM[3], NUM[4]))
SU3 = [mm(V[a], W[b]) for a in PAIRS for b in PAIRS if a != b] + [msub(NUM[0], NUM[1]), msub(NUM[1], NUM[2])]

# Clifford algebra of the ten in GA, signature (+,-) per mode
SQ = tuple([1, -1] * NM)
EMAT = [fock.majorana(p, NM) for p in range(2 * NM)]  # a_m^dag + a_m, a_m - a_m^dag


def gv(m):
    return {(2 * m,): F(1, 2), (2 * m + 1,): F(-1, 2)}


def gw(m):
    return {(2 * m,): F(1, 2), (2 * m + 1,): F(1, 2)}


def gmul(*xs):
    out = xs[0]
    for y in xs[1:]:
        out = GA.mul(out, y, SQ)
    return out


def gwedge2(a, b):
    return GA.scal(F(1, 2), GA.sub(gmul(a, b), gmul(b, a)))


def gnum(m):
    return gmul(gv(m), gw(m))


def grades(x):
    return sorted({len(b) for b in x})


def gpart(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def to_mat(x):
    out = {}
    for b, c in x.items():
        M = ONE
        for i in b:
            M = mm(M, EMAT[i])
        out = madd(out, msc(c, M))
    return out


def ga_BL():
    return GA.add(GA.sc(1), GA.scal(F(-2, 3), GA.add(*[gnum(i) for i in PAIRS])))


def ga_chi():
    return GA.neg(gmul(GA.sub(GA.sc(1), GA.scal(2, gnum(3))), GA.sub(GA.sc(1), GA.scal(2, gnum(4)))))


def ga_TGJ():
    return gmul(gw(3), ga_BL(), ga_chi())


def T_GJ():
    return mm(W[3], BL, CHI)


def T_GJ_up():
    return mm(V[3], BL, CHI)


def kernel(vecs):
    """Exact rank and kernel of a list of sparse vectors: returns (rank, [coefficient dicts c with sum c_i vecs_i = 0])."""
    piv, ker = [], []
    for i, v in enumerate(vecs):
        v = {k: x for k, x in v.items() if x}
        c = {i: F(1)}
        for key, pv, pc in piv:
            x = v.get(key)
            if x:
                v = madd(v, msc(-x, pv))
                c = madd(c, msc(-x, pc))
        if v:
            key = next(iter(v))
            x = v[key]
            piv.append((key, msc(1 / x, v), msc(1 / x, c)))
        else:
            ker.append(c)
    return len(piv), ker


def rank(vecs):
    return kernel(vecs)[0]




def combined(f, A):
    return {((s, i), (t, j)): x * A[i][j] for (s, t), x in f.items() for i in range(3) for j in range(3) if A[i][j]}


def check_grade_three_couplings_ratio_three():
    premise("families.imported-decomposition-grade-dictionary")
    premise("standard-model.grade-three-georgi-jarlskog-direction")
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    for gx, X, lep, qrk in ((gw(3), W[3], ("L", "ec"), ("Q", "dc")), (gv(3), V[3], ("L", "nuc"), ("Q", "uc"))):
        t = gmul(gx, ga_BL())
        ok = ok and grades(t) == [3] and meq(to_mat(t), mm(X, BL))
        f = form(mm(X, BL))
        cl = clebsch(f)
        ok = ok and f != {} and meq(f, msc(-1, ftr(f))) and set(cl) == {lep, qrk}
        ml, mq = {abs(x) for x in cl[lep]}, {abs(x) for x in cl[qrk]}
        ok = ok and len(ml) == 1 and len(mq) == 1 and ml.pop() / mq.pop() == 3
    GA.check("one-sided weightings: grade three, couplings exactly as stated, lepton:quark modulus 3", ok)
    return ok


def check_antisymmetric_family_coupling_between_families():
    premise("standard-model.grade-three-georgi-jarlskog-direction")
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    for X in (W[3], V[3]):
        f = form(mm(X, BL))
        Y = combined(f, FAM_A)
        ok = ok and all(Y.get((b, a)) == x for (a, b), x in Y.items())
        blocks = {(a[1], b[1]) for (a, b) in Y}
        ok = ok and len(blocks) == 6 and all(i != j for i, j in blocks)
        Z = combined(f, FAM_S)
        ok = ok and any(Z.get((b, a)) != x for (a, b), x in Z.items())
    GA.check("antisymmetric family coupling: symmetric combined form, only between different families", ok)
    return ok
