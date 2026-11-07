---
id: odd-extensions.boost-dilation-ratio-gauge
kind: claim
version: 3
title: The boost is the dilation; the ratio $b/a$ is gauge
status: proved
region: odd-extensions
subject: conformal-spacetime
tags: [frozen-point, rotors-and-stabilisers, cosmological-constant]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14a, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-energy.point-infinity-has-no-physical-fluctuation@4
  - odd-extensions.transport-constrains-frozen-point-only-through@3
  - std-algebra.orthogonal-anticommute@1
  - std-algebra.bivector-exponential@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_bivector_is_the_dilation_generator
- kind: check
  ref: check.py::check_rotor_scales_the_null_pair
- kind: check
  ref: check.py::check_ratio_is_gauge_and_product_invariant
locators:
  paper: T14a
  number: Prop 9.2
  label: prop:dilation
  line: 698
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.orthogonal-anticommute, std-algebra.bivector-exponential where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: B = -e_+e_- squares to 1 and commutes with the Lorentz frame, rational rotors scale I by t and phi by 1/t, and frozen points of equal norm are joined by a rotor. Version 1 -> 2.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'Both uses are cited in the proof of clause (iii) and kept; no context references or repairs
      to review. Levels pass: conditions already kept.'
---

## formal
In the rung, with the canonical null frame realised as $I = (e_{+} + e_{-})/2$, $\varphi = e_{+} - e_{-}$ in the hyperbolic plane orthogonal to the Lorentz frame:
\begin{enumerate}
\item[(i)] the bivector $B = I \wedge \varphi = -e_{+}e_{-}$ squares to $+1$, commutes with every Lorentz bivector and with every Lorentz vector, and anticommutes with $e_{\pm}$: it is the generator of the dilations of the conformal model;
\item[(ii)] the rotor $R = \cosh\theta + B\sinh\theta$ fixes the Lorentz frame and acts on the plane by $I \mapsto tI$, $\varphi \mapsto \varphi/t$ with $t = e^{2\theta}$, so the boosts of Theorem \claimref{odd-extensions.transport-constrains-frozen-point-only-through}(iii) are the dilations;
\item[(iii)] hence the ratio $b/a$ of the frozen point's components is a dilation gauge and only the product $2ab = \Lambda/3$ is invariant, and by Fact \claimref{dark-energy.point-infinity-has-no-physical-fluctuation} the gauge is not fixed by the dynamics either: the components are unphysical, not merely symmetry-related, and the frame the transport supplies carries no quantity beyond $\Lambda$ itself.
\end{enumerate}

## technical
In the hyperbolic plane orthogonal to the Lorentz frame take $I = (e_+ + e_-)/2$ and $\varphi = e_+ - e_-$. The bivector $B = I \wedge \varphi = -e_+e_-$ satisfies $B^2 = +1$, commutes with every Lorentz vector and bivector, and anticommutes with $e_\pm$, so it generates the dilations of the conformal model. The rotor $R = \cosh\theta + B\sinh\theta$ fixes the Lorentz frame and acts by $I \mapsto tI$, $\varphi \mapsto \varphi/t$ with $t = e^{2\theta}$, so the boosts that move the frozen point are dilations.

Hence the ratio $b/a$ of the frozen point's components is a dilation gauge and only $2ab = \Lambda/3$ is invariant. Since the point at infinity has no physical fluctuation, the dynamics does not fix this gauge either, and the frame that the transport supplies carries no quantity beyond $\Lambda$.

## lay
The frozen point is described by two numbers, but a change of overall scale (a dilation) can trade one for the other while keeping their product fixed. This result shows that the freedom the transport leaves is exactly such a change of scale. So only the product, which is set by the cosmological constant, has physical meaning.

## one-liner
The boosts that move the frozen point are the conformal dilations, so the ratio $b/a$ is pure gauge and only $2ab = \Lambda/3$ is physical.
