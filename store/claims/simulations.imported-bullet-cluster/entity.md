---
id: simulations.imported-bullet-cluster
kind: claim
version: 1
title: 'Imported: the Bullet Cluster'
status: imported
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
imported_from:
- citation: D. Clowe, M. Bradac, A. H. Gonzalez, M. Markevitch, S. W. Randall, C. Jones and D. Zaritsky,
    A direct empirical proof of the existence of dark matter, Astrophys. J. 648 (2006) L109.
  key: Clowe2006
- citation: S. W. Randall, M. Markevitch, D. Clowe, A. H. Gonzalez and M. Bradac, Constraints on the self-interaction
    cross section of dark matter from numerical simulations of the merging galaxy cluster 1E 0657-56,
    Astrophys. J. 679 (2008) 1173.
  key: Randall2008
- citation: D. Harvey, R. Massey, T. Kitching, A. Taylor and E. Tittley, The nongravitational interactions
    of dark matter in colliding galaxy clusters, Science 347 (2015) 1462.
  key: Harvey2015
- citation: 'D. Wittman, N. Golovich and W. A. Dawson, The mismeasure of mergers: revised limits on self-interacting
    dark matter in merging galaxy clusters, Astrophys. J. 869 (2018) 104.'
  key: Wittman2018
locators:
  paper: T14b
  number: Fact 2.4
  label: fact:bullet
  line: 114
extraction:
  typing:
    by: ai-typing-pass
    note: Imported observational fact; levels only, no edges to review.
  env: fact
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: Observational import used only as comparison data (lineage from the merger); no proof uses it
      and no definition bears on it.
---

## formal
In 1E0657-558 the two galaxy concentrations are $0.72$ Mpc apart on the sky; the lensing peaks lie $9.6''$ ($42$ kpc, subcluster) and $11.8''$ ($52$ kpc, main cluster) from the brightest cluster galaxies, within $1\sigma$ of the galaxy luminosity centroids, and the centres of total mass are offset from the plasma at $8\sigma$ \cite{Clowe2006}. The mass-to-light ratios give $(M/L)_{\mathrm{sub}}/(M/L)_{\mathrm{main}} = 0.84 \pm 0.07$, from which the subcluster has lost no more than about $23$ percent of its mass (a bound on mass loss inferred from the ratio, not on the mass inside a fixed aperture). The self-interaction cross-section per mass is below $1.25\ \cmg$ ($68$ percent) from the absence of an offset between mass and galaxies, whose centroids are known to about $5''$ ($22$ kpc), and below $0.7\ \cmg$ from the mass-to-light ratios \cite{Randall2008}. From $72$ cluster collisions $\sigma/m < 0.47\ \cmg$ at $95$ percent \cite{Harvey2015}, relaxed to about $2\ \cmg$ when that sample's offsets are corrected \cite{Wittman2018}.

## technical
In the merging cluster 1E0657-558 the two galaxy concentrations are $0.72$ Mpc apart, the lensing mass peaks lie within $1\sigma$ of the galaxy luminosity centroids ($42$ and $52$ kpc from the brightest cluster galaxies), and the centres of total mass are offset from the hot plasma at $8\sigma$. The subcluster's mass-to-light ratio relative to the main cluster's, $0.84 \pm 0.07$, implies it has lost no more than about $23$ percent of its mass; this bounds lost mass, not the mass inside a fixed aperture.

The resulting limits on the self-interaction cross-section per mass are $\sigma/m < 1.25\ \cmg$ ($68$ percent) from the absence of a mass-galaxy offset and $\sigma/m < 0.7\ \cmg$ from the mass-to-light ratios. A sample of $72$ cluster collisions gives $\sigma/m < 0.47\ \cmg$ at $95$ percent, relaxed to about $2\ \cmg$ once that sample's offsets are corrected.

## lay
The Bullet Cluster is a pair of galaxy clusters that have passed through each other. Gravitational lensing shows that most of the mass travelled with the galaxies while the hot gas lagged behind. That would not happen if dark matter collided strongly with itself, so the observation caps how much dark-matter particles can scatter off one another.

## one-liner
The Bullet Cluster and other cluster collisions bound dark-matter self-interaction at between about $0.47$ and $2\ \cmg$ depending on the method, and bound the subcluster's mass loss at about $23$ percent.
