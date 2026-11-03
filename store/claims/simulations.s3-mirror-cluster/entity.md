---
id: simulations.s3-mirror-cluster
kind: claim
version: 1
title: 'S3: the mirror in a cluster'
status: postulate
region: simulations
subject: dark-matter
tags:
- halos-and-clusters
- mirror-sector
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
  number: Premise 2.9
  label: prem:S3
  line: 138
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
    note: Assumed by the merger and cluster-assembly runs (the cluster mirror model); the Galaxy model
      of Obs 9.1 uses its own semi-analytic model, so mirror-galaxy does not assume it.
---

## formal
Mirror matter in a cluster is a fully ionised helium plasma, $\gamma = 5/3$, cooling by bremsstrahlung alone (below about $10^{6}$ K He$^{+}$ line cooling would in reality dominate, so settling would come sooner; Cost K3). Gas that cools below about $7 \times 10^{4}$ K becomes collisionless (the settled phase). There is no mirror star formation and no feedback.

## technical
A modelling premise: mirror matter in a cluster is a fully ionised helium plasma with $\gamma = 5/3$, cooling by bremsstrahlung alone. Gas that cools below about $7 \times 10^{4}$ K becomes collisionless (the settled phase), and there is no mirror star formation and no feedback. Below about $10^{6}$ K, He$^{+}$ line cooling would in reality dominate and bring settling sooner, a cost the model records.

## lay
In the cluster simulations the mirror matter is a hot, fully ionised helium gas that loses heat only through the simplest radiation process. Gas that cools enough is treated as settled and no longer collides. The model has no mirror stars, so nothing heats the gas back up.

## one-liner
Mirror matter in clusters is modelled as a $\gamma = 5/3$ helium plasma cooling by bremsstrahlung, becoming collisionless below about $7 \times 10^{4}$ K, with no star formation and no feedback.
