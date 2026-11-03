---
id: interior.exact-parallelism-convergence-rate
kind: claim
version: 5
title: Exact parallelism, and the convergence rate
status: proved
region: interior
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
  source: authorship disclosure of T06, deposited version
review: typed
about:
- obj.interior.weighted-blow-up-hubble-normalisation-admissible
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - interior.kasner-form-interior@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T06.py
  tags:
  - num:5.2
- kind: check
  ref: check.py::check_frame_exactly_parallel
- kind: check
  ref: check.py::check_rates_converge_to_kasner_exponents
- kind: check
  ref: check.py::check_one_uniform_rate
locators:
  paper: T06
  number: Lem 5.2
  label: lem:parallel
  line: 612
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: exact D-parallelism of the interior frame from the GTG gauge fields, the rate constants -1/3 - 4/15 R and 2/3 - 2/15 R, and one O(tau^{2/3}) rate for every deviation. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  typing:
    by: ai-typing-pass
    note: 'The interior-connection lemma in context_refs is only a pointer for the separate rotation rate and is not used by the proof, so it was not added (it would also close a cycle with that lemma, which is set in this frame).'
  env: lemma
  context_refs:
  - interior.interior-connection-exactly
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the frame is the normalised physical frame g_mu = hb^{-1}(e_mu) of the interior gravitational field, parallel transport is D-parallel transport, the geodesics are worldlines of D-parallel velocity, and the Kasner comparison is of the field read through its derived metric. Rates and constants unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact.'
---

## formal
For the Schwarzschild interior field $(\hb, \Omega)$ on flat spacetime in the synchronous gauge of Lemma \claimref{interior.kasner-form-interior}, with physical frame $g_\mu = \hb^{-1}(e_\mu)$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), let $e_0 := g_\tau$ and let $(e_1, e_2, e_3)$ be the orthonormal frame obtained by normalising the physical vectors $(g_t, g_\theta, g_\varphi)$. Then:
\begin{enumerate}
\item the frame is \emph{exactly} $D$-parallel along the free-fall worldlines of velocity $g_\tau$ (the geodesics of the derived metric), at every $\tau > 0$: parallel transport into the singularity is not an asymptotic question for the frame;
\item with $\sigma_1 := \partial_\tau \log \sqrt{A}$ and $\sigma_2 = \sigma_3 := \partial_\tau \log r$ the Hubble-normalised expansion rates, in units $2M = 1$,
\[
\tau\sigma_1 \;=\; -\tfrac13 - \tfrac{4}{15}R + O(R^2),
\qquad
\tau\sigma_2 \;=\; \tau\sigma_3 \;=\; \tfrac23 - \tfrac{2}{15}R + O(R^2),
\]
so the rates converge to the Kasner exponents at the rate $O(\tau^{2/3})$, with explicit leading constants;
\item every relative deviation of the interior field, read through its derived metric, from the exact Kasner model with these exponents (scale factors, the diagonal expansion rates $\sigma_i$, and the curvature of the $S^2$ sections measured against the dominant scale $\tau^{-2}$) is $O(\tau^{2/3})$: the approach is velocity-dominated with one uniform power-law rate, each deviation one-signed near the singularity, with no oscillations; the sphere's rotation coefficient lies outside the Kasner comparison and carries the separate Hubble-normalised rate $O(\tau^{1/3})$ (Lemma \claimref{interior.interior-connection-exactly}, Definition \claimref{obj.interior.weighted-blow-up-hubble-normalisation-admissible}).
\end{enumerate}

## technical
For the Schwarzschild interior gravitational field on flat spacetime in synchronous gauge, let $e_0 = g_\tau$ and let $(e_1, e_2, e_3)$ be the normalised physical frame vectors $(g_t, g_\theta, g_\varphi)$, $g_\mu = \hb^{-1}(e_\mu)$. This frame is exactly parallel for the covariant derivative $D$ along the free-fall worldlines of velocity $g_\tau$ at every $\tau > 0$, so parallel transport into the singularity is not an asymptotic question for the frame. With $\sigma_1 = \partial_\tau\log\sqrt A$ and $\sigma_2 = \sigma_3 = \partial_\tau\log r$, in units $2M = 1$, the Hubble-normalised rates are $\tau\sigma_1 = -\tfrac13 - \tfrac{4}{15}R + O(R^2)$ and $\tau\sigma_2 = \tau\sigma_3 = \tfrac23 - \tfrac{2}{15}R + O(R^2)$, with $R = (3\tau/2)^{2/3}$, so they reach the Kasner exponents at rate $O(\tau^{2/3})$.

Every relative deviation from the exact Kasner model (scale factors, expansion rates, and the curvature of the spheres against the dominant scale $\tau^{-2}$) is $O(\tau^{2/3})$ and one-signed near the singularity: the approach is velocity-dominated with one power-law rate and no oscillation. The sphere's rotation coefficient lies outside this comparison and has the separate Hubble-normalised rate $O(\tau^{1/3})$.

## lay
Inside a non-rotating black hole, an observer falling towards the centre can carry a set of reference directions along. This result shows that a natural choice of such directions is carried along perfectly, with no drift at all, right up to the singularity. It also gives the exact rate at which the stretching and squeezing of space approach the idealised Kasner pattern, and shows that the approach is smooth, without oscillation.

## one-liner
In the Schwarzschild interior the adapted physical frame is exactly $D$-parallel along the infalling free-fall worldlines, and the Hubble-normalised expansion rates reach the Kasner exponents $(-\tfrac13, \tfrac23, \tfrac23)$ at the single, non-oscillating rate $O(\tau^{2/3})$.
