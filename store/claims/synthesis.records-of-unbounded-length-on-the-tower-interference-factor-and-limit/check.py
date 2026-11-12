"""synthesis.records-of-unbounded-length-on-the-tower-interference-factor-and-limit: exact checks.

Fock module of the ladder pairs (lib/fock.py, LSB bitmask basis): v_j = a_j^dag (wedge), w_j = a_j
(contraction), tied to the Clifford generators e_j = v_j + w_j, f_j = v_j - w_j of GA signature
(1, -1, 1, -1, ...). System rungs 0, 1; record pair j is the rungs 2 + 2j, 3 + 2j. All arithmetic exact.
"""
from fractions import Fraction as F
from itertools import product
import GA
import fock
from tp_premise import premise

AL, BE = F(3, 5), F(4, 5)          # the system's amplitudes on rungs 0 and 1


def vadd(*vs):
    out = {}
    for x in vs:
        for k, c in x.items():
            out[k] = out.get(k, F(0)) + c
    return {k: c for k, c in out.items() if c != 0}


def vsc(c, x):
    return {k: F(c) * cc for k, cc in x.items()} if c != 0 else {}


def ip(x, y):
    return sum(c * y.get(k, F(0)) for k, c in x.items())


def cre(k, x):
    return fock.cre_on(k, x)


def ann(k, x):
    return fock.ann_on(k, x)


def num(k, x):
    return cre(k, ann(k, x))


def pair(j):
    return 2 + 2 * j, 3 + 2 * j


def rot(j, c, s, x):
    """The rotor of pair j with cosine c: (1 - Pi) + c Pi + s h, h = v_a w_b - v_b w_a, Pi the one-quantum test."""
    a, b = pair(j)
    na, nb = num(a, x), num(b, x)
    nab = num(a, nb)
    Pi = vadd(na, nb, vsc(-2, nab))                      # n_a (1 - n_b) + n_b (1 - n_a)
    h = vadd(cre(a, ann(b, x)), vsc(-1, cre(b, ann(a, x))))
    return vadd(x, vsc(-1, Pi), vsc(c, Pi), vsc(s, h))


def couple(j, c, s, x):
    """U_j = off_0 + on_0 R_j."""
    on = num(0, x)
    return vadd(x, vsc(-1, on), rot(j, c, s, on))


def uncouple(j, c, s, x):
    """U_j^dagger = off_0 + on_0 R_j^dagger (the rotor with -s)."""
    on = num(0, x)
    return vadd(x, vsc(-1, on), rot(j, c, -s, on))


def branches(N, c, s, coupled):
    """Branch vectors after coupling the pairs in `coupled`: A (system on rung 0), B (on rung 1)."""
    base = {0: F(1)}
    for j in reversed(range(N)):
        base = cre(pair(j)[0], base)
    A, B = cre(0, base), cre(1, base)
    for j in sorted(coupled):
        A, B = couple(j, c, s, A), couple(j, c, s, B)
    return A, B


OPS = (lambda k, x: x, cre, ann, num)        # a basis of one rung's algebra: 1, v, w, v w


def apply_word(word, rungs, x):
    for op, k in zip(word, rungs):
        x = OPS[op](k, x)
        if not x:
            break
    return x


def interference(word, rungs, A, B):
    return AL * BE * (ip(A, apply_word(word, rungs, B)) + ip(B, apply_word(word, rungs, A)))


def check_fock_module_is_the_clifford_algebra_of_the_ladder_pairs():
    premise("tower.fock-module-one-qubit-per-rung")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    m = 3
    sq = tuple([1, -1] * m)
    gens = fock.fock_generators([(2 * j, 2 * j + 1) for j in range(m)], sq)
    ok = fock.clifford_ok(gens, sq, 2 ** m)
    for j in range(m):
        # v_j = (e_j + f_j)/2 is the wedge (creation) and w_j = (e_j - f_j)/2 the contraction
        vj = fock.msc(F(1, 2), fock.madd(gens[2 * j], gens[2 * j + 1]))
        wj = fock.msc(F(1, 2), fock.msub(gens[2 * j], gens[2 * j + 1]))
        ok = ok and fock.meq(vj, fock.cre(j, m)) and fock.meq(wj, fock.ann(j, m))
        ok = ok and fock.meq(fock.dag(vj), wj)                 # the adjoint of (P) is the Fock adjoint
    # the vector-level operators used below agree with the matrices
    for s in range(2 ** m):
        for j in range(m):
            ok = ok and cre(j, {s: F(1)}) == fock.apply(fock.cre(j, m), {s: F(1)})
            ok = ok and ann(j, {s: F(1)}) == fock.apply(fock.ann(j, m), {s: F(1)})
    GA.check("the Fock module carries Cl(3,3) with v_j the wedge, w_j the contraction, dagger the Fock adjoint", ok)
    return ok


def check_interference_factor_on_a_full_basis_for_three_pairs():
    premise("synthesis.premise-positivity-of-values")
    premise("tower.fock-module-one-qubit-per-rung")
    N = 3
    ok = True
    nonzero = {}
    for c, s in ((F(3, 5), F(4, 5)), (F(0), F(1))):
        A_N, B_N = branches(N, c, s, range(N))
        # the coupling is unitary on these vectors and leaves B alone
        ok = ok and ip(A_N, A_N) == 1 and ip(B_N, B_N) == 1 and ip(A_N, B_N) == 0
        ok = ok and B_N == branches(N, c, s, ())[1]
        count = 0
        for mask in range(2 ** N - 1):                       # every proper subset K of the pairs
            K = [j for j in range(N) if (mask >> j) & 1]
            rungs = [0, 1] + [r for j in K for r in pair(j)]
            A_K, B_K = branches(N, c, s, K)
            factor = c ** (N - len(K))
            for word in product(range(4), repeat=len(rungs)):   # a full linear basis of the algebra on these rungs
                lhs = interference(word, rungs, A_N, B_N)
                rhs = factor * interference(word, rungs, A_K, B_K)
                ok = ok and lhs == rhs
                if interference(word, rungs, A_K, B_K) != 0:
                    count += 1
        nonzero[c] = count
    # the comparison is not vacuous: basis elements with nonzero interference before the factor is applied
    ok = ok and nonzero[F(3, 5)] > 0 and nonzero[F(0)] > 0
    ok = ok and (nonzero[F(3, 5)], nonzero[F(0)]) == EXPECTED_NONZERO
    GA.check("N = 3: I_N(x) = c^(N-k) I_K(x) on a full basis of the algebra on the system and every proper K", ok)
    return ok


EXPECTED_NONZERO = (74, 14)   # basis elements with nonzero I_K, for c = 3/5 and c = 0


def bell_element(N, c, s, x):
    """O_N = U O_0 U^dagger applied to x, with O_0 = v_0 w_1 + v_1 w_0 and U the product of the couplings."""
    for j in reversed(range(N)):
        x = uncouple(j, c, s, x)
    x = vadd(cre(0, ann(1, x)), cre(1, ann(0, x)))
    for j in range(N):
        x = couple(j, c, s, x)
    return x


def check_interference_is_full_for_an_element_touching_every_pair():
    premise("synthesis.premise-positivity-of-values")
    ok = True
    for c, s in ((F(3, 5), F(4, 5)), (F(0), F(1))):
        for N in (1, 2, 3):
            m = 2 + 2 * N
            A, B = branches(N, c, s, range(N))
            psi = vadd(vsc(AL, A), vsc(BE, B))
            O = lambda x, N=N: bell_element(N, c, s, x)
            ok = ok and ip(psi, O(psi)) == F(24, 25)                  # value in the state after the couplings
            ok = ok and ip(A, O(A)) == 0 and ip(B, O(B)) == 0         # value in each branch
            ok = ok and AL * BE * (ip(A, O(B)) + ip(B, O(A))) == F(24, 25)
            # weights of the system's tests are those of the mixture
            ok = ok and ip(psi, num(0, psi)) == F(9, 25) and ip(psi, num(1, psi)) == F(16, 25)
            basis = [{t: F(1)} for t in range(2 ** m)]
            for x in basis:
                Ox = O(x)
                # even: it preserves the parity of the number of quanta
                (t,) = x.keys()
                ok = ok and all(bin(u).count("1") % 2 == bin(t).count("1") % 2 for u in Ox)
                # the square of O is idempotent
                O2x = O(Ox)
                ok = ok and O(O(O2x)) == O2x
            # self-adjoint
            for t in range(0, 2 ** m, 7):
                for u in range(0, 2 ** m, 5):
                    ok = ok and ip({t: F(1)}, O({u: F(1)})) == ip(O({t: F(1)}), {u: F(1)})
    GA.check("for N = 1, 2, 3 an even self-adjoint element touching every pair has interference 24/25", ok)
    return ok


def check_record_modes_differ_by_a_fixed_hilbert_schmidt_amount_per_pair():
    premise("synthesis.imported-powers-stormer-takesaki-disjointness")
    ok = True
    for c, s in ((F(3, 5), F(4, 5)), (F(0), F(1)), (F(5, 13), F(12, 13))):
        ok = ok and c * c + s * s == 1
        # one-quantum mode of the pair in each branch: (1, 0) and (c, -s); their projections
        Pb = [[F(1), F(0)], [F(0), F(0)]]
        Pa = [[c * c, -c * s], [-c * s, s * s]]
        hs2 = sum((Pa[i][j] - Pb[i][j]) ** 2 for i in range(2) for j in range(2))
        ok = ok and hs2 == 2 * s * s and hs2 > 0
        # the overlap of the two record vectors of one pair is c
        A, B = branches(1, c, s, [0])
        a_rec = ann(0, A)
        b_rec = ann(1, B)
        ok = ok and ip(a_rec, b_rec) == c
    GA.check("per pair the two record modes overlap by c and their projections differ by 2 s^2 in Hilbert-Schmidt norm squared", ok)
    return ok
