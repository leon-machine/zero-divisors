---
id: correspondence.statistics-no-go
kind: claim
version: 2
title: "The statistics no-go"
status: proved
region: correspondence
subject: conformal-spacetime
tags: [no-go, car-algebra, conformal-spinors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_trace_argument_in_finite_dimensions
- kind: check
  ref: check.py::check_cl24_commutators_have_no_scalar_part
- kind: check
  ref: check.py::check_ladder_pairs_satisfy_car_in_cl24
locators:
  paper: T09
  number: Prop 5.1
  label: prop:statistics
  line: 646
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the trace argument on sample matrices, the vanishing scalar part of every blade commutator in Cl(2,4) with tr L_x = 64 <x>_0, and the CAR ladder pairs (two real, one complex) as the contrast. Version 1 -> 2.'
  env: proposition
  typing:
    by: ai-typing-pass
    removed:
    - correspondence.imported-ladder-pairs-fock-modules-over
    note: 'Removed the ladder-pairs fact: the proof cites it only in the closing contrast with the fermionic
      side, and the trace argument does not use it.'
  source_title: "The statistics no-go"
  source_formal: |-
    The palatial algebra admits no nonzero finite-dimensional representation, and no embedding of unital algebras into any finite-dimensional algebra; in particular none into $\Cl(2,4)$ or $\Cl(2,4)_\C$, of dimension $64$.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Cosmetic only: the lay level names Penrose's programme without the word twistor. The formal level and proof are already in Clifford terms and are unchanged."
---

## formal
The palatial algebra admits no nonzero finite-dimensional representation, and no embedding of unital algebras into any finite-dimensional algebra; in particular none into $\Cl(2,4)$ or $\Cl(2,4)_\C$, of dimension $64$.

## technical
The palatial algebra, whose generators obey canonical commutation relations $[Z^\alpha, \bar Z_\beta] = \hbar\,\delta^\alpha_\beta$, has no nonzero finite-dimensional representation and admits no embedding of unital algebras into any finite-dimensional algebra. In particular it cannot sit inside $\Cl(2,4)$ or $\Cl(2,4)_\C$, each of dimension $64$.

## lay
Penrose's palatial programme uses operators obeying the same kind of commutation rule as position and momentum in quantum mechanics. Such operators can never be written as finite matrices. So the palatial algebra cannot be placed inside the completion's Clifford algebra, which has only sixty-four dimensions.

## one-liner
The palatial algebra has no nonzero finite-dimensional representation and no unital embedding into a finite-dimensional algebra, in particular none into $\Cl(2,4)$ or its complexification.
