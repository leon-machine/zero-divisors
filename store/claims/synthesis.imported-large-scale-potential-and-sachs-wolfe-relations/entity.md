---
id: synthesis.imported-large-scale-potential-and-sachs-wolfe-relations
kind: claim
version: 1
title: 'Imported: super-Hubble potential and Sachs-Wolfe relations'
status: imported
region: synthesis
subject: dark-energy
tags: [confronted-with-data, classical-theorem]
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
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'L. Sriramkumar, An introduction to inflation and cosmological perturbation theory, arXiv:0904.4584 (2009).'
  key: Sriramkumar2009
  locator: 'eqs. (69), (70a), (70b)'
- citation: 'D. Langlois and A. Riazuelo, Correlated mixtures of adiabatic and isocurvature cosmological perturbations, Phys. Rev. D 62 (2000), 043504; arXiv:astro-ph/9912497.'
  key: LangloisRiazuelo2000
  locator: 'eqs. (2), (3), (26), (28), (29), (36)'
extraction:
  note: >-
    Imported so that synthesis.holographic-thermal-fluctuations-fall-short-in-the-descent-window
    (the radiation-era factor 2/3) and synthesis.adiabatic-deposit-modulation-is-a-time-shift (the
    large-angle combination) can pin relations they cited from memory. Checked on 2026-11-01:
    Sriramkumar, arXiv:0904.4584, eq. (69), R_k = ((3w + 5)/(3(w + 1))) Phi_k on super-Hubble scales
    for constant w, and eqs. (70a), (70b), Phi = (2/3) and (3/5) of the growing-mode amplitude;
    Langlois and Riazuelo, arXiv:astro-ph/9912497 (PDF): the entropy perturbation S_AB = delta
    n_A/n_A - delta n_B/n_B (eqs. (2), (3)), the Sachs-Wolfe term (Delta T/T)_SW = Delta_gamma/4 + 2
    Phi at last scattering in the matter era (eq. (26)), its adiabatic part (1/10)(3 + (4/5)
    Omega_nu) Phi_hat (eq. (28)), its CDM-isocurvature part -(2/5) Omega_c S_c (eq. (29)), and the
    hybrid combination (eq. (36)). The journal reference of Langlois and Riazuelo and the
    bibliographic data of Sriramkumar are from memory. The form proportional to zeta + 2 Omega_c
    S_c, with the neutrino fraction neglected and the radiation-era potential read as -(2/3) zeta,
    is arithmetic on the checked equations in a stated sign convention; the sources use different
    signs, so only the relative weight 2 is used.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Leon approved the import of Phi = (2/3) zeta in the radiation era and of the Langlois-Riazuelo large-scale combination as routine Facts).'
---

## formal
For adiabatic perturbations of a spatially flat FLRW field (a gravitational field on flat spacetime, Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) dominated by a fluid of constant equation of state $w$, the Bardeen potential $\Phi$ and the comoving curvature perturbation $\mathcal{R}$ (equal to $\zeta$ on super-Hubble scales) are related outside the Hubble length by
\[
\mathcal{R} = \frac{3w + 5}{3(w + 1)}\,\Phi,
\qquad\text{so}\qquad
\Phi = \tfrac23\,\mathcal{R}\ (w = \tfrac13),\qquad \Phi = \tfrac35\,\mathcal{R}\ (w = 0),
\]
in the sign convention of \cite{Sriramkumar2009}. For a mixture of adiabatic and cold-dark-matter isocurvature modes, with $S_{c} = \delta n_{c}/n_{c} - \delta n_{\gamma}/n_{\gamma}$ and last scattering in the matter era, the large-angle (Sachs-Wolfe) temperature anisotropy is $(\Delta T/T)_{\mathrm{SW}} = \tfrac14\Delta_{\gamma} + 2\Phi$, with adiabatic part $\tfrac{1}{10}(3 + \tfrac45\Omega_{\nu})\hat\Phi$ ($\hat\Phi$ the radiation-era potential, $\Omega_{\nu}$ the neutrino fraction of the radiation) and isocurvature part $-\tfrac25\,\Omega_{c}S_{c}$ ($\Omega_{c}$ the dark-matter fraction of the matter). With the neutrino fraction neglected and $\hat\Phi = -\tfrac23\zeta$, the sum is $-\tfrac15(\zeta + 2\,\Omega_{c}S_{c})$. \emph{Provenance:} \cite{Sriramkumar2009} (eqs. (69), (70a), (70b)); \cite{LangloisRiazuelo2000} (eqs. (2), (3), (26), (28), (29), (36)).

## technical
Outside the Hubble length the gravitational potential is a fixed fraction of the conserved curvature perturbation: two thirds while radiation dominates and three fifths once matter does, so the potential drops by $9/10$ at the transition. On the largest angular scales the temperature anisotropy is the Sachs-Wolfe term, one fifth of the curvature perturbation for adiabatic modes; an isocurvature perturbation of the dark matter contributes twice its matter-weighted amplitude with the same weight, which is why matter isocurvature is about six times more visible in the temperature map than an adiabatic mode of the same amplitude.

## lay
These are standard relations between the frozen primordial ripples and the gravitational dips and bumps they produce at different epochs, and the formula for how both kinds of primordial ripple, the kind where everything fluctuates together and the kind where only the dark matter does, show up as hot and cold spots on the largest scales of the microwave sky.

## one-liner
On super-Hubble scales $\Phi = \tfrac{3(1 + w)}{5 + 3w}\mathcal{R}$ ($\tfrac23$ for radiation, $\tfrac35$ for matter), and the large-angle anisotropy of adiabatic plus CDM-isocurvature modes is $\propto \zeta + 2\Omega_{c}S_{c}$ (Langlois and Riazuelo 2000).
