"""transport.embedding-independent-minimality-fusion: exact checks.

(1) The proof's case analysis, enumerated: for F in {R, H} (f = 1, 4), k = 1..6, D in {R, C, H}
    (d = 1, 2, 4) and multiplicities a, b = 1..12 with D embedding unitally in Mat_a(F) and in
    Mat_b(F) (over R: C needs a even, H needs 4 | a; over H every a >= 1), and m d = (a + b) k f
    with m an integer, the minimum of dim B = m^2 d is 4 k^2 f = 2^(n+1), attained only at D = F,
    a = b = 1, m = 2k; the per-case minima 8k^2 (F = R, D = C), 16k^2 (F = R, D = H), 32k^2
    (F = H, D = C), 64k^2 (F = H, D = R) are the proof's.
(2) The embedding rules used: explicit unital embeddings C -> Mat_2(R), H -> Mat_4(R),
    C -> H (relations checked exactly); no C in Mat_a(R) for odd a since det(J)^2 = det(-1) =
    (-1)^a would be negative.
(3) The equality case on Clifford algebras, p - q = 1 mod 4, n <= 5: A = Cl(p,q) has two blocks
    (central omega, omega^2 = 1) of dimension 2^(n-1) = k^2 f; the Rule-2 ascent B (exports of the
    transport.rule-2-ideal-fusion-sharp-form check) is simple of dimension 2^(n+1); a primitive
    idempotent e of B has corner e B e = F (dimension 1, or the quaternion relations for
    dimension 4) and dim B e = 2k f: B = Mat_2k(F), with F = R at p - q = 1 mod 8 and H at 5.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

FIELDS = {"R": 1, "C": 2, "H": 4}


def _embeds(D, Fld, a):
    if Fld == "H" or D == "R":
        return a >= 1
    if D == "C":
        return a % 2 == 0
    return a % 4 == 0


def check_case_analysis_minimum():
    premise("transport.classification-real-clifford-algebras")
    ok = True
    for Fld in ("R", "H"):
        f = FIELDS[Fld]
        for k in range(1, 7):
            best = {}
            for D, d in FIELDS.items():
                for a in range(1, 13):
                    for b in range(1, 13):
                        if not (_embeds(D, Fld, a) and _embeds(D, Fld, b)):
                            continue
                        tot = (a + b) * k * f
                        if tot % d:
                            continue
                        m = tot // d
                        dim = m * m * d
                        if D not in best or dim < best[D][0]:
                            best[D] = (dim, a, b, m)
            overall = min(v[0] for v in best.values())
            ok = ok and overall == 4 * k * k * f
            winners = [(D, v) for D, v in best.items() if v[0] == overall]
            ok = ok and winners == [(Fld, (4 * k * k * f, 1, 1, 2 * k))]
            if Fld == "R":
                ok = ok and best["C"][0] == 8 * k * k and best["H"][0] == 16 * k * k
            else:
                ok = ok and best["C"][0] == 32 * k * k and best["R"][0] == 64 * k * k
    GA.check("dim B >= 4 k^2 f = 2^(n+1) with equality only at Mat_2k(F); proof's case minima", ok)
    return ok


def _mm(A, B):
    return [[sum(A[i][t] * B[t][j] for t in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def _neg_id(n):
    return [[F(-1) if i == j else F(0) for j in range(n)] for i in range(n)]


def check_embedding_rules():
    ok = True
    J = [[F(0), F(-1)], [F(1), F(0)]]
    ok = ok and _mm(J, J) == _neg_id(2)
    # H in Mat_4(R): left multiplication by i and j on (1, i, j, k)
    I4 = [[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]]
    J4 = [[0, 0, -1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, -1, 0, 0]]
    I4 = [[F(x) for x in r] for r in I4]
    J4 = [[F(x) for x in r] for r in J4]
    ok = ok and _mm(I4, I4) == _neg_id(4) and _mm(J4, J4) == _neg_id(4)
    IJ, JI = _mm(I4, J4), _mm(J4, I4)
    ok = ok and IJ == [[-x for x in r] for r in JI]
    ok = ok and GA.mat_rank([[I4[i][j] for j in range(4)] + [J4[i][j] for j in range(4)]
                             + [IJ[i][j] for j in range(4)] for i in range(4)]) == 4
    # C in H: the quaternion units in Cl(0,2) = H: e0 squares to -1
    sq = GA.sig(0, 2)
    ok = ok and GA.eq(GA.mul(GA.gen(0), GA.gen(0), sq), GA.sc(-1))
    # odd a: det(J)^2 would equal det(-1_a) = (-1)^a = -1 < 0
    for a in (1, 3, 5, 7):
        det = F(1)
        for i in range(a):
            det *= _neg_id(a)[i][i]
        ok = ok and det == -1
    GA.check("unital embeddings C -> Mat_2(R), H -> Mat_4(R), C -> H; none of C in Mat_odd(R)", ok)
    return ok


def _rank(elems, m):
    blades = GA.all_blades(m)
    rows = [GA.basis_vector_of(x, blades) for x in elems if x]
    return GA.rank_of_vectors(rows) if rows else 0


def _primitive_idempotent(sq, m):
    e = GA.sc(1)
    chosen = []
    for b in GA.all_blades(m):
        if not b:
            continue
        x = {b: F(1)}
        if not GA.eq(GA.mul(x, x, sq), GA.sc(1)) or not all(GA.commutes(x, c, sq) for c in chosen):
            continue
        g = GA.mul(e, GA.scal(F(1, 2), GA.add(GA.sc(1), x)), sq)
        if GA.is_zero(g) or GA.eq(g, e):
            continue
        e, chosen = g, chosen + [x]
    return e


def _corner(e, sq, m):
    els = [GA.mul(GA.mul(e, {b: F(1)}, sq), e, sq) for b in GA.all_blades(m)]
    els = [x for x in els if x]
    basis = []
    for x in els:
        if _rank(basis + [x], m) > len(basis):
            basis.append(x)
    return basis


def check_equality_case_is_mat_2k_f():
    ex = premise("transport.rule-2-ideal-fusion-sharp-form")
    premise("transport.corner-even-subalgebra")
    fusion, central_blades = ex["fusion"], ex["central_blades"]
    ok = True
    for (p, q, Fld) in [(1, 0, "R"), (2, 1, "R"), (0, 3, "H"), (3, 2, "R"), (1, 4, "H"), (5, 0, "H")]:
        n = p + q
        f = FIELDS[Fld]
        sqA = GA.sig(p, q)
        ok = ok and central_blades(sqA, n) == [(), tuple(range(n))]
        k2 = 2 ** (n - 1) // f
        k = next(kk for kk in range(1, 9) if kk * kk == k2)
        sq = fusion(p, q, 1)["sq"]
        ok = ok and central_blades(sq, n + 1) == [()]
        e = _primitive_idempotent(sq, n + 1)
        cb = _corner(e, sq, n + 1)
        ok = ok and len(cb) == f
        if f == 4:
            units = [x for x in cb if GA.eq(GA.mul(x, x, sq), GA.scal(-1, e))]
            pair = [(u, v) for u in units for v in units
                    if GA.is_zero(GA.add(GA.mul(u, v, sq), GA.mul(v, u, sq)))]
            ok = ok and len(pair) > 0
        Be = [GA.mul({b: F(1)}, e, sq) for b in GA.all_blades(n + 1)]
        ok = ok and _rank(Be, n + 1) == 2 * k * f
        ok = ok and (2 * k) ** 2 * f == 2 ** (n + 1)
    GA.check("the fused algebra of each split Cl(p,q), n <= 5, is Mat_2k(F) of dimension 2^(n+1)", ok)
    return ok
