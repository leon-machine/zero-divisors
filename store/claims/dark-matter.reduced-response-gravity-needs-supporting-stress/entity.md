---
id: dark-matter.reduced-response-gravity-needs-supporting-stress
kind: claim
version: 3
title: A reduced response to gravity needs a supporting stress; the sheets move
status: proved
region: dark-matter
subject: dark-matter
tags: [no-go]
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
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - dark-matter.imported-linear-momentum-equation-traceless-field@2
  - dark-matter.projection-every-towers-content-dilutes-ones@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_setting_derived_metric_linear_order
- kind: check
  ref: check.py::check_unique_stress_for_reduced_response
- kind: check
  ref: check.py::check_potential_with_the_stress
- kind: check
  ref: check.py::check_projected_response_and_orientation_average
locators:
  paper: T14
  number: Prop 7.28
  label: prop:sheetsmove
  line: 1175
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: derived metric of the Newtonian-gauge field at linear order; unique stress (1-g) psi; the psi formula from the traceless equation; projected response sin^2 by GA rejection and its average 2/3. Version 2 -> 3.'
  typing:
    by: ai-typing-pass
    note: 'Kept both edges: the imported perturbation equations give (i) and (ii), and the dilution lemma''s
      stress-free comoving sheets are the premise of the conclusion that the sheets move. Levels pass:
      the lay level and one-liner now keep "on the series as written" and "at linear order".'
  env: proposition
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the component responds to the gravitational field (the perturbed FLRW field in conformal Newtonian gauge, potentials psi, phi) rather than to the metric; the sourcing rule couples to the one gravitational field (hb, Omega). Clauses (i), (ii) and the conclusion unchanged.'
---

## formal
Let a pressureless component respond to the gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}; the perturbed FLRW field in the conformal Newtonian gauge of Fact \claimref{dark-matter.imported-linear-momentum-equation-traceless-field}, potentials $\psi$, $\phi$) at a fraction $g$ of the full strength, $\theta' = -\mathcal{H}\theta + g\,k^{2}\psi$. Then (i) it carries the anisotropic stress $\sigma = (1 - g)\psi$, and no other value; (ii) that stress enters the field equations, so that with the other components' stresses $\Sigma$,
\[
\psi \;=\; \frac{\phi - 12\pi G a^{2}\Sigma/k^{2}}{1 + 12\pi G a^{2}\rho\,(1 - g)/k^{2}} .
\]
For a three-dimensional tower whose sheets are held fixed, $g = \sin^{2}\theta$ for a wavevector at angle $\theta$ to the missing direction (script: $k_{\perp}^{2}/k^{2}$), $\tfrac{2}{3}$ averaged over orientations, and the stress of (i) is that of a medium holding the sheets in place. The series supplies no such medium: nothing in Lemma \claimref{dark-matter.projection-every-towers-content-dilutes-ones} or in the towers' content gives the sheet family a rigidity along its normal, and the sourcing rule couples the sheets' matter to the one gravitational field $(\hb, \Omega)$ like any other. Hence, on the series as written, the sheets are displaced along their normal by the potential gradient, $g = 1$, and the three-dimensional towers respond to gravity in full at linear order.

## technical
Let a pressureless component respond to the gravitational field at a fraction $g$ of full strength, $\theta' = -\mathcal{H}\theta + g\,k^{2}\psi$. By the linear momentum equation it then carries the anisotropic stress $\sigma = (1 - g)\psi$ and no other value, and that stress enters the traceless field equation, giving $\psi = (\phi - 12\pi G a^{2}\Sigma/k^{2})/(1 + 12\pi G a^{2}\rho(1 - g)/k^{2})$.

For a three-dimensional tower whose sheets are held fixed, $g = \sin^{2}\theta$ at angle $\theta$ to the missing direction, $\frac{2}{3}$ on average, and the stress is that of a medium holding the sheets in place. The series supplies no such medium, so on the series as written the sheets are displaced along their normal by the potential gradient, $g = 1$, and the three-dimensional towers respond to gravity in full at linear order.

## lay
Matter in a sector with fewer dimensions than ours might be expected to feel only part of gravity's pull. This result shows that a reduced response would need something physically holding that matter in place, and nothing in the framework does so. So, on the theory as it stands, the matter moves freely and responds to gravity in full, like ordinary dark matter, at least for small disturbances (at linear order).

## one-liner
A partial gravitational response $g < 1$ requires the anisotropic stress $(1 - g)\psi$, which nothing in the series supplies, so on the series as written the three-dimensional towers respond with $g = 1$ at linear order.
