---
id: note.singularity.declared-residual-size
kind: note
version: 1
title: The declared residual, and its size
status: remark
subject: entropy
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
comments_on:
- singularity.class-relative-no-go-no-supplied
- singularity.bundle-maps-quantise-without-hopping
- singularity.function-linear-endomorphisms-are-bundle-maps
- singularity.envelope-endpoint-why-boundary-mode-locality
locators:
  paper: T05
  number: Rem C.9
  label: rem:hopresidual
  line: 2714
---

## formal
The excluded class is small, as the theorem itself records: for a line bundle the $C^\infty(E)$-linear endomorphisms are multiplication operators, and the supplied class is ultralocal. Every dynamics with a kinetic term lies in the residual: a first-order differential operator of Dirac type has $[D, f] = c(df) \neq 0$, lies outside the $C^\infty$-linear class, and would hop; and so, at the coefficient-linear level, would the pairing terms named in the theorem. The closure constructs none of these, and nothing here excludes one in nature. Two remarks on method. First, support preservation is not the right criterion: a $C^\infty$-linear map preserves supports, but so does every differential operator (Peetre's theorem identifies the support-preserving linear maps of sections with the differential operators), so support preservation alone would not have given Proposition \claimref{singularity.bundle-maps-quantise-without-hopping}; tensoriality, Lemma \claimref{singularity.function-linear-endomorphisms-are-bundle-maps}, is what is needed. Second, the necessity witness of Corollary \claimref{singularity.envelope-endpoint-why-boundary-mode-locality} is a pairing rotation, $|00\rangle \mapsto \tfrac35|00\rangle + \tfrac45|11\rangle$ with $\Delta N = \pm 2$, not a hop: the generator that shows (L$_E$) cannot be dropped is one this theorem's criterion does not exclude, which is consistent, and is why the exclusion of pairing terms stays with the premise. The sharp remaining form of Remark \claimref{note.singularity.steps-status-what-still-open}(b)'s question is therefore: is the physical dynamics on the singular boundary generated within the supplied class, or does it carry a differential or pairing term? That is a successor question, recorded beside the closure-completeness programme; Proposition \claimref{singularity.l-stabiliser-tangent} separates the two residual types by what they do to the vacuum, the differential term lying in its stabiliser and the pairing term in the tangent of its orbit.

## technical
pending

## lay
pending

## one-liner
pending
