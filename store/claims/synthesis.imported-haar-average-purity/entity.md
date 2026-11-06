---
id: synthesis.imported-haar-average-purity
kind: claim
version: 1
title: 'Imported: average purity of a random pure state (Lubkin 1978)'
status: imported
region: synthesis
subject: entropy
tags: [entanglement, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'E. Lubkin, Entropy of an n-system from its correlation with a k-reservoir, J. Math. Phys. 19 (1978), 1028.'
  key: Lubkin1978
  doi: 10.1063/1.523763
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: >-
      New imported Fact, created at Leon's decision of 2026-10-26 so that clause (iii) of
      synthesis.eviction-keeps-one-replica-saddle can cite its source. Journal, volume, page and DOI checked on
      2026-10-26 against the reference list of arXiv:1406.5776 (which cites Lubkin for the mean of
      $\operatorname{Tr}(\rho - \mathbb{1}/m)^{2}$ over the invariant measure); the article title and the exact
      form of Lubkin's equation are cited from memory, not checked against the source. The secondary source
      displays that mean as $(m^{2} - 1)/(mn + 1)$; the value implied by the purity stated here is
      $(m^{2} - 1)/(m(mn + 1))$, and at $m = n = 2$ the displayed form gives $3/5$, above the largest possible
      value $\tfrac12$, so the display appears to drop a factor $1/m$. The statement here is the purity form,
      which follows from the second moment of the invariant measure and is recomputed exactly (by counting the
      traces of the two swap operators) in the check of synthesis.eviction-keeps-one-replica-saddle. Matrix
      and Hilbert-space language is kept: the statement is about an imported Hilbert space, with no
      geometric-algebra unit involved.
---

## formal
Let $\mathcal{H} = \C^{m}\otimes\C^{n}$ and let $\ket{\psi}$ be a unit vector drawn from the unitarily invariant probability measure on the unit sphere of $\mathcal{H}$, with $\rho_{A} = \operatorname{Tr}_{B}\ket{\psi}\bra{\psi}$ its marginal on $\C^{m}$. Then
\[
\bigl\langle \operatorname{Tr}\rho_{A}^{2} \bigr\rangle = \frac{m + n}{mn + 1},
\qquad\text{equivalently}\qquad
\bigl\langle \operatorname{Tr}(\rho_{A} - \mathbb{1}/m)^{2} \bigr\rangle = \frac{m^{2} - 1}{m(mn + 1)},
\]
symmetric in $m$ and $n$. It follows from the second moment $\langle \ket{\psi}\bra{\psi}^{\otimes 2}\rangle = (\mathbb{1} + F)/(mn(mn + 1))$, $F$ the swap of the two copies, since $\operatorname{Tr}\rho_{A}^{2}$ is the expectation of the swap of the two $\C^{m}$ factors. \emph{Provenance:} \cite{Lubkin1978}.

## technical
For a pure state of a system of dimension $mn$ chosen at random with the unitarily invariant measure, the purity of the $m$-dimensional part averages to $(m + n)/(mn + 1)$. This lies between $1/\min(m, n)$, the value for a maximally mixed smaller part, and $1/m + 1/n$, and is the second-moment counterpart of Page's average entropy. The series uses it as the random-state reference for the Renyi-2 comparison of the eviction mechanism with the replica-wormhole computation.

## lay
If a quantum system in a pure state is split in two and the state is chosen at random, each part is typically close to maximally mixed. Lubkin computed in 1978 the average of the simplest measure of how mixed a part is, its purity, which comes out as a simple ratio of the two dimensions. The series compares this random-state value with its own radiation and with the wormhole calculation of black hole radiation.

## one-liner
For a random pure state on $\C^{m}\otimes\C^{n}$ the mean purity of either part is $(m + n)/(mn + 1)$ (Lubkin 1978).
