---
id: simulations.s2-sheet-fluid
kind: claim
version: 3
title: 'S2: the sheet fluid (model specification, reading (W))'
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
  role: 'typed as model specification; S2 and C recorded as premises of the exclusive readings (W) and (C)'
  version: 3
  source: maintainer pass of 2026-11-10
review: typed
locators:
  paper: T14b
  number: Premise 2.8
  label: prem:S2
  line: 134
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 2 -> 3. Leon''s decision 10 of 10 November 2026: the six simulation premises (C, S1 to S5) are typed as model specification. The store has no entity type for a model specification, and an object cannot be the target of an assumes edge, so the entity keeps kind claim and status postulate (the assumes edges of simulations.halo-shapes and simulations.merger stand) and is marked in its title and at every level. S2 and C are recorded as the premises of the two exclusive readings (W) and (C), not as jointly assumed.'
  typing:
    by: ai-typing-pass
    note: Postulate; no edges. The averaged pair operator lemma in context_refs describes a property of
      the adopted rule, not a premise of a postulate.
  env: premise
  context_refs:
  - dark-matter.projection-every-towers-content-dilutes-ones
  - simulations.averaged-pair-operator
  outside_pilot_cites:
  - ButlerT14
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises:
    - dark-matter.projection-every-towers-content-dilutes-ones (motivated_by)
    - dark-matter.r3-one-cell-per-unshared-direction (motivated_by)
    - simulations.averaged-pair-operator (motivated_by)
    added_dependants:
    - simulations.merger
    - simulations.halo-shapes
    added_about: []
    verdict: connected
    note: Assumed by the merger and cluster-assembly runs; lineage to the T14 projection lemma and R3
      it cites for the shared sheet family and to the averaged pair operator lemma.
lineage:
  motivated_by:
  - dark-matter.projection-every-towers-content-dilutes-ones
  - dark-matter.r3-one-cell-per-unshared-direction
  - simulations.averaged-pair-operator
---

## formal
At composite strength the three-dimensional towers' matter is an ideal gas with two degrees of freedom ($\gamma = 2$) whose pressure and viscosity act only within its sheet. Along the sheet's normal it moves without pressure, since sheets cross freely \cite[Rem.~7.30]{ButlerT14}. The sheets of a given orientation form one family shared by all the matter of the tower \cite[Lem.~6.1, Prem.~7.4]{ButlerT14}, so parcels of different halos on the same sheet collide. T14 does not say how quanta on differently oriented sheets interact; between two such parcels the force and separation are contracted with the mean of the two in-plane projectors, $(P_{i} + P_{j})/2$, which is the projection onto the sheet when the normals are parallel and otherwise keeps a fraction of each normal component (Lemma \claimref{simulations.averaged-pair-operator}).

\emph{Type: model specification.} This is a clause of the specification of the numerical model of the cluster simulations (Premises S1 to S5 and C), not a hypothesis of the series about nature; it is kept with the premises so that the two simulation results show it among their conditions. Premises C and S2 belong to two exclusive readings of the three-dimensional towers' matter in the simulations: reading (C), collisionless, under Premise \claimref{simulations.c-odd-towers-collisionless}, and reading (W), a sheet fluid at composite strength, under Premise \claimref{simulations.s2-sheet-fluid}. The two simulation results (\claimref{simulations.halo-shapes}, \claimref{simulations.merger}) list both among their conditions because each reports both readings; no result holds the two together. S2 is conditional on the three-dimensional towers' matter interacting at composite strength, the negation of C for those towers; under C it is vacuous for them. In the merger result reading (W) holds the subcluster's sheet fluid back with its gas and, with random or line-of-sight normals, gives no separate lensing peak (\claimref{simulations.merger}).

## technical
A modelling premise: at composite interaction strength the three-dimensional towers' matter is an ideal gas with two degrees of freedom, $\gamma = 2$, whose pressure and viscosity act only within its sheet; along the sheet normal it moves without pressure, since sheets cross freely. Sheets of a given orientation form one family shared by all the tower's matter, so parcels of different halos on the same sheet collide.

For parcels on differently oriented sheets, which the dark-matter paper leaves open, force and separation are contracted with the averaged projector $(P_{i} + P_{j})/2$, which is the in-sheet projection when the normals are parallel and otherwise keeps a fraction of each normal component.

Type: model specification, the premise of reading (W) of the simulations, exclusive with reading (C) (Premise C); under C it is vacuous for the three-dimensional towers. The two simulation results list both premises because each reports both readings.

## lay
The sheet-bound dark matter is modelled as a gas that pushes and resists only within its own sheet and moves freely across sheets. Matter from different halos on the same sheet can collide. Where sheets of different orientations meet, a simple averaging rule is adopted, because the underlying theory does not say what happens there. It is part of the set-up of a computer model, not a claim of the theory about nature. It belongs to one of two alternative versions of the model, the one in which this matter collides with itself; the other version (C) treats it as collisionless, and the two are never assumed together.

## one-liner
Model specification, reading (W) of the simulations (exclusive with reading (C) of Premise C): the three-dimensional towers' matter is modelled as a $\gamma = 2$ ideal gas acting only within shared sheet families, with the averaged projector $(P_{i} + P_{j})/2$ between differently oriented sheets.
