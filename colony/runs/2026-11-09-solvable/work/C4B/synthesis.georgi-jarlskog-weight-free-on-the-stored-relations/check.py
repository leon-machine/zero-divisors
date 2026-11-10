"""synthesis.georgi-jarlskog-weight-free-on-the-stored-relations: exact checks.

Module part: the five-mode module Lambda(W + R_2) as 32 x 32 rational matrices (fock.py, LSB order), modes 0, 1, 2
the pairs, 3, 4 the rungs, as in the stored checks of the Majorana element's square; T = v_1 ... v_5; the pair part
of the square P_4 = (3/32)(B - L)(-1)^{N_P} (stored identity); mass forms B(psi, X phi) on the sixteen with the
stored pairing. Pati-Salam part: 3 x 3 rational family matrices with the imported Clebsch structure
M_u = v_u Y + w_u f + c_u h, M_nu = v_u Y - 3 w_u f + c_nu h, M_d = v_d Y + w_d f + c_d h,
M_e = v_d Y - 3 w_d f + c_e h, M_R = v_R f, m_nu = -M_nu M_R^{-1} M_nu^T; h_mu: w_d -> mu w_d.
"""
from fractions import Fraction as F
from itertools import combinations, permutations

import GA
import fock
from tp_premise import premise

NM = 5
STATES = [s for k in range(NM + 1) for s in combinations(range(NM), k)]
IDX = {s: sum(1 << x for x in s) for s in STATES}
STATE_OF = {i: s for s, i in IDX.items()}
D = len(STATES)
mm, madd, msc, tr, comm = fock.mm, fock.madd, fock.msc, fock.transpose, fock.comm
PAIRS = (0, 1, 2)
SIXTEEN = [s for s in STATES if len(s) % 2 == 0]


def nw(s):
    return sum(1 for x in s if x in PAIRS)


def nr(s):
    return sum(1 for x in s if x not in PAIRS)


def diag(fn):
    return fock.diag(lambda i: fn(STATE_OF[i]), D)


V = [fock.cre(k, NM) for k in range(NM)]
W = [tr(v) for v in V]
ONE = fock.eye(D)
BL = diag(lambda s: 1 - F(2, 3) * nw(s))
CHI = diag(lambda s: -(-1) ** nr(s))
PPAR = diag(lambda s: (-1) ** nw(s))
P4 = msc(F(3, 32), mm(BL, PPAR))
T = mm(mm(mm(mm(V[0], V[1]), V[2]), V[3]), V[4])
TD = tr(T)
W4, V4 = W[3], V[3]

BMAT = {}
for s in STATES:
    comp = tuple(x for x in range(NM) if x not in s)
    seq = list(s) + list(comp)
    inv = sum(1 for i in range(NM) for j in range(i + 1, NM) if seq[i] > seq[j])
    k = len(s)
    BMAT[(IDX[s], IDX[comp])] = F((-1) ** (k * (k - 1) // 2) * (-1) ** inv)


def forms(X):
    """symmetric and antisymmetric parts of B(psi, X phi) on the sixteen."""
    BX = mm(BMAT, X)
    sym, anti = {}, {}
    for a in SIXTEEN:
        for b in SIXTEEN:
            x, y = BX.get((IDX[a], IDX[b]), 0), BX.get((IDX[b], IDX[a]), 0)
            if x + y:
                sym[(a, b)] = (x + y) * F(1, 2)
            if x - y:
                anti[(a, b)] = (x - y) * F(1, 2)
    return sym, anti


def is_multiple(f, g):
    c = None
    for k in set(f) | set(g):
        a, b = f.get(k, F(0)), g.get(k, F(0))
        if b == 0:
            if a != 0:
                return None
            continue
        if c is None:
            c = a / b
        elif a != c * b:
            return None
    return c if c is not None else F(0)


S10, A10 = forms(W4)
SGJ, _ = forms(mm(mm(W4, BL), CHI))
LEP = [k for k in S10 if nw(k[0]) in (0, 3)]
QRK = [k for k in S10 if nw(k[0]) in (1, 2)]


def entries(sym):
    """(quark entry, lepton entry) of a symmetric rung form, relative to the 10 form's entries."""
    q = {sym.get(k, F(0)) / S10[k] for k in QRK}
    l = {sym.get(k, F(0)) / S10[k] for k in LEP}
    if len(q) != 1 or len(l) != 1 or set(sym) - set(S10):
        return None
    return q.pop(), l.pop()


def check_operator_functions_of_the_majorana_element_give_only_the_ten():
    """(i) T^2 = 0, (T^dag)^2 = 0, T T^dag T = T, T^dag T T^dag = T^dag, so 1, T, T^dag, T T^dag, T^dag T span the
    algebra they generate; with the down-type rung vector w_4 only 1 gives a mass form on the sixteen, the 10 form,
    so every operator function of T and T^dag gives w_4 a multiple of the 10, never the GJ form; with v_4 the one
    further form, from T^dag T, is half the 10's neutrino entry (plus an antisymmetric part), with no quark entry."""
    premise("standard-model.majorana-element")
    premise("standard-model.invariant-pairing-five-modes")
    premise("synthesis.georgi-jarlskog-square-of-majorana-element")
    TT, DT = mm(T, TD), mm(TD, T)
    GA.check("T^2 = 0", mm(T, T) == {})
    GA.check("Tdag^2 = 0", mm(TD, TD) == {})
    GA.check("T Tdag T = T", mm(TT, T) == T)
    GA.check("Tdag T Tdag = Tdag", mm(DT, TD) == TD)
    basis = [T, TD, TT, DT]
    prods = [mm(x, y) for x in basis for y in basis]
    span = [ONE, T, TD, TT, DT]
    GA.check("products stay in the span", all(p == {} or any(p == s or p == msc(F(-1), s) for s in span) for p in prods))
    GA.check("10 form nonzero, symmetric", S10 != {} and A10 == {})
    for E in basis:
        s, a = forms(mm(W4, E))
        GA.check("w_4 E: no mass form for E = T, Tdag, T Tdag, Tdag T", s == {} and a == {})
    for E in (T, TD, TT):
        s, a = forms(mm(V4, E))
        GA.check("v_4 E: no mass form for E = T, Tdag, T Tdag", s == {} and a == {})
    S10u, _ = forms(V4)
    s, a = forms(mm(V4, DT))
    nu = {k: v for k, v in S10u.items() if k[0] == () or k[1] == ()}
    GA.check("v_4 Tdag T: symmetric part half the 10's neutrino entry, no quark entry, an antisymmetric part",
             is_multiple(s, nu) == F(1, 2) and len(nu) == 2 and a != {})
    GA.check("the GJ form is not a multiple of the 10", is_multiple(SGJ, S10) is None)
    return True


WEIGHTS = ((F(1), F(0), F(1)), (F(0), F(1), F(-3)), (F(3), F(32), F(3)), (F(1), F(16), F(5)),
           (F(2), F(-5), F(49, 69)))


def check_weighting_of_the_pair_part_moves_the_lepton_quark_ratio():
    """(ii) w_4 (a + b P_4) gives the symmetric form with quark entries a - b/32 and lepton entries a + 3b/32 (relative
    to the 10's), no antisymmetric part, P_4 commuting with B - L and the rung parity (its Pati-Salam type is stored); the ratio is
    (32a + 3b)/(32a - b): 1 at b = 0, -3 at a = 0, +3 at b/a = 32/3; with (a, b) = (v_d Y_kk, -32 w_d f_kk) the
    entries are v_d Y + w_d f and v_d Y - 3 w_d f, the down-type and lepton entries of the imported Clebsch structure."""
    premise("synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square")
    premise("families.doublet-direction-module-georgi-jarlskog-clebsch")
    premise("standard-model.imported-clebsch-structure-seesaw")
    GA.check("P_4 commutes with B - L and the rung parity, not with the pair bracket",
             comm(P4, BL) == {} and comm(P4, CHI) == {} and comm(P4, mm(V[0], V[1])) != {})
    for a, b, ratio in WEIGHTS:
        s, an = forms(mm(W4, madd(msc(a, ONE), msc(b, P4))))
        e = entries(s)
        GA.check("no antisymmetric part", an == {})
        GA.check("quark a - b/32, lepton a + 3b/32", e == (a - b / 32, a + 3 * b / 32))
        GA.check("lepton/quark ratio (32a + 3b)/(32a - b)", e[1] / e[0] == ratio == (32 * a + 3 * b) / (32 * a - b))
    for vd, Ykk, wd, fkk, expect in ((F(1), F(-1), F(1, 3), F(1), (F(-2, 3), F(-2))),
                                     (F(1, 2), F(3), F(-2), F(1, 7), (F(17, 14), F(33, 14)))):
        s, _ = forms(mm(W4, madd(msc(vd * Ykk, ONE), msc(-32 * wd * fkk, P4))))
        GA.check("module coupling realises the Clebsch down and lepton entries",
                 entries(s) == (vd * Ykk + wd * fkk, vd * Ykk - 3 * wd * fkk) == expect)
    return True


def mat(rows):
    return [[F(x) for x in r] for r in rows]


def mmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(3)), F(0)) for j in range(3)] for i in range(3)]


def madd3(*args):
    out = [[F(0)] * 3 for _ in range(3)]
    for c, A in args:
        out = [[out[i][j] + c * A[i][j] for j in range(3)] for i in range(3)]
    return out


def tp3(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]


def inv3(A):
    a = A
    det = (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
           + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
    cof = [[(a[(j + 1) % 3][(i + 1) % 3] * a[(j + 2) % 3][(i + 2) % 3]
             - a[(j + 1) % 3][(i + 2) % 3] * a[(j + 2) % 3][(i + 1) % 3]) for j in range(3)] for i in range(3)]
    return [[cof[i][j] / det for j in range(3)] for i in range(3)]


def sym(A):
    return madd3((F(1, 2), A), (F(1, 2), tp3(A)))


E33 = mat([[0, 0, 0], [0, 0, 0], [0, 0, 1]])


def masses(d, mu):
    Y, f, h = d["Y"], d["f"], d["h"]
    vu, vd, wu, wd, vR = d["vu"], d["vd"], d["wu"], mu * d["wd"], d["vR"]
    cu, cn, cd, ce = d["c"]
    Mu = madd3((vu, Y), (wu, f), (cu, h))
    Mn = madd3((vu, Y), (-3 * wu, f), (cn, h))
    Md = madd3((vd, Y), (wd, f), (cd, h))
    Me = madd3((vd, Y), (-3 * wd, f), (ce, h))
    MR = madd3((vR, f))
    mnu = madd3((F(-1), mmul(mmul(Mn, inv3(MR)), tp3(Mn))))
    return Mu, Mn, Md, Me, MR, mnu


# diagonal model: v_u = v_d = w_u = 1, f = diag(1/10, 1, 1), M_u = diag(0, 0, 4), (EW) exact
DIAG = {"Y": mat([[F(-1, 10), 0, 0], [0, -1, 0], [0, 0, 3]]), "f": mat([[F(1, 10), 0, 0], [0, 1, 0], [0, 0, 1]]),
        "h": mat([[0] * 3] * 3), "vu": F(1), "vd": F(1), "wu": F(1), "wd": F(1, 3), "vR": F(1000),
        "c": (F(0), F(0), F(0), F(0))}
# general model: symmetric f with off-diagonal entries, a 120, M_u = diag(1/1000, 1/10, 4) in the (EW) basis
F_GEN = mat([[F(1, 10), F(1, 20), 0], [F(1, 20), 1, F(1, 5)], [0, F(1, 5), 1]])
H_GEN = mat([[0, F(1, 50), F(-1, 30)], [F(-1, 50), 0, F(1, 40)], [F(1, 30), F(-1, 40), 0]])
MU_GEN = mat([[F(1, 1000), 0, 0], [0, F(1, 10), 0], [0, 0, 4]])
GEN = {"Y": madd3((F(1), MU_GEN), (F(-1), F_GEN), (F(-1, 2), H_GEN)), "f": F_GEN, "h": H_GEN,
       "vu": F(1), "vd": F(1, 2), "wu": F(1), "wd": F(1, 4), "vR": F(5000), "c": (F(1, 2), F(-3, 2), F(2), F(-1))}
MUS = (F(1), F(3, 5), F(-2), F(7, 3))


def check_h_mu_fixes_every_stored_relation_and_moves_the_down_type_126():
    """(iii) Under h_mu (w_d -> mu w_d, mu nonzero): M_u, M_nu, M_R and m_nu are unchanged; Premise (EW)
    (M_u)_33 = m_t = 4 w_u f_33 and (M_nu)_33 = 0 holds; the Majorana scale (M_R)_33 = m_t v_R/(4 w_u) holds;
    f-hat = Sym(M_d - M_e)/(M_d - M_e)_33 = f/f_33 is unchanged (no 120), so is M_nu = M_u - m_t f-hat;
    Sym(M_d - M_e) = 4 mu w_d f and Sym(M_u - M_nu) = 4 w_u f; the antisymmetric parts are untouched; composing
    with (Y, v_u, v_d) -> (Y/k, k v_u, k v_d) fixes every Dirac matrix (electroweak normalisation)."""
    premise("standard-model.imported-clebsch-structure-seesaw")
    premise("synthesis.majorana-scale-is-126-doublet-vev")
    premise("standard-model.neutrino-dirac-matrix-charged-fermions")
    premise("synthesis.hypothesis-u-under-ew-is-a-charged-fermion-condition")
    premise("standard-model.imported-spinor-bilinears")
    for d in (DIAG, GEN):
        Mu0, Mn0, Md0, Me0, MR0, mn0 = masses(d, F(1))
        mt = Mu0[2][2]
        GA.check("Sym M_u diagonal in the (EW) basis", all(sym(Mu0)[i][j] == 0 for i in range(3) for j in range(3) if i != j))
        for mu in MUS:
            Mu, Mn, Md, Me, MR, mnu = masses(d, mu)
            GA.check("M_u, M_nu, M_R, m_nu unchanged", (Mu, Mn, MR, mnu) == (Mu0, Mn0, MR0, mn0))
            GA.check("(EW): (M_nu)_33 = 0 and m_t = 4 w_u f_33", Mn[2][2] == 0 and mt == 4 * d["wu"] * d["f"][2][2])
            GA.check("Majorana scale (M_R)_33 = m_t v_R/(4 w_u)", MR[2][2] == mt * d["vR"] / (4 * d["wu"]))
            GA.check("Sym(M_d - M_e) = 4 mu w_d f", sym(madd3((F(1), Md), (F(-1), Me))) == madd3((4 * mu * d["wd"], d["f"])))
            GA.check("Sym(M_u - M_nu) = 4 w_u f", sym(madd3((F(1), Mu), (F(-1), Mn))) == madd3((4 * d["wu"], d["f"])))
            GA.check("antisymmetric parts of M_d - M_e unchanged",
                     madd3((F(1), Md), (F(-1), Me), (F(-1), sym(madd3((F(1), Md), (F(-1), Me))))) ==
                     madd3((F(1), Md0), (F(-1), Me0), (F(-1), sym(madd3((F(1), Md0), (F(-1), Me0))))))
            if d is DIAG:
                dm = madd3((F(1), Md), (F(-1), Me))
                fhat = madd3((1 / dm[2][2], dm))
                GA.check("f-hat = f/f_33 unchanged", fhat == madd3((1 / d["f"][2][2], d["f"])))
                GA.check("M_nu = M_u - m_t f-hat", Mn == madd3((F(1), Mu), (-mt, fhat)))
            k = F(2)
            d2 = dict(d, Y=madd3((1 / k, d["Y"])), vu=k * d["vu"], vd=k * d["vd"])
            GA.check("10 rescaling fixes every Dirac matrix", masses(d2, mu)[:4] == (Mu, Mn, Md, Me))
        GA.check("M_d moves", masses(d, F(3, 5))[2] != Md0)
    return True


PERMS = [[[F(1) if p[i] == j else F(0) for j in range(3)] for i in range(3)] for p in permutations(range(3))]


def check_two_models_of_the_premises_differ_in_the_second_family_factor():
    """(iv) In the diagonal model, w_d = 1/3 gives m_mu/m_s = (M_e)_22/(M_d)_22 = 3 and w_d = 1/5 gives 2, with M_u,
    M_nu (singular values 2/5, 4, 0, so the top reading of (U), sigma_1(M_nu) = m_t), M_R, m_nu, (EW) and the
    Majorana scale identical; w_d = 1/5 with v_d = 47/45 gives 37/19 at the same bottom mass sigma_1(M_d) = 10/3 as
    w_d = 1/3, v_d = 1 (the bottom reading of (U) on the model's own m_b); with an S_3-invariant Majorana matrix (f = alpha Pi + M_3 J/3) Sym(M_d - M_e) =
    4 mu w_d f stays S_3-invariant and its light-plane value 4 mu w_d alpha moves with mu."""
    premise("standard-model.imported-clebsch-structure-seesaw")
    premise("synthesis.residual-s2-fixes-120-family-form")
    premise("neutrino.breaking-relation")
    A = masses(DIAG, F(1))
    B = masses(DIAG, F(3, 5))
    GA.check("model A: second-family factor 3", A[3][1][1] / A[2][1][1] == 3)
    GA.check("model B: second-family factor 2", B[3][1][1] / B[2][1][1] == 2)
    GA.check("the 126 down-type weight differs", A[2][1][1] - B[2][1][1] == F(2, 15))
    GA.check("same M_u, M_nu, M_R, m_nu", A[0] == B[0] and A[1] == B[1] and A[4] == B[4] and A[5] == B[5])
    GA.check("M_nu = diag(-2/5, -4, 0): top reading sigma_1 = m_t", A[1] == mat([[F(-2, 5), 0, 0], [0, -4, 0], [0, 0, 0]])
             and A[0][2][2] == 4)
    C = masses(dict(DIAG, vd=F(47, 45)), F(3, 5))
    GA.check("model C: factor 37/19 at the same bottom mass 10/3",
             C[3][1][1] / C[2][1][1] == F(37, 19) and C[2][2][2] == A[2][2][2] == F(10, 3)
             and all(abs(X[2][i][i]) < X[2][2][2] for X in (A, C) for i in range(2)))
    GA.check("model C: same M_u, M_nu, M_R, m_nu", C[0] == A[0] and C[1] == A[1] and C[4] == A[4] and C[5] == A[5])
    J = mat([[1] * 3] * 3)
    PI = madd3((F(1), mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]])), (F(-1, 3), J))
    alpha, M3 = F(2, 7), F(5)
    fS = madd3((alpha, PI), (M3 / 3, J))
    u = [F(1), F(-1), F(0)]
    for mu in MUS:
        dS = madd3((4 * mu * F(1, 3), fS))
        GA.check("S_3-invariant", all(mmul(mmul(P, dS), tp3(P)) == dS for P in PERMS))
        GA.check("light-plane value 4 mu w_d alpha",
                 [sum((dS[i][j] * u[j] for j in range(3)), F(0)) for i in range(3)] == [4 * mu * F(1, 3) * alpha * x for x in u])
    return True
