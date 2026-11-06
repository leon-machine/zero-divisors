---
id: synthesis.imported-superhorizon-zeta-conservation
kind: claim
version: 3
title: 'Imported: superhorizon conservation of the curvature perturbation (Wands et al.)'
status: imported
region: synthesis
subject: dark-energy
tags: [confronted-with-data, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-23
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
- citation: 'D. Wands, K. A. Malik, D. H. Lyth and A. R. Liddle, A new approach to the evolution of cosmological perturbations on large scales, Phys. Rev. D 62 (2000), 043527.'
  key: WandsMalikLythLiddle2000
  doi: 10.1103/PhysRevD.62.043527
extraction:
  note: >-
    Imported so that synthesis.finite-range-descent-deposit-cannot-seed-cmb can pin the
    superhorizon conservation of an adiabatic zeta, which it cites from memory in its passive
    reading. Checked on 2026-10-23 against the abstract of arXiv:astro-ph/0003278: title,
    authors, DOI, the statement that on sufficiently large scales the curvature perturbation on
    uniform-density hypersurfaces is conserved when the non-adiabatic pressure perturbation is
    negligible, and that this is shown independently of the gravitational field equations (from
    local energy conservation). The displayed evolution equation is the paper's result as
    remembered, not checked line by line.
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Created by the maintainer pass (the fix round asked for superhorizon conservation of adiabatic zeta, cited from memory by the finite-range descent result, to be imported as a Fact).'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the perturbed FLRW universe is a gravitational field on flat spacetime perturbing the comoving FLRW field; zeta read from the derived metric of the slices; energy conservation as covariant conservation under D. Content and provenance unchanged.'
  maintainer_pass_five_fronts:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 3: the per-species statement added (Leon approved the import of the conservation of decoupled species'' zeta), so that synthesis.adiabatic-deposit-modulation-is-a-time-shift can pin it; checked on 2026-11-01 against arXiv:astro-ph/0003278, Section III C: the curvature perturbation on the uniform-density hypersurfaces of each fluid, remaining constant on large scales for adiabatic perturbations of any fluid whose energy-momentum is locally conserved, applied there to non-interacting cold dark matter and radiation, with the total zeta constant only when the two coincide and the entropy perturbation between them proportional to the difference of the two (their eq. (21)). The definition is written in the store''s notation (-psi + delta rho_i/(3(rho_i + p_i)), equivalent to their form through the continuity equation); the sign convention of their eq. (21) was not checked. The total-zeta clause is unchanged.'
---

## formal
Let $\zeta$ be the curvature perturbation on hypersurfaces of uniform energy density in a perturbed FLRW universe, a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) perturbing the comoving FLRW field $\hb^{-1}(e_t) = e_t$, $\hb^{-1}(e_i) = a(t)\,e_i$ ($\zeta$ read from the spatial curvature of the slices in the derived metric), with total pressure perturbation $\delta p = c_{s}^{2}\delta\rho + \delta p_{\mathrm{nad}}$. On scales much larger than the Hubble length, $k \ll aH$, local energy conservation alone (the covariant conservation of the stress-energy under $D$) gives $\dot\zeta = -\tfrac{H}{\rho + p}\,\delta p_{\mathrm{nad}}$ up to terms suppressed by $(k/aH)^{2}$, so for adiabatic perturbations ($\delta p_{\mathrm{nad}} = 0$) $\zeta$ is constant while the mode is outside the Hubble length, whatever the gravitational field equations. The same holds species by species: for components that do not exchange energy, each covariantly conserved on its own with a pressure perturbation adiabatic within the species, the curvature perturbation on that species' own uniform-density slices, $\zeta_{i} = -\psi + \delta\rho_{i}/(3(\rho_{i} + p_{i}))$ ($\psi$ the curvature perturbation of the slicing), is constant outside the Hubble length; the total $\zeta$ is then constant only if the $\zeta_{i}$ agree, and the entropy perturbation between two species, $3(\zeta_{i} - \zeta_{j})$ up to sign convention, is conserved. \emph{Provenance:} \cite{WandsMalikLythLiddle2000}.

## technical
The comoving curvature perturbation of the uniform-density slices is the standard variable for primordial fluctuations. On scales larger than the Hubble length it changes only through non-adiabatic pressure, that is through relative fluctuations between components; for an adiabatic perturbation it is frozen. The result follows from energy conservation alone, so it holds for any theory of the gravitational field on flat spacetime, or metric theory, in which matter is covariantly conserved. It is why the amplitude measured at a scale can be traced back unchanged to the time the scale was last outside the Hubble length. The same argument applies to each component that exchanges no energy with the others: its own curvature perturbation is conserved, so relative (isocurvature) perturbations between decoupled components are conserved too.

## lay
The primordial ripples in the density of the universe stay frozen while they are larger than the distance light can travel in the age of the universe at that time, provided all the components fluctuate together. That is why the ripples seen in the microwave background can be read as the ripples laid down at the beginning.

## one-liner
For adiabatic perturbations the curvature perturbation $\zeta$ on uniform-density slices is constant outside the Hubble length, by energy conservation alone, and so is each non-interacting species' own $\zeta_{i}$ (Wands, Malik, Lyth and Liddle 2000).
