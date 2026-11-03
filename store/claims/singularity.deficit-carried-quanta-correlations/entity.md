---
id: singularity.deficit-carried-quanta-correlations
kind: claim
version: 5
title: The deficit is carried by the quanta correlations
status: proved
region: singularity
subject: entropy
tags: [descent-map, entanglement]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
about:
- obj.singularity.multi-mode-descent
derivations:
- name: main
  uses:
  - singularity.deficit-theorem-cost-descent-exactly@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:9.4
- kind: check
  ref: check.py::check_diagonal_marginals_pass_through_descent
- kind: check
  ref: check.py::check_deficit_is_total_correlation_drop_mixed
- kind: check
  ref: check.py::check_pure_state_deficit_is_whole_descended_entropy
locators:
  paper: T05
  number: Cor 9.4
  label: cor:correlations
  line: 2101
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: diagonal marginals pass through E_N unchanged, D = C(rho) - C(E_N rho) on mixed states as formal logarithms, and D = S(E_N rho) for pure model states. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  env: corollary
  context_refs:
  - singularity.modular-descent
  - singularity.parity-protection
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    note: Removed the mechanically added transport-algorithm edge (framing only); modular descent and
      parity protection are cited as cases where the diagonal-marginal hypothesis holds, not as premises,
      so they were not added.
---

## formal
Write $\rho_k$ for the single-mode marginals of $\rho$ and $C(\rho) := \sum_k S(\rho_k) - S(\rho)$ for the total correlation. If every $\rho_k$ is diagonal in its number basis (as Theorem \claimref{singularity.modular-descent} guarantees for thermofield injections and Lemma \claimref{singularity.parity-protection} for the model), then the single-mode marginals of $\EN(\rho)$ equal those of $\rho$, and
\[
\rel{\rho}{\EN\rho} \;=\; C(\rho) - C(\EN\rho) :
\]
the deficit is the total correlation of the ascended state minus the classical, number-basis correlation that survives descent. No single-quantum quantity contributes anything: the cost of the descent consists entirely of inter-quanta correlations. In particular, for a globally pure $\rho$, $S(\rho) = 0$ and the deficit is the whole descended entropy, $\rel{\rho}{\EN\rho} = S(\EN\rho)$.

## technical
Let $\rho_k$ be the single-mode marginals of $\rho$ and $C(\rho) = \sum_k S(\rho_k) - S(\rho)$ its total correlation. If every $\rho_k$ is diagonal in its number basis, then $\EN$ leaves each single-mode marginal unchanged and the deficit of descent is $\rel{\rho}{\EN\rho} = C(\rho) - C(\EN\rho)$.

So the cost of descent consists entirely of correlations between quanta. For globally pure $\rho$ it is the whole descended entropy, $\rel{\rho}{\EN\rho} = S(\EN\rho)$.

## lay
Descent replaces a quantum state by a version that keeps only its classical occupation records. When each individual mode already looks classical on its own, this result shows that everything lost in descent lies in the correlations between modes. No single mode on its own carries any of the loss.

## one-liner
When every single-mode marginal is number-diagonal, the descent deficit $\rel{\rho}{\EN\rho}$ equals the drop in total correlation $C(\rho) - C(\EN\rho)$.
