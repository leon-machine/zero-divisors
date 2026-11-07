---
id: mass.weight-composite
kind: claim
version: 7
title: The weight of a composite
status: proved
region: mass
subject: mass
tags:
- conformal-spinors
- representation-theory
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 7
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  uses:
  - mass.exact-join@7
  - mass.weight-polynomial-two-series@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T11.py
  tags:
  - label:prop:weight
- kind: check
  ref: check.py::check_induced_weight_principal_series
- kind: check
  ref: check.py::check_real_weight_exactly_below_threshold
- kind: check
  ref: check.py::check_leading_order_im_w
locators:
  paper: T11
  number: Prop 5.9
  label: prop:weight
  line: 806
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The de Sitter weight -3/2 +- i nu, a physical number, is written -3/2 +- I_4 nu with numbers read in span{1, I_4}; no bare i remains.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: nu^2 = 6|B|^2/Lambda + C - 9/4 from the grip, the real-weight threshold, and Im w ~ sqrt 2 |B|/H at leading order. Version 4 -> 5. Check strengthened: leading-order regime pinned exactly (B and C scaling, closed form of the relative error from the grip, nonzero t^-2 coefficient) in place of loose thresholds; samples moved to module level. Version 5 -> 6.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - the de Sitter weight -3/2 +- i nu (a complex number labelling a principal-series representation,
      not an operator unit)
  env: proposition
  eqrefs: 1
  typing:
    by: ai-typing-pass
    added:
    - mass.exact-join
    note: 'The statement takes $m^{2}$ from the exact join''s formula and the proof substitutes it, so
      the exact join was added alongside the corollary. Levels pass: lay and one-liner now keep Lambda
      > 0; one-liner states the 3H/2 threshold and the leading-order regime instead of an unqualified
      heavy composite.'
  source_title: The weight of a composite
  source_formal: 'Let $\Lambda > 0$. Define the \emph{induced weight} of a composite of mass $m$ as the
    weight of a density with that mass under the dictionary, that is, a solution $w$ of $-w(w+3)H^{2}
    = m^{2}$. For the two-twistor composite with $m^{2}$ given by \eqref{eq:grip}:

    \begin{equation}

    w = -\frac32 \pm i\nu, \qquad \nu^{2} = \frac{6\,|B_{\Lambda}|^{2}}{\Lambda} + C - \frac94,

    \end{equation}

    the weight being real exactly when $6|B_{\Lambda}|^{2}/\Lambda + C \le \tfrac94$, and otherwise on
    the principal series with $\nu = m/H - \tfrac98 H/m + O((H/m)^{3})$. The real part is $-\tfrac32$
    for every composite heavier than $3H/2$; the mass lies in the imaginary part, and for $|B_{\Lambda}|
    \gg H\sqrt{C}$, which is the regime of every known particle when $C$ is of order one, $\mathrm{Im}\,w
    = \sqrt{2}\,|B_{\Lambda}|/H$ at leading order.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: The composite is now one of two conformal spinors. The i in the weight w = -3/2 +- i nu is the
      complex weight of a de Sitter density, not a twistor unit, and is kept.
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - mass.exact-join
about:
- obj.mass.grip-mass-composite
---

## formal
Let $\Lambda > 0$. Define the \emph{induced weight} of a composite of mass $m$ as the weight of a density with that mass under the dictionary, that is, a solution $w$ of $-w(w+3)H^{2} = m^{2}$. For the composite of two conformal spinors with $m^{2}$ given by \eqref{eq:grip}:
\begin{equation}
w = -\frac32 \pm I_4\nu, \qquad \nu^{2} = \frac{6\,|B_{\Lambda}|^{2}}{\Lambda} + C - \frac94,
\end{equation}
numbers being read in $\mathrm{span}\{1, I_4\}$, the weight being real exactly when $6|B_{\Lambda}|^{2}/\Lambda + C \le \tfrac94$, and otherwise on the principal series with $\nu = m/H - \tfrac98 H/m + O((H/m)^{3})$. The real part is $-\tfrac32$ for every composite heavier than $3H/2$; the mass lies in the imaginary part, and for $|B_{\Lambda}| \gg H\sqrt{C}$, which is the regime of every known particle when $C$ is of order one, $\mathrm{Im}\,w = \sqrt{2}\,|B_{\Lambda}|/H$ at leading order.

## technical
For $\Lambda > 0$ the induced weight of a composite of mass $m$ is a solution $w$ of $-w(w+3)H^{2} = m^{2}$. For a composite of two conformal spinors with mass given by the exact join, $w = -\tfrac32 \pm I_4\nu$ (numbers are read in $\mathrm{span}\{1, I_4\}$) with $\nu^{2} = 6|B_{\Lambda}|^{2}/\Lambda + C - \tfrac94$. The weight is real exactly when $6|B_{\Lambda}|^{2}/\Lambda + C \le \tfrac94$, and otherwise lies on the principal series with $\nu = m/H - \tfrac98 H/m + O((H/m)^{3})$.

Every composite heavier than $3H/2$ has real part $-\tfrac32$ and carries its mass in the imaginary part; when $|B_{\Lambda}| \gg H\sqrt{C}$, the regime of every known particle when $C$ is of order one, $\mathrm{Im}\,w = \sqrt{2}\,|B_{\Lambda}|/H$ at leading order.

## lay
With a positive cosmological constant, each composite particle can be given a weight: the number that would produce its mass under the framework's mass rule. For anything heavier than a tiny threshold set by the expansion of the universe, that weight is complex. Its real part is the same for every such particle, and its imaginary part is essentially the mass measured in cosmological units, an enormous number for every known particle.

## one-liner
For $\Lambda > 0$ the induced weight of a composite of two conformal spinors is $w = -\tfrac32 \pm I_4\nu$ (numbers are read in $\mathrm{span}\{1, I_4\}$) with $\nu^{2} = 6|B_{\Lambda}|^{2}/\Lambda + C - \tfrac94$, so a composite heavier than $3H/2$ carries its mass in $\mathrm{Im}\,w$, which at leading order is $\sqrt{2}\,|B_{\Lambda}|/H$ when $|B_{\Lambda}| \gg H\sqrt{C}$.
