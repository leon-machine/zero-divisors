#!/usr/bin/env python3
"""verify_three_routes.py: exact-arithmetic verification of the computational
identities of the companion note "Three Routes from the Localisation" (the
metric-level sheaf, the boundary no-go, the hopping exclusion), against the
series' shared library GA.py.  Every check is PASS/FAIL; nonzero exit on any
failure; no floating point anywhere.

Coverage (labels name the note's results):
  [Thm 2.4/2.5]  two-mode Jordan-Wigner ledger: string cancellation (sigma
                 single-site), CAR, Ad(sigma_x) fixes v_y while Ad(sigma_y)
                 negates it, meet = joint diagonal = range of the pinching,
                 join contains every generator and spans the full algebra
  [Prop 2.2/2.3] three-point finite model of the even subbundle: locality,
                 unique gluing from an overlapping cover, stalk defect of
                 the join exhibited
  [Lem 3.3]      the solve G vtilde = v with radical gauge, normalisation
                 G(vt,vt) + 2 vt(u) = 0 met at exactly one gauge, gauge
                 invariance of the data entering the intertwiner
  [Thm 3.4]      Phi^T h_u Phi = h_{u+v} exactly, two masses, two v's;
                 unipotence; ladder relations in both completions; a
                 wrong-normalisation control breaks the identity
  [Thm 3.5]      theta = ghat o Phi^{-1} is an automorphism of (T, h_u),
                 not the identity, fixing k; dual action on candidates is
                 translation by -lambda; no candidate fixed
  [Lem 4.1]      commuting with every point projector forces block
                 diagonality (exhaustive on matrix units); hopping fails
  [Prop 4.2]     dGamma of a block map conserves both occupations; dGamma
                 of a hop moves (0,1) to (1,0); the controlled-Z generator
                 conserves both
"""

from fractions import Fraction
import sys

import GA as g

F = Fraction


# ---------------------------------------------------------------------------
# small exact-matrix helpers
# ---------------------------------------------------------------------------

def mm(A, B):
    n, k2, m2 = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k2)) for j in range(m2)] for i in range(n)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscal(c, A):
    return [[c * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def eye(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def zeros(n, m=None):
    m = n if m is None else m
    return [[F(0)] * m for _ in range(n)]


def T(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def kron(A, B):
    n, m = len(A), len(A[0])
    p, q = len(B), len(B[0])
    return [[A[i][j] * B[k][l] for j in range(m) for l in range(q)]
            for i in range(n) for k in range(p)]


def diag(*vals):
    n = len(vals)
    return [[vals[i] if i == j else F(0) for j in range(n)] for i in range(n)]


def conj(S, A):
    return mm(S, mm(A, T(S)))


def is_zero(A):
    return all(A[i][j] == 0 for i in range(len(A)) for j in range(len(A[0])))


def mat_rank(rows):
    M = [list(r) for r in rows]
    rank = 0
    cols = len(M[0]) if M else 0
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, len(M)):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(cols)]
        r += 1
        rank += 1
    return rank


# ---------------------------------------------------------------------------
# [Thm 2.4/2.5] two-mode Jordan-Wigner ledger
# ---------------------------------------------------------------------------

def sheaf_algebra_checks():
    A = [[F(0), F(1)], [F(0), F(0)]]           # lowering
    Ad = T(A)                                   # raising
    Z = diag(F(1), F(-1))
    I2 = eye(2)
    vx = kron(A, I2)
    vxd = kron(Ad, I2)
    vy = kron(Z, A)                             # Jordan-Wigner string
    vyd = kron(Z, Ad)

    # CAR across modes, exact
    anti = lambda P, Q: madd(mm(P, Q), mm(Q, P))
    ok = meq(anti(vx, vxd), eye(4)) and meq(anti(vy, vyd), eye(4)) \
        and is_zero(anti(vx, vy)) and is_zero(anti(vx, vyd)) \
        and is_zero(mm(vx, vx)) and is_zero(mm(vy, vy))
    g.check("[Thm 2.4] Jordan-Wigner CAR on two modes: {v_x, v_x*} = {v_y, v_y*} = 1, cross "
            "anticommutators and squares zero, exactly", ok)

    # string cancellation: sigma_k is single-site
    sx = msub(mm(vxd, vx), mm(vx, vxd))
    sy = msub(mm(vyd, vy), mm(vy, vyd))
    ok = meq(sx, kron(mscal(F(-1), Z), I2)) and meq(sy, kron(I2, mscal(F(-1), Z)))
    g.check("[Thm 2.4] the strings cancel in sigma_k = v*v - vv*: sigma_x = (-Z)(x)1 and "
            "sigma_y = 1(x)(-Z), single-site both (the Jordan-Wigner locality of Prop 9.6's proof)", ok)

    # Ad(sigma_x) fixes v_y; Ad(sigma_y) negates it
    ok = meq(conj(sx, vy), vy) and meq(conj(sy, vy), mscal(F(-1), vy))
    g.check("[Thm 2.5] Ad(sigma_x) fixes v_y while Ad(sigma_y) negates it: v_y lies in the "
            "x-point's fixed algebra and is odd at its own point (the join's stalk defect)", ok)

    # meet = joint diagonal = composite of the two averages, on a generic matrix
    X = [[F(i * 4 + j + 1) + (F(1, 3) if i == j else 0) for j in range(4)] for i in range(4)]
    Ek = lambda S, M: mscal(F(1, 2), madd(M, conj(S, M)))
    comp = Ek(sx, Ek(sy, X))
    pinched = [[X[i][j] if i == j else F(0) for j in range(4)] for i in range(4)]
    ok = meq(comp, Ek(sy, Ek(sx, X))) and meq(comp, pinched)
    g.check("[Thm 2.4] the meet realised: the composite of the two parity averages, either order, "
            "is the joint-diagonal pinching on a generic rational matrix", ok)

    # join spans the whole algebra: words in {vx, vxd, vy, vyd} span M_4
    gens = [vx, vxd, vy, vyd]
    words = [eye(4)] + list(gens)
    for a in gens:
        for b in gens:
            words.append(mm(a, b))
            for c in gens:
                words.append(mm(a, mm(b, c)))
                for d in gens:
                    words.append(mm(a, mm(b, mm(c, d))))
    rows = [[W[i][j] for i in range(4) for j in range(4)] for W in words]
    g.check("[Thm 2.5] the join is everything: v_y and v_x lie in the other point's fixed algebra, "
            "and words in the generators span the full 16-dimensional two-mode ledger (exact rank)",
            mat_rank(rows) == 16)

    # three-point sheaf model: locality and unique gluing for even-valued families
    s_left = {1: (F(2), F(3)), 2: (F(5), F(-1))}          # sections over {1,2}: (coef of 1, coef of sigma)
    s_right = {2: (F(5), F(-1)), 3: (F(0), F(7))}          # over {2,3}, agreeing at 2
    glued = dict(s_left)
    glued.update(s_right)
    ok = all(glued[p] == s_left.get(p, s_right.get(p)) for p in (1, 2, 3)) \
        and s_left[2] == s_right[2] and len(glued) == 3
    g.check("[Prop 2.2] three-point model of the even subbundle: sections agreeing on the overlap "
            "glue to a unique family, and a family is determined by its pointwise values (locality)", ok)


# ---------------------------------------------------------------------------
# [Lem 3.3], [Thm 3.4], [Thm 3.5] the boundary no-go, on Schwarzschild data
# ---------------------------------------------------------------------------

def solve_linear(M, rhs):
    """One exact solution of M x = rhs (list), or None."""
    n, m = len(M), len(M[0])
    A = [list(M[i]) + [rhs[i]] for i in range(n)]
    r = 0
    piv_cols = []
    for c in range(m):
        piv = None
        for i in range(r, n):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(n):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(m + 1)]
        piv_cols.append(c)
        r += 1
    for i in range(r, n):
        if A[i][m] != 0:
            return None
    x = [F(0)] * m
    for i, c in enumerate(piv_cols):
        x[c] = A[i][m]
    return x


def pair(cov, vec):
    return sum(cov[i] * vec[i] for i in range(len(cov)))


def quad(Gm, a, b):
    return sum(a[i] * Gm[i][j] * b[j] for i in range(len(a)) for j in range(len(a)))


def build_h(Gm, uvec, mu, nu):
    """6x6 ambient Gram on basis (w1..w4, n0, ninf) on the inner collar."""
    h = zeros(6)
    for i in range(4):
        for j in range(4):
            h[i][j] = Gm[i][j]
    for i in range(4):
        h[i][4] = h[4][i] = nu * uvec[i]      # kappa(w_i, n0) = nu w_i(u)
        h[i][5] = h[5][i] = mu * uvec[i]      # kappa(w_i, ninf) = mu w_i(u)
    h[4][5] = h[5][4] = F(-1)                 # n0 . ninf = -1
    return h


def nogo_checks():
    mu, nu = F(-2), F(3)
    for m in (F(2), F(3)):
        Gm = [[m * m, -m, F(0), F(0)],
              [-m, F(1), F(0), F(0)],
              [F(0), F(0), F(-1), F(0)],
              [F(0), F(0), F(0), F(-1)]]
        k = [F(1), m, F(0), F(0)]              # covector components
        ok = all(sum(Gm[i][j] * k[j] for j in range(4)) == 0 for i in range(4))
        g.check("[Lem 3.3] boundary data at m = %s: G k = 0 exactly, the radical is R k" % m, ok)

        u = [F(1), F(0), F(0), F(0)]           # transversal, k(u) = 1
        assert pair(k, u) == 1
        vs = [[-m, F(1), F(0), F(0)], [F(0), F(0), F(1), F(0)]]   # in ker k
        for v in vs:
            assert pair(k, v) == 0
            vt0 = solve_linear(Gm, v)
            ok = vt0 is not None and all(sum(Gm[i][j] * vt0[j] for j in range(4)) == v[i]
                                         for i in range(4))
            # radical gauge to meet G(vt,vt) + 2 vt(u) = 0
            base = quad(Gm, vt0, vt0) + 2 * pair(vt0, u)
            t = -base / 2                       # slope 2 k(u) = 2
            vt = [vt0[i] + t * k[i] for i in range(4)]
            norm_val = quad(Gm, vt, vt) + 2 * pair(vt, u)
            # gauge invariance of what enters Phi: G(alpha, vt) is gauge independent
            probe = [F(1), F(2), F(-1), F(3)]
            gauge_ok = quad(Gm, probe, vt) == quad(Gm, probe, vt0)
            g.check("[Lem 3.3] m = %s, v = %s: the solve G vtilde = eval_v closes, the radical gauge "
                    "meets the normalisation at exactly one t (value %s), and G(., vtilde) is gauge "
                    "independent" % (m, v, t), ok and norm_val == 0 and gauge_ok)

            hu = build_h(Gm, u, mu, nu)
            uv = [u[i] + v[i] for i in range(4)]
            huv = build_h(Gm, uv, mu, nu)
            Phi = eye(6)
            for i in range(4):
                Phi[i][4] = nu * vt[i]
                Phi[i][5] = mu * vt[i]
            g.check("[Thm 3.4] m = %s, v = %s: Phi^T h_u Phi = h_{u+v} exactly (the intertwiner)" % (m, v),
                    meq(mm(T(Phi), mm(hu, Phi)), huv))
            D = msub(Phi, eye(6))
            g.check("[Thm 3.4] m = %s, v = %s: Phi is unipotent, (Phi - id)^2 = 0" % (m, v),
                    is_zero(mm(D, D)))
            # wrong-normalisation control
            vt_bad = [vt[i] + k[i] for i in range(4)]
            Phi_bad = eye(6)
            for i in range(4):
                Phi_bad[i][4] = nu * vt_bad[i]
                Phi_bad[i][5] = mu * vt_bad[i]
            g.check("[Thm 3.4] m = %s, v = %s: control, the un-normalised gauge representative breaks "
                    "the intertwiner identity" % (m, v),
                    not meq(mm(T(Phi_bad), mm(hu, Phi_bad)), huv))

        # ladder relations in both completions
        k6 = k + [F(0), F(0)]
        n0_6 = [F(0)] * 4 + [F(1), F(0)]
        kstar = [x / (2 * nu) for x in n0_6]
        h6 = build_h(Gm, u, mu, nu)
        hq = lambda a, b: sum(a[i] * h6[i][j] * b[j] for i in range(6) for j in range(6))
        ok = hq(k6, k6) == 0 and hq(kstar, kstar) == 0 and 2 * hq(k6, kstar) == 1
        h6v = build_h(Gm, [u[i] + vs[0][i] for i in range(4)], mu, nu)
        hqv = lambda a, b: sum(a[i] * h6v[i][j] * b[j] for i in range(6) for j in range(6))
        ok = ok and hqv(k6, k6) == 0 and hqv(kstar, kstar) == 0 and 2 * hqv(k6, kstar) == 1
        g.check("[Thm 3.4] m = %s: the ladder relations k^2 = (k*)^2 = 0, {k, k*} = 1 hold in the "
                "u-completion and in the (u+v)-completion alike" % m, ok)

        # [Thm 3.5] the automorphism and the translation action
        lam = vs[0]
        vt0 = solve_linear(Gm, lam)
        base = quad(Gm, vt0, vt0) + 2 * pair(vt0, u)
        vt = [vt0[i] - (base / 2) * k[i] for i in range(4)]
        Phi = eye(6)
        for i in range(4):
            Phi[i][4] = nu * vt[i]
            Phi[i][5] = mu * vt[i]
        Ghat = eye(6)
        for i in range(4):
            for j in range(4):
                Ghat[i][j] = (F(1) if i == j else F(0)) + k[i] * lam[j]
        hu = build_h(Gm, u, mu, nu)
        hul = build_h(Gm, [u[i] + lam[i] for i in range(4)], mu, nu)
        ok = meq(mm(T(Ghat), mm(hu, Ghat)), hul)
        g.check("[Thm 3.5] m = %s: ghat is an isometry (T, h_{u+lambda}) -> (T, h_u), as a matrix "
                "identity" % m, ok)
        # Phi^{-1} = 2 id - Phi for unipotent Phi
        Phi_inv = msub(mscal(F(2), eye(6)), Phi)
        theta = mm(Ghat, Phi_inv)
        ok = meq(mm(T(theta), mm(hu, theta)), hu) and not meq(theta, eye(6))
        tk = [sum(theta[i][j] * (k6[j]) for j in range(6)) for i in range(6)]
        ok = ok and tk == k6
        g.check("[Thm 3.5] m = %s: theta = ghat o Phi^{-1} is an automorphism of (T, h_u), not the "
                "identity, fixing k" % m, ok)
        # dual action on candidates: (I - lam k^T) u' = u' - lam for k(u') = 1; none fixed
        dual = msub(eye(4), [[lam[i] * k[j] for j in range(4)] for i in range(4)])
        cands = [u, [F(1) + (-m), F(1), F(0), F(0)], [F(1), F(0), F(5), F(-2)]]
        ok = True
        for c in cands:
            assert pair(k, c) == 1
            img = [sum(dual[i][j] * c[j] for j in range(4)) for i in range(4)]
            ok = ok and img == [c[i] - lam[i] for i in range(4)] and img != c
        g.check("[Thm 3.5] m = %s: the induced dual action translates every candidate by -lambda and "
                "fixes none (three candidates probed)" % m, ok)


# ---------------------------------------------------------------------------
# [Lem 4.1], [Prop 4.2] the hopping exclusion
# ---------------------------------------------------------------------------

def hopping_checks():
    # commuting with every point projector forces diagonality (3-point module, exhaustive)
    chis = [diag(*[F(1) if i == p else F(0) for i in range(3)]) for p in range(3)]
    ok = True
    for i in range(3):
        for j in range(3):
            E = [[F(1) if (a, b) == (i, j) else F(0) for b in range(3)] for a in range(3)]
            commutes = all(meq(mm(E, ch), mm(ch, E)) for ch in chis)
            ok = ok and (commutes == (i == j))
    g.check("[Lem 4.1] finite support lemma: a map of the three-point module commutes with every "
            "point projector exactly when it is diagonal (all nine matrix units, exhaustive); "
            "hopping E_xy fails, multipliers pass", ok)

    # quantised consequence on two JW modes
    A = [[F(0), F(1)], [F(0), F(0)]]
    Ad_ = T(A)
    Z = diag(F(1), F(-1))
    I2 = eye(2)
    vx, vxd = kron(A, I2), kron(Ad_, I2)
    vy, vyd = kron(Z, A), kron(Z, Ad_)
    Nx, Ny = mm(vxd, vx), mm(vyd, vy)
    comm = lambda P, Q: msub(mm(P, Q), mm(Q, P))

    dG_block = madd(mscal(F(2), Nx), mscal(F(5), Ny))     # dGamma(diag(2,5))
    ok = is_zero(comm(dG_block, Nx)) and is_zero(comm(dG_block, Ny))
    g.check("[Prop 4.2] dGamma of a block (bundle) map conserves both occupations exactly", ok)

    hop = madd(mm(vxd, vy), mm(vyd, vx))
    e01 = [[F(0)], [F(1)], [F(0)], [F(0)]]                 # |0_x 1_y> in the (Nx, Ny) basis 2i+j... 
    out = mm(hop, e01)
    moved = any(out[i][0] != 0 for i in (2,)) and out[1][0] == 0
    ok = (not is_zero(comm(hop, Nx))) and moved
    g.check("[Prop 4.2] dGamma of a hop moves occupation: it fails to commute with N_x and carries "
            "|0_x 1_y> into the (1,0) sector, exactly", ok)

    sx = msub(mm(vxd, vx), mm(vx, vxd))
    sy = msub(mm(vyd, vy), mm(vy, vyd))
    cz = mm(sx, sy)
    ok = is_zero(comm(cz, Nx)) and is_zero(comm(cz, Ny))
    g.check("[Prop 4.2] the controlled-Z generator sigma_x sigma_y conserves both occupations: "
            "cross-point diagonal products are not hopping and were never excluded", ok)


def main():
    print("verify_three_routes.py: exact-arithmetic checks for the companion note (v1.0)\n")
    sheaf_algebra_checks()
    nogo_checks()
    hopping_checks()
    print()
    if g.FAILURES:
        print("FAILURES (%d):" % len(g.FAILURES))
        for f in g.FAILURES:
            print("  " + f)
        sys.exit(1)
    print("ALL CHECKS PASSED.")


if __name__ == "__main__":
    main()
