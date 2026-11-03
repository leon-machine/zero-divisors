---
id: dark-tower-matter.imported-our-towers-chain
kind: claim
version: 3
title: 'Imported: our tower''s Standard-Model chain'
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [ladder-pairs, mass-generation]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T14c, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - mass.mass-symplectic-area-two-twistor-formula@3
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - standard-model.global-form-quotient-determined@3
  - standard-model.hypercharge-global-form-pair-counting-consistency@5
  - standard-model.imported-pair-systems-two-chirality-halves@5
  - standard-model.internal-symmetry-ladder@3
  - standard-model.pair-count-dimension@3
  - standard-model.quarks-leptons-two-level-fermion-content@5
  - standard-model.ten-transported-ambient-space-doublets-are@2
  - tower.ladder-pairs-satisfy-car-vectors@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_one_and_two_constituents
- kind: check
  ref: check.py::check_three_ladder_pairs
- kind: check
  ref: check.py::check_mixings_are_unitary
- kind: check
  ref: check.py::check_content_anomalies_and_lattice
locators:
  paper: T14c
  number: Fact 2.3
  label: fact:chain
  line: 206
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: null and two-constituent momenta, three ladder pairs obeying the CAR, unitary mixings, and the content''s anomalies, Z_6 lattice and 12-dimensional algebra. Version 2 -> 3.'
  env: fact
  context_refs:
  - mass.mass-symplectic-area-two-twistor-formula
  - standard-model.gauge-algebra-minimal-massive-composite
  - standard-model.global-form-quotient-determined
  - standard-model.hypercharge-global-form-pair-counting-consistency
  - standard-model.imported-pair-systems-two-chirality-halves
  - standard-model.internal-symmetry-ladder
  - standard-model.pair-count-dimension
  - standard-model.quarks-leptons-two-level-fermion-content
  - standard-model.ten-transported-ambient-space-doublets-are
  - tower.ladder-pairs-satisfy-car-vectors
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'Reviewed the ten mechanically added sources: each is a result the fact restates (mass formula,
      ladder pairs, CAR rungs, the U(n) ladder, content, global form, hypercharges, Higgs doublets), so
      all were kept. Levels pass: levels written from scratch, keeping every condition and level qualifier
      of the formal statement.'
---

## formal
In this tower: a single constituent has null momentum and two have the squared mass of T11's two-constituent formula \cite[Prop.~4.1]{ButlerT11}, \cite[Fact~2.1]{ButlerT12}; each constituent carries three ladder pairs \cite[Fact~2.2, Lem.~2.12]{ButlerT12}, the tower's rungs satisfying the canonical anticommutation relations \cite[Prop.~4.1]{ButlerT3}; the mixings of $n$ constituents preserving their total momentum and helicity form are $U(n)$ \cite[Prop.~3.1]{ButlerT12}; and the content, hypercharges, anomalies and Higgs representation are \cite[Thm.~4.1, Thm.~4.2, Prop.~5.3, Thm.~5.5, Prop.~9.22]{ButlerT12}.

## technical
The facts about this tower that the note transposes: a single constituent has null momentum and two have the squared mass of the mass paper's two-constituent formula; each constituent carries three ladder pairs, the tower's rungs satisfying the canonical anticommutation relations; the mixings of $n$ constituents preserving their total momentum and helicity form are $U(n)$; and the content, hypercharges, anomaly cancellation and Higgs representation are those of the Standard-Model paper.

## lay
This collects the steps by which the series derives our own particle physics: when mass first appears, how many internal pairs each constituent has, which mixings keep total momentum, and the resulting particles and charges. The dark-tower note repeats each step in the other towers.

## one-liner
In our tower one constituent is massless and two give the mass paper's formula, each carries three canonical ladder pairs, momentum-preserving mixings form $U(n)$, and the Standard-Model content follows.
