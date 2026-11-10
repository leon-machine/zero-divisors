---
id: synthesis.eviction-keeps-one-of-catalan-many-replica-saddles
kind: claim
version: 4
title: 'Eviction keeps one of Catalan-many replica saddles'
status: proved
region: synthesis
subject: entropy
tags: [boundary-modes, entanglement, dictionaries]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle (U1 to U6)
  version: 3
  source: maintainer pass 2026-11-07 (resolve units)
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
derivations:
- name: main
  uses:
  - synthesis.eviction-keeps-one-replica-saddle@3
  - singularity.eviction-window-thermal-product-radiation-entropy@7
  - synthesis.eviction-deficit-against-page-deficit@4
  - singularity.imported-page-average-entropy-subsystem@1
  - synthesis.imported-replica-wormhole-two-saddle-purity@1
  - synthesis.imported-haar-moments-of-random-pure-state@2
  - synthesis.imported-non-crossing-permutations-are-geodesic@1
  - tower.commuting-copies@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_planar_replica_saddles_are_catalan
- kind: check
  ref: check.py::check_haar_moments_tend_to_catalan
- kind: check
  ref: check.py::check_eviction_keeps_one_saddle_every_index
- kind: check
  ref: check.py::check_gap_family_interpolates_half_nat_to_ln4
- kind: check
  ref: check.py::check_parity_sector_moments_keep_the_catalan_limit
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - note.singularity.island-dictionary-one-dissonance
  - synthesis.eviction-keeps-one-replica-saddle
extraction:
  restatement_mode_split:
    by: ai-2026-11-09-bridges
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
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By the unit principle (U1) the abstract Hilbert spaces C^d (x) C^d and C^D of the Haar computation have their numbers read in span{1, I_4}, stated once in clause (iii); the entity wrote no bare i (the detector''s hits were the product index of the Haar denominator, renamed l); the outside_ga declaration, whose reason was that Hilbert-space structure, is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the C^d of the Haar-random states is an abstract Hilbert space, not built from GA modes; the i in prod_{i<n}(d^2 + i) is an index; declared (version and levels unchanged).'
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'uses edges added to the new Facts synthesis.imported-non-crossing-permutations-are-geodesic@1 (the geodesic characterisation and Catalan count of proof (ii)) and synthesis.imported-haar-moments-of-random-pure-state@1 (the symmetric-power moment of proof (iii)), both previously cited from memory; the proof now cites them. Version 1 -> 2.'
  open_problem: op.island-dictionary
  note: >-
    Extends the stored Renyi-2 comparison to every integer Renyi index and ties it to the stored von Neumann
    comparison. Cross-subject input: the combinatorics of non-crossing permutations (the planar sum behind
    the replica computation, and the moments of the Page spectrum at equal dimensions), and Schur-Weyl
    duality for the Haar average of the n-th tensor power of a random pure state (cited from memory; the
    n = 2 case is the stored Lubkin Fact and is recomputed). The n -> 1 statement is a consistency check
    of the analytic continuation of ln C_n/(n-1) against the stored half nat, not a derivation of the
    von Neumann gap. Transport-absent: quantum-information combinatorics on the stored eviction theorem.
---

## formal
Work at zero weight under the hypotheses of \claimref{singularity.eviction-window-thermal-product-radiation-entropy}, after $j$ radiated quanta with capacity bound $c\ln 2$, and write $\eta = (1\,2\,\cdots\,n)$ and $\#(\sigma)$ for the number of cycles of $\sigma \in S_{n}$. Then for every integer $n \geq 2$:
\begin{enumerate}
\item[(i)] (eviction) the radiation spectrum is flat of rank $2^{\min(j,c)}$, so $\operatorname{tr}\rho_{R}^{n} = 2^{-(n-1)\min(j,c)} = \max\bigl(2^{-(n-1)j},\, 2^{-(n-1)c}\bigr)$: the larger of the two extremal replica terms (identity and cyclic), as in clause (ii) of \claimref{synthesis.eviction-keeps-one-replica-saddle} at $n = 2$;
\item[(ii)] (planar saddles) $\#(\sigma) + \#(\sigma^{-1}\eta) \leq n + 1$ for every $\sigma \in S_{n}$, with equality for exactly $C_{n} = \binom{2n}{n}/(n+1)$ permutations (the non-crossing ones); at the crossing $j = c = m$, $d = 2^{m}$, each contributes $d^{1-n}$ to the replica sum $\sum_{\sigma} k^{\#(\sigma) - n} d^{\#(\sigma^{-1}\eta) - n}$ at $k = d$, the others are suppressed by powers of $d^{-2}$;
\item[(iii)] (random states) for a pure even state of $2c'$ modes, $d = 2^{c'}$, $c' \ge 1$, drawn from the unitarily invariant measure of its parity sector (numbers read in $\mathrm{span}\{1, I_4\}$, conventions, the unit principle, U1), the reduction $\rho$ to $c'$ of the modes, in the sub-Clifford algebra they generate, has
\[
\langle \operatorname{tr}\rho^{n} \rangle = \frac{2\sum_{\sigma} (d/2)^{\#(\sigma^{-1}\eta) + \#(\sigma)}}{\prod_{l=0}^{n-1}(d^{2}/2 + l)} ,
\qquad
d^{\,n-1}\langle \operatorname{tr}\rho^{n} \rangle = \frac{\sum_{g}N_{n,g}(4/d^{2})^{g}}{\prod_{l<n}(1 + 2l/d^{2})} \;\to\; C_{n} ,
\]
$N_{n,g}$ the number of $\sigma$ with $\#(\sigma) + \#(\sigma^{-1}\eta) = n + 1 - 2g$; at $n = 2$ it is $2d/(d^{2} + 2)$; it exceeds $d^{1-n}$, and is below $C_{n}d^{1-n}$ for $2 \le n \le 6$, $d \le 32$ (verified). Without the parity condition, for a random pure state of an abstract tensor product of two spaces of dimension $d$, $\langle \operatorname{tr}\rho^{n} \rangle = \sum_{\sigma} d^{\#(\sigma^{-1}\eta) + \#(\sigma)} / \prod_{l=0}^{n-1}(d^{2} + l)$, which at $n = 2$ is the value $2d/(d^{2} + 1)$ of \claimref{synthesis.eviction-keeps-one-replica-saddle}(iii), lies strictly between $d^{1-n}$ and $C_{n}d^{1-n}$ ($n = 2, 3, 4$, $d = 2, 4, 8$ verified), and satisfies $d^{n-1}\langle \operatorname{tr}\rho^{n}\rangle \to C_{n}$ as well;
\item[(iv)] (the gap) hence at the crossing, to leading order in $d$, the eviction Renyi entropy exceeds the planar replica one, and the random-state one of (iii) on a parity sector or on an abstract tensor product, by
\[
\Delta S_{n} = \frac{\ln C_{n}}{n - 1}, \qquad \Delta S_{2} = \ln 2,\quad \Delta S_{3} = \tfrac12 \ln 5,\quad \Delta S_{n} \uparrow \ln 4,
\]
strictly increasing in $n$; and the continuation $\ln C_{n}$, $C_{n} = \Gamma(2n+1)/(\Gamma(n+1)\Gamma(n+2))$, has $\frac{d}{dn}\ln C_{n}\big|_{n=1} = \tfrac12$, which is the von Neumann gap $\tfrac12$ between eviction and Page's average at the crossing stored in \claimref{synthesis.eviction-deficit-against-page-deficit}.
\end{enumerate}
So the term-by-term dictionary of the Renyi-2 comparison holds at every index: eviction keeps one of the $C_{n}$ planar saddles of the $n$-replica computation (the dominant extremal one away from the crossing), and the quantity on which the two accounts differ is the count of the others, one family of numbers from $\tfrac12$ at $n \to 1$ through $\ln 2$ to $\ln 4$.

## technical
The stored comparison found that, at Renyi index two and zero weight, eviction keeps the dominant of the two replica saddles where the island computation adds both, a difference of $\ln 2$ in Renyi-2 entropy at the crossing, and separately that in von Neumann entropy eviction sits half a nat above Page's average there. This result places both numbers in one family. The split of window from radiation is the one in the Clifford algebra of the modes (sub-Clifford algebras, reduction by projection onto blades); for the even states concerned it gives the same reduced states as a tensor product, and the random-state moments are stated on a parity sector, where a permutation of genus $g$ is weighted by $4^{g}$ and the planar limit is unchanged. In the $n$-replica computation the radiation's $n$-th moment is a sum over permutations of the replicas; the leading ones are the non-crossing permutations, which saturate a genus bound and number $C_{n}$, the Catalan number, and at the crossing each contributes the same amount. Eviction's radiation spectrum at zero weight is flat, so its moment is exactly one such term. The gap in Renyi-$n$ entropy is therefore $\ln C_{n}/(n-1)$, and the Haar average reproduces the planar value at large dimension. Continuing the Catalan numbers to $n \to 1$ gives the derivative of $\ln C_n$ at one, which is exactly one half: the stored von Neumann gap. The quantity on which eviction and the island computation differ is the number of subleading planar saddles at each index.

## lay
When a black hole has given away half its information, two accounts of where the information sits disagree slightly. The replica method, which underlies the island computation, adds up several geometric contributions; the series' eviction mechanism keeps only the largest one. Earlier results measured the gap with two different entropy measures and found half a nat and $\ln 2$. Here the gap is computed for the whole family of Renyi entropies: it is the logarithm of a Catalan number, which counts the contributions the replica method keeps, divided by the index minus one. The family starts at half a nat, passes through $\ln 2$, and approaches $\ln 4$, so the two earlier numbers are two members of one sequence.

## one-liner
At zero weight and at the crossing, eviction's radiation Renyi-$n$ entropy exceeds the planar replica value, and the random-state average (on a parity sector of the modes or on an abstract tensor product, to leading order), by $\ln C_{n}/(n-1)$ with $C_{n}$ the Catalan number counting non-crossing replica saddles, of which eviction keeps one; the family is $\ln 2$ at $n = 2$, rises to $\ln 4$, and continues to the stored half nat at $n \to 1$.
