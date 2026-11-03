"""standard-model.imported-sectors-superselection-mirror-copy: exact checks of the algebraic part.

Checked:
(1) Towers are residues: the Rule-1 step Cl(p,q) -> Cl(p+1,q+1) keeps r = p - q mod 8 and is the
    Morita step Cl(p+1,q+1) = Cl(p,q) (x) Mat_2(R) (twisted generators e_i e+ e- commute with the
    matrix units of Cl(1,1) and the products span), for all 10 signatures with n <= 3; this world
    (1,3) has r = 6 and the mirror (3,1) has r = 2, two different towers: Cl(1,3) has a primitive
    corner H (dimension 4, quaternion relations) and Cl(3,1) a corner R (dimension 1), and the same
    holds one rung up, Cl(2,4) and Cl(4,2).
(2) The copy is blind to the reversal: the derived content uses the conformal spin group and its
    complex representations, i.e. the even subalgebras. For (1,3), (3,1) and the ambients (2,4),
    (4,2) the even subalgebra has dimension 2^(n-1), its centre (computed as the kernel of the
    commutators with the even generators e_i e_j) is span(1, I) with I^2 = -1: the even subalgebras
    of a signature and its reversal are the same simple complex algebra (Mat_2(C), Mat_4(C)).
Not computable: the superselection of the tower charge, the unreachability of the walls and the
gravitational-only coupling are physical statements of T14 with no finite algebraic core here;
the equality of the beta-functions is the identity of the two listings (computed in the check of
standard-model.under-s-mirror-inherits-desert).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


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


def _corner_type(p, q):
    m = p + q
    sq = GA.sig(p, q)
    e = _primitive_idempotent(sq, m)
    els = [GA.mul(GA.mul(e, {b: F(1)}, sq), e, sq) for b in GA.all_blades(m)]
    basis = []
    for x in els:
        if x and _rank(basis + [x], m) > len(basis):
            basis.append(x)
    quat = False
    if len(basis) == 4:
        units = [x for x in basis if GA.eq(GA.mul(x, x, sq), GA.scal(-1, e))]
        quat = any(GA.is_zero(GA.add(GA.mul(u, v, sq), GA.mul(v, u, sq))) for u in units for v in units)
    return len(basis), quat


def check_towers_are_residues_and_mirror_is_another():
    premise("dark-matter.towers-are-residues-single-clock-filter")
    ok = True
    for n in range(0, 4):
        for p in range(n + 1):
            q = n - p
            sqB = GA.sig(p, q) + (1, -1)
            ok = ok and ((p + 1) - (q + 1)) % 8 == (p - q) % 8
            ep, em = GA.gen(n), GA.gen(n + 1)
            f = GA.mul(ep, em, sqB)
            Ap = [GA.mul(GA.gen(i), f, sqB) for i in range(n)]
            units = [GA.sc(1), f, ep, em]
            ok = ok and all(GA.commutes(a, u, sqB) for a in Ap for u in units)
            prods = []
            for b in GA.all_blades(n):
                a = GA.sc(1)
                for i in b:
                    a = GA.mul(a, Ap[i], sqB)
                prods.extend(GA.mul(a, u, sqB) for u in units)
            ok = ok and _rank(prods, n + 2) == 2 ** (n + 2)
    ok = ok and (1 - 3) % 8 == 6 and (3 - 1) % 8 == 2
    ok = ok and _corner_type(1, 3) == (4, True) and _corner_type(3, 1) == (1, False)
    ok = ok and _corner_type(2, 4) == (4, True) and _corner_type(4, 2) == (1, False)
    GA.check("Rule 1 keeps the residue (Morita step, n <= 3); (1,3) at r = 6 (H) and (3,1) at r = 2 (R)", ok)
    return ok


def check_even_subalgebras_of_reversal_pair_agree():
    premise("dark-matter.mirror-tower-copy-one")
    ok = True
    for (p, q) in [(1, 3), (3, 1), (2, 4), (4, 2)]:
        m = p + q
        sq = GA.sig(p, q)
        evens = [b for b in GA.all_blades(m) if len(b) % 2 == 0]
        ok = ok and len(evens) == 2 ** (m - 1)
        gens = [GA.mul(GA.gen(i), GA.gen(j), sq) for i in range(m) for j in range(i + 1, m)]
        # kernel of x -> ([x, g])_g on the even subalgebra
        cols = []
        for b in evens:
            col = []
            for g in gens:
                c = GA.sub(GA.mul({b: F(1)}, g, sq), GA.mul(g, {b: F(1)}, sq))
                col.extend(GA.basis_vector_of(c, evens))
            cols.append(col)
        mat = [[cols[j][i] for j in range(len(evens))] for i in range(len(cols[0]))]
        ker = GA.field_kernel(mat)
        ok = ok and len(ker) == 2
        I = {tuple(range(m)): F(1)}
        ok = ok and GA.eq(GA.mul(I, I, sq), GA.sc(-1))
        ok = ok and all(GA.commutes(I, g, sq) for g in gens)
    GA.check("even subalgebras of (1,3)/(3,1) and (2,4)/(4,2): centre span(1, I), I^2 = -1, same type", ok)
    return ok
