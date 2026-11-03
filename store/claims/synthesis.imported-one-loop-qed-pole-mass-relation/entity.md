---
id: synthesis.imported-one-loop-qed-pole-mass-relation
kind: claim
version: 1
title: 'Imported: at one loop in QED the pole mass of a charged lepton is m_pole = [1 + (alpha/pi)(1 + (3/4) ln(mu^2/mbar^2))] mbar(mu), and Koide''s relation written in running masses is shifted by about 0.1 percent (Sumino 2009)'
status: imported
region: synthesis
subject: generations
tags: [running-and-unification, flavour-and-mixing]
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
- citation: 'Y. Sumino, Family gauge symmetry as an origin of Koide''s mass formula and charged lepton spectrum, arXiv:0903.3640 (2009), report TU-842.'
  key: Sumino2009b
  locator: 'eq. (6)'
  url: https://arxiv.org/abs/0903.3640
- citation: 'Y. Sumino, Family gauge symmetry as an origin of Koide''s mass formula and charged lepton spectrum, J. High Energy Phys. 05 (2009), 075.'
  key: Sumino2009
extraction:
  note: >-
    Imported so that synthesis.koide-channel-phase-target-depends-on-mass-definition can pin the
    pole to running mass relation it uses; the QED counterpart of the stored QCD Fact
    synthesis.imported-one-loop-pole-mass-relation (colour factor 4/3 replaced by the unit charge
    squared). Checked on 2026-11-01 against arXiv:0903.3640 (abstract page and PDF): eq. (6),
    m_i^pole = [1 + (alpha/pi){(3/4) log(mu^2/mbar_i(mu)^2) + 1}] mbar_i(mu), introduced as the
    one-loop QED radiative correction, and the statement that Koide's formula, if it held for
    running masses, is corrected by about 0.1 percent, 120 times the experimental error at the time
    (citing Li and Ma 2006 and Xing and Zhang 2006). The arXiv text is a short account of the
    author's family-gauge work; the journal paper Sumino2009 of the references file is cited with
    it, its identity with the arXiv number not checked.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Leon approved the import of the one-loop QED pole to MS-bar relation as a routine Fact).'
---

## formal
For a charged lepton $i$ of unit charge, the pole mass and the $\overline{\mathrm{MS}}$ running mass at scale $\mu$ are related at one loop in QED by
\[
m_{i}^{\mathrm{pole}} = \Bigl[1 + \frac{\alpha}{\pi}\Bigl\{\frac34\ln\frac{\mu^{2}}{\bar{m}_{i}(\mu)^{2}} + 1\Bigr\}\Bigr]\bar{m}_{i}(\mu),
\]
the QED analogue of the QCD relation of \claimref{synthesis.imported-one-loop-pole-mass-relation} with the colour factor replaced by the squared charge. Since the correction depends on the lepton through $\ln\bar{m}_{i}$, ratios of running masses at a common scale differ from ratios of pole masses at first order in $\alpha$, and Koide's relation, which holds for the pole masses to about $10^{-5}$, would be corrected by about $0.1\%$ if it held for running masses instead. \emph{Provenance:} \cite{Sumino2009b} (eq. (6)), \cite{Sumino2009}.

## technical
A charged lepton's mass can be defined as the pole of its propagator or as a running mass in the minimal-subtraction scheme. At one loop in QED the two differ by a fraction of order $\alpha/\pi$ that contains the logarithm of the mass itself, so the electron, muon and tau are shifted by different amounts. Mass ratios, and Koide's relation among the three, therefore depend on which definition is used, at the level of a part in a thousand.

## lay
There are two standard ways to define the mass of a charged particle such as the electron, and quantum effects of electromagnetism make them differ slightly, by different amounts for the electron, muon and tau. A famous exact-looking relation among the three masses holds for one definition and is off by a tenth of a percent for the other.

## one-liner
$m^{\mathrm{pole}} = [1 + (\alpha/\pi)(1 + \tfrac34\ln(\mu^{2}/\bar{m}^{2}))]\bar{m}(\mu)$ at one loop in QED, so running-mass ratios differ from pole-mass ratios at order $\alpha$ (Sumino 2009).
