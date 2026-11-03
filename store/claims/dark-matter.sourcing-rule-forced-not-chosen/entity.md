---
id: dark-matter.sourcing-rule-forced-not-chosen
kind: claim
version: 3
title: The sourcing rule is forced, not chosen
status: proved
region: dark-matter
subject: dark-matter
tags: [forcing-and-uniqueness]
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
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_dust_dilution_exponents
- kind: check
  ref: check.py::check_kaluza_klein_newton_constant_cancels
- kind: check
  ref: check.py::check_projected_dust_and_heavier_rest_mass
locators:
  paper: T14
  number: Prop 7.24
  label: prop:sourcing
  line: 1147
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: clause (ii): rho_5 = C/(a^3 b) from the GTG volume factor with a^-3 dilution of rho_5 L for b ~ a and b const, G_4 rho_4 = G_5 rho_5 from the Kaluza-Klein volume factor, and the projected dust and five-momentum identity. Version 2 -> 3.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the field equations are those of a gravitational field on flat spacetime (Einstein equations for its derived metric), and the five-dimensional product metric is the derived metric of a diagonal field on flat R^{1,4} (d-dimensional clause); content unchanged. Proof prefixed.'
  typing:
    by: ai-typing-pass
    note: "No edges: the proof uses only the field equations and Kaluza-Klein reduction, and the dilution lemma is cited only as what the rule agrees with; the derivation is itself standard physics, with no imported Einstein-equation or Kaluza-Klein claim in the store, so no separate standard route was added."
  env: proposition
  context_refs:
  - dark-matter.projection-every-towers-content-dilutes-ones
---

## formal
(i) The field equations of a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), Einstein's equations $G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$ for its derived metric, are sourced by a local energy density and never by a total; the only covariant four-dimensional stress tensor obtainable from matter homogeneous along a direction the metric does not see is its integral over that direction, $\rho_{4} = \rho_{5}L$, which is Lemma \claimref{dark-matter.projection-every-towers-content-dilutes-ones} read from the field equations. (ii) It passes the three standard tests. Continuity for dust in a product metric $a(t)^{2}dx^{2} + b(t)^{2}dy^{2}$ (the derived metric of the diagonal field $\hb^{-1}(e_x) = a\,e_x$, $\hb^{-1}(e_y) = b\,e_y$ on flat $\R^{1,4}$, the $d$-dimensional clause of the definition) gives $\rho_{5} \propto 1/(a^{3}b)$, so with $L \propto b$ the projected density $\rho_{5}L$ dilutes as $a^{-3}$ for a co-expanding and a static fifth direction alike, as the lemma states. Kaluza-Klein reduction over a metric fifth direction of size $L$ gives $G_{4} = G_{5}/L$ with $\rho_{4} = \rho_{5}L$, so $G_{4}\rho_{4} = G_{5}\rho_{5}$ is independent of $L$ for the bulk tower and the share $\rho_{5}L/\rho_{\mathrm{us}}$ is the same however Newton's constant is defined. And the projected stress tensor of five-dimensional dust comoving with our slice is four-dimensional dust, a quantum with momentum along the fifth direction appearing as a heavier particle at rest, by $p^{\mu}p_{\mu} = m^{2} + p_{5}^{2}$.

## technical
The field equations of a gravitational field on flat spacetime, $G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$ for its derived metric, are sourced by a local energy density, never by a total, so for matter homogeneous along a direction the metric does not see, the only covariant four-dimensional stress tensor is its integral over that direction, $\rho_{4} = \rho_{5}L$. This is the dilution lemma's sourcing rule read from the field equations.

It passes three standard tests. Continuity for dust in $a(t)^{2}dx^{2} + b(t)^{2}dy^{2}$ gives $\rho_{5} \propto 1/(a^{3}b)$, so with $L \propto b$ the density $\rho_{5}L$ dilutes as $a^{-3}$ for co-expanding and static directions alike; Kaluza-Klein reduction gives $G_{4} = G_{5}/L$, so $G_{4}\rho_{4} = G_{5}\rho_{5}$ is independent of $L$; and five-dimensional dust projects to four-dimensional dust, momentum along the fifth direction appearing as mass through $p^{\mu}p_{\mu} = m^{2} + p_{5}^{2}$.

## lay
The paper's rule for how hidden higher-dimensional matter affects our gravity might look like an arbitrary choice. This result shows that ordinary general relativity leaves no alternative, because gravity responds to density at a point rather than to a total. The rule also passes the standard consistency checks.

## one-liner
General relativity forces the sourcing rule $\rho_{4} = \rho_{5}L$, which passes the continuity, Kaluza-Klein and dust-projection checks.
