---
id: field-theory.contact-interactions-tower
kind: claim
version: 4
title: Contact interactions in the tower
status: proved
region: field-theory
subject: quantum-fields
tags: [scattering-amplitudes]
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
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_INT.py
  tags:
  - id:C1.1
  - id:C1.2
  - id:C1.3
  - id:C1.4
  - id:C2.1
  - id:C2.2
  - id:C2.3
  - id:C2.4
  - id:C3
  - id:C3b
- kind: check
  ref: check.py::check_contact_term_structure
- kind: check
  ref: check.py::check_matrix_element_and_s_squared_law
- kind: check
  ref: check.py::check_crossed_amplitude_u_squared_law
- kind: check
  ref: check.py::check_boosted_frames
locators:
  paper: FT
  number: Prop 6.2
  label: prop:contact
  line: 166
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: self-adjointness, charge conservation and grade four of the contact term, the tower matrix element, |M|^2/s^2 = 1/4 and the crossed |M|^2/u^2 = 1/4, and boosted frames. Version 1 -> 2. The formal level restated: Fix round 2026-10-23: the 1/4 laws hold for spinors normalised to J(f, f) = k (in general |M|^2/(g^2 c1c2c3c4 s^2) = 1/4), as the checks compute; the coupling g made explicit. Version 2 -> 3. The technical level restated: Fix round 2026-10-23: the 1/4 laws hold for spinors normalised to J(f, f) = k (in general |M|^2/(g^2 c1c2c3c4 s^2) = 1/4), as the checks compute; the coupling g made explicit. The one-liner level restated: Fix round 2026-10-23: the 1/4 laws hold for spinors normalised to J(f, f) = k (in general |M|^2/(g^2 c1c2c3c4 s^2) = 1/4), as the checks compute; the coupling g made explicit. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - obj.field-theory.single-algebra-field
    note: 'Added the single-algebra field as about. The source calls Fermi contact scattering a textbook
      result reproduced in the series'' algebra; no imported Fermi-theory claim is in the store, so no
      standard-route derivation was added. Levels pass: levels written from scratch, keeping every condition
      and level qualifier of the formal statement.'
about:
- obj.field-theory.single-algebra-field
---

## formal
For two right-handed species the current-current density $H = g J_A\cdot J_B$, built in the single algebra on four particle modes, is self-adjoint, commutes with both charges, and has tower grade four. Its tower matrix element is $\langle A3, B4|H|A1, B2\rangle = g J_A(3,1)\cdot J_B(4,2)$, with $|M|^2/(g^2 s^2) = 1/4$ for spinors normalised to $J^{\mu}(f, f) = k^{\mu}$ (in general $|M|^2/(g^2 c_1c_2c_3c_4\,s^2) = 1/4$ with $J(f_i, f_i) = c_i k_i$) at every configuration tested, in centre-of-mass and boosted frames; with the second species as antiparticles the crossed amplitude gives $|M|^2/(g^2 u^2) = 1/4$ under the same normalisation.

## technical
For two right-handed species the current-current density $H = gJ_A\cdot J_B$, built in the single algebra on four particle modes, is self-adjoint, commutes with both charges and has tower grade four. Its tower matrix element is $\langle A3, B4|H|A1, B2\rangle = gJ_A(3,1)\cdot J_B(4,2)$, with $|M|^2/(g^2 s^2) = 1/4$ for spinors normalised to $J^{\mu}(f, f) = k^{\mu}$ (in general $|M|^2/(g^2 c_1c_2c_3c_4\,s^2) = 1/4$ with $J(f_i, f_i) = c_i k_i$) at every configuration tested, in centre-of-mass and boosted frames; with the second species as antiparticles the crossed amplitude gives $|M|^2/(g^2 u^2) = 1/4$ under the same normalisation.

## lay
The simplest interaction between two kinds of fermion, a contact interaction between their currents like Fermi's theory of weak decay, can be written as an element of the tower. Its scattering amplitudes come out as in the standard theory in every frame tested, for particles and antiparticles alike.

## one-liner
For two right-handed species the contact term $gJ_A\cdot J_B$ is a self-adjoint, charge-conserving tower element with $|M|^2/(g^2 s^2) = 1/4$ at every tested configuration and $|M|^2/(g^2 u^2) = 1/4$ crossed, for spinors normalised to $J^{\mu}(f, f) = k^{\mu}$.
