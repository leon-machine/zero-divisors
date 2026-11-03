---
id: dark-matter.imported-schwinger-discharge-charged-hole
kind: claim
version: 1
title: 'Imported: Schwinger discharge of a charged hole'
status: imported
region: dark-matter
subject: dark-matter
tags: [radiation-spectrum, classical-theorem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
imported_from:
- citation: G. W. Gibbons, Vacuum polarization and the spontaneous loss of charge by black holes, Commun.
    Math. Phys. 44 (1975) 245--264.
  key: Gibbons1975
- citation: W. A. Hiscock and L. D. Weems, Evolution of charged evaporating black holes, Phys. Rev. D
    41 (1990) 1142--1151.
  key: HiscockWeems1990
locators:
  paper: T14
  number: Fact 2.12
  label: fact:discharge
  line: 140
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported; levels only.
---

## formal
A charged hole whose horizon field exceeds $E_{c} = m_{e}^{2}c^{3}/e\hbar$ discharges by pair creation, faster than it evaporates, toward $Q_{c} = 4\pi\varepsilon_{0}E_{c}r_{+}^{2}$, into the lightest charged carrier (for the mirror, the mirror electron). $Q_{c}/Q_{\mathrm{ext}} \propto M$ reaches one at about $1.3 \times 10^{5}$ solar masses (at one solar mass $Q_{c} \approx 1.3 \times 10^{15}$ C, $7.5 \times 10^{-6}$ of extremal, with $E_{c} = 1.32 \times 10^{18}$ V/m), so below that mass discharge returns the Gauss-law charge and above it does not limit it. \emph{Provenance:} \cite{Gibbons1975, HiscockWeems1990}, from the record (the charged exterior is outside the Hawking paper's scope).

## technical
A charged black hole whose horizon field exceeds the Schwinger field $E_{c} = m_{e}^{2}c^{3}/e\hbar$ loses charge by pair creation faster than it evaporates, down to $Q_{c} = 4\pi\varepsilon_{0}E_{c}r_{+}^{2}$, into the lightest charged carrier (for the mirror, the mirror electron). Since $Q_{c}/Q_{\mathrm{ext}} \propto M$ reaches one at about $1.3 \times 10^{5}$ solar masses, below that mass discharge brings the charge down to the Gauss-law value and above it does not limit the charge.

## lay
A black hole with a strong enough electric charge pulls electron-positron pairs out of empty space and sheds charge quickly. For holes lighter than about a hundred thousand Suns this caps the charge they can keep; for heavier ones the cap is above the largest charge possible and does nothing. In the mirror world the same happens with mirror electrons.

## one-liner
A charged hole discharges by pair creation toward $Q_{c} = 4\pi\varepsilon_{0}E_{c}r_{+}^{2}$, which limits its charge below about $1.3 \times 10^{5}$ solar masses and not above.
