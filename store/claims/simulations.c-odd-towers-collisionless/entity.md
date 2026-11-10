---
id: simulations.c-odd-towers-collisionless
kind: claim
version: 3
title: 'C: the odd towers collisionless (model specification, reading (C))'
status: postulate
region: simulations
subject: dark-matter
tags:
- halos-and-clusters
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14b, deposited version
- name: Claude Fable 5.2
  role: 'typed as model specification; C and S2 recorded as premises of the exclusive readings (C) and (W)'
  version: 3
  source: maintainer pass of 2026-11-10
review: typed
locators:
  paper: T14b
  number: Premise 2.12
  label: prem:C
  line: 150
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 2 -> 3. Leon''s decision 10 of 10 November 2026: the six simulation premises (C, S1 to S5) are typed as model specification. The store has no entity type for a model specification, and an object cannot be the target of an assumes edge, so the entity keeps kind claim and status postulate (the assumes edges of simulations.halo-shapes and simulations.merger stand) and is marked in its title and at every level. C and S2 are recorded as the premises of the two exclusive readings (C) and (W), not as jointly assumed; C is recorded as the condition the cluster bound requires, undecided in the store.'
  env: premise
  context_refs:
  - simulations.confinement-scale-does-not-matter
  typing:
    by: ai-typing-pass
    note: Postulate; no edges. The confinement-scale corollary supplies the quoted numbers but is not
      a premise of a premise.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises:
    - simulations.confinement-scale-does-not-matter (motivated_by)
    added_dependants:
    - simulations.merger
    - simulations.halo-shapes
    added_about: []
    verdict: connected
    note: The merger and cluster-assembly observations hold for reading (C) under this premise; lineage
      to the confinement corollary that supplies its phase-shift numbers.
lineage:
  motivated_by:
  - simulations.confinement-scale-does-not-matter
---

## formal
The matter of the four odd towers (the two three-dimensional and the two five-dimensional towers) has no self-interaction of order one. For the three-dimensional towers this means an in-sheet s-wave phase shift below about $2 \times 10^{-7}$ at cluster speeds for isotropic compression, $4 \times 10^{-6}$ for compression normal to the sheets (Corollary \claimref{simulations.confinement-scale-does-not-matter}).

\emph{Type: model specification.} This is a clause of the specification of the numerical model of the cluster simulations (Premises S1 to S5 and C), not a hypothesis of the series about nature; it is kept with the premises so that the two simulation results show it among their conditions. Premises C and S2 belong to two exclusive readings of the three-dimensional towers' matter in the simulations: reading (C), collisionless, under Premise \claimref{simulations.c-odd-towers-collisionless}, and reading (W), a sheet fluid at composite strength, under Premise \claimref{simulations.s2-sheet-fluid}. The two simulation results (\claimref{simulations.halo-shapes}, \claimref{simulations.merger}) list both among their conditions because each reports both readings; no result holds the two together. C is not a statement about the series' structure: it is the condition the cluster bound requires (Corollary \claimref{simulations.confinement-scale-does-not-matter}), adopted as the premise of reading (C). Whether it holds is not decided by anything stored: the radiation audit leaves the three-dimensional towers' self-interaction at composite strength if their matter is the confined charged matter its closure leaves, which the series does not establish (Proposition \claimref{dark-matter.radiation-audit-what-theorem-closes-what}).

## technical
The premise is that the matter of the four odd towers, the two three-dimensional and the two five-dimensional towers, has no self-interaction of order one. For the three-dimensional towers this is quantified as an in-sheet s-wave phase shift below about $2 \times 10^{-7}$ at cluster speeds for isotropic compression, and below $4 \times 10^{-6}$ for compression normal to the sheets, the values given by the confinement-scale corollary.

Type: model specification, the premise of reading (C) of the simulations. Reading (C) and reading (W) (the sheet fluid, Premise S2) are exclusive; the two simulation results list both premises because each reports both readings. C is what the cluster bound requires, adopted as a premise, and nothing stored decides it.

## lay
The simulations assume that dark matter in the four odd towers passes through itself without significant collisions. For the towers that live on sheets this is made precise as a very weak scattering strength at the speeds typical of galaxy clusters. It is stated as a premise of the simulations, not derived. It is part of the set-up of a computer model, not a claim of the theory about nature. It belongs to one of two alternative versions of the model, the one in which this matter does not collide; the other version (S2) treats it as a fluid, and the two are never assumed together.

## one-liner
Model specification, reading (C) of the simulations (exclusive with reading (W) of S2): the odd towers' matter has no self-interaction of order one, which for the three-dimensional towers means an in-sheet s-wave phase shift below about $2 \times 10^{-7}$ (isotropic) or $4 \times 10^{-6}$ (normal compression) at cluster speeds.
