---
id: odd-extensions.four-extensions-are-four-odd-towers
kind: claim
version: 4
title: The four extensions are the four odd towers
status: proved
region: odd-extensions
subject: tower
tags: [towers-by-residue, mirror-sector]
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
about:
- obj.odd-extensions.single-extension
derivations:
- name: main
  uses:
  - odd-extensions.belongs-tower@5
  - odd-extensions.imported-representatives-dimension-nearest-four-types@4
  - odd-extensions.imported-towers-clock@5
  - odd-extensions.translation-bivectors-frozen-point@4
  - odd-extensions.four-extensions-oriented-pair@6
  - odd-extensions.imported-conformal-completion@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_residues_and_roles
- kind: check
  ref: check.py::check_conformal_step_is_one_rung
- kind: check
  ref: check.py::check_frozen_point_algebra_coincides_as_algebra_only
- kind: proof
  derivation: main
locators:
  paper: T14a
  number: Prop 5.1
  label: prop:clock
  line: 545
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: residues and roles of the four extensions, Cl(2,3) and Cl(3,2) as one rung over Cl(1,2) and Cl(2,1), and the frozen point''s quadratic space against its soldered part. Version 3 -> 4.'
  env: proposition
  context_refs:
  - odd-extensions.four-extensions-oriented-pair
  - odd-extensions.imported-conformal-completion
  typing:
    by: ai-typing-pass
    added:
    - odd-extensions.four-extensions-oriented-pair
    - odd-extensions.imported-conformal-completion
    note: 'Added the four-extensions corollary (source of the residues the statement opens with) and the
      conformal-completion fact (the proof''s identification of the ambients); all four existing uses
      are cited in the proof and kept. Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - odd-extensions.four-extensions-oriented-pair
    - odd-extensions.imported-conformal-completion
---

## formal
The residues of the four extensions are $5$, $7$, $1$, $3$ (Corollary \claimref{odd-extensions.four-extensions-oriented-pair}), and they land on the odd towers in two roles: $\Cl(1,4)$ and $\Cl(4,1)$, this world's space extension and the mirror's time extension, are the representatives at the dimension nearest four of the residues $5$ and $3$ (Fact \claimref{odd-extensions.imported-representatives-dimension-nearest-four-types}), the two five-dimensional dark towers; $\Cl(2,3)$ and $\Cl(3,2)$, this world's time extension and the mirror's space extension, are the conformal ambients (Fact \claimref{odd-extensions.imported-conformal-completion}) of the representatives $(1,2)$ and $(2,1)$ of the residues $7$ and $1$, the two three-dimensional dark towers. This is a statement about abstract algebras: the frozen point's algebra $\Cl(I^{\perp})$ of Proposition \claimref{odd-extensions.translation-bivectors-frozen-point} coincides with a five-dimensional shadow for $\Lambda > 0$ and with a three-dimensional ambient for $\Lambda < 0$ as an algebra, and Proposition \claimref{odd-extensions.belongs-tower} says that as a soldered object it is neither.

## technical
The four single extensions have residues $5, 7, 1, 3$ and land on the four odd towers in two roles. $\Cl(1,4)$ and $\Cl(4,1)$, this world's space extension and the mirror's time extension, are the representatives at the dimension nearest four of residues $5$ and $3$, the two five-dimensional dark towers. $\Cl(2,3)$ and $\Cl(3,2)$, this world's time extension and the mirror's space extension, are the conformal ambients of the representatives $(1,2)$ and $(2,1)$ of residues $7$ and $1$, the two three-dimensional dark towers.

This is a statement about abstract algebras only. The frozen point's algebra $\Cl(I^{\perp})$ coincides as an algebra with a five-dimensional shadow for $\Lambda > 0$ and with a three-dimensional ambient for $\Lambda < 0$, but as a soldered object it is neither.

## lay
Adding one direction to our spacetime's algebra, or to its mirror's, can be done in four ways, and the four results match, as algebras, the four odd dark towers of the series. Two match the dark towers' own algebras directly and two match them after the one-step conformal enlargement. The matching is purely algebraic: once one tracks which directions belong to spacetime, the frozen point's algebra is none of them.

## one-liner
As abstract algebras the four single extensions, of residues $5, 7, 1, 3$, are the four odd dark towers, two as five-dimensional representatives and two as conformal ambients of three-dimensional ones, though the frozen point's algebra is neither as a soldered object.
