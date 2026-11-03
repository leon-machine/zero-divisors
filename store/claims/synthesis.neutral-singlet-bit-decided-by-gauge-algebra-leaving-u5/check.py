"""synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5: exact checks.

Five fermionic modes on Lambda(C^5) (fock.py, LSB bitmask basis, Jordan-Wigner signs): modes 0, 1 the slot
modes, modes 2, 3, 4 the pair modes; n, k the slot and pair numbers, N = n + k, Y = (3n - 2k)/6. so(10) is
spanned by the bilinears: u(5) = {a_i* a_j} (number conserving, 25) and p = {a_i* a_j*, a_i a_j : i < j}
(pair creation and annihilation, 20). Gamma = (-1)^N; Gamma' = (-1)^N - 2 P_Omega + 2 P_top, the vacuum-swapped
halving of the stored ladder. Every commutation statement is a linear condition, so it is tested on a basis
of the complex span of each algebra (real matrices only; no complex unit needed).
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

M = 5
DIM = 2 ** M
TOP = DIM - 1
ONE = fock.eye(DIM)
SLOT = (0, 1)
PAIR = (2, 3, 4)
YMODE = {0: F(1, 2), 1: F(1, 2), 2: F(-1, 3), 3: F(-1, 3), 4: F(-1, 3)}


def cre(k):
    return fock.cre(k, M)


def ann(k):
    return fock.ann(k, M)


def bil(i, j):
    return fock.mm(cre(i), ann(j))


def deg(s):
    return fock.popcount(s)


def diag(fn):
    return {(s, s): F(fn(s)) for s in range(DIM) if fn(s) != 0}


YOP = diag(lambda s: sum((YMODE[k] for k in range(M) if s >> k & 1), F(0)))
PARITY = fock.parity(M)
PVAC = diag(lambda s: 1 if s == 0 else 0)
PTOP = diag(lambda s: 1 if s == TOP else 0)
GSWAP = fock.madd(fock.msub(PARITY, fock.msc(2, PVAC)), fock.msc(2, PTOP))
SWAP = fock.madd(fock.msub(fock.msub(ONE, PVAC), PTOP), {(0, TOP): F(1), (TOP, 0): F(1)})

U5 = [((i, j), bil(i, j)) for i in range(M) for j in range(M)]
PCRE = [((i, j), fock.mm(cre(i), cre(j))) for i in range(M) for j in range(i + 1, M)]
PANN = [((i, j), fock.mm(ann(j), ann(i))) for i in range(M) for j in range(i + 1, M)]

# the Standard Model gauge algebra (complex span): u(2) traceless on the slots, su(3) on the pairs, Y
SM = [bil(0, 1), bil(1, 0), fock.msub(bil(0, 0), bil(1, 1))]
SM += [bil(a, b) for a in PAIR for b in PAIR if a != b]
SM += [fock.msub(bil(2, 2), bil(3, 3)), fock.msub(bil(3, 3), bil(4, 4)), YOP]
SLOTBIL = [bil(i, j) for i in SLOT for j in SLOT] + [fock.mm(cre(0), cre(1)), fock.mm(ann(1), ann(0))]
PAIRBIL = [bil(i, j) for i in PAIR for j in PAIR] \
    + [fock.mm(cre(i), cre(j)) for i in PAIR for j in PAIR if i < j] \
    + [fock.mm(ann(j), ann(i)) for i in PAIR for j in PAIR if i < j]
BMINUSL = diag(lambda s: sum((F(-1, 3) for k in PAIR if s >> k & 1), F(0)))  # B - L up to a central constant
ALGEBRAS = {
    "sm": (SM, False),
    "sm + total mode number": (SM + [fock.num_total(M)], False),
    "u(5) (Georgi-Glashow with U(1)_X)": ([X for _, X in U5], False),
    "sm + B - L": (SM + [BMINUSL], False),
    "left-right su(3) + su(2)_L + su(2)_R + u(1)_{B-L}": (SM + SLOTBIL + [BMINUSL], True),
    "Pati-Salam so(4) + so(6)": (SLOTBIL + PAIRBIL, True),
    "su(4) + su(2)_L + u(1)": (SM + PAIRBIL, True),
    "flipped u(5)": ([bil(i, j) for i in SLOT for j in SLOT] + [bil(i, j) for i in PAIR for j in PAIR]
                     + [fock.mm(ann(i), ann(j)) for i in SLOT for j in PAIR]
                     + [fock.mm(cre(j), cre(i)) for i in SLOT for j in PAIR], True),
    "so(10)": ([X for _, X in U5] + [X for _, X in PCRE] + [X for _, X in PANN], True),
}


def commutes(A, B):
    return fock.is_zero(fock.comm(A, B))


def solve_affine(eqs, nvar):
    """eqs: list of (coeff list, const) meaning sum c_i x_i + const = 0. Returns (consistent, rank, particular)."""
    rows = [list(c) + [k] for c, k in eqs if any(c) or k]
    rk = 0
    piv_cols = []
    for col in range(nvar):
        piv = next((r for r in range(rk, len(rows)) if rows[r][col] != 0), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        p = rows[rk][col]
        rows[rk] = [x / p for x in rows[rk]]
        for r in range(len(rows)):
            if r != rk and rows[r][col] != 0:
                f = rows[r][col]
                rows[r] = [a - f * b for a, b in zip(rows[r], rows[rk])]
        piv_cols.append(col)
        rk += 1
    consistent = all(any(r[:nvar]) or r[nvar] == 0 for r in rows)
    sol = [F(0)] * nvar
    for r, col in enumerate(piv_cols):
        sol[col] = -rows[r][nvar]
    return consistent, rk, sol


def neutral_block_solutions(gens, s):
    """Involutions Gamma = s(-1)^N on the charged states plus an unknown 2 x 2 block on (Omega, top):
    Gamma Omega = a Omega + c top, Gamma top = b Omega + d top. Returns (consistent, rank, (a, b, c, d))."""
    base = {(t, t): F(s * (-1) ** deg(t)) for t in range(1, TOP)}
    units = [{(0, 0): F(1)}, {(0, TOP): F(1)}, {(TOP, 0): F(1)}, {(TOP, TOP): F(1)}]  # a, b, c, d
    eqs = []
    for g in gens:
        c0 = fock.comm(base, g)
        cs = [fock.comm(u, g) for u in units]
        keys = set(c0) | set(k for c in cs for k in c)
        for key in keys:
            eqs.append(([c.get(key, F(0)) for c in cs], c0.get(key, F(0))))
    return solve_affine(eqs, 4)


def check_hypercharge_grading_splits_so10():
    """ad(Y) acts on u(5) with eigenvalues {0, +-5/6} and on p with {+-1, +-1/6, +-2/3}: disjoint, so every
    ad(Y)-stable subspace of so(10) (any algebra containing Y) is its part in u(5) plus its part in p; the
    creation eigenvalues {1, 1/6, -2/3} and the annihilation ones {-1, -1/6, 2/3} are disjoint too."""
    premise("standard-model.hyp-s-slot-statistics")
    ev_u5, ev_cre, ev_ann = set(), set(), set()
    ok = True
    for (i, j), X in U5:
        lam = YMODE[i] - YMODE[j]
        ok = ok and fock.meq(fock.comm(YOP, X), fock.msc(lam, X))
        ev_u5.add(lam)
    for (i, j), X in PCRE:
        lam = YMODE[i] + YMODE[j]
        ok = ok and fock.meq(fock.comm(YOP, X), fock.msc(lam, X))
        ev_cre.add(lam)
    for (i, j), X in PANN:
        lam = -(YMODE[i] + YMODE[j])
        ok = ok and fock.meq(fock.comm(YOP, X), fock.msc(lam, X))
        ev_ann.add(lam)
    GA.check("ad(Y) eigenvectors on the bilinear basis", ok)
    GA.check("u(5) eigenvalues 0, +-5/6", ev_u5 == {F(0), F(5, 6), F(-5, 6)})
    GA.check("creation eigenvalues 1, 1/6, -2/3", ev_cre == {F(1), F(1, 6), F(-2, 3)})
    GA.check("annihilation eigenvalues -1, -1/6, 2/3", ev_ann == {F(-1), F(-1, 6), F(2, 3)})
    GA.check("the three sets are disjoint", not (ev_u5 & ev_cre) and not (ev_u5 & ev_ann) and not (ev_cre & ev_ann))
    GA.check("dimensions 25 + 10 + 10 = 45", len(U5) == 25 and len(PCRE) == 10 and len(PANN) == 10)
    return True


def check_swapped_halving_fails_on_every_element_of_p():
    """Gamma commutes with all of so(10); Gamma' commutes with u(5) and with no nonzero element of p: the
    columns of [Gamma', x] at Omega (creation x) and at the top state (annihilation x) are 20 independent
    vectors, so x -> [Gamma', x] is injective on p."""
    premise("synthesis.spin10-clause-content-is-the-neutral-singlet-choice")
    GA.check("Gamma' is an involution of trace zero", fock.meq(fock.mm(GSWAP, GSWAP), ONE)
             and sum(GSWAP.get((t, t), F(0)) for t in range(DIM)) == 0)
    GA.check("Gamma' = S (-1)^N S", fock.meq(fock.mm(SWAP, fock.mm(PARITY, SWAP)), GSWAP))
    GA.check("Gamma commutes with so(10)", all(commutes(PARITY, X) for _, X in U5 + PCRE + PANN))
    GA.check("Gamma' commutes with u(5)", all(commutes(GSWAP, X) for _, X in U5))
    cols = []
    for _, X in PCRE:
        C = fock.comm(GSWAP, X)
        cols.append({r: v for (r, c), v in C.items() if c == 0})
    for _, X in PANN:
        C = fock.comm(GSWAP, X)
        cols.append({r: v for (r, c), v in C.items() if c == TOP})
    keys = sorted({r for c in cols for r in c})
    eqs = [([c.get(r, F(0)) for c in cols], F(0)) for r in keys]
    # rank of the 20 columns = rank of the transposed system
    _, rk, _ = solve_affine(eqs, len(cols))
    GA.check("x -> [Gamma', x] injective on p (rank 20)", rk == 20)
    return True


def check_neutral_block_fixed_by_one_pair_of_p():
    """With the anomaly-free charged chirality s(-1)^N (stored) and an unknown 2 x 2 block on the neutral
    singlets: the Standard Model leaves the whole block free (rank 0); u(5) or the total mode number make it
    diagonal (rank 2); each single element of p together with its adjoint fixes it to Gamma = s(-1)^N
    (rank 4, a = s, d = -s, b = c = 0); a creation element alone fixes a = s, b = 0, d = -s and leaves c (the
    Omega-to-top entry) free (rank 3): the involution with c = 1 commutes with sm and x but not with x^dagger."""
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    premise("synthesis.spin10-clause-content-is-the-neutral-singlet-choice")
    for s in (1, -1):
        cons, rk, _ = neutral_block_solutions(SM, s)
        GA.check(f"s={s}: sm leaves the neutral block free", cons and rk == 0)
        cons, rk, sol = neutral_block_solutions(SM + [fock.num_total(M)], s)
        GA.check(f"s={s}: total mode number makes the block diagonal", cons and rk == 2 and sol[1] == 0 and sol[2] == 0)
        for ((i, j), X), (_, Xd) in zip(PCRE, PANN):
            cons, rk, sol = neutral_block_solutions(SM + [X, Xd], s)
            GA.check(f"s={s}: v{i}v{j} and its adjoint fix the block", cons and rk == 4
                     and sol == [F(s), F(0), F(0), F(-s)])
            cons, rk, _ = neutral_block_solutions(SM + [X], s)
            GA.check(f"s={s}: v{i}v{j} alone fixes three of four entries", cons and rk == 3)
            Gc = {(t, t): F(s * (-1) ** deg(t)) for t in range(DIM)}
            Gc[(TOP, 0)] = F(1)
            GA.check(f"s={s}: v{i}v{j}: the free entry is c", fock.meq(fock.mm(Gc, Gc), ONE)
                     and all(commutes(Gc, g) for g in SM + [X]) and not commutes(Gc, Xd))
    return True


def check_intermediate_gauge_algebras():
    """For each algebra between sm and so(10): it lies in u(5) iff Gamma' commutes with it; Gamma = (-1)^N
    commutes with all; for the algebras leaving u(5) the neutral block is fixed to s(-1)^N, for those inside
    it two neutral choices (or the free block) remain. Pati-Salam is the 21 split-preserving bivectors."""
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    u5set = [X for _, X in U5]
    GA.check("Pati-Salam basis has 6 + 15 = 21 elements", len(SLOTBIL) + len(PAIRBIL) == 21)
    for name, (gens, leaves) in ALGEBRAS.items():
        GA.check(f"{name}: contains Y", any(fock.meq(g, YOP) for g in gens) or _in_span(YOP, gens))
        inside = all(_in_span(g, u5set) for g in gens)
        GA.check(f"{name}: leaves u(5) as registered", inside == (not leaves))
        GA.check(f"{name}: Gamma commutes", all(commutes(PARITY, g) for g in gens))
        GA.check(f"{name}: Gamma' commutes iff inside u(5)", all(commutes(GSWAP, g) for g in gens) == inside)
        cons, rk, sol = neutral_block_solutions(gens, 1)
        if leaves:
            GA.check(f"{name}: block fixed to (-1)^N", cons and rk == 4 and sol == [F(1), F(0), F(0), F(-1)])
        else:
            GA.check(f"{name}: block not fixed", cons and rk < 4)
    return True


def _in_span(X, gens):
    keys = sorted(set(X) | set(k for g in gens for k in g))
    eqs = [([g.get(key, F(0)) for g in gens], -X.get(key, F(0))) for key in keys]
    cons, _, _ = solve_affine(eqs, len(gens))
    return cons


def odd_monomials(grades):
    gam = [fock.majorana(p, M, kind="real") for p in range(2 * M)]
    out = []

    def rec(start, chosen):
        if len(chosen) in grades:
            P = ONE
            for p in chosen:
                P = fock.mm(P, gam[p])
            out.append((tuple(chosen), P))
        if len(chosen) == max(grades):
            return
        for p in range(start, 2 * M):
            rec(p + 1, chosen + [p])
    rec(0, [])
    return out


def form(B, psi, X, phi):
    """B(e_psi, X e_phi) for basis states."""
    col = {r: v for (r, c), v in X.items() if c == phi}
    return sum((B.get((psi, r), F(0)) * v for r, v in col.items()), F(0))


def check_yukawa_forms_see_the_bit():
    """With the stored invariant pairing B: under Gamma = (-1)^N the empty state pairs with the lepton
    doublet (one slot, three pairs) through a slot vector (the rung direction), the Dirac coupling; under
    Gamma' the full state pairs with no other state of its half through any odd-grade Clifford element
    (grades 1, 3, 5: the 10, 120, 126 forms), while the charged entries are unchanged; it pairs with the
    lepton doublet only through grade four."""
    exp = premise("standard-model.invariant-pairing-five-modes")
    premise("standard-model.hyp-s-slot-statistics")
    premise("synthesis.spin10-clause-content-is-the-neutral-singlet-choice")
    B = exp["pairing"]()
    # control: B is so(10)-invariant in this labelling of the modes
    GA.check("B invariant under a creation and a mixing bilinear",
             all(fock.is_zero(fock.madd(fock.mm(fock.transpose(X), B), fock.mm(B, X)))
                 for X in (fock.mm(cre(0), cre(3)), bil(1, 4))))
    halfG = [t for t in range(DIM) if deg(t) % 2 == 0]
    halfS = [t for t in range(1, TOP) if deg(t) % 2 == 0] + [TOP]
    lepton = [t for t in range(DIM) if fock.popcount(t & 3) == 1 and fock.popcount(t >> 2) == 3]
    GA.check("two lepton-doublet states in both halves", len(lepton) == 2 and all(t in halfG and t in halfS for t in lepton))
    slot_vecs = [fock.majorana(p, M, kind="real") for p in range(4)]
    dirac = [form(B, L, c, 0) for L in lepton for c in slot_vecs]
    GA.check("Gamma: rung vectors pair the lepton doublet with the empty state", sum(1 for x in dirac if x != 0) >= 2)
    odd = odd_monomials({1, 3, 5})
    GA.check("10 + 120 + 252 odd monomials of grades 1, 3, 5", len(odd) == 382)
    others = [t for t in halfS if t != TOP]
    dead = all(form(B, TOP, X, t) == 0 and form(B, t, X, TOP) == 0 for _, X in odd for t in others)
    GA.check("Gamma': the full state has no odd-grade pairing with any other state of its half", dead)
    selfm = any(form(B, TOP, X, TOP) != 0 for _, X in odd)
    GA.check("Gamma': the full state keeps an odd-grade self pairing (Majorana)", selfm)
    charged_same = [t for t in halfG if t != 0] == others
    GA.check("the charged states of the two halves coincide", charged_same)
    even4 = odd_monomials({4})
    lep4 = any(form(B, L, X, TOP) != 0 for L in lepton for _, X in even4)
    GA.check("Gamma': lepton doublet pairs with the full state through grade four", len(even4) == 210 and lep4)
    lepodd = any(form(B, L, X, TOP) != 0 for L in lepton for _, X in odd)
    GA.check("Gamma': and through no odd grade", not lepodd)
    return True


def check_clifford_cpt_antiunitary_is_blind():
    """Theta = U K, U = product of the five real Majoranas a_k* + a_k, K complex conjugation in the occupation
    basis: Theta commutes with every Hermitian Majorana (a_k* + a_k and i(a_k* - a_k)), so with Spin(10); it
    carries Omega to the top state, commutes with the swap S and reverses both Gamma and Gamma'. The Clifford
    CPT conjugation therefore exchanges the halves of both candidates and does not decide the bit."""
    premise("synthesis.spin10-clause-content-is-the-neutral-singlet-choice")
    premise("standard-model.hyp-s-slot-statistics")
    re_maj = [fock.madd(cre(k), ann(k)) for k in range(M)]
    im_maj_over_i = [fock.msub(cre(k), ann(k)) for k in range(M)]  # i times this is Hermitian; K flips its sign
    U = ONE
    for g in re_maj:
        U = fock.mm(U, g)
    GA.check("U^2 = +-1", fock.meq(fock.mm(U, U), ONE) or fock.meq(fock.mm(U, U), fock.msc(-1, ONE)))
    Uinv = U if fock.meq(fock.mm(U, U), ONE) else fock.msc(-1, U)
    GA.check("Theta fixes the real Majoranas", all(fock.meq(fock.mm(U, fock.mm(g, Uinv)), g) for g in re_maj))
    GA.check("Theta fixes i(a* - a): U (a* - a) U^-1 = -(a* - a)",
             all(fock.meq(fock.mm(U, fock.mm(g, Uinv)), fock.msc(-1, g)) for g in im_maj_over_i))
    img = fock.apply(U, {0: F(1)})
    GA.check("Theta Omega = +- top", set(img) == {TOP} and abs(img[TOP]) == 1)
    GA.check("Theta commutes with S", fock.meq(fock.mm(U, fock.mm(SWAP, Uinv)), SWAP))
    GA.check("Theta Gamma Theta^-1 = -Gamma", fock.meq(fock.mm(U, fock.mm(PARITY, Uinv)), fock.msc(-1, PARITY)))
    GA.check("Theta Gamma' Theta^-1 = -Gamma'", fock.meq(fock.mm(U, fock.mm(GSWAP, Uinv)), fock.msc(-1, GSWAP)))
    return True
