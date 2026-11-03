"""standard-model.family-no-go-vev-cannot-separate: exact checks.

The five-mode module as 32 x 32 rational matrices with the invariant pairing B (the same construction as
families.doublet-direction-module-georgi-jarlskog-clebsch, rebuilt here because that claim is not a premise),
species named by Hypothesis (S); Y_x(psi, phi) = B(psi, x phi) on the sixteen.
(1) One-family Clebsches. For each of the four rung mode vectors w_4, w_5 (Y = -1/2) and v_4, v_5 (Y = +1/2),
    and for the doublet combinations a w_4 + b w_5, a v_4 + b v_5 at sample rational (a, b), the form is
    symmetric, couples only (L, e^c), (Q, d^c) (Y = -1/2) or (L, nu^c), (Q, u^c) (Y = +1/2), and the set of
    entry magnitudes on the lepton pair equals that on the quark pair, {|a|, |b|} with |a|, |b| read off the
    coefficients: |y_e| = |y_d| and |y_nu| = |y_u|.
(2) Family factor. For a non-symmetric invertible rational F and every signed entry pair (y_e, y_d) of the
    10 form, the characteristic polynomials of y_e F and y_d F agree coefficientwise up to the signs (-1)^k
    (roots negated), and M M^T has the same characteristic polynomial (equal singular spectra). Control: the
    126 entries (y_e, y_d) = (-1, +-1/3) of T_GJ = w_4 (B - L) chi give different spectra, so the test
    discriminates. Up-type: the same with x = v_4.
EXPORTS["module"] passes the module construction on (no premise call inside it).
"""
from fractions import Fraction as F

import GA
from pyutil import get_or_set
import fock
from tp_premise import premise

# sample rung-plane coefficients and a generic family matrix (inputs, not asserted values)
SAMPLES = [(F(1), F(0)), (F(0), F(1)), (F(2), F(-3)), (F(5, 7), F(1, 2))]
FAM = [[F(2), F(1, 3), F(-1)], [F(0), F(5, 7), F(4)], [F(-1), F(3), F(1, 2)]]

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


mm, madd, msc, msub = fock.mm, fock.madd, fock.msc, fock.msub
comm, acomm, meq = fock.comm, fock.acomm, fock.meq
tr = fock.transpose   # the transpose (fock.trace is the trace); kept for EXPORTS["module"]


def create(m):
    return fock.cre(m, NM)


def diag(fn):
    return fock.diag(fn, DIM)


ONE = fock.eye(DIM)
V = [fock.cre(m, NM) for m in range(NM)]
W = [fock.ann(m, NM) for m in range(NM)]
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
EMAT = []
for _m in range(NM):
    EMAT += [madd(V[_m], W[_m]), msub(W[_m], V[_m])]


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


EXPORTS = {"module": {k: v for k, v in globals().items() if not k.startswith("_") and k not in ("GA", "fock", "F", "premise")}}


def charpoly3(M):
    """(trace, sum of principal 2-minors, det) of a 3 x 3 matrix: det(t - M) = t^3 - c1 t^2 + c2 t - c3."""
    t = M[0][0] + M[1][1] + M[2][2]
    m2 = sum(M[i][i] * M[j][j] - M[i][j] * M[j][i] for i, j in ((0, 1), (0, 2), (1, 2)))
    d = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
         - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
         + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    return (t, m2, d)


def m3(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def t3(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]


def s3(c, A):
    return [[c * x for x in row] for row in A]


def magnitudes(f, pair):
    return {abs(x) for (s, t), x in f.items() if tuple(sorted((species(s), species(t)))) == pair}


def check_one_family_clebsches_equal():
    premise("standard-model.yukawa-pattern-two-rung-module")
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    for x, y, lep, qrk in ((W[3], W[4], ("L", "ec"), ("Q", "dc")), (V[3], V[4], ("L", "nuc"), ("Q", "uc"))):
        sign = -1 if x is W[3] else 1
        for a, b in SAMPLES:
            X = madd(msc(a, x), msc(b, y))
            f = form(X)
            cl = clebsch(f)
            ok = ok and op_weight(HYP, X) == F(sign, 2)
            ok = ok and meq(f, ftr(f)) and set(cl) == {lep, qrk}
            want = {abs(a), abs(b)} - {0}
            ok = ok and magnitudes(f, lep) == want == magnitudes(f, qrk)
    GA.check("every rung vector of either hypercharge: symmetric form, |y_e| = |y_d| and |y_nu| = |y_u|", ok)
    return ok


def check_family_factor_keeps_spectra():
    premise("standard-model.yukawa-pattern-two-rung-module")
    premise("standard-model.hyp-s-slot-statistics")
    ok = FAM != t3(FAM) and charpoly3(FAM)[2] != 0
    for x, lep, qrk in ((W[3], ("L", "ec"), ("Q", "dc")), (V[3], ("L", "nuc"), ("Q", "uc"))):
        cl = clebsch(form(x))
        for ye in cl[lep]:
            for yd in cl[qrk]:
                ce, cd = charpoly3(s3(ye, FAM)), charpoly3(s3(yd, FAM))
                sgn = 1 if ye == yd else -1
                ok = ok and all(ce[k] == sgn ** (k + 1) * cd[k] for k in range(3))
                Me, Md = s3(ye, FAM), s3(yd, FAM)
                ok = ok and charpoly3(m3(Me, t3(Me))) == charpoly3(m3(Md, t3(Md)))
    # control: the 126 entries separate the spectra
    cg = clebsch(form(mm(W[3], BL, CHI)))
    ok = ok and cg[("L", "ec")] == {F(-1)} and cg[("Q", "dc")] == {F(1, 3), F(-1, 3)}
    Me, Md = s3(F(-1), FAM), s3(F(1, 3), FAM)
    ok = ok and charpoly3(m3(Me, t3(Me))) != charpoly3(m3(Md, t3(Md)))
    GA.check("M_e = y_e F and M_d = y_d F: same spectra in magnitude for the 10, for any F; 126 control differs", ok)
    return ok
