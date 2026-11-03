"""families.doublet-direction-module-georgi-jarlskog-clebsch: exact checks.

The five-mode module Lambda(C^5) as 32 x 32 rational matrices (Jordan-Wigner, occupation basis; code modes
0, 1, 2 are the pair modes, 3, 4 the text's rung modes 4, 5), and in parallel the Clifford algebra of the ten
as GA's Cl(5,5): e_{2m} = v_m + w_m (square +1), e_{2m+1} = w_m - v_m (square -1), so v_m = (e_{2m} - e_{2m+1})/2
and w_m = (e_{2m} + e_{2m+1})/2. Grades are read off GA blades; the matrix image of every GA element used is
compared with the Jordan-Wigner operator built directly. B is the invariant pairing B(e_S, e_T) =
(-1)^(|S|(|S|-1)/2) eps(S, S^c) [T = S^c]; Y_T(psi, phi) = B(psi, T phi) on the sixteen (the even states).
(i) B - L = 1 - (2/3) N_W equals -(2/3) sum v_i ^ w_i (pure grade 2); w_4 chi = w_4 (1 - 2 n_5) = -2 w_4 (v_5 ^ w_5);
    T_GJ = w_4 (B - L) chi is pure grade 5 (no grade 1 or 3) and equals 4/3 of the grade-5 part of
    w_4 (v_5 ^ w_5) sum v_i ^ w_i. Of the two duality halves (1 +- omega)/2 T_GJ of the grade-5 element, both
    nonzero, one acts as zero on the sixteen (the 126bar half; that grade 5 on the sixteen is 126 + 126bar and
    that the surviving half is the 126 is the imported grade dictionary, not recomputed).
(ii) Species from (S): Y_{T_GJ} is symmetric, conserves hypercharge entry by entry ([Y, T_GJ] = -T_GJ/2),
    is nonzero exactly on (L, e^c) with entries {-1} and (Q, d^c) with entries {+1/3, -1/3}; Y_{w_4} has entries
    +-1 on the same pairs; |y_e / y_d| = 3 = |(B - L)(L) / (B - L)(Q)|.
(iii) Y_{w_4 (B - L)} is nonzero and antisymmetric, with (B - L)(L) + (B - L)(e^c) = 0 = (B - L)(Q) + (B - L)(d^c).
(iv) Y_{v_4 (B - L) chi} is symmetric, {+1} on (L, nu^c), {+1/3, -1/3} on (Q, u^c), and the sign on (Q, u^c)
    changes with the colour of the pair.
EXPORTS["module"] gives the construction to the claims that build on T_GJ.
"""
from fractions import Fraction as F

import GA
from pyutil import get_or_set
import fock
from tp_premise import premise

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


EXPORTS = {"module": {k: v for k, v in globals().items() if not k.startswith("_") and k not in ("GA", "F", "premise", "fock")}}


# ---------------------------------------------------------------------------
# checks
# ---------------------------------------------------------------------------

def check_t_gj_pure_grade_five():
    premise("families.imported-decomposition-grade-dictionary")
    pairbiv = GA.add(*[gwedge2(gv(i), gw(i)) for i in PAIRS])
    bl = ga_BL()
    ok = GA.eq(bl, GA.scal(F(-2, 3), pairbiv)) and grades(bl) == [2]
    # the GA model is the module: generators and B - L, chi agree with the Jordan-Wigner operators
    ok = ok and all(meq(to_mat(gv(m)), V[m]) and meq(to_mat(gw(m)), W[m]) for m in range(NM))
    ok = ok and meq(to_mat(bl), BL) and meq(to_mat(ga_chi()), CHI)
    # chi is +1 on the doublet sector N_R = 1, -1 on N_R = 0, 2
    ok = ok and all(CHI[(s, s)] == (1 if nr(s) == 1 else -1) for s in range(DIM))
    area5 = gwedge2(gv(4), gw(4))
    w4chi = gmul(gw(3), ga_chi())
    ok = ok and GA.eq(w4chi, gmul(gw(3), GA.sub(GA.sc(1), GA.scal(2, gnum(4)))))
    ok = ok and GA.eq(w4chi, GA.scal(-2, gmul(gw(3), area5)))
    t = ga_TGJ()
    ok = ok and grades(t) == [5] and gpart(t, 1) == {} and gpart(t, 3) == {}
    ok = ok and GA.eq(t, GA.scal(F(4, 3), gpart(gmul(gw(3), area5, pairbiv), 5)))
    ok = ok and meq(to_mat(t), T_GJ())
    # duality halves: omega^2 = 1, omega constant on the sixteen; the half that kills the sixteen
    omega = {tuple(range(2 * NM)): F(1)}
    ok = ok and GA.eq(gmul(omega, omega), GA.sc(1))
    om = to_mat(omega)
    cvals = {om.get((s, s)) for s in SIXTEEN}
    ok = ok and len(cvals) == 1 and all(k[0] == k[1] for k in om)
    c = cvals.pop()
    plus = GA.scal(F(1, 2), GA.add(t, gmul(omega, t)))
    minus = GA.scal(F(1, 2), GA.sub(t, gmul(omega, t)))
    killer = plus if c == 1 else minus
    survivor = minus if c == 1 else plus
    on16 = lambda M: {k: x for k, x in M.items() if k[1] in SIXTEEN}
    ok = ok and plus != {} and minus != {} and grades(plus) == [5] and grades(minus) == [5]
    ok = ok and on16(to_mat(killer)) == {} and meq(on16(to_mat(survivor)), on16(T_GJ()))
    GA.check("T_GJ = w4 (B-L) chi is pure grade 5 = 4/3 w4^(v5^w5)^sum v_i^w_i; the 126bar half kills the 16", ok)
    return ok


def check_georgi_jarlskog_entries():
    premise("standard-model.hyp-s-slot-statistics")
    T = T_GJ()
    f = form(T)
    cl = clebsch(f)
    ok = meq(f, ftr(f))
    ok = ok and set(cl) == {("L", "ec"), ("Q", "dc")}
    ok = ok and cl[("L", "ec")] == {F(-1)} and cl[("Q", "dc")] == {F(1, 3), F(-1, 3)}
    # hypercharge: T_GJ has charge -1/2 and every entry conserves it
    ok = ok and op_weight(HYP, T) == F(-1, 2)
    ok = ok and all(HYP.get((s, s), 0) + HYP.get((t, t), 0) == F(1, 2) for (s, t) in f)
    c10 = clebsch(form(W[3]))
    ok = ok and set(c10) == {("L", "ec"), ("Q", "dc")} and c10[("L", "ec")] | c10[("Q", "dc")] == {F(1), F(-1)}
    ye = {abs(x) for x in cl[("L", "ec")]}
    yd = {abs(x) for x in cl[("Q", "dc")]}
    bl = {species(s): BL[(s, s)] for s in SIXTEEN}
    ok = ok and len(ye) == 1 and len(yd) == 1 and ye.pop() / yd.pop() == 3 == abs(bl["L"] / bl["Q"])
    GA.check("Y_TGJ symmetric, -1 on (L,e^c), +-1/3 on (Q,d^c), conserves Y; ratio 3 = (B-L)(L)/(B-L)(Q)", ok)
    return ok


def check_one_sided_weighting_antisymmetric():
    premise("standard-model.hyp-s-slot-statistics")
    f = form(mm(W[3], BL))
    ok = f != {} and meq(f, msc(-1, ftr(f))) and sym(f) == {}
    bl = {species(s): BL[(s, s)] for s in SIXTEEN}
    ok = ok and bl["L"] + bl["ec"] == 0 and bl["Q"] + bl["dc"] == 0
    ok = ok and bl["L"] == -1 and bl["Q"] == F(1, 3)
    # with chi the same weighting is symmetric: chi is what makes it so
    g = form(T_GJ())
    ok = ok and meq(g, ftr(g)) and g != {}
    GA.check("w4 (B-L) without chi: nonzero antisymmetric form; Yukawa pairs are B-L neutral", ok)
    return ok


def check_up_type_twin():
    premise("standard-model.hyp-s-slot-statistics")
    T = T_GJ_up()
    f = form(T)
    cl = clebsch(f)
    ok = meq(f, ftr(f)) and set(cl) == {("L", "nuc"), ("Q", "uc")}
    ok = ok and cl[("L", "nuc")] == {F(1)} and cl[("Q", "uc")] == {F(1, 3), F(-1, 3)}
    ok = ok and op_weight(HYP, T) == F(1, 2)
    # the sign on (Q, u^c) depends on colour: group the entries by the colour mode missing from the u^c state
    bycol = {}
    for (s, t), x in f.items():
        u = s if species(s) == "uc" else t
        if species(u) == "uc":
            empty = [m for m in PAIRS if not u >> m & 1]
            get_or_set(bycol, empty[0], set()).add(x)
    ok = ok and len(bycol) == 3 and all(len(v) == 1 for v in bycol.values())
    ok = ok and len({next(iter(v)) for v in bycol.values()}) == 2
    GA.check("v4 (B-L) chi: symmetric, +1 on (L,nu^c), +-1/3 on (Q,u^c) by colour: |m_nu^D| = 3 |m_u|", ok)
    return ok
