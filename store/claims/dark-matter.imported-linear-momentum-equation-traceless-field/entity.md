---
id: dark-matter.imported-linear-momentum-equation-traceless-field
kind: claim
version: 3
title: 'Imported: the linear momentum equation and the traceless field equation'
status: imported
region: dark-matter
subject: dark-matter
tags: [classical-theorem]
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
- name: Claude Opus 5.5
  role: 'GA rewrite (covariant conservation)'
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: C.-P. Ma and E. Bertschinger, Cosmological perturbation theory in the synchronous and conformal
    Newtonian gauges, Astrophys. J. 455, 7 (1995).
  key: MaBertschinger1995
  locator: eqs.~(30), (23d)
locators:
  paper: T14
  number: Fact 7.27
  label: fact:linpert
  line: 1171
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The covariant conservation is written dot-T(dot-D) = 0 for the stress-energy map of Gauge Theory Gravity, with nabla_mu T^{mu nu} = 0 as a labelled reading; the source''s form (the previous formal level) is in source_formal; the equations are unchanged; status imported.'
  source_formal: |-
    For the perturbed FLRW gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) in conformal Newtonian gauge, $\hb^{-1}(e_\tau) = a(1 + \psi)\,e_\tau$, $\hb^{-1}(e_i) = a(1 - \phi)\,e_i$ at linear order, whose derived metric in the source's signature $(-,+,+,+)$ is $ds^{2} = a^{2}[-(1 + 2\psi)d\tau^{2} + (1 - 2\phi)dx^{2}]$, the covariant conservation of the stress-energy under $D$ ($\nabla_{\mu}T^{\mu\nu} = 0$) gives a pressureless component of velocity divergence $\theta$ and anisotropic stress $\sigma$ the momentum equation $\theta' = -\mathcal{H}\theta + k^{2}\psi - k^{2}\sigma$, and the traceless part of the field equations of the gravitational field gives $k^{2}(\phi - \psi) = 12\pi G a^{2}\sum_{i}(\rho_{i} + p_{i})\sigma_{i}$. \emph{Provenance:} \cite[eqs.~(30), (23d)]{MaBertschinger1995}.
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported; levels only.
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: conformal Newtonian gauge as the perturbed FLRW field hb^{-1}(e_tau) = a(1 + psi) e_tau, hb^{-1}(e_i) = a(1 - phi) e_i at linear order, its derived metric kept in the source''s signature (-,+,+,+) (DICTIONARY C7); conservation under D; field equations of the gravitational field. Equations and provenance unchanged.'
---

## formal
For the perturbed FLRW gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) in conformal Newtonian gauge, $\hb^{-1}(e_\tau) = a(1 + \psi)\,e_\tau$, $\hb^{-1}(e_i) = a(1 - \phi)\,e_i$ at linear order, whose derived metric in the source's signature $(-,+,+,+)$ is $ds^{2} = a^{2}[-(1 + 2\psi)d\tau^{2} + (1 - 2\phi)dx^{2}]$, the covariant conservation of the stress-energy map under $D$, $\dot T(\dot D) = 0$ (in components $\nabla_{\mu}T^{\mu\nu} = 0$), gives a pressureless component of velocity divergence $\theta$ and anisotropic stress $\sigma$ the momentum equation $\theta' = -\mathcal{H}\theta + k^{2}\psi - k^{2}\sigma$, and the traceless part of the field equations of the gravitational field gives $k^{2}(\phi - \psi) = 12\pi G a^{2}\sum_{i}(\rho_{i} + p_{i})\sigma_{i}$. \emph{Provenance:} \cite[eqs.~(30), (23d)]{MaBertschinger1995}.

## technical
For the perturbed FLRW gravitational field on flat spacetime in conformal Newtonian gauge, whose derived metric is $ds^{2} = a^{2}[-(1 + 2\psi)d\tau^{2} + (1 - 2\phi)dx^{2}]$, covariant conservation of the stress tensor gives a pressureless component with velocity divergence $\theta$ and anisotropic stress $\sigma$ the momentum equation $\theta' = -\mathcal{H}\theta + k^{2}\psi - k^{2}\sigma$. The traceless part of the field equations ties the difference of the two potentials to the total anisotropic stress, $k^{2}(\phi - \psi) = 12\pi G a^{2}\sum_{i}(\rho_{i} + p_{i})\sigma_{i}$. These are the standard linear-perturbation equations of Ma and Bertschinger.

## lay
These are the standard textbook equations for how small ripples in the early universe's matter move and how they disturb the gravitational field. One says how a component's flow speeds up or slows down under gravity and its own internal stresses; the other says that sideways stresses make the two kinds of gravitational potential differ.

## one-liner
In conformal Newtonian gauge a pressureless component obeys $\theta' = -\mathcal{H}\theta + k^{2}\psi - k^{2}\sigma$, and the traceless field equation gives $k^{2}(\phi - \psi) = 12\pi G a^{2}\sum_{i}(\rho_{i} + p_{i})\sigma_{i}$.
