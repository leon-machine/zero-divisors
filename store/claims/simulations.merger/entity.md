---
id: simulations.merger
kind: claim
version: 2
title: The merger
status: conjectured
region: simulations
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
  source: authorship disclosure of T14b, deposited version
review: typed
lineage:
  motivated_by:
  - simulations.imported-bullet-cluster
  - simulations.confinement-scale-does-not-matter
locators:
  paper: T14b
  number: Obs 7.1
  label: obs:merger
  line: 445
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'No version change (note only). Leon''s decision 10 of 10 November 2026: the six premises S1 to S5 and C assumed here are model specification, and S2 and C are the premises of the two exclusive readings (W) and (C): this result lists both because it reports both readings, and does not hold them together. The pins to the six premises are left for the pin review (each is raised by one).'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: simulations.imported-mirror repinned 5 -> 6 after reviewing its G1 restatement (the cold mirror is an exception to P2 at its version-1 reach, P2 as scoped leaves xi free, and the cold mirror then needs a non-equilibrium descent; the simulated content is unchanged); the use here holds as cited.'
  typing:
    by: ai-typing-pass
    note: 'Kept conjectured: a simulation output the paper labels observation level, with no proof text
      to copy; motivated by the Bullet Cluster observation it is tested against and by the corollary that
      makes the sheet matter a fluid. Levels pass: the lay level and one-liner now keep the observation-level
      status and the single-realisation caveat.'
  env: observation
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises:
    - simulations.s1-one-species-per-tower
    - simulations.s2-sheet-fluid
    - simulations.s3-mirror-cluster
    - simulations.s4-our-matter
    - simulations.s5-halos
    - simulations.c-odd-towers-collisionless
    - simulations.imported-unit-ball-rule-family
    - simulations.imported-mirror
    added_dependants: []
    added_about: []
    verdict: connected
    note: 'Simulation output: given a premise-only derivation assuming S1 to S5 and C (C for reading (C))
      and using the imported composition and mirror; no proof text, since a conjecture carries none.'
derivations:
- name: simulation
  uses:
  - simulations.imported-unit-ball-rule-family@4
  - simulations.imported-mirror@8
  assumes:
  - simulations.s1-one-species-per-tower@3
  - simulations.s2-sheet-fluid@3
  - simulations.s3-mirror-cluster@4
  - simulations.s4-our-matter@2
  - simulations.s5-halos@2
  - simulations.c-odd-towers-collisionless@3
  note: 'Simulation output at observation level: the runs are set up under Premises S1 to S5, and reading
    (C) under Premise C, with the composition of the imported unit-ball rule and the mirror; no proof
    text, since the result is computed, not proved.'
---

## formal
In reading (W) the subcluster's sheet fluid and mirror gas are held back with its gas, $71$ percent of its mass ($56$ percent in the mixed count). Its potential collapses, its galaxies spread, and by the end of the runs it has not separated beyond $500$ to $630$ kpc. With random normals, or with the normals along the line of sight so that the merger axis lies in the sheets, it has no separate lensing peak (contrast $0.81$ to $0.95$). With every normal along this merger's axis (\texttt{rule\_par}) the fluid slides through along the axis; the subcluster then has a lensing peak (contrast $3.24$, $15$ kpc from its galaxies) but keeps half its mass. The mixed count fails in the same way. With the mirror collisionless from the start, so that only the sheet fluid collides, the subcluster keeps a weaker peak (contrast $2.69$ in the mixed count, $3.78$ with one three-dimensional tower colliding) and $0.44$ to $0.55$ of CDM's own mass: with a quarter to a third of the dark matter as sheet fluid, the sheet fluid alone costs about half the subcluster's central mass.

In reading (C) the subcluster reaches the observed separation with its mass peak on its galaxies and its gas $355$ kpc behind. Its own mass inside $150$ kpc of its galaxies is $0.57$ of CDM's, a deficit larger than the $23$ percent bound, because its halo puffs more than it strips. Its galaxies spread with it: the galaxy mass within $150$ kpc of the galaxy peak is $0.83$ of its start, where CDM's is compressed to $1.31$. Mass and light leave the aperture together, so the ratio inside it is kept while the mass inside it falls. Per unit of its collisionless content, the subcluster's collisionless matter inside the aperture is $0.683$ as concentrated as CDM's, and $0.683 \times 0.814$ (the collisionless share of the dark matter in reading (C), $1 - 0.186$) gives $0.556$, its collisionless matter against CDM's dark matter in the aperture; with stars and settled mirror matter the own mass is $0.57$. The mass-to-light ratio, from which the bound is derived, is therefore the test: its change is $0.82$ (the ratio itself $0.89$) against the observed $0.84 \pm 0.07$; CDM's is $0.87$ (ratio $1.00$). With a sampling error of $15$ to $21$ percent this measure does not separate reading (C) from CDM; the lensing peak and the gas offset separate both from reading (W). Its contrast, $4.7$ against CDM's $7.5$, is lower, and it has lost its mirror gas and part of its outer halo (Figure \ref{fig:retention}). Each composition is one realisation of one geometry. Computed; observation level.

## technical
In simulations of a Bullet-like merger, reading (W), with the sheet fluid and mirror gas colliding, holds back $71$ percent of the subcluster's mass with its gas ($56$ percent in the mixed count): its potential collapses, it separates no further than $500$ to $630$ kpc, and with random or line-of-sight normals it has no separate lensing peak. With every sheet normal along the merger axis the fluid slides through and a peak survives, but half the mass is lost; with only the sheet fluid colliding the subcluster keeps a weaker peak and $0.44$ to $0.55$ of CDM's mass.

In reading (C) the subcluster reaches the observed separation with its mass peak on its galaxies and its gas $355$ kpc behind. Its own mass in a $150$ kpc aperture is $0.57$ of CDM's, but its galaxies spread with it, so its mass-to-light change of $0.82$ sits near the observed $0.84 \pm 0.07$ and, with a sampling error of $15$ to $21$ percent, does not separate it from CDM's $0.87$; the lensing peak and gas offset separate both from reading (W). Each composition is one realisation of one geometry; observation level.

## lay
Simulated collisions of two galaxy clusters were run with the proposed dark-matter mixture. If the sheet-bound dark matter flows as a fluid, the smaller cluster's dark matter is held back with its gas, and the result does not resemble the observed Bullet Cluster. If that matter does not collide, the simulation reaches the observed separation with the mass on the galaxies, and the measured mass-to-light change cannot tell it apart from standard dark matter. Each run is one realisation of one geometry, and the result is recorded at observation level.

## one-liner
At observation level, in single realisations of a simulated Bullet-like merger, reading (W) loses the subcluster's separate lensing peak, while reading (C) reaches the observed separation and a mass-to-light change that cannot be separated from CDM's within sampling error.
