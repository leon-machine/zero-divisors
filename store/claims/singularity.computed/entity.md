---
id: singularity.computed
kind: claim
version: 5
title: $\kappa = 1/4M$, computed
status: proved
region: singularity
subject: thermality
tags: [hawking-temperature, schwarzschild]
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
- name: Claude Opus 5.5
  role: 'GA rewrite (acceleration as (u.D)u)'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - singularity.imported-surface-gravity-redshifted-acceleration@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_killing_field_and_its_norm
- kind: check
  ref: check.py::check_redshifted_acceleration_of_static_observers
- kind: check
  ref: check.py::check_surface_gravity_on_the_horizon_locus
locators:
  paper: T05
  number: Prop A.2
  label: prop:kappaval
  line: 2583
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The static observer''s acceleration is named the physical vector field (u.D)u, with A^mu = u^nu nabla_nu u^mu and the static-chart Christoffel symbol as its labelled component reading (dictionary Fact (ii)); the computation is unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: PG gauge fields: K = hb^{-1}(e_t) Killing with Q(K) = f; redshifted acceleration of static observers equals f''/2; (K.D)K = K/4M on the horizon locus. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    removed: [singularity.plane-rate]
    note: 'the plane-rate proposition is cited because its time conversion follows from this result, not as a premise, so it was removed'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the static observers of the Schwarzschild field on flat spacetime, K = hb^{-1}(e_t), Q(K) = f, acceleration (v.D)v; same value kappa = 1/4M. Proof given a pointer to the GTG dictionary.'
---

## formal
For the Schwarzschild gravitational field of \ref{app:metric} (the stored field $\hb = 1 - \beta P$ on flat spacetime, Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), the static Killing field $K = \hb^{-1}(e_t)$ has $Q(K) = f = 1 - 2M/r$, and the static observers, of velocity $v = K/\sqrt f$, have redshifted proper acceleration $\sqrt f\,\sqrt{-Q((v \cdot D)v)} = f'(r)/2$ at every $r > 2M$, so the surface gravity of the horizon locus $r = 2M$ is
\[
\kappa \;=\; \lim_{r \to 2M} \frac{f'(r)}{2} \;=\; \frac{1}{2}\cdot\frac{2M}{(2M)^2} \;=\; \frac{1}{4M} .
\]

## technical
For the static black-hole field on flat spacetime, a static observer has velocity $v = K/\sqrt f$, with $K = \hb^{-1}(e_t)$ the static Killing field and $Q(K) = f$. Its acceleration $(v \cdot D)v$ has the single radial coordinate component $A^r = f'/2$, its proper magnitude is $f'/(2\sqrt f)$, and multiplying by the redshift factor $\sqrt f$ gives the redshifted acceleration $f'(r)/2$ at every $r > 2M$.

Surface gravity is the horizon limit of this redshifted acceleration, so $\kappa = \lim_{r \to 2M} f'(r)/2 = \tfrac12 \cdot 2M/(2M)^2 = 1/4M$.

## lay
Surface gravity measures how strongly a black hole's horizon pulls, as judged from far away. It is found by taking the acceleration an observer needs to hover at fixed distance, correcting it for the gravitational redshift, and following that quantity down to the horizon. For a non-rotating black hole of mass M the result is 1/(4M) in natural units.

## one-liner
For the Schwarzschild field on flat spacetime the redshifted acceleration of static observers, $v = K/\sqrt f$, is $f'(r)/2$, so the surface gravity is $\kappa = 1/4M$.
