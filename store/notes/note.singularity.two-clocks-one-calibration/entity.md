---
id: note.singularity.two-clocks-one-calibration
kind: note
version: 2
title: Two clocks, one calibration
status: remark
subject: thermality
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
- name: Claude Opus 5.5
  role: merge of the duplicate state-selection remark
  version: 2
  source: maintainer pass of 7 November 2026
comments_on:
- singularity.rate-rigidity-temperature-not-algebra-intrinsic
- singularity.plane-rate
locators:
  paper: T05
  number: Rem 7.17
  label: rem:clocks
  line: 1844
extraction:
  merged_from:
  - id: note.state-selection.two-clocks-one-calibration
    version: 2
    locators:
      paper: T05-state-selection
      number: Rem 4.6
      label: rem:clocks
      line: 256
  maintainer_pass_warnings:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2: the state-selection note''s copy of this remark (Rem 4.6, similarity 0.94) was retired into this one, as the other state-selection duplicates of T05 entities were on 22 October; its locator is kept under merged_from and its label points here.'
---

## formal
Theorem \claimref{singularity.rate-rigidity-temperature-not-algebra-intrinsic} is a no-go, and a constructive one: it says exactly what kind of input is needed and how much of it. The inverse temperature is a ratio of two clocks, the modular clock of the state and the geometric clock of the Killing boost, and a ratio of clocks is meaningless until one is calibrated. The chain calibrates exactly once, in Proposition \claimref{singularity.plane-rate}: an interval of $2\pi$ in rapidity is $2\pi/\kappa = 8\pi M$ of Schwarzschild time. Everything numerical in this step passes through that conversion, as the step already said, and the rigidity theorem now proves that no rearrangement of the algebra can remove the need for it. The residual sign in clause (2) is not new either: it is the orientation of the boost, the labelling of outgoing against ingoing, flagged in Remark \claimref{note.singularity.frame-made-explicit} as the $\mathbb{Z}_2$ attached to the weights of $v$ and $v^{*}$. The rigidity theorem identifies that $\mathbb{Z}_2$ as the entire automorphism-theoretic freedom in the temperature.

## technical
pending

## lay
pending

## one-liner
pending
