"""synthesis.joint-clifford-clause-is-an-instance-of-the-signed-direction-postulates: exact checks.

V = Lambda C^5 in the occupation (bitmask) basis of lib/fock.py, modes 0, 1 the slots and 2, 3, 4 the pairs. The
Jordan-Wigner operators a_k (fock.ann, fock.cre) are the Klein-twisted slot operators and the pair operators of
synthesis.joint-clifford-clause-is-a-klein-convention-on-the-composite-space: one five-mode system. The untwisted
slot operators are a_i (-1)^k with (-1)^k the pair parity. Real Majoranas (fock.majorana, kind 'real'):
gamma_{2k} = a_k^dag + a_k (square +1), gamma_{2k+1} = a_k - a_k^dag (square -1). Every product of Majoranas is a
signed permutation matrix on the 32 states, stored as a tuple col -> (row, sign).
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

NM = 5
DIM = 1 << NM
SLOT_MAJ = 4
PAIR_MODES = [2, 3, 4]


def mono(M):
    out = [None] * DIM
    for (r, c), v in M.items():
        if out[c] is not None or v not in (1, -1):
            return None
        out[c] = (r, int(v))
    return tuple(out) if all(x is not None for x in out) else None


def mmul(A, B):
    return tuple((A[B[j][0]][0], A[B[j][0]][1] * B[j][1]) for j in range(DIM))


IDN = tuple((j, 1) for j in range(DIM))
NEG = tuple((j, -1) for j in range(DIM))


def neg(A):
    return mmul(NEG, A)


def transpose(A):
    out = [None] * DIM
    for j in range(DIM):
        r, s = A[j]
        out[r] = (j, s)
    return tuple(out)


def trace(A):
    return sum(A[j][1] for j in range(DIM) if A[j][0] == j)


def twisted():
    return [mono(fock.majorana(p, NM)) for p in range(2 * NM)]


def pair_parity():
    return mono(fock.parity(NM, modes=PAIR_MODES))


def untwisted():
    tw, P = twisted(), pair_parity()
    return [mmul(tw[p], P) if p < SLOT_MAJ else tw[p] for p in range(2 * NM)]


def group(gens):
    G = {IDN}
    frontier = [IDN]
    while frontier:
        nf = []
        for g in frontier:
            for h in gens:
                x = mmul(g, h)
                if x not in G:
                    G.add(x)
                    nf.append(x)
        frontier = nf
    return G


def relation(A, B):
    """+1 if A, B commute, -1 if they anticommute, 0 otherwise"""
    ab, ba = mmul(A, B), mmul(B, A)
    return 1 if ab == ba else -1 if ab == neg(ba) else 0


def square_sign(A):
    s = mmul(A, A)
    return 1 if s == IDN else -1 if s == NEG else 0


def blade(gens, S):
    out = IDN
    for i in sorted(S):
        out = mmul(out, gens[i])
    return out


def subsets(n):
    return [tuple(i for i in range(n) if m >> i & 1) for m in range(1 << n)]


def run_directions(gens):
    """(group order, c central, off-diagonal relations, squares, nonempty blades traceless, blades distinct mod sign)"""
    G = group(gens + [NEG])
    central = all(mmul(g, NEG) == mmul(NEG, g) for g in G) and NEG in G and NEG != IDN
    rels = sorted(set(relation(gens[i], gens[j]) for i in range(len(gens)) for j in range(len(gens)) if i != j))
    sq = [square_sign(g) for g in gens]
    blades = [blade(gens, S) for S in subsets(len(gens))]
    traceless = all(trace(b) == 0 for b in blades[1:]) and trace(blades[0]) == DIM
    classes = set(min(b, neg(b)) for b in blades)
    return len(G), central, rels, sq, traceless, len(classes)


def run_car_from_directions():
    """modes recovered as a_k = (gamma_{2k} + gamma_{2k+1})/2, adjoint (gamma_{2k} - gamma_{2k+1})/2: (failures of
    equality with the Fock operators, failures of the CAR)"""
    gam = [fock.majorana(p, NM) for p in range(2 * NM)]
    half = F(1, 2)
    eq_bad = car_bad = 0
    a = [fock.msc(half, fock.madd(gam[2 * k], gam[2 * k + 1])) for k in range(NM)]
    ad = [fock.msc(half, fock.msub(gam[2 * k], gam[2 * k + 1])) for k in range(NM)]
    for k in range(NM):
        eq_bad += 0 if fock.meq(a[k], fock.ann(k, NM)) and fock.meq(ad[k], fock.cre(k, NM)) else 1
        eq_bad += 0 if fock.meq(ad[k], fock.dag(a[k])) else 1
    one = fock.eye(DIM)
    for k in range(NM):
        for l in range(NM):
            car_bad += 0 if fock.meq(fock.acomm(a[k], ad[l]), one if k == l else {}) else 1
            car_bad += 0 if fock.is_zero(fock.acomm(a[k], a[l])) else 1
    return eq_bad, car_bad


def inverse(g):
    s = square_sign(g)
    return g if s == 1 else neg(g)


def commutant_dim(gens):
    """dimension of {K in M(32, Q) : g K g^-1 = K for every g in gens}, by signed union-find on the entries"""
    parent = {}
    par = {}

    def find(x):
        if parent[x] == x:
            return x, 0
        r, p = find(parent[x])
        parent[x] = r
        par[x] = (par[x] + p) % 2
        return r, par[x]
    dead = set()
    for i in range(DIM):
        for j in range(DIM):
            parent[(i, j)] = (i, j)
            par[(i, j)] = 0
    for g in gens:
        for i in range(DIM):
            for j in range(DIM):
                # (g K g^-1)_{pi(i) pi(j)} = s_i s_j K_ij, so K_{pi(i) pi(j)} = s_i s_j K_ij
                (pi, si), (pj, sj) = g[i], g[j]
                flip = 0 if si * sj == 1 else 1
                ra, pa = find((i, j))
                rb, pb = find((pi, pj))
                if ra == rb:
                    if (pa + pb + flip) % 2:
                        dead.add(ra)
                else:
                    parent[ra] = rb
                    par[ra] = (pa + pb + flip) % 2
    roots = set()
    for x in list(parent):
        r, _ = find(x)
        roots.add(r)
    dead_roots = set(find(d)[0] for d in dead)
    return len(roots - dead_roots)


def run_adjoint():
    tw = twisted()
    G = group(tw + [NEG])
    adj_is_inverse = sum(1 for g in G if transpose(g) == inverse(g))
    return len(G), adj_is_inverse, commutant_dim(tw), commutant_dim(tw[:-1])


def run_untwisted():
    tw, ut = twisted(), untwisted()
    G, G0 = group(tw + [NEG]), group(ut + [NEG])
    cross = [relation(ut[i], ut[j]) for i in range(SLOT_MAJ) for j in range(SLOT_MAJ, 2 * NM)]
    prod_pairs = blade(tw, range(SLOT_MAJ, 2 * NM))
    P = pair_parity()
    twist_inside = P == prod_pairs or P == neg(prod_pairs)
    return G0 == G, cross.count(1), len(cross), [square_sign(g) for g in ut] == [square_sign(g) for g in tw], \
        twist_inside


def run_gauss():
    """(operator Gauss sum, agreement of operator blade squares with GA blade squares, GA Gauss sums of other
    signatures (10,0) and (0,10))"""
    tw = twisted()
    sq = tuple(square_sign(g) for g in tw)
    ops = 0
    agree = 0
    for S in subsets(2 * NM):
        s = square_sign(blade(tw, S))
        ops += s
        sg, _ = GA.blade_mul(S, S, sq)
        agree += 1 if sg == s else 0

    def ga_sum(squares):
        return sum(GA.blade_mul(S, S, squares)[0] for S in subsets(2 * NM))
    return ops, agree, ga_sum(tuple([1] * (2 * NM))), ga_sum(tuple([-1] * (2 * NM))), sq


# ---------------------------------------------------------------- checks
def check_majoranas_form_a_group_of_signed_directions():
    """the ten twisted Majoranas and -1 generate a group of order 2^11, -1 central, every two distinct directions
    anticommute, squares +1, -1 alternating, the 1023 nonempty blades traceless and the 1024 blades distinct up to
    sign: (F2) with the sign bit acting as -1 (F3); the untwisted family fails F2c."""
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    order, central, rels, sq, traceless, classes = run_directions(untwisted())
    ok = order == 2048 and central and rels == [-1] and sq == [1, -1] * 5 and traceless and classes == 1024
    rels_u = run_directions(untwisted())[2]
    ok = ok and rels_u == [-1, 1]
    GA.check("slot and pair Majoranas with -1: a group of signed directions of order 2^11, signature (5,5)", ok)
    return ok


def check_car_is_equivalent_to_the_direction_relations():
    """a_k = (gamma_{2k} + gamma_{2k+1})/2 and a_k^dag = (gamma_{2k} - gamma_{2k+1})/2 are the Fock operators, the
    second the adjoint of the first, and they satisfy the CAR of one five-mode system (50 relations)."""
    premise("std-algebra.witt-basis-car")
    premise("synthesis.joint-clifford-clause-is-a-klein-convention-on-the-composite-space")
    eq_bad, car_bad = run_car_from_directions()
    ok = eq_bad == 0 and car_bad == 0
    GA.check("the CAR of the five modes are the signed-direction relations of their ten Majoranas", ok)
    return ok


def check_adjoint_is_the_group_inverse_and_the_invariant_form_is_unique():
    """on all 2048 elements of G the Fock adjoint (transpose) is the group inverse; the commutant of G on Q^32 is
    one-dimensional, so the G-invariant symmetric form is the Fock form up to scale; nine Majoranas leave two."""
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("std-algebra.fock-representation")
    order, adj_inv, dim10, dim9 = run_adjoint()
    ok = order == 2048 and adj_inv == 2048 and dim10 == 1 and dim9 == 2
    GA.check("the adjoint of the CAR is the inversion of the group of signed directions; the invariant form is unique",
             ok)
    return ok


def check_untwisted_directions_generate_the_same_group():
    """the untwisted Majoranas generate the same group G with the same squares, but all 24 slot-pair pairs commute;
    the pair parity is +-1 times the product of the six pair Majoranas, an element of G (the Klein twist inside G)."""
    premise("synthesis.joint-clifford-clause-is-a-klein-convention-on-the-composite-space")
    same, commuting, total, same_sq, twist_inside = run_untwisted()
    ok = same and (commuting, total) == (24, 24) and same_sq and twist_inside
    GA.check("untwisted and twisted directions generate one group; only the choice of directions differs", ok)
    return ok


def check_signature_gauss_sum():
    """operator blade squares agree with GA's blade squares for the signature (5,5) on all 1024 blades; the Gauss
    sum is 32 = 2^5, as for (10,0), while (0,10) gives -32."""
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("synthesis.blade-square-signs-f2-quadratic-form")
    ops, agree, s100, s010, sq = run_gauss()
    ok = ops == 32 and agree == 1024 and s100 == 32 and s010 == -32 and sq == (1, -1) * 5
    GA.check("Gauss sum of the slot-pair directions 2^5: Cl(5,5) and Cl(10,0) are one class", ok)
    return ok


if __name__ == "__main__":
    for fn in (check_majoranas_form_a_group_of_signed_directions, check_car_is_equivalent_to_the_direction_relations,
               check_adjoint_is_the_group_inverse_and_the_invariant_form_is_unique,
               check_untwisted_directions_generate_the_same_group, check_signature_gauss_sum):
        print(fn.__name__, fn())
