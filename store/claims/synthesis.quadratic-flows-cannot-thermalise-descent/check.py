"""synthesis.quadratic-flows-cannot-thermalise-descent: exact checks.

(1) CAR from null pairs in Cl(3,3) (GA engine): a_j = (e_j + f_j)/2, a_j^+ = (e_j - f_j)/2 with
    e_j^2 = +1, f_j^2 = -1. For a generic rational symmetric one-particle matrix k the quadratic
    generator X = sum k_ij a_i^+ a_j commutes with every Q_n = sum (k^n)_ij a_i^+ a_j; the boost
    generator H_F = sum w_j N_j commutes with each N_j, and so does H_F plus any product sigma_j sigma_k
    (the number-diagonal generators (L_E) permits); an occupation-moving quartic term does not.
(2) One-particle level over Q(i): the Cayley unitary U = (1 - i s k)(1 + i s k)^(-1) is exactly
    unitary; C -> U C U^+ preserves tr(k^n C) and tr(C^m), so occupations of k's eigenmodes and the
    correlation spectrum are frozen; under the boost flow (k diagonal) the occupations n_j are frozen
    and the coherences only rotate. A descent state with n_j != FD(w_j) never reaches the I-state.
(3) A pure two-mode Bogoliubov pair c|00> + s|11> restricts to the Gibbs state of one mode with
    e^(-beta w) = s^2/c^2: the Fermi-Dirac occupations are reached by restriction, not by evolution.
"""
from fractions import Fraction as F
from GA import mul, add, sub, scal, sc, gen, eq, QI, field_solve
from tp_premise import premise

NM = 3
SQ = (1, 1, 1, -1, -1, -1)


def a(j):
    return scal(F(1, 2), add(gen(j), gen(NM + j)))


def ad(j):
    return scal(F(1, 2), sub(gen(j), gen(NM + j)))


def comm(x, y):
    return sub(mul(x, y, SQ), mul(y, x, SQ))


def acomm(x, y):
    return add(mul(x, y, SQ), mul(y, x, SQ))


def bil(k):
    out = {}
    for i in range(NM):
        for j in range(NM):
            if k[i][j] != 0:
                out = add(out, scal(F(k[i][j]), mul(ad(i), a(j), SQ)))
    return out


def mm(A, B):
    n = len(A)
    return [[sum((A[i][l] * B[l][j] for l in range(n)), A[0][0] * 0) for j in range(n)] for i in range(n)]


def ident(n, one):
    return [[one if i == j else one * 0 for j in range(n)] for i in range(n)]


K = [[F(1), F(2), F(0)], [F(2), F(-1), F(3)], [F(0), F(3), F(2)]]


def check_conserved_quadratic_charges():
    premise("hawking.imported-algebra-boundary-modes-car-algebra")
    premise("scrambling.clock-inventory-boundary-modes")
    premise("singularity.number-diagonal-dynamics-models-scrambling-derived")
    for i in range(NM):
        for j in range(NM):
            assert eq(acomm(a(i), ad(j)), sc(F(1)) if i == j else {})
            assert eq(acomm(a(i), a(j)), {})
    X = bil(K)
    P = ident(NM, F(1))
    for n in range(4):                                   # Q_0 = total number, Q_1 = X, Q_2, Q_3
        assert eq(comm(X, bil(P)), {})
        P = mm(P, K)
    N1 = mul(ad(0), a(0), SQ)
    # [X_k, N_1] = X_[k, E_11]: the hop k_12 = 2 moves the site occupation
    assert eq(comm(X, N1), bil([[F(0), F(-2), F(0)], [F(2), F(0), F(0)], [F(0), F(0), F(0)]]))
    assert eq(comm(bil([[K[i][j] for j in range(NM)] for i in range(NM)]), bil(mm(K, K))), {})
    assert K[0][1] == 2 and K[1][2] == 3 and K[1][1] == -1   # the generic k used throughout
    W = [F(1), F(3), F(7)]                                # boost flow: H_F = sum w_j N_j
    HF = bil([[W[i] if i == j else F(0) for j in range(NM)] for i in range(NM)])
    for j in range(NM):
        assert eq(comm(HF, mul(ad(j), a(j), SQ)), {})
    # number-diagonal products (sigma_j sigma_k = (2N_j - 1)(2N_k - 1), the class (L_E) permits)
    # conserve every N_l, alone or added to the boost generator
    sig = [sub(scal(F(2), mul(ad(j), a(j), SQ)), sc(F(1))) for j in range(NM)]
    for j in range(NM):
        for k in range(j + 1, NM):
            ss = mul(sig[j], sig[k], SQ)
            for l in range(NM):
                assert eq(comm(add(HF, ss), mul(ad(l), a(l), SQ)), {})
    # an occupation-moving quartic term (hop between modes 1 and 2 weighted by N_3) does not:
    hop = add(mul(ad(0), a(1), SQ), mul(ad(1), a(0), SQ))
    Vh = mul(hop, mul(ad(2), a(2), SQ), SQ)
    assert not eq(comm(add(HF, Vh), N1), {})
    # [hop N_3, N_1] = (a2^+ a1 - a1^+ a2) N_3, exactly
    expect = mul(sub(mul(ad(1), a(0), SQ), mul(ad(0), a(1), SQ)), mul(ad(2), a(2), SQ), SQ)
    assert eq(comm(Vh, N1), expect)
    return True


def herm(A):
    n = len(A)
    return [[A[j][i].conj() for j in range(n)] for i in range(n)]


def trace(A):
    return sum((A[i][i] for i in range(len(A))), QI(0))


def cayley(k, s):
    n = len(k)
    I = ident(n, QI(1))
    iks = [[QI(0, s * k[i][j]) for j in range(n)] for i in range(n)]
    num = [[I[i][j] - iks[i][j] for j in range(n)] for i in range(n)]
    den = [[I[i][j] + iks[i][j] for j in range(n)] for i in range(n)]
    # U = num den^(-1): solve den^T column by column via field_solve on rows
    cols = []
    for c in range(n):
        e = [I[r][c] for r in range(n)]
        cols.append(field_solve(den, e))
    dinv = [[cols[c][r] for c in range(n)] for r in range(n)]
    return mm(num, dinv)


def check_occupations_frozen():
    premise("hawking.i-state")
    premise("synthesis.phase-flow-is-time-rotor-flow-kms-continuation")
    # a non-equilibrium quasi-free descent state: occupations (1/2, 0, 1/3) with coherences
    C = [[QI(F(1, 2)), QI(F(1, 5), F(1, 7)), QI(F(0))],
         [QI(F(1, 5), F(-1, 7)), QI(F(0)), QI(F(1, 9))],
         [QI(F(0)), QI(F(1, 9)), QI(F(1, 3))]]
    # (a) boost flow, k = diag(w): occupations frozen, coherences rotate by unimodular phases
    Wd = [F(1), F(3), F(7)]
    kd = [[Wd[i] if i == j else F(0) for j in range(NM)] for i in range(NM)]
    fd = [F(1, 4), F(1, 8), F(1, 16)]                     # I-state at e^(beta w_j) = 3, 7, 15
    for j, eb in enumerate((3, 7, 15)):
        assert fd[j] == F(1, 1 + eb)
    U0 = cayley(kd, F(1, 2))                              # Cayley phases (1 - i w/2)/(1 + i w/2)
    assert [U0[j][j] for j in range(NM)] == [QI(F(3, 5), F(-4, 5)), QI(F(-5, 13), F(-12, 13)),
                                             QI(F(-45, 53), F(-28, 53))]
    assert mm(mm(U0, C), herm(U0))[0][1] == QI(F(-7, 325), F(557, 2275))
    for s in (F(1, 2), F(2), F(5, 3)):
        U = cayley(kd, s)
        UU = mm(U, herm(U))
        assert all(UU[i][j] == (QI(1) if i == j else QI(0)) for i in range(NM) for j in range(NM))
        Ct = C
        for step in range(3):
            Ct = mm(mm(U, Ct), herm(U))
            for j in range(NM):
                assert Ct[j][j] == C[j][j]                # n_j(t) = n_j(0)
                assert Ct[j][j] != QI(fd[j])              # never the Fermi-Dirac value
            z = Ct[0][1]
            assert z * z.conj() == C[0][1] * C[0][1].conj()   # coherence modulus kept
        assert mm(mm(U, C), herm(U))[0][1] != C[0][1]     # but its phase moves (w_1 != w_2)
    # (b) generic quadratic flow k: tr(k^n C) and tr(C^m) are invariants
    kq = [[QI(x) for x in row] for row in K]
    U = cayley(K, F(1, 3))
    UU = mm(U, herm(U))
    assert all(UU[i][j] == (QI(1) if i == j else QI(0)) for i in range(NM) for j in range(NM))
    Ct = mm(mm(U, C), herm(U))
    P = ident(NM, QI(1))
    for n in range(NM + 1):
        assert trace(mm(P, Ct)) == trace(mm(P, C))
        P = mm(P, kq)
    Cm, Ctm = C, Ct
    for m in range(1, NM + 1):
        assert trace(Ctm) == trace(Cm)
        Cm, Ctm = mm(Cm, C), mm(Ctm, Ct)
    assert Ct[0][0] != C[0][0]                            # site occupations do move
    assert Ct[0][0] == QI(F(73147, 214550))
    assert trace(mm(mm(kq, kq), C)) == QI(F(15, 2))
    return True


def check_thermofield_restriction():
    premise("hawking.i-state")
    for c, s in ((F(4, 5), F(3, 5)), (F(12, 13), F(5, 13)), (F(15, 17), F(8, 17))):
        assert c * c + s * s == 1
        # basis |00>, |01>, |10>, |11> (mode 1, partner); psi = c|00> + s|11>
        psi = [c, F(0), F(0), s]
        rho = [[psi[i] * psi[j] for j in range(4)] for i in range(4)]
        red = [[rho[0][0] + rho[1][1], rho[0][2] + rho[1][3]],
               [rho[2][0] + rho[3][1], rho[2][2] + rho[3][3]]]
        assert red[0][1] == 0 and red[1][0] == 0          # gauge invariant: no coherence
        n = red[1][1]
        boltz = s * s / (c * c)                           # e^(-beta w)
        assert red[1][1] / red[0][0] == boltz             # Gibbs ratio of a single mode
        assert n == 1 / (1 / boltz + 1)                   # Fermi-Dirac occupation
    return True
