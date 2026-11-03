---
id: synthesis.imported-atlas-charged-higgs-top-decay-tau-nu-limits
kind: claim
version: 1
title: 'Imported: ATLAS limits on charged Higgs bosons from top decays and $H^{\pm} \to \tau\nu$ at $13$ TeV with $140$ fb$^{-1}$; for $80 \le m_{H^{\pm}} \le 160$ GeV, $\mathcal{B}(t \to bH^{+})\,\mathcal{B}(H^{+} \to \tau\nu)$ below values between $0.27\%$ and $0.02\%$'
status: imported
region: synthesis
subject: standard-model
tags: [confronted-with-data, symmetry-breaking]
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
- citation: 'ATLAS Collaboration, Search for charged Higgs bosons produced in top-quark decays or in association with top quarks and decaying via $H^{\pm} \to \tau^{\pm}\nu_{\tau}$ in $13$ TeV $pp$ collisions with the ATLAS detector, Phys. Rev. D 111 (2025), 072006; arXiv:2412.17584.'
  key: ATLAS2025ChargedHiggsTauNu
  doi: 10.1103/PhysRevD.111.072006
extraction:
  note: >-
    Imported so that the charged-pair result can pin the top-decay search it confronts instead of
    citing it from the abstract in its proof. Checked on 2026-11-01 against the arXiv abstract page of
    arXiv:2412.17584: the title, the ATLAS authorship, the data set (140 fb^-1 of pp collisions at
    13 TeV), the mass range 80 to 3000 GeV, the absence of a significant excess, the limits on the
    production cross-section times branching fraction (4.5 pb to 0.4 fb) and, for 80 to 160 GeV with
    the Standard Model ttbar cross-section assumed, the upper limits between 0.27 per cent and 0.02 per
    cent on B(t -> bH+) B(H+ -> tau nu); the journal reference and DOI are those of the arXiv record. The
    abstract gives the end values of the range without saying at which masses they are reached, so no
    mass dependence inside 80 to 160 GeV is stated here.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (collider limits as Facts, by Leon''s list of imports).'
---

## formal
The ATLAS search for charged Higgs bosons $H^{\pm}$ produced in top-quark decays $t \to bH^{+}$ or in association with a top quark, and decaying as $H^{\pm} \to \tau^{\pm}\nu_{\tau}$, with $140$ fb$^{-1}$ of proton-proton collisions at $\sqrt{s} = 13$ TeV, covering $80 \le m_{H^{\pm}} \le 3000$ GeV, finds no significant excess over the Standard Model expectation and sets $95$ per cent confidence upper limits on the production cross-section times branching fraction from $4.5$ pb to $0.4$ fb over that range. In the range $80 \le m_{H^{\pm}} \le 160$ GeV, with the Standard Model $t\bar{t}$ cross-section assumed, these are upper limits on $\mathcal{B}(t \to bH^{+}) \times \mathcal{B}(H^{+} \to \tau\nu)$ with values between $0.27\%$ and $0.02\%$. \emph{Provenance:} \cite{ATLAS2025ChargedHiggsTauNu} (abstract).

## technical
ATLAS searched the full data set of the LHC's second run for an electrically charged scalar that is lighter than the top quark and is produced in its decays, or heavier and produced alongside it, decaying to a tau lepton and a neutrino. Nothing beyond the Standard Model was seen. For charged-scalar masses between $80$ and $160$ GeV the result bounds the fraction of top quarks that decay to a bottom quark and the charged scalar, times the scalar's branching to a tau and a neutrino, below values between a quarter of a per cent and two hundredths of a per cent across that mass range.

## lay
If a heavy electrically charged cousin of the Higgs particle existed and were lighter than the top quark, top quarks would sometimes decay into it. The ATLAS experiment at CERN looked for this in its full 2015 to 2018 data and found nothing: at most a few top quarks in a thousand, and in part of the mass range a few in ten thousand, can decay that way when the charged particle then decays to a tau lepton.

## one-liner
ATLAS, $13$ TeV, $140$ fb$^{-1}$: no charged Higgs in $t \to bH^{+}$, $H^{+} \to \tau\nu$; for $80$ to $160$ GeV, $\mathcal{B}(t \to bH^{+})\mathcal{B}(H^{+} \to \tau\nu)$ is bounded by values between $0.27\%$ and $0.02\%$ (arXiv:2412.17584).
