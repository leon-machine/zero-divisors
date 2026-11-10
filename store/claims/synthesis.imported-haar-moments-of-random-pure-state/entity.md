---
id: synthesis.imported-haar-moments-of-random-pure-state
kind: claim
version: 3
title: 'Imported: Haar moments of a random pure state (Schur-Weyl duality)'
status: imported
region: synthesis
subject: entropy
tags: [entanglement, representation-theory, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-31
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'GA rewrite (the complex field named by its unit)'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Fable 5.2
  role: 'the n = 2 value (mean purity) stated in the Fact itself, with Lubkin 1978 as its source, on retirement of the separate mean-purity Fact'
  version: 3
  source: maintainer pass of 2026-11-10
review: draft
imported_from:
- citation: 'R. Goodman and N. R. Wallach, Symmetry, Representations, and Invariants, Graduate Texts in Mathematics 255, Springer (2009), Chapter 9 (Schur-Weyl duality).'
  key: GoodmanWallach2009
- citation: 'A. W. Harrow, The church of the symmetric subspace, arXiv:1308.6595 (2013).'
  key: Harrow2013
- citation: 'E. Lubkin, Entropy of an n-system from its correlation with a k-reservoir, J. Math. Phys. 19 (1978), 1028.'
  key: Lubkin1978
  doi: 10.1063/1.523763
  locator: 'the n = 2 case (the mean purity); prior art for general dimensions'
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 2 -> 3, by decision 2 of 9 November 2026: the separate imported mean-purity Fact (id synthesis.imported-haar-average-purity) is retired in favour of the derived result synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three, which gives the value at dimensions that are powers of two only; the formal text therefore carries the n = 2 value itself for general dimensions, with Lubkin 1978 named as prior art, in place of the reference to the retired Fact.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. The complex-field stand-in \C is tied to its unit, span{1, I_4} (U1), by one parenthetical at its first use (readers R02 and R08: the language check does not flag the macro). Notation only; the mathematics is unchanged. Imported (status kept): the source''s formula is unchanged, so no source_formal is needed.'
  note: >-
    Imported for the replica-saddle count of eviction, whose proof (iii) derives the moment formula
    from Schur's lemma and the irreducibility of the symmetric power, cited from memory. Generalises
    Lubkin's n = 2 average. Cited from memory, not checked
    against the sources (chapter numbers included); the n = 2 case agrees with Lubkin's value
    (m + n)/(mn + 1), and the stated value at n = 3, d_A = d_B = 2 is 7/10, both of which the
    eviction result's check confirms in exact arithmetic.
    The n = 2 value (10 November 2026). Until version 2 the formal text referred to a separate imported Fact for
    the mean purity (id synthesis.imported-haar-average-purity, retired on 10 November 2026). The store now
    derives the second moment, and with it the mean purity (m + n)/(mn + 1), as a finite average for dimensions
    m, n that are powers of two (synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three);
    for general m, n the value is the classical one (Lubkin 1978), prior art named here and imported as the
    n = 2 case of this Fact. Carried over from the retired Fact's record: Lubkin's journal, volume, page and DOI
    were checked on 2026-10-26 against the reference list of arXiv:1406.5776; the article title and the exact form
    of Lubkin's equation are cited from memory. That secondary source displays the mean of Tr(rho - 1/m)^2 as
    (m^2 - 1)/(mn + 1); the value implied by the purity is (m^2 - 1)/(m(mn + 1)), and at m = n = 2 the displayed
    form gives 3/5, above the largest possible value 1/2, so the display appears to drop a factor 1/m.
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Created by the maintainer pass of 2026-10-31 (literature cited from memory by an accepted result; Leon''s list of imports).'
---

## formal
Let $\ket{\psi}$ be a unit vector of $\C^{D}$ (an abstract Hilbert space, its numbers read in $\mathrm{span}\{1, I_4\}$, conventions U1; the source writes the complex numbers for that field) drawn from the unitarily invariant probability measure. For every $n \ge 1$,
\[
\bigl\langle (\ket{\psi}\bra{\psi})^{\otimes n} \bigr\rangle \;=\; \frac{\Pi_{\mathrm{sym}}}{\dim \mathrm{Sym}^{n}\C^{D}} \;=\; \frac{\sum_{\sigma \in S_{n}} P_{\sigma}}{D(D + 1)\cdots(D + n - 1)},
\]
with $P_{\sigma}$ the operator permuting the $n$ tensor factors: the average commutes with $U^{\otimes n}$ for every unitary $U$ and is supported on the symmetric power, which is irreducible under $U(D)$ (Schur-Weyl duality), so by Schur's lemma it is the normalised projection onto it. Consequently, for $D = d_{A}d_{B}$ and $\rho_{A} = \operatorname{Tr}_{B}\ket{\psi}\bra{\psi}$,
\[
\bigl\langle \operatorname{tr}\rho_{A}^{n} \bigr\rangle \;=\; \frac{\sum_{\sigma \in S_{n}} d_{A}^{\#(\sigma^{-1}\eta)}\, d_{B}^{\#(\sigma)}}{D(D + 1)\cdots(D + n - 1)},
\]
with $\eta$ the cyclic permutation $(1\,2\,\cdots\,n)$ and $\#(\cdot)$ the number of cycles. At $n = 2$ the average is $(\mathbb{1} + F)/(D(D + 1))$, $F$ the swap of the two copies, and the mean purity is
\[
\bigl\langle \operatorname{tr}\rho_{A}^{2} \bigr\rangle \;=\; \frac{d_{A} + d_{B}}{d_{A}d_{B} + 1}, \qquad\text{equivalently}\qquad \bigl\langle \operatorname{tr}(\rho_{A} - \mathbb{1}/d_{A})^{2} \bigr\rangle \;=\; \frac{d_{A}^{2} - 1}{d_{A}(d_{A}d_{B} + 1)},
\]
symmetric in $d_{A}$ and $d_{B}$, for all dimensions $d_{A}, d_{B} \geq 1$: the classical value of Lubkin \cite{Lubkin1978}, prior art, imported here as the case $n = 2$. For $d_{A}$, $d_{B}$ powers of two the same value is derived in the store as a finite average (Theorem \claimref{synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three}); for other dimensions it rests on this Fact. \emph{Provenance:} \cite[Chapter 9]{GoodmanWallach2009}; \cite{Harrow2013}; \cite{Lubkin1978} for $n = 2$.

## technical
For a random pure state of a large system, the average of $n$ copies of its projector is fixed by symmetry: it commutes with every unitary acting the same way on each copy and lives on the symmetric part of the $n$-fold product, which is irreducible, so it is the projector onto that part divided by its dimension, a sum over all permutations of the copies. Splitting the system in two and taking the partial trace turns each permutation into a power of the two dimensions, counted by cycles, which gives every Renyi moment of a random subsystem. The first case, two copies, is the mean purity $(d_{A} + d_{B})/(d_{A}d_{B} + 1)$ of a part, computed by Lubkin in 1978: it lies between $1/\min(d_{A}, d_{B})$, the value for a maximally mixed smaller part, and $1/d_{A} + 1/d_{B}$, and is the second-moment counterpart of Page's average entropy. The store derives that value by a finite average when both dimensions are powers of two and takes it from this Fact otherwise; it is the random-state reference of the abstract tensor-product column in the comparison of the eviction mechanism with the replica-wormhole computation.

## lay
If you pick a quantum state of a large system completely at random, the average amount of entanglement between two of its parts can be computed exactly. Symmetry does all the work: the answer is a sum over the ways of reshuffling copies of the state, each weighted by the sizes of the two parts. This is the standard formula behind Page's result on the entropy of a random subsystem.

## one-liner
For a Haar-random pure state on $\C^{D}$, $\langle(\ket{\psi}\bra{\psi})^{\otimes n}\rangle = \sum_{\sigma}P_{\sigma}/(D(D + 1)\cdots(D + n - 1))$, so $\langle\operatorname{tr}\rho_{A}^{n}\rangle = \sum_{\sigma}d_{A}^{\#(\sigma^{-1}\eta)}d_{B}^{\#(\sigma)}/(D)_{n}$ (Schur-Weyl duality); at $n = 2$ the mean purity is $(d_{A} + d_{B})/(d_{A}d_{B} + 1)$ (Lubkin 1978).
