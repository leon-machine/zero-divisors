---
id: simulations.s5-halos
kind: claim
version: 2
title: 'S5: halos (model specification)'
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
  number: Premise 2.11
  label: prem:S5
  line: 146
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 1 -> 2. Leon''s decision 10 of 10 November 2026: the six simulation premises (C, S1 to S5) are typed as model specification. The store has no entity type for a model specification, and an object cannot be the target of an assumes edge, so the entity keeps kind claim and status postulate (the assumes edges of simulations.halo-shapes and simulations.merger stand) and is marked in its title and at every level. Recorded as a numerical set-up.'
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
    note: Assumed by the merger and cluster-assembly runs, whose initial conditions are built from it.
---

## formal
Each halo is a Hernquist sphere matched to a Navarro-Frenk-White halo of the same mass and concentration, in equilibrium, with every species sharing the profile in proportion to its mass fraction.

\emph{Type: model specification.} This is a clause of the specification of the numerical model of the cluster simulations (Premises S1 to S5 and C), not a hypothesis of the series about nature; it is kept with the premises so that the two simulation results show it among their conditions. It is the numerical set-up of the initial conditions; nothing in the series bears on it.

## technical
A modelling premise: each halo starts as a Hernquist sphere matched to a Navarro-Frenk-White halo of the same mass and concentration, in equilibrium, and every species follows that profile in proportion to its mass fraction.

Type: model specification: the set-up of the initial conditions, on which nothing in the series bears.

## lay
Each simulated halo begins in a standard balanced shape, chosen to match the usual description of dark-matter halos. Every kind of matter starts out spread in the same way, in proportion to its share of the mass. It is part of the set-up of a computer model, not a claim of the theory about nature.

## one-liner
Model specification: each halo is an equilibrium Hernquist sphere matched to a Navarro-Frenk-White halo of equal mass and concentration, with all species sharing the profile by mass fraction.
