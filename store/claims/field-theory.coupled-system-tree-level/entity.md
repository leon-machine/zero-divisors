---
id: field-theory.coupled-system-tree-level
kind: claim
version: 4
title: The coupled system at tree level
status: proved
region: field-theory
subject: quantum-fields
tags: [recovers-known-physics, gauge-fields, scattering-amplitudes]
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
- name: Claude Opus 5.5
  role: 'maintainer pass on Leon''s decisions, the unit named as I_4 in place of ''i = I_4'' (wording)'
  version: 4
  source: maintainer pass 2026-11-07 (decisions)
review: typed
derivations:
- name: main
  uses:
  - field-theory.fock-space-maxwell-modes@4
  - field-theory.imported-standard-field-theory@4
  proof: proof-main.tex
- name: standard-route
  uses:
  - field-theory.imported-standard-field-theory@4
  proof: proof-standard-route.tex
checked_by:
- kind: proof
  derivation: main
- kind: proof
  derivation: standard-route
- kind: legacy
  script: verify_PHO.py
  tags:
  - id:C1
  - id:C1q
  - id:C2
  - id:C2c
  - id:C3
  - id:C3h
  - id:C4
  - id:C4c
- kind: check
  ref: check.py::check_vertex_self_adjoint_and_charge_conserving
- kind: check
  ref: check.py::check_second_order_amplitude_distinguishable
- kind: check
  ref: check.py::check_coulomb_term_and_both_helicities_needed
- kind: check
  ref: check.py::check_ga_product_vertex_same_amplitude
- kind: check
  ref: check.py::check_identical_fermions_exchange_sign
locators:
  paper: FT
  number: Prop 8.2
  label: prop:coupled
  line: 229
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit naming (DECISIONS H1, R06 item 1): ''with $i = I_4$'' identified a bare i with the unit, which the unit principle treats as a bare unit; the levels and proofs now name the unit (''with the unit $I_4$'', ''the field theory''s unit $I_4$''). Mechanical; no content change.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: self-adjointness and charge conservation of the vertex, the second-order amplitude on the coupled space with its controls, the GA-product vertex, and the identical-fermion exchange sign. Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - field-theory.fock-space-maxwell-modes
    - field-theory.imported-standard-field-theory
    note: 'Added the Fock-space proposition (the polynomial factor of the coupled state space) and the
      standard field-theory fact (the Coulomb-gauge Hamiltonian, which supplies H_C). Standard route added:
      the ledger calls Coulomb-gauge exchange a textbook result reproduced in the algebra. Levels pass:
      levels written from scratch, keeping every condition and level qualifier of the formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - field-theory.fock-space-maxwell-modes
    - field-theory.imported-standard-field-theory
---

## formal
On the coupled state space (tower element times polynomial), $H_{\mathrm{int}} = e\sum J^\mu A_\mu$ is self-adjoint and conserves the fermion charges. The second-order amplitude $H_{\mathrm{int}}(E_i - H_0)^{-1}H_{\mathrm{int}} + H_C$, with $H_0$ applied as an operator, equals $-e^2J_A(3,1)\cdot J_B(4,2)/t$ for distinguishable fermions and $-e^2(J_{31}\cdot J_{42}/t - J_{41}\cdot J_{32}/u)$ for identical ones, exactly. Dropping the Coulomb term, one helicity, or the fermionic ordering gives a different amplitude.

## technical
On the coupled state space, tower element times polynomial, $H_{\mathrm{int}} = e\sum J^\mu A_\mu$ is self-adjoint and conserves the fermion charges. The second-order amplitude $H_{\mathrm{int}}(E_i - H_0)^{-1}H_{\mathrm{int}} + H_C$, with $H_0$ applied as an operator, equals $-e^2J_A(3,1)\cdot J_B(4,2)/t$ for distinguishable fermions and $-e^2(J_{31}\cdot J_{42}/t - J_{41}\cdot J_{32}/u)$ for identical ones, exactly. Dropping the Coulomb term, one helicity or the fermionic ordering gives a different amplitude.

## lay
Coupling the tower's fermions to the photon's quantum states, the computation reproduces at lowest order the textbook scattering of two charged particles by photon exchange, including the exchange term for identical particles. Each ingredient matters: leaving out the Coulomb term, one photon helicity or the fermions' sign rule changes the answer.

## one-liner
At tree level the coupled fermion-photon system gives exactly $-e^2J_A\cdot J_B/t$ for distinguishable fermions and the antisymmetrised amplitude for identical ones.
