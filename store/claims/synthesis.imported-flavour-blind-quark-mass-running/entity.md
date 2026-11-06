---
id: synthesis.imported-flavour-blind-quark-mass-running
kind: claim
version: 1
title: 'Imported: flavour-blind running of quark masses'
status: imported
region: synthesis
subject: generations
tags: [running-and-unification, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: S. Navas et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110 (2024) 030001.
  key: PDG2024
  locator: 'Review 60, Quark masses (R. M. Barnett, L. P. Lellouch and A. V. Manohar), Eq. (60.2) and the paragraph on mass ratios'
  doi: 10.1103/PhysRevD.110.030001
- citation: 'K. G. Chetyrkin, B. A. Kniehl and M. Steinhauser, Decoupling relations to O(alpha_s^3) and their connection to low-energy theorems, Nucl. Phys. B 510 (1998), 61--87.'
  key: ChetyrkinKniehlSteinhauser1998
  doi: 10.1016/S0550-3213(97)00649-4
extraction:
  note: >-
    Imported for synthesis.mass-ordered-dressing-cannot-spoil-koide, whose classification of the
    perturbative strong dressing as flavour-blind at a common scale rests on these two facts, cited
    there from memory. Checked on 2026-10-26 against the PDG 2024 quark-mass review: the running
    equation mu^2 dm/dmu^2 = -gamma(alpha_s) m with gamma = sum_r gamma_r (alpha_s/4pi)^r,
    gamma_1 = 4 (Eq. 60.2), and the statement that in the same scheme and at the same scale the QCD
    renormalisation factors are identical for all quark flavours, so quark mass ratios are scheme
    and scale independent up to electromagnetic corrections; the review also says that crossing a
    quark threshold requires matching with finite threshold corrections. Checked against the
    arXiv abstract page of hep-ph/9708255: the authors, title, DOI, the MS-bar setting and the
    decoupling constant zeta_m that relates the light-quark masses across a heavy-quark threshold.
    From memory, not checked: that zeta_m is a function of alpha_s and ln(mu/m_h) only, the same for
    every lighter flavour, with zeta_m = 1 + O(alpha_s^2) at mu = m_h; the volume pages 61--87.
    Electroweak and electromagnetic running, which are not flavour-blind, are outside this Fact.
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Created by the maintainer pass of 2026-10-26 (Leon accepted the Koide-dressing result and asked for this import); clause (i) checked against the PDG review, clause (ii) partly from memory.'
---

## formal
In QCD with $n_{f}$ active flavours, renormalised in the $\overline{\mathrm{MS}}$ scheme (mass independent):
\begin{enumerate}
\item[(i)] \emph{(Flavour-blind running.)} Every quark mass obeys $\mu^{2}\,dm_{q}(\mu)/d\mu^{2} = -\gamma_{m}(\alpha_{s}(\mu))\,m_{q}(\mu)$ with $\gamma_{m} = \sum_{r \ge 1}\gamma_{r}(\alpha_{s}/4\pi)^{r}$, $\gamma_{1} = 4$, and the coefficients $\gamma_{r}$ depend on $n_{f}$ but not on the flavour $q$ or on any mass. Hence $m_{q}(\mu_{1})/m_{q}(\mu_{2})$ is the same factor for every active flavour, and the ratio of two quark masses at a common scale does not depend on that scale or on the scheme (up to electromagnetic and electroweak corrections).
\item[(ii)] \emph{(Flavour-blind decoupling.)} At the threshold of a heavy quark $h$ the masses of the lighter quarks in the theories with $n_{f}$ and $n_{f} - 1$ flavours are related by $m_{q}^{(n_{f} - 1)}(\mu) = \zeta_{m}\,m_{q}^{(n_{f})}(\mu)$, with one decoupling constant $\zeta_{m}$, a function of $\alpha_{s}(\mu)$ and $\ln(\mu/m_{h})$ only, the same for every lighter flavour; $\zeta_{m} = 1 + O(\alpha_{s}^{2})$ at $\mu = m_{h}$.
\end{enumerate}
So, between common scales and across heavy-quark thresholds, perturbative QCD multiplies all quark masses by one common factor. \emph{Provenance:} \cite{PDG2024} (Review 60, Eq. (60.2) and the statement on mass ratios), \cite{ChetyrkinKniehlSteinhauser1998} (the decoupling constant $\zeta_{m}$).

## technical
Quark masses are not fixed numbers in quantum chromodynamics: they depend on the energy scale at which they are defined, and they change at the thresholds where a heavier quark stops taking part. In the standard minimal-subtraction scheme both effects treat every quark alike. The rate of running is one function of the strong coupling for all flavours, and at a heavy-quark threshold all lighter masses are matched by one common factor. So, at any common scale, perturbative QCD rescales all quark masses together, and their ratios do not depend on the scale chosen. Electromagnetic and electroweak corrections, which do distinguish flavours, are not part of this statement.

## lay
The mass of a quark, as physicists define it, changes slowly with the energy at which it is measured, because of the strong force. This standard result says that the strong force changes all the quark masses by the same factor when they are compared at the same energy, so it does not alter how the masses compare with each other.

## one-liner
In $\overline{\mathrm{MS}}$, $\mu^{2}\,dm_{q}/d\mu^{2} = -\gamma_{m}(\alpha_{s})\,m_{q}$ with a flavour-independent $\gamma_{m}$ ($\gamma_{1} = 4$), and heavy-quark decoupling rescales every lighter mass by one constant $\zeta_{m}$, so perturbative QCD multiplies all quark masses at a common scale by one factor.
