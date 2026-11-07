---
id: singularity.universality-temperature-under-g
kind: claim
version: 3
title: Universality of the temperature under (G)
status: proved
region: singularity
subject: thermality
tags: [hawking-temperature, modular-theory]
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
derivations:
- name: main
  uses:
  - singularity.kms-uniqueness-factor@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:7.15
- kind: check
  ref: check.py::check_g_gives_one_temperature
- kind: check
  ref: check.py::check_product_satisfies_g_only_at_equal_betas
locators:
  paper: T05
  number: Cor 7.15
  label: cor:universal
  line: 1822
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the K_geo Gibbs state has Gibbs marginals at one beta on nonzero-weight modes (zero-weight marginal maximally mixed), and a product of Gibbs marginals is a K_geo Gibbs state only at equal betas. Version 2 -> 3.'
  env: corollary
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    - singularity.q-joint-quasi-freeness-s-wave
    added:
    - obj.singularity.geometric-modular-condition-g
    note: 'Removed the mechanical transport-algorithm edge and the (Q) assumption: the statement is already
      restricted to modes of nonzero weight, and the proof cites (Q) only to explain why a zero-weight
      mode occurs.'
  merged_from:
  - id: state-selection.universality-temperature
    version: 1
    locators:
      paper: T05-state-selection
      number: Cor 4.4
      label: cor:universal
      line: 235
    about:
    - obj.state-selection.geometric-modular-condition
    uses:
    - state-selection.kms-uniqueness-factor@1
    checked_by: verify_state_selection.py num:4.4
    proof_files:
    - proof-main.tex (kept here as merged-state-selection.universality-temperature-proof-main.tex)
    formal: 'A state satisfying the GMC has $\beta_k = \beta$ independent of $k$: one temperature for the whole ledger.
      Conversely a state with per-mode marginals $\mathrm{Gibbs}(\beta_k\omega_k)$ and no inter-mode correlation satisfies
      the GMC only if the $\beta_k$ coincide.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Merged the state-selection note''s Cor 4.4 (state-selection.universality-temperature, retired to tombstones.yaml)
      into this entity: the same corollary; the T05 statement adds the nonzero-weight scope. Kept this statement,
      levels and checks; the note''s entity is recorded above and its proof files are kept in this folder. References
      to the note''s id were repointed here. Extraction-only change, so the version and the dependants'' pins are
      unchanged.'
---

## formal
A state satisfying (G) has $\beta_k = \beta$ independent of $k$ over the modes of nonzero weight: one temperature for all the boundary modes. Conversely a state with per-mode marginals $\mathrm{Gibbs}(\beta_k\omega_k)$ and no inter-mode correlation satisfies (G) only if the $\beta_k$ of the modes of nonzero weight coincide.

## technical
By KMS uniqueness on the factor, a state satisfying (G) is $\varrho \propto e^{-\beta K_{\mathrm{geo}}} = \bigotimes_k e^{-\beta\omega_k K_k}$, whose marginal at mode $k$ is $\mathrm{Gibbs}(\beta\omega_k)$: the same inverse temperature $\beta_k = \beta$ at every mode of nonzero weight.

Conversely, a product state with marginals $\mathrm{Gibbs}(\beta_k\omega_k)$ has modular generator $-\sum_k \beta_k\omega_k N_k$ up to a constant, which is proportional to $K_{\mathrm{geo}}$ only if $\beta_k\omega_k = \lambda\omega_k$ for a single $\lambda$; so it satisfies (G) only if the $\beta_k$ of the modes of nonzero weight coincide. A mode of zero weight constrains nothing.

## lay
If the boundary modes' internal clock runs exactly along the black hole's time symmetry, every mode has the same temperature. Conversely, independent modes at different temperatures cannot have such a clock. Modes that carry no energy are left out, since for them the temperature makes no difference.

## one-liner
A state satisfying (G) has one inverse temperature $\beta_k = \beta$ for all boundary modes of nonzero weight, and an uncorrelated state with Gibbs marginals satisfies (G) only if those $\beta_k$ coincide.
