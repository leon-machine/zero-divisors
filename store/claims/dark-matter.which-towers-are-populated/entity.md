---
id: dark-matter.which-towers-are-populated
kind: claim
version: 2
title: Which towers are populated
status: conjectured
region: dark-matter
subject: dark-matter
tags:
- towers-by-residue
- dark-matter-ratio
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
  role: 'note: the inference registered as a premise of the total'
  version: 2
  source: maintainer pass of 2026-11-10
review: typed
lineage:
  motivated_by:
  - dark-matter.mirror-tower-copy-one
  - dark-matter.towers-are-residues-single-clock-filter
locators:
  paper: T14
  number: Obs 4.10
  label: obs:population
  line: 498
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 1 -> 2. Leon''s decision 5 of 10 November 2026: the inference that the odd towers hold matter is registered as the postulate dark-matter.odd-towers-populated, assumed by the stored statements of the total; the formal and technical levels point to it. The observation is unchanged.'
  env: observation
  context_refs:
  - dark-matter.mirror-tower-copy-one
  flags:
  - 'statement names postulates: dark-matter.r2-one-quantum-per-unit-ball'
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.towers-are-residues-single-clock-filter
    note: 'Kept as a conjecture, since the source calls it an inference at observation level; added the
      residue census to motivated_by, as the observation is prompted by the census''s gap between admitting
      and holding matter. Levels pass: the lay level now flags the mirror''s population as resting on
      premise P2 rather than presenting it as an argument (review item 10).'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - dark-matter.r2-one-quantum-per-unit-ball (motivated_by)
    added_about: []
    verdict: connected
    note: Nothing derived depends on the odd towers being populated (the source says so); Premise R2 presupposes
      this inference, recorded as R2's lineage.
---

## formal
The census says which towers can hold matter; it does not say which the descent filled, and the two are at different levels. This tower is populated by observation. The mirror is populated by P2: residues $6$ and $2$ are equivalent under signature reversal, so a descent that filled one filled the other, at the same asymmetry (Theorem \claimref{dark-matter.mirror-tower-copy-one}(v)); this is the one case in which population is derived. The four odd towers are reached by nothing in the series: P2 does not equate them with this tower, the tower paper gives them algebras and not contents, and what the descent deposited in each is the pre-descent theory's, successor problem (2). What supports their population is the record read inside the framework: with the mirror's share exactly one, an empty set of odd towers would make the ratio $1$ against the observed $5.364$, and the framework has no other dark candidate, so, granted the framework, the observed remainder is the evidence that the odd towers hold matter. That is an inference at observation level, not a count, and it is what the unit-ball rule presupposes when it sums over six towers (Premise \claimref{dark-matter.r2-one-quantum-per-unit-ball}); since 10 November 2026 it is registered as a premise of the total, \claimref{dark-matter.odd-towers-populated}, with the statement that it is inferred from the number the rule fits. Nothing derived in this paper depends on the odd towers being populated: the mirror share, the superselection, the parity theorem and the arrow are the same if they are empty, and refutation item 6 says so.

## technical
The census fixes which towers can hold matter, not which the descent filled. This tower is populated by observation, and the mirror by premise P2: residues $6$ and $2$ are exchanged by signature reversal, so a descent that filled one filled the other at the same asymmetry, the one case in which population is derived. Nothing in the series reaches the four odd towers. Their population is an inference at observation level: with the mirror's share exactly one, empty odd towers would give $\Omega_{\mathrm{dark}}/\Omega_{b} = 1$ against the observed $5.364$, and, granted the framework, there is no other dark candidate. The unit-ball rule presupposes this inference when it sums over six towers, and it is now registered as a premise of that total, inferred from the number it helps fit; no derived result of the paper depends on it.

## lay
Our world plainly contains matter, and the mirror tower contains it too if one grants premise P2, that two worlds related by reversing the signature were filled alike. For the four odd towers nothing in the theory says whether they hold any matter. The paper infers that they do because, within its framework, they are the only place the observed dark matter beyond the mirror's share could be; this is a reading of observation, not a calculation.

## one-liner
This tower is populated by observation and the mirror by P2, while the population of the four odd towers is an observation-level inference from the observed dark-to-baryon ratio, granted the framework.
