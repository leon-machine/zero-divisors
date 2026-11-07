---
id: singularity.imported-interior-collar-kasner-form
kind: claim
version: 7
title: 'Imported: the interior collar in Kasner form'
status: proved
region: singularity
subject: interior
tags: [schwarzschild, kasner, limits]
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
  role: 'notation: d Omega^2 written as the explicit round metric'
  version: 7
  source: maintainer pass 2026-11-07 (decisions, second round)
review: typed
about:
- obj.interior.weighted-blow-up-hubble-normalisation-admissible
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - interior.exact-parallelism-convergence-rate@6
  - interior.interior-connection-exactly@8
  - interior.kasner-form-interior@7
  - interior.weighted-limit-theorem@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_derived_metric_and_tau
- kind: check
  ref: check.py::check_parallel_frame_and_t_line_connection
- kind: check
  ref: check.py::check_rates_and_kasner_limits
- kind: check
  ref: check.py::check_limiting_boosts_generate_so13
locators:
  paper: T05
  number: Fact 13.1
  label: fact:collar
  line: 2439
extraction:
  maintainer_pass_decisions_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Notation (Leon, second round, answer 8; DECISIONS H5, consistency-R03 C): the derived line element wrote the round two-sphere as d Omega^2 beside Omega the rotation-gauge field of the gravitational field (hb, Omega). It is now written (d theta^2 + sin^2 theta d varphi^2), the angles of the frame adapted to (t, theta, varphi) that the entity already names. No content change.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: interior gauge field: derived metric, tau series, D-parallel frame, sigma_1 on the (t,r) boost, rates and Kasner limits by exact series, the three boosts generate so(1,3). Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6.'
  typing:
    by: ai-typing-pass
    added: [interior.exact-parallelism-convergence-rate]
    note: 'Added the parallel-frame lemma, whose parallelism and rates the fact restates; the source calls only the exponents classical and the imported Kasner claim covers just those, so no standard-route was added.'
  env: fact
  context_refs:
  - interior.interior-connection-exactly
  - interior.kasner-form-interior
  - interior.weighted-limit-theorem
  flags:
  - 'fact restating several series results: derived from them'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the Schwarzschild interior is the gravitational field (hb, Omega) on flat spacetime with synchronous derived metric; the frame is the physical frame, D-parallel along the free-fall worldlines; the Levi-Civita connection is the rotation-gauge field. Series, limits, algebra and exceptional set unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact. Fix (Leon 2026-10-23, referee GR1): displayed connection values re-signed to the GTG sign of the definition, D_a = a.nabla + Omega(a) x (Cartan forms omega^i_0 = sigma_i theta^i assemble to -sigma_i B_i; Hubble-normalised Kasner model -sum_i p_i B_i, DICTIONARY C10); content unchanged.'
---

## formal
In units $2M = 1$ the Schwarzschild interior gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), in synchronous gauge, has derived metric $d\tau^2 - A\,dt^2 - r^2(d\theta^{2} + \sin^{2}\theta\,d\varphi^{2})$ with $A = 1/r - 1$ and $\tau = \tfrac23 r^{3/2}(1 + \tfrac{3}{10}r + O(r^2))$; the orthonormal physical frame $(e_0, e_1, e_2, e_3)$, $e_0 = g_\tau$, adapted to $(t, \theta, \varphi)$ is exactly $D$-parallel along the free-fall worldlines of velocity $g_\tau$; the rotation-gauge field on the unit direction $e_1$ along a $t$-line is $-\sigma_1 B_1$ with $\sigma_1 = \partial_\tau \log\sqrt{A}$ and $B_1 = e_0 \wedge e_1$ the boost of the $(t, r)$ plane; the Hubble-normalised rates are $\tau\sigma_1 = -\tfrac13 - \tfrac{4}{15}R + O(R^2)$ and $\tau\sigma_2 = \tau\sigma_3 = \tfrac23 - \tfrac{2}{15}R + O(R^2)$ with $R = (3\tau/2)^{2/3}$, whose limits are the Kasner exponents $(p_1, p_2, p_3) = (-\tfrac13, \tfrac23, \tfrac23)$; the three limiting boosts $B_i$ generate $\mathfrak{so}(1,3)$ and do not commute; and the exceptional set of the weighted blow-up is $\{\tau = 0\} \times \R_t \times S^2$. \emph{Provenance:} \cite[Lemmas 5.1 to 5.3, Def.~5.5, Thm.~5.6]{ButlerT6}; the exponents are classical.

## technical
In units $2M = 1$ the Schwarzschild interior gravitational field on flat spacetime has, in synchronous gauge, derived metric $d\tau^2 - A\,dt^2 - r^2(d\theta^{2} + \sin^{2}\theta\,d\varphi^{2})$ with $A = 1/r - 1$ and $\tau = \tfrac23 r^{3/2}(1 + \tfrac{3}{10}r + O(r^2))$. The physical frame adapted to $(t, \theta, \varphi)$ is exactly $D$-parallel along the free-fall worldlines; the rotation-gauge field on the unit direction $e_1$ along a $t$-line is $-\sigma_1 B_1$ with $\sigma_1 = \partial_\tau\log\sqrt A$ and $B_1$ the boost of the $(t, r)$ plane; and the Hubble-normalised rates $\tau\sigma_1 = -\tfrac13 - \tfrac{4}{15}R + O(R^2)$ and $\tau\sigma_2 = \tau\sigma_3 = \tfrac23 - \tfrac{2}{15}R + O(R^2)$ tend to the Kasner exponents $(-\tfrac13, \tfrac23, \tfrac23)$.

The three limiting boosts generate $\mathfrak{so}(1,3)$ and do not commute, and the exceptional set of the weighted blow-up is $\{\tau = 0\} \times \R_t \times S^2$. The statement collects results proved earlier in the series; the exponents are classical.

## lay
This collected result recalls the description of the region just outside the singularity of a non-rotating black hole: a Kasner-like collar in which one direction stretches and two shrink at fixed powers of time. It also records that the limiting stretchings do not commute with one another and together generate the full Lorentz algebra. The singular boundary itself is a line times a sphere.

## one-liner
The Schwarzschild interior collar has synchronous derived metric and an exactly $D$-parallel adapted physical frame, its Hubble-normalised rates tend to the Kasner exponents $(-\tfrac13, \tfrac23, \tfrac23)$, the limiting boosts generate $\mathfrak{so}(1,3)$, and the exceptional set is $\{\tau = 0\} \times \R_t \times S^2$.
