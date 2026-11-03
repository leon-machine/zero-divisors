---
id: interior.imported-equivalence-einstein-equations
kind: claim
version: 2
title: 'Imported: equivalence with the Einstein equations'
status: imported
region: interior
subject: einstein
tags: [classical-theorem, curvature-and-field-equations]
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
imported_from:
- citation: A. Lasenby, C. Doran and S. Gull, Gravity, gauge theories and geometric algebra, Phil. Trans.
    R. Soc. Lond. A 356 (1998), 487--582.
  key: LDG1998
  locator: \S 4 (\S 4.3, covariant forms of the field equations), App.~C
- citation: C. Doran and A. Lasenby, Geometric Algebra for Physicists, Cambridge University Press (2003).
  key: DoranLasenby2003
  locator: Ch.~13-14
locators:
  paper: T06
  number: Fact 2.1
  label: fact:gtg
  line: 362
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Locator corrected from \S 7 (which is "Electromagnetism in a gravitational background") to \S 4, the field equations and their covariant forms (Sec. 4.3, Covariant forms of the field equations), and Appendix C, the translation of tensor calculus; section titles checked against arXiv:gr-qc/0405033 on 2026-10-23.'
  env: fact
  typing:
    by: ai-typing-pass
    note: 'Imported fact with no derivation; nothing to edge.'
---

## formal
On any region where $\hb$ is invertible, the GTG field equations for $(\hb, \Omega)$ are equivalent to the Einstein field equations for the metric $g(a,b) = \hb^{-1}(a)\cdot\hb^{-1}(b)$; in vacuum, to Ricci-flatness of $g$. \emph{Provenance:} Lasenby, Doran and Gull \cite[\S 4.3 and App.~C]{LDG1998}; textbook form \cite[Ch.~13-14]{DoranLasenby2003}.

## technical
On any region where the gauge field $\hb$ is invertible, the field equations of gauge theory gravity (GTG) for $(\hb, \Omega)$ are equivalent to the Einstein field equations for the metric $g(a,b) = \hb^{-1}(a)\cdot\hb^{-1}(b)$. In vacuum they are equivalent to Ricci-flatness of $g$. This is imported from the gauge-theory-gravity literature.

## lay
Gauge theory gravity rewrites general relativity in the language of geometric algebra. This imported result says that, wherever its basic field can be inverted, its equations say exactly the same as Einstein's equations for the corresponding metric. In empty space this means the metric has vanishing Ricci curvature.

## one-liner
Wherever $\hb$ is invertible, the GTG field equations are equivalent to Einstein's equations for the induced metric, and in vacuum to its Ricci-flatness.
