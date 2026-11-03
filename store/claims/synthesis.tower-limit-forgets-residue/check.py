"""synthesis.tower-limit-forgets-residue: exact checks on truncations of the towers.

Layout over Cl(p,q): ground generators 0..n-1 (first p of square +1); plane j (j >= 1) has
e_j = n + 2(j-1) (square +1) and f_j = n + 2(j-1) + 1 (square -1). The tower over Cl(0,0) uses the
same layout with n = 0 (primed frame). sigma: x_i -> e'_i (i <= p), x_{p+i} -> f'_i (i <= q),
e_j -> e'_{p+j}, f_j -> f'_{q+j}.

check_limit_forgets_residue:
  (i)   the frame bijection preserves squares and anticommutation (images computed and multiplied in
        GA.py), T_k lands in T'_{k+max(p,q)}, and the inverse map returns every generator;
  (iii) for odd n the elements u_i = x_i x_n present Cl^0(p,q) as Cl(p,q-1) (or Cl(0,p-1) for q = 0), of
        even residue, and generate all even blades; on floors of odd residue the centre is spanned by 1 and
        the volume element, and the elements of T_k commuting with the next plane's generators and with
        T_k are the scalars; for even residue the floor centre is R.
"""
from fractions import Fraction as F
import GA
from GA import mul, gen, sc, eq, add, commutes, all_blades, sig
from tp_premise import premise


def floor_squares(p, q, k):
    return tuple([1] * p + [-1] * q) + (1, -1) * k


def sigma(p, q, g):
    """index of the image of generator g of the tower over (p,q) in the tower over (0,0)"""
    n = p + q
    if g < p:
        return 2 * g                         # e'_{g+1}
    if g < n:
        return 2 * (g - p) + 1               # f'_{g-p+1}
    j = (g - n) // 2 + 1
    if (g - n) % 2 == 0:
        return 2 * (p + j - 1)               # e'_{p+j}
    return 2 * (q + j - 1) + 1               # f'_{q+j}


def sigma_inv(p, q, h):
    n = p + q
    j = h // 2 + 1
    if h % 2 == 0:
        return j - 1 if j <= p else n + 2 * (j - p - 1)
    return p + j - 1 if j <= q else n + 2 * (j - q - 1) + 1


def centre_blades(sq):
    m = len(sq)
    return [B for B in all_blades(m)
            if all(commutes(gen(g), {B: F(1)}, sq) for g in range(m))]


def check_limit_forgets_residue():
    premise("tower.algebraic-limit-even-charge")
    premise("tower.grade-twist-when-it-inner")
    premise("tower.structure-tower-c-norms")
    premise("tower.car-limit-even-charge")
    premise("synthesis.plane-commutant-even-ground")
    sigs = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1), (2, 1), (1, 2), (3, 0), (0, 3), (1, 3), (3, 1), (2, 2)]
    for (p, q) in sigs:
        n = p + q
        for k in (0, 1, 2):
            src = floor_squares(p, q, k)
            K = k + max(p, q)
            tgt = floor_squares(0, 0, K)
            gens = list(range(n + 2 * k))
            img = {g: sigma(p, q, g) for g in gens}
            assert len(set(img.values())) == len(gens)                       # injective
            for a in gens:
                assert img[a] < 2 * K                                          # lands in T'_{k+max(p,q)}
                assert tgt[img[a]] == src[a]                                   # squares preserved
                ia = gen(img[a])
                assert eq(mul(ia, ia, tgt), sc(src[a]))
                for b in gens:
                    if a < b:
                        assert add(mul(ia, gen(img[b]), tgt), mul(gen(img[b]), ia, tgt)) == {}
                assert sigma_inv(p, q, img[a]) == a                            # Psi Phi = id on generators
            for h in range(2 * k):                                             # Psi: T'_k into T_k
                assert sigma_inv(p, q, h) < n + 2 * k
                assert sigma(p, q, sigma_inv(p, q, h)) == h                    # Phi Psi = id on generators
                assert floor_squares(p, q, k)[sigma_inv(p, q, h)] == floor_squares(0, 0, k)[h]
    GA.check("(i): the frame bijection is square-preserving, T_k -> T'_{k+max(p,q)}, T'_k -> T_k, "
             "and inverse to Psi on generators", True)

    for (p, q) in [(1, 0), (0, 1), (2, 1), (1, 2), (3, 0), (0, 3), (3, 2), (2, 3), (4, 1), (1, 4), (5, 0)]:
        n = p + q
        sq = sig(p, q)
        u = [mul(gen(i), gen(n - 1), sq) for i in range(n - 1)]
        want = [sq[i] for i in range(n - 1)] if q >= 1 else [-1] * (n - 1)
        for i in range(n - 1):
            assert eq(mul(u[i], u[i], sq), sc(want[i]))
            for j in range(i + 1, n - 1):
                assert add(mul(u[i], u[j], sq), mul(u[j], u[i], sq)) == {}
        pp = sum(1 for w in want if w == 1)
        assert (pp - (n - 1 - pp)) % 2 == 0                                    # even residue
        span = set()
        for B in all_blades(n - 1):                                            # products of u's
            x = sc(1)
            for i in B:
                x = mul(x, u[i], sq)
            assert len(x) == 1
            span.add(next(iter(x)))
        assert span == {B for B in all_blades(n) if len(B) % 2 == 0}         # all even blades
    GA.check("(iii): u_i = x_i x_n present Cl^0(p,q) as Cl(p,q-1) or Cl(0,p-1), of even residue", True)

    for (p, q) in [(1, 0), (0, 1), (2, 1), (0, 3), (1, 2), (3, 0)]:
        n = p + q
        for k in (0, 1, 2):
            sq = floor_squares(p, q, k)
            m = n + 2 * k
            assert sorted(centre_blades(sq)) == [(), tuple(range(m))]          # centre span{1, omega}
            nxt = floor_squares(p, q, k + 1)
            surv = [B for B in centre_blades(sq)
                    if commutes(gen(m), {B: F(1)}, nxt) and commutes(gen(m + 1), {B: F(1)}, nxt)]
            assert surv == [()]                                                # only R survives
    for (p, q) in [(0, 0), (1, 1), (2, 0), (0, 2), (1, 3)]:
        for k in (0, 1):
            assert centre_blades(floor_squares(p, q, k)) == [()]               # even residue: centre R
    GA.check("(iii): odd-residue floors have centre span{1, omega}; only R commutes with the next plane", True)
    return True
