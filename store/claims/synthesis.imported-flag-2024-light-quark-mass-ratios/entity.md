---
id: synthesis.imported-flag-2024-light-quark-mass-ratios
kind: claim
version: 1
title: 'Imported: the FLAG 2024 lattice averages of the light-quark mass ratios, m_s/m_ud = 27.227(81), m_u/m_d = 0.465(24), m_c/m_s = 11.766(30) for N_f = 2+1+1 (FLAG Review 2024)'
status: imported
region: synthesis
subject: generations
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
- citation: 'Y. Aoki et al. (Flavour Lattice Averaging Group), FLAG Review 2024, arXiv:2411.04268.'
  key: FLAG2024
  locator: 'Table 1'
  doi: 10.1103/nfzp-p5dn
extraction:
  note: >-
    Imported so that synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase
    can pin the lattice ratios its windows cover. Checked on 2026-11-01 against arXiv:2411.04268v3
    (abstract page and PDF): title, DOI, and Table 1 (summary of the main results, quark masses in
    MS-bar at 2 GeV or as indicated): N_f = 2+1+1: m_ud = 3.427(51) MeV, m_s = 93.46(58) MeV,
    m_s/m_ud = 27.227(81), m_u/m_d = 0.465(24), m_c/m_s = 11.766(30); N_f = 2+1: 3.387(39) MeV,
    92.4(1.0) MeV, 27.42(12), 0.485(19), 11.82(16). The derived ratios m_s/m_d and m_c/m_u are
    arithmetic on the central values (floating point). The journal of the DOI is not stated on the
    page and is not given here.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Leon approved the import of the FLAG 2024 quark-mass ratios as a routine Fact).'
---

## formal
The FLAG 2024 averages of lattice QCD results (Table 1; quark masses in the $\overline{\mathrm{MS}}$ scheme at $2$ GeV) are, for $N_{f} = 2+1+1$: $m_{ud} = 3.427(51)$ MeV, $m_{s} = 93.46(58)$ MeV, $m_{s}/m_{ud} = 27.227(81)$, $m_{u}/m_{d} = 0.465(24)$, $m_{c}/m_{s} = 11.766(30)$; and for $N_{f} = 2+1$ (three dynamical flavours, a different lattice average, hence a strange mass below the stored quantity.strange-quark-mass): $m_{ud} = 3.387(39)$ MeV, a strange mass of $92.4(1.0)$ MeV, $m_{s}/m_{ud} = 27.42(12)$, $m_{u}/m_{d} = 0.485(19)$, $m_{c}/m_{s} = 11.82(16)$, with $m_{ud} = (m_{u} + m_{d})/2$. The ratios are scale independent in QCD. At the $N_{f} = 2+1+1$ central values $m_{s}/m_{d} = \tfrac12(m_{s}/m_{ud})(1 + m_{u}/m_{d}) \approx 19.94$ and $m_{c}/m_{u} \approx 505$; at the $N_{f} = 2+1$ central values about $20.36$ and $496$. \emph{Provenance:} \cite{FLAG2024} (Table 1).

## technical
The Flavour Lattice Averaging Group reviews lattice QCD computations and quotes world averages. Its 2024 averages of the light-quark mass ratios, with and without a dynamical charm quark, fix the ratios of the down to the strange and of the up to the charm mass to a few percent, more precisely than the individual running masses.

## lay
The masses of the light quarks cannot be weighed directly; they are computed by large simulations of the strong force on a lattice. The FLAG review collects and averages these computations; its ratios of quark masses are the most precise available.

## one-liner
FLAG 2024 ($N_{f} = 2+1+1$): $m_{s}/m_{ud} = 27.227(81)$, $m_{u}/m_{d} = 0.465(24)$, $m_{c}/m_{s} = 11.766(30)$, so $m_{s}/m_{d} \approx 19.94$ and $m_{c}/m_{u} \approx 505$.
