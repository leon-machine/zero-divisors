---
id: descent-lift.imported-descent-modes-univalence-supplied-class-external
kind: claim
version: 1
title: 'Imported: the descent on modes, univalence, and the supplied class (external ingredients)'
status: imported
region: descent-lift
subject: descent
tags: [classical-theorem, univalence, superselection]
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
imported_from:
- citation: G. C. Wick, A. S. Wightman, E. P. Wigner, The intrinsic parity of elementary particles, Phys.
    Rev. 88 (1952) 101--105.
  key: WWW1952
locators:
  paper: T05-descent-lift
  number: Fact 1.2
  label: ''
  line: 155
extraction:
  env: fact
  context_refs:
  - singularity.descent-parity-average
  - singularity.envelope-endpoint-why-boundary-mode-locality
  - singularity.imported-univalence-superselection-rule
  - singularity.l-stabiliser-tangent
  - singularity.p-reduced-metric-level-reading-many
  - singularity.purity-output-partner-commutant
  - singularity.schmidt-forcing-proved-outright
  flags:
  - external ingredients of descent-lift.imported-descent-modes-univalence-supplied-class
  - 'statement names postulates: singularity.l-boundary-mode-locality, singularity.p-univalence'
  typing:
    by: ai-typing-pass
    note: external ingredient only (the univalence rule of Wick, Wightman and Wigner); levels written,
      nothing else changed.
---

## formal
The results from outside the series on which \claimref{descent-lift.imported-descent-modes-univalence-supplied-class} draws, as cited there: G. C. Wick, A. S. Wightman, E. P. Wigner, The intrinsic parity of elementary particles, Phys. Rev. 88 (1952) 101--105..

## technical
The external ingredient is the univalence superselection rule of Wick, Wightman and Wigner: coherent superpositions of states of opposite fermion parity are not observable, so the observable algebra of a fermionic system is the even subalgebra. The series' collected statement on the descent, univalence and the supplied class draws on it for its univalence clause.

## lay
Nature does not allow observable superpositions of a state with an even number of fermions and one with an odd number. This result of Wick, Wightman and Wigner is the outside ingredient behind the rule that physical states have even fermion parity.

## one-liner
The univalence superselection rule of Wick, Wightman and Wigner: superpositions of opposite fermion parity are unobservable, so the observable algebra is the even subalgebra.
