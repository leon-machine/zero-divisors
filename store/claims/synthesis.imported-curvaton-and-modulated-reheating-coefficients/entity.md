---
id: synthesis.imported-curvaton-and-modulated-reheating-coefficients
kind: claim
version: 1
title: 'Imported: a dominant curvaton gives zeta = (2/3) X - (1/3) X^2 + (2/9) X^3 + ... in X = delta sigma/sigma, and a modulated decay rate gives zeta = -(1/6) delta Gamma/Gamma at first order (Choi and Seto 2012)'
status: imported
region: synthesis
subject: dark-energy
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
- citation: 'K.-Y. Choi and O. Seto, Modulated reheating by curvaton, Phys. Rev. D 85 (2012), 123528; arXiv:1204.1419.'
  key: ChoiSeto2012
  locator: 'eqs. (16), (45), (46)'
  doi: 10.1103/PhysRevD.85.123528
extraction:
  note: >-
    Imported so that synthesis.local-conversion-cannot-redden-a-gaussian-spectator can pin the two
    local conversions it reads in the series' terms. Checked on 2026-11-01 against arXiv:1204.1419
    (abstract page and PDF): title, authors, DOI; eq. (16), zeta_sigma = (2/3)(delta
    sigma_*/sigma_*) - (1/3)(delta sigma_*/sigma_*)^2 + (2/9)(delta sigma_*/sigma_*)^3 + ..., for
    the quadratic curvaton potential with R = 1 (the curvaton dominates when it decays) in the
    instant-decay approximation; eq. (45), Q = -(1/6) log(Gamma_phi(sigma)/H_c) when Gamma_phi/m_phi
    is small, and eq. (46), Q_sigma = -(1/6) d_sigma Gamma_phi/Gamma_phi. The journal reference is
    inferred from the DOI. The originators of the two mechanisms (Lyth and Wands; Moroi and
    Takahashi; Enqvist and Sloth; Dvali, Gruzinov and Zaldarriaga; Kofman) are named from memory,
    and the inherited tilt n_s - 1 = 2 eta_sigma - 2 epsilon of a dominant curvaton is not part of
    this Fact.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Leon approved the import of the curvaton and modulated-reheating coefficients as routine Facts).'
---

## formal
For a curvaton $\sigma$ with quadratic potential that dominates the energy density when it decays ($R = 1$) and decays instantly, the curvature perturbation after the decay is a local function of the curvaton's fractional fluctuation $X = \delta\sigma_{*}/\sigma_{*}$ at horizon exit:
\[
\zeta_{\sigma} = \tfrac23 X - \tfrac13 X^{2} + \tfrac29 X^{3} + \cdots.
\]
For modulated reheating, an inflaton decaying while it oscillates at a rate $\Gamma_{\phi}(\sigma)$ set by a light field, with $\Gamma_{\phi}/m_{\phi}$ small, the generated curvature perturbation is $Q \simeq -\tfrac16\log(\Gamma_{\phi}(\sigma)/H_{c})$, so at first order $\zeta = Q_{\sigma}\,\delta\sigma$ with $Q_{\sigma} = -\tfrac16\,\partial_{\sigma}\Gamma_{\phi}/\Gamma_{\phi}$, that is $\zeta = -\tfrac16\,\delta\Gamma/\Gamma$. \emph{Provenance:} \cite{ChoiSeto2012} (eqs. (16), (45), (46)).

## technical
In the curvaton and modulated-reheating mechanisms the curvature perturbation is not made by the field that drives the expansion but converted, at a decay, from the fluctuation of a light spectator: in the first through the spectator's own energy density at its decay, in the second through a decay rate that depends on it. Either way the curvature perturbation at each point is a fixed function of the spectator's local value, given here to third order for a dominant curvaton and to first order for a modulated rate.

## lay
Two well-known proposals let a light field other than the one driving the universe's expansion set the primordial ripples: either it decays late and dominates for a while, or it controls how quickly the universe reheats. In both, the ripple at each place is a simple formula in that field's local value, and these are the formulas.

## one-liner
A dominant curvaton gives $\zeta = \tfrac23X - \tfrac13X^{2} + \tfrac29X^{3} + \cdots$, $X = \delta\sigma/\sigma$; a modulated decay rate gives $\zeta = -\tfrac16\delta\Gamma/\Gamma$ at first order (Choi and Seto 2012).
