"""synthesis.invariant-forms-on-spinor-ideal-factor-through-reversion: exact checks.

Signatures (p, q): p generators of square +1, q of square -1, n = p + q, residue r = p - q mod 8,
causal when min(p, q) = 1, the time being the minority-sign generator. T14c's spinor ideal
S = Cl0(V) f with f = (1 + e_t e_a)/2 (obj.dark-tower-matter.ideals-fields-momentum); in dimension
six f carries the chiral factor (1 +- w)/2, in dimension two the two ideals are spanned by
(1 +- e_t e_a)/2 (synthesis.lowest-causal-residues-zero-four-content). The spin Lie algebra acts on S
by left multiplication by bivectors; a bilinear form B on S x S' is invariant when
B(b psi, phi) + B(psi, b phi) = 0 for every bivector b.
The check:
  (a) at the nine causal signatures of dimensions two to six, for every ideal (both chiralities in
      dimensions two and six), the space of invariant forms is computed as a kernel, and the forms
      psi, phi -> (component of rev(psi) phi on a blade) are shown to span exactly that space; its
      dimension is 0 at (1,1), (1,5), (5,1) for one ideal, and 1 and 4 on S+ x S-;
  (b) the ingredients of the general proof for every signature with 2 <= n <= 7: products of
      bivector blades span the even subalgebra, and rev(w) = -w exactly when n = 2 or 3 mod 4;
      and the adjoint identity B(a psi, phi) = B(psi, rev(a) phi) for every even blade a, on every
      invariant form at (1,4) and (4,1);
  (c) the symmetry types: at n = 3, 4 every invariant form is alternating, at n = 5 a symmetric one
      exists, so the least number of constituents with a nonzero invariant pairing is 2, 2, 1, the
      thresholds of dark-tower-matter.where-mass-begins, and there is none at n = 2, 6.
"""
from fractions import Fraction as F
import GA
from GA import mul, add, sub, scal, sc, gen, reverse, all_blades, rank_of_vectors, field_kernel
from tp_premise import premise


def squares(p, q):
    return tuple([1] * p + [-1] * q)


def pseudo(n):
    return {tuple(range(n)): F(1)}


def setup(p, q, chiral=0):
    n, s = p + q, squares(p, q)
    t = 0 if p == 1 else p
    a = 1 if t == 0 else 0
    f = scal(F(1, 2), add(sc(1), mul(gen(t), gen(a), s)))
    if chiral:
        f = mul(f, scal(F(1, 2), add(sc(1), scal(chiral, pseudo(n)))), s)
    assert mul(f, f, s) == f
    blades = all_blades(n)
    even = [B for B in blades if len(B) % 2 == 0]
    rows, S = [], []
    for B in even:
        g = mul({B: F(1)}, f, s)
        cand = rows + [[g.get(C, F(0)) for C in blades]]
        if g and rank_of_vectors(cand) == len(cand):
            rows, S = cand, S + [g]
    return dict(n=n, s=s, f=f, S=S, blades=blades)


def ideals(p, q):
    n = p + q
    if n == 2:
        D = setup(p, q)
        D2 = dict(D)
        D2["f"] = sub(sc(1), D["f"])
        D2["S"] = [D2["f"]]
        return [D, D2]
    if n == 6:
        return [setup(p, q, chiral=1), setup(p, q, chiral=-1)]
    return [setup(p, q)]


def coords(v, S, blades):
    cols = len(S)
    M = [[S[i].get(B, F(0)) for i in range(cols)] + [v.get(B, F(0))] for B in blades]
    r = 0
    for c in range(cols):
        piv = next(i for i in range(r, len(M)) if M[i][c] != 0)
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                g = M[i][c]
                M[i] = [x - g * y for x, y in zip(M[i], M[r])]
        r += 1
    assert all(M[i][cols] == 0 for i in range(r, len(M)))
    return [M[i][cols] for i in range(cols)]


def rep(D, X):
    return [coords(mul(X, v, D["s"]), D["S"], D["blades"]) for v in D["S"]]


def invariant_forms(D, D2):
    n = D["n"]
    d1, d2 = len(D["S"]), len(D2["S"])
    eqs = []
    for i in range(n):
        for j in range(i + 1, n):
            b = {(i, j): F(1)}
            A, Bm = rep(D, b), rep(D2, b)
            for k in range(d1):
                for l in range(d2):
                    row = [F(0)] * (d1 * d2)
                    for m in range(d1):
                        row[m * d2 + l] += A[k][m]
                    for m in range(d2):
                        row[k * d2 + m] += Bm[l][m]
                    eqs.append(row)
    return field_kernel(eqs)


def reversion_components(D, D2):
    d1, d2 = len(D["S"]), len(D2["S"])
    comps = {}
    for a in range(d1):
        for b in range(d2):
            x = mul(reverse(D["S"][a]), D2["S"][b], D["s"])
            for C, c in x.items():
                comps.setdefault(C, [F(0)] * (d1 * d2))[a * d2 + b] = c
    return list(comps.values())


def span_dims(D, D2):
    ker = invariant_forms(D, D2)
    comps = reversion_components(D, D2)
    rk = rank_of_vectors(comps) if comps else 0
    joint = rank_of_vectors(comps + ker) if (comps or ker) else 0
    return len(ker), rk, joint, ker


CAUSAL_LOW = [(1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (1, 4), (4, 1), (1, 5), (5, 1)]


def check_invariant_forms_factor_through_reversion():
    premise("synthesis.reversion-pairing-vanishes-residues-zero-four")
    premise("synthesis.lowest-causal-residues-zero-four-content")
    dims, zero_at = {}, set()
    for (p, q) in CAUSAL_LOW:
        for D in ideals(p, q):
            k, rk, joint, _ = span_dims(D, D)
            # every invariant form is a functional of the reversion pairing, and conversely
            assert k == rk == joint
            dims.setdefault((p, q), set()).add(k)
            if k == 0:
                zero_at.add((p, q))
    assert zero_at == {(1, 1), (1, 5), (5, 1)}
    assert dims == {(1, 1): {0}, (1, 2): {1}, (2, 1): {1}, (1, 3): {2}, (3, 1): {2},
                    (1, 4): {4}, (4, 1): {4}, (1, 5): {0}, (5, 1): {0}}
    assert {(p - q) % 8 for (p, q) in zero_at} == {0, 4}
    # opposite chiralities pair: the vector-like alternative carries forms
    cross = {}
    for (p, q) in ((1, 1), (1, 5), (5, 1)):
        Dp, Dm = ideals(p, q)
        k, rk, joint, _ = span_dims(Dp, Dm)
        assert k == rk == joint
        cross[(p, q)] = k
    assert cross == {(1, 1): 1, (1, 5): 4, (5, 1): 4}
    return True


def check_general_proof_ingredients():
    premise("synthesis.reversion-pairing-vanishes-residues-zero-four")
    seen = 0
    for n in range(2, 8):
        for p in range(n + 1):
            q = n - p
            s = squares(p, q)
            even = [B for B in all_blades(n) if len(B) % 2 == 0]
            biv = [{B: F(1)} for B in even if len(B) == 2]
            # products of bivector blades are signed blades: close the set of reached blades
            reached, frontier = set(), list(biv)
            while frontier:
                x = frontier.pop()
                (B, c), = x.items()
                if B in reached:
                    continue
                reached.add(B)
                frontier.extend(mul(x, y, s) for y in biv)
            assert reached == set(even) and len(reached) == 2 ** (n - 1)
            w = pseudo(n)
            assert (reverse(w) == scal(-1, w)) == (n % 4 in (2, 3))
            seen += 1
    assert seen == 33
    # the adjoint identity on every invariant form at (1,4) and (4,1)
    for (p, q) in ((1, 4), (4, 1)):
        D = ideals(p, q)[0]
        d, s = len(D["S"]), D["s"]
        ker = invariant_forms(D, D)
        assert len(ker) == 4
        even = [B for B in all_blades(D["n"]) if len(B) % 2 == 0]
        for v in ker:
            Bm = [[v[a * d + b] for b in range(d)] for a in range(d)]
            for B in even:
                A = rep(D, {B: F(1)})
                Ar = rep(D, reverse({B: F(1)}))
                for k in range(d):
                    for l in range(d):
                        lhs = sum(A[k][m] * Bm[m][l] for m in range(d))
                        rhs = sum(Ar[l][m] * Bm[k][m] for m in range(d))
                        assert lhs == rhs
    return True


def check_symmetry_types_give_mass_thresholds():
    premise("dark-tower-matter.where-mass-begins")
    premise("synthesis.reversion-pairing-vanishes-residues-zero-four")
    threshold, types = {}, {}
    for (p, q) in CAUSAL_LOW:
        D = ideals(p, q)[0]
        d = len(D["S"])
        ker = invariant_forms(D, D)
        sym = anti = 0
        for v in ker:
            Bm = [[v[a * d + b] for b in range(d)] for a in range(d)]
            sym += all(Bm[a][b] == Bm[b][a] for a in range(d) for b in range(d))
            anti += all(Bm[a][b] == -Bm[b][a] for a in range(d) for b in range(d))
        types[(p, q)] = (len(ker), sym, anti)
        # a nonzero invariant pairing of one constituent with itself exists iff some form is
        # not alternating (char 0: alternating iff B(psi, psi) = 0 for all psi)
        not_alt = any(v[a * d + a] != 0 or any(v[a * d + b] != -v[b * d + a]
                                                for b in range(d)) for v in ker for a in range(d))
        n = p + q
        if not ker:
            threshold[n] = None
        else:
            threshold[n] = 1 if not_alt else 2
    assert types == {(1, 1): (0, 0, 0), (1, 2): (1, 0, 1), (2, 1): (1, 0, 1), (1, 3): (2, 0, 2),
                     (3, 1): (2, 0, 2), (1, 4): (4, 1, 3), (4, 1): (4, 1, 3), (1, 5): (0, 0, 0),
                     (5, 1): (0, 0, 0)}
    # the thresholds of where-mass-begins: two at n = 3, 4, one at n = 5; none at n = 2, 6
    assert threshold == {2: None, 3: 2, 4: 2, 5: 1, 6: None}
    return True
