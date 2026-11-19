---
id: dark-matter.r3-one-cell-per-unshared-direction
kind: claim
version: 3
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
- name: Claude Fable 5.2
  role: 'the unit of thickness restated: the one common length of Premise E, not each tower''s own cell radius'
  version: 3
  source: maintainer pass of 2026-11-19
amendments:
- version: 3
  kind: restatement
  defect: 'version 2 took the unit of thickness to be each tower''s own cell radius, which makes the total depend on the masses and numbers of the quanta separately; by the decision of 19 November 2026 the unit is one length common to all towers'
review: typed
locators:
  paper: T14
  number: Premise 7.4
  label: prem:R3
  line: 792
extraction:
  maintainer_pass_2026_11_19:
    by: maintainer-2026-11-19
    date: '2026-11-19'
    note: 'Version 2 -> 3. Leon''s decision of 19 November 2026, reversing decision 9 of 10 November 2026: R3''s unit of thickness is one fixed length common to all towers, the length d of Premise E (dark-matter.e-equal-mass-per-unit-ball), and not each tower''s own cell radius. Under R1 with R2 the two readings coincide. With this reading the total rests on E and not on R1 and R2 (synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball (i)). The premise''s value (one unit, one side) is unchanged.'
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
In the sourcing rule, a tower's matter counts through exactly one unit of length of each direction its neighbour lacks, on one side: a five-dimensional tower's matter through one unit of its extra direction, and a three-dimensional tower's sheets stacked one unit apart along the direction it lacks. Section \ref{subsec:free} gives a mechanism that returns this value and costs it.

\emph{The unit.} The unit is the length $d$ of Premise E (\claimref{dark-matter.e-equal-mass-per-unit-ball}): one length common to all towers, the radius of the ball in which E counts mass, and independent of how a tower's mass is divided into quanta. This is the fixed-common-length reading, adopted by the decision of 19 November 2026; it replaces the reading of 10 November 2026, in which the unit was each tower's own cell radius, the Wigner-Seitz radius of its own filling. Under R1 and R2 (\claimref{dark-matter.r1-equal-mass-per-quantum}, \claimref{dark-matter.r2-one-quantum-per-unit-ball}), E holds in R2's common length, which is then $d$ (Proposition \claimref{dark-matter.unit-ball-rule}(iv)), every tower's cell radius is $d$ and the two readings coincide; under R2 alone they coincide only if R2 is taken in the length $d$. They differ when R2 fails: with a tower's own cell radius $a_{r}$ as the unit the shares are $(m_{r}/m_{6})(V_{3}/V_{D_{r}})(a_{6}/a_{r})^{3}$, which Premise E does not fix, and with the common length they are $V_{3}/V_{D_{r}}$ under E alone (Theorem \claimref{synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball}(i)). The title keeps the word cell: the cell is the unit ball of Premise E. The premise takes its unit from E, so where E is not assumed the unit has to be supplied in another way: by R1 with R2, whose common cell radius is then E's length, or by the democracy premise (\claimref{dark-matter.d-democracy-total-mass}), whose length is the de Sitter radius.

## technical
Within the sourcing rule, a tower's matter counts through exactly one unit of length of each direction its neighbour lacks, on one side: a five-dimensional tower's matter through one unit of its extra direction, and a three-dimensional tower's sheets stacked one unit apart along the direction it lacks. A contact mechanism returns this value, at a stated cost, without deriving it.

The unit is the length $d$ of Premise E, one length common to all towers and independent of how a tower's mass is divided into quanta (the reading adopted on 19 November 2026). The earlier reading took each tower's own cell radius; the two coincide under R1 with R2 and differ when R2 fails, and only with the common length does the total rest on E alone. The unit is E's, so a result that assumes R3 without E has to supply it otherwise, from R1 with R2 or from the democracy premise.

## lay
When a hidden sector has a direction our world lacks, only a thin slice of it counts towards the gravity we feel, and this assumption fixes that slice at one unit of length. A mechanism is offered that gives this value, but it explains the choice rather than proving it. The unit is the same length for every sector: the radius of the ball in which another assumption (E) says every sector holds the same mass. It is not a sector's own particle spacing, which would bring the particles' masses and numbers back into the formula.

## one-liner
Premise: in the sourcing rule a tower's matter counts through exactly one unit of length, the length $d$ of Premise E common to all towers, of each direction its neighbour lacks.
