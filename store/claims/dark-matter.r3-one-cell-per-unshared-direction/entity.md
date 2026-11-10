---
id: dark-matter.r3-one-cell-per-unshared-direction
kind: claim
version: 2
title: 'R3: one cell per unshared direction'
status: postulate
region: dark-matter
subject: dark-matter
tags: [counting-rules]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
- name: Claude Fable 5.2
  role: 'the unit of thickness stated: each tower''s own cell radius, so R2 also supplies R3''s unit'
  version: 2
  source: maintainer pass of 2026-11-10
review: typed
locators:
  paper: T14
  number: Premise 7.4
  label: prem:R3
  line: 792
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 1 -> 2. Leon''s decision 9 of 10 November 2026: R3''s unit of thickness is each tower''s own cell radius (the literal wording, and the convention of the thickness function). Version 1 did not say whose cell radius is meant when R2 is varied. R2 therefore also supplies R3''s unit and stays a premise of the total; the fixed-common-length reading, under which synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball holds, is recorded as not adopted. The premise''s value (one cell radius, one side) is unchanged.'
  typing:
    by: ai-typing-pass
    note: "Postulate: no edges to type; levels only."
  env: premise
---

## formal
In the sourcing rule, a tower's matter counts through exactly one cell radius of each direction its neighbour lacks, on one side: a five-dimensional tower's matter through one radius of its extra direction, and a three-dimensional tower's sheets stacked one radius apart along the direction it lacks. Section \ref{subsec:free} gives a mechanism that returns this value and costs it.

\emph{The unit.} The cell radius of the premise is each tower's own cell radius, the Wigner-Seitz radius of that tower's own filling (the convention of the thickness $c\,d_{b}$ of Proposition \claimref{dark-matter.total-function-thickness}). Under R2 (\claimref{dark-matter.r2-one-quantum-per-unit-ball}) every tower has the same cell radius, so R2 also supplies R3's unit: it enters the total twice, as a number density and as this unit, and stays a premise of the total. The other reading, in which the thickness is one fixed length common to all towers and independent of their filling, is not adopted; the reduction of R1 and R2 to equal mass per unit ball (Theorem \claimref{synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball}) holds only in that reading.

## technical
Within the sourcing rule, a tower's matter counts through exactly one cell radius of each direction its neighbour lacks, on one side: a five-dimensional tower's matter through one radius of its extra direction, and a three-dimensional tower's sheets stacked one radius apart along the direction it lacks. A contact mechanism returns this value, at a stated cost, without deriving it.

The unit is each tower's own cell radius. Under R2 that radius is common to all towers, so R2 also supplies R3's unit and stays a premise of the total. The reading with one fixed common length independent of the filling is not adopted; the reduction of R1 and R2 to equal mass per unit ball holds only in that reading.

## lay
When a hidden sector has a direction our world lacks, only a thin slice of it counts towards the gravity we feel, and this assumption fixes that slice at one particle spacing. A mechanism is offered that gives this value, but it explains the choice rather than proving it. The spacing meant is each sector's own particle spacing; since another assumption (R2) makes that spacing the same in every sector, that assumption is also what gives this one its unit of length.

## one-liner
Premise: in the sourcing rule a tower's matter counts through exactly one cell radius, the tower's own (common to all towers under R2, which so also supplies the unit), of each direction its neighbour lacks.
