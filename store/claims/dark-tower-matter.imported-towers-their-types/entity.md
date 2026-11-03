---
id: dark-tower-matter.imported-towers-their-types
kind: claim
version: 4
title: 'Imported: the towers and their residues'
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [towers-by-residue, superselection]
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
  - dark-matter.flag-bit-exists-exactly-tower-dimension@3
  - dark-matter.superselected-hence-dark-exactly-stable@5
  - dark-matter.towers-are-residues-single-clock-filter@5
  - dark-matter.type-residue-what-each-tower-can@5
  - tower.rigidity-clock-frozen@5
  assumes:
  - dark-matter.p3-nearest-dimension-representatives@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_residue_constant_along_ascents
- kind: check
  ref: check.py::check_representatives_under_p3
- kind: check
  ref: check.py::check_odd_residues_carry_no_bit
locators:
  paper: T14c
  number: Fact 2.1
  label: fact:towers
  line: 198
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: residue invariance under (1,1) ascents, the P3 representatives and sterile residues, and the odd residues'' central pseudoscalar with no bit. Version 3 -> 4.'
  env: fact
  context_refs:
  - dark-matter.flag-bit-exists-exactly-tower-dimension
  - dark-matter.superselected-hence-dark-exactly-stable
  - dark-matter.towers-are-residues-single-clock-filter
  - dark-matter.type-residue-what-each-tower-can
  - tower.rigidity-clock-frozen
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.p3-nearest-dimension-representatives
    note: 'Kept the five restated sources; added Premise P3 as assumed, since the statement gives the
      representatives under it. Levels pass: levels written from scratch, keeping every condition and
      level qualifier of the formal statement.'
---

## formal
The residue $r = p - q \bmod 8$ is constant along each tower of $(1,1)$ ascents. Under T14's Premise P3 the representatives are $(1,3)$ at $r = 6$, $(3,1)$ at $r = 2$, $(2,1)$ and $(1,2)$ at $r = 1, 7$, $(4,1)$ and $(1,4)$ at $r = 3, 5$, $(2,2)$ at $r = 0$ and $(4,0)$ or $(0,4)$ at $r = 4$; $r = 0$ and $r = 4$ are sterile. The odd residues carry no orientation bit and therefore no asymmetry. The towers interact only through the one metric (exact superselection). Sources: \cite[Prop.~3.1, Thm.~3.4, Thm.~3.10, Prop.~4.1]{ButlerT14}, \cite[Thm.~3.6]{ButlerT3}.

## technical
The residue $r = p - q \bmod 8$ is constant along each tower of $(1,1)$ ascents. Under the dark-matter paper's Premise P3 the representatives are $(1,3)$ at $r = 6$, $(3,1)$ at $r = 2$, $(2,1)$ and $(1,2)$ at $r = 1, 7$, $(4,1)$ and $(1,4)$ at $r = 3, 5$, $(2,2)$ at $r = 0$ and $(4,0)$ or $(0,4)$ at $r = 4$, the last two sterile. The odd residues carry no orientation bit and therefore no asymmetry, and the towers interact only through the one metric (exact superselection).

## lay
The dark-matter paper sorts the possible worlds into eight towers by a number that counts, modulo eight, the difference between their space and time directions; under its premise that each tower is represented by its nearest-dimension member, this fixes one or two signatures per tower. Two towers are sterile, the odd-dimensional towers cannot store a matter-antimatter asymmetry, and the towers affect one another only through gravity.

## one-liner
Under Premise P3 the eight towers have the listed representatives, $r = 0, 4$ are sterile, the odd residues carry no asymmetry, and the towers interact only through the one metric.
