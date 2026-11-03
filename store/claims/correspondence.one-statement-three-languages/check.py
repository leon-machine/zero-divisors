"""correspondence.one-statement-three-languages: exact checks in Cl(2,4).

Conventions: e0 (+1), e1..e3 (-1), e+ (+1), e- (-1); n0 = (e+ + e-)/2, ninf = e+ - e-. Conformal
spinor space CS = Cl^+(2,4) P with P = (1 + e0e1)(1 + e2e+)/4, complex unit I6 (I6 psi = psi I6 on CS).
The map Psi from vectors to Lambda^2 CS is realised by the antisymmetric I6-bilinear forms
    b_v(psi, phi) = <psi~ v phi M>_0 - i <psi~ v phi I6 M>_0,     M = e0 e2 e3,
which are Spin(2,4)-equivariant for any fixed M (psi~ R~ R v R~ R phi = psi~ v phi); a bivector of
CS and a 2-form correspond through the volume form, so simplicity is rank 2 and eps(P ^ P) is the
Pfaffian up to one normalising constant.
  (a) b_v is complex bilinear (b(I6 psi, phi) = i b(psi, phi)) and antisymmetric, and Pf(b_v) = -Q(v)/16
      on the 21 vectors e_i, e_i + e_j, hence identically (both sides quadratic): eps := -16 Pf gives
      eps(Psi(v) ^ Psi(v)) = Q(v), and for the scale tractor I_g = ninf + (Lambda/6) n0, eps = Lambda/3.
  (b) Psi(I_g) is simple (rank 2) exactly when Lambda = 0; then its plane is ker(ninf) in CS (the
      infinity line); non-null vectors give rank 4 and null ones rank 2.
  (c) Constancy in three languages: for every bivector B, b_{B x v}(psi, phi) + b_v(B psi/2, phi)
      + b_v(psi, B phi/2) = 0, so the induced derivative of Psi(I) under the tractor gauge field is
      Psi(D^T I); it vanishes on an Einstein Schouten map P = (Lambda/6) id and not on a non-Einstein one.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
ER = [GA.scal(F(1, S[i]), E[i]) for i in range(4)]
N0 = GA.scal(F(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])
BLADES = GA.all_blades(6)


def mul(*xs):
    r = GA.sc(1)
    for x in xs:
        r = GA.mul(r, x, S)
    return r


def comm(X, Y):
    return GA.scal(F(1, 2), GA.sub(GA.mul(X, Y, S), GA.mul(Y, X, S)))


def dot(a, b):
    return GA.dot(a, b, S)


def vec(c):
    return GA.add(*[GA.scal(F(c[i]), E[i]) for i in range(len(c))])


def rank(xs):
    return GA.rank_of_vectors([GA.basis_vector_of(x, BLADES) for x in xs]) if xs else 0


I6 = mul(*E)
PID = GA.scal(F(1, 4), mul(GA.add(GA.sc(1), mul(E[0], E[1])), GA.add(GA.sc(1), mul(E[2], E[4]))))
MFUN = mul(E[0], E[2], E[3])


def _complex_basis():
    out = []
    for b in BLADES:
        if len(b) % 2:
            continue
        c = GA.mul({b: F(1)}, PID, S)
        trial = out + [c]
        if rank(trial + [mul(I6, t) for t in trial]) == 2 * len(trial):
            out.append(c)
    return out


CB = _complex_basis()


def bform(v, psi, phi):
    X = mul(GA.reverse(psi), v, phi)
    return GA.qi(mul(X, MFUN).get((), F(0)), -mul(X, I6, MFUN).get((), F(0)))


def bmat(v):
    return [[bform(v, CB[j], CB[k]) for k in range(4)] for j in range(4)]


def pf(A):
    return A[0][1] * A[2][3] - A[0][2] * A[1][3] + A[0][3] * A[1][2]


def smap(M):
    return lambda A: GA.add(*[GA.scal(sum(F(M[m][n]) * dot(A, ER[m]) for m in range(4)), ER[n])
                              for n in range(4)])


def theta(A, P):
    return GA.add(GA.neg(comm(NI, A)), comm(N0, P(A)))


POLAR = [E[i] for i in range(6)] + [GA.add(E[i], E[j]) for i in range(6) for j in range(i + 1, 6)]
LAMS = (F(3, 2), F(-6, 5), F(1, 7))
NULLS = [GA.add(E[0], E[1]), GA.add(E[4], E[2]), GA.add(vec([1, 0, 0, 0, 0, 0]), vec([0, 0, 0, 0, 0, 1])),
         GA.add(NI, vec([2, 0, 0, 0]), GA.scal(-2, N0)), GA.add(N0, GA.scal(F(1, 2), GA.add(E[0], E[3])))]
PNON = [[2, 1, 0, -3], [1, -1, 4, 0], [0, 4, 5, 2], [-3, 0, 2, 7]]
DIRS = ([1, 0, 0, 0], [0, 1, 2, 0], [3, 1, -2, 5])
OMS = [mul(E[0], E[1]), GA.add(mul(E[1], E[2]), mul(E[0], E[3]))]
VS = [GA.add(NI, GA.scal(F(1, 4), N0)), GA.add(E[0], GA.scal(2, E[2]), E[5])]   # sample vectors for the invariance of the form
BIV_DIRS = DIRS[:2]                          # directions whose soldering bivectors are sampled
LAM_E = F(3, 2)                              # sample cosmological constant of the Einstein case
OM_E = OMS[0]                                # sample Lorentz part of the transported bivector


def check_infinity_bivector_norm_is_lambda_over_three():
    premise("correspondence.spinor-identification")
    premise("correspondence.imported-vacuum-equations-scale-tractor")
    ok = len(CB) == 4
    i = GA.QI_I
    for v in (E[0], NI, GA.add(E[1], E[4])):
        for j in range(4):
            for k in range(4):
                ok = ok and bform(v, mul(I6, CB[j]), CB[k]) == i * bform(v, CB[j], CB[k])
                ok = ok and bform(v, CB[k], CB[j]) == -bform(v, CB[j], CB[k])
    for v in POLAR:
        ok = ok and pf(bmat(v)) == GA.qi(-dot(v, v) / 16)
    for lam in LAMS:
        Ig = GA.add(NI, GA.scal(lam / 6, N0))
        eps = -16 * pf(bmat(Ig))
        ok = ok and eps == GA.qi(lam / 3) and eps == GA.qi(dot(Ig, Ig))
    # by hand: Lambda = 3/2 gives eps(I ^ I) = 1/2
    ok = ok and -16 * pf(bmat(GA.add(NI, GA.scal(F(1, 4), N0)))) == GA.qi(F(1, 2))
    GA.check("infinity bivector: eps(Psi(I_g) ^ Psi(I_g)) = Q(I_g) = Lambda/3", ok)
    assert ok


def check_infinity_bivector_simple_iff_lambda_zero():
    premise("correspondence.spinor-identification")
    premise("correspondence.imported-vacuum-equations-scale-tractor")
    ok = GA.field_rank(bmat(NI)) == 2
    for lam in LAMS:
        ok = ok and GA.field_rank(bmat(GA.add(NI, GA.scal(lam / 6, N0)))) == 4
    for v in NULLS:
        ok = ok and dot(v, v) == 0 and GA.field_rank(bmat(v)) == 2
    for v in (E[0], E[3], GA.add(E[0], E[4]), GA.add(N0, NI)):
        ok = ok and GA.field_rank(bmat(v)) == 4
    # the infinity line: ker(ninf) on CS (complex dimension 2) is the radical of b_ninf
    real = CB + [mul(I6, c) for c in CB]
    cols = [GA.basis_vector_of(mul(NI, c), BLADES) for c in real]
    M = [row for row in ([cols[j][r] for j in range(8)] for r in range(len(BLADES))) if any(row)]
    ker = [GA.add(*[GA.scal(k[j], real[j]) for j in range(8) if k[j]]) for k in GA.field_kernel(M)]
    ok = ok and len(ker) == 4 and rank(ker) == 4
    for w in ker:
        for k in range(4):
            ok = ok and bform(NI, CB[k], w) == GA.qi(0)
    GA.check("infinity bivector is simple exactly at Lambda = 0, with plane ker(ninf)", ok)
    assert ok


def check_constancy_in_three_languages():
    premise("correspondence.spinor-identification")
    premise("correspondence.imported-vacuum-equations-scale-tractor")
    ok = True
    bivs = [theta(vec(a), smap(PNON)) for a in BIV_DIRS] + OMS
    for B in bivs:
        for v in VS:
            for j in range(len(CB)):
                for k in range(len(CB)):
                    lhs = (bform(comm(B, v), CB[j], CB[k])
                           + bform(v, GA.scal(F(1, 2), mul(B, CB[j])), CB[k])
                           + bform(v, CB[j], GA.scal(F(1, 2), mul(B, CB[k]))))
                    ok = ok and lhs == GA.qi(0)
    # Einstein: P = (Lambda/6) id with I = ninf + (Lambda/6) n0 -> the induced derivative of Psi(I) is zero
    lam = LAM_E
    Ig = GA.add(NI, GA.scal(lam / 6, N0))
    pe = lambda A: GA.scal(lam / 6, A)
    moved = False
    for a in DIRS:
        for P, einstein in ((pe, True), (smap(PNON), False)):
            Bt = GA.add(OM_E, theta(vec(a), P))
            vals = [bform(Ig, GA.scal(F(1, 2), mul(Bt, CB[j])), CB[k]) + bform(Ig, CB[j], GA.scal(F(1, 2), mul(Bt, CB[k])))
                    for j in range(len(CB)) for k in range(len(CB))]
            zero = all(x == GA.qi(0) for x in vals)
            ok = ok and zero == GA.is_zero(comm(Bt, Ig))
            if einstein:
                ok = ok and zero
            else:
                moved = moved or not zero
    ok = ok and moved
    GA.check("field equations, tractor parallelism and infinity-bivector constancy coincide", ok)
    assert ok
