---
id: descent-lift.imported-fermionic-operations-are-even-reduced
kind: claim
version: 1
title: 'Imported: fermionic operations are even, and reduced states are restrictions'
status: imported
region: descent-lift
subject: descent
tags: [classical-theorem, grading-and-parity]
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
- citation: S. B. Bravyi, A. Yu. Kitaev, Fermionic quantum computation, Ann. Phys. 298 (2002) 210--226.
  key: BravyiKitaev2002
- citation: H. Araki, H. Moriya, Joint extension of states of subsystems for a CAR system, Commun. Math.
    Phys. 237 (2003) 105--122.
  key: ArakiMoriya2003
  locator: Thm.~1
- citation: G. C. Wick, A. S. Wightman, E. P. Wigner, The intrinsic parity of elementary particles, Phys.
    Rev. 88 (1952) 101--105.
  key: WWW1952
locators:
  paper: T05-descent-lift
  number: Fact 1.4
  label: fact:even
  line: 163
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Note only, version kept: for mode algebras the content of this Fact (the reduced state is the restriction to the subsystem''s algebra; it agrees with the partial trace when the complement''s states are even; products with an even factor exist) is now derived in the algebra, and sharpened, in synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product, clauses (i), (iii), (iv), (v): the reduction to one side is a partial trace of the twisted tensor split for every state, and the other reduction differs exactly on listed odd blades. This Fact is not retired: it is stated for a general fermionic system with the univalence rule, and its first sentence (the implementable unitaries are the even ones) is not part of that result. Whether its dependants cite the derived result in its place is left open.'
  env: fact
  context_refs:
  - descent-lift.imported-descent-modes-univalence-supplied-class
  typing:
    by: ai-typing-pass
    note: imported with provenance; no edges; the context reference to the series' univalence fact is
      attribution of the rule, not a premise of an imported result.
---

## formal
In a fermionic system with the univalence rule, the physically implementable unitaries are those commuting with the total parity, the even ones; an odd operation would carry an even state to an odd one or to a superposition of the two. The reduced state of a subsystem is the restriction of the state to the subsystem's algebra; when the complementary subsystem's states are even, this agrees with the partial trace in the tensor-product basis, and a product state $\omega_{S} \otimes \omega_{R}$ exists whenever one factor is even. \emph{Provenance:} \cite{BravyiKitaev2002}; \cite[Thm.~1]{ArakiMoriya2003}; the univalence rule \cite{WWW1952}, imported by the singularity paper as Fact \claimref{descent-lift.imported-descent-modes-univalence-supplied-class}.

## technical
Under the univalence rule the implementable unitaries of a fermionic system are the even ones, those commuting with the total parity; an odd operation would take an even state to an odd one or to a superposition of the two. The reduced state of a subsystem is the restriction of the state to the subsystem's algebra.

When the complementary subsystem's states are even this restriction agrees with the partial trace in the tensor-product basis, and a product state $\omega_{S}\otimes\omega_{R}$ exists whenever one factor is even.

## lay
For fermions, the operations one can actually perform must preserve whether the particle number is even or odd. Looking at part of a fermionic system means restricting attention to the operators on that part, and when the rest has even parity this matches the usual recipe of tracing it out. Two independent subsystems can always be combined when one of them has even parity.

## one-liner
Under univalence the implementable fermionic operations are the even ones, and reduced states are restrictions to subalgebras, agreeing with the partial trace when the complement is even.
