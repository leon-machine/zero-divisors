---
id: synthesis.imported-mssm-charged-higgs-tree-sum-rule
kind: claim
version: 1
title: 'Imported: in the minimal supersymmetric Standard Model, at tree level, $m_{H^{\pm}}^{2} = m_{A}^{2} + M_{W}^{2}$'
status: imported
region: synthesis
subject: standard-model
tags: [symmetry-breaking, mass-generation, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-31
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'J. F. Gunion and H. E. Haber, Higgs bosons in supersymmetric models (I), Nucl. Phys. B 272 (1986), 1--76.'
  key: GunionHaber1986
- citation: 'A. Djouadi, The anatomy of electroweak symmetry breaking. Tome II: The Higgs bosons in the minimal supersymmetric model, Phys. Rept. 459 (2008), 1--241, Section 1.2.2; arXiv:hep-ph/0503173.'
  key: Djouadi2008
- citation: 'B. Dudley and C. Kolda, Constraining the charged Higgs mass in the MSSM: a low-energy approach, arXiv:0901.3337, equation (1).'
  key: DudleyKolda2009
extraction:
  note: >-
    Imported because synthesis.rung-field-charged-scalar-sum-rule cites the minimal supersymmetric tree
    sum rule as the model for its own sum rule. That result does not rest on it: its sum rule is derived
    from the stored D-term action, in which no second neutral field exists and m_h itself enters, so no
    uses edge is drawn. The relation was checked on 2026-10-31 against Dudley and Kolda, arXiv:0901.3337,
    equation (1) ("at tree level, the charged Higgs mass depends on the CP-odd Higgs, A, through the
    relationship m_{H+-}^2 = m_A^2 + m_W^2"); the Gunion and Haber and Djouadi citations, and the
    Djouadi section number, are from memory and were not checked against the sources.
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Created by the maintainer pass of 2026-10-31 (literature cited from memory by an accepted result; Leon''s list of imports).'
---

## formal
In the minimal supersymmetric extension of the Standard Model, whose Higgs sector is two complex doublets with the quartic couplings fixed by the gauge couplings through the D-terms, the tree-level masses of the charged Higgs pair $H^{\pm}$ and of the CP-odd neutral scalar $A$ satisfy
\[
m_{H^{\pm}}^{2} \;=\; m_{A}^{2} + M_{W}^{2},
\]
with $M_{W}$ the tree-level $W$ mass; in particular $m_{H^{\pm}} > M_{W}$ at tree level. Loop corrections modify the relation. \emph{Provenance:} \cite{GunionHaber1986}, \cite{Djouadi2008} (Section 1.2.2), \cite{DudleyKolda2009} (equation (1)).

## technical
In the minimal supersymmetric Standard Model the Higgs potential's quartic terms come from the gauge interactions, so the Higgs masses at tree level are fixed by two parameters, usually the CP-odd mass $m_{A}$ and the ratio of the two vacuum values. The charged pair's mass is then tied to the CP-odd one by $m_{H^{\pm}}^{2} = m_{A}^{2} + M_{W}^{2}$, which places the charged pair above the $W$ mass at tree level. Radiative corrections shift the relation slightly.

## lay
In the simplest supersymmetric version of the Standard Model there are five Higgs particles, and their masses are not independent. At the simplest level of approximation the mass of the electrically charged pair is fixed by the mass of one of the neutral ones and the mass of the W boson.

## one-liner
In the MSSM at tree level, $m_{H^{\pm}}^{2} = m_{A}^{2} + M_{W}^{2}$ (Gunion and Haber; Djouadi).
