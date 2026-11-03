---
id: simulations.s1-one-species-per-tower
kind: claim
version: 2
title: 'S1: one species per tower'
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
  number: Premise 2.7
  label: prem:S1
  line: 130
extraction:
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
The matter of each populated tower is one species. Within its tower it is either collisionless or a fluid; across towers species interact only through gravity (Fact \claimref{dark-matter.superselected-hence-dark-exactly-stable}). Our matter is two species: galaxies, collisionless, and our gas.

## technical
A modelling premise for the simulations: the matter of each populated tower is a single species, either collisionless or a fluid within its tower, and species in different towers interact only through gravity, as superselection of the tower charge implies. Our own matter is modelled as two species, collisionless galaxies and our gas.

## lay
For the simulations, each hidden sector's matter is treated as one kind of stuff, which either passes through itself or flows like a fluid. Different sectors feel each other only through gravity. Ordinary matter is split into galaxies, which pass through each other, and gas, which does not.

## one-liner
Each populated tower's matter is one species, collisionless or fluid, interacting with other towers only through gravity; our matter is collisionless galaxies plus gas.
