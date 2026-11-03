"""dark-energy.walls-free-sector: exact checks of the free sector at a corank-one wall of the soldering form.

Exact rational linear algebra on the component spaces of the Einstein-Cartan equations (frame indices
0..3, eta = diag(+, -, -, -), coordinates 0..3, epsilon_{abcd} with epsilon_{0123} = 1). The connection
equation is epsilon_{abcd} e^c ^ T^d (rows (a<b, triple)), the frame equation epsilon_{abcd} e^b ^ F^{cd}
(rows (a, triple)). Three corank-one normal forms, by the type of the wall's tangent space: Lorentzian
(e^3 = 0), Riemannian (e^0 = 0) and null (e^0 = e^1 = dx^0); for the null form the rows and columns are
re-expressed in the frame adapted to the dying direction (e = Q f, Q the null rotation), where ranks are
unchanged and vacated components become visible.
(a) Invertible coframe: the connection equation has rank 24 on the 24 torsion components and the frame
    equation rank 16 on the 36 curvature components. At each normal form: rank 18 (six torsion components
    freed), exactly 3 identically vacated rows, injective on the 15 non-tangential torsion components (radical
    leg or cokernel direction), 3 conditions on the 9 tangential ones; the frame equation keeps rank 16 with
    no vacated row; for an explicit integer curvature its radical-leg and cokernel components are nonzero.
(b) On the 24 connection components (de = 0): rank 12 at each normal form, 12 free. At the Lorentzian and
    Riemannian forms every free connection has K_ab (lowered with the wall metric) and M_{c mu} symmetric
    and no radical-leg component omega^{ab}_r, and the kernel splits as 6 boost (K) and 6 tangential (M).
(c) The principal symbol of the frame equation on the free sector has rank 6 in the radical direction and
    3 in each tangential direction (all three normal forms).
(d) For constant free connections the quadratic frame equation has exactly one surviving component, the
    cokernel component on the tangential triple (at the null form the pair E_0 = -E_1); at the Lorentzian and
    Riemannian forms E_D = sigma_2'(M) - sigma_2'(K) exactly with no cross term (four random free
    connections each); the cosmological term contributes -6 (Lambda/3) = -2 Lambda to E_3 at the Lorentzian
    form, +6 (Lambda/3) to E_0 at the Riemannian form, and (+6, -6) (Lambda/3) to (E_0, E_1) at the null form.
Not checked: the identification t = (tr M) 1 - M of the freed torsion, and the curved-wall remarks.
"""
from fractions import Fraction as F
from itertools import combinations, permutations

import GA
from tp_premise import premise

TRIPLES = list(combinations(range(4), 3))
PAIRS4 = [(m, n) for m in range(4) for n in range(m + 1, 4)]
ETA4 = [F(1), F(-1), F(-1), F(-1)]
OMEGA_IDX = [(p, mu) for p in PAIRS4 for mu in range(4)]


def perm_sign(p):
    p = list(p)
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def eps4(a, b, c, d):
    if len({a, b, c, d}) < 4:
        return 0
    return perm_sign((a, b, c, d))


def wedge_1_2(one, two):
    def b(m, n):
        if m == n:
            return F(0)
        return two.get((m, n), F(0)) if m < n else -two.get((n, m), F(0))
    return {(m, n, r): one[m] * b(n, r) - one[n] * b(m, r) + one[r] * b(m, n) for (m, n, r) in TRIPLES}


def torsion_matrix(e):
    cols = [(d, mn) for d in range(4) for mn in PAIRS4]
    rows = []
    for (a, b) in PAIRS4:
        for tri in TRIPLES:
            row = []
            for (d0, mn0) in cols:
                tot = F(0)
                for c in range(4):
                    s = eps4(a, b, c, d0)
                    if s:
                        tot += s * wedge_1_2(e[c], {mn0: F(1)})[tri]
                row.append(tot)
            rows.append(row)
    return rows


def frame_matrix(e):
    cols = [(cd, mn) for cd in PAIRS4 for mn in PAIRS4]
    rows = []
    for a in range(4):
        for tri in TRIPLES:
            row = []
            for ((c0, d0), mn0) in cols:
                tot = F(0)
                for b in range(4):
                    s = eps4(a, b, c0, d0)
                    if s:
                        tot += 2 * s * wedge_1_2(e[b], {mn0: F(1)})[tri]
                row.append(tot)
            rows.append(row)
    return rows


def zero_rows(M):
    return sum(1 for r in M if all(x == 0 for x in r))


def I4():
    return [[F(int(i == j)) for j in range(4)] for i in range(4)]


E_INV = I4()
E_LOR = [[F(int(m == a and a < 3)) for m in range(4)] for a in range(4)]
E_RIE = [[F(int(m == a and a > 0)) for m in range(4)] for a in range(4)]
E_NUL = [[F(0)] * 4 for _ in range(4)]
E_NUL[0][0] = E_NUL[1][0] = E_NUL[2][2] = E_NUL[3][3] = F(1)
Q_NUL = [[F(1), F(1), F(0), F(0)], [F(1), F(-1), F(0), F(0)], [F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)]]
FORMS = [("lorentzian", E_LOR, 3, 3, I4()), ("riemannian", E_RIE, 0, 0, I4()), ("null", E_NUL, 1, 1, Q_NUL)]
F_SEED = 7
COEFS = [[3, -1, 2, 0, 1, -2, 4, 1, -3, 2, 0, 1], [-2, 1, 0, 3, -1, 1, 2, -4, 1, 0, 2, -1],
         [1, 1, -1, 2, 3, 0, -2, 1, 1, -1, 4, 2], [0, -3, 1, 1, 2, 2, -1, 0, 3, 1, -2, 1]]


def adapt_rows(rows, Q, pairs=True):
    nt = len(TRIPLES)
    out = []
    if pairs:
        for (a1, b1) in PAIRS4:
            for t in range(nt):
                acc = [F(0)] * len(rows[0])
                for pi, (a, b) in enumerate(PAIRS4):
                    c = Q[a][a1] * Q[b][b1] - Q[b][a1] * Q[a][b1]
                    if c:
                        acc = [x + c * y for x, y in zip(acc, rows[pi * nt + t])]
                out.append(acc)
    else:
        for a1 in range(4):
            for t in range(nt):
                acc = [F(0)] * len(rows[0])
                for a in range(4):
                    if Q[a][a1]:
                        acc = [x + Q[a][a1] * y for x, y in zip(acc, rows[a * nt + t])]
                out.append(acc)
    return out


def adapt_cols(rows, Q):
    npairs = len(PAIRS4)
    return [[sum(Q[d][d1] * r[d * npairs + pi] for d in range(4)) for d1 in range(4) for pi in range(npairs)]
            for r in rows]


def check_torsion_and_frame_ranks():
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    Tinv, Finv = torsion_matrix(E_INV), frame_matrix(E_INV)
    assert GA.rank_of_vectors(Tinv) == 24 and GA.rank_of_vectors(Finv) == 16
    assert zero_rows(Tinv) == 0
    for (name, e, D, rad, Q) in FORMS:
        Tw = adapt_cols(adapt_rows(torsion_matrix(e), Q), Q)
        Fw = adapt_rows(frame_matrix(e), Q, pairs=False)
        assert GA.rank_of_vectors(Tw) == 18 and zero_rows(Tw) == 3
        assert GA.rank_of_vectors(Fw) == 16 and zero_rows(Fw) == 0
        cols = [(d, mn) for d in range(4) for mn in PAIRS4]
        tang = [k for k, (d, (m, n)) in enumerate(cols) if d != D and rad not in (m, n)]
        nontan = [k for k in range(24) if k not in tang]
        assert len(tang) == 9 and len(nontan) == 15
        assert GA.rank_of_vectors([[row[k] for k in nontan] for row in Tw]) == 15
        assert GA.rank_of_vectors([[row[k] for k in tang] for row in Tw]) == 3
    # the radical-leg and cokernel components of the frame equation do not vanish identically
    Fint, seed = {}, F_SEED
    for cd in PAIRS4:
        for mn in PAIRS4:
            seed = (seed * 31 + 11) % 17
            Fint[(cd, mn)] = F(seed - 8)
    rows = frame_matrix(E_LOR)
    cols = [(cd, mn) for cd in PAIRS4 for mn in PAIRS4]
    vals = {(a, tri): sum(rows[a * 4 + t][k] * Fint[cols[k]] for k in range(36))
            for a in range(4) for t, tri in enumerate(TRIPLES)}
    radical_nonzero = sum(1 for (a, tri), v in vals.items() if 3 in tri and v != 0)
    cokernel_nonzero = sum(1 for (a, tri), v in vals.items() if a == 3 and v != 0)
    assert radical_nonzero > 0 and cokernel_nonzero > 0


def om_get(om, a, b, mu):
    if a == b:
        return F(0)
    if a < b:
        return om.get(((a, b), mu), F(0))
    return -om.get(((b, a), mu), F(0))


def om_mixed(om, a, b, mu):
    return om_get(om, a, b, mu) * ETA4[b]


def torsion_of(om, e):
    return {(a, m, n): sum(om_mixed(om, a, b, m) * e[b][n] - om_mixed(om, a, b, n) * e[b][m] for b in range(4))
            for a in range(4) for m in range(4) for n in range(4)}


def conn_eq_on_omega(e):
    rows = []
    Ts = [torsion_of({u: F(1)}, e) for u in OMEGA_IDX]
    for (a, b) in PAIRS4:
        for (m, n, r) in TRIPLES:
            row = []
            for T in Ts:
                tot = F(0)
                for c in range(4):
                    for d in range(4):
                        s4 = eps4(a, b, c, d)
                        if s4:
                            tot += s4 * (e[c][m] * T[(d, n, r)] - e[c][n] * T[(d, m, r)] + e[c][r] * T[(d, m, n)])
                row.append(tot)
            rows.append(row)
    return rows


def kernel(rows):
    return GA.field_kernel([[F(x) for x in r] for r in rows])


def frame_symbol(e, direction):
    rows = []
    for a in range(4):
        for (m, n, r) in TRIPLES:
            row = []
            for ((c, d), nu) in OMEGA_IDX:
                two = {}
                if direction != nu:
                    two[(min(direction, nu), max(direction, nu))] = F(1 if direction < nu else -1)
                tot = F(0)
                for b in range(4):
                    for (cc, dd, sg) in ((c, d, 1), (d, c, -1)):
                        s4 = eps4(a, b, cc, dd)
                        if s4:
                            tot += s4 * wedge_1_2(e[b], {k: sg * v for k, v in two.items()})[(m, n, r)]
                row.append(tot)
            rows.append(row)
    return rows


def check_connection_rank_and_symbols():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    for (name, e, D, rad, Q) in FORMS:
        rows = conn_eq_on_omega(e)
        Kb = kernel(rows)
        assert GA.rank_of_vectors(rows) == 12 and len(Kb) == 12
        ranks = []
        for d in range(4):
            S = frame_symbol(e, d)
            ranks.append(GA.rank_of_vectors([[sum(row[k] * v[k] for k in range(24)) for v in Kb] for row in S]))
        assert ranks[rad] == 6 and [ranks[d] for d in range(4) if d != rad] == [3, 3, 3]


def lin_comb(vecs, coeffs):
    om = {}
    for v, c in zip(vecs, coeffs):
        for k in range(24):
            if v[k]:
                om[OMEGA_IDX[k]] = om.get(OMEGA_IDX[k], F(0)) + c * v[k]
    return om


def K_mixed(om, D):
    W = [a for a in range(4) if a != D]
    return [[om_mixed(om, a, D, b) for b in W] for a in W]


def M_lower(om, D):
    W = [a for a in range(4) if a != D]
    return [[sum(eps4(c, a, b, D) * om_get(om, a, b, mu) for a in W for b in W) / 2 for mu in W] for c in W]


def M_mixed(om, D):
    W = [a for a in range(4) if a != D]
    Ml = M_lower(om, D)
    return [[ETA4[W[c]] * Ml[c][mu] for mu in range(3)] for c in range(3)]


def sigma2p(A):
    tr = sum(A[i][i] for i in range(3))
    return tr * tr - sum(A[i][j] * A[j][i] for i in range(3) for j in range(3))


def check_free_sector_is_k_plus_m():
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    for (name, e, D, rad, Q) in FORMS[:2]:
        W = [a for a in range(4) if a != D]
        Kb = kernel(conn_eq_on_omega(e))
        for v in Kb:
            om = lin_comb([v], [F(1)])
            Km = K_mixed(om, D)
            Kl = [[ETA4[W[a]] * Km[a][b] for b in range(3)] for a in range(3)]
            Ml = M_lower(om, D)
            assert all(Kl[a][b] == Kl[b][a] and Ml[a][b] == Ml[b][a] for a in range(3) for b in range(3))
            assert all(om.get((p, rad), F(0)) == 0 for p in PAIRS4)
        Kc = [v for v in Kb if any(v[k] and D in OMEGA_IDX[k][0] for k in range(24))]
        Mc = [v for v in Kb if all(D not in OMEGA_IDX[k][0] for k in range(24) if v[k])]
        assert len(Kb) == 12 and len(Kc) == 6 and len(Mc) == 6


def frame_full_const(om, e, lam_over_3=F(0)):
    Rt = {}
    for c in range(4):
        for d in range(4):
            for m in range(4):
                for n in range(4):
                    v = sum(om_mixed(om, c, f, m) * om_get(om, f, d, n) - om_mixed(om, c, f, n) * om_get(om, f, d, m)
                            for f in range(4))
                    Rt[(c, d, m, n)] = v + lam_over_3 * (e[c][m] * e[d][n] - e[c][n] * e[d][m])
    out = {}
    for a in range(4):
        for (m, n, r) in TRIPLES:
            tot = F(0)
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        s4 = eps4(a, b, c, d)
                        if s4:
                            tot += s4 * (e[b][m] * Rt[(c, d, n, r)] - e[b][n] * Rt[(c, d, m, r)]
                                         + e[b][r] * Rt[(c, d, m, n)])
            out[(a, (m, n, r))] = tot
    return out


def check_hamiltonian_constraint():
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    for (name, e, D, rad, Q) in FORMS:
        Kb = kernel(conn_eq_on_omega(e))
        tri = tuple(i for i in range(4) if i != rad)
        for coeffs in COEFS[:2]:
            E1 = frame_full_const(lin_comb(Kb, [F(c) for c in coeffs]), e)
            nz = [k for k, v in E1.items() if v != 0]
            assert nz and all(k[1] == tri for k in nz)
            if name == "null":
                assert {k[0] for k in nz} == {0, 1} and E1[(0, tri)] == -E1[(1, tri)]
            else:
                assert len(nz) == 1 and nz[0][0] == rad
        lam = frame_full_const({}, e, F(1))
        if name == "lorentzian":
            assert lam[(3, tri)] == -6
        elif name == "riemannian":
            assert lam[(0, tri)] == 6
        else:
            assert (lam[(0, tri)], lam[(1, tri)]) == (6, -6)
    for (name, e, D, rad, Q) in FORMS[:2]:
        tri = tuple(a for a in range(4) if a != D)
        Kb = kernel(conn_eq_on_omega(e))
        Kc = [v for v in Kb if any(v[k] and D in OMEGA_IDX[k][0] for k in range(24))]
        Mc = [v for v in Kb if all(D not in OMEGA_IDX[k][0] for k in range(24) if v[k])]
        for coeffs in COEFS:
            omK = lin_comb(Kc, [F(c) for c in coeffs[:6]])
            omM = lin_comb(Mc, [F(c) for c in coeffs[6:]])
            both = dict(omK)
            for k, v in omM.items():
                both[k] = both.get(k, F(0)) + v
            EK = frame_full_const(omK, e)[(D, tri)]
            EM = frame_full_const(omM, e)[(D, tri)]
            EB = frame_full_const(both, e)[(D, tri)]
            assert EK == -sigma2p(K_mixed(omK, D)) and EM == sigma2p(M_mixed(omM, D)) and EB == EK + EM
            assert EK != 0 and EM != 0


EXPORTS = {"torsion_matrix": torsion_matrix, "frame_matrix": frame_matrix,
           "conn_eq_on_omega": conn_eq_on_omega, "kernel": kernel, "E_INV": E_INV, "E_LOR": E_LOR}
