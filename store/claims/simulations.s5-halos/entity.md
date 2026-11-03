---
id: simulations.s5-halos
kind: claim
version: 1
title: 'S5: halos'
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
  number: Premise 2.11
  label: prem:S5
  line: 146
extraction:
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

## technical
A modelling premise: each halo starts as a Hernquist sphere matched to a Navarro-Frenk-White halo of the same mass and concentration, in equilibrium, and every species follows that profile in proportion to its mass fraction.

## lay
Each simulated halo begins in a standard balanced shape, chosen to match the usual description of dark-matter halos. Every kind of matter starts out spread in the same way, in proportion to its share of the mass.

## one-liner
Each halo is an equilibrium Hernquist sphere matched to a Navarro-Frenk-White halo of equal mass and concentration, with all species sharing the profile by mass fraction.
