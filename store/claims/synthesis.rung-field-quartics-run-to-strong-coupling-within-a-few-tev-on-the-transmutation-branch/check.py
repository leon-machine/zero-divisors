"""Running of the scale-free linear rung field's quartic couplings: exact checks.

The rung field c = sum_a (alpha_a v_a + beta_a w_a) in Cl(3,5) (spacetime and the two rung planes), coefficients in
span{1, I4} (i = I4); eight real components phi = (Re a4, Im a4, Re a5, Im a5, Re b4, Im b4, Re b5, Im b5), each with
kinetic coefficient one. The slot U(2) generators are commutators with rung bivectors (times I4), built in the GA
engine; Q(c) = c^2 is read off the GA product. The potential is the stored ten-invariant quartic
V = k1 A^2 + k2 B^2 + k3 AB + A(k4 ReQ + k5 ImQ) + B(k6 ReQ + k7 ImQ) + k8 Re Q^2 + k9 Im Q^2 + k10 |Q|^2,
A = |alpha|^2, B = |beta|^2. Third-family coupling of the covariant completion at the vacuum alpha = 0: y2 on
conj(beta) to (q, u^c) and y1 on conj(alpha) to (q, d^c), Weyl fermions, three colours.

One loop (Landau gauge): 16 pi^2 beta_V = (1/2)[Tr V''^2 + 3 Tr M_V^4 - 2 Tr (M_F M_F^dag)^2] + phi.gamma.grad V,
gamma = Y2(S) + 3 sum_A g_A^2 t_A t_A. Two loops, pure quartic part:
(16 pi^2)^2 beta_V = -(1/2) V''_ef V'''_egh V'''_fgh + (1/12)(lam lam)_ab phi_a d_b V.
Exact arithmetic throughout (Fractions, Gaussian rationals).
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement, permutations

import GA
from tp_premise import premise

QI = GA.QI

# ---------------------------------------------------------------- Clifford setting
SQ = GA.sig(1, 3) + (F(1), F(-1), F(1), F(-1))


def mul(x, y):
    return GA.mul(x, y, SQ)


I4 = mul(mul(GA.gen(0), GA.gen(1)), mul(GA.gen(2), GA.gen(3)))
VV = {4: GA.scal(F(1, 2), GA.add(GA.gen(4), GA.gen(5))), 5: GA.scal(F(1, 2), GA.add(GA.gen(6), GA.gen(7)))}
WW = {4: GA.scal(F(1, 2), GA.sub(GA.gen(4), GA.gen(5))), 5: GA.scal(F(1, 2), GA.sub(GA.gen(6), GA.gen(7)))}


def cnum(re, im):
    return GA.add(GA.sc(re), GA.scal(im, I4))


def field_of(phi):
    """c = sum_a alpha_a v_a + beta_a w_a for the real components phi."""
    parts = []
    for j, a in enumerate((4, 5)):
        parts.append(mul(cnum(phi[2 * j], phi[2 * j + 1]), VV[a]))
        parts.append(mul(cnum(phi[4 + 2 * j], phi[5 + 2 * j]), WW[a]))
    return GA.add(*parts)


def split(x):
    """(scalar part, I4 part) of an element of span{1, I4}; any other blade is an error."""
    ib = tuple(range(4))
    assert all(b in ((), ib) for b, v in x.items() if v != 0)
    return x.get((), F(0)), x.get(ib, F(0)) / I4[ib]


def coeffs_of(c):
    """Real components of a rung vector: alpha_a = {w_a, c}, beta_a = {v_a, c}."""
    out = []
    for a in (4, 5):
        al = GA.add(mul(WW[a], c), mul(c, WW[a]))
        out.extend(split(al))
    for a in (4, 5):
        be = GA.add(mul(VV[a], c), mul(c, VV[a]))
        out.extend(split(be))
    return [F(x) for x in out]


E = [[F(1) if i == j else F(0) for i in range(8)] for j in range(8)]


def comm(b, x):
    return GA.sub(mul(b, x), mul(x, b))


B4 = GA.sub(mul(VV[4], WW[4]), GA.sc(F(1, 2)))
B5 = GA.sub(mul(VV[5], WW[5]), GA.sc(F(1, 2)))
BIV = {
    "T1": GA.scal(F(1, 2), mul(I4, GA.add(mul(VV[4], WW[5]), mul(VV[5], WW[4])))),
    "T2": GA.scal(F(1, 2), GA.sub(mul(VV[4], WW[5]), mul(VV[5], WW[4]))),
    "T3": GA.scal(F(1, 2), mul(I4, GA.sub(B4, B5))),
    "Y": GA.scal(F(1, 2), mul(I4, GA.add(B4, B5))),
}


def gen_matrix(name):
    """Real 8x8 matrix t with (t phi) the components of [bivector, c(phi)]."""
    cols = [coeffs_of(comm(BIV[name], field_of(E[j]))) for j in range(8)]
    return [[cols[j][i] for j in range(8)] for i in range(8)]


def qform():
    """c^2 = phi^T QR phi + I4 phi^T QI phi, from GA products of basis fields."""
    QR = [[F(0)] * 8 for _ in range(8)]
    QIm = [[F(0)] * 8 for _ in range(8)]
    fs = [field_of(E[j]) for j in range(8)]
    for i in range(8):
        for j in range(8):
            s, t = split(GA.scal(F(1, 2), GA.add(mul(fs[i], fs[j]), mul(fs[j], fs[i]))))
            QR[i][j], QIm[i][j] = s, t
    return QR, QIm


# ---------------------------------------------------------------- the potential
def sparse(M):
    return [(i, j, M[i][j]) for i in range(8) for j in range(8) if M[i][j] != 0]


def build(k, QR, QIm):
    sr, si = sparse(QR), sparse(QIm)

    def V(phi):
        A = sum(x * x for x in phi[:4])
        Bn = sum(x * x for x in phi[4:])
        rq = sum(c * phi[i] * phi[j] for i, j, c in sr)
        iq = sum(c * phi[i] * phi[j] for i, j, c in si)
        return (k[0] * A * A + k[1] * Bn * Bn + k[2] * A * Bn + A * (k[3] * rq + k[4] * iq) + Bn * (k[5] * rq + k[6] * iq)
                + k[7] * (rq * rq - iq * iq) + k[8] * 2 * rq * iq + k[9] * (rq * rq + iq * iq))
    return V


def invariants(phi, QR, QIm):
    A = sum(x * x for x in phi[:4])
    Bn = sum(x * x for x in phi[4:])
    rq = sum(QR[i][j] * phi[i] * phi[j] for i in range(8) for j in range(8))
    iq = sum(QIm[i][j] * phi[i] * phi[j] for i in range(8) for j in range(8))
    return [A * A, Bn * Bn, A * Bn, A * rq, A * iq, Bn * rq, Bn * iq, rq * rq - iq * iq, 2 * rq * iq, rq * rq + iq * iq]


def tensor(V, n=8):
    """lam_abcd = d^4 V by polarisation: F(u1..u4) = sum_S (-1)^(4-|S|) V(sum_S u)."""
    lam = {}
    for idx in combinations_with_replacement(range(n), 4):
        tot = F(0)
        for mask in range(16):
            vec = [F(0)] * n
            for b in range(4):
                if mask >> b & 1:
                    vec[idx[b]] += 1
            sgn = -1 if (4 - bin(mask).count("1")) % 2 else 1
            tot += sgn * V(vec)
        for p in set(permutations(idx)):
            lam[p] = tot
    return lam


def derivs(lam, phi, n=8):
    """V'' (matrix), V''' (3-tensor), grad V at phi for a homogeneous quartic with 4th derivative lam."""
    V3 = {}
    for e in range(n):
        for g in range(n):
            for h in range(n):
                V3[(e, g, h)] = sum(lam[(e, g, h, a)] * phi[a] for a in range(n))
    V2 = [[sum(V3[(e, f, a)] * phi[a] for a in range(n)) / 2 for f in range(n)] for e in range(n)]
    grad = [sum(V2[e][a] * phi[a] for a in range(n)) / 3 for e in range(n)]
    return V2, V3, grad


# ---------------------------------------------------------------- the third-family coupling
FERM = [("q", 0, c) for c in range(3)] + [("q", 1, c) for c in range(3)] + [("u", c) for c in range(3)] + [("d", c) for c in range(3)]
FI = {f: i for i, f in enumerate(FERM)}


def yukawa(phi, y1, y2):
    """Complex symmetric Weyl mass matrix M_F(phi): y2 eps q conj(beta) u^c - y1 (q . conj(alpha)) d^c."""
    al = [QI(phi[0], phi[1]), QI(phi[2], phi[3])]
    be = [QI(phi[4], phi[5]), QI(phi[6], phi[7])]
    M = [[QI(0)] * 12 for _ in range(12)]
    for c in range(3):
        terms = [(("q", 0, c), ("u", c), be[1].conj() * QI(y2)), (("q", 1, c), ("u", c), -(be[0].conj() * QI(y2))),
                 (("q", 0, c), ("d", c), -(al[0].conj() * QI(y1))), (("q", 1, c), ("d", c), -(al[1].conj() * QI(y1)))]
        for f1, f2, co in terms:
            M[FI[f1]][FI[f2]] = M[FI[f1]][FI[f2]] + co
            M[FI[f2]][FI[f1]] = M[FI[f2]][FI[f1]] + co
    return M


def cmm(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), QI(0)) for j in range(n)] for i in range(n)]


def dag(A):
    n = len(A)
    return [[A[j][i].conj() for j in range(n)] for i in range(n)]


def ctr(A):
    return sum((A[i][i] for i in range(len(A))), QI(0))


def fermion_gens():
    """Complex 12x12 generators on the Weyl fields matching the scalar ones (SU(2) on q; hypercharges 1/6, -2/3, 1/3)."""
    sig = {"T1": [[QI(0), QI(1)], [QI(1), QI(0)]], "T2": [[QI(0), QI(0, -1)], [QI(0, 1), QI(0)]], "T3": [[QI(1), QI(0)], [QI(0), QI(-1)]]}
    out = {}
    for name, s in sig.items():
        M = [[QI(0)] * 12 for _ in range(12)]
        for c in range(3):
            for i in range(2):
                for j in range(2):
                    M[FI[("q", i, c)]][FI[("q", j, c)]] = QI(0, F(1, 2)) * s[i][j]
        out[name] = M
    M = [[QI(0)] * 12 for _ in range(12)]
    for f in FERM:
        y = {"q": F(1, 6), "u": F(-2, 3), "d": F(1, 3)}[f[0]]
        M[FI[f]][FI[f]] = QI(0, y)
    out["Y"] = M
    return out


# ---------------------------------------------------------------- beta functions computed from the field
_Y2CACHE = {}


def y2_matrix(y1, y2):
    """Y2(S)_ab = (1/2) Tr(Y^a^dag Y^b + Y^b^dag Y^a), Y^a = M_F(e_a); traces of products as sums of entries."""
    key = (y1, y2)
    if key not in _Y2CACHE:
        Ys = [yukawa(E[a], y1, y2) for a in range(8)]
        _Y2CACHE[key] = [[sum((Ys[a][i][j].conj() * Ys[b][i][j] + Ys[b][i][j].conj() * Ys[a][i][j] for i in range(12) for j in range(12)), QI(0)).re / 2
                          for b in range(8)] for a in range(8)]
    return _Y2CACHE[key]


def beta_V_one_loop(lam, phi, gens, gcoup, y1, y2):
    V2, V3, grad = derivs(lam, phi)
    trH2 = sum(V2[e][f] * V2[e][f] for e in range(8) for f in range(8))
    tphi = [[sum(t[i][j] * phi[j] for j in range(8)) for i in range(8)] for t in gens]
    MV = [[gcoup[A] * gcoup[B] * sum(tphi[A][i] * tphi[B][i] for i in range(8)) for B in range(4)] for A in range(4)]
    trMV4 = sum(MV[A][B] * MV[B][A] for A in range(4) for B in range(4))
    M = yukawa(phi, y1, y2)
    MM = cmm(M, dag(M))
    trF = ctr(cmm(MM, MM))
    assert trF.im == 0
    Y2 = y2_matrix(y1, y2)
    G = [[sum(3 * gcoup[A] ** 2 * sum(gens[A][i][m] * gens[A][m][j] for m in range(8)) for A in range(4)) for j in range(8)] for i in range(8)]
    gam = sum(phi[a] * (Y2[a][b] + G[a][b]) * grad[b] for a in range(8) for b in range(8))
    return (trH2 + 3 * trMV4 - 2 * trF.re) / 2 + gam


def beta_V_two_loop(lam, phi):
    V2, V3, grad = derivs(lam, phi)
    t1 = F(0)
    for e in range(8):
        for f in range(8):
            if V2[e][f] == 0:
                continue
            t1 += V2[e][f] * sum(V3[(e, g, h)] * V3[(f, g, h)] for g in range(8) for h in range(8))
    LL = [[sum(lam[(a, c, d, e)] * lam[(b, c, d, e)] for c in range(8) for d in range(8) for e in range(8)) for b in range(8)] for a in range(8)]
    t2 = sum(phi[a] * LL[a][b] * grad[b] for a in range(8) for b in range(8))
    return -t1 / 2 + t2 / 12


# ---------------------------------------------------------------- the closed forms (the result)
def beta1(k, g, gp, y1, y2):
    k1, k2, k3, k4, k5, k6, k7, k8, k9, k10 = k
    g2, gp2 = g * g, gp * gp
    gauge_d = F(9, 32) * g2 * g2 + F(3, 16) * g2 * gp2 + F(3, 32) * gp2 * gp2
    w = 9 * g2 + 3 * gp2
    return [
        96 * k1 ** 2 + 8 * k3 ** 2 + 8 * k3 * k10 + 4 * k10 ** 2 + 4 * k8 ** 2 + 4 * k9 ** 2 + 12 * k4 ** 2 + 12 * k5 ** 2
        + gauge_d - w * k1 + 24 * k1 * y1 ** 2 - 6 * y1 ** 4,
        96 * k2 ** 2 + 8 * k3 ** 2 + 8 * k3 * k10 + 4 * k10 ** 2 + 4 * k8 ** 2 + 4 * k9 ** 2 + 12 * k6 ** 2 + 12 * k7 ** 2
        + gauge_d - w * k2 + 24 * k2 * y2 ** 2 - 6 * y2 ** 4,
        48 * (k1 + k2) * k3 + 16 * (k1 + k2) * k10 + 16 * k3 ** 2 + 8 * k10 ** 2 + 8 * k8 ** 2 + 8 * k9 ** 2
        + 4 * (k4 ** 2 + k5 ** 2 + k6 ** 2 + k7 ** 2) + 16 * (k4 * k6 + k5 * k7)
        + F(9, 16) * g2 * g2 - F(3, 8) * g2 * gp2 + F(3, 16) * gp2 * gp2 - w * k3 + 12 * k3 * (y1 ** 2 + y2 ** 2) - 12 * y1 ** 2 * y2 ** 2,
        (96 * k1 + 32 * k10 + 24 * k3 + 40 * k8) * k4 + 40 * k5 * k9 + (16 * k10 + 24 * k3 + 8 * k8) * k6 + 8 * k7 * k9
        - w * k4 + (18 * y1 ** 2 + 6 * y2 ** 2) * k4,
        (96 * k1 + 32 * k10 + 24 * k3 - 40 * k8) * k5 + 40 * k4 * k9 + (16 * k10 + 24 * k3 - 8 * k8) * k7 + 8 * k6 * k9
        - w * k5 + (18 * y1 ** 2 + 6 * y2 ** 2) * k5,
        (96 * k2 + 32 * k10 + 24 * k3 + 40 * k8) * k6 + 40 * k7 * k9 + (16 * k10 + 24 * k3 + 8 * k8) * k4 + 8 * k5 * k9
        - w * k6 + (6 * y1 ** 2 + 18 * y2 ** 2) * k6,
        (96 * k2 + 32 * k10 + 24 * k3 - 40 * k8) * k7 + 40 * k6 * k9 + (16 * k10 + 24 * k3 - 8 * k8) * k5 + 8 * k4 * k9
        - w * k7 + (6 * y1 ** 2 + 18 * y2 ** 2) * k7,
        (16 * (k1 + k2) + 48 * k10 + 32 * k3) * k8 + 10 * (k4 ** 2 - k5 ** 2 + k6 ** 2 - k7 ** 2) + 4 * (k4 * k6 - k5 * k7)
        - w * k8 + 12 * k8 * (y1 ** 2 + y2 ** 2),
        (16 * (k1 + k2) + 48 * k10 + 32 * k3) * k9 + 20 * (k4 * k5 + k6 * k7) + 4 * (k4 * k7 + k5 * k6)
        - w * k9 + 12 * k9 * (y1 ** 2 + y2 ** 2),
        16 * (k1 + k2) * k10 + 16 * k10 ** 2 + 32 * k10 * k3 + 32 * (k8 ** 2 + k9 ** 2) + 10 * (k4 ** 2 + k5 ** 2 + k6 ** 2 + k7 ** 2)
        + 4 * (k4 * k6 + k5 * k7) + F(3, 4) * g2 * gp2 - w * k10 + 12 * k10 * (y1 ** 2 + y2 ** 2) + 12 * y1 ** 2 * y2 ** 2,
    ]


def beta2_z2(k):
    """Two-loop pure-quartic part on the subspace k4 = k5 = k6 = k7 = 0 (the stored scale-free branch)."""
    k1, k2, k3, k4, k5, k6, k7, k8, k9, k10 = k
    s = k8 ** 2 + k9 ** 2
    return [
        -4992 * k1 ** 3 - 192 * k1 * k10 ** 2 - 320 * k1 * k10 * k3 - 320 * k1 * k3 ** 2 - 224 * k1 * s - 96 * k10 ** 3
        - 256 * k10 ** 2 * k3 - 192 * k10 * k3 ** 2 - 352 * k10 * s - 128 * k3 ** 3 - 320 * k3 * s,
        -4992 * k2 ** 3 - 192 * k2 * k10 ** 2 - 320 * k2 * k10 * k3 - 320 * k2 * k3 ** 2 - 224 * k2 * s - 96 * k10 ** 3
        - 256 * k10 ** 2 * k3 - 192 * k10 * k3 ** 2 - 352 * k10 * s - 128 * k3 ** 3 - 320 * k3 * s,
        -(k1 ** 2 + k2 ** 2) * (256 * k10 + 960 * k3) - (k1 + k2) * (448 * k10 ** 2 + 512 * k10 * k3 + 1152 * k3 ** 2 + 576 * s)
        - 192 * k10 ** 3 - 256 * k10 ** 2 * k3 - 64 * k10 * k3 ** 2 - 704 * k10 * s - 192 * k3 ** 3 - 288 * k3 * s,
        F(0), F(0), F(0), F(0),
        k8 * (-448 * (k1 ** 2 + k2 ** 2) - 1408 * (k1 + k2) * k10 - 1280 * (k1 + k2) * k3 - 512 * k10 ** 2 - 1216 * k10 * k3
              - 448 * k3 ** 2 + 96 * s),
        k9 * (-448 * (k1 ** 2 + k2 ** 2) - 1408 * (k1 + k2) * k10 - 1280 * (k1 + k2) * k3 - 512 * k10 ** 2 - 1216 * k10 * k3
              - 448 * k3 ** 2 + 96 * s),
        -448 * (k1 ** 2 + k2 ** 2) * k10 - 640 * (k1 + k2) * k10 ** 2 - 1280 * (k1 + k2) * k10 * k3 - 768 * (k1 + k2) * s
        - 448 * k10 ** 2 * k3 - 448 * k10 * k3 ** 2 - 416 * k10 * s - 768 * k3 * s,
    ]


PHIS = [[F(1), F(-2), F(3, 2), F(1, 3), F(-1), F(2, 5), F(1, 2), F(-3, 4)],
        [F(2), F(1), F(-1, 2), F(3), F(1, 4), F(-1), F(5, 3), F(1)],
        [F(-1, 3), F(1, 2), F(2), F(-1), F(3), F(1, 7), F(-2), F(1, 5)],
        [F(3, 4), F(0), F(-1), F(2, 3), F(1, 2), F(-5, 2), F(1), F(2)]]
GC = (F(13, 20), F(9, 25))   # g, g' (rational sample values)


def setting():
    QR, QIm = qform()
    gens = [gen_matrix(n) for n in ("T1", "T2", "T3", "Y")]
    return QR, QIm, gens


def check_rung_field_generators_and_form_from_the_clifford_algebra():
    """The four slot generators are commutators with rung bivectors (I4 the unit) and reproduce the stored U(2)
    action; c^2 = Q(c) = alpha^T beta; V is U(2)-invariant; the Yukawa coupling is gauge invariant."""
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    premise("synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix")
    QR, QIm, gens = setting()
    # stored action: alpha -> (i/2) sigma_j alpha, beta -> conj((i/2) sigma_j) beta; Y: +i/2, -i/2
    sig = {"T1": [[QI(0), QI(1)], [QI(1), QI(0)]], "T2": [[QI(0), QI(0, -1)], [QI(0, 1), QI(0)]], "T3": [[QI(1), QI(0)], [QI(0), QI(-1)]],
           "Y": [[QI(1), QI(0)], [QI(0), QI(1)]]}
    ok = True
    for t, name in zip(gens, ("T1", "T2", "T3", "Y")):
        Mx = [[QI(0, F(1, 2)) * sig[name][i][j] for j in range(2)] for i in range(2)]
        for phi in PHIS[:2]:
            al = [QI(phi[0], phi[1]), QI(phi[2], phi[3])]
            be = [QI(phi[4], phi[5]), QI(phi[6], phi[7])]
            na = [Mx[i][0] * al[0] + Mx[i][1] * al[1] for i in range(2)]
            nb = [Mx[i][0].conj() * be[0] + Mx[i][1].conj() * be[1] for i in range(2)]
            want = [na[0].re, na[0].im, na[1].re, na[1].im, nb[0].re, nb[0].im, nb[1].re, nb[1].im]
            got = [sum(t[i][j] * phi[j] for j in range(8)) for i in range(8)]
            ok = ok and want == got
    GA.check("bivector commutators reproduce the stored U(2) action (T_j = (i/2) sigma_j, Y = i/2, conjugate on beta)", ok)
    GA.check("generators are real antisymmetric", all(t[i][j] == -t[j][i] for t in gens for i in range(8) for j in range(8)))
    phi = PHIS[0]
    al = [QI(phi[0], phi[1]), QI(phi[2], phi[3])]
    be = [QI(phi[4], phi[5]), QI(phi[6], phi[7])]
    q = al[0] * be[0] + al[1] * be[1]
    c = field_of(phi)
    s, t = split(mul(c, c))
    GA.check("c^2 = alpha^T beta in span{1, I4} (Q from the Clifford product)", (s, t) == (q.re, q.im))
    rq = sum(QR[i][j] * phi[i] * phi[j] for i in range(8) for j in range(8))
    iq = sum(QIm[i][j] * phi[i] * phi[j] for i in range(8) for j in range(8))
    GA.check("the bilinear form read from GA gives Q", (rq, iq) == (q.re, q.im))
    k = [F(1, 3), F(2), F(-1, 2), F(1, 5), F(-2, 7), F(3), F(1, 4), F(-1), F(5, 4), F(2, 3)]
    V = build(k, QR, QIm)
    lam = tensor(V)
    _, _, grad = derivs(lam, PHIS[1])
    GA.check("V is invariant under all four generators (grad V . t phi = 0)",
             all(sum(grad[i] * sum(t[i][j] * PHIS[1][j] for j in range(8)) for i in range(8)) == 0 for t in gens))
    fg = fermion_gens()
    ok = True
    for t, name in zip(gens, ("T1", "T2", "T3", "Y")):
        phi = PHIS[2]
        tphi = [sum(t[i][j] * phi[j] for j in range(8)) for i in range(8)]
        M = yukawa(phi, F(2, 3), F(5, 7))
        Mt = yukawa(tphi, F(2, 3), F(5, 7))
        tau = fg[name]
        tauT = [[tau[j][i] for j in range(12)] for i in range(12)]
        S1, S2 = cmm(tauT, M), cmm(M, tau)
        ok = ok and all(Mt[i][j] + S1[i][j] + S2[i][j] == QI(0) for i in range(12) for j in range(12))
    GA.check("the third-family coupling is SU(2) x U(1) invariant (M_F(t phi) + tau^T M_F + M_F tau = 0)", ok)
    Mv = yukawa([F(0)] * 4 + [F(-1), F(0), F(0), F(0)], F(2, 3), F(5, 7))
    GA.check("at alpha = 0, beta = (-1, 0) only the up-type pair has mass y2 (top), the alpha coupling is off",
             Mv[FI[("q", 1, 0)]][FI[("u", 0)]] == QI(F(5, 7)) and all(Mv[FI[("q", i, 0)]][FI[("d", 0)]] == QI(0) for i in range(2)))


def check_method_reproduces_one_doublet_and_on_coefficients():
    """The tensor formulas give the standard one-doublet beta_lambda (one loop) and the O(N) coefficients
    (N + 8)/3 and -(3N + 14)/3 for N = 1 and N = 8."""
    premise("synthesis.imported-coleman-weinberg-gildener-weinberg-scalon-mass")
    premise("synthesis.rung-field-on-the-lift-locus")
    QR, QIm, gens = setting()
    g, gp = GC
    y = F(5, 7)
    lamSM = F(3, 10)
    # one doublet: V = lamSM |H|^4 with beta = sqrt2 H, so k2 = lamSM / 4; y2 = y_t / sqrt2
    k = [F(0), lamSM / 4] + [F(0)] * 8
    V = build(k, QR, QIm)
    lam = tensor(V)
    phi = [F(0)] * 4 + PHIS[0][4:]
    bV = beta_V_one_loop(lam, phi, gens, [g, g, g, gp], F(0), y)
    H2 = sum(x * x for x in phi[4:]) / 2
    yt2 = 2 * y * y
    sm = (24 * lamSM ** 2 - 3 * lamSM * (3 * g * g + gp * gp) + F(3, 8) * (2 * g ** 4 + (g * g + gp * gp) ** 2)
          + 12 * lamSM * yt2 - 6 * yt2 * yt2)
    GA.check("one doublet: 16pi^2 beta_lambda = 24l^2 - 3l(3g^2+g'^2) + (3/8)(2g^4+(g^2+g'^2)^2) + 12 l y_t^2 - 6 y_t^4", bV == sm * H2 * H2)
    for N in (1, 8):
        c = F(1, 24)
        lam_on = 24 * c
        if N == 1:
            Von = lambda p: c * p[0] ** 4
            phi = [F(3, 2)] + [F(0)] * 7
        else:
            Von = lambda p: c * sum(x * x for x in p) ** 2
            phi = PHIS[1]
        lamt = tensor(Von)
        r2 = sum(x * x for x in phi) ** 2
        b1 = beta_V_one_loop(lamt, phi, gens, [F(0)] * 4, F(0), F(0))
        b2 = beta_V_two_loop(lamt, phi)
        GA.check("O(%d): one loop (N + 8)/3 lam^2" % N, b1 == F(N + 8, 3) * lam_on ** 2 * r2 / 24)
        GA.check("O(%d): two loops -(3N + 14)/3 lam^3" % N, b2 == -F(3 * N + 14, 3) * lam_on ** 3 * r2 / 24)


SETS1 = [([F(1, 3), F(2), F(-1, 2), F(1, 5), F(-2, 7), F(3), F(1, 4), F(-1), F(5, 4), F(2, 3)], F(2, 3), F(5, 7)),
         ([F(0), F(0), F(6, 5), F(0), F(0), F(0), F(0), F(1, 3), F(-1, 4), F(7, 10)], F(7, 10), F(7, 10))]
PHIS3 = PHIS[:3]
PA = [F(1), F(2), F(-1), F(1, 2), F(0), F(0), F(0), F(0)]     # alpha only: P1 = A^2, every other invariant zero
K0 = [F(0)] * 10
GSAMPLE = (F(2, 3), F(1, 3))
YSAMPLE = F(3, 5)


def unit_k(i, x=F(1)):
    k = list(K0)
    k[i] = x
    return k


def field_coef(k, gc, y1, y2, phi, QR, QIm, gens):
    """16 pi^2 beta_V(phi) / A(phi)^2 from the field, for phi with beta = 0 (so it is 16 pi^2 beta_k1)."""
    lam = tensor(build(k, QR, QIm))
    A = sum(x * x for x in phi[:4])
    return beta_V_one_loop(lam, phi, gens, [gc[0], gc[0], gc[0], gc[1]], y1, y2) / (A * A)


def check_one_loop_running_of_the_ten_rung_quartics():
    """The closed one-loop beta functions of k1..k10 equal the field computation at sampled couplings and points;
    coefficients of beta_k1 read directly off the field at a point with beta = 0."""
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    premise("synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix")
    QR, QIm, gens = setting()
    g, gp = GC
    ok = True
    for k, y1, y2 in SETS1:
        lam = tensor(build(k, QR, QIm))
        bk = beta1(k, g, gp, y1, y2)
        for phi in PHIS3:
            lhs = beta_V_one_loop(lam, phi, gens, [g, g, g, gp], y1, y2)
            rhs = sum(b * p for b, p in zip(bk, invariants(phi, QR, QIm)))
            ok = ok and lhs == rhs
    GA.check("16 pi^2 beta_k (closed forms) = field computation, two coupling sets x three points", ok)
    zero = (F(0), F(0))
    GA.check("field: k1 alone gives 96 k1^2", field_coef(unit_k(0), zero, F(0), F(0), PA, QR, QIm, gens) == 96)
    GA.check("field: k3 alone gives 8 k3^2, k10 alone 4 k10^2, k8 alone 4 k8^2, k4 alone 12 k4^2",
             [field_coef(unit_k(i), zero, F(0), F(0), PA, QR, QIm, gens) for i in (2, 9, 7, 3)] == [8, 4, 4, 12])
    gg, gq = GSAMPLE
    GA.check("field: gauge alone gives (9/32) g^4 + (3/16) g^2 g'^2 + (3/32) g'^4",
             field_coef(K0, GSAMPLE, F(0), F(0), PA, QR, QIm, gens) == F(9, 32) * gg ** 4 + F(3, 16) * gg ** 2 * gq ** 2 + F(3, 32) * gq ** 4)
    GA.check("field: k1 with gauge and the alpha coupling gives 96 k1^2 + G - (9 g^2 + 3 g'^2) k1 + 24 k1 y1^2 - 6 y1^4",
             field_coef(unit_k(0), GSAMPLE, YSAMPLE, F(0), PA, QR, QIm, gens)
             == 96 + F(9, 32) * gg ** 4 + F(3, 16) * gg ** 2 * gq ** 2 + F(3, 32) * gq ** 4 - (9 * gg ** 2 + 3 * gq ** 2) + 24 * YSAMPLE ** 2 - 6 * YSAMPLE ** 4)
    GA.check("field: the beta coupling y2 does not enter beta_k1 at k1 = 0", field_coef(K0, zero, F(0), YSAMPLE, PA, QR, QIm, gens) == 0)


def check_two_loop_pure_quartic_running_on_the_z2_branch():
    """Closed two-loop pure-quartic beta functions on k4 = k5 = k6 = k7 = 0 equal the field computation; the
    subspace is closed at one loop (with the coupling) and at two loops."""
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    premise("synthesis.imported-general-quartic-running-and-two-doublet-renormalisation-group-equations")
    QR, QIm, gens = setting()
    k = [F(1, 2), F(1, 3), F(6, 5), F(0), F(0), F(0), F(0), F(1, 3), F(-1, 4), F(7, 10)]
    lam = tensor(build(k, QR, QIm))
    b2 = beta2_z2(k)
    ok = True
    for phi in PHIS[:3]:
        lhs = beta_V_two_loop(lam, phi)
        rhs = sum(b * p for b, p in zip(b2, invariants(phi, QR, QIm)))
        ok = ok and lhs == rhs
    GA.check("(16 pi^2)^2 beta2_k (closed forms, k4..k7 = 0) = field computation at three points", ok)
    b1 = beta1(k, GC[0], GC[1], F(2, 3), F(5, 7))
    GA.check("k4 = k5 = k6 = k7 = 0 is preserved at one loop", all(b1[i] == 0 for i in (3, 4, 5, 6)))
    GA.check("k4 = k5 = k6 = k7 = 0 is preserved at two loops", all(b2[i] == 0 for i in (3, 4, 5, 6)))


FLAT_SAMPLES = [(F(6, 5), F(7, 10), F(1, 3), F(-1, 4), F(13, 20), F(9, 25), F(7, 10), F(1)),
                (F(3, 2), F(-1, 2), F(2, 5), F(0), F(2, 3), F(1, 3), F(5, 7), F(3, 2)),
                (F(1, 2), F(1), F(0), F(1, 2), F(3, 5), F(2, 5), F(3, 4), F(2))]
FLAT_K1, FLAT_Y1 = F(1, 7), F(1, 3)


def scalon_sum(k3, k10, k8, k9, g, gp, y2, v):
    MW2, MZ2 = g * g * v * v / 4, (g * g + gp * gp) * v * v / 4
    mpm2 = 2 * k3 * v * v
    s, r2 = k3 + k10, k8 * k8 + k9 * k9
    mH4_plus_mA4 = 8 * v ** 4 * (s * s + r2)       # m_{H,A}^2 = 2 v^2 (k3 + k10 +- r)
    return 6 * MW2 ** 2 + 3 * MZ2 ** 2 + 2 * mpm2 ** 2 + mH4_plus_mA4 - 12 * (y2 * v) ** 4


def check_flat_direction_running_is_the_scalon_sum():
    """On the stored flat ray (k2 = k6 = k7 = 0) the running of k2 is the scalon sum:
    2 v^4 (16 pi^2 beta_k2) = 6 M_W^4 + 3 M_Z^4 + 2 m_pm^4 + m_H^4 + m_A^4 - 12 m_t^4, so m_h^2 = 4 v^2 beta_k2,
    with the stored tree masses; and the field's beta_V on the ray is (1/2) STr M^4."""
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    premise("synthesis.imported-coleman-weinberg-gildener-weinberg-scalon-mass")
    premise("synthesis.imported-two-doublet-scalon-sum-rule-and-lep-neutrino-count")
    QR, QIm, gens = setting()
    ok = True
    for k3, k10, k8, k9, g, gp, y2, v in FLAT_SAMPLES:
        k = [FLAT_K1, F(0), k3, F(0), F(0), F(0), F(0), k8, k9, k10]
        b = beta1(k, g, gp, FLAT_Y1, y2)[1]
        X = scalon_sum(k3, k10, k8, k9, g, gp, y2, v)
        lam = tensor(build(k, QR, QIm))
        phi = [F(0)] * 4 + [-v, F(0), F(0), F(0)]
        bV = beta_V_one_loop(lam, phi, gens, [g, g, g, gp], FLAT_Y1, y2)
        ok = ok and 2 * v ** 4 * b == X and bV == b * v ** 4 and 2 * bV == X
    GA.check("2 v^4 x 16pi^2 beta_k2 = scalon sum with the stored masses, three samples; beta_V(ray) = beta_k2 v^4", ok)
    k3, k10, k8, k9, g, gp, y2, v = FLAT_SAMPLES[0]
    b = beta1([F(0), F(0), k3, F(0), F(0), F(0), F(0), k8, k9, k10], g, gp, F(0), y2)[1]
    X0 = 6 * (g * g * v * v / 4) ** 2 + 3 * ((g * g + gp * gp) * v * v / 4) ** 2 + 2 * (2 * k3 * v * v) ** 2 - 12 * (y2 * v) ** 4
    GA.check("control: the sum without m_H^4 + m_A^4 (the stored constrained bracket) differs", 2 * v ** 4 * b != X0)
    k3, k10, k8, k9, g, gp, y2, v = FLAT_SAMPLES[1]
    b = beta1([FLAT_K1, F(0), k3, F(0), F(0), F(0), F(0), k8, k9, k10], g, gp, FLAT_Y1, y2)[1]
    GA.check("m_h^2 = 4 v^2 beta_k2: pi^2 m_h^2 = X / (8 v^2) equals pi^2 4 v^2 (b / 16 pi^2)",
             scalon_sum(k3, k10, k8, k9, g, gp, y2, v) / (8 * v ** 2) == 4 * v ** 2 * b / 16)


def check_dictionary_to_the_standard_two_doublet_equations():
    """With lambda1 = 8k1, lambda2 = 8k2, lambda3 = 4k3, lambda4 = 4k10, lambda5 = 4(k8 - i k9), y_b = sqrt2 y1,
    y_t = sqrt2 y2, the closed forms are the standard one-loop two-doublet equations (Z2-symmetric, type-II-like
    couplings): compared term by term at sampled couplings."""
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    premise("synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix")
    premise("synthesis.imported-general-quartic-running-and-two-doublet-renormalisation-group-equations")
    g, gp = GC
    ok = True
    for k1, k2, k3, k10, k8, k9, y1, y2 in [(F(1, 3), F(1, 5), F(6, 5), F(7, 10), F(1, 3), F(-1, 4), F(2, 3), F(5, 7)),
                                              (F(2), F(-1, 2), F(1, 7), F(-3, 2), F(0), F(1, 2), F(1, 2), F(3, 4))]:
        k = [k1, k2, k3, F(0), F(0), F(0), F(0), k8, k9, k10]
        b = beta1(k, g, gp, y1, y2)
        l1, l2, l3, l4 = 8 * k1, 8 * k2, 4 * k3, 4 * k10
        l5sq = 16 * (k8 * k8 + k9 * k9)
        yb2, yt2 = 2 * y1 * y1, 2 * y2 * y2
        g2, gp2 = g * g, gp * gp
        w = 3 * (3 * g2 + gp2)
        s1 = 12 * l1 ** 2 + 4 * l3 ** 2 + 4 * l3 * l4 + 2 * l4 ** 2 + 2 * l5sq + F(3, 4) * (3 * g2 ** 2 + gp2 ** 2 + 2 * g2 * gp2) - w * l1 + 12 * l1 * yb2 - 12 * yb2 ** 2
        s2 = 12 * l2 ** 2 + 4 * l3 ** 2 + 4 * l3 * l4 + 2 * l4 ** 2 + 2 * l5sq + F(3, 4) * (3 * g2 ** 2 + gp2 ** 2 + 2 * g2 * gp2) - w * l2 + 12 * l2 * yt2 - 12 * yt2 ** 2
        s3 = (l1 + l2) * (6 * l3 + 2 * l4) + 4 * l3 ** 2 + 2 * l4 ** 2 + 2 * l5sq + F(3, 4) * (3 * g2 ** 2 + gp2 ** 2 - 2 * g2 * gp2) - w * l3 + 6 * l3 * (yt2 + yb2) - 12 * yt2 * yb2
        s4 = 2 * (l1 + l2) * l4 + 8 * l3 * l4 + 4 * l4 ** 2 + 8 * l5sq + 3 * g2 * gp2 - w * l4 + 6 * l4 * (yt2 + yb2) + 12 * yt2 * yb2
        s5 = 2 * (l1 + l2) + 8 * l3 + 12 * l4 - w + 6 * (yt2 + yb2)
        ok = ok and (8 * b[0], 8 * b[1], 4 * b[2], 4 * b[9]) == (s1, s2, s3, s4)
        ok = ok and 4 * b[7] == s5 * 4 * k8 and 4 * b[8] == s5 * 4 * k9
    GA.check("closed forms = standard one-loop two-doublet equations under the dictionary", ok)


def check_scalon_trilinear_is_five_thirds():
    """Along the flat ray V = B rho^4 (L - 1/2), L = ln(rho^2/v^2): V'(v) = 0, V''(v) = 8 B v^2 = m_h^2,
    V'''(v) = 40 B v = (5/3)(3 m_h^2 / v): the scalon's self-coupling is 5/3 of the tree value for the same mass.
    Terms c rho^n L^m are differentiated exactly with dL/drho = 2/rho; L symbolic."""
    premise("synthesis.imported-coleman-weinberg-gildener-weinberg-scalon-mass")

    def d(poly):
        out = {}
        for (n, m), c in poly.items():
            if n:
                out[(n - 1, m)] = out.get((n - 1, m), F(0)) + c * n
            if m:
                out[(n - 1, m - 1)] = out.get((n - 1, m - 1), F(0)) + c * m * 2
        return {key: val for key, val in out.items() if val}

    def at_v(poly, v):   # L(v) = 0
        return sum((c * v ** n for (n, m), c in poly.items() if m == 0), F(0))
    Bc, v = F(3, 11), F(7, 4)
    V = {(4, 1): Bc, (4, 0): -Bc / 2}
    d1 = d(V)
    d2 = d(d1)
    d3 = d(d2)
    GA.check("V'(v) = 0", at_v(d1, v) == 0)
    GA.check("V''(v) = 8 B v^2", at_v(d2, v) == 8 * Bc * v * v)
    GA.check("V'''(v) = 40 B v = (5/3) 3 m_h^2 / v", at_v(d3, v) == 40 * Bc * v and at_v(d3, v) == F(5, 3) * 3 * at_v(d2, v) / v)


# ---------------------------------------------------------------- clause (v): the one-loop 4 pi crossing, bracketed
PI_LO, PI_HI = F(333, 106), F(355, 113)          # pi_lo < pi < pi_hi
V_EW = F(24622, 100)
MT0 = F(173)                                       # mu0 = m_t (GeV)
G0 = (F(81, 125), F(179, 500), F(291, 250), F(331, 500))   # g, g', g3, y1 = y2 at mu0 (0.648, 0.358, 1.164, 0.662)
ENDPOINTS = [((F(80), F(528), F(305)), F(3, 4), F(17, 20)),        # (m_pm, m_H, m_A) GeV; bracket (TeV) for the crossing
             ((F(320), F(418), F(418)), F(19, 5), F(21, 5))]
HSTEP = F(1, 25)
GRID = 10 ** 12


def rnd(x):
    return F(round(x * GRID), GRID)


def flow(state, pi):
    """One-loop right-hand side d/dt of (k1..k10, g, g', g3, y): the closed forms with y1 = y2 = y, the stored
    two-doublet gauge coefficients (7, -3, -7) in the non-GUT normalisation of g', and the top coupling."""
    k, (g, gp, g3, y) = state[:10], state[10:]
    L = 16 * pi * pi
    dk = [b / L for b in beta1(k, g, gp, y, y)]
    dg = [7 * gp ** 3 / L, -3 * g ** 3 / L, -7 * g3 ** 3 / L]
    dy = y * (10 * y * y - 8 * g3 * g3 - F(9, 4) * g * g - F(11, 12) * gp * gp) / L
    return dk + [dg[1], dg[0], dg[2], dy]


def rk4(state, pi):
    f1 = flow(state, pi)
    f2 = flow([a + HSTEP / 2 * b for a, b in zip(state, f1)], pi)
    f3 = flow([a + HSTEP / 2 * b for a, b in zip(state, f2)], pi)
    f4 = flow([a + HSTEP * b for a, b in zip(state, f3)], pi)
    return [rnd(a + HSTEP / 6 * (b + 2 * c + 2 * d + e)) for a, b, c, d, e in zip(state, f1, f2, f3, f4)]


def lam_max(state):
    k = state[:10]
    return max(abs(8 * k[0]), abs(8 * k[1]), abs(4 * k[2]), abs(4 * k[9]), 4 * abs(k[7]))


def exp_bounds(t, n=30):
    """Rational lo <= e^t <= hi for 0 <= t <= 4 (partial sum; tail bounded by the next term times 2)."""
    term, tot = F(1), F(1)
    for j in range(1, n):
        term = term * t / j
        tot += term
    return tot, tot + 2 * term * t / n


def crossing_step(spec, pi):
    mpm, mH, mA = spec
    v2 = V_EW * V_EW
    k3 = mpm * mpm / (2 * v2)
    k10 = (mH * mH + mA * mA - 2 * mpm * mpm) / (4 * v2)
    r = abs(mH * mH - mA * mA) / (4 * v2)
    state = [F(0), F(0), rnd(k3), F(0), F(0), F(0), F(0), rnd(r), F(0), rnd(k10)] + list(G0)
    n = 0
    while lam_max(state) < 4 * pi:
        state = rk4(state, pi)
        n += 1
        if n > 200:
            return None
    return n


def check_one_loop_quartics_reach_four_pi_within_a_few_tev():
    """Clause (v) at its two endpoint spectra, one loop, exact rationals: fourth-order Runge-Kutta in t = ln(mu/m_t)
    with step 1/25 and states rounded to 10^-12, run with both rational bounds of pi; the first step at which
    max|lambda_i| >= 4 pi lies in a bracket that, through rational bounds on e^t, puts the crossing between
    0.75 and 0.85 TeV for (m_pm, m_H, m_A) = (80, 528, 305) GeV and between 3.8 and 4.2 TeV for (320, 418, 418) GeV."""
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    premise("synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix")
    premise("synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces")
    ok = True
    for spec, lo_tev, hi_tev in ENDPOINTS:
        for pi in (PI_LO, PI_HI):
            n = crossing_step(spec, pi)
            ok = ok and n is not None
            if n is None:
                break
            t_before, t_after = (n - 1) * HSTEP, n * HSTEP
            e_lo, _ = exp_bounds(t_before)
            _, e_hi = exp_bounds(t_after)
            ok = ok and MT0 * e_lo >= 1000 * lo_tev and MT0 * e_hi <= 1000 * hi_tev
    GA.check("one-loop crossing of 4 pi: (80, 528, 305) GeV in (0.75, 0.85) TeV, (320, 418, 418) GeV in (3.8, 4.2) TeV", ok)
    GA.check("control: the gauge coefficient 7 of g' is the stored 21/5 times 5/3", F(21, 5) * F(5, 3) == 7)

if __name__ == "__main__":
    for fn in [check_rung_field_generators_and_form_from_the_clifford_algebra,
               check_method_reproduces_one_doublet_and_on_coefficients,
               check_one_loop_running_of_the_ten_rung_quartics,
               check_two_loop_pure_quartic_running_on_the_z2_branch,
               check_flat_direction_running_is_the_scalon_sum,
               check_dictionary_to_the_standard_two_doublet_equations,
               check_scalon_trilinear_is_five_thirds,
               check_one_loop_quartics_reach_four_pi_within_a_few_tev]:
        fn()
    print("FAILURES:", GA.FAILURES)
