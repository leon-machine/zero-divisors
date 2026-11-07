---
id: dark-energy.cosmological-constant-does-not-change-residue
kind: claim
version: 7
title: The cosmological constant does not change the residue
status: proved
region: dark-energy
subject: interior
tags: [cosmological-constant, kasner, schwarzschild]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
- name: Claude Opus 5.5
  role: GA rewrite (gauge field and connection stated in GA, forms as labelled reading)
  version: 7
  source: maintainer pass 2026-11-07 (consistency)
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - interior.schwarzschild-de-sitter-weighted-limit@7
  - dark-energy.imported-weighted-limit-schwarzschild-singularity-matching@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T10.py
  tags:
  - label:prop:lambdacorr
- kind: check
  ref: check.py::check_field_equations_of_the_bianchi_field
- kind: check
  ref: check.py::check_unique_odd_formal_solution
- kind: check
  ref: check.py::check_constraint_propagates
- kind: check
  ref: check.py::check_schwarzschild_de_sitter_residue_unchanged
locators:
  paper: T10
  number: Prop 4.8
  label: prop:lambdacorr
  line: 871
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Forms to GA: the Bianchi I field is given by its gauge field, hb^{-1}(e_tau) = gamma_0, hb^{-1}(e_i) = a_i gamma_i, with the derived metric line element and the Levi-Civita connection forms omega^{i0} = H_i e^i kept only as labelled component readings (formal and technical). A notation change: the line element is Q(hb^{-1}(dx)) and the forms are the components of the stated Omega (DICTIONARY C10), the same field as in dark-energy.frozen-point-datum-kasner-wall, whose GA values were checked exactly. Proof unchanged (not in forms).'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Bianchi I field equations computed from the GTG gauge fields, the unique odd formal series with formal Lambda and its quoted coefficients, constraint propagation, and the unchanged SdS residue. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6.'
  typing:
    by: ai-typing-pass
    added:
    - dark-energy.imported-weighted-limit-schwarzschild-singularity-matching
    note: 'Added the imported weighted-limit fact from context_refs because the Schwarzschild-de Sitter
      clause takes its correction rates from it; the source does not present the Bianchi I computation
      as classical, so no standard-route was added. Levels pass: lay and one-liner now say diagonal Bianchi
      I and unique formal solution; lay adds that the Schwarzschild-de Sitter corrections are larger and
      singular.'
  env: proposition
  context_refs:
  - dark-energy.imported-weighted-limit-schwarzschild-singularity-matching
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-energy.imported-weighted-limit-schwarzschild-singularity-matching
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the diagonal Bianchi I metric becomes the derived metric of a gravitational field (hb, Omega) on flat spacetime; the Levi-Civita connection is the rotation-gauge field on the orthonormal physical frame, Omega(gamma_i) = H_i gamma_0 ^ gamma_i (the convention of interior.interior-connection-exactly), with the one-form reading kept in parentheses; Ric = Lambda g becomes R(a) = Lambda a in the store sign. Equations, series and conclusions unchanged; proof not in metric language, untouched. Fix (Leon 2026-10-23, referee GR1): displayed connection values re-signed to the GTG sign of the definition, D_a = a.nabla + Omega(a) x (Cartan forms omega^i_0 = sigma_i theta^i assemble to -sigma_i B_i; Hubble-normalised Kasner model -sum_i p_i B_i, DICTIONARY C10); content unchanged. Omega(gamma_i) = -H_i gamma_0 ^ gamma_i (the one-form reading omega^{i0} = H_i e^i unchanged).'
---

## formal
Let $(\hb, \Omega)$ be a diagonal Bianchi I gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), given by $\hb^{-1}(e_\tau) = \gamma_0$, $\hb^{-1}(e_i) = a_i(\tau)\,\gamma_i$ on the background frame of the labels $(\tau, x^i)$ (derived metric, in components, $g = d\tau^2 - \sum_i a_i(\tau)^2(dx^i)^2$), with Hubble rates $H_i = \dot a_i/a_i$, so that on the orthonormal physical frame $\{\gamma_0, \gamma_i\}$ over $(\partial_\tau, \partial_i)$ the rotation-gauge field is $\Omega(\gamma_i) = -H_i\,\gamma_0 \wedge \gamma_i$, $\Omega(\gamma_0) = 0$ (in components, a labelled reading: the Levi-Civita connection forms $\omega^{i0} = H_i\,e^i$ of the coframe $e^i = a_i\,dx^i$), and impose the vacuum field equations with cosmological constant, $\mathcal{R}(a) = \Lambda a$ in the store's sign (for the derived metric, $\mathrm{Ric} = \Lambda g$):
\[
\dot H_i + H_i\sum_j H_j = \Lambda \quad (i = 1,2,3), \qquad \sum_{i<j}H_iH_j = \Lambda .
\]
Then for every Kasner point $(p_1, p_2, p_3)$ there is a unique formal solution with a simple pole of residue $p$ at $\tau = 0$, and it is odd in $\tau$ with regular corrections:
\[
H_i \;=\; \frac{p_i}{\tau} \;+\; \frac{\Lambda}{2}\,(1 - p_i)\,\tau \;+\; \sum_{n \geq 2} h_{i,n}\,\tau^{2n-1},
\]
every $h_{i,n}$ a polynomial in $\Lambda$ and $p$ determined by the evolution equations alone, the constraint then holding identically. In the Bianchi I class the first correction to the connection is therefore $O(\Lambda\tau)$ and regular. At a Schwarzschild-de Sitter wall, whose slices are Kantowski-Sachs rather than flat, the sphere's intrinsic curvature adds corrections of relative order $\tau^{1/3}$ in the rotation block and $\tau^{2/3}$ in the boost block (Fact \claimref{dark-energy.imported-weighted-limit-schwarzschild-singularity-matching}), larger than $\Lambda\tau^2$ and singular in absolute terms; what this proposition establishes there is only that the residue, the coefficient of $\tau^{-1}$, is the Kasner boost of the $\Lambda = 0$ approach and that the field equations at the wall remain the Kasner relations.

## technical
For a diagonal Bianchi I gravitational field on flat spacetime, $\hb^{-1}(e_\tau) = \gamma_0$, $\hb^{-1}(e_i) = a_i\gamma_i$ (derived metric $d\tau^2 - \sum_i a_i^2 (dx^i)^2$), with Hubble rates $H_i = \dot a_i/a_i$ and rotation-gauge field $\Omega(\gamma_i) = -H_i\,\gamma_0 \wedge \gamma_i$ on the orthonormal physical frame, the field equations with cosmological constant, $\mathcal{R}(a) = \Lambda a$ (for the derived metric $\mathrm{Ric} = \Lambda g$), are the evolution equations $\dot H_i + H_i \sum_j H_j = \Lambda$ together with the constraint $\sum_{i<j} H_i H_j = \Lambda$. For every Kasner point $p$ there is a unique formal solution with a simple pole of residue $p$ at $\tau = 0$. It is odd in $\tau$, $H_i = p_i/\tau + \tfrac{\Lambda}{2}(1 - p_i)\tau + \sum_{n \geq 2} h_{i,n}\tau^{2n-1}$, each coefficient a polynomial in $\Lambda$ and $p$ fixed by the evolution equations, and the constraint then holds identically.

So within the Bianchi I class the cosmological constant enters only through a regular correction of order $\Lambda\tau$. At a Schwarzschild-de Sitter wall, whose slices are Kantowski-Sachs, the sphere's curvature adds larger corrections, of relative order $\tau^{1/3}$ in the rotation block and $\tau^{2/3}$ in the boost block; there the result asserts only that the residue, the coefficient of $\tau^{-1}$, is the Kasner boost of the $\Lambda = 0$ approach and that the field equations at the wall remain the Kasner relations.

## lay
Near a Kasner-type singularity the expansion rates of space blow up like one over time, with fixed coefficients called the Kasner exponents. This result shows that, in the simplest anisotropic cosmologies (diagonal Bianchi I), adding a cosmological constant leaves those leading coefficients untouched: for each choice of exponents there is exactly one solution as a formal power series, and it differs only by small, well-behaved corrections. For the interior of a black hole with a cosmological constant the claim is narrower: the leading singular coefficient is the same as without it, while the sphere's curvature adds larger corrections that are not well behaved.

## one-liner
A cosmological constant leaves the residue of the Kasner pole unchanged: in diagonal Bianchi I the unique formal solution has only regular odd corrections starting at order $\Lambda\tau$, and at a Schwarzschild-de Sitter wall the residue is still the Kasner boost of the $\Lambda = 0$ approach.
