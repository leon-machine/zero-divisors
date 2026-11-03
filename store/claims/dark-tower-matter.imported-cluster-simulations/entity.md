---
id: dark-tower-matter.imported-cluster-simulations
kind: claim
version: 1
title: 'Imported: the cluster merger simulations'
status: imported
region: dark-tower-matter
subject: dark-matter
tags:
- halos-and-clusters
- confronted-with-data
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T14c, the series'' standard disclaimer'
review: typed
imported_from:
- citation: 'L. Butler, Simulating the Dark Towers: Methods, Assumptions and Tests of the Unit-Ball Composition,
    Transport Papers T14b (2026)'
  key: ButlerT14b
  locator: Obs. 7.1, Table 3
  series: true
locators:
  paper: T14c
  number: Fact 2.5
  label: fact:sims
  line: 214
extraction:
  env: fact
  outside_pilot_cites:
  - ButlerT14b
  flags:
  - imported fact with no citation
  typing:
    by: ai-typing-pass
    note: 'The extractor found no citation; the source cites the simulations companion, Obs. 7.1 and Table
      3, so that is the provenance, with lineage to the merger observation (simulations.merger). Kept
      imported rather than restated as proved, because the source result is an observation (conjectured
      in the store), which a proved restatement would exceed. Levels pass: levels written from scratch,
      keeping every condition and level qualifier of the formal statement.'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: Series import of the T14b merger runs, linked by lineage to the merger observation and from
      the towers-built observation; no proof uses it and no definition bears on it.
lineage:
  derived_from:
  - simulations.merger
---

## formal
In the idealised Bullet-like merger runs of T14b \cite[Obs.~7.1, Table~3]{ButlerT14b}: (i) with only the mirror colliding ($18.6$ percent of the dark matter, as gas) the subcluster keeps a separate lensing peak on its galaxies and a mass-to-light change of $0.82$ against the observed $0.84 \pm 0.07$; (ii) with the mirror gas and one three-dimensional tower's share of colliding fluid ($43.5$ percent colliding) the subcluster dissolves, and with more it dissolves too; (iii) with the mirror collisionless and $24.9$ or $31.6$ percent of colliding fluid, the subcluster keeps a weaker peak but only $0.55$ or $0.44$ of its central mass: the colliding fluid alone costs about half of it. In (i) the subcluster's own mass is $0.57$ of the cold-dark-matter run's, but mass and light leave together and the mass-to-light change, the quantity the observational bound is inferred from, is consistent. No run lies between $18.6$ and $24.9$ percent colliding. The colliding components there are fluids.

## technical
In the idealised Bullet-like merger runs of the simulations companion: with only the mirror colliding ($18.6$ percent of the dark matter, as gas) the subcluster keeps a separate lensing peak on its galaxies and a mass-to-light change of $0.82$ against the observed $0.84 \pm 0.07$, although its own mass is $0.57$ of the cold-dark-matter run's; with the mirror and one three-dimensional tower's share colliding ($43.5$ percent), or more, the subcluster dissolves; with the mirror collisionless and $24.9$ or $31.6$ percent of colliding fluid, it keeps a weaker peak but only $0.55$ or $0.44$ of its central mass. No run lies between $18.6$ and $24.9$ percent colliding, and the colliding components are fluids.

## lay
Computer simulations of colliding galaxy clusters, from the series' simulations note, test how much of the dark matter can collide with itself. They pass the observational test only when the mirror tower alone collides, and lose much of the smaller cluster's mass as soon as another colliding component is added. The colliding matter in these runs is modelled as a fluid.

## one-liner
Imported from the simulation runs: a merger passes only when the mirror alone ($18.6$ percent) collides, and at $24.9$ percent colliding or more the subcluster loses about half its central mass or dissolves.
