---
id: odd-extensions.imported-representatives-dimension-nearest-four-types
kind: claim
version: 4
title: 'Imported: the representatives at the dimension nearest four, and the types'
status: proved
region: odd-extensions
subject: dark-matter
tags: [towers-by-residue, clifford-classification]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14a, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-matter.towers-are-residues-single-clock-filter@5
  - dark-matter.type-residue-what-each-tower-can@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_representatives_and_sterile
- kind: check
  ref: check.py::check_shadow_types
- kind: check
  ref: check.py::check_type_depends_on_residue_alone
locators:
  paper: T14a
  number: Fact 1.2
  label: fact:reps
  line: 411
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the P3 representatives and sterile residues, and the Wedderburn types Mat(2,H) and Mat(4,R) as functions of the residue. Version 3 -> 4.'
  source_formal: |-
    At the dimension nearest four the residues are represented by the shadows $(1,3)$ at $r = 6$, $(3,1)$ at $r = 2$, $(2,2)$ at $r = 0$, $(0,4)$ and $(4,0)$ at $r = 4$, $(2,1)$ at $r = 1$, $(1,2)$ at $r = 7$, $(4,1)$ at $r = 3$ and $(1,4)$ at $r = 5$; the residues $0$ and $4$ are sterile and the other six are populated. The real spinor type is a function of the residue alone: $\Cl(1,3) \cong \Mat(2,\HH)$ (quaternionic, one module) and $\Cl(3,1) \cong \Mat(4,\R)$ (real, one module); in particular the two are not isomorphic as real algebras. \emph{Provenance:} \cite[Prop.~3.1, Thm.~3.4]{ButlerT14}.
  env: fact
  context_refs:
  - dark-matter.towers-are-residues-single-clock-filter
  - dark-matter.type-residue-what-each-tower-can
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'Restatement; kept both uses edges. The source fact says the six are populated, whereas the
      dark-matter census proves only that they admit matter and the population of the odd towers is an
      observation-level inference. Levels pass: all three levels now mark the populated clause for the
      odd towers as observation level (review item 5); status left unchanged as the pass requires.'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 12
    note: "The restatement said the other six residues 'are populated'; the originals (T14 Prop 3.1, Thm 3.4) say they admit matter, and which the descent populated is a further question (the odd towers' population is held as conjectured in dark-matter.which-towers-are-populated). Corrected to 'admit matter' at every level and in the proof; the paper's wording is kept in source_formal and orig-proof-main.tex. Dependants checked: none carries the phrase."
---

## formal
At the dimension nearest four the residues are represented by the shadows $(1,3)$ at $r = 6$, $(3,1)$ at $r = 2$, $(2,2)$ at $r = 0$, $(0,4)$ and $(4,0)$ at $r = 4$, $(2,1)$ at $r = 1$, $(1,2)$ at $r = 7$, $(4,1)$ at $r = 3$ and $(1,4)$ at $r = 5$; the residues $0$ and $4$ are sterile and the other six admit matter. The real spinor type is a function of the residue alone: $\Cl(1,3) \cong \Mat(2,\HH)$ (quaternionic, one module) and $\Cl(3,1) \cong \Mat(4,\R)$ (real, one module); in particular the two are not isomorphic as real algebras. \emph{Provenance:} \cite[Prop.~3.1, Thm.~3.4]{ButlerT14}.

## technical
Imported from earlier in the series. At the dimension nearest four the residues are represented by the shadows $(1,3)$ at $r = 6$, $(3,1)$ at $r = 2$, $(2,2)$ at $r = 0$, $(0,4)$ and $(4,0)$ at $r = 4$, $(2,1)$ at $r = 1$, $(1,2)$ at $r = 7$, $(4,1)$ at $r = 3$ and $(1,4)$ at $r = 5$; the residues $0$ and $4$ are sterile and the other six admit matter; which of them the descent populated is a further question, answered for the mirror by Premise P2 and for the odd towers only by the record. The real spinor type is a function of the residue alone; in particular $\Cl(1,3) \cong \Mat(2,\HH)$ is quaternionic and $\Cl(3,1) \cong \Mat(4,\R)$ is real, each with one module, so the two are not isomorphic as real algebras.

## lay
This collects, for the odd-extensions note, which signature stands for each of the eight towers when the dimension is kept as close to four as possible. Two of the eight have no single time direction and are ruled out; the other six can hold matter, though whether the odd ones actually do is a further question, which only observation can answer. It also records that our world's algebra and the mirror's differ as real algebras, one built on quaternions and the other on real numbers.

## one-liner
Imported: the nearest-four representatives of the eight residues, with $r = 0, 4$ sterile and the other six admitting matter, and spinor type a function of the residue, so that $\Cl(1,3) \cong \Mat(2,\HH)$ and $\Cl(3,1) \cong \Mat(4,\R)$ differ.
