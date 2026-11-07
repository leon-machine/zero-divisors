---
id: sheaf.weighted-limit
kind: claim
version: 7
title: The weighted limit
status: proved
region: sheaf
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
  source: authorship disclosure of T04, deposited version
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
  - interior.boosts-generate-exactly-levi-factor@5
  - interior.exact-parallelism-convergence-rate@6
  - interior.interior-connection-exactly@8
  - interior.kasner-form-interior@6
  - interior.weighted-limit-theorem@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_synchronous_derived_metric_and_tau
- kind: check
  ref: check.py::check_frame_parallel_and_connection_shape
- kind: check
  ref: check.py::check_hubble_normalised_rates
- kind: check
  ref: check.py::check_weighted_limit_and_values_level_holonomy
locators:
  paper: T04
  number: Fact 8.25
  label: fact:weightedlimit
  line: 1131
extraction:
  maintainer_pass_decisions_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Notation (Leon, second round, answer 8; DECISIONS H5, consistency-R03 C): the derived line element wrote the round two-sphere as d Omega^2 beside Omega the rotation-gauge field of the gravitational field (hb, Omega). It is now written (d theta^2 + sin^2 theta d varphi^2), the angles of the frame adapted to (t, theta, varphi) that the entity already names. No content change.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: interior gauge field: derived metric, tau series, D-parallel frame and connection shape, Hubble-normalised rates by exact series; Kasner member and values-level holonomy so(1,3) over a grid. Version 4 -> 5. Proof: the Hubble-normalised connection displayed in the GTG sign, -sum p_i B_i (one sentence missed by the earlier re-sign). Version 5 -> 6.'
  typing:
    by: ai-typing-pass
    added: [interior.exact-parallelism-convergence-rate, interior.interior-connection-exactly]
    note: 'Fact restating the interior paper: added the parallel-frame and interior-connection lemmas, whose content (exact parallelism, rates, connection on unit directions) it restates and its provenance names.'
  env: fact
  context_refs:
  - interior.boosts-generate-exactly-levi-factor
  - interior.kasner-form-interior
  - interior.weighted-limit-theorem
  flags:
  - 'fact restating several series results: derived from them'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - interior.kasner-form-interior
    - interior.exact-parallelism-convergence-rate
    - interior.interior-connection-exactly
    - interior.boosts-generate-exactly-levi-factor
    - interior.weighted-limit-theorem
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the Schwarzschild interior is the gravitational field (hb, Omega) on flat spacetime with synchronous derived metric; the frame is D-parallel along the free-fall worldlines; the connection is the rotation-gauge field; admissible synchronous metric becomes admissible gravitational field in synchronous gauge (Einstein: R(a) = Lambda a, store sign). Series, limit and holonomy unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact. Fix (Leon 2026-10-23, referee GR1): displayed connection values re-signed to the GTG sign of the definition, D_a = a.nabla + Omega(a) x (Cartan forms omega^i_0 = sigma_i theta^i assemble to -sigma_i B_i; Hubble-normalised Kasner model -sum_i p_i B_i, DICTIONARY C10); content unchanged.'
---

## formal
For the Schwarzschild interior gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with $2M = 1$: in synchronous gauge the derived metric is $d\tau^2 - A\,dt^2 - r^2(d\theta^{2} + \sin^{2}\theta\,d\varphi^{2})$, $A = (1-r)/r$, with $\tau = \tfrac23 r^{3/2}(1 + \tfrac{3}{10}r + O(r^2))$; the orthonormal physical frame adapted to $(t, \theta, \varphi)$ is exactly $D$-parallel along the free-fall worldlines of velocity $g_\tau$; its Hubble-normalised expansion rates are $\tau\sigma_1 = -\tfrac13 - \tfrac{4}{15}R + O(R^2)$ and $\tau\sigma_2 = \tau\sigma_3 = \tfrac23 - \tfrac{2}{15}R + O(R^2)$, $R = (3\tau/2)^{2/3}$; the rotation-gauge field on unit tangential directions is $\Omega(e_i) = -\sigma_i B_i$ plus a sphere term of size $O(1/r)$, with $B_i$ the boosts (the sign of the Definition, in which the Cartan forms $\omega^i{}_0 = \sigma_i\theta^i$ assemble to $-\sigma_i B_i$); and for every admissible gravitational field in synchronous gauge (Einstein, $\mathcal{R}(a) = \Lambda a$ in the store's sign, so $\mathrm{Ric} = \Lambda g$ for the derived metric, with $\Lambda$ constant; Hubble-normalised connection $-\sum_i p_iB_i \otimes \hat\theta^i + E_\tau$ with \emph{constant} $p_i \neq 0$, $E_\tau \to 0$, and $\|E_\tau\|/\tau$ integrable, both locally uniformly on the boundary base) the weighted limit exists, equals $\widehat\Omega_0 = -\sum_i p_i B_i \otimes \hat\theta^i$, extends the parallel tractor, and has boundary holonomy exactly $\mathfrak{so}(1,3)$ in the values-level sense of \cite[Def.~5.5]{ButlerT6} (the algebra generated by the limiting connection values). \emph{Provenance:} \cite{ButlerT6}, Lemmas 5.1-5.4, Definition 5.5, and Theorem 5.6.

## technical
For the Schwarzschild interior gravitational field on flat spacetime ($2M = 1$) the derived metric is synchronous, $d\tau^2 - A\,dt^2 - r^2(d\theta^{2} + \sin^{2}\theta\,d\varphi^{2})$ with $A = (1 - r)/r$ and $\tau = \tfrac23 r^{3/2}(1 + \tfrac{3}{10}r + O(r^2))$; the adapted physical frame is exactly $D$-parallel along the free-fall worldlines; the Hubble-normalised rates are $\tau\sigma_1 = -\tfrac13 - \tfrac{4}{15}R + O(R^2)$ and $\tau\sigma_2 = \tau\sigma_3 = \tfrac23 - \tfrac{2}{15}R + O(R^2)$, with $R = (3\tau/2)^{2/3}$; and the rotation-gauge field on unit tangential directions is $-\sigma_i B_i$ plus a sphere term of size $O(1/r)$.

For every admissible gravitational field in synchronous gauge (Einstein, with Hubble-normalised connection $-\sum_i p_i B_i \otimes \hat\theta^i + E_\tau$ for constant $p_i \neq 0$, $E_\tau \to 0$ and $\|E_\tau\|/\tau$ integrable, locally uniformly) the weighted limit exists, equals $\widehat\Omega_0 = -\sum_i p_i B_i \otimes \hat\theta^i$, extends the parallel tractor, and has values-level boundary holonomy exactly $\mathfrak{so}(1,3)$. The statement collects results proved in the series' treatment of the interior.

## lay
This collected result summarises what the series proved about the centre of a non-rotating black hole. The gravitational field there approaches a Kasner pattern at explicit rates, and the clock-rescaled rules for carrying directions settle to a simple limit. That limit holds for a whole class of similar singularities, and the algebra it generates is the Lorentz algebra.

## one-liner
For Schwarzschild, with explicit rates, and for every admissible gravitational field in synchronous gauge, the weighted limit exists, equals $-\sum_i p_i B_i \otimes \hat\theta^i$, extends the parallel tractor and has boundary holonomy exactly $\mathfrak{so}(1,3)$.
