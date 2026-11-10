---
id: simulations.s4-our-matter
kind: claim
version: 2
title: 'S4: our matter (model specification)'
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
  role: 'typed as model specification'
  version: 2
  source: maintainer pass of 2026-11-10
review: typed
locators:
  paper: T14b
  number: Premise 2.10
  label: prem:S4
  line: 142
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 1 -> 2. Leon''s decision 10 of 10 November 2026: the six simulation premises (C, S1 to S5) are typed as model specification. The store has no entity type for a model specification, and an object cannot be the target of an assumes edge, so the entity keeps kind claim and status postulate (the assumes edges of simulations.halo-shapes and simulations.merger stand) and is marked in its title and at every level. Recorded as a numerical approximation.'
  typing:
    by: ai-typing-pass
    note: Postulate; no edges.
  env: premise
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - simulations.merger
    - simulations.halo-shapes
    added_about: []
    verdict: connected
    note: Assumed by the merger and cluster-assembly runs.
---

## formal
Our gas is adiabatic, $\gamma = 5/3$, without cooling. Galaxies are collisionless particles carrying $2$ percent of each halo's mass. They are stellar-mass tracers on galaxy scales (each carries $10^{10}$ to $4 \times 10^{10}\ \Msun$), not galaxies with internal structure.

\emph{Type: model specification.} This is a clause of the specification of the numerical model of the cluster simulations (Premises S1 to S5 and C), not a hypothesis of the series about nature; it is kept with the premises so that the two simulation results show it among their conditions. It is a numerical approximation of this tower's matter and is not true of it as a statement about nature (our gas cools).

## technical
A modelling premise: our gas is adiabatic with $\gamma = 5/3$ and does not cool. Galaxies are collisionless particles carrying $2$ percent of each halo's mass, each of $10^{10}$ to $4 \times 10^{10}\ \Msun$; they trace stellar mass on galaxy scales and have no internal structure.

Type: model specification: a numerical approximation of this tower's matter, not a statement about nature (our gas cools).

## lay
In the simulations ordinary gas is not allowed to cool, and galaxies are represented by heavy point-like particles that pass through one another. These particles carry a small fixed share of each halo's mass and stand in for where the stars are, not for the inner workings of galaxies. It is part of the set-up of a computer model, not a claim of the theory about nature.

## one-liner
Model specification: our gas is adiabatic with $\gamma = 5/3$ and no cooling, and galaxies are collisionless tracer particles carrying $2$ percent of each halo's mass.
