---
id: field-theory.path-integral-inside-tower
kind: claim
version: 3
title: The path integral is inside the tower
status: proved
region: field-theory
subject: quantum-fields
tags: [ladder-pairs, recovers-known-physics]
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
  - field-theory.imported-tower-limit@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_QFT.py
  tags:
  - id:D1.1
  - id:D2.1
  - id:D2.2
  - id:D2.3
  - id:D2.4
  - id:D2.5
  - id:D2.6
  - id:D2.7
  - id:D2.8
  - id:D3.1
  - id:D3.2
  - id:D3.3
  - id:D4.1
  - id:D4.2
  - id:D4.3
  - id:D4.4
- kind: check
  ref: check.py::check_grassmann_variables_are_rungs
- kind: check
  ref: check.py::check_exact_slicing_is_trace
- kind: check
  ref: check.py::check_continuum_limit_gibbs_and_fermi_dirac
- kind: check
  ref: check.py::check_two_point_function_matsubara
locators:
  paper: FT
  number: Prop 3.4
  label: prop:pathintegral
  line: 113
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Grassmann variables as further rungs, the sliced Berezin integral equal to Tr(1 - delta N)^M and the supertrace, the Gibbs and Fermi-Dirac limit with exact brackets, and the antiperiodic and periodic two-point functions. Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'No edges: exact computation on further rungs. The imported period (and the assembly-level D5
      of the run, which is not a tagged check) are not in the store. Levels pass: levels written from
      scratch, keeping every condition and level qualifier of the formal statement.'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises:
    - field-theory.imported-tower-limit
    added_dependants: []
    added_about:
    - obj.tower.tower
    verdict: connected
    note: Rests on the tower's CAR for its Grassmann rungs; the period it leaves imported is not an entity
      it relies on, and nothing in the store uses the proposition, so the link is one way.
---

## formal
Grassmann variables are further rungs. The Grassmann path integral at slicing $M$ gives $\operatorname{Tr}(1 - \delta H)^M$ exactly, and $\operatorname{Tr}\exp(-\beta H)$ and the Fermi-Dirac occupation in the limit; its two-point function is antiperiodic for the trace and periodic for the supertrace at every slicing. The period itself is imported.

## technical
Grassmann variables are further rungs of the tower. The Grassmann path integral at slicing $M$ gives $\operatorname{Tr}(1 - \delta H)^M$ exactly, and in the limit $\operatorname{Tr}\exp(-\beta H)$ and the Fermi-Dirac occupation; its two-point function is antiperiodic for the trace and periodic for the supertrace at every slicing. The period itself is imported.

## lay
The fermionic path integral, a standard tool of quantum field theory, can be built from further rungs of the tower itself. It then gives the thermal partition function and the Fermi-Dirac distribution exactly, with the usual sign rule around the thermal circle, although the length of that circle is taken from outside.

## one-liner
With Grassmann variables as further rungs, the path integral gives $\operatorname{Tr}(1 - \delta H)^M$ exactly and the thermal trace in the limit, antiperiodic for the trace, with the period imported.
