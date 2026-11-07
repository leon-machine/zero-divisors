---
id: singularity.exact-equilibrium-over-determines-boundary-modes
kind: claim
version: 5
title: Exact equilibrium over-determines the boundary modes
status: proved
region: singularity
subject: thermality
tags: [thermal-premises, entanglement]
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
- obj.singularity.geometric-modular-condition-g
- obj.singularity.multi-mode-descent
derivations:
- name: main
  uses:
  - singularity.deficit-carried-quanta-correlations@5
  - singularity.deficit-theorem-cost-descent-exactly@4
  - singularity.kms-uniqueness-factor@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:7.28
- kind: check
  ref: check.py::check_geometric_state_is_product
- kind: check
  ref: check.py::check_zero_correlation_and_zero_deficit
- kind: check
  ref: check.py::check_correlated_state_carries_the_deficit
locators:
  paper: T05
  number: Thm 7.28
  label: thm:overdet
  line: 1956
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the geometric Gibbs state is the product of single-mode Gibbs states, with total correlation and descent deficit exactly zero (entropies as exact prime-log vectors), and an entangled control carrying deficit S(m) = C(rho) - C(E_N rho). Version 4 -> 5.'
  env: theorem
  context_refs:
  - singularity.deficit-theorem-cost-descent-exactly
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    added:
    - singularity.deficit-theorem-cost-descent-exactly
    - obj.singularity.geometric-modular-condition-g
    note: Removed the mechanical transport-algorithm edge and added the deficit theorem, which the statement
      and proof invoke for the vanishing deficit.
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - singularity.deficit-theorem-cost-descent-exactly
  merged_from:
  - id: state-selection.exact-equilibrium-over-determines-ledger
    version: 3
    locators:
      paper: T05-state-selection
      number: Thm 7.1
      label: thm:overdet
      line: 337
    about:
    - obj.singularity.multi-mode-descent
    - obj.state-selection.geometric-modular-condition
    uses:
    - singularity.deficit-carried-quanta-correlations@5
    - singularity.deficit-theorem-cost-descent-exactly@4
    - state-selection.kms-uniqueness-factor@1
    checked_by: verify_state_selection.py num:7.1
    proof_files:
    - orig-proof-main.tex (kept here as merged-state-selection.exact-equilibrium-over-determines-ledger-orig-proof-main.tex)
    - proof-main.tex (kept here as merged-state-selection.exact-equilibrium-over-determines-ledger-proof-main.tex)
    formal: 'Let $\omega$ satisfy the geometric modular condition exactly. Then $\rho \propto e^{-\beta K_{\mathrm{geo}}}
      = \bigotimes_k e^{-\beta\omega_k K_k}$ is a product state across modes. Consequently:

      \begin{enumerate}

      \item every inter-mode correlation vanishes: the total correlation $C(\rho) = \sum_k S(\rho_k) - S(\rho)$ is
      zero;

      \item the deficit of the multi-mode descent vanishes: $\rel{\rho}{\EN\rho} = 0$ by \cite[Thm.~9.3]{ButlerT5},
      since $\rho$ is already a fixed point of $\EN$;

      \item no information whatever is carried by the inter-quanta correlations of \cite[Cor.~9.4]{ButlerT5}, and
      the two ledgers agree exactly.

      \end{enumerate}

      Hence the exact geometric modular condition is available only in the stationary idealisation, and the correlations
      on which Steps 5 and 6b depend are precisely the deviation from it.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Merged the state-selection note''s Thm 7.1 (state-selection.exact-equilibrium-over-determines-ledger, retired
      to tombstones.yaml) into this entity: the same theorem, the note''s ledger being the boundary modes. Kept this
      statement, levels and checks; the note''s entity is recorded above and its proof files are kept in this folder.
      References to the note''s id were repointed here. Extraction-only change, so the version and the dependants''
      pins are unchanged.'
---

## formal
Let a state satisfy the geometric modular condition exactly. Then $\varrho \propto e^{-\beta K_{\mathrm{geo}}} = \bigotimes_k e^{-\beta\omega_k K_k}$ is a product across modes, and consequently: every inter-mode correlation vanishes, $C(\varrho) = \sum_k S(\varrho_k) - S(\varrho) = 0$; the descent deficit vanishes, $\rel{\varrho}{\EN\varrho} = 0$ by Theorem \claimref{singularity.deficit-theorem-cost-descent-exactly}, the state being already a fixed point of $\EN$; and no information whatever is carried by the inter-quanta correlations of Corollary \claimref{singularity.deficit-carried-quanta-correlations}, the two levels agreeing exactly. The exact geometric modular condition is therefore available only in the stationary idealisation, and the correlations on which Steps 5 and 6b depend are precisely the deviation from it.

## technical
If a state satisfies the geometric modular condition exactly, then by KMS uniqueness $\varrho \propto e^{-\beta K_{\mathrm{geo}}} = \bigotimes_k e^{-\beta\omega_k K_k}$, a product across modes. Consequently the inter-mode correlation vanishes, $C(\varrho) = \sum_k S(\varrho_k) - S(\varrho) = 0$; the state is already a fixed point of the descent $\EN$, so by the deficit theorem $\rel{\varrho}{\EN\varrho} = 0$; and the inter-quanta correlations that carry the deficit carry no information at all, the two levels agreeing exactly.

The exact condition is therefore available only in the stationary idealisation, and the correlations on which the chain's later descent and information steps depend are precisely the deviation from it.

## lay
Requiring the boundary modes to be in perfect equilibrium with the black hole's time symmetry forces them to be completely independent of one another. Then there are no correlations between them, and stepping down to the ordinary description loses nothing. Since later steps of the argument rely on exactly those correlations, perfect equilibrium can only be an idealisation, and what matters is the departure from it.

## one-liner
A state satisfying the geometric modular condition exactly is a product across modes, so its inter-mode correlations and its descent deficit both vanish, and the correlations the later steps need are exactly the departure from this idealisation.
