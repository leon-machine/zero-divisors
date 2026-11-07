---
id: pairing.imported-schwarzschild-connection-curvature
kind: claim
version: 7
title: 'Imported: the Schwarzschild connection and curvature'
status: proved
region: pairing
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
  source: 'authorship disclosure of T05-pairing, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'GA rewrite (round-sphere line element renamed)'
  version: 6
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'notation: d Omega^2 written as the explicit round metric'
  version: 7
  source: maintainer pass 2026-11-07 (decisions, second round)
review: typed
about:
- obj.dark-matter.witt-flag
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - singularity.curvature-gauge-field-exact-shape-decoupling@5
  - singularity.euclidean-rotor-where-it-lies@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_static_connection_is_the_torsion_free_field
- kind: check
  ref: check.py::check_curvature_eigenvalues_on_coordinate_planes
- kind: check
  ref: check.py::check_extreme_pair_and_sign_of_square
- kind: check
  ref: check.py::check_painleve_gullstrand_gauge_field
locators:
  paper: T05-pairing
  number: Fact 1.5
  label: fact:schw
  line: 204
extraction:
  maintainer_pass_decisions_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Notation (Leon, second round, answer 8; DECISIONS H5, consistency-R03 C): the derived line element wrote the round two-sphere as d Omega^2 beside Omega the rotation-gauge field of the gravitational field (hb, Omega). It is now written (d vartheta^2 + sin^2 vartheta d varphi^2) in formal and proof, with the polar angle vartheta of the coframe (theta^i is the coframe here); the technical level''s explicit form, which wrote the angle theta beside the coframe theta^i, now writes vartheta too. No content change.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The round-sphere element r^2 dOmega^2 of the line element is written r^2(d theta^2 + sin^2 theta d phi^2), so that Omega names only the rotation-gauge field (reader R03); the line element is the derived metric''s reading and stays; notation only.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: static Schwarzschild gauge fields: connection forms torsion-free and unique, curvature eigenvalues 2M/r^3, -M/r^3 from the field strength, the extreme pair and its squares, PG gauge field hb = 1 - beta P and its derived metric. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  typing:
    by: ai-typing-pass
    removed:
    - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
    note: Removed the dark-matter asymmetry proposition, cited only for the remark that the flag bit is
      initial data (the flag itself stays in about); repinned the two singularity results to their current
      version 2; the connection forms come from the singularity paper's appendix, which has no store entity.
  env: fact
  context_refs:
  - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
  - singularity.curvature-gauge-field-exact-shape-decoupling
  - singularity.euclidean-rotor-where-it-lies
  outside_pilot_cites:
  - ButlerT5
  flags:
  - 'fact restating several series results: derived from them'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the static coframe is the orthonormal coframe of the Schwarzschild field in the static gauge on flat spacetime, the connection forms are the components of the rotation-gauge field Omega there, the curvature operator is the store-sign R(B) on physical bivectors, and the Painleve-Gullstrand form is the derived metric of the stored gauge hb = 1 - beta P, invertible through the horizon. Formulas and eigenvalues unchanged; proof given a pointer to the dictionary Fact.'
---

## formal
For the Schwarzschild gravitational field $(\hb, \Omega)$ on flat spacetime in the static gauge (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with static orthonormal coframe $\theta^{0} = \sqrt f\,dt$, $\theta^{1} = dr/\sqrt f$, $\theta^{2} = r\,d\vartheta$, $\theta^{3} = r\sin\vartheta\,d\varphi$, $f = 1 - 2M/r$, the rotation-gauge field $\Omega$, read as the connection forms of that coframe, is $\omega^{0}{}_{1} = (f'/2\sqrt f)\,\theta^{0}$, $\omega^{2}{}_{1} = (\sqrt f/r)\,\theta^{2}$, $\omega^{3}{}_{1} = (\sqrt f/r)\,\theta^{3}$, $\omega^{3}{}_{2} = (\cot\vartheta/r)\,\theta^{3}$, and the curvature operator $\mathcal{R}(B)$ on physical bivectors (the field strength in the store's sign) is diagonal on the coordinate planes with eigenvalues $2M/r^{3}$ on the radial plane $\hat0\hat1$ and the angular plane $\hat2\hat3$ and $-M/r^{3}$ on the four mixed planes. The extreme eigenvalue distinguishes the pair $\{\sigma_{r}, I\sigma_{r}\}$ invariantly, the radial plane and its Hodge dual; the radial member is selected within the pair by the sign of the square, $\sigma_{r}^{2} = +1$ against $(I\sigma_{r})^{2} = -1$. Which of the two null directions of the radial plane is the vacuum's is the flag bit, which the series takes as initial data. In the Painlev\'e-Gullstrand gauge $\hb = 1 - \beta P$, $P(a) = (a \cdot e_{t})\,e_{r}$, the derived metric is $ds^{2} = dT^{2} - (dr + \beta\,dT)^{2} - r^{2}(d\vartheta^{2} + \sin^{2}\vartheta\,d\varphi^{2})$ with $\beta^{2} = 2M/r$, and $\hb$ is invertible through the horizon. \emph{Provenance:} the connection and curvature forms \cite[App.~A.2]{ButlerT5}; the pair, the sign of the square and the matching \cite[Thm.~6.1, Prop.~7.21(3)]{ButlerT5}; the Painlev\'e-Gullstrand form \cite[App.~A.1]{ButlerT5}; the flag bit \cite[Def.~2.10, Prop.~5.1]{ButlerT14}.

## technical
For the Schwarzschild field on flat spacetime in the static gauge, with static orthonormal coframe $\theta^0 = \sqrt f\,dt$, $\theta^1 = dr/\sqrt f$, $\theta^2 = r\,d\vartheta$, $\theta^3 = r\sin\vartheta\,d\varphi$ and $f = 1 - 2M/r$, the rotation-gauge field read as connection forms is $\omega^0{}_1 = (f'/2\sqrt f)\,\theta^0$, $\omega^2{}_1 = (\sqrt f/r)\,\theta^2$, $\omega^3{}_1 = (\sqrt f/r)\,\theta^3$ and $\omega^3{}_2 = (\cot\vartheta/r)\,\theta^3$. The curvature operator $\mathcal{R}(B)$ is diagonal on the coordinate planes, with eigenvalue $2M/r^3$ on the radial plane and the angular plane and $-M/r^3$ on the four mixed planes.

The extreme eigenvalue picks out the pair $\{\sigma_r, I\sigma_r\}$ invariantly, and the sign of the square, $\sigma_r^2 = +1$ against $(I\sigma_r)^2 = -1$, selects the radial member; which null direction of the radial plane is the vacuum's is the flag bit, taken as initial data. In the Painlev\'e-Gullstrand gauge $\hb = 1 - \beta P$ the derived metric is $ds^2 = dT^2 - (dr + \beta\,dT)^2 - r^2(d\vartheta^2 + \sin^2\vartheta\,d\varphi^2)$ with $\beta^2 = 2M/r$, and the gauge field is invertible through the horizon.

## lay
This records the standard formulas for the gravitational field of a non-rotating black hole, described as two gauge fields on flat spacetime: how frames turn from point to point, and the field strength that plays the part of curvature, written in a frame adapted to the radius. One pair of planes, the radial one and its dual, carries the strongest field strength, which singles it out without any choice of coordinates. A second gauge, built on the clocks of infalling observers, shows that nothing goes wrong at the horizon.

## one-liner
In the static frame the curvature operator $\mathcal{R}(B)$ of the Schwarzschild field is diagonal, $2M/r^3$ on the radial and angular planes and $-M/r^3$ on the mixed ones, singling out the radial plane and its dual.
