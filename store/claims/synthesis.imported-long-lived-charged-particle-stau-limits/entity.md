---
id: synthesis.imported-long-lived-charged-particle-stau-limits
kind: claim
version: 1
title: 'Imported: searches for heavy long-lived charged particles exclude directly pair-produced long-lived staus below $339$ GeV (CMS, $7$ and $8$ TeV) and below $430$ GeV (ATLAS, $13$ TeV, $36.1$ fb$^{-1}$)'
status: imported
region: synthesis
subject: standard-model
tags: [confronted-with-data]
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
- citation: 'CMS Collaboration, Searches for long-lived charged particles in $pp$ collisions at $\sqrt{s} = 7$ and $8$ TeV, J. High Energy Phys. 07 (2013), 122; arXiv:1305.0491.'
  key: CMS2013LongLivedCharged
  doi: 10.1007/JHEP07(2013)122
- citation: 'ATLAS Collaboration, Search for heavy charged long-lived particles in the ATLAS detector in $36.1$ fb$^{-1}$ of proton-proton collision data at $\sqrt{s} = 13$ TeV, Phys. Rev. D 99 (2019), 092007; arXiv:1902.01636.'
  key: ATLAS2019LongLivedCharged
  doi: 10.1103/PhysRevD.99.092007
extraction:
  note: >-
    Imported so that the charged-pair result can pin the stable-charged-particle limits it reinterprets.
    Checked on 2026-11-01: for CMS, against the arXiv abstract page of arXiv:1305.0491 (title, data sets
    of 5.0 fb^-1 at 7 TeV and 18.8 fb^-1 at 8 TeV, the long-lived staus among the models constrained,
    the DOI 10.1007/JHEP07(2013)122) and against the paper's Section 7, where the tracker plus
    time-of-flight analysis excludes stau masses below 500 GeV for direct plus indirect production and
    below 339 GeV for direct production only, and its Table 7 (direct-produced staus), whose observed
    ratio of the cross-section limit to the predicted cross-section is 0.16 at the lowest tabulated mass,
    126 GeV; for ATLAS, against the arXiv abstract page of arXiv:1902.01636 (title, 36.1 fb^-1 at 13 TeV,
    ionisation and time-of-flight identification, lower mass limit 430 GeV for directly pair-produced
    staus, DOI 10.1103/PhysRevD.99.092007). The lowest stau mass of the ATLAS signal grid is not checked
    and is not stated here. Reading a stable charged scalar of other origin through these stau limits is a
    reinterpretation made by the results that cite this Fact, not by the searches.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (collider limits as Facts, by Leon''s list of imports).'
---

## formal
Searches for heavy charged particles that cross the detectors before decaying, identified by anomalous ionisation energy loss and long time of flight, set $95$ per cent confidence lower mass limits on long-lived scalar tau leptons (staus):
\begin{enumerate}
\item[(i)] CMS, with $5.0$ fb$^{-1}$ at $\sqrt{s} = 7$ TeV and $18.8$ fb$^{-1}$ at $\sqrt{s} = 8$ TeV, tracker plus time-of-flight analysis: staus produced directly in pairs are excluded below $339$ GeV, and with direct and indirect production in the gauge-mediated benchmark below $500$ GeV; for directly produced staus the observed cross-section limit is $0.16$ of the predicted cross-section at the lowest tabulated mass, $126$ GeV;
\item[(ii)] ATLAS, with $36.1$ fb$^{-1}$ at $\sqrt{s} = 13$ TeV: directly pair-produced staus are excluded below $430$ GeV.
\end{enumerate}
\emph{Provenance:} \cite{CMS2013LongLivedCharged} (Section 7 and Table 7), \cite{ATLAS2019LongLivedCharged} (abstract).

## technical
An electrically charged particle that lives long enough to cross a collider detector leaves a slow, heavily ionising track that the standard searches for heavy stable charged particles pick out. CMS, in the data of the LHC's first run, excluded long-lived staus produced directly in pairs through the electroweak interaction up to $339$ GeV, and up to $500$ GeV when production through heavier states is included; ATLAS, in part of the second run's data, excluded directly pair-produced long-lived staus up to $430$ GeV. A stable charged scalar of comparable electroweak couplings is constrained by the same searches, through a reinterpretation of these limits.

## lay
If a new electrically charged particle were stable, or lived long enough to cross a detector, it would leave an unusual slow and heavily ionising track. The CMS and ATLAS experiments at CERN looked for such tracks and found none, ruling out long-lived partners of the tau lepton lighter than several hundred GeV.

## one-liner
Long-lived staus produced directly in pairs are excluded below $339$ GeV by CMS ($7$, $8$ TeV) and below $430$ GeV by ATLAS ($13$ TeV, $36.1$ fb$^{-1}$) (arXiv:1305.0491, arXiv:1902.01636).
