---
id: descent-lift.imported-pinching-one-way-door
kind: claim
version: 3
title: 'Imported: the pinching and the one-way door'
status: proved
region: descent-lift
subject: descent
tags: [descent-map, no-go]
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
derivations:
- name: main
  uses:
  - transport.door-one-way@5
  - transport.pinching-kernel@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_pinching_is_conditional_expectation
- kind: check
  ref: check.py::check_kernel_is_ladder_sector
- kind: check
  ref: check.py::check_no_return_homomorphism
locators:
  paper: T05-descent-lift
  number: Fact 1.1
  label: fact:oneway
  line: 151
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: in Cl(p+1,q+1), p+q <= 2, the pinching as an idempotent bimodule conditional expectation onto the commutant of P with kernel A f + A f*, the Wedderburn blocks of B exceeding dim A (p+q <= 3) and the non-multiplicativity. Version 2 -> 3.'
  env: fact
  context_refs:
  - transport.door-one-way
  - transport.pinching-kernel
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'restates the root paper''s pinching and one-way-door results; both uses edges are the restated
      results and are kept. Levels pass: conditions already kept.'
---

## formal
For the ascent $B = \Cl(p+1, q+1) \cong \mathrm{Mat}_{2}(A)$ of $A = \Cl(p,q)$ with ladder pair $f, f^{*}$ and occupation projector $P = f^{*}f$, the pinching $\EN(x) = PxP + (1-P)x(1-P)$ is an idempotent conditional expectation onto the commutant of $P$; its kernel is the ladder sector. There is no unital algebra homomorphism $B \to A$: every descent is non-multiplicative, and the pinching is the canonical linear surrogate. \emph{Provenance:} \cite[Prop.~7.5, Thm.~7.6]{ButlerT1}.

## technical
For the ascent $B = \Cl(p+1, q+1) \cong \Mat_{2}(A)$ of $A = \Cl(p,q)$, with ladder pair $f, f^{*}$ and occupation projector $P = f^{*}f$, the pinching $\EN(x) = PxP + (1 - P)x(1 - P)$ is an idempotent conditional expectation onto the commutant of $P$, and its kernel is the ladder sector.

There is no unital algebra homomorphism $B \to A$, so every descent is non-multiplicative and the pinching is the canonical linear surrogate.

## lay
Going up one rung of the Clifford tower doubles the algebra by adjoining a ladder pair. Coming back down can only be done by a linear averaging map that keeps what commutes with the occupation and discards the ladder, and no structure-preserving map returns. The way down is a one-way door.

## one-liner
The pinching onto the commutant of the occupation projector is an idempotent conditional expectation whose kernel is the ladder sector, and no unital homomorphism returns from the ascent to its base.
