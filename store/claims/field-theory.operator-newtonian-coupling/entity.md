---
id: field-theory.operator-newtonian-coupling
kind: claim
version: 4
title: The operator Newtonian coupling
status: proved
region: field-theory
subject: quantum-fields
tags: [quantum-gravity, entanglement, live-prediction]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of FT, the series'' standard disclaimer'
review: typed
about:
- obj.field-theory.single-algebra-field
derivations:
- name: main
  uses:
  - field-theory.conserved-numbers-mass-block@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_GRV.py
  tags:
  - id:G4
  - id:G4c
  - id:G4m
  - id:G4q
  - id:G5
  - id:G5c
  - id:G6
- kind: check
  ref: check.py::check_operator_coupling_gives_registered_phase
- kind: check
  ref: check.py::check_no_self_interaction_unlike_mean_field
- kind: check
  ref: check.py::check_massive_sources_quasi_particles_and_block_charges
- kind: check
  ref: check.py::check_rigid_composites_monopole_plus_a_squared
locators:
  paper: FT
  number: Prop 9.2
  label: prop:newton
  line: 254
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: H_N from commuting numbers in GA gives the registered phase +Phi at three layouts, no self-interaction against the mean-field control, quasi-particle and block-charge sources on a mass block, and the (a/R)^2 composite correction as an exact rational function. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - field-theory.conserved-numbers-mass-block
    - pred.gravity-entangles-standard-phase
    note: 'Added the mass-block proposition, which supplies the quasi-particle numbers and block charges
      the coupling is built from, and a supports link to the registered prediction whose phase and sign
      the statement reproduces. The static weak-field limit of the minimal coupling, imported in the proof,
      is not in the store. Levels pass: levels written from scratch, keeping every condition and level
      qualifier of the formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - field-theory.conserved-numbers-mass-block
supports:
- pred.gravity-entangles-standard-phase@3
- pred.no-gravitational-settling@1
---

## formal
With $H_N = -G\sum_{i<j}M_iM_jN_iN_j/r_{ij}$ built from commuting conserved numbers (rung numbers of massless modes, quasi-particle numbers or block charges of massive ones), the branch states are eigenstates and the relative phase $\arg(c_{11}c_{22}/(c_{12}c_{21}))$ under $\exp(-I_4Ht)$ is $+\Phi$, the registered phase with its sign. The operator source gives no interaction between a body's own branches, unlike the mean-field (Schr\"odinger-Newton) source, which entangles nothing. For rigid composite bodies the phase is that of the total mass plus a correction of relative order $(a/R)^2$.

## technical
With $H_N = -G\sum_{i<j}M_iM_jN_iN_j/r_{ij}$ built from commuting conserved numbers (rung numbers of massless modes, quasi-particle numbers or block charges of massive ones), the branch states are eigenstates and the relative phase $\arg(c_{11}c_{22}/(c_{12}c_{21}))$ under $\exp(-I_4Ht)$ is $+\Phi$, the registered phase with its sign. The operator source gives no interaction between a body's own branches, unlike the mean-field (Schr\"odinger-Newton) source, which entangles nothing. For rigid composite bodies the phase is that of the total mass plus a correction of relative order $(a/R)^2$.

## lay
If gravity's Newtonian pull is built from conserved particle numbers, two masses each held in a superposition of two places pick up exactly the entangling phase the series registered as a prediction, with the right sign. A mean-field version of gravity would entangle nothing, and composite bodies, if rigid, behave like point masses up to a small correction.

## one-liner
Built from commuting conserved numbers, the operator Newtonian coupling gives the registered entangling phase $+\Phi$ with its sign, unlike the mean-field source, with an $(a/R)^2$ correction for rigid composites.
