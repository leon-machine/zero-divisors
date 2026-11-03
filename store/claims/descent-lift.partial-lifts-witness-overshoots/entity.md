---
id: descent-lift.partial-lifts-witness-overshoots
kind: claim
version: 4
title: Partial lifts, and the witness overshoots
status: proved
region: descent-lift
subject: descent
tags: [descent-map, pairing-and-bogoliubov, finite-models]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-descent-lift, the series'' standard disclaimer'
review: typed
about:
- obj.descent-lift.lift
derivations:
- name: main
  uses:
  - descent-lift.lift-costs-one-rung-per-mode@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_partial_descent_map
- kind: check
  ref: check.py::check_coherence_fraction
- kind: check
  ref: check.py::check_complete_iff_maximally_paired
locators:
  paper: T05-descent-lift
  number: Cor 5.2
  label: cor:partial
  line: 247
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the induced map rho + A^2 G0 rho G0 on every even unit for six A, the coherence factor (1 - A^2)/(1 + A^2) with values 1, 7/25, 0, -7/25, and completeness exactly at A^2 = 1. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: corollary
  typing:
    by: ai-typing-pass
    added:
    - descent-lift.lift-costs-one-rung-per-mode
    note: 'added the lift theorem, whose factorisation clause supplies the coupling C and the paired record
      state that the statement varies; the witness amplitude is a comparison with the singularity paper,
      not a premise. Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - descent-lift.lift-costs-one-rung-per-mode
---

## formal
With the record prepared in $\ket{00} + A\ket{11}$ instead of $\varphi$, the same coupling induces the partial descent $\rho \mapsto (\rho + A^{2}\G_{0}\rho\G_{0})/(1 + A^{2})$, which leaves the fraction $(1 - A^{2})/(1 + A^{2})$ of the pair's coherence: all of it at $A = 0$, $\tfrac{7}{25}$ at $A = \tfrac34$, none at $A = 1$, and $-\tfrac{7}{25}$ at $A = \tfrac43$, the amplitude of the singularity paper's witness rotation, which overshoots the descent into a sign flip. The descent is complete if and only if the record is maximally paired.

## technical
With the record prepared in $\ket{00} + A\ket{11}$ instead of the paired state $\varphi = \ket{00} + \ket{11}$, the lift's coupling $C$ induces the partial descent $\rho\mapsto(\rho + A^{2}\G_{0}\rho\G_{0})/(1 + A^{2})$, which multiplies the pair's coherence by $(1 - A^{2})/(1 + A^{2})$.

This keeps all the coherence at $A = 0$, the fraction $\tfrac{7}{25}$ at $A = \tfrac34$ and none at $A = 1$, and gives $-\tfrac{7}{25}$ at $A = \tfrac43$, the amplitude of the singularity paper's witness rotation, which overshoots the descent into a sign flip. The descent is complete if and only if the record is maximally paired.

## lay
How much of the pair's coherence is erased depends on how strongly the record is paired before the coupling acts. An unpaired record erases nothing, an evenly paired record erases everything, and an over-paired record, such as the one in the earlier black-hole witness, goes past erasure and flips the sign of the coherence.

## one-liner
With the record prepared at pairing amplitude $A$, the lift's coupling multiplies the pair's coherence by $(1 - A^{2})/(1 + A^{2})$, so the descent is complete exactly at $A = 1$ and the witness amplitude $\tfrac43$ overshoots it.
