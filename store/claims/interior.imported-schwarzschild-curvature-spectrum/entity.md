---
id: interior.imported-schwarzschild-curvature-spectrum
kind: claim
version: 7
title: 'Imported: the Schwarzschild curvature spectrum'
status: proved
region: interior
subject: einstein
tags: [schwarzschild, curvature-and-field-equations]
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
- name: Claude Opus 5.5
  role: 'GA rewrite (round-sphere line element renamed)'
  version: 7
  source: maintainer pass 2026-11-07 (consistency)
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - interior.imported-equivalence-einstein-equations@3
  - singularity.solution-where-divergence-lies@4
  proof: proof-main.tex
- name: standard-route
  uses:
  - interior.imported-schwarzschild-curvature-spectrum-external@1
  proof: proof-standard-route.tex
checked_by:
- kind: legacy
  script: verify_T06.py
  tags:
  - num:2.2
- kind: check
  ref: check.py::check_static_gauge_field_is_torsion_free_with_static_metric
- kind: check
  ref: check.py::check_static_spectrum_on_frame_planes
- kind: check
  ref: check.py::check_painleve_gullstrand_gauge_gives_the_same_spectrum
- kind: check
  ref: check.py::check_top_eigenspace_is_sigma_r_and_its_dual
locators:
  paper: T06
  number: Fact 2.2
  label: fact:spectrum
  line: 366
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The round-sphere element r^2 dOmega^2 of the line element is written r^2(d theta^2 + sin^2 theta d phi^2), so that Omega names only the rotation-gauge field (reader R03); the line element is the derived metric''s reading and stays; notation only.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: static-gauge Schwarzschild field torsion-free with the static derived metric; store-sign calR from hb and Omega diagonal with 2M/r^3 on sigma_r and I sigma_r and -M/r^3 on mixed planes, Ricci zero; the same from the PG gauge field with Omega(e_t) = (M/r^2) sigma_r; top eigenspace dimension 2. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6.'
  typing:
    by: ai-typing-pass
    removed:
    - interior.imported-schwarzschild-curvature-spectrum-external
    added:
    - interior.imported-equivalence-einstein-equations
    note: 'The Doran-Lasenby textbook is cited as the same computation elsewhere, so it moved from main to a standard-route; the GTG-Einstein equivalence from context_refs was added because the agreement of the two computations rests on it; the mixed-plane Cartan computation of the singularity paper''s appendix has no store entity.'
  env: fact
  context_refs:
  - interior.imported-equivalence-einstein-equations
  - singularity.solution-where-divergence-lies
  flags:
  - 'fact restating several series results: derived from them'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the static spherically symmetric vacuum metric is now the derived metric of the Schwarzschild field on flat spacetime in the static gauge, the curvature operator is the store-sign operator R(B) of the definition object on physical bivectors, and the frame is the static orthonormal frame of physical vectors. Eigenvalues and planes unchanged; proof given a pointer to the dictionary Fact.'
---

## formal
For the Schwarzschild gravitational field $(\hb, \Omega)$ on flat spacetime in the static gauge, whose derived metric is the static spherically symmetric vacuum metric $f\,dt_s^2 - f^{-1}dr^2 - r^2(d\theta^2 + \sin^2\theta\,d\varphi^2)$ with $f = 1 - 2M/r$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), the curvature operator $B \mapsto \mathcal{R}(B)$ on physical bivectors, in the store's sign, is diagonal on the coordinate planes of the static orthonormal frame of physical vectors, with eigenvalue of one magnitude, $2M/r^3$, on the radial boost plane $\sigma_r$ and its Hodge dual $I\sigma_r$, and eigenvalue of half that magnitude and opposite sign, $-M/r^3$, on the four mixed planes. \emph{Provenance:} the radial-plane eigenvalue from the gauge field alone in \cite[Prop.~2.4(1)]{ButlerT5}; the mixed- and angular-plane eigenvalues by the Cartan structure equations in the static chart in \cite[App.~A]{ButlerT5}, the two computations agreeing on the invertible region by Fact \claimref{interior.imported-equivalence-einstein-equations}; the same computation in the GTG literature is \cite[Ch.~14]{DoranLasenby2003}.

## technical
For the Schwarzschild field on flat spacetime in the static gauge, with derived metric $f\,dt_s^2 - f^{-1}dr^2 - r^2(d\theta^2 + \sin^2\theta\,d\varphi^2)$ and $f = 1 - 2M/r$, the field strength read as the curvature operator $\mathcal{R}(B)$ on physical bivectors is diagonal on the coordinate planes of the static orthonormal frame. Its eigenvalue is $2M/r^3$ on the radial boost plane $\sigma_r$ and its dual $I\sigma_r$, and $-M/r^3$ on the four mixed planes.

The radial-plane value comes from the gauge field alone, the others from the Cartan structure equations in the static chart, and the two computations agree on the invertible region by the equivalence of the gauge field equations with Einstein's. The same computation appears in the gauge theory gravity literature.

## lay
The tidal part of the gravitational field strength around a non-rotating black hole has a simple form: one pair of planes feels a stretching or squeezing of one strength, and the four remaining mixed planes feel half that strength with the opposite sign. This standard result is restated from earlier work in the series.

## one-liner
The curvature operator $\mathcal{R}(B)$ of the Schwarzschild field is diagonal in the static frame, with eigenvalue $2M/r^3$ on the radial plane and its dual and $-M/r^3$ on the four mixed planes.
