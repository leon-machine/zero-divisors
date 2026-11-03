---
id: simulations.s2-sheet-fluid
kind: claim
version: 2
title: 'S2: the sheet fluid'
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
review: typed
locators:
  paper: T14b
  number: Premise 2.8
  label: prem:S2
  line: 134
extraction:
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

## technical
A modelling premise: at composite interaction strength the three-dimensional towers' matter is an ideal gas with two degrees of freedom, $\gamma = 2$, whose pressure and viscosity act only within its sheet; along the sheet normal it moves without pressure, since sheets cross freely. Sheets of a given orientation form one family shared by all the tower's matter, so parcels of different halos on the same sheet collide.

For parcels on differently oriented sheets, which the dark-matter paper leaves open, force and separation are contracted with the averaged projector $(P_{i} + P_{j})/2$, which is the in-sheet projection when the normals are parallel and otherwise keeps a fraction of each normal component.

## lay
The sheet-bound dark matter is modelled as a gas that pushes and resists only within its own sheet and moves freely across sheets. Matter from different halos on the same sheet can collide. Where sheets of different orientations meet, a simple averaging rule is adopted, because the underlying theory does not say what happens there.

## one-liner
The three-dimensional towers' matter is modelled as a $\gamma = 2$ ideal gas acting only within shared sheet families, with the averaged projector $(P_{i} + P_{j})/2$ between differently oriented sheets.
