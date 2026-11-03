---
id: singularity.pinching-against-partial-trace-scope-coincidence
kind: claim
version: 3
title: 'Pinching against partial trace: the scope of a coincidence'
status: proved
region: singularity
subject: descent
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
  - singularity.descent-what-it-erases@5
  - singularity.purity-correlation-transfer-recovery@3
  - singularity.two-levels-finite-model@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:9.2
- kind: check
  ref: check.py::check_single_mode_partial_trace_equals_pinching
- kind: check
  ref: check.py::check_many_modes_partial_trace_keeps_coherence_pinching_kills_it
- kind: check
  ref: check.py::check_marginal_of_pinching_is_pinching_of_marginal
locators:
  paper: T05
  number: Prop 9.2
  label: prop:coincidence
  line: 2073
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: single-mode coincidence of partial trace and pinching for number-basis Schmidt states, the two-mode coherence c1 s1 gamma kept by tr_L and killed by E_N, and marginals commuting with the pinching. Version 2 -> 3.'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    note: 'Removed the mechanical transport-algorithm edge as the proof rests only on the single-mode
      descent display and the two exact model computations; the Schmidt-forcing and parity-protection
      lemmas are cited as instances where the clause (i) hypothesis holds, not as premises, so they were
      not added. Levels pass: the lay level now says what the Schmidt-basis condition is instead of referring
      to it as "the stated condition".'
  env: proposition
  context_refs:
  - singularity.parity-protection
  - singularity.schmidt-forcing-proved-outright
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
---

## formal
\leavevmode
\begin{enumerate}
\item[(i)] (One mode: they agree.) For any global state whose Schmidt basis across the pair/partner cut is the number basis (as boost invariance forces in Lemma \claimref{singularity.schmidt-forcing-proved-outright}, and as the support constraint forces in the model, Lemma \claimref{singularity.parity-protection}), the mode marginal $\tr_{\mathrm{partner}}\,\rho$ is diagonal in the number basis and hence a fixed point of $E$: partial trace and pinching coincide, mode by mode.
\item[(ii)] (Many modes: they differ, by exactly the inter-mode coherence.) On $N \geq 2$ modes, $\tr_L$ and $\EN$ are different maps: $\tr_L$ retains the radiation's off-diagonal joint-number matrix elements, $\EN$ annihilates them, and the two agree on every single-mode marginal. The two maps answer different questions: $\tr_L$ asks what the radiation alone contains; $\EN$ asks what the metric level can carry. Conflating them is harmless for single-mode spectra and fatal for the computation of correlations, which is why the conflation is scoped once, in this step: Step 4d's identification uses clause (i), and Step 6b's computation uses clause (ii).
\end{enumerate}

## technical
(i) For one mode, if the global state's Schmidt basis across the pair/partner cut is the number basis, the marginal $\tr_{\mathrm{partner}}\,\rho$ is diagonal in the number basis and hence a fixed point of the pinching $E$: partial trace and pinching coincide, mode by mode.

(ii) On $N \geq 2$ modes, $\tr_L$ and $\EN$ are different maps. They agree on every single-mode marginal, but $\tr_L$ keeps the radiation's off-diagonal joint-number matrix elements while $\EN$ annihilates them, so they differ by exactly the inter-mode coherence. Conflating them is harmless for single-mode spectra and fatal for the computation of correlations.

## lay
There are two ways of looking at one side of an entangled system: forget the partner, or read the system at the classical level. For a single mode, provided the state's entanglement with its partner is lined up with the occupation numbers (its Schmidt basis is the number basis), the two give the same answer. For several modes they differ: forgetting the partner keeps the coherences between modes, while the classical reading erases them. Agreement seen one mode at a time therefore says nothing about correlations.

## one-liner
Partial trace and pinching agree on a single mode whose Schmidt basis is the number basis, and on two or more modes they differ by exactly the inter-mode coherence.
