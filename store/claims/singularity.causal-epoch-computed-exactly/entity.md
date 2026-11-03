---
id: singularity.causal-epoch-computed-exactly
kind: claim
version: 4
title: The causal epoch, computed exactly
status: proved
region: singularity
subject: entropy
tags: [schwarzschild]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:10.4
- kind: check
  ref: check.py::check_integrand_partial_fractions_antiderivative
- kind: check
  ref: check.py::check_closed_form_inside_riemann_bracket
- kind: check
  ref: check.py::check_expansion_remainder_and_energy_independence
locators:
  paper: T05
  number: Lem 10.4
  label: lem:epoch
  line: 2145
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the integrand, partial fractions and antiderivative as rational-function identities, the closed form inside exact Riemann brackets (old form outside), and the O(eps) remainder bounded by 2M eps and 4M eps. Version 3 -> 4.'
  env: lemma
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    note: 'Removed the mechanically added transport-algorithm edge: the lemma is a geodesic integral in
      the Schwarzschild interior and uses no step of the algorithm; it is classical general relativity
      throughout, so no separate standard route is needed.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: rain geodesics are the radial worldlines of the Schwarzschild field on flat spacetime with D-parallel velocity hb^{-1}(x'') (the Painleve-Gullstrand frame, velocity e_t); the singularity named as the singular locus r = 0. Same integral and expansion; proof given a pointer.'
---

## formal
For the Schwarzschild gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), along the rain worldlines of the interior, the radial infall worldlines with unit energy at infinity whose velocity $\hb^{-1}(x')$ is $D$-parallel and which are the worldlines of the Painlev\'e-Gullstrand frame of Section \ref{sec:locate} (velocity $e_t$ in the gauge $\hb = 1 - \beta P$), $|dt/dr| = \sqrt{r/2M}\;r/(2M - r)$ in static Killing time $t$, so the span of Killing time between crossing $r = 2M(1 - \varepsilon)$ and reaching the singular locus $r = 0$ is
\[
\Delta t(\varepsilon) \;=\; \int_0^{2M(1-\varepsilon)} \sqrt{\frac{r}{2M}}\,\frac{r\,dr}{2M - r}
\;=\; 4M\Bigl(\tfrac12\ln\frac{1+u}{1-u} - u - \tfrac{u^{3}}{3}\Bigr)\Big|_{u = \sqrt{1-\varepsilon}}
\;=\; 2M\Bigl(\ln\tfrac{1}{\varepsilon} - \tfrac83 + 2\ln 2\Bigr) + O(\varepsilon) :
\]
of order $M$ for any fixed regulator $\varepsilon$, with only logarithmic sensitivity to the horizon-crossing cutoff, the coefficient $2M$ of the logarithm being independent of the worldline's energy. The informal estimate ``$\Delta t \sim M$ up to a logarithm'' is exactly this statement, with the logarithm identified.

## technical
For the Schwarzschild field on flat spacetime, along the rain worldlines of the interior, radial free fall (velocity $\hb^{-1}(x')$ $D$-parallel) with unit energy at infinity, the worldlines of the Painlev\'e-Gullstrand frame, $|dt/dr| = \sqrt{r/2M}\;r/(2M - r)$ in static Killing time. The span of Killing time between crossing $r = 2M(1-\varepsilon)$ and reaching the singular locus $r = 0$ is computed in closed form, and expands as $\Delta t(\varepsilon) = 2M\bigl(\ln\tfrac{1}{\varepsilon} - \tfrac83 + 2\ln 2\bigr) + O(\varepsilon)$.

So the epoch is of order $M$ for any fixed regulator $\varepsilon$, with only logarithmic sensitivity to the horizon-crossing cutoff, and the coefficient $2M$ of the logarithm does not depend on the worldline's energy.

## lay
An observer falling into a black hole from rest far away crosses the horizon and then reaches the singularity. This result computes exactly how much of the outside clock time that journey spans. The answer is about the black hole's mass in natural units, with a mild logarithmic dependence on exactly where the horizon crossing is taken to be.

## one-liner
For the Schwarzschild field on flat spacetime, the Killing-time span from horizon crossing to the singular locus along the rain worldlines is $2M(\ln\tfrac{1}{\varepsilon} - \tfrac83 + 2\ln 2) + O(\varepsilon)$, of order $M$.
