---
id: field-theory.ground-does-not-attach-modes
kind: claim
version: 4
title: The ground does not attach the modes
status: proved
region: field-theory
subject: quantum-fields
tags: [no-go, conformal-model]
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
- obj.tower.tower
derivations:
- name: main
  uses:
  - tower.commuting-copies@5
  - tower.volume-elements-planes@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_QFT.py
  tags:
  - id:A1.1
  - id:A1.2
  - id:A1.3
  - id:A1.4
  - id:A1.5
  - id:A1.6
  - id:A1.7
  - id:A1.8
- kind: check
  ref: check.py::check_even_ground_commutes_with_modes
- kind: check
  ref: check.py::check_translations_and_lorentz_rotors_act_trivially
- kind: check
  ref: check.py::check_covariance_forces_constant_mode_functions
locators:
  paper: FT
  number: Prop 3.1
  label: prop:blind
  line: 92
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: that every even ground blade, translation and Lorentz rotor of Cl(2,4) fixes the mode operators of three planes, and that covariance then fixes the mode coefficients. Version 2 -> 3. Sample inputs moved to module level; no change to what is tested. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'No edges: exact computation. The proof also cites check A2, but no check of verify_QFT.py carries
      the identifier A2 (the corrected finite-dimensionality obstruction is not a tagged check), so only
      A1.1 to A1.8 are attached. Levels pass: levels written from scratch, keeping every condition and
      level qualifier of the formal statement.'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises:
    - tower.commuting-copies
    - tower.volume-elements-planes
    added_dependants:
    - field-theory.twistor-attachment
    added_about:
    - obj.tower.tower
    verdict: connected
    note: The source proves the commutation by exact computation; the added premises give the structural
      reason from T03 (even ground products are products of twisted generators), with a sentence added to
      the proof. The twistor attachment records this result as its motivation (lineage), its own proof not
      using it.
---

## formal
Over the conformal ground every even ground element commutes with every mode operator of every higher plane. In particular the conformal bivectors, the chart translations and the Lorentz rotors act trivially on the modes, so a field $\psi(x) = \sum_j u_j(x)a_j$ on which the ground's translations act covariantly has constant mode functions. The obstruction is finite-dimensionality: a noncompact group has no nontrivial unitary representation on a finite floor.

## technical
Over the conformal ground every even ground element commutes with every mode operator of every higher plane. So the conformal bivectors, the chart translations and the Lorentz rotors act trivially on the modes, and a field $\psi(x) = \sum_ju_j(x)a_j$ on which the ground's translations act covariantly has constant mode functions. The obstruction is finite-dimensionality: a noncompact group has no nontrivial unitary representation on a finite floor.

## lay
The tower adds quantum modes on top of the spacetime algebra, but the spacetime symmetries, translations, rotations and boosts, do not act on those modes at all. So the tower alone cannot place its modes in spacetime; something else must supply the link.

## one-liner
Every even ground element commutes with every higher mode operator, so the ground's translations and Lorentz rotors cannot attach the tower's modes to spacetime.
