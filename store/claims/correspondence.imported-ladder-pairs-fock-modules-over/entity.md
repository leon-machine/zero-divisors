---
id: correspondence.imported-ladder-pairs-fock-modules-over
kind: claim
version: 1
title: 'Imported: ladder pairs and Fock modules over the reals'
status: imported
region: correspondence
subject: tower
tags: [ladder-pairs, spinor-modules, witt-index]
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
imported_from:
- citation: cite[ S7] ButlerT1 ;  cite[ S 4] ButlerT3
locators:
  paper: T09
  number: Fact 2.2
  label: fact:fock
  line: 327
extraction:
  env: fact
  context_refs:
  - correspondence.fock-model-complexified-ascended-algebra
  outside_pilot_cites:
  - ButlerT1
  - ButlerT3
  flags:
  - citation taken from inline provenance (no \cite)
  typing:
    by: ai-typing-pass
    note: Kept as imported with no derivations; the context reference to the complexified Fock model is
      a forward pointer, not a premise, and no standard-route sentence applies.
---

## formal
A hyperbolic (Witt) pair $e_+, e_-$ in a real Clifford algebra yields the null pair $f = \tfrac12(e_+ + e_-)$, $f^* = \tfrac12(e_+ - e_-)$ with $f^2 = f^{*2} = 0$, $ff^* + f^*f = 1$, and the ladder pairs of a Witt decomposition act on the exterior algebra of the creation span as a fermionic Fock module, irreducibly when the form is split. \emph{Provenance:} \cite[\S7]{ButlerT1}; \cite[\S 4]{ButlerT3}. The complexified version needed below is proved in Theorem \claimref{correspondence.fock-model-complexified-ascended-algebra} rather than imported, since the maximal isotropic planes of $V_\C$ are larger than the real Witt index allows.

## technical
In a real Clifford algebra a hyperbolic (Witt) pair $e_+, e_-$ gives the null pair $f = \tfrac12(e_+ + e_-)$, $f^* = \tfrac12(e_+ - e_-)$, with $Q(f) = Q(f^*) = 0$ and $ff^* + f^*f = 1$: one annihilation and one creation operator for a single fermionic mode.

The ladder pairs of a Witt decomposition act on the exterior algebra of the creation span as a fermionic Fock module, and this module is irreducible when the form is split. The imported statement is the real one; the complexified version, where the maximal isotropic subspaces are larger than the real Witt index allows, is proved separately in the store rather than imported.

## lay
Two directions in this kind of algebra, one squaring to plus one and one to minus one, can be recombined into two elements of zero length that behave exactly like the operators that create and destroy a single fermion. Several such pairs together act on a space of states built by filling or emptying each mode, the usual Fock space of fermions. This is an imported result over the real numbers; the complex version is treated separately.

## one-liner
Each hyperbolic pair in a real Clifford algebra gives a fermionic ladder pair, and the ladder pairs of a Witt decomposition act as a Fock module on the exterior algebra of the creation span, irreducibly when the form is split.
