---
id: note.state-selection.setting-univalence-marginals-upstairs-2
kind: note
version: 3
title: Univalence, and the marginals upstairs
status: setting
subject: descent
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-state-selection, the series'' standard disclaimer'
comments_on:
- singularity.ascended-marginals-are-diagonal
- singularity.p-univalence
- obj.singularity.grading-parity-automorphism
- singularity.descent-parity-average
locators:
  paper: T05-state-selection
  number: Setting
  section: The form is forced; only one number is free
  line: 191
  subsection: Univalence, and the marginals upstairs
extraction:
  source_formal: |-
    Premise \claimref{state-selection.p-univalence} is available to the chain for a reason the chain itself supplies: the ledger is a CAR algebra by the tower limit \cite[Thm.~5.6]{ButlerT3}, its grading is the Clifford grading of Definition \claimref{obj.state-selection.grading-parity-automorphism}, and by Theorem \claimref{state-selection.descent-parity-average} its even part is exactly the metric-level algebra. What the univalence rule asserts is that the odd sector carries no expectation values, and Theorem \claimref{state-selection.descent-parity-average} says that this is the same as asserting that the ascended and descended readings agree \emph{per mode}. That is a considerably weaker demand than boost invariance of the whole state, and it is not a choice of state: it is a statement about which elements of the algebra are observables.
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 7
    note: 'Moved the comments_on link and the claimref in the formal level from the retired state-selection.p-univalence to singularity.p-univalence (merge of duplicates); version bumped.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: The state-selection note's duplicates of T05 entities were retired to tombstones.yaml (merged into the T05
      entities). References moved from the retired obj.state-selection.grading-parity-automorphism, state-selection.ascended-marginals-are-diagonal,
      state-selection.descent-parity-average to obj.singularity.grading-parity-automorphism, singularity.ascended-marginals-are-diagonal,
      singularity.descent-parity-average; version 2 -> 3.
---

## formal
Premise \claimref{singularity.p-univalence} is available to the chain for a reason the chain itself supplies: the ledger is a CAR algebra by the tower limit \cite[Thm.~5.6]{ButlerT3}, its grading is the Clifford grading of Definition \claimref{obj.singularity.grading-parity-automorphism}, and by Theorem \claimref{singularity.descent-parity-average} its even part is exactly the metric-level algebra. What the univalence rule asserts is that the odd sector carries no expectation values, and Theorem \claimref{singularity.descent-parity-average} says that this is the same as asserting that the ascended and descended readings agree \emph{per mode}. That is a considerably weaker demand than boost invariance of the whole state, and it is not a choice of state: it is a statement about which elements of the algebra are observables.

## technical
pending

## lay
pending

## one-liner
pending
