---
id: simulations.s1-one-species-per-tower
kind: claim
version: 3
title: 'S1: one species per tower (model specification)'
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
  role: 'typed as model specification; the second clause cited as a stored theorem'
  version: 3
  source: maintainer pass of 2026-11-10
review: typed
locators:
  paper: T14b
  number: Premise 2.7
  label: prem:S1
  line: 130
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 2 -> 3. Leon''s decision 10 of 10 November 2026: the six simulation premises (C, S1 to S5) are typed as model specification. The store has no entity type for a model specification, and an object cannot be the target of an assumes edge, so the entity keeps kind claim and status postulate (the assumes edges of simulations.halo-shapes and simulations.merger stand) and is marked in its title and at every level. S1''s second clause is cited as the stored theorem dark-matter.superselected-hence-dark-exactly-stable (it was called a Fact in the text; it is a proved claim) and no longer reads as a premise; the first clause is recorded as a simplification against the stored five-dimensional content.'
  typing:
    by: ai-typing-pass
    note: Postulate; no edges. The superselection fact in context_refs is the stated justification, not
      a premise of a postulate.
  env: premise
  context_refs:
  - dark-matter.superselected-hence-dark-exactly-stable
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises:
    - dark-matter.superselected-hence-dark-exactly-stable (motivated_by)
    added_dependants:
    - simulations.merger
    - simulations.halo-shapes
    added_about: []
    verdict: connected
    note: Assumed by the merger and cluster-assembly runs; the superselection fact it cites as justification
      is recorded as lineage, not a premise of a premise.
lineage:
  motivated_by:
  - dark-matter.superselected-hence-dark-exactly-stable
---

## formal
The matter of each populated tower is one species. Within its tower it is either collisionless or a fluid; across towers species interact only through gravity (Theorem \claimref{dark-matter.superselected-hence-dark-exactly-stable}). Our matter is two species: galaxies, collisionless, and our gas.

\emph{Type: model specification.} This is a clause of the specification of the numerical model of the cluster simulations (Premises S1 to S5 and C), not a hypothesis of the series about nature; it is kept with the premises so that the two simulation results show it among their conditions. Its second clause, that species of different towers interact only through gravity, is not a premise: it is the stored Theorem \claimref{dark-matter.superselected-hence-dark-exactly-stable}, under that theorem's own conditions. Its first clause is a simplification of the model: for the five-dimensional towers the stored content under (S) is four Dirac species (Proposition \claimref{dark-tower-matter.five-dimensional-content}), treated here as one fluid component.

## technical
A modelling premise for the simulations: the matter of each populated tower is a single species, either collisionless or a fluid within its tower, and species in different towers interact only through gravity, as superselection of the tower charge implies. Our own matter is modelled as two species, collisionless galaxies and our gas.

Type: model specification. The second clause (towers interact only through gravity) is a stored theorem, under its own conditions, and not a premise; the first (one species per tower) is a simplification of the model, the five-dimensional towers' stored content under (S) being four Dirac species.

## lay
For the simulations, each hidden sector's matter is treated as one kind of stuff, which either passes through itself or flows like a fluid. Different sectors feel each other only through gravity. Ordinary matter is split into galaxies, which pass through each other, and gas, which does not. It is part of the set-up of a computer model, not a claim of the theory about nature. That different sectors feel each other only through gravity is a result proved elsewhere in the series, not an assumption made here.

## one-liner
Model specification: each populated tower's matter is one species, collisionless or fluid, interacting with other towers only through gravity; our matter is collisionless galaxies plus gas.
