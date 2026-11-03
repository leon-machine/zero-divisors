---
id: field-theory.composite-gauge-bosons-what-excluded
kind: claim
version: 4
title: 'Composite gauge bosons: what is excluded'
status: proved
region: field-theory
subject: quantum-fields
tags: [gauge-fields, no-go]
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
  - field-theory.imported-standard-field-theory@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_BOS.py
  tags:
  - id:V2
- kind: check
  ref: check.py::check_current_transforms_as_a_vector
- kind: check
  ref: check.py::check_vector_condensate_breaks_lorentz
locators:
  paper: FT
  number: Prop 7.2
  label: prop:composite
  line: 194
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the vector covariance of the GA current under rotors and definite-parity elements (failing for mixed parity) and that a vector condensate is moved by boosts. Version 2 -> 3. Sample inputs moved to module level; no change to what is tested. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - field-theory.imported-standard-field-theory
    note: 'Added the standard field-theory fact for the Weinberg-Witten exclusion (V1 is imported, not
      a check of the run; only V2 is a check). Levels pass: levels written from scratch, keeping every
      condition and level qualifier of the formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - field-theory.imported-standard-field-theory
---

## formal
The GA current transforms as a vector, $J(Sf, Sg) = SJ(f,g)\tilde S$, for every element $S$ of definite parity; so a nonzero vector condensate breaks Lorentz invariance, and a massless composite photon as a Goldstone mode of one (Bjorken) conflicts with the exact Lorentz invariance of the series' exterior. Massless composites charged under a covariant current of the fermions are excluded by Weinberg and Witten. Massive composite vectors and gauge bosons of an emergent gauge symmetry are not addressed. The elementary route was taken because the author chose it, not because it is forced.

## technical
The geometric-algebra current transforms as a vector, $J(Sf, Sg) = SJ(f,g)\tilde S$ for every element $S$ of definite parity, so a nonzero vector condensate breaks Lorentz invariance, and a massless composite photon as a Goldstone mode of one (Bjorken's) conflicts with the exact Lorentz invariance of the series' exterior. Massless composites charged under a covariant current of the fermions are excluded by the Weinberg-Witten theorem. Massive composite vectors and gauge bosons of an emergent gauge symmetry are not addressed, so the elementary route is the author's choice, not forced.

## lay
One could try to build the photon out of pairs of fermions. Two standard versions are ruled out: a photon arising from a vector condensate would break the exact relativity symmetry of the series' spacetime, and a known theorem forbids massless charged composites of this kind. Other composite routes are left open, so making the photon elementary was a choice, not a necessity.

## one-liner
A vector condensate breaks Lorentz invariance and Weinberg and Witten exclude charged massless composites, but massive or emergent composites are not addressed, so the elementary photon is chosen, not forced.
