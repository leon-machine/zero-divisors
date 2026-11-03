---
id: sheaf.local-freeness-constant-rank
kind: claim
version: 2
title: Local freeness at constant rank
status: proved
region: sheaf
subject: walls
tags: [degenerate-algebras]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
about:
- obj.sheaf.clifford-sheaf
derivations:
- name: main
  uses:
  - sheaf.blade-basis-degenerate-forms-included@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_constant_rank_sixteen_through_degeneration
- kind: check
  ref: check.py::check_structure_functions_polynomial_in_gram
locators:
  paper: T04
  number: Prop 2.8
  label: prop:localfree
  line: 447
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: blade symbols of rank 16 at every point of two degenerating cometrics while the Gram rank jumps, and structure functions polynomial in the Gram entries. Version 1 -> 2.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: "kept the blade-basis edge (the whole proof); added about: obj.sheaf.clifford-sheaf, the object the statement is about"
---

## formal
For any cometric $G$ on $M$, degenerate or not, $\shA$ is a locally free sheaf of $\mathcal{O}_M$-modules of constant rank $2^n$, with multiplication given in any blade frame by structure functions polynomial in the components of $G$, hence smooth. In particular the rank of $\shA$ does not detect the degeneration: no dimension jump occurs, or can occur, in the Clifford sheaf of a degenerating cometric.

## technical
For any cometric $G$ on $M$, degenerate or not, the Clifford sheaf $\shA$ is a locally free sheaf of $\mathcal{O}_M$-modules of constant rank $2^n$. On any open set where $T^*M$ has a frame, the blades $e_I$ give a basis of each fibre, by the blade-basis lemma applied pointwise to $G_x$, so they form a frame of $\shA$; the structure functions are polynomials in the smooth functions $G(e_i, e_j)$, hence smooth.

In particular the rank of $\shA$ does not detect the degeneration: no dimension jump occurs, or can occur, in the Clifford sheaf of a degenerating cometric.

## lay
Gluing together the Clifford algebras at all points of a space gives a smoothly varying family of algebras. This result shows that the family has the same size everywhere, even where the geometry degenerates. So degeneration cannot be detected by counting dimensions; it has to show up in the structure of the algebra instead.

## one-liner
For any cometric, degenerate or not, the Clifford sheaf is locally free of constant rank $2^n$ with smooth structure functions, so its rank never detects degeneration.
