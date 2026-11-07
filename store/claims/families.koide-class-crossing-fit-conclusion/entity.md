---
id: families.koide-class-crossing-fit-conclusion
kind: claim
version: 3
title: 'Koide in the class: the crossing, and the fit conclusion'
status: proved
region: families
subject: generations
tags: [flavour-and-mixing, refutation]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
review: typed
derivations:
- name: main
  uses:
  - families.skeleton-rank-one-plus-ordering-shift@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T13.py
  tags:
  - label:prop:crossing
- kind: check
  ref: check.py::check_s2_reduction_and_the_root
- kind: check
  ref: check.py::check_crossing_unique_and_bracketed
- kind: check
  ref: check.py::check_canonical_depth_fails
locators:
  paper: T13
  number: Prop 6.3
  label: prop:crossing
  line: 839
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the S_2 root 4 + 3 sqrt 2 and K = 2308 + 1632 sqrt 2 in Z[sqrt 2], the unique crossing bracketed at 769.3325, and the canonical depth ratio 13/2. Version 2 -> 3.'
  env: proposition
  eqrefs: 2
  typing:
    by: ai-typing-pass
    removed:
    - families.chart-computation-sign-twist-bracket-form
    added:
    - families.skeleton-rank-one-plus-ordering-shift
    note: "Removed the chart computation, used only as a cross-check of the root already obtained from the quadratic, and added the skeleton, whose spectrum supplies the crossing equation and whose unbreakable S2 makes the S2 point the only Koide-compatible configuration; doubt over whether the chart edge should stay as a second route."
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - families.skeleton-rank-one-plus-ordering-shift
---

## formal
Within the Gaussian class the only Koide-compatible configuration is the $S_{2}$-symmetric point (one heavy, two exactly degenerate light), where the relation reduces to a single ratio: $Q_{\sqrt{m}} = 2/3$ for the mass triple $(t, t, T)$ holds iff $\sqrt{T/t} = 4 + 3\sqrt{2}$, equivalently a heavy-to-light mass-squared ratio of $K = (4+3\sqrt{2})^{4} = 2308 + 1632\sqrt{2} \approx 4616$. In the model's variables the condition is
\begin{equation}
\frac{1 + 6x + 6x^{2}}{1 + x} \;=\; 6x + \frac{1}{1+x} \;=\; K,
\end{equation}
which the depth crosses exactly once, at $x^{*} = \sinh^{2}r^{*} = K/6 - 1/(6(1 + x^{*})) = 769.3325$, within $2.2 \times 10^{-4}$ of $K/6 = 769.3328$. The conclusion: the depth is not canonical; $x^{*}$ is $K/6$ up to the $1/(6(1+x))$ term because the skeleton's ratio is $6x$ at large depth, so the depth is Koide's own number transcribed by the spectrum of \eqref{eq:H}, and two parameters (depth and scale) against two observables is a reparametrisation, not a mechanism. \textbf{The mechanism stands as a fit; the derivation claim is refuted at this order.} The relation reverts, within the framework as it stands, to a measurement: of the freezing depth, at $10^{-5}$ precision.

## technical
In the Gaussian class the only Koide-compatible configuration is the $S_{2}$-symmetric point, one heavy and two exactly degenerate light masses $(t, t, T)$. There $Q_{\sqrt{m}} = \tfrac23$ holds if and only if $\sqrt{T/t} = 4 + 3\sqrt{2}$, a heavy-to-light mass-squared ratio $K = (4 + 3\sqrt{2})^{4} = 2308 + 1632\sqrt{2} \approx 4616$. With the skeleton's spectrum the ratio is $(1 + 6x + 6x^{2})/(1 + x) = 6x + 1/(1 + x)$ in $x = \sinh^{2}r$, strictly increasing, so it crosses $K$ exactly once, at $x^{*} = 769.3325$, within $2.2 \times 10^{-4}$ of $K/6$.

Because the ratio is $6x$ at large depth, $x^{*}$ is Koide's number transcribed, and two parameters (depth and scale) against two observables is a reparametrisation. The mechanism stands as a fit, the derivation claim is refuted at this order, and the relation becomes a measurement of the freezing depth.

## lay
Within the paper's simplest class of vacuum states, the Koide mass relation can only hold in a special symmetric case, and there it fixes one number, the ratio of the heavy mass to the light ones. The model can match that number by choosing its depth parameter, and it does so at exactly one value. But that value is essentially the Koide number rewritten, so the model fits the relation rather than explaining it. The attempted derivation is therefore recorded as refuted at this level, and the relation is treated as a measurement of the depth.

## one-liner
In the Gaussian class Koide holds only at the $S_{2}$ point, where the depth crosses the required ratio exactly once at $x^{*} \approx K/6 \approx 769.33$, so the mechanism is a fit and the derivation claim is refuted at this order.
