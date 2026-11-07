---
id: interior.schwarzschild-lines-exactly
kind: claim
version: 5
title: The Schwarzschild $\varphi$-lines, exactly
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
derivations:
- name: main
  uses:
  - interior.exact-parallelism-convergence-rate@6
  - interior.interior-connection-exactly@8
  - interior.kasner-form-interior@6
  - interior.transport-level-convergence-along-tangential-curves@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T06.py
  tags:
  - num:5.12
- kind: check
  ref: check.py::check_phi_line_generator_constant
- kind: check
  ref: check.py::check_delta_epsilon_series
- kind: check
  ref: check.py::check_exponential_comparison
- kind: check
  ref: check.py::check_rates_in_tau
locators:
  paper: T06
  number: Cor 5.12
  label: cor:phi
  line: 749
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the phi-line generator constant from the GTG gauge fields, the delta and epsilon series, the exponential comparison identity with the norm bound, and the rates. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Gauge Theory Gravity sign: the generator is displayed with the connection bivector in the GTG sign, G = -(2/3 + delta) B_3 + epsilon R_23 (B_3 = e_0 ^ e_3, R_23 = e_2 ^ e_3), the Hubble-normalised value of Omega(e_3) of the interior connection Lemma, and the model transport is exp(-(2/3) lambda B_3), at formal and technical; norms, series, bound and rates unchanged. Version kept at 4 (raised today with the check); the proof already reads in GTG.'
  typing:
    by: ai-typing-pass
    note: 'All four uses are premises: constancy of the generator, the series and rates, the parallel frame in the symmetry argument, and the constant-generator case of the general transport bound.'
  env: corollary
---

## formal
For the Schwarzschild interior in units $2M = 1$, along a $\varphi$-coordinate line at fixed $(r, \theta)$ the Hubble-normalised generator is constant along the line,
\begin{align*}
G \;&=\; -\bigl(\tfrac23 + \delta(r)\bigr) B_{3} + \varepsilon(r)\, R_{23}, \\
\delta(r) \;&=\; \tau\sigma_{3} - \tfrac23 \;=\; -\tfrac{2}{15}\,r - \tfrac{8}{105}\,r^{2} - \tfrac{16}{315}\,r^{3} - \cdots, \\
\varepsilon(r) \;&=\; \frac{\tau\cot\theta}{r} \;=\; \tfrac23\cot\theta\; r^{1/2}\bigl(1 + \tfrac{3}{10} r + \tfrac{9}{56} r^{2} + \cdots\bigr),
\end{align*}
so the transport over a segment of Hubble-normalised length $\lambda$ is the single exponential $\exp(\lambda G)$, the model transport is $\exp(-\tfrac23\lambda B_{3})$, and
\[
\|\exp(\lambda G) - \exp(-\tfrac23\lambda B_{3})\| \;\le\; \lambda\,(|\delta(r)| + |\varepsilon(r)|)\,e^{\lambda(1 + |\delta| + |\varepsilon|)} \;=\; O(r^{1/2}) \;=\; O(\tau^{1/3}) .
\]
The rate is $\tau^{1/3}$, slower than the $\theta$-line's $\tau^{2/3}$, and it is the sphere's intrinsic connection that sets it. Along all tangential curves of fixed Hubble-normalised length the bound of Theorem \claimref{interior.transport-level-convergence-along-tangential-curves} applies with $\|E_{\tau}\|_{K} = O(\tau^{1/3})$ away from the poles. The tangential regularity of the boundary data on the exceptional set holds by symmetry: the data are $SO(3) \times \R_{t}$-invariant, hence constant along $\mathcal{B}$ in an invariant frame and smooth in any patch.

## technical
Along a $\varphi$-coordinate line at fixed $(r, \theta)$ in the Schwarzschild interior ($2M = 1$), the Hubble-normalised generator is constant, $G = -(\tfrac23 + \delta(r))B_3 + \varepsilon(r)R_{23}$, with $\delta(r) = \tau\sigma_3 - \tfrac23 = -\tfrac{2}{15}r + O(r^2)$ and $\varepsilon(r) = \tau\cot\theta/r = \tfrac23\cot\theta\,r^{1/2}(1 + O(r))$. The transport over Hubble-normalised length $\lambda$ is therefore $\exp(\lambda G)$, the model transport is $\exp(-\tfrac23\lambda B_3)$, and their distance is at most $\lambda(|\delta| + |\varepsilon|)e^{\lambda(1 + |\delta| + |\varepsilon|)} = O(\tau^{1/3})$.

The rate $\tau^{1/3}$ is slower than the $\theta$-line's $\tau^{2/3}$ and is set by the sphere's intrinsic connection. Along all tangential curves of fixed Hubble-normalised length the general transport bound applies with $\|E_\tau\|_K = O(\tau^{1/3})$ away from the poles, and the boundary data are tangentially regular on the exceptional set by the $SO(3) \times \R_t$ symmetry.

## lay
Moving around a circle of latitude inside a non-rotating black hole, the twisting of directions is the same at every step, so it can be computed exactly. The result compares it with the idealised Kasner model and finds that the two agree more and more closely near the centre. The agreement improves more slowly here than in other directions, because the curvature of the spheres themselves gets in the way.

## one-liner
Along the Schwarzschild $\varphi$-lines the Hubble-normalised transport is a single exponential and converges to the Kasner model's transport at the rate $O(\tau^{1/3})$, set by the sphere's intrinsic connection.
