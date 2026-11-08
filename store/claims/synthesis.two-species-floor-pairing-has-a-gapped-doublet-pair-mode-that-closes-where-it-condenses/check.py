"""Exact checks: the two-species pairing element on a floor and its doublet pair mode.

Floor of Om blocks; block b holds three tower modes, psi_1 = mode 3b, psi_2 = mode 3b + 1 (an isospin doublet)
and chi = mode 3b + 2 (a singlet). The tower planes generate the CAR (field-theory.imported-tower-limit); the
Fock states are GA's exterior model (creation v = wedge, annihilation w = contraction), as in the stored pairing
checks; the block algebra is also checked in the Clifford algebra of the tower planes themselves (GA.mul).
  S = sum_b w_1 w_2 (singlet pair), B_a = sum_b w_a w_chi (doublet pair), S* = sum v_2 v_1, B_a* = sum v_chi v_a,
  H = Kp N_psi + Kc N_chi - GS S*S - GD (B_1*B_1 + B_2*B_2),
  doublet quanta Z_2* = sum w_1 v_chi, Z_1* = sum v_chi w_2 (each turns a singlet pair into a doublet pair),
  isospin t_+ = sum v_1 w_2, t_- = sum v_2 w_1, t_3 = (N_1 - N_2)/2,
  W = S*S + B_1*B_1 + B_2*B_2 (the pair sum with equal couplings).
Every number is a Fraction; spectra are certified by exact inertia (congruence diagonalisation of a rational
symmetric matrix, checked against GA.congruence_signature on the small cases).
"""
from fractions import Fraction as F
from itertools import combinations, permutations

import GA
from tp_premise import premise

# (Kp, Kc, GS, GD): rational samples, singlet-condensed (GS > GD), degenerate (GS = GD), doublet-condensed
COUPLINGS = [(F(1, 3), F(2), F(3), F(1)), (F(0), F(0), F(5, 2), F(1, 2)), (F(-1, 2), F(1, 4), F(2), F(2)),
             (F(1), F(1, 2), F(1), F(3))]
FLOORS = (1, 2, 3, 4)
W_FLOORS = (2, 3, 4, 5, 6)
H_FLOORS = (2, 3, 4, 5)
# clause (x): (n_b, P, GD) at K = 0, GS = 1 with omega_D > 0 where the sector (2, 2, 2) has a level below E(P, 0);
# and doublet-condensed (n_b, P) at K = 0, GS = 1, GD = 3 with isospin-one levels below the pair-breaking threshold
BELOW_BAND = [(5, 3, F(1, 2)), (6, 3, F(4, 5)), (7, 3, F(9, 10))]
CONDENSED = [(4, 2), (5, 2)]
H_SAMPLES = [(F(3), F(1)), (F(3), F(29, 10)), (F(7, 2), F(1, 3))]   # (GS, GD), GS > GD > 0


# ---------------------------------------------------------------- exterior model of the CAR
def _ann(i, st, m):
    return GA.ext_contract([F(1) if j == i else F(0) for j in range(m)], st)


def _cre(i, st, m):
    return GA.ext_wedge(i, st)


def _acc(out, x, c=F(1)):
    for k, v in x.items():
        out[k] = out.get(k, F(0)) + c * v
    return out


def _clean(x):
    return {k: v for k, v in x.items() if v != 0}


def _lin(*terms):
    out = {}
    for c, x in terms:
        _acc(out, x, F(c))
    return _clean(out)


def _vac():
    return {frozenset(): F(1)}


def _bil(om, ops, st):
    """sum_b of a product of single-block operators, ops = [(kind, flavour)] applied right to left."""
    m = 3 * om
    out = {}
    for b in range(om):
        y = st
        for kind, f in reversed(ops):
            y = (_cre if kind == 'v' else _ann)(3 * b + f, y, m)
            if not y:
                break
        _acc(out, y)
    return _clean(out)


def S(om, st):
    return _bil(om, [('w', 0), ('w', 1)], st)


def Ss(om, st):
    return _bil(om, [('v', 1), ('v', 0)], st)


def B(om, a, st):
    return _bil(om, [('w', a), ('w', 2)], st)


def Bs(om, a, st):
    return _bil(om, [('v', 2), ('v', a)], st)


def Z2s(om, st):
    return _bil(om, [('w', 0), ('v', 2)], st)


def Z2(om, st):
    return _bil(om, [('w', 2), ('v', 0)], st)


def Z1s(om, st):
    return _bil(om, [('v', 2), ('w', 1)], st)


def tp(om, st):
    return _bil(om, [('v', 0), ('w', 1)], st)


def tm(om, st):
    return _bil(om, [('v', 1), ('w', 0)], st)


def num(om, f, st):
    return _bil(om, [('v', f), ('w', f)], st)


def Hop(om, cp, st):
    Kp, Kc, GS, GD = cp
    out = {}
    _acc(out, num(om, 0, st), Kp)
    _acc(out, num(om, 1, st), Kp)
    _acc(out, num(om, 2, st), Kc)
    _acc(out, Ss(om, S(om, st)), -GS)
    for a in (0, 1):
        _acc(out, Bs(om, a, B(om, a, st)), -GD)
    return _clean(out)


def Wop(om, st):
    out = dict(Ss(om, S(om, st)))
    for a in (0, 1):
        _acc(out, Bs(om, a, B(om, a, st)))
    return _clean(out)


def band_state(om, nS, n1, n2):
    x = _vac()
    for _ in range(n2):
        x = Bs(om, 1, x)
    for _ in range(n1):
        x = Bs(om, 0, x)
    for _ in range(nS):
        x = Ss(om, x)
    return x


def isospin_casimir(om, st):
    t3 = _lin((F(1, 2), num(om, 0, st)), (F(-1, 2), num(om, 1, st)))
    t3t3 = _lin((F(1, 2), num(om, 0, t3)), (F(-1, 2), num(om, 1, t3)))
    return _lin((1, t3t3), (F(1, 2), tp(om, tm(om, st))), (F(1, 2), tm(om, tp(om, st))))


def eq(x, y):
    return GA.ext_state_eq(x, y)


def sector(om, nums):
    m = 3 * om
    return [frozenset(Sx) for k in range(m + 1) for Sx in combinations(range(m), k)
            if tuple(sum(1 for j in Sx if j % 3 == f) for f in range(3)) == nums]


def sector_matrix(om, nums, op):
    basis = sector(om, nums)
    idx = {Sx: i for i, Sx in enumerate(basis)}
    rows = [dict() for _ in basis]
    for j, Sx in enumerate(basis):
        for T, v in op({Sx: F(1)}).items():
            rows[idx[T]][j] = rows[idx[T]].get(j, F(0)) + v
    return [{k: v for k, v in r.items() if v != 0} for r in rows]


def shifted(rows, a, sign):
    """sign * rows - a * 1 as sparse rows (a symmetric rational matrix)."""
    out = []
    for i, r in enumerate(rows):
        d = {k: sign * v for k, v in r.items()}
        d[i] = d.get(i, F(0)) - a
        out.append({k: v for k, v in d.items() if v != 0})
    return out


def inertia(rows):
    """(n_plus, n_minus, n_zero) of a sparse rational symmetric matrix by congruence diagonalisation
    (symmetric elimination; a zero diagonal is repaired by adding a row and column, as GA.congruence_signature)."""
    A = [dict(r) for r in rows]
    alive = set(range(len(A)))
    pos = neg = zer = 0
    while alive:
        piv = next((i for i in sorted(alive) if A[i].get(i, 0) != 0), None)
        if piv is None:
            found = None
            for i in sorted(alive):
                j = next((j for j in sorted(A[i]) if j != i and j in alive), None)
                if j is not None:
                    found = (i, j)
                    break
            if found is None:
                zer += len(alive)
                break
            i, j = found
            for k, x in list(A[j].items()):
                A[i][k] = A[i].get(k, F(0)) + x
            for k in alive:
                if j in A[k]:
                    A[k][i] = A[k].get(i, F(0)) + A[k][j]
            for k in list(A[i]):
                if A[i][k] == 0:
                    del A[i][k]
            continue
        d = A[piv][piv]
        if d > 0:
            pos += 1
        else:
            neg += 1
        alive.discard(piv)
        rp = {k: x for k, x in A[piv].items() if k in alive}
        for i, xi in rp.items():
            f = xi / d
            Ai = A[i]
            for k, xk in rp.items():
                v = Ai.get(k, F(0)) - f * xk
                if v != 0:
                    Ai[k] = v
                else:
                    Ai.pop(k, None)
    return pos, neg, zer


def dense(rows):
    n = len(rows)
    return [[rows[i].get(j, F(0)) for j in range(n)] for i in range(n)]


def count_above(rows, a):
    """number of eigenvalues > a, and the multiplicity of a."""
    p, n, z = inertia(shifted(rows, a, 1))
    return p, z


# ---------------------------------------------------------------- sectors and block permutations
def sector_basis(om, nums):
    out = []
    for c1 in combinations(range(om), nums[0]):
        for c2 in combinations(range(om), nums[1]):
            for c3 in combinations(range(om), nums[2]):
                out.append(frozenset([3 * b for b in c1] + [3 * b + 1 for b in c2] + [3 * b + 2 for b in c3]))
    return out


def permuted(pi, Sx):
    """the Fock basis vector of Sx with block b relabelled pi[b], and the sign of reordering its creators."""
    seq = [3 * pi[k // 3] + k % 3 for k in sorted(Sx)]
    inv = sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq)) if seq[i] > seq[j])
    return frozenset(seq), (F(-1) if inv % 2 else F(1))


def fixed_block_inertia(om, nums, cp, E):
    """inertia of H - E on the vectors of the sector invariant under the permutations of blocks 1, ..., om - 1
    (Gram form <s_i, (H - E) s_j> on the orbit sums s_i, which are orthogonal and nonzero)."""
    perms = [tuple([0] + list(q)) for q in permutations(range(1, om))]
    seen, vecs = set(), []
    for Sx in sector_basis(om, nums):
        if Sx in seen:
            continue
        v = {}
        for pi in perms:
            T, sg = permuted(pi, Sx)
            seen.add(T)
            v[T] = v.get(T, F(0)) + sg
        v = _clean(v)
        if v:
            vecs.append(v)
    hv = [Hop(om, cp, v) for v in vecs]
    ip = lambda a, b: sum((c * b.get(k, F(0)) for k, c in a.items()), F(0))
    rows = []
    for i in range(len(vecs)):
        r = {j: ip(vecs[i], hv[j]) - E * ip(vecs[i], vecs[j]) for j in range(len(vecs))}
        rows.append({j: x for j, x in r.items() if x != 0})
    return len(vecs), inertia(rows)


# ---------------------------------------------------------------- Clifford algebra of one block
def _block_cl():
    # kernel g1, g2 (square -1), then three tower planes (e, f): squares +1, -1
    s = tuple([-1, -1] + [1, -1] * 3)
    mul = lambda x, y: GA.mul(x, y, s)
    v = [GA.add(GA.scal(F(1, 2), GA.gen(2 + 2 * j)), GA.scal(F(1, 2), GA.gen(3 + 2 * j))) for j in range(3)]
    w = [GA.add(GA.scal(F(1, 2), GA.gen(2 + 2 * j)), GA.scal(F(-1, 2), GA.gen(3 + 2 * j))) for j in range(3)]
    J = mul(GA.gen(0), GA.gen(1))
    gam = GA.sc(1)
    for j in range(3):
        gam = mul(gam, mul(GA.gen(2 + 2 * j), GA.gen(3 + 2 * j)))
    return s, mul, v, w, J, gam


# ================================================================ checks
def check_block_algebra_in_the_tower_planes():
    premise("field-theory.imported-tower-limit")
    premise("synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower")
    s, mul, v, w, J, gam = _block_cl()
    ok = True
    for i in range(3):
        for j in range(3):
            ok = ok and GA.eq(GA.add(mul(w[i], v[j]), mul(v[j], w[i])), GA.sc(int(i == j)))
            ok = ok and GA.is_zero(GA.add(mul(v[i], v[j]), mul(v[j], v[i])))
        ok = ok and GA.commutes(J, v[i], s) and GA.commutes(J, w[i], s)
        ok = ok and GA.anticommutes(gam, v[i], s)
    # pair creators: any two of the three sharing a mode multiply to zero, so a block holds at most one pair
    pc = {(0, 1): mul(v[1], v[0]), (0, 2): mul(v[2], v[0]), (1, 2): mul(v[2], v[1])}
    for a in pc:
        for b in pc:
            ok = ok and GA.is_zero(mul(pc[a], pc[b]))
        ok = ok and GA.commutes(gam, pc[a], s) and not GA.is_zero(pc[a])
    # the doublet transfers are even and commute with J; [Z_2*, S*] = B_2*, [Z_1*, S*] = B_1*, [t_+, Z_2*] = Z_1*,
    # [t_-, B_1*] = B_2* on one block
    z2s, z1s = mul(w[0], v[2]), mul(v[2], w[1])
    ss, b1s, b2s = pc[(0, 1)], pc[(0, 2)], pc[(1, 2)]
    tpl, tmi = mul(v[0], w[1]), mul(v[1], w[0])
    com = lambda x, y: GA.sub(mul(x, y), mul(y, x))
    ok = ok and GA.commutes(gam, z2s, s) and GA.commutes(J, z2s, s) and GA.commutes(gam, z1s, s)
    ok = ok and GA.eq(com(z2s, ss), b2s) and GA.eq(com(z1s, ss), b1s)
    ok = ok and GA.eq(com(tpl, z2s), z1s) and GA.eq(com(tmi, b1s), b2s)
    ok = ok and GA.is_zero(com(tpl, b1s)) and GA.is_zero(com(tpl, z1s)) and GA.is_zero(com(tpl, ss))
    GA.check("one block of three tower planes: CAR, J central, pair creators sharing a mode multiply to zero, "
             "even doublet transfers with [Z*, S*] = B*", ok)
    return ok


def check_symmetric_band_spectrum_and_isospin():
    premise("field-theory.composite-scalars-mean-field-level")
    premise("field-theory.imported-tower-limit")
    ok = True
    for om in FLOORS:
        for P in range(om + 1):
            for nS in range(P + 1):
                for n1 in range(P - nS + 1):
                    n2 = P - nS - n1
                    x = band_state(om, nS, n1, n2)
                    n = n1 + n2
                    ok = ok and len(x) > 0
                    for cp in COUPLINGS:
                        Kp, Kc, GS, GD = cp
                        E = Kp * (2 * nS + n) + Kc * n - (GS * nS + GD * n) * (om - P + 1)
                        ok = ok and eq(Hop(om, cp, x), _lin((E, x)))
                    # isospin n/2: Casimir (n/2)(n/2 + 1)
                    ok = ok and eq(isospin_casimir(om, x), _lin((F(n, 2) * (F(n, 2) + 1), x)))
            # beyond one pair per block the band vanishes
            ok = ok and len(band_state(om, om + 1, 0, 0)) == 0 and len(band_state(om, 0, 1, om)) == 0
    # H commutes with the isospin raising and lowering operators on every Fock state of the floors om = 1, 2
    for om in (1, 2):
        for k in range(3 * om + 1):
            for Sx in combinations(range(3 * om), k):
                st = {frozenset(Sx): F(1)}
                for cp in COUPLINGS:
                    ok = ok and eq(Hop(om, cp, tp(om, st)), tp(om, Hop(om, cp, st)))
                    ok = ok and eq(Hop(om, cp, tm(om, st)), tm(om, Hop(om, cp, st)))
    GA.check("block-symmetric even states: E = Kp(2nS + n) + Kc n - (GS nS + GD n)(Om - P + 1), isospin n/2", ok)
    return ok


def check_doublet_quanta_ladder_charges_and_canonical_defect():
    premise("synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower")
    premise("field-theory.how-close-tower-comes-ccr")
    ok = True
    for om in FLOORS:
        for P in range(1, om + 1):
            for nq in range(P):
                x, y = band_state(om, P - nq, 0, nq), band_state(om, P - nq - 1, 0, nq + 1)
                ok = ok and eq(Z2s(om, x), _lin((P - nq, y)))
                # [Z_2, Z_2*] = N_1 - N_chi, equal to P - 2 nq on the ladder
                c = _lin((1, Z2(om, Z2s(om, x))), (-1, Z2s(om, Z2(om, x))))
                ok = ok and eq(c, _lin((P - 2 * nq, x)))
                for cp in COUPLINGS:
                    Kp, Kc, GS, GD = cp
                    wD = (Kc - Kp) + (GS - GD) * (om - P + 1)
                    E0 = 2 * Kp * P - GS * P * (om - P + 1)
                    ok = ok and eq(Hop(om, cp, x), _lin((E0 + nq * wD, x)))
                # charges: N_chi up by one, N_psi down by one, doublet partner Z_1* = [t_+, Z_2*]
                zx = Z2s(om, x)
                ok = ok and eq(num(om, 2, zx), _lin((nq + 1, zx))) and eq(
                    _lin((1, num(om, 0, zx)), (1, num(om, 1, zx))), _lin((2 * P - nq - 1, zx)))
                ok = ok and eq(_lin((1, tp(om, Z2s(om, x))), (-1, Z2s(om, tp(om, x)))), Z1s(om, x))
    # the operator identity [Z_2, Z_2*] = N_1 - N_chi on every basis state of the floors om = 1, 2
    for om in (1, 2):
        for k in range(3 * om + 1):
            for Sx in combinations(range(3 * om), k):
                st = {frozenset(Sx): F(1)}
                c = _lin((1, Z2(om, Z2s(om, st))), (-1, Z2s(om, Z2(om, st))))
                ok = ok and eq(c, _lin((1, num(om, 0, st)), (-1, num(om, 2, st))))
    GA.check("doublet quanta: Z_2* x_n = (P - n) x_(n+1), harmonic quantum (Kc - Kp) + (GS - GD)(Om - P + 1), "
             "[Z_2, Z_2*] = N_1 - N_chi = P - 2n", ok)
    return ok


def check_condensed_doublet_is_degenerate_and_has_no_subthreshold_amplitude():
    premise("synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy")
    ok = True
    for om in FLOORS:
        for P in range(1, om + 1):
            for cp in COUPLINGS:
                Kp, Kc, GS, GD = cp
                Eq = (Kp + Kc) * P - GD * P * (om - P + 1)
                # every member of the isospin P/2 multiplet of the doublet band has the same energy
                for n1 in range(P + 1):
                    x = band_state(om, 0, n1, P - n1)
                    ok = ok and eq(Hop(om, cp, x), _lin((Eq, x)))
                # both doublet components add a pair at the same cost
                if P < om:
                    x = band_state(om, 0, 0, P)
                    E1 = (Kp + Kc) * (P + 1) - GD * (P + 1) * (om - P)
                    for a in (0, 1):
                        y = Bs(om, a, x)
                        ok = ok and len(y) > 0 and eq(Hop(om, cp, y), _lin((E1, y)))
            # stretched doublet sector (0, P, P): next level exactly GD * om above the band, none between
            if 0 < P < om:
                cp = COUPLINGS[3]
                Kp, Kc, GS, GD = cp
                rows = sector_matrix(om, (0, P, P), lambda st: Hop(om, cp, st))
                Eq = (Kp + Kc) * P - GD * P * (om - P + 1)
                p, n, z = inertia(shifted(rows, Eq, 1))
                ok = ok and n == 0 and z == 1
                p, n, z = inertia(shifted(rows, Eq + GD * om, 1))
                ok = ok and n == 1 and z >= 1
    GA.check("doublet-condensed: isospin multiplet degenerate, both components add pairs alike, "
             "amplitude threshold GD Om with no level between", ok)
    return ok


def check_casimir_identity_for_the_pair_sum():
    premise("field-theory.imported-tower-limit")
    ok = True
    for om in (1, 2, 3):
        m = 3 * om
        for k in range(m + 1):
            for Sx in combinations(range(m), k):
                st = {frozenset(Sx): F(1)}
                Nst = _lin(*[(1, num(om, f, st)) for f in range(3)])
                cu = {}
                for i in range(3):
                    for j in range(3):
                        _acc(cu, _bil(om, [('v', i), ('w', j)], _bil(om, [('v', j), ('w', i)], st)))
                co = {}
                for b in range(om):
                    for c in range(b + 1, om):
                        def L(x, b=b, c=c):
                            out = {}
                            for i in range(3):
                                _acc(out, _cre(3 * b + i, _ann(3 * c + i, x, m), m))
                                _acc(out, _cre(3 * c + i, _ann(3 * b + i, x, m), m), F(-1))
                            return _clean(out)
                        _acc(co, L(L(st)), F(-1))
                lhs = _lin((2, Wop(om, st)))
                rhs = _lin((om + 2, Nst), (-1, _clean(cu)), (-1, _clean(co)))
                ok = ok and eq(lhs, rhs)
    GA.check("2W = N(Om + 2) - C_u3 - C_O on every Fock state of the floors Om = 1, 2, 3", ok)
    return ok


def check_threshold_binding_and_the_pair_sum_spectrum():
    premise("synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy")
    ok = True
    for om in W_FLOORS:
        for P in range(1, om + 1):
            nums = (P - 1, P, 1)
            Wr = sector_matrix(om, nums, lambda st: Wop(om, st))
            WD = P * (om - P + 1)
            if P == 1:
                X, X2 = om, 0
            else:
                X = (P - 1) * (om - P + 1) + max(om - P + 1, 3)
                X2 = (P - 1) * (om - P + 1) + 3
            above, mult = count_above(Wr, X)
            ok = ok and above == 0 and mult >= 1
            if om - P + 1 > 3 or P == 1:
                above, mult = count_above(Wr, X2)
                ok = ok and above == 1 and mult >= 1 and X == WD
            # the collective state is an eigenvector of W with WD, so D is in the sector
            xD = band_state(om, P - 1, 0, 1)
            ok = ok and eq(Wop(om, xD), _lin((WD, xD)))
            if om <= 3:
                ok = ok and GA.congruence_signature(dense(shifted(Wr, X, 1)))[0] == 0
            # the G_D = 0 threshold: lowest level of H at GD = 0 is E_th0 (stored one-species spectrum)
            if om <= 4:
                cp = (F(1, 3), F(2), F(3), F(0))
                Hr = sector_matrix(om, nums, lambda st: Hop(om, cp, st))
                Eth = cp[0] * (2 * P - 1) + cp[1] - cp[2] * (P - 1) * (om - P + 1)
                p, n, z = inertia(shifted(Hr, Eth, 1))
                ok = ok and n == 0 and z >= 1
    GA.check("pair-sum spectrum on the one-quantum sector: max (P-1)(Om-P+1) + max(Om-P+1, 3), second "
             "(P-1)(Om-P+1) + 3; G_D = 0 threshold (P-1)(Om-P+1) pairs", ok)
    return ok


def check_lowest_doublet_level_and_its_separation():
    premise("synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy")
    ok = True
    cases = [(om, P) for om in H_FLOORS for P in range(1, om + 1)]
    for om, P in cases:
        nums = (P - 1, P, 1)
        for GS, GD in H_SAMPLES:
            cp = (F(0), F(0), GS, GD)
            Hr = sector_matrix(om, nums, lambda st: Hop(om, cp, st))
            ED = -(GS * (P - 1) + GD) * (om - P + 1)
            Eth = -GS * (P - 1) * (om - P + 1)
            c = max(0, P + 2 - om) if P > 1 else 0
            p, n, z = inertia(shifted(Hr, ED, 1))
            # the collective level is the lowest when the pair-sum maximum is the collective one; otherwise no
            # level lies more than c GD below it, and on a full floor (P = om) that bound is attained
            ok = ok and z >= 1 and (n == 0 or c > 0)
            p, n, z = inertia(shifted(Hr, ED - c * GD, 1))
            ok = ok and n == 0 and (z >= 1 or P < om)
            if om - P + 1 > 3 or (P == 1 and om > 1):
                # exactly one level (the collective one) below E_th0 - 3 GD (P > 1) or below E_th0 (P = 1)
                bound = Eth - 3 * GD if P > 1 else Eth
                p, n, z = inertia(shifted(Hr, bound, 1))
                ok = ok and n == 1
    GA.check("one doublet quantum, GS > GD: lowest level E_D for Om - P + 1 >= 3, within c GD otherwise; "
             "every other level >= E_th0 - 3 GD", ok)
    return ok


def check_band_need_not_hold_the_ground_state_and_condensate_levels_below_threshold():
    premise("synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy")
    ok = True
    # singlet regime (omega_D > 0, n_b - P + 1 >= 3): a level with N_chi = 2 lies below the singlet band E(P, 0)
    for om, P, GD in BELOW_BAND:
        cp = (F(0), F(0), F(1), GD)
        wD = (F(1) - GD) * (om - P + 1)
        EP = -P * (om - P + 1)
        ok = ok and wD > 0 and om - P + 1 >= 3
        dim, (p, n, z) = fixed_block_inertia(om, (P - 1, P - 1, 2), cp, EP)
        ok = ok and n >= 1
        # the singlet sector itself has nothing below its band, which is its lowest level
        if om == 5:
            rows = sector_matrix(om, (P, P, 0), lambda st: Hop(om, cp, st))
            p, n, z = inertia(shifted(rows, EP, 1))
            ok = ok and n == 0 and z == 1
    # doublet-condensed band (omega_D < 0): at the condensate's numbers N_psi = N_chi = P, the stretched sector has one
    # level below the pair-breaking threshold E(0, P) + GD n_b, the sector (1, P - 1, P) (isospin P/2 - 1 and up) many
    for om, P in CONDENSED:
        cp = (F(0), F(0), F(1), F(3))
        Eq = -3 * P * (om - P + 1)
        thr = Eq + 3 * om
        ok = ok and (F(1) - F(3)) * (om - P + 1) < 0
        st = inertia(shifted(sector_matrix(om, (0, P, P), lambda x: Hop(om, cp, x)), thr, 1))
        lo = inertia(shifted(sector_matrix(om, (1, P - 1, P), lambda x: Hop(om, cp, x)), thr, 1))
        bnd = inertia(shifted(sector_matrix(om, (1, P - 1, P), lambda x: Hop(om, cp, x)), Eq, 1))
        ok = ok and st[1] == 1 and lo[1] == om * om and bnd[1] == 0 and bnd[2] == 1
    GA.check("the band need not hold the ground state at fixed N with omega_D > 0 (n_b = 5, 6, 7, P = 3); "
             "condensed band: isospin-one levels below pair breaking (n_b = 4, 5, P = 2)", ok)
    return ok
