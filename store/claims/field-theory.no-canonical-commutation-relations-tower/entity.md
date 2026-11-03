---
id: field-theory.no-canonical-commutation-relations-tower
kind: claim
version: 3
title: No canonical commutation relations in the tower
status: proved
region: field-theory
subject: quantum-fields
tags: [no-go, car-algebra]
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
  - field-theory.imported-statistics-no-go-palatial-algebra@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_INT.py
  tags:
  - id:B1
- kind: check
  ref: check.py::check_scalar_part_is_a_trace_on_every_floor
- kind: check
  ref: check.py::check_matrix_trace_kills_commutators
- kind: check
  ref: check.py::check_composite_pair_is_not_excluded
locators:
  paper: FT
  number: Prop 6.3
  label: prop:nocc
  line: 173
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the scalar part is a trace on every floor up to Cl(3,5) (all blade pairs), the matrix trace of commutators, and the fermion-pair composite obeying the relation on the vacuum. Version 1 -> 2. Fix round: the matrix-unit trace loop of check_matrix_trace_kills_commutators extended to three modes (all 64 x 64 unit pairs), matching docstring (1). Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'Kept the statistics fact (the trace argument and the Wielandt-Wintner theorem the proof cites).
      Levels pass: levels written from scratch, keeping every condition and level qualifier of the formal
      statement.'
---

## formal
No floor contains a pair with $[a, a^*] = 1$, and no bounded element of the CAR limit satisfies it. Bosons made of fermions are not excluded by this.

## technical
No floor of the tower contains a pair with $[a, a^*] = 1$, since the scalar part is a trace on each floor and kills every commutator, and no bounded element of the CAR limit satisfies it, by the Wielandt-Wintner theorem. This does not exclude bosons made of fermions.

## lay
The exact commutation rule of elementary bosons cannot be satisfied inside any finite part of the tower, nor by bounded operators in its limit. That does not rule out bosons that are composites of the tower's fermions.

## one-liner
No floor contains a pair with $[a, a^*] = 1$ and no bounded element of the CAR limit satisfies it, though bosons made of fermions are not excluded.
