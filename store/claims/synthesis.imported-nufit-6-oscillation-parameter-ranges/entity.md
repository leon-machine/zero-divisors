---
id: synthesis.imported-nufit-6-oscillation-parameter-ranges
kind: claim
version: 1
title: 'Imported: the three-sigma ranges of the lepton mixing angles in the NuFIT 6.0 global fit, sin^2 theta12 in [0.275, 0.345], sin^2 theta23 in [0.430, 0.597], sin^2 theta13 in [0.02023, 0.02409] over its four data sets (Esteban et al. 2024)'
status: imported
region: synthesis
subject: neutrinos
tags: [confronted-with-data, flavour-and-mixing]
proposed_by:
  kind: ai
  session: maintainer-2026-11-01
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'I. Esteban, M. C. Gonzalez-Garcia, M. Maltoni, I. Martinez-Soler, J. P. Pinheiro and T. Schwetz, NuFit-6.0: updated global analysis of three-flavor neutrino oscillations, J. High Energy Phys. 12 (2024), 216; arXiv:2410.05380.'
  key: NuFIT2024
  locator: 'Table 1'
  doi: 10.1007/JHEP12(2024)216
extraction:
  note: >-
    Imported so that synthesis.complex-neutrino-stages-keep-the-solar-sum-rule and
    synthesis.circulant-charged-leptons-excluded-with-real-neutrino-sectors can pin the data they
    compare with. Checked on 2026-11-01 against arXiv:2410.05380v2 (abstract page and PDF): title,
    authors, DOI, and Table 1, the three-sigma ranges in all four columns (IC19 without SK
    atmospheric data, normal and inverted ordering; IC24 with SK atmospheric data, normal and
    inverted ordering): sin^2 theta12 0.275 to 0.345 in all four; sin^2 theta23 0.430 to 0.596,
    0.437 to 0.597, 0.435 to 0.585, 0.440 to 0.584; sin^2 theta13 0.02023 to 0.02376, 0.02053 to
    0.02397, 0.02030 to 0.02388, 0.02060 to 0.02409; delta_CP 96 to 422, 201 to 348, 124 to 364, 201
    to 335 degrees. The union ranges are taken here.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Leon approved the import of NuFIT 6.0 Table 1 as a routine Fact).'
---

## formal
In the standard parametrisation of the lepton mixing matrix, the NuFIT 6.0 global fit (Table 1) gives the following three-sigma ranges in its four analyses (IC19 without Super-Kamiokande atmospheric data and IC24 with them, each for normal and inverted ordering): $\sin^{2}\theta_{12} \in [0.275, 0.345]$ in all four; $\sin^{2}\theta_{23} \in [0.430, 0.596]$, $[0.437, 0.597]$, $[0.435, 0.585]$, $[0.440, 0.584]$; $\sin^{2}\theta_{13} \in [0.02023, 0.02376]$, $[0.02053, 0.02397]$, $[0.02030, 0.02388]$, $[0.02060, 0.02409]$; $\delta_{CP} \in [96^{\circ}, 422^{\circ}]$, $[201^{\circ}, 348^{\circ}]$, $[124^{\circ}, 364^{\circ}]$, $[201^{\circ}, 335^{\circ}]$. Over the union of the four, $\sin^{2}\theta_{12} \in [0.275, 0.345]$, $\sin^{2}\theta_{23} \in [0.430, 0.597]$ and $\sin^{2}\theta_{13} \in [0.02023, 0.02409]$. \emph{Provenance:} \cite{NuFIT2024} (Table 1).

## technical
The NuFIT collaboration combines all neutrino oscillation data into best-fit values and confidence ranges for the three mixing angles, the CP phase and the mass splittings, in two variants of the analysis and for both mass orderings. The three-sigma ranges of the angles quoted here, and their union over the four columns, are the ranges a texture must meet; combining one-dimensional ranges is conservative for an exclusion.

## lay
Neutrinos change type as they travel, by amounts set by three mixing angles. The NuFIT global analysis of all the experiments gives the ranges these angles can have; any theory of neutrino masses must land inside them.

## one-liner
NuFIT 6.0, three sigma, union of four analyses: $\sin^{2}\theta_{12} \in [0.275, 0.345]$, $\sin^{2}\theta_{23} \in [0.430, 0.597]$, $\sin^{2}\theta_{13} \in [0.02023, 0.02409]$.
