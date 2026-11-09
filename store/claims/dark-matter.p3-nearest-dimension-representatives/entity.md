---
id: dark-matter.p3-nearest-dimension-representatives
kind: claim
version: 3
title: 'P3: nearest-dimension representatives'
status: postulate
region: dark-matter
subject: dark-matter
tags: [premises-p1-p5, towers-by-residue]
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
  role: note on the premise by residue, the odd residues' choice following from Premise U at 1 and 7 and independent at 3 and 5
  version: 3
  source: maintainer pass of 2026-11-09
review: typed
locators:
  paper: T14
  number: Premise 2.3
  label: prem:window
  line: 104
extraction:
  maintainer_pass_2026_11_09:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Version 2 -> 3. Note added at the formal and technical levels: the premise''s lowest-causal choice at residues 1 and 7 follows from Premise U (dark-tower-matter.u-transposition-rule), and at residues 3 and 5 it is independent of the descent, by synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free (ii), (iii). What the premise asserts is unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 1 -> 2. Note added at the formal and technical levels (decision of 2026-10-31): premise (W) of synthesis.frozen-point-complement-window-lowest-causal is recorded as a costed alternative restating this window, found with the fit known; not adopted, with no postulate and no assumes edge. What the premise asserts is unchanged.'
  typing:
    by: ai-typing-pass
    note: "Postulate: no edges to type; levels only."
  env: premise
  context_refs:
  - dark-matter.towers-are-residues-single-clock-filter
---

## formal
Each tower is represented at the dimension nearest four; where two are equally near (the odd residues, three and five), the lower one with a single time, else the higher. \emph{Support:} P1's one metric read as minimality. Structural premise; Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter}(iii) records the other windows. \emph{Note.} Premise (W) of \claimref{synthesis.frozen-point-complement-window-lowest-causal}, that every tower's spacetime is, up to sign, a nondegenerate subspace of the frozen point's complement, is recorded as a costed alternative that restates this premise's window (with the single-clock filter it would replace this premise and the residue-$4$ half of the costed single-ideal clause of Observation \claimref{dark-matter.status-rule}(vi) by one hypothesis; at residue $0$ it admits the causal $(1,1)$ where this premise has $(2,2)$); it was found with the fit known and is not adopted. This premise is unchanged. \emph{Note (by residue).} At the odd residues this premise takes the lowest causal member, $(2,1)$, $(1,2)$ at residues $1$, $7$ and $(4,1)$, $(1,4)$ at residues $3$, $5$. At residues $1$ and $7$ that choice follows from Premise U (\claimref{dark-tower-matter.u-transposition-rule}): the constituent field is $\R$ in every causal member and the stored pair count exceeds the real Witt index $2$ above dimension three, so U admits only $(2,1)$ and $(1,2)$. At residues $3$ and $5$ it is independent of the descent: a model with those towers at $(12,1)$ and $(1,12)$ satisfies every premise of the window-sensitive results other than this one, Premise U included, so there the window is an input (Theorem \claimref{synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free}(ii), (iii)).

## technical
Each tower, labelled by its residue mod $8$, is represented at the dimension nearest four. For the odd residues, where dimensions three and five are equally near, the lower is taken if it has a single time, otherwise the higher. The support offered is a reading of the one metric of Premise P1 as a minimality condition; what other windows would give is recorded separately. A geometric restatement of the window, that every tower's spacetime is up to sign a nondegenerate subspace of the frozen point's complement, is recorded as a costed alternative found with the fit known, and is not adopted. At the residues one and seven the choice of the lowest causal member follows from Premise U, which admits no higher causal member there; at the residues three and five it is independent of the other premises, which a model with those towers at dimension thirteen also satisfies.

## lay
Each hidden sector could in principle be realised with several different numbers of dimensions. This assumption picks, for each one, the number closest to our four, with a tie-break for the cases exactly in between. It is a choice the paper makes, not something it derives.

## one-liner
Premise: each tower is represented at the dimension nearest four, ties going to the lower dimension when it has a single time.
