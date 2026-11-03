---
id: field-theory.boost-modes
kind: claim
version: 3
title: The boost on the modes
status: proved
region: field-theory
subject: quantum-fields
tags: [rotors-and-stabilisers, car-algebra, modular-theory]
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
  uses:
  - field-theory.imported-tower-limit@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_QFT.py
  tags:
  - id:B1.0
  - id:B1.1
  - id:B1.2
  - id:B1.3
  - id:B1.4
  - id:B1.5
  - id:B1.6
  - id:B1.7
  - id:B1.8
- kind: check
  ref: check.py::check_real_rapidity_is_not_a_star_map
- kind: check
  ref: check.py::check_uniform_real_boost_unbounded
- kind: check
  ref: check.py::check_imaginary_rapidity_is_unitary_phase
locators:
  paper: FT
  number: Prop 3.3
  label: prop:boost
  line: 106
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the real-rapidity rotor (scaling, CAR, not a *-map), its unbounded uniform action over k planes, and the unitary imaginary-rapidity rotor as the number flow. Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - field-theory.imported-tower-limit
    note: 'Added the tower-limit fact, whose CAR and CAR algebra the statement is about. The reading of
      the parent paper''s premise (R) that the run flags is in the proof''s level note, not in the statement,
      so nothing was added for it. Levels pass: levels written from scratch, keeping every condition and
      level qualifier of the formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - field-theory.imported-tower-limit
---

## formal
On a plane's mode operators the real-rapidity rotor acts by scaling, preserves the CAR, and is not a $*$-map; uniformly over many planes it has no bounded extension to the CAR algebra. The imaginary-rapidity rotor is unitary and acts by phases. So on the modes the series' geometric boost is the imaginary-time (KMS-strip) map, and the unitary real-time flow is the rotor at imaginary rapidity.

## technical
On a tower plane's mode operators the real-rapidity rotor acts by scaling $v$ and $v^*$ by inverse factors: it preserves the CAR but is not a $*$-map, and uniformly over many planes it has no bounded extension to the CAR algebra. The rotor at imaginary rapidity is unitary and acts by phases. So on the modes the series' geometric boost is the imaginary-time (KMS-strip) map, and the unitary real-time flow is the rotor at imaginary rapidity.

## lay
In the series a boost between observers is a rotation in a plane of the algebra. Acting on the tower's quantum modes, such a boost stretches and squeezes them rather than rotating them, so it is not a quantum symmetry in the usual sense. Its imaginary-angle counterpart is one, and the two are related as real and imaginary time are in thermal field theory.

## one-liner
On a plane's modes the real-rapidity rotor scales and is not a $*$-map, while the imaginary-rapidity rotor is unitary, so the geometric boost is the imaginary-time map.
