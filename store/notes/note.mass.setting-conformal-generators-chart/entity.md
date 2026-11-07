---
id: note.mass.setting-conformal-generators-chart
kind: note
version: 2
title: The conformal generators in the chart
status: setting
subject: conformal-spacetime
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
- name: Claude Opus 5.5
  role: 'consistency pass, legacy twistor macros written with the conformal spinor macros'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
comments_on:
- mass.chart-form-spin-isomorphism
- mass.imported-flat-model-twistor-chart-infinity
locators:
  paper: T11
  number: Setting
  section: The exact join
  line: 632
  subsection: The conformal generators in the chart
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Notation only: the legacy macros for twistor space and its projective space (and, where used, the two summand planes) are written with the store''s conformal spinor macros CS, PCS (and S_omega, S_pi), as in the results this note comments on; no change of content.'
---

## formal
Write $\CS = \Som \oplus \Spi$ with bases $e_{1}, e_{2}$ of $\Som$ and $e_{3}, e_{4}$ of $\Spi$, so that $n_{\infty} = e_{1}\wedge e_{2}$, $n_{0} = e_{3}\wedge e_{4}$, the $x$-slot is spanned by the mixed bivectors $e_{a}\wedge e_{a'}$ ($a \in \{1,2\}$, $a' \in \{3,4\}$), and $\varepsilon(e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4}) = 1$, which gives $\ip{n_{0}}{n_{\infty}} = +1$. A twistor is $Z = \omega + \pi = \omega^{a}e_{a} + \pi^{a'}e_{a'}$. Let $\varepsilon_{ab}$ and $\varepsilon_{a'b'}$ be the antisymmetric symbols with $\varepsilon_{12} = \varepsilon_{34} = 1$, so that $e_{a}\wedge e_{b} = \varepsilon_{ab}\,n_{\infty}$, $e_{a'}\wedge e_{b'} = \varepsilon_{a'b'}\,n_{0}$, and the brackets are the determinants $\br{\pi^{1}\pi^{2}} := \varepsilon_{a'b'}\pi_{1}^{a'}\pi_{2}^{b'}$ and $[\omega^{1}\omega^{2}] := \varepsilon_{ab}\omega_{1}^{a}\omega_{2}^{b}$. For the ambient vector $U \wedge V$ let $R_{U\wedge V}$ be the rotation $W \mapsto \ip{U}{W}V - \ip{V}{W}U$ of $\Lambda^{2}\CS$, and let $A(U \wedge V) \in \mathfrak{sl}(\CS)$ be its preimage under the isomorphism of Fact \claimref{mass.imported-flat-model-twistor-chart-infinity}. Matrices act on column vectors in the basis $(e_{1}, e_{2}, e_{3}, e_{4})$, in block form according to $\Som \oplus \Spi$.

## technical
pending

## lay
pending

## one-liner
pending
