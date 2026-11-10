import sys
d = sys.argv[1] + '/'
s = open(d + 'entity.md').read()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("kind: claim\nversion: 3\n", "kind: claim\nversion: 4\n")
rep("""  source: maintainer pass 2026-11-07 (resolve units)
review: draft
""", """  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Fable 5.2
  role: 'restatement of clause (iii) for even states on the mode split of the Clifford algebra (one parity sector)'
  version: 4
  source: run 2026-11-09-bridges
amendments:
- version: 4
  kind: restatement
  defect: 'Clause (iii) gave the random-state moments for an abstract tensor product only; the states of the modes left by the parity average are even and lie in one parity sector, which is not a tensor product, and there a permutation of genus g carries the weight 4^g and the denominator is prod(d^2/2 + l). The limit C_n and the gap of clause (iv) are unchanged. The premise synthesis.imported-haar-average-purity, used only to name the index-two value, is dropped.'
  evidence: check.py::check_parity_sector_moments_keep_the_catalan_limit
review: draft
""")
rep("""  - synthesis.imported-haar-average-purity@2
""", "")
rep("""  - synthesis.imported-non-crossing-permutations-are-geodesic@1
  proof: proof-main.tex""", """  - synthesis.imported-non-crossing-permutations-are-geodesic@1
  - tower.commuting-copies@5
  proof: proof-main.tex""")
rep("""  ref: check.py::check_gap_family_interpolates_half_nat_to_ln4
""", """  ref: check.py::check_gap_family_interpolates_half_nat_to_ln4
- kind: check
  ref: check.py::check_parity_sector_moments_keep_the_catalan_limit
""")
rep("""extraction:
""", """extraction:
  restatement_mode_split:
    by: run 2026-11-09-bridges
    date: '2026-11-09'
    note: >-
      Version 3 -> 4, at Leon's request that the tensor product of the eviction comparisons be replaced by the
      split in the algebra of the modes (sub-Clifford algebras, reduction by projection onto blades). Clauses
      (i), (ii), (iv) are unchanged: the eviction state is an even product of pair states and its reductions
      are the same on the two splits. Clause (iii) now states the moments for a random even state (one parity
      sector) and keeps the value for an abstract tensor product beside it; the limit C_n is the same. The
      premise synthesis.imported-haar-average-purity is dropped from the derivation and its claimref from the
      proof (Leon's decision to retire that Fact); the index-two value is the n = 2 case of the formula.
      Intended citations, not made because they are proposals of the same session: the split and the twist are
      synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product; the sector form
      of the moments is clause (iv) of
      synthesis.finite-normaliser-averages-leave-the-haar-moments-at-order-four-and-on-a-parity-sector, repeated
      in the proof only to keep it closed; version 4 of synthesis.eviction-keeps-one-replica-saddle (also a
      proposal) carries the same restatement at index two, and the pin on that theorem stays at the stored
      version 3 until the maintainer repins. Kill condition registered before computing: a leading term changes
      on the split (did not fire).
""")
old_iii = s[s.index("\\item[(iii)] (Haar)"):s.index("\\item[(iv)] (the gap)")]
new_iii = r"""\item[(iii)] (random states) for a pure even state of $2c'$ modes, $d = 2^{c'}$, $c' \ge 1$, drawn from the unitarily invariant measure of its parity sector (numbers read in $\mathrm{span}\{1, I_4\}$, conventions, the unit principle, U1), the reduction $\rho$ to $c'$ of the modes, in the sub-Clifford algebra they generate, has
\[
\langle \operatorname{tr}\rho^{n} \rangle = \frac{2\sum_{\sigma} (d/2)^{\#(\sigma^{-1}\eta) + \#(\sigma)}}{\prod_{l=0}^{n-1}(d^{2}/2 + l)} ,
\qquad
d^{\,n-1}\langle \operatorname{tr}\rho^{n} \rangle = \frac{\sum_{g}N_{n,g}(4/d^{2})^{g}}{\prod_{l<n}(1 + 2l/d^{2})} \;\to\; C_{n} ,
\]
$N_{n,g}$ the number of $\sigma$ with $\#(\sigma) + \#(\sigma^{-1}\eta) = n + 1 - 2g$; at $n = 2$ it is $2d/(d^{2} + 2)$; it exceeds $d^{1-n}$, and is below $C_{n}d^{1-n}$ for $2 \le n \le 6$, $d \le 32$ (verified). Without the parity condition, for a random pure state of an abstract tensor product of two spaces of dimension $d$, $\langle \operatorname{tr}\rho^{n} \rangle = \sum_{\sigma} d^{\#(\sigma^{-1}\eta) + \#(\sigma)} / \prod_{l=0}^{n-1}(d^{2} + l)$, which at $n = 2$ is the value $2d/(d^{2} + 1)$ of \claimref{synthesis.eviction-keeps-one-replica-saddle}(iii), lies strictly between $d^{1-n}$ and $C_{n}d^{1-n}$ ($n = 2, 3, 4$, $d = 2, 4, 8$ verified), and satisfies $d^{n-1}\langle \operatorname{tr}\rho^{n}\rangle \to C_{n}$ as well;
"""
s = s.replace(old_iii, new_iii)
rep("""the eviction Renyi entropy exceeds the planar replica (and Haar) one by""", """the eviction Renyi entropy exceeds the planar replica one, and the random-state one of (iii) on a parity sector or on an abstract tensor product, by""")
open(d + 'entity.md', 'w').write(s)

p = open(d + 'proof-main.tex').read()
def prep(a, b):
    global p
    assert p.count(a) == 1, (p.count(a), a[:80])
    p = p.replace(a, b)
prep(r"""\emph{(iii).} For a pure state""", r"""\emph{(iii).} First the abstract tensor product. For a pure state""")
prep(r"""Lubkin's value (Fact \claimref{synthesis.imported-haar-average-purity}), which the check confirms at five dimension pairs.""", r"""the value of \claimref{synthesis.eviction-keeps-one-replica-saddle}(iii), which the check confirms at five dimension pairs.""")
prep(r"""(for instance $4/5$ at $n = 2$, $d = 2$ and $7/10$ at $n = 3$, $d = 2$).""", r"""(for instance $4/5$ at $n = 2$, $d = 2$ and $7/10$ at $n = 3$, $d = 2$).

Now the even states. Let the modes be null pairs of a Clifford algebra with generators $e_{k}, f_{k}$, $Q(e_{k}) = 1$, $Q(f_{k}) = -1$, mode parity $p_{k} = f_{k}e_{k}$, $A$ and $B$ complementary sets of $c'$ modes with sub-Clifford algebras $\Cl(A)$, $\Cl(B)$, $\Gamma_{A}$, $\Gamma_{B}$ the products of their $p_{k}$ and $\Gamma = \Gamma_{A}\Gamma_{B}$. The generators of $\Cl(B)$ multiplied by $\Gamma_{A}$ keep their squares, anticommute with each other and commute with $\Cl(A)$, and generate an algebra $B'$ with $\Cl(A) \otimes B'$ the whole algebra as an ordinary tensor product (Theorem \claimref{tower.commuting-copies}, ground algebra $\Cl(B)$, the planes of $A$). Blades being orthogonal for $\langle xy\rangle_{0}$, the projection onto the blades of $\Cl(A)$ times $d$ is the partial trace of this tensor product over $B'$; so the reduction of the statement is a partial trace and $\operatorname{tr}\rho^{n} = \operatorname{tr}\bigl(\psi^{\otimes n}\psi^{*\otimes n}(P^{A}_{\eta} \otimes 1)\bigr)$ as before. (The projection onto $\Cl(B)$ agrees with the other partial trace on even elements, the two differing only on odd blades, so for an even pure state the two reductions have the same moments.) A pure even state has its vector in an eigenspace of the involution $\Gamma = \Gamma_{A} \otimes \Gamma_{B}$, a parity sector, of dimension $d^{2}/2$. The Fact applied to the sector gives $\langle \psi^{\otimes n}\psi^{*\otimes n}\rangle = \sum_{\sigma}P_{\sigma}\Pi^{\otimes n}/\prod_{l<n}(d^{2}/2 + l)$ with $\Pi = \tfrac12(1 \pm \Gamma)$, and $\Pi^{\otimes n} = 2^{-n}\sum_{U}(\pm 1)^{|U|}\Gamma_{(U)}$ over the subsets $U$ of the $n$ copies. The trace of $\Gamma_{(U)}P_{\sigma}(P^{A}_{\eta} \otimes 1)$ factorises over the cycles of $\tau = \sigma^{-1}\eta$ on the $A$ side and of $\sigma$ on the $B$ side, a cycle $z$ contributing the trace of $\Gamma_{A}^{|U \cap z|}$ or $\Gamma_{B}^{|U \cap z|}$, which is $d$ if $|U \cap z|$ is even and $0$ otherwise. The $U$ meeting every cycle of $\sigma$ and of $\tau$ evenly are the common zeros in $\mathbb{F}_{2}^{n}$ of the indicators of the cycles; a linear relation among the indicators equates a union of cycles of $\sigma$ with a union of cycles of $\tau$, a set invariant under $\sigma$, $\tau$ and so under $\eta = \sigma\tau$, hence empty or everything, so the indicators span a space of dimension $\#(\sigma) + \#(\tau) - 1$ and there are $2^{n+1-\#(\sigma)-\#(\tau)}$ such $U$, each of even size. The trace on the sector is therefore $2^{-n}2^{n+1-\#(\sigma)-\#(\tau)}d^{\#(\sigma)+\#(\tau)} = 2(d/2)^{\#(\sigma)+\#(\tau)}$, which gives the first formula. With $\#(\sigma) + \#(\tau) = n + 1 - 2g$ ($g$ is an integer since the signs of $\sigma$ and $\tau$ multiply to that of $\eta$, and $g \ge 0$ by (ii)) a term is $2(d/2)^{n+1-2g}/(d^{2}/2)^{n} = 4^{g}d^{1-n-2g}$ before the factor $\prod_{l}(1 + 2l/d^{2})^{-1}$, which gives the second formula and, with $N_{n,0} = C_{n}$ from (ii), the limit. At $n = 2$: $N_{2,0} = 2$, so the value is $2d^{-1}/(1 + 2d^{-2}) = 2d/(d^{2} + 2)$. The lower bound holds because $\rho$ is a state on $d$ dimensions, with equality only for a flat spectrum; the upper bound is verified in the stated range and not proved in general. The check counts the sector traces by enumeration at small sizes and evaluates both forms for $n \le 6$, $d \le 32$.""")
open(d + 'proof-main.tex', 'w').write(p)

c = open(d + 'check.py').read()
a = '    premise("synthesis.imported-haar-average-purity")\n'
assert c.count(a) == 1
c = c.replace(a, '')
c = c.replace("assert haar_moment(2, m, nn) == F(m + nn, m * nn + 1)           # the stored Haar purity", "assert haar_moment(2, m, nn) == F(m + nn, m * nn + 1)           # the index-two value")
add = '''

# ---------------------------------------------------------------- version 4: a parity sector
def sector_trace(d, s, tau):
    """Number of n-tuples of sector basis states (a_i, b_i), parity(a_i) = parity(b_i), fixed when the a are
    permuted by tau and the b by s: the trace of P_sigma (P_eta on A) on the n-th power of the sector."""
    from itertools import product
    n = len(s)
    par = lambda x: bin(x).count("1") % 2
    count = 0
    for a in product(range(d), repeat=n):
        if any(a[tau[i]] != a[i] for i in range(n)):
            continue
        for b in product(range(d), repeat=n):
            if all(b[s[i]] == b[i] for i in range(n)) and all(par(a[i]) == par(b[i]) for i in range(n)):
                count += 1
    return count


def sector_moment(n, d, perms):
    den = F(1)
    for l in range(n):
        den *= F(d * d, 2) + l
    return 2 * sum(F(d, 2) ** (cs + ct) for cs, ct in perms) / den


def check_parity_sector_moments_keep_the_catalan_limit():
    premise("synthesis.imported-haar-moments-of-random-pure-state")
    premise("tower.commuting-copies")
    premise("synthesis.eviction-keeps-one-replica-saddle")
    # the twist behind the reduction: two modes, generators e (square +1), f (square -1); A = the first mode
    sq = (1, -1, 1, -1)
    p_a = mul(gen(1), gen(0), sq)                                    # the parity f e of the first mode
    assert GA.eq(mul(p_a, p_a, sq), sc(F(1)))
    for y in (gen(2), gen(3)):
        t = mul(y, p_a, sq)
        assert GA.eq(mul(t, t, sq), mul(y, y, sq))
        assert all(GA.commutes(t, x, sq) and GA.anticommutes(y, x, sq) for x in (gen(0), gen(1)))
    cyc = {}
    for n in (2, 3, 4, 5, 6):
        eta = tuple((i + 1) % n for i in range(n))
        cyc[n] = []
        for s in permutations(range(n)):
            tau = compose(inverse(s), eta)
            cyc[n].append((cycles(s), cycles(tau)))
            if (n, len(set(s))) in ((2, 2), (3, 3)):
                for d in (2, 4) if n == 2 else (2,):
                    assert sector_trace(d, s, tau) == 2 * F(d, 2) ** (cycles(s) + cycles(tau))
    genus_one = {2: 0, 3: 1, 4: 10, 5: 70, 6: 420}
    for n in (2, 3, 4, 5, 6):
        ng = {}
        for cs, ct in cyc[n]:
            assert (n + 1 - cs - ct) % 2 == 0
            g = (n + 1 - cs - ct) // 2
            ng[g] = ng.get(g, 0) + 1
        assert ng[0] == catalan(n) and ng.get(1, 0) == genus_one[n]
        for d in (2, 4, 8, 16, 32):
            u = F(1, d * d)
            v = sector_moment(n, d, cyc[n])
            den = F(1)
            for l in range(n):
                den *= 1 + 2 * l * u
            assert v * d ** (n - 1) == sum(c * (4 * u) ** g for g, c in ng.items()) / den
            assert F(1, d ** (n - 1)) < v < catalan(n) * F(1, d ** (n - 1))
            if n <= 4 and d <= 8:
                assert v < haar_moment(n, d, d)
            if n == 2:
                assert v == F(2 * d, d * d + 2)
    assert sector_moment(3, 2, cyc[3]) == F(1, 2) and sector_moment(2, 4, cyc[2]) == F(4, 9)
    return True
'''
i = c.index('\n\nif __name__ == "__main__":')
c = c[:i] + add.rstrip("\n") + "\n" + c[i:]
c = c.replace("check_eviction_keeps_one_saddle_every_index, check_gap_family_interpolates_half_nat_to_ln4]:", "check_eviction_keeps_one_saddle_every_index, check_gap_family_interpolates_half_nat_to_ln4,\n               check_parity_sector_moments_keep_the_catalan_limit]:")
open(d + 'check.py', 'w').write(c)
