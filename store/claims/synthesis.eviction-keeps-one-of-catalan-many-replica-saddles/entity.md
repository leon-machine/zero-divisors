---
id: synthesis.eviction-keeps-one-of-catalan-many-replica-saddles
kind: claim
version: 2
title: 'At every Renyi index the eviction mechanism keeps one replica saddle where the planar replica sum keeps the Catalan number of them: at the crossing the eviction radiation entropy exceeds the planar (Page) one by $\ln C_{n}/(n-1)$, which is $\ln 2$ at $n = 2$, rises to $\ln 4$, and continues to the stored half nat at $n = 1$'
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
review: draft
derivations:
- name: main
  uses:
  - synthesis.eviction-keeps-one-replica-saddle@2
  - singularity.eviction-window-thermal-product-radiation-entropy@7
  - synthesis.eviction-deficit-against-page-deficit@3
  - singularity.imported-page-average-entropy-subsystem@1
  - synthesis.imported-haar-average-purity@1
  - synthesis.imported-replica-wormhole-two-saddle-purity@1
  - synthesis.imported-haar-moments-of-random-pure-state@1
  - synthesis.imported-non-crossing-permutations-are-geodesic@1
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
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - note.singularity.island-dictionary-one-dissonance
  - synthesis.eviction-keeps-one-replica-saddle
extraction:
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
\item[(iii)] (Haar) for a random pure state on $\C^{d} \otimes \C^{d}$, $\langle \operatorname{tr}\rho^{n} \rangle = \sum_{\sigma} d^{\#(\sigma^{-1}\eta) + \#(\sigma)} / \prod_{i=0}^{n-1}(d^{2} + i)$, which at $n = 2$ is the stored Haar purity, lies strictly between $d^{1-n}$ and $C_{n}d^{1-n}$, and satisfies $d^{n-1}\langle \operatorname{tr}\rho^{n}\rangle \to C_{n}$;
\item[(iv)] (the gap) hence at the crossing, to leading order in $d$, the eviction Renyi entropy exceeds the planar replica (and Haar) one by
\[
\Delta S_{n} = \frac{\ln C_{n}}{n - 1}, \qquad \Delta S_{2} = \ln 2,\quad \Delta S_{3} = \tfrac12 \ln 5,\quad \Delta S_{n} \uparrow \ln 4,
\]
strictly increasing in $n$; and the continuation $\ln C_{n}$, $C_{n} = \Gamma(2n+1)/(\Gamma(n+1)\Gamma(n+2))$, has $\frac{d}{dn}\ln C_{n}\big|_{n=1} = \tfrac12$, which is the von Neumann gap $\tfrac12$ between eviction and Page's average at the crossing stored in \claimref{synthesis.eviction-deficit-against-page-deficit}.
\end{enumerate}
So the term-by-term dictionary of the Renyi-2 comparison holds at every index: eviction keeps one of the $C_{n}$ planar saddles of the $n$-replica computation (the dominant extremal one away from the crossing), and the quantity on which the two accounts differ is the count of the others, one family of numbers from $\tfrac12$ at $n \to 1$ through $\ln 2$ to $\ln 4$.

## technical
The stored comparison found that, at Renyi index two and zero weight, eviction keeps the dominant of the two replica saddles where the island computation adds both, a difference of $\ln 2$ in Renyi-2 entropy at the crossing, and separately that in von Neumann entropy eviction sits half a nat above Page's average there. This result places both numbers in one family. In the $n$-replica computation the radiation's $n$-th moment is a sum over permutations of the replicas; the leading ones are the non-crossing permutations, which saturate a genus bound and number $C_{n}$, the Catalan number, and at the crossing each contributes the same amount. Eviction's radiation spectrum at zero weight is flat, so its moment is exactly one such term. The gap in Renyi-$n$ entropy is therefore $\ln C_{n}/(n-1)$, and the Haar average reproduces the planar value at large dimension. Continuing the Catalan numbers to $n \to 1$ gives the derivative of $\ln C_n$ at one, which is exactly one half: the stored von Neumann gap. The quantity on which eviction and the island computation differ is the number of subleading planar saddles at each index.

## lay
When a black hole has given away half its information, two accounts of where the information sits disagree slightly. The replica method, which underlies the island computation, adds up several geometric contributions; the series' eviction mechanism keeps only the largest one. Earlier results measured the gap with two different entropy measures and found half a nat and $\ln 2$. Here the gap is computed for the whole family of Renyi entropies: it is the logarithm of a Catalan number, which counts the contributions the replica method keeps, divided by the index minus one. The family starts at half a nat, passes through $\ln 2$, and approaches $\ln 4$, so the two earlier numbers are two members of one sequence.

## one-liner
At zero weight and at the crossing, eviction's radiation Renyi-$n$ entropy exceeds the planar replica (and Haar-average) value by $\ln C_{n}/(n-1)$ with $C_{n}$ the Catalan number counting non-crossing replica saddles, of which eviction keeps one; the family is $\ln 2$ at $n = 2$, rises to $\ln 4$, and continues to the stored half nat at $n \to 1$.
