"""synthesis.two-loop-running-cannot-fix-majorana-coupling: exact checks.

Fermions are two-component (Weyl), kappa = 1/2, Yukawas in the form -L > (1/2) Y^a_jk psi_j psi_k phi_a + h.c.
with real scalars phi_a (the imported two-loop Fact). A complex scalar component Phi_c = (phi_c1 + i phi_c2)/sqrt2
with coupling -L > (1/2) (y (x) T^c)_jk psi_j psi_k Phi_c (Majorana type) or (y (x) T^c)_(psi)(psi^c) psi psi^c Phi_c
(Dirac type) gives sum_a Y^a Y^a^dag = y y^dag (x) sum_c T^c T^c^dag, T^c an orthonormal basis of the scalar's
components inside the fermion bilinear. Gauge indices: SU(4) a in 0..3, SU(2) alpha in 0..1; psi = (4,2,1),
psi^c = (4b,1,2), each 8 components (a, alpha).
(1) sum_c T^c T^c^dag is a multiple of the unit on the 8 components, computed from explicit bases: (10,1,3)
    in Sym(psi^c psi^c): 30/8; (1,2,2) in psi psi^c: 4/8; (15,2,2) in psi psi^c: 60/8.
(2) Y_4^i = Tr[C_2^i(F) Y Y^dag]/d(G_i) per unit family trace, with C_2 from the stored Casimirs:
    (10,1,3): (15/4, 0, 15/2) in (4, 2L, 2R); Dirac type: (1/4) dim R (1, 1, 1). Matched at M_I with
    a_1 = (3/5) a_2R + (2/5) a_4: (6, 0, 15/4) and (1/4) dim R (1, 1, 1).
(3) The running a_i(M_Z) = a_U + b_i^SM x + (b_i^eff - eps v_i) y + u (u a universal shift) is linear in
    (a_U, x, y) at each eps; det(eps) is affine in eps with the stated D0 and positive on the grid
    eps in {0, 1/8, ..., 3} (eps <= 3 is singular values of f at most 4 pi); the solution back-substitutes and
    x increases strictly with eps; a universal shift u moves a_U only.
(4) Sensitivities at the one-loop baseline with certified bounds on pi: d ln M_I / d Tr(f f^dag) and the move
    of ln M_I for alpha_s -> alpha_s +- 9/10000; with M_I given, the alpha_s band in Tr(f f^dag).
"""
from fractions import Fraction as F

import GA
import series
from tp_premise import premise

H = F(1, 2)
SM_GROUPS = [("U1",), ("SU", 2), ("SU", 3)]
PS_GROUPS = [("SU", 4), ("SU", 2), ("SU", 2)]
GEN = [((F(1, 6), "N", "N"), 1), ((F(-1, 2), "N", "1"), 1), ((F(-2, 3), "1", "Nb"), 1),
       ((F(1, 3), "1", "Nb"), 1), ((F(1), "1", "1"), 1), ((F(0), "1", "1"), 1)]
SM_WEYL = [(r, 3 * m) for r, m in GEN]
SM_SCALAR = [((H, "N", "1"), 1)]
PS_WEYL = [(("N", "N", "1"), 3), (("Nb", "1", "N"), 3)]
CHAINS = {
    "real": [(("1", "N", "N"), H), (("sym", "1", "adj"), 1)],
    "complex": [(("1", "N", "N"), 1), (("sym", "1", "adj"), 1)],
    "complex15": [(("1", "N", "N"), 1), (("sym", "1", "adj"), 1), (("adj", "N", "N"), 1)],
}
INPUTS = (F(128), F(2312, 10000), F(500, 59))
COMP = [(a, al) for a in range(4) for al in range(2)]   # the 8 components of psi or psi^c


def su_rep(N, name):
    if name == "1":
        return (1, F(0), F(0))
    if name in ("N", "Nb"):
        return (N, H, F(N * N - 1, 2 * N))
    if name == "adj":
        return (N * N - 1, F(N), F(N))
    return (N * (N + 1) // 2, F(N + 2, 2), F((N - 1) * (N + 2), N))


def data(groups, rep):
    dims, T, C = [], [], []
    for g, r in zip(groups, rep):
        if g[0] == "U1":
            dims.append(1)
            T.append(F(3, 5) * r * r)
            C.append(F(3, 5) * r * r)
        else:
            d, t, c = su_rep(g[1], r)
            dims.append(d)
            T.append(t)
            C.append(c)
    return dims, T, C


def weighted_T(groups, rep, i):
    dims, T, C = data(groups, rep)
    w = T[i]
    for k, d in enumerate(dims):
        if k != i:
            w *= d
    return w


def one_loop(groups, weyl, scal):
    CG = [F(0) if g[0] == "U1" else F(g[1]) for g in groups]
    b = []
    for i in range(len(groups)):
        tw = sum((m * weighted_T(groups, r, i) for r, m in weyl), F(0))
        ts = sum((m * weighted_T(groups, r, i) for r, m in scal), F(0))
        b.append(-F(11, 3) * CG[i] + F(2, 3) * tw + F(1, 3) * ts)
    return b


def record():
    A, s2, a3 = INPUTS
    a2 = s2 * A
    return [F(3, 5) * (A - a2), a2, a3]


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def cramer(M, a):
    d = det3(M)
    out = []
    for k in range(3):
        Mk = [[a[i] if j == k else M[i][j] for j in range(3)] for i in range(3)]
        out.append(det3(Mk) / d)
    return out, d


def match(v4, v2L, v2R):
    return [F(3, 5) * v2R + F(2, 5) * v4, v2L, v4]


# (1) explicit component bases ---------------------------------------------------------------------

def sum_TTdag(basis):
    """basis: list of dicts {(row_comp, col_comp): coeff} (unnormalised, mutually orthogonal);
    returns the 8 x 8 matrix sum_c T^c T^c^dag with T^c = B^c/|B^c| (rational: divide by |B^c|^2)."""
    S = {(r, s): F(0) for r in COMP for s in COMP}
    for B in basis:
        n2 = sum((c * c for c in B.values()), F(0))
        for (r, k), c in B.items():
            for (s, k2), c2 in B.items():
                if k == k2:
                    S[(r, s)] += c * c2 / n2
    return S


def gram_orthogonal(basis):
    for i in range(len(basis)):
        for j in range(i + 1, len(basis)):
            if sum((c * basis[j].get(k, F(0)) for k, c in basis[i].items()), F(0)) != 0:
                return False
    return True


def delta_R_basis():
    """(10,1,3): symmetric in the SU(4) pair and in the SU(2)_R pair, as a symmetric 8 x 8 matrix."""
    out = []
    for a in range(4):
        for b in range(a, 4):
            for al in range(2):
                for be in range(al, 2):
                    B = {}
                    for (p, q) in {(a, b), (b, a)}:
                        for (r, s) in {(al, be), (be, al)}:
                            B[((p, r), (q, s))] = F(1)
                    out.append(B)
    return out


def bidoublet_basis():
    """(1,2,2) in psi psi^c: delta_ab (x) E_(alpha, beta')."""
    return [{((a, al), (a, be)): F(1) for a in range(4)} for al in range(2) for be in range(2)]


def adj_basis():
    """(15,2,2) in psi psi^c: E_ab (a != b) and the diagonal traceless H_k = sum_{j<k} E_jj - k E_kk."""
    out = []
    for al in range(2):
        for be in range(2):
            for a in range(4):
                for b in range(4):
                    if a != b:
                        out.append({((a, al), (b, be)): F(1)})
            for k in range(1, 4):
                B = {((j, al), (j, be)): F(1) for j in range(k)}
                B[((k, al), (k, be))] = F(-k)
                out.append(B)
    return out


def is_unit_multiple(S, c):
    return all(S[(r, s)] == (c if r == s else F(0)) for r in COMP for s in COMP)


# checks ---------------------------------------------------------------------------------------------

def check_component_sums_are_unit_multiples():
    premise("standard-model.majorana-element")
    premise("standard-model.imported-pati-salam-representation-theory-survival")
    dR, bd, ad = delta_R_basis(), bidoublet_basis(), adj_basis()
    ok = len(dR) == 30 and len(bd) == 4 and len(ad) == 60
    ok = ok and gram_orthogonal(dR) and gram_orthogonal(bd) and gram_orthogonal(ad)
    ok = ok and is_unit_multiple(sum_TTdag(dR), F(30, 8))
    ok = ok and is_unit_multiple(sum_TTdag(bd), F(4, 8)) and is_unit_multiple(sum_TTdag(ad), F(60, 8))
    # the Dirac-type sums on the psi^c side (transpose) are the same multiples
    def transposed(basis):
        return [{(k, r): c for (r, k), c in B.items()} for B in basis]
    ok = ok and is_unit_multiple(sum_TTdag(transposed(bd)), F(4, 8))
    ok = ok and is_unit_multiple(sum_TTdag(transposed(ad)), F(60, 8))
    GA.check("sum_c T^c T^c^dag = (30/8, 4/8, 60/8) x unit for the (10,1,3), (1,2,2), (15,2,2)", ok)
    return ok


def yukawa_vectors():
    C4, C2 = su_rep(4, "N")[2], su_rep(2, "N")[2]
    d4, d2 = 15, 3
    # Majorana type (10,1,3): only psi^c couples; Tr over psi^c = 8 * (30/8) per unit Tr(f f^dag)
    tM = 8 * F(30, 8)
    maj = [C4 * tM / d4, F(0), C2 * tM / d2]
    dirac = {}
    for name, dimR in (("bidoublet", 4), ("adj15", 60)):
        t = 8 * F(dimR, 8)   # on each of psi and psi^c
        dirac[name] = [(C4 + C4) * t / d4, (C2 + 0) * t / d2, (0 + C2) * t / d2]
    return maj, dirac


def check_yukawa_casimir_vectors():
    premise("synthesis.imported-two-loop-yukawa-gauge-terms")
    premise("standard-model.majorana-element")
    premise("standard-model.matching-traces")
    maj, dirac = yukawa_vectors()
    ok = maj == [F(15, 4), F(0), F(15, 2)] and match(*maj) == [F(6), F(0), F(15, 4)]
    ok = ok and dirac["bidoublet"] == [F(1)] * 3 and dirac["adj15"] == [F(15)] * 3
    ok = ok and match(*dirac["bidoublet"]) == [F(1)] * 3 and match(*dirac["adj15"]) == [F(15)] * 3
    GA.check("Majorana Yukawa vector (15/4, 0, 15/2) -> (6, 0, 15/4); Dirac-type vectors universal", ok)
    return ok


def chain_system(k, eps, u=F(0), a=None):
    bSM = one_loop(SM_GROUPS, SM_WEYL, SM_SCALAR)
    bPS = one_loop(PS_GROUPS, PS_WEYL, CHAINS[k])
    beff = match(*bPS)
    v = match(*yukawa_vectors()[0])
    a = list(a or record())
    M = [[F(1), bSM[i], beff[i] - eps * v[i]] for i in range(3)]
    sol, d = cramer(M, [a[i] - u for i in range(3)])
    back = all(sol[0] + bSM[i] * sol[1] + (beff[i] - eps * v[i]) * sol[2] + u == a[i] for i in range(3))
    return sol, d, back


def check_running_family_never_fixes_eps():
    premise("standard-model.chain")
    premise("standard-model.spectrum-run")
    premise("standard-model.imported-coefficient-sum-indices")
    premise("synthesis.imported-two-loop-yukawa-gauge-terms")
    ok = True
    grid = [F(n, 8) for n in range(0, 25)]   # eps in [0, 3]
    for k in CHAINS:
        prev = None
        for e in grid:
            (aU, x, y), d, back = chain_system(k, e)
            ok = ok and back and d > 0 and x > 0 and y > 0
            if prev is not None:
                ok = ok and x > prev
            prev = x
        # a universal shift (Dirac-type Yukawas) moves alpha_U only
        (aU0, x0, y0), _, _ = chain_system(k, F(1, 10))
        (aU1, x1, y1), _, _ = chain_system(k, F(1, 10), u=F(7, 3))
        ok = ok and x1 == x0 and y1 == y0 and aU1 == aU0 - F(7, 3)
    # det is affine in eps with the stated D0 at eps = 0
    d0 = {k: chain_system(k, F(0))[1] for k in CHAINS}
    ok = ok and d0 == {"real": F(364, 15), "complex": F(386, 15), "complex15": F(114, 5)}
    bSM = one_loop(SM_GROUPS, SM_WEYL, SM_SCALAR)
    v = match(*yukawa_vectors()[0])
    slope = -det3([[F(1), bSM[i], v[i]] for i in range(3)])
    ok = ok and slope == F(201, 4)
    ok = ok and slope == -(v[2] * (bSM[1] - bSM[0]) + v[0] * (bSM[2] - bSM[1]))
    for k in CHAINS:
        da, db, dc = (chain_system(k, F(n))[1] for n in (0, 1, 2))
        ok = ok and da - 2 * db + dc == 0
        ok = ok and db - da == slope
    GA.check("det = D0 + (201/4) eps with 201/4 the same for every chain; for every eps in [0, 3] the measured couplings fix (a_U, x, y) uniquely; x rises with eps", ok)
    return ok


def dx_deps(k):
    """exact derivative of x at eps = 0 (x is a ratio of affine functions of eps)."""
    (aU0, x0, y0), d0, _ = chain_system(k, F(0))
    (aU1, x1, y1), d1, _ = chain_system(k, F(1))
    # x(eps) = (p0 + p1 eps)/(d0 - D1 eps); recover p1, D1
    D1 = d0 - d1
    p0 = x0 * d0
    p1 = x1 * d1 - p0
    return (p1 * d0 + p0 * D1) / (d0 * d0)


def check_sensitivities():
    premise("standard-model.chain")
    premise("standard-model.spectrum-run")
    premise("synthesis.imported-two-loop-yukawa-gauge-terms")
    p_lo, p_hi = series.pi_bounds()
    ok = True
    want = {"real": (F(9, 100), F(10, 100)), "complex": (F(8, 100), F(9, 100)), "complex15": (F(10, 100), F(11, 100))}
    for k, (lo, hi) in want.items():
        c = dx_deps(k)
        # d ln M_I / d Tr(f f^dag) = 2 pi dx/deps * 1/(16 pi^2) = c/(8 pi)
        ok = ok and c > 0 and lo < c / (8 * p_hi) and c / (8 * p_lo) < hi
        # alpha_s +- 9/10000 at eps = 0: |d ln M_I| between 3/100 and 5/100, of opposite sign to the alpha_s move
        A, s2, a3 = INPUTS
        x0 = chain_system(k, F(0))[0][1]
        for das in (F(9, 10000), F(-9, 10000)):
            rec = record()
            rec[2] = F(1) / (F(1) / a3 + das)
            xs = chain_system(k, F(0), a=rec)[0][1]
            dl_lo, dl_hi = 2 * p_lo * (xs - x0), 2 * p_hi * (xs - x0)
            if das > 0:
                ok = ok and -F(5, 100) < dl_lo and dl_hi < -F(3, 100)
            else:
                ok = ok and F(3, 100) < dl_lo and dl_hi < F(5, 100)
    GA.check("ln M_I rises by 0.08 to 0.11 per unit Tr(f f^dag); alpha_s +- 0.0009 moves it by 0.03 to 0.05", ok)
    return ok


def check_given_mi_alpha_s_band_in_trace():
    """If x (M_I) were supplied, the system is linear in (a_U, y, z = y eps): solve, then move alpha_s."""
    premise("standard-model.chain")
    premise("standard-model.spectrum-run")
    premise("synthesis.imported-two-loop-yukawa-gauge-terms")
    p_lo, p_hi = series.pi_bounds()
    bSM = one_loop(SM_GROUPS, SM_WEYL, SM_SCALAR)
    v = match(*yukawa_vectors()[0])
    ok = True
    for k in CHAINS:
        beff = match(*one_loop(PS_GROUPS, PS_WEYL, CHAINS[k]))
        e_true = F(1, 158)          # Tr(f f^dag) close to 1
        (aU, x, y), _, _ = chain_system(k, e_true)
        M = [[F(1), beff[i], -v[i]] for i in range(3)]
        A, s2, a3 = INPUTS
        eps_band = []
        for das in (F(0), F(9, 10000), F(-9, 10000)):
            rec = record()
            rec[2] = F(1) / (F(1) / a3 + das)
            (aU2, y2, z2), d = cramer(M, [rec[i] - bSM[i] * x for i in range(3)])
            eps_band.append(z2 / y2)
        ok = ok and eps_band[0] == e_true
        # the alpha_s 1 sigma band in Tr(f f^dag) = 16 pi^2 eps is wider than +-0.3 on each side
        for e in eps_band[1:]:
            ok = ok and abs(e - e_true) * 16 * p_lo * p_lo > F(3, 10)
    GA.check("with M_I given, alpha_s +- 0.0009 moves the inferred Tr(f f^dag) by more than 0.3", ok)
    return ok


if __name__ == "__main__":
    import sys
    r = [check_component_sums_are_unit_multiples(), check_yukawa_casimir_vectors(),
         check_running_family_never_fixes_eps(), check_sensitivities(), check_given_mi_alpha_s_band_in_trace()]
    sys.exit(0 if all(r) else 1)
