---
id: mass.de-sitter-scale-frozen-point
kind: claim
version: 6
title: The de Sitter scale and its frozen point
status: proved
region: mass
subject: dark-energy
tags: [frozen-point, tractors, conformal-model]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - mass.imported-flat-model-twistor-chart-infinity@7
  - mass.imported-frozen-point-tractor-connection@6
  - mass.imported-thomas-operator@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T11.py
  tags:
  - label:lem:dsscale
- kind: check
  ref: check.py::check_scale_tractor_parallel_with_norm
- kind: check
  ref: check.py::check_gauge_field_sigma_is_de_sitter
- kind: check
  ref: check.py::check_frozen_point_unique_constant_vector
- kind: check
  ref: check.py::check_frozen_point_norm_and_null_limit
locators:
  paper: T11
  number: Lem 5.1
  label: lem:dsscale
  line: 575
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the scale tractor of sigma = 1 - Lambda Q/12 is parallel with norm Lambda/3; from the gauge fields hb = sigma, Omega = -(a ^ grad sigma)/sigma (torsion-free, unique) the store curvature is (Lambda/3) B; the unique constant vector with scale function sigma is n_inf + (Lambda/6) n_0. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5. Sample inputs moved to module level; no change to what is tested (frame loops range over len(g) and its pairs; the rank-invariant commutator normalisation moved to a module helper). Version 5 -> 6.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the flat chart is the flat background itself, eta its fixed product, and de Sitter space is the gravitational field hb = sigma (hb^{-1}(a) = a/sigma) on flat spacetime whose derived metric is sigma^{-2} eta; tractors are the Cl(2,4) vectors sigma ninf + mu + rho n0. The tractor theorem is not cited here, since it rests on this result. Proof prefixed.'
  typing:
    by: ai-typing-pass
    removed: [correspondence.one-statement-three-languages]
    note: 'Removed the twistor-correspondence corollary: the proof cites it only as the general statement behind clause (3) and does the chart computation itself, so it is context, not a premise; this also removes the reported E204 cause.'
  env: lemma
  eqrefs: 3
  source_title: 'The de Sitter scale and its frozen point'
  source_formal: |-
    Let $\eta$ be the flat metric on the chart of Fact \claimref{mass.imported-flat-model-twistor-chart-infinity}, $Q(x) = \eta(x,x)$, and $\sigma(x) := 1 - \Lambda Q(x)/12$.
    \begin{enumerate}
    \item The scale tractor of $\sigma$ in the flat scale is
    \[
    I_{\sigma} = \bigl(\sigma,\; \nabla\sigma,\; -\tfrac14\Box\sigma\bigr) = \Bigl(1 - \frac{\Lambda Q}{12},\; -\frac{\Lambda}{6}\,x_{a},\; \frac{\Lambda}{6}\Bigr),
    \]
    it is parallel for the connection \eqref{eq:tractorconn} of $\eta$, and $\ip{I_{\sigma}}{I_{\sigma}} = \Lambda/3$ identically. Hence $g = \sigma^{-2}\eta$ is Einstein with cosmological constant $\Lambda$, on the region $\sigma \neq 0$: it is de Sitter space in the flat conformal chart, and $I_{\sigma}$ is its frozen point.
    \item The constant ambient vector whose scale function is $\sigma$ is
    \[
    I_{\Lambda} := n_{\infty} + \frac{\Lambda}{6}\, n_{0},
    \]
    and it is the only one: $\ip{X(x)}{n_{\infty} + \lambda n_{0}} = 1 - \lambda Q(x)/2$, which equals $\sigma$ iff $\lambda = \Lambda/6$, and the points $X(x)$ span the ambient space. The vector $n_{0} + \lambda n_{\infty}$, of the same norm, has scale function $\lambda - Q/2$: the inverted chart, not this one.
    \item $\ip{I_{\Lambda}}{I_{\Lambda}} = 2 \cdot \tfrac{\Lambda}{6}\ip{n_{\infty}}{n_{0}} = \Lambda/3$, in agreement with (1). At $\Lambda = 0$, $I_{\Lambda} = n_{\infty}$: the frozen point of flat space is the infinity twistor, and it becomes non-simple exactly when $\Lambda \neq 0$.
    \end{enumerate}
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted the infinity twistor to the point at infinity $n_\infty$ of the conformal model, with simplicity read as a bivector through the Klein correspondence (kept, as conformal-model geometry), in the formal level, all levels and one sentence of the proof. The computation is unchanged.'
---

## formal
Let $\eta$ be the fixed product of flat spacetime, the chart of Fact \claimref{mass.imported-flat-model-twistor-chart-infinity}, $Q(x) = \eta(x,x)$, and $\sigma(x) := 1 - \Lambda Q(x)/12$; on the region $\sigma \neq 0$ let $(\hb, \Omega)$ be the gravitational field with $\hb(a) = \sigma\,a$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), whose derived metric is $g = \sigma^{-2}\eta$. Write tractors in the flat scale as the vectors $\sigma\,n_{\infty} + \mu + \rho\,n_{0}$ of $\Cl(2,4)$.
\begin{enumerate}
\item The scale tractor of $\sigma$ in the flat scale is
\[
I_{\sigma} = \bigl(\sigma,\; \nabla\sigma,\; -\tfrac14\Box\sigma\bigr) = \Bigl(1 - \frac{\Lambda Q}{12},\; -\frac{\Lambda}{6}\,x_{a},\; \frac{\Lambda}{6}\Bigr),
\]
it is parallel for the connection \eqref{eq:tractorconn} of $\eta$, and $\ip{I_{\sigma}}{I_{\sigma}} = \Lambda/3$ identically. Hence the derived metric $g = \sigma^{-2}\eta$ is Einstein with cosmological constant $\Lambda$, on the region $\sigma \neq 0$: the gravitational field $\hb = \sigma$ is de Sitter space on flat spacetime, and $I_{\sigma}$ is its frozen point.
\item The constant ambient vector whose scale function is $\sigma$ is
\[
I_{\Lambda} := n_{\infty} + \frac{\Lambda}{6}\, n_{0},
\]
and it is the only one: $\ip{X(x)}{n_{\infty} + \lambda n_{0}} = 1 - \lambda Q(x)/2$, which equals $\sigma$ iff $\lambda = \Lambda/6$, and the points $X(x)$ span the ambient space. The vector $n_{0} + \lambda n_{\infty}$, of the same norm, has scale function $\lambda - Q/2$: the inverted chart, not this one.
\item $\ip{I_{\Lambda}}{I_{\Lambda}} = 2 \cdot \tfrac{\Lambda}{6}\ip{n_{\infty}}{n_{0}} = \Lambda/3$, in agreement with (1). At $\Lambda = 0$, $I_{\Lambda} = n_{\infty}$: the frozen point of flat space is the point at infinity $n_{\infty}$ of the conformal model (the infinity twistor), and, read through the Klein correspondence as a bivector, it becomes non-simple exactly when $\Lambda \neq 0$.
\end{enumerate}

## technical
On flat spacetime with its fixed product $\eta$ and $Q(x) = \eta(x,x)$ set $\sigma = 1 - \Lambda Q(x)/12$, and take the gravitational field $\hb = \sigma$, whose derived metric is $\sigma^{-2}\eta$. The scale tractor of $\sigma$ in the flat scale, $I_\sigma = (\sigma, \nabla\sigma, -\tfrac14\Box\sigma) = (1 - \Lambda Q/12,\ -(\Lambda/6)x_a,\ \Lambda/6)$, is parallel for the flat tractor connection with squared norm $\Lambda/3$ identically, so $\sigma^{-2}\eta$ is Einstein with cosmological constant $\Lambda$ on $\sigma\neq 0$: the field $\hb = \sigma$ is de Sitter space on flat spacetime, with $I_\sigma$ its frozen point.

The unique constant ambient vector whose scale function is $\sigma$ is $I_\Lambda = n_\infty + (\Lambda/6)\,n_0$, since $\langle X(x), n_\infty + \lambda n_0\rangle = 1 - \lambda Q(x)/2$ and the points $X(x)$ span the ambient space; its squared norm is $\Lambda/3$. At $\Lambda = 0$ it is the point at infinity $n_\infty$ of the conformal model, and, read as a bivector through the Klein correspondence, it is non-simple exactly when $\Lambda\neq 0$.

## lay
De Sitter space, the universe with only a positive cosmological constant, needs no curved background: on ordinary flat spacetime it is a gravitational field that rescales every length by one simple function of position. This lemma finds the frozen point of that field and shows that it is a single fixed vector of the larger conformal space. When the cosmological constant is switched off, that vector becomes the familiar point at infinity of flat space's conformal model.

## one-liner
On flat spacetime de Sitter space is the gravitational field $\hb = \sigma$, $\sigma = 1 - \Lambda Q(x)/12$, with derived metric $\sigma^{-2}\eta$, and its frozen point is the unique constant vector $I_\Lambda = n_\infty + (\Lambda/6)n_0$, of squared norm $\Lambda/3$, which is the point at infinity $n_\infty$ at $\Lambda = 0$.
