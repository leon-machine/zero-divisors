---
id: dark-matter.total-function-thickness
kind: claim
version: 5
title: The total as a function of the thickness
status: proved
region: dark-matter
subject: dark-matter
tags: [dark-matter-ratio, confronted-with-data, needs-continuum]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-matter.population-count-one-share-half-percent@6
  - dark-matter.projection-every-towers-content-dilutes-ones@3
  assumes:
  - dark-matter.p2-indifference@2
  - dark-matter.r1-equal-mass-per-quantum@1
  - dark-matter.r2-one-quantum-per-unit-ball@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_family_from_densities
- kind: check
  ref: check.py::check_exchange_symmetry
- kind: check
  ref: check.py::check_minimum
- kind: check
  ref: check.py::check_two_roots
- kind: check
  ref: check.py::check_windows
- kind: check
  ref: check.py::check_self_interacting_fraction
locators:
  paper: T14
  number: Prop 7.15
  label: prop:Tc
  line: 947
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.population-count-one-share-half-percent repinned 5 -> 6 after reviewing its C1 restatement (the share of one now rests also on the common-ceiling-coupling premise, with an assumes edge; the numbers are unchanged); the use here holds as cited.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: T(c) from the densities, the exchange symmetry, the minimum and floor, the two roots, the one- and two-sigma windows and the self-interacting fractions. Version 3 -> 4. Check strengthened: the three-dimensional fraction pinned to seven figures at c = 1, c* and pi/2. Version 4 -> 5.'
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.population-count-one-share-half-percent
    - dark-matter.projection-every-towers-content-dilutes-ones
    - dark-matter.p2-indifference
    - dark-matter.r1-equal-mass-per-quantum
    - dark-matter.r2-one-quantum-per-unit-ball
    note: 'The statement is under R1, R2 and the sourcing rule, and the sum it evaluates takes the mirror
      share one from the population count and the equal shares within each odd pair from P2, so those
      were added; the radiation audit is cited only for the self-interaction remark in (v). Levels pass:
      all three levels now name R1, R2 and P2, which the sum assumes.'
  env: proposition
  context_refs:
  - dark-matter.radiation-audit-what-theorem-closes-what
  eqrefs: 1
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.population-count-one-share-half-percent
    - dark-matter.projection-every-towers-content-dilutes-ones
    - dark-matter.p2-indifference
    - dark-matter.r1-equal-mass-per-quantum
    - dark-matter.r2-one-quantum-per-unit-ball
---

## formal
Let the five-dimensional towers' matter count through a length $c\,d_{b}$ of the extra direction and the three-dimensional towers' sheets be stacked $c\,d_{b}$ apart, with R1, R2 and the sourcing rule otherwise as before. Then
\[
T(c) \;:=\; \frac{\Omega_{\mathrm{dark}}}{\Omega_{b}} \;=\; 1 + \frac{8}{3c} + \frac{16c}{3\pi},
\]
and:
\begin{enumerate}
\item[(i)] $T(c) = T\!\left(\dfrac{\pi}{2c}\right)$ for every $c > 0$;
\item[(ii)] $T$ has a single minimum,
\[
c_{\ast} = \sqrt{\frac{\pi}{2}} = 1.2533, \qquad T_{\ast} = 1 + 2\sqrt{\frac{128}{9\pi}} = 5.2554,
\]
which is $1.7\sigma$ below the observed value; no thickness gives less;
\item[(iii)] $T(c) = 5.3643$ exactly at $c = 1$ and $c = \tfrac{\pi}{2}$, the two roots of one quadratic, with product $\tfrac{\pi}{2}$;
\item[(iv)] against $5.364 \pm 0.065$ the allowed thicknesses are $c \in [0.943, 1.086]$ or $c \in [1.447, 1.667]$ at one standard deviation, and the single interval $c \in [0.898, 1.750]$ at two;
\item[(v)] the three-dimensional fraction of dark matter, which self-interacts if that matter is at composite strength (Proposition \claimref{dark-matter.radiation-audit-what-theorem-closes-what}), is
\[
\frac{2 f_{3\mathrm{D}}}{T(c)} \;=\; \frac{8}{3c\,T(c)} : \qquad 49.7\% \text{ at } c = 1, \quad 40.5\% \text{ at } c_{\ast}, \quad 31.6\% \text{ at } c = \tfrac{\pi}{2}.
\]
\end{enumerate}

## technical
Let the five-dimensional towers' matter count through a length $c\,d_{b}$ of the extra direction and the three-dimensional towers' sheets be stacked $c\,d_{b}$ apart, assuming R1, R2 and the sourcing rule otherwise unchanged, with the mirror share one and, under P2, equal shares within each odd pair. Then $T(c) = \Omega_{\mathrm{dark}}/\Omega_{b} = 1 + \frac{8}{3c} + \frac{16c}{3\pi}$, which satisfies $T(c) = T(\pi/2c)$ and has a single minimum $T_{*} = 1 + 2\sqrt{128/9\pi} = 5.2554$ at $c_{*} = \sqrt{\pi/2}$, $1.7\sigma$ below the observed value.

$T(c) = 5.3643$ exactly at $c = 1$ and $c = \frac{\pi}{2}$, the two roots of one quadratic with product $\frac{\pi}{2}$. Against $5.364 \pm 0.065$ the allowed thicknesses are $c \in [0.943, 1.086]$ or $c \in [1.447, 1.667]$ at one standard deviation, and $[0.898, 1.750]$ at two; the three-dimensional fraction of dark matter is $8/(3c\,T(c))$, about $50\%$ at $c = 1$.

## lay
Under the paper's counting rules (equal mass per quantum, R1, and one quantum per unit ball, R2) and its indifference premise P2, the dark matter formula has one adjustable length: how deep into an extra dimension hidden matter counts towards our gravity. This result maps how the predicted total changes with that length. The total can never fall below about 5.26 times ordinary matter, and it matches the observed 5.36 at exactly two values of the length.

## one-liner
Under R1, R2 and P2, with thickness $c\,d_{b}$ the dark-to-baryon ratio is $T(c) = 1 + 8/3c + 16c/3\pi$, minimal at $c = \sqrt{\pi/2}$ and equal to $5.3643$ at $c = 1$ and $c = \pi/2$.
