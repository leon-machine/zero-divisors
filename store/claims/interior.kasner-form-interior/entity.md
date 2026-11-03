---
id: interior.kasner-form-interior
kind: claim
version: 5
title: Kasner form of the interior
status: proved
region: interior
subject: interior
tags: [schwarzschild, kasner]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - interior.imported-schwarzschild-curvature-spectrum@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T06.py
  tags:
  - num:5.1
- kind: check
  ref: check.py::check_synchronous_derived_metric_and_free_fall
- kind: check
  ref: check.py::check_tau_series_and_inversion
- kind: check
  ref: check.py::check_kasner_exponents_of_the_approach
locators:
  paper: T06
  number: Lem 5.1
  label: lem:kasnerform
  line: 581
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the synchronous derived metric and free fall from the GTG gauge fields, the tau series and its inversion, and the Kasner exponents (-1/3, 2/3, 2/3). Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  typing:
    by: ai-typing-pass
    note: 'Kept the curvature-spectrum fact (it supplies the static metric) and re-pinned it to its current
      version 2; another paper calls the Kasner exponents classical, but the imported Kasner claim gives
      only the exponents, not this lemma''s series and rates, so no standard-route was added. Levels pass:
      the lay level now keeps the leading-order qualifier on the Kasner powers.'
  env: lemma
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the Schwarzschild metric in synchronous form is restated as the derived metric of the Schwarzschild gravitational field (hb, Omega) on flat spacetime in a synchronous position gauge; the radial geodesics are worldlines of D-parallel velocity. Series and exponents unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact.'
---

## formal
In the interior, with $A(r) := 2M/r - 1 > 0$, the Schwarzschild gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), taken in a synchronous position gauge, has derived metric of diagonal form
\[
ds^2 \;=\; d\tau^2 - A\,dt^2 - r^2\,d\Omega^2,
\qquad
\tau(r) \;=\; \int_0^r A(u)^{-1/2}\,du ,
\]
where $\tau$ is proper time along the radial timelike worldlines ruling the interior, whose velocity $\hb^{-1}(x')$ is $D$-parallel (the geodesics of the derived metric), normalised so that the singularity is $\tau = 0$. In units $2M = 1$,
\[
\tau(r) \;=\; \tfrac23\, r^{3/2}\bigl(1 + \tfrac{3}{10}\,r + O(r^2)\bigr),
\qquad
r \;=\; R\,\bigl(1 - \tfrac15 R + O(R^2)\bigr), \quad R := (3\tau/2)^{2/3},
\]
and the scale factors obey $\sqrt{A} \propto \tau^{-1/3}$ and $r \propto \tau^{2/3}$ to leading order: the Kasner exponents of the approach are
\[
(p_1, p_2, p_3) \;=\; \bigl(-\tfrac13,\ \tfrac23,\ \tfrac23\bigr),
\qquad
p_1 + p_2 + p_3 \;=\; 1, \qquad p_1^2 + p_2^2 + p_3^2 \;=\; 1 .
\]

## technical
Inside the horizon, with $A(r) = 2M/r - 1 > 0$, the Schwarzschild gravitational field on flat spacetime, in a synchronous position gauge, has the diagonal derived metric $ds^2 = d\tau^2 - A\,dt^2 - r^2 d\Omega^2$, where $\tau(r) = \int_0^r A(u)^{-1/2}\,du$ is proper time along the radial free-fall worldlines, those whose velocity is parallel for the covariant derivative $D$, with the singularity at $\tau = 0$. In units $2M = 1$, $\tau = \tfrac23 r^{3/2}(1 + \tfrac{3}{10}r + O(r^2))$ and, inversely, $r = R(1 - \tfrac15 R + O(R^2))$ with $R = (3\tau/2)^{2/3}$.

To leading order $\sqrt A \propto \tau^{-1/3}$ and $r \propto \tau^{2/3}$, so the approach has Kasner exponents $(p_1, p_2, p_3) = (-\tfrac13, \tfrac23, \tfrac23)$, which satisfy $\sum_i p_i = 1$ and $\sum_i p_i^2 = 1$.

## lay
Inside a non-rotating black hole the roles of space and time swap, and the fall towards the centre becomes a passage of time. In the right time variable the gravitational field near the centre looks like a Kasner universe: one direction stretches while the other two shrink, each, to leading order, as a fixed power of time. This result gives those powers, minus one third and two thirds twice, together with the first corrections.

## one-liner
In proper time $\tau$ the derived metric of the Schwarzschild interior field is synchronous and diagonal, with Kasner exponents $(-\tfrac13, \tfrac23, \tfrac23)$ to leading order and explicit series corrections.
