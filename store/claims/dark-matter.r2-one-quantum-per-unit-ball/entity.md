---
id: dark-matter.r2-one-quantum-per-unit-ball
kind: claim
version: 3
title: 'R2: one quantum per unit ball'
status: postulate
region: dark-matter
subject: dark-matter
tags:
- counting-rules
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
- name: Claude Opus 5.5
  role: wording of the premise, the list of dimensions marked as P3's window
  version: 3
  source: maintainer pass of 2026-11-09
review: typed
locators:
  paper: T14
  number: Premise 7.3
  label: prem:R2
  line: 788
extraction:
  maintainer_pass_2026_11_19:
    by: maintainer-2026-11-19
    date: '2026-11-19'
    note: 'Note, version kept, no statement changed. By Leon''s decision of 19 November 2026 the dark-to-baryon total rests on Premise E (dark-matter.e-equal-mass-per-unit-ball) and not on R1 and R2, which together imply E; R3''s unit is E''s length, so R2 no longer supplies it. The technical and lay levels say this. R2 remains a premise of the results that use a tower''s number of quanta by itself.'
  maintainer_pass_2026_11_09:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Version 2 -> 3. Wording: the list of dimensions "(2, 3 or 4)" now reads "(under P3, 2, 3 or 4)" at the formal and technical levels, since the list is the window of dark-matter.p3-nearest-dimension-representatives and the rule itself is stated for a space of any dimension (the dimension-generic reading used by synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free). What the premise asserts under P3 is unchanged.'
  typing:
    by: ai-typing-pass
    note: 'Postulate: no edges to type; levels only.'
  env: premise
  context_refs:
  - dark-matter.which-towers-are-populated
lineage:
  motivated_by:
  - dark-matter.which-towers-are-populated
---

## formal
A populated tower whose space has $D$ dimensions (under P3, \claimref{dark-matter.p3-nearest-dimension-representatives}, $2$, $3$ or $4$) holds one quantum per unit ball $\B^{D}$ of that space, in one unit of length common to all towers: every tower has the same Wigner-Seitz radius. The rule presupposes that all six towers are populated, which for the odd four is the inference of Observation \claimref{dark-matter.which-towers-are-populated}.

## technical
A populated tower whose space has $D$ dimensions (under P3, $D = 2, 3, 4$) holds one quantum per unit ball $\mathrm{B}^{D}$ of that space, in one unit of length common to all towers, so every tower has the same Wigner-Seitz radius. The rule presupposes that all six towers are populated, which for the four odd towers is an inference from the observed remainder rather than a result.

With R1 it implies Premise E, equal mass per unit ball, which is what the dark-to-baryon total uses; since the decision of 19 November 2026 the total rests on E and not on R2, and R3's unit is E's length, which is R2's cell radius only when R1 holds with it. R2 remains a premise of the stored results that use a tower's number of quanta by itself.

## lay
This assumption says that in every hidden sector the particles are packed at the same typical spacing: one per ball of a fixed size, measured in that sector's own number of dimensions. It also takes for granted that every sector contains matter at all. The formula for the amount of dark matter was first stated with it, and no longer needs it: it needs only the mass per ball, not the number of particles. The assumption is kept for the results that do count particles.

## one-liner
Premise: each populated tower holds one quantum per unit ball of its space, with one Wigner-Seitz radius common to all towers.
