---
id: singularity.p-reduced-metric-level-reading-many
kind: claim
version: 6
title: '(P$_{\mathrm{loc}}$), reduced: the metric-level reading on many modes'
status: proved
region: singularity
subject: descent
tags: [univalence, descent-map]
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
- obj.singularity.grading-parity-automorphism
- obj.singularity.two-fibres-two-assemblies
derivations:
- name: main
  uses:
  - singularity.descent-parity-average@4
  - singularity.imported-one-sided-completion-singularity@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:9.6
- kind: check
  ref: check.py::check_modewise_descents_commute_and_compose_to_joint_pinching
- kind: check
  ref: check.py::check_fixed_subalgebra_dimension_and_uniqueness_step
- kind: check
  ref: check.py::check_meet_is_joint_diagonal_smaller_than_parity_even
locators:
  paper: T05
  number: Prop 9.6
  label: prem:localuniv
  line: 2117
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the mode-wise descents commute and compose in every order to E_N, each fixed subalgebra has dimension 4^N/2, and the meet is the joint-diagonal algebra smaller than the parity-even one. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6.'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    added:
    - singularity.imported-one-sided-completion-singularity
    note: 'Added the one-sided completion fact because the conditional clause reads the metric level through
      the pointwise descents that this localisation attaches to each point of E; removed the mechanical
      transport-algorithm edge since the proof uses only the parity-average uniqueness argument and the
      multi-mode definition. Levels pass: conditions already kept; lay now adds the two-or-more-modes
      scope of the strictness clause.'
  env: proposition
  context_refs:
  - singularity.imported-one-sided-completion-singularity
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    stated_role:
    - singularity.imported-one-sided-completion-singularity
---

## formal
The mode-wise descents commute, each is the unique conditional expectation of the boundary mode space onto the $\operatorname{Ad}(\sigma_k)$-fixed subalgebra (the elements even in mode $k$, of dimension $4^{N}/2$ on $N$ modes, not the two-dimensional even part of the mode factor alone), and their composite, in any order, is $\EN$: a conditional expectation onto the intersection of the mode-wise ranges, the joint-number-diagonal algebra. Consequently, if the metric-level reading of the full boundary mode space is taken to be the simultaneous performance of the pointwise descents that the localisation attaches, one per point of $E$ (Fact \claimref{singularity.imported-one-sided-completion-singularity}), then that reading is $\EN$ and the metric level is the joint-diagonal algebra, strictly smaller than the total-parity-even algebra on two or more modes. The antecedent is a \emph{choice}, not a consequence: it adopts the sheaf assembly of the pointwise levels over the net assembly, the two quantified, and not decided between, in Appendix \ref{app:threeroutes}.

## technical
On $N$ completed modes each mode-wise descent $E_k(x) = \tfrac12(x + \sigma_k x \sigma_k)$ is the unique conditional expectation of the whole boundary mode space onto the elements even in mode $k$, a subalgebra of dimension $4^{N}/2$. The $\sigma_k$ are single-site in a Jordan-Wigner representation and commute, so the $E_k$ commute, and their composite in any order is the pinching $\EN$, a conditional expectation onto the intersection of their ranges, the joint-number-diagonal algebra.

Consequently, if the metric-level reading of the boundary mode space is taken to be the simultaneous performance of the pointwise descents that the localisation attaches to the points of $E$, that reading is $\EN$ and the metric level is the joint-diagonal algebra, strictly smaller than the total-parity-even algebra when $N \geq 2$. The antecedent is a choice, the sheaf assembly of the pointwise levels over the net assembly, and is not derived.

## lay
When many boundary modes are read at the classical level, the separate one-mode readings can be done in any order and together amount to keeping only the joint occupation records. If one adopts the reading in which every point's own descent is applied, the classical level is exactly that record algebra, which, on two or more modes, is smaller than what fermion parity alone would allow. Adopting that reading is a choice the paper names, not something it proves.

## one-liner
The mode-wise descents commute and compose to the pinching $\EN$, so if the metric level is read as all pointwise descents at once, it is the joint-number-diagonal algebra.
