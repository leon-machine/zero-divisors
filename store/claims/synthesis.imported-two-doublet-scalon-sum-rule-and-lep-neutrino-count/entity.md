---
id: synthesis.imported-two-doublet-scalon-sum-rule-and-lep-neutrino-count
kind: claim
version: 1
title: 'Imported: the Gildener-Weinberg sum rule of the scale-invariant two-doublet model, $(\sum M_{\mathcal H}^{4})^{1/4} = 540$ GeV over the extra scalars for $m_{h} = 125$ GeV (Lee and Pilaftsis 2012; Lane and Shepherd 2018), and the number of light neutrino species from the $Z$ resonance, $N_{\nu} = 2.9840 \pm 0.0082$ (LEP and SLD 2006)'
status: imported
region: synthesis
subject: standard-model
tags: [symmetry-breaking, mass-generation, confronted-with-data, classical-theorem]
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
- citation: 'J. S. Lee and A. Pilaftsis, Radiative corrections to scalar masses and mixing in a scale invariant two Higgs doublet model, Phys. Rev. D 86 (2012), 035004, arXiv:1201.4891.'
  key: LeePilaftsis2012
  doi: 10.1103/PhysRevD.86.035004
- citation: 'K. Lane and W. Shepherd, Natural stabilization of the Higgs boson''s mass and alignment, arXiv:1808.07927, equation (10).'
  key: LaneShepherd2018
- citation: 'The ALEPH, DELPHI, L3, OPAL and SLD Collaborations, the LEP Electroweak Working Group and the SLD Electroweak and Heavy Flavour Groups, Precision electroweak measurements on the Z resonance, Phys. Rep. 427 (2006), 257, arXiv:hep-ex/0509008.'
  key: LEPSLD2006
  doi: 10.1016/j.physrep.2005.12.006
extraction:
  note: >-
    Imported so that the linear rung-field result can pin the two-doublet sum rule it identifies with and the Z-width
    datum behind its argued exclusion instead of citing them from memory. Checked on 2026-11-01: equation (10) of Lane
    and Shepherd, arXiv:1808.07927, (sum over the extra Higgs bosons of M^4)^(1/4) = 540 GeV for M_H = 125 GeV,
    which the text says follows from its equation (9) and was obtained in an earlier reference it cites; the
    bibliographic data and abstract of Lee and Pilaftsis, arXiv:1201.4891 (a classically scale-invariant two-doublet
    model broken by gauge, Higgs self-coupling and top Yukawa loops; with a 125 GeV Standard-Model-like Higgs, a
    non-standard neutral scalar near 400 GeV roughly degenerate with the charged one and the third below about 500
    GeV); the abstract does not state the sum rule itself; and N_nu = 2.9840 +- 0.0082 against the abstract of
    arXiv:hep-ex/0509008 (DOI from that page). Cited from memory, not checked: the journal volume and first page of the
    Z-resonance report (Phys. Rep. 427, 257), and the general form of (i) in terms of the scalon formula, which is the
    stored Gildener-Weinberg Fact applied to the two-doublet content.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (the two-doublet Gildener-Weinberg sum rule and the LEP invisible Z width as a Fact, by Leon''s list of imports).'
---

## formal
\begin{enumerate}
\item[(i)] \emph{(The two-doublet sum rule.)} In the classically scale-invariant model with two Higgs doublets of hypercharge $\tfrac12$, radiative breaking along a flat direction (Fact \claimref{synthesis.imported-coleman-weinberg-gildener-weinberg-scalon-mass}) makes the scalon the Standard-Model-like Higgs $h$, and the scalon formula becomes a sum rule on the extra scalars $\mathcal{H} = H, A, H^{\pm}$ (the charged one counted twice): $8\pi^{2}v^{2}m_{h}^{2} = 6M_{W}^{4} + 3M_{Z}^{4} + \sum_{\mathcal H}M_{\mathcal H}^{4} - 12m_{t}^{4}$ up to the lighter fermions, which for $m_{h} = 125$ GeV gives $\bigl(\sum_{\mathcal H}M_{\mathcal H}^{4}\bigr)^{1/4} = 540$ GeV \cite{LeePilaftsis2012, LaneShepherd2018}.
\item[(ii)] \emph{(Light neutrino species.)} The invisible width of the $Z$ boson, measured at its resonance, corresponds to $N_{\nu} = 2.9840 \pm 0.0082$ light neutrino species \cite{LEPSLD2006}.
\end{enumerate}

## technical
If the Higgs boson is the pseudo-Goldstone boson of broken scale invariance in a model with two Higgs doublets, its mass comes from one loop and is fixed by the fourth powers of the other masses; the extra scalars must then compensate the top quark, which fixes the sum of their fourth powers: about $540$ GeV to the fourth power. Separately, the precision measurements of the $Z$ resonance at LEP and SLC fix the width of its decays into invisible particles, equivalent to $2.984 \pm 0.008$ species of light neutrino, so any additional light neutral particles the $Z$ can decay into are tightly limited.

## lay
In one class of theories the Higgs boson gets its mass purely from quantum effects, and if the Higgs field comes in two copies the extra particles must be heavy enough to make up for the top quark: a standard calculation puts a combined measure of their masses at about $540$ GeV. Separately, experiments at the Z boson showed there are just three kinds of light neutrino, which leaves no room for further light neutral particles the Z could produce. The series takes both from the literature.

## one-liner
Scale-invariant two-doublet model: $(\sum_{\mathcal H}M_{\mathcal H}^{4})^{1/4} = 540$ GeV over the extra scalars for $m_{h} = 125$ GeV (Lee-Pilaftsis; Lane-Shepherd eq. (10)); the $Z$ resonance gives $N_{\nu} = 2.9840 \pm 0.0082$ light neutrino species.
