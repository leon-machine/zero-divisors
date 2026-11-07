---
id: synthesis.imported-haar-moments-of-random-pure-state
kind: claim
version: 2
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
review: draft
imported_from:
- citation: 'R. Goodman and N. R. Wallach, Symmetry, Representations, and Invariants, Graduate Texts in Mathematics 255, Springer (2009), Chapter 9 (Schur-Weyl duality).'
  key: GoodmanWallach2009
- citation: 'A. W. Harrow, The church of the symmetric subspace, arXiv:1308.6595 (2013).'
  key: Harrow2013
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. The complex-field stand-in \C is tied to its unit, span{1, I_4} (U1), by one parenthetical at its first use (readers R02 and R08: the language check does not flag the macro). Notation only; the mathematics is unchanged. Imported (status kept): the source''s formula is unchanged, so no source_formal is needed.'
  note: >-
    Imported for the replica-saddle count of eviction, whose proof (iii) derives the moment formula
    from Schur's lemma and the irreducibility of the symmetric power, cited from memory. Generalises
    Lubkin's n = 2 average (synthesis.imported-haar-average-purity). Cited from memory, not checked
    against the sources (chapter numbers included); the n = 2 case agrees with Lubkin's value
    (m + n)/(mn + 1), and the stated value at n = 3, d_A = d_B = 2 is 7/10, both of which the
    eviction result's check confirms in exact arithmetic.
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
with $\eta$ the cyclic permutation $(1\,2\,\cdots\,n)$ and $\#(\cdot)$ the number of cycles. At $n = 2$ this is Lubkin's $(d_{A} + d_{B})/(d_{A}d_{B} + 1)$ (Fact \claimref{synthesis.imported-haar-average-purity}). \emph{Provenance:} \cite[Chapter 9]{GoodmanWallach2009}; \cite{Harrow2013}.

## technical
For a random pure state of a large system, the average of $n$ copies of its projector is fixed by symmetry: it commutes with every unitary acting the same way on each copy and lives on the symmetric part of the $n$-fold product, which is irreducible, so it is the projector onto that part divided by its dimension, a sum over all permutations of the copies. Splitting the system in two and taking the partial trace turns each permutation into a power of the two dimensions, counted by cycles, which gives every Renyi moment of a random subsystem.

## lay
If you pick a quantum state of a large system completely at random, the average amount of entanglement between two of its parts can be computed exactly. Symmetry does all the work: the answer is a sum over the ways of reshuffling copies of the state, each weighted by the sizes of the two parts. This is the standard formula behind Page's result on the entropy of a random subsystem.

## one-liner
For a Haar-random pure state on $\C^{D}$, $\langle(\ket{\psi}\bra{\psi})^{\otimes n}\rangle = \sum_{\sigma}P_{\sigma}/(D(D + 1)\cdots(D + n - 1))$, so $\langle\operatorname{tr}\rho_{A}^{n}\rangle = \sum_{\sigma}d_{A}^{\#(\sigma^{-1}\eta)}d_{B}^{\#(\sigma)}/(D)_{n}$ (Schur-Weyl duality).
